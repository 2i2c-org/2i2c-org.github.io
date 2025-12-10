#!/usr/bin/env python3
"""
Generate HTML alias/redirect files for blog posts.

Since we use slugs instead of paths for the blog, we need to create
HTML files with meta-refresh redirects for the path-based URL structure.

This helps when we forget to link to a slug, and instead use a path.

This script scans content/blog/YYYY/slug/ directories and creates redirect pages
at public/blog/YYYY/slug/index.html that redirect to /blog/slug/

Run this AFTER `hugo build` to generate the redirect HTML files.
"""

from pathlib import Path

REDIRECT_TEMPLATE = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="utf-8">
    <title>Redirecting...</title>
    <link rel="canonical" href="{new_url}">
    <meta http-equiv="refresh" content="0; url={new_url}">
    <meta name="robots" content="noindex">
</head>
<body>
    <p>This page has moved to <a href="{new_url}">{new_url}</a>.</p>
    <script>window.location.href="{new_url}";</script>
</body>
</html>
"""

def get_blog_posts_from_content():
    """Find all blog post directories in content/blog/YYYY/."""
    blog_dir = Path("content/blog")
    posts = []

    for year_dir in sorted(blog_dir.glob("202[0-9]")):
        if year_dir.is_dir():
            for post_dir in sorted(year_dir.iterdir()):
                if post_dir.is_dir() and (post_dir / "index.md").exists():
                    year = year_dir.name
                    slug = post_dir.name
                    posts.append((year, slug))

    return posts

def create_redirect_file(year, slug, base_url="https://2i2c.org"):
    """Create an HTML redirect file for a year-based URL."""
    # Old URL: /blog/YYYY/slug/
    # New URL: /blog/slug/
    old_path = Path(f"public/blog/{year}/{slug}")
    new_url = f"{base_url}/blog/{slug}/"

    # Create directory
    old_path.mkdir(parents=True, exist_ok=True)

    # Create redirect HTML file
    redirect_html = REDIRECT_TEMPLATE.format(new_url=new_url)
    (old_path / "index.html").write_text(redirect_html)

    return old_path

def main():
    print("Generating blog post redirects for GitHub Pages...")

    # Make sure public/ directory exists
    if not Path("public").exists():
        print("❌ public/ directory not found. Run 'hugo' first to build the site.")
        return 1

    posts = get_blog_posts_from_content()

    created = 0
    for year, slug in posts:
        redirect_path = create_redirect_file(year, slug)
        created += 1

    print(f"✨ Created {created} redirect files in public/")
    return 0

if __name__ == "__main__":
    exit(main())
