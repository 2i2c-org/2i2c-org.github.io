---
title: NASA VEDA & 2i2c Update for Q4 2024 (Oct-Dec 2024)
subtitle: ""
summary: ""
authors:
  - Yuvi Panda
tags:
  - geoscience
categories:
  - impact
date: 2025-01-07T15:18:37-08:00
lastmod: 2025-01-07T15:18:37-08:00
featured: false
draft: false
projects:
  - nasa-veda
---

A non-exhaustive list of things 2i2c and [Development Seed](https://developmentseed.org/) did with the [NASA VEDA](https://www.earthdata.nasa.gov/data/tools/veda) project last quarter!

## Automated backups and alerting with `jupyterhub-home-nfs`

[Tracking Issue](https://github.com/NASA-IMPACT/veda-jupyterhub/issues/56)

[jupyterhub-home-nfs](https://github.com/2i2c-org/jupyterhub-home-nfs/) is a young project to provide flexible per-user home directory limits on JupyterHub - an important feature for controlling cloud costs. [Tarashish Mishra](https://sunu.in/) and [Sarah Gibson](https://sgibson91.github.io/cv/) have been leading this project for the last few months. Since we are moving away from [AWS Managed EFS](https://aws.amazon.com/efs/) here, we had to do some work to recreate some of the benefits EFS gives us out of the box. During this quarter, we:

1. Set up automated backups so we can recover files in cases of disaster
2. Set up automated alerting (via prometheus and pagerduty) to know if our backing EBS device is getting full and we need to perform a manual intervention
3. Deployed this to a few other communities ([CryoCloud](https://www.cryocloud.io/) and [NMFS Openscapes](https://nmfs-openscapes.github.io/)) to broaden adoption.

We will continue doing work on `jupyterhub-home-nfs` in the upcoming quarter! If this is functionality you are interested in deploying, please reach out to us to collaborate!

## Enable users to dynamically build environments with `jupyterhub-fancy-profiles`

[Tracking Issue](https://github.com/NASA-IMPACT/veda-jupyterhub/issues/58)

We covered this more extensively in [another blog post](https://2i2c.org/blog/2024/jupyterhub-fancy-profiles-rollout/), so go read that!

This work in particular is a good demonstrator of 2i2c's value - it started off with a [grant from GESIS](https://2i2c.org/blog/2024/jupyterhub-binderhub-gesis/), and now with support from [NASA IMPACT](https://impact.earthdata.nasa.gov/) we are able to bring it to a *lot* of communities, not just the ones that funded it.

Ongoing work here will focus on improving the UX as well as better documentation so users can actually use it!

## "Open in QGIS" from VEDA UI

[Tracking Issue](https://github.com/NASA-IMPACT/veda-jupyterhub/issues/59)

We had worked in the past with many communities in enabling [QGIS on the Cloud](https://2i2c.org/blog/2023/qgis-greenland/), and this quarter we got closer to enabling a contextual 'Open in QGIS' button in the [VEDA Dashboard](https://www.earthdata.nasa.gov/dashboard/)! Here is a quick demo:

<video src="./open-in-qgis.mp4" muted controls></video>

(This shows the workflow when user is already logged into the JupyterHub and had started the server)

You can play with this in [this preview](https://deploy-preview-688--ghg-demo.netlify.app/exploration), although you need to have access to the NASA VEDA hub to fully try it out at this point.

Tarashish from Development Seed is again responsible for most of the work here, available in [jupyter-remote-qgis-proxy](https://github.com/sunu/jupyter-remote-qgis-proxy). You can use it to create 'magic links' that will open QGIS in a desktop environment in your browser, and add a specific layer to it! Our hope is that this allows primarily GIS folks to better use tools they already are familiar with in cloud based contexts.

## Other updates

- We participated heavily in an evaluation process for the authentication and authorization solution to be used across NASA VEDA! [Tracking Issue](https://github.com/NASA-IMPACT/veda-jupyterhub/issues/57)
- We are very close to [rolling out JupyterHub 5.0](https://github.com/2i2c-org/infrastructure/issues/5209) and associated changes across all our hubs, which will enable us to eventually offer per-group shared directories! [Tracking Issue](https://github.com/NASA-IMPACT/veda-jupyterhub/issues/61)