---
title: "2i2c supports Jupyter Docker Stacks ARM builds"
date: "2023-12-01"
authors: ["Chris Holdgraf", "Yuvi Panda"]
tags: [open source]
categories: [impact]
featured: false
draft: false
---

The [Jupyter Docker Stacks](https://jupyter-docker-stacks.readthedocs.io/) project provides a collection of ready-to-use Docker images for Jupyter environments. These images are used by many in the Jupyter community, including 2i2c which uses them as base images for our JupyterHub deployments.

The project recently began publishing [ARM-compatible images](https://github.com/jupyter/docker-stacks/issues/1019) alongside the standard x86 images, making it easier for users with ARM-based systems (like M1 Macs) to use these environments. However, building and hosting these ARM images comes with additional cloud computing costs that were being personally covered by [@mathbunnyru](https://github.com/mathbunnyru), one of the project's maintainers.

A part of 2i2c's mission is supporting upstream communities that we rely on, especially where the upstream project has limited resources. For this reason, we've decided to support Jupyter Docker Stack's ARM building costs, with a total budget of `$2000` (approximately `$150` per month). As a regular user and beneficiary of the Jupyter Docker Stacks, we believe it's important to contribute to the maintenance and sustainability of this crucial piece of infrastructure that benefits the entire Jupyter community.

We hope this support helps the Docker Stacks project remain healthy, and continue providing high-quality, multi-architecture images that work across different computing platforms. We'll revisit this decision as the landscape of technology providers changes and other options arise.
