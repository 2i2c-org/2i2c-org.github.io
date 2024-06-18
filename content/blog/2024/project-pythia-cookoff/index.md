---
title: Hacking the Project Pythia Cook-off with MyST Markdown 
date: "2024-06-18"
lastmod: "2024-06-21"
authors: ["Jenny Wong", "James Munroe", "Angus Hollands"]
tags: [community]
categories: [updates]
featured: false
draft: true
---

![Group selfie of Project Pythia Cook-off participants.](./cover.png)

## What is Project Pythia?

[Project Pythia](https://projectpythia.org/) is the education working group for [Pangeo](https://pangeo.io/index.html), a community platform for Big Data geoscience in which 2i2c operates a cloud hub. The core aim of Project Pythia is to spearhead the creation and curation of community-driven, open-source documentation, in the form of "cookbooks", to enable the adoption of *open*, *scalable* and *reproducible* workflows for geoscientists.

## What did 2i2c do?

Jenny, James and Angus from the 2i2c team participated in the annual [Project Pythia Cook-off 2024](https://projectpythia.org/pythia-cookoff-2024/), a hackathon where cookbook authors and collaborators can spend dedicated time on creating and maintaining their content using [Jupyter Book](https://jupyterbook.org/en/stable/intro.html) (see the latest blog post on [Jupyter Book 2.0 will use MyST](../myst-jupyter-book/index)) and publishing their cookbooks with GitHub actions.

Prior to the hackathon, 2i2c deployed a JupyterHub with a *binderhub-service* that allowed participants to "self-serve" containers for their software environment, which were specified by including a list of packages in an `environment.yml` file placed in their Git repository.

<!-- TBC: number of participants, how many used the JupyterHub, cost $$$ to run the service -->

2i2c teamed up with the infrastructure breakout group during the hackathon, led by Katelyn FitzGerald (UCAR) and Kevin Tyle (University at Albany), and members of the [Curvenote](https://curvenote.com/) team also joined the group.

## Day 1

We quickly identified a number of issues that were proving to be a maintenance headache for Project Pythia:

- [ ] Configuration files for each cookbook were difficult to update at scale. Project Pythia currently have a collection of over 30 cookbooks!
- [ ] Changes to Sphinx-based themes inherited from upstream were prone to breaking custom Project Pythia branding.
