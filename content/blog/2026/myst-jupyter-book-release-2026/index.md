---
title: "New Jupyter Book / MyST stack release (Jan 2026)"
slug: "jupyter-book-release-jan-2026"
date: 2026-01-29
authors:
  - Chris Holdgraf
categories:
  - upstream-impact
tags:
  - update
  - open-source
  - myst
  - jupyterbook
---

The MyST/Jupyter Book stack shipped new releases this week. Release pages:

- [mystmd 1.8.0](https://github.com/jupyter-book/mystmd/releases/tag/mystmd%401.8.0)
- [myst-theme 1.1.0](https://github.com/jupyter-book/myst-theme/releases/tag/myst-to-react%401.1.0)
- [Jupyter Book 2.1.1](https://github.com/jupyter-book/jupyter-book/releases/tag/v2.1.1)

## Where we contributed

We've spent extra time lately trying to fix bugs and generally improve stability, reliability, and UX papercuts.
Here are some of the things we focused on:

- Extra review time to get in [concurrent executions in mystmd](https://github.com/jupyter-book/mystmd/pull/2428)
- Fixing broken edit URL logic so our community ["edit buttons" worked again](https://github.com/jupyter-book/mystmd/pull/2642)
- [Standardized link styles](https://github.com/jupyter-book/myst-theme/pull/757) so users know what to expect from links
- [Added extra hover metadata for github issues and PRs](https://github.com/jupyter-book/myst-theme/pull/747) for communities that often link to their GitHub issues
- Made all of these releases and wrote up the release notes!

Most of our contributions were foundational in nature - we fixed a bunch of bugs, did review on the PRs of others, and managed the release process itself.  Check out the changelogs for more details!

## Acknowledgements

Thanks to our [member communities](../../../members/) - their memberships cover the cost of [foundational upstream contributions](../../2025/foundational-contributions/) to projects like these.

Particular thanks to [Project Pythia](../../../collaborators/pythia/) which currently supports much of our upstream contributions in Jupyter Book.
