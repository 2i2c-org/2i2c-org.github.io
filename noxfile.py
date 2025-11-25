"""Nox sessions for building and serving the Hugo documentation site."""

import platform
import tarfile
import urllib.request
from pathlib import Path

import nox

# Hugo version to download from GitHub releases
HUGO_VERSION = "0.125.3"
# Lychee version to download from GitHub releases
LYCHEE_VERSION = "0.21.0"

nox.options.default_venv_backend = "uv"
nox.options.reuse_existing_virtualenvs = True


@nox.session(name="docs")
def docs(session):
    """Build the Hugo documentation site.

    Downloads Hugo Extended v{HUGO_VERSION} from GitHub releases if not cached.
    """
    hugo_path = install_hugo(session)

    # Build the site
    session.run(hugo_path, "--cleanDestinationDir", external=True)

@nox.session(name="linkcheck")
def linkcheck(session):
    """Build the site and run lychee link checker against the built output."""
    hugo_path = install_hugo(session)
    lychee_path = install_lychee(session)

    # Build the site
    session.run(hugo_path, "--cleanDestinationDir", external=True)

    # Run link checker offline against the generated site
    session.run(
        lychee_path,
        "--offline",
        "--accept",
        "200,301,302",
        "--max-concurrency",
        "50",
        "public",
        external=True,
    )

@nox.session(name="docs-live")
def docs_live(session):
    """Build and serve the Hugo documentation site with live reload.

    Downloads Hugo Extended v{HUGO_VERSION} from GitHub releases if not cached.
    The site will be available at http://localhost:1313
    """
    hugo_path = install_hugo(session)

    # Serve the site with live reload
    session.run(hugo_path, "server", external=True)


def get_hugo_download_url(version):
    """Get the download URL for Hugo based on the current platform."""
    system = platform.system().lower()
    machine = platform.machine().lower()

    if system == "darwin":
        # macOS uses universal binary
        filename = f"hugo_extended_{version}_darwin-universal.tar.gz"
    elif system == "linux":
        if machine in ("x86_64", "amd64"):
            filename = f"hugo_extended_{version}_linux-amd64.tar.gz"
        elif machine in ("arm64", "aarch64"):
            filename = f"hugo_extended_{version}_linux-arm64.tar.gz"
        else:
            raise RuntimeError(f"Unsupported Linux architecture: {machine}")
    elif system == "windows":
        if machine in ("x86_64", "amd64"):
            filename = f"hugo_extended_{version}_windows-amd64.zip"
        else:
            raise RuntimeError(f"Unsupported Windows architecture: {machine}")
    else:
        raise RuntimeError(f"Unsupported operating system: {system}")

    base_url = "https://github.com/gohugoio/hugo/releases/download"
    return f"{base_url}/v{version}/{filename}"


def install_hugo(session):
    """Download and install Hugo if not already present in the session."""
    # Create a bin directory in the session's virtualenv
    bin_dir = Path(session.virtualenv.location) / "bin"
    bin_dir.mkdir(exist_ok=True)
    hugo_path = bin_dir / "hugo"

    # Check if Hugo is already installed in this session
    if hugo_path.exists():
        session.log(f"Hugo already installed at {hugo_path}")
        # Verify it's the correct version
        result = session.run(
            str(hugo_path), "version", silent=True, external=True
        )
        if HUGO_VERSION in result:
            session.log(f"Using cached Hugo {HUGO_VERSION}")
            return str(hugo_path)
        else:
            session.log("Cached Hugo version mismatch, re-downloading...")
            hugo_path.unlink()

    # Download Hugo
    download_url = get_hugo_download_url(HUGO_VERSION)
    session.log(f"Downloading Hugo {HUGO_VERSION} from {download_url}")

    download_path = bin_dir / "hugo.tar.gz"
    urllib.request.urlretrieve(download_url, download_path)

    # Extract Hugo binary
    session.log("Extracting Hugo binary...")
    with tarfile.open(download_path, "r:gz") as tar:
        # Extract only the hugo binary
        for member in tar.getmembers():
            if member.name == "hugo":
                member.name = "hugo"
                tar.extract(member, path=bin_dir)
                break

    # Make executable
    hugo_path.chmod(0o755)

    # Clean up downloaded archive
    download_path.unlink()

    session.log(f"Hugo {HUGO_VERSION} installed successfully at {hugo_path}")
    return str(hugo_path)


def get_lychee_download_url(version):
    """Get the download URL for Lychee based on the current platform."""
    system = platform.system().lower()
    machine = platform.machine().lower()

    if system == "darwin":
        arch = "arm64-macos" if machine in ("arm64", "aarch64") else "x86_64-macos"
        filename = f"lychee-{arch}.tar.gz"
    elif system == "linux":
        if machine in ("x86_64", "amd64"):
            filename = f"lychee-{version}-x86_64-unknown-linux-gnu.tar.gz"
        elif machine in ("arm64", "aarch64"):
            filename = f"lychee-{version}-aarch64-unknown-linux-gnu.tar.gz"
        else:
            raise RuntimeError(f"Unsupported Linux architecture: {machine}")
    else:
        raise RuntimeError(f"Unsupported operating system: {system}")

    base_url = "https://github.com/lycheeverse/lychee/releases/download"
    tag = f"lychee-v{version}"
    return f"{base_url}/{tag}/{filename}"


def install_lychee(session):
    """Download and install Lychee if not already present in the session."""
    bin_dir = Path(session.virtualenv.location) / "bin"
    bin_dir.mkdir(exist_ok=True)
    lychee_path = bin_dir / "lychee"

    if lychee_path.exists():
        session.log(f"Lychee already installed at {lychee_path}")
        return str(lychee_path)

    download_url = get_lychee_download_url(LYCHEE_VERSION)
    session.log(f"Downloading Lychee {LYCHEE_VERSION} from {download_url}")

    download_path = bin_dir / "lychee.tar.gz"
    urllib.request.urlretrieve(download_url, download_path)

    session.log("Extracting Lychee binary...")
    with tarfile.open(download_path, "r:gz") as tar:
        for member in tar.getmembers():
            if member.name.endswith("/lychee"):
                member.name = "lychee"
                tar.extract(member, path=bin_dir)
                break
            if member.name == "lychee":
                tar.extract(member, path=bin_dir)
                break

    lychee_path.chmod(0o755)
    download_path.unlink()

    session.log(f"Lychee {LYCHEE_VERSION} installed successfully at {lychee_path}")
    return str(lychee_path)
