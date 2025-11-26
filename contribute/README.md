# Contributing guide

This section contains information for *developers* to contribute to the site.

## Pre-commit hooks

We use [`pre-commit`](https://pre-commit.com/) to keep the repo consistent:

- Install once: `pip install pre-commit` and run `pre-commit install`.
- Run all hooks before you open a PR: `pre-commit run --all-files`.
- Hooks currently include PNG optimization and a helper that ensures every blog post front matter has a `slug` (needed for permalinks). The slug hook writes changes to your files; review and keep them.
