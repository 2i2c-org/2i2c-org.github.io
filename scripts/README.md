# Build Scripts

This directory contains scripts used during the website build process.

## generate-blog-aliases.py

Generates HTML redirect pages for blog posts to maintain old year-based URLs.

**Purpose:** Since GitHub Pages doesn't support server-side redirects (like Netlify's `_redirects` file), we need client-side HTML redirects using meta refresh tags.

**What it does:**
- Scans `content/blog/YYYY/slug/` directories
- Creates HTML redirect files at `public/blog/YYYY/slug/index.html`
- Each redirect page uses meta refresh + JavaScript to redirect to `/blog/slug/`

**When to run:** After `hugo build` and before deploying to GitHub Pages.

**Usage:**
```bash
hugo build
python scripts/generate-blog-aliases.py
```

## extract_org_logos.py

Extracts organization logos for the collaborators page.

**When to run:** Before building the site.

**Usage:**
```bash
python scripts/extract_org_logos.py
```

**Automatic execution:** This script runs automatically in `.github/workflows/deploy.yml` before the Hugo build step.
