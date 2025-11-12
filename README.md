# 2i2c brochure

This is a brochure website for the International Interactive Computing Collaboration (2i2c).
It is built from the [academic hugo theme](https://github.com/HugoBlox).

## Where the website is hosted

This website is **hosted** by GitHub Pages, and we use Netlify to display previews of the website from PRs.

## How to edit, build, and preview this website

### Using nox (recommended)

This project includes nox automation for building and previewing the website:

First [install nox](https://nox.thea.codes/en/stable/tutorial.html#installation).
Then:

```bash
# Build the website
nox -s docs

# Build and serve with live reload at http://localhost:1313
nox -s docs-live
```

The nox sessions will automatically download Hugo Extended v0.125.3 from GitHub releases on first run and cache it for subsequent runs. To force a clean rebuild, use `nox -s docs --no-reuse-existing-virtualenvs`.

### Manual Hugo usage

See [the Team Compass blog documentation](https://compass.2i2c.org/communication/blog/) for more information.

## Blogging

See `contribute/blog.md`.

## Website-specific features

See `contribute/features.md`.

## Job postings

See `contribute/jobs.md`.

## This website's theme

We are using the latest version of the [Hugo Blox theme](https://hugoblox.com/docs/) (used to be the "Wowchemy Academic Theme"). See its documentation for information about customization and usage.
