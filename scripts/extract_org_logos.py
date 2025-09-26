#!/usr/bin/env python3
"""
Extract organization info from 2i2c infrastructure and download logos.
"""

import yaml
import requests
import tempfile
import subprocess
import shutil
from pathlib import Path
from urllib.parse import urlparse
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def clone_repo():
    """Clone infrastructure repo using git."""
    temp_dir = Path(tempfile.mkdtemp())
    repo_path = temp_dir / "infrastructure"
    
    try:
        subprocess.run(["git", "clone", "https://github.com/2i2c-org/infrastructure.git", str(repo_path)], 
                      capture_output=True, check=True)
        logger.info(f"Cloned repo to {repo_path}")
        return repo_path
    except (subprocess.CalledProcessError, FileNotFoundError) as e:
        logger.error(f"Failed to clone repo: {e}")
        exit(1)

def load_yaml_file(filepath):
    """Load YAML file."""
    try:
        with open(filepath, 'r') as f:
            return yaml.safe_load(f)
    except Exception:
        return None

def extract_org_from_values(values_config, hub_domain):
    """Extract org info from values file."""
    try:
        org = values_config.get('jupyterhub', {}).get('custom', {}).get('homepage', {}).get('templateVars', {}).get('org', {})
        if org and org.get('name'):
            name = org['name']
            # Skip entries with 2i2c or staging in the name
            if '2i2c' in name.lower() or 'staging' in name.lower():
                return None
            return {
                'name': name,
                'url': f'https://{hub_domain}' if hub_domain else org.get('url'),
                'logo_url': org.get('logo_url')
            }
    except Exception:
        pass
    return None

def process_clusters(clusters_dir):
    """Process all clusters and extract org info."""
    orgs = []

    for cluster_dir in clusters_dir.iterdir():
        if not cluster_dir.is_dir():
            continue

        cluster_file = cluster_dir / "cluster.yaml"
        cluster_config = load_yaml_file(cluster_file)

        if not cluster_config:
            continue

        for hub in cluster_config.get('hubs', []):
            hub_domain = hub.get('domain')
            for values_file in hub.get('helm_chart_values_files', []):
                if values_file.endswith('.values.yaml'):
                    values_path = cluster_dir / values_file
                    values_config = load_yaml_file(values_path)

                    if values_config:
                        org_info = extract_org_from_values(values_config, hub_domain)
                        if org_info:
                            orgs.append(org_info)
    
    # Deduplicate by name
    seen = set()
    unique_orgs = []
    for org in orgs:
        key = org['name'].lower()
        if key not in seen:
            seen.add(key)
            unique_orgs.append(org)
    
    logger.info(f"Found {len(unique_orgs)} unique organizations")
    return unique_orgs

def download_logo(org, images_dir, session):
    """Download a logo."""
    logo_url = org.get('logo_url')
    if not logo_url:
        return False, None
    
    # Create filename
    safe_name = "".join(c for c in org['name'] if c.isalnum() or c in (' ', '-', '_')).strip()
    safe_name = safe_name.replace(' ', '_').lower()
    
    # Get file extension
    ext = 'png'
    try:
        parsed = urlparse(logo_url)
        if '.' in parsed.path:
            ext = parsed.path.split('.')[-1].lower()
    except Exception:
        pass
    
    filepath = images_dir / f"{safe_name}.{ext}"
    
    # Skip if exists
    if filepath.exists():
        logger.info(f"Skipping {org['name']} (exists)")
        return True, None
    
    # Download
    try:
        response = session.get(logo_url, stream=True, timeout=10)
        response.raise_for_status()
        
        with open(filepath, 'wb') as f:
            for chunk in response.iter_content(chunk_size=8192):
                f.write(chunk)
        
        logger.info(f"Downloaded {org['name']}")
        return True, None
    except Exception as e:
        return False, f"Failed to download {org['name']}: {e}"

def main():
    # Hard-coded paths
    images_dir = Path("content/members/images")
    images_dir.mkdir(parents=True, exist_ok=True)
    
    # Clone repo
    repo_path = clone_repo()
    clusters_dir = repo_path / "config" / "clusters"
    
    try:
        # Extract orgs
        orgs = process_clusters(clusters_dir)
        
        if not orgs:
            logger.error("No organizations found!")
            return
        
        # Print summary
        print(f"\nFound {len(orgs)} organizations:")
        for org in sorted(orgs, key=lambda x: x['name'].lower()):
            print(f"  {org['name']}")
        
        # Download logos
        session = requests.Session()
        session.headers.update({
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
        })
        success_count = 0
        errors = []
        
        for org in orgs:
            if org.get('logo_url'):
                success, error = download_logo(org, images_dir, session)
                if success:
                    success_count += 1
                elif error:
                    errors.append(error)
        
        logger.info(f"Downloaded {success_count} logos")
        
        # Print errors at the end
        if errors:
            print("\nDownload errors:")
            for error in errors:
                print(f"  {error}")
        
        # Save data file
        data_file = Path("data/org_summary.yaml")
        data_file.parent.mkdir(exist_ok=True)
        
        with open(data_file, 'w') as f:
            yaml.dump(sorted(orgs, key=lambda x: x['name'].lower()), f, default_flow_style=False)
        
        logger.info(f"Saved data to {data_file}")
        
    finally:
        # Cleanup
        shutil.rmtree(repo_path.parent)

if __name__ == "__main__":
    main()