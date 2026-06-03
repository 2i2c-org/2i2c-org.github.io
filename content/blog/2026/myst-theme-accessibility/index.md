---
title: "Accessibility improvements in Jupyter Book"
slug: "myst-theme-accessibility"
date: 2026-5-22
authors:
  - Chris Holdgraf
categories:
  - upstream-impact
tags:
  - update
  - open source
  - jupyterbook
  - myst
  - accessibility
---

We helped shepherd and implement a batch of accessibility improvements in `myst-theme` as part of the [Jupyter Book](../../../collaborators/jupyter-book/) project.
The Jupyter Book team blogged about it here:

https://jupyterbook.org/blog/posts/2026/accessibility-improvements

Accessibility is a key part of making technology broadly impactful and useful, and it's increasingly a requirement for the institutions we serve.
The work started from an audit by Silas at [BIDS](../../../collaborators/bids/), who surfaced and iterated on the issues with the rest of the Jupyter Book team.

A few of the fixes that landed:

- Improved keyboard focus for horizontally scrollable content
- Better ARIA semantics for screen readers
- Better color contrast in ANSI outputs
- Better re-flow / re-size for dynamic screen widths

The team also published accessibility statements you can point your own institutions to:

- [Jupyter Book accessibility statement](https://jupyterbook.org/accessibility)
- [MyST accessibility and performance guide](https://mystmd.org/guide/accessibility-and-performance)

## Acknowledgements

- Thanks to Silas ([@pancakereport](https://github.com/pancakereport)) at [BIDS](../../../collaborators/bids/) for surfacing these issues and iterating on them!
