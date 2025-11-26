---
title: Refactoring Jupyter Book 2 documentation ahead of a major release
slug: "jupyter-book-docs-refactor"
date: 2025-11-01
authors:
  - Chris Holdgraf
categories:
  - upstream-impact
tags:
  - update
  - open-source
  - jupyterbook
  - learning
  - community
---

Documentation is what turns open source code into products that people actually want to use. We recently spent a few days refactoring the [Jupyter Book](../../../collaborators/jupyter-book/) documentation to prepare for the upcoming Jupyter Book 2 release, and we're excited about how much clearer the docs have become!

## What we did

We restructured the docs using the [Diataxis framework](https://diataxis.fr/) to better organize content by user type and task:

- Reorganized into clear topic areas with landing pages for easier navigation
- Added missing content like the feature voting table and contributing guides
- Created upgrade guidance to help users understand the relationship between Jupyter Book 2 and MyST

This work helps users find what they need faster and gives the project a stronger foundation to build on going forward.

## Why we're excited about it

Better documentation reduces maintainer burden by helping users answer their own questions, and it makes the project more welcoming and useful to new contributors. We hope this makes Jupyter Book more accessible to everyone and lays a good foundation for the new release!

We're also excited because so many others helped provide edits and comments!

## Learn more

- [PR implementing the refactor](https://github.com/jupyter-book/jupyter-book/pull/2422)
- [Documentation principles we developed](https://github.com/jupyter-book/jupyter-book/blob/next/docs/contribute/docs.md)
- [Jupyter Book 2 documentation](https://next.jupyterbook.org)

## Acknowledgements

- Thanks to [@rlanzafame](https://github.com/rlanzafame), [@FreekPols](https://github.com/FreekPols), and [@bsipocz](https://github.com/bsipocz) for their helpful reviews, edits, and feedback on the PR!
- [Project Pythia](../../../collaborators/pythia/), [CryoCloud](../../../collaborators/cryocloud/), and the Berkeley educational projects are our primary member communities using MyST and [Jupyter Book](../../../collaborators/jupyter-book/). Their support covers the cost of these kinds of foundational contributions.
