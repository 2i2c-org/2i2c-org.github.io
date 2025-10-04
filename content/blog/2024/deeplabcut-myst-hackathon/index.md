---
title: MyST Mini-Hackathon with the DeepLabCut Team
date: 2024-09-02
authors:
  - Jenny Wong
  - Angus Hollands
  - Chris Holdgraf
tags:
  - bioscience
  - open-source
categories:
  - impact
featured: false
draft: false
---

## The DeepLabCut Team

![Animal pose estimation using deep neural networks. Courtesy of the DeepLabCut Jupyter Book](https://images.squarespace-cdn.com/content/v1/57f6d51c9f74566f55ecf271/daed7f16-527f-4150-8bdd-cbb20e267451/cheetah-ezgif.com-video-to-gif-converter.gif?format=180w "Animal pose estimation using deep neural networks. Courtesy of the [DeepLabCut Jupyter Book](https://deeplabcut.github.io/DeepLabCut/README.html)")

The [DeepLabCut team](http://www.mackenziemathislab.org/deeplabcut) is a group of researchers and developers who are working on open source tools for analyzing animal pose estimation by training deep neural networks on videos.

Chris Holdgraf visited the lab in early August to learn more about how the group were using open-source tools to document and share their work.

## Jupyter Book and MyST

Extensive documentation for using the DeepLabCut software package is already available as a [Jupyter Book](https://deeplabcut.github.io/DeepLabCut/README.html). The group was interested in adopting MyST Markdown to stay ahead of the curve and upgrade their Jupyter Book (see the related announcement [Jupyter Book 2 will be build upon the MyST-MD engine](https://executablebooks.org/en/latest/blog/2024-05-20-jupyter-book-myst/)).

Chris led a mini-hackathon to introduce the group to MyST and collect feedback on where enhancement features could be made in the future. Here's a summary of the outcomes:

- Many improvements were made to the [MyST documentation](https://mystmd.org/guide/) 📖
  - The [MyST Quick Start Guide](https://mystmd.org/guide/quickstart) was used to onboard new users. Amendments were [upstreamed to the MyST docs directly](https://github.com/jupyter-book/mystmd/pull/1433) and were immediately available to all.
  - A [tutorial on executable documents](https://mystmd.org/guide/quickstart-executable-documents) was added to the collection of MyST tutorials.
  - MyST-MD installation instructions were [simplified using `mamba`](https://github.com/jupyter-book/mystmd/pull/1454).
- A bunch of enhancement features were requested ✨
  - [Using cell tags for labelling notebook cells](https://github.com/jupyter-book/mystmd/issues/1455)
  - [Support for loading user-defined CSS stylesheets for theming](https://github.com/jupyter-book/myst-theme/issues/321)
  - [Better UX for multi-versioned documentation](https://github.com/jupyter-book/mystmd/issues/1458)
  - [Bibliography styling in HTML](https://github.com/jupyter-book/mystmd/issues/1462)
  - [Automatic API documentation generation](https://github.com/DeepLabCut/DeepLabCut/pull/2712)
- And we found a bug in the [table of contents validation](https://github.com/jupyter-book/mystmd/issues/1456) 🐞

## Summary

Hackathons are a great way for quickly imparting knowledge and gathering feedback in a short space of time. The event spurred rapid contributions to the MyST ecosystem – embracing reuse of the MyST quick start guides saved time and effort, while engaging with users directly closed a tight feedback loop for enhancements.

## Acknowledgments

- Thank to the [Mackenzie Mathis Lab](http://www.mackenziemathislab.org/) for hosting Chris Holdgraf at EPFL, Lausanne, Switzerland.
- Thanks to the [Jupyter Book team](../../../collaborators/jupyter-book/) for collaborating on this with us.