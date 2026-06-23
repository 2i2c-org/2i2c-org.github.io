---
title: "Rebuilding Project Pythia's gallery on reusable MyST tooling"
slug: "pythia-cookoff-myst-tooling"
date: 2026-06-23
authors:
  - Chris Holdgraf
categories:
  - upstream-impact
tags:
  - update
  - open source
  - myst
  - jupyterbook
  - binder
---

At the [2026 Pythia Cookoff](https://projectpythia.org/pythia-cookoff-2026/) at NCAR, we spent some hackathon time rebuilding the [Project Pythia](../../../collaborators/pythia/) Cookbook Gallery and blog on shared [MyST Engine](https://mystmd.org) tooling, replacing the one-off custom scripts Pythia had been using before.

{{< figure src="featured.png" title="The redesigned Pythia Cookbook Gallery, now with a search bar and consistent cards.">}}

The gallery and blog now run on the same new [`myst-listing` plugin](https://contrib.mystmd.org/myst-listing), which we created in the new [`myst-contrib`](https://github.com/myst-contrib) organization. It defines an experimental **collect -> transform -> display** pipeline for turning sources of content into galleries, blogs, or other listings. Two very different pages running on one plugin is a good sign it can generalize!

We also pushed on [`clinder`](https://2i2c-org.github.io/clinder/), a BinderHub CLI and GitHub Action that allows you to execute a Jupyter Book's notebooks on [mybinder.org](https://mybinder.org) in CI instead of on the Actions machine. This is a nice fit for cookbook-style content that requires additional computational resources to run. It now has docs, preview deploys, and tests on PRs.

## Learn more

- [Chris's write-up on the Pythia blog](https://projectpythia.org/posts/2026/gallery-listing)
- [`myst-listing` plugin docs](https://contrib.mystmd.org/myst-listing)
- [`clinder` documentation](https://2i2c-org.github.io/clinder/)

## Acknowledgements

Thanks to [Project Pythia](../../../collaborators/pythia/) for hosting the Cookoff, and to our [member communities](../../../members/) whose memberships cover [foundational upstream contributions](../../2025/foundational-contributions/) like these.
