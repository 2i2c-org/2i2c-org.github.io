---
title: Upgrading community infrastructure to Kubernetes 1.34 and JupyterHub 4.3.3
slug: "infra-upgrades-k8s-jupyterhub"
date: 2026-04-08
authors:
  - Georgiana Dolocan
categories:
  - service enhancements
tags:
  - devops
  - reliability
  - jupyterhub
  - open source
---

We've completed a major round of infrastructure upgrades across all 2i2c-managed hubs - every hub is now running [Kubernetes 1.34](https://kubernetes.io/releases/) and [Z2JH helm chart 4.3.3](https://z2jh.jupyter.org/en/stable/changelog.html).

Running up-to-date versions of both Kubernetes and the [JupyterHub](/collaborators/jupyterhub) helm chart ensures that our communities get the best support and reliability, both in terms of features and security.

## A new approach to infrastructure upgrades: upgrading in rounds

This was the first time we rolled out JupyterHub helm chart upgrades **in rounds** rather than all at once. By upgrading a subset of hubs at a time, we could identify and fix issues in isolation before they affected the broader network. This made the process safer and more predictable.

We're planning to perform these kinds of upgrades on a regular schedule for our member communities. Around **every 6 months** we'll create an issue to make sure nothing falls through the cracks (here's [example config for creating our reminder issues](https://github.com/2i2c-org/infrastructure/blob/main/.github/workflows/recurrent-k8s-gcp-upgrades.yaml)).

Check out our [process docs for multi-hub upgrades](https://compass.2i2c.org/services/interactive-computing/multiple-hub-upgrades/#making-changes-to-multiple-hubs) for more information.

## Learn more

Check out these pages for what kinds of improvements we've brought into our clusters / hubs with these latest updates.

- [Z2JH Helm Chart Changelog](https://z2jh.jupyter.org/en/stable/changelog.html)
- [Kubernetes 1.34 Changelog](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.34.md)

## Acknowledgements

- Thanks to [Georgiana Dolocan](/authors/georgiana-dolocan) for leading this upgrade effort and establishing the rounds-based approach.
- Thanks to [Chris Holdgraf](/authors/chris-holdgraf) for adapting and editing Georgiana's notes into a blog post.
