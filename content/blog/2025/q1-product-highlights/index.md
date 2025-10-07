---
title: Our product highlights from Q2 2025
authors:
  - Chris Holdgraf
  - Giuliano Maccioci
categories:
  - organization
date: 2025-04-16
tags:
  - update
---

_These describe the major service improvements that we rolled out in Q1 2025. See this [blog post describing our product enhancement goals in Q1 2025](../q1-product-goals/index.md) for the targets we intended to hit this quarter. Below is a brief description of what we accomplished._

## User storage quotas

A key part of 2i2c’s service is **making the cloud safe to try**. One of the biggest concerns from our communities is that their cloud costs will be unexpectedly high. This quarter we decided to make cloud storage a bit safer. Storage can get expensive, especially when a user accidentally downloads a particularly large file - they may not even realize that doing so incurs an extra cost. For this reason, we added the ability to limit user storage on JupyterHubs:

[Enforcing per-user storage quotas with `jupyterhub-home-nfs`](https://2i2c.org/blog/2025/per-user-storage-quota/)

We initially deployed this feature on our AWS hubs, and followed up by deploying it on GCP hubs as well. Any community with a hub on AWS and GCP now has the ability to limit the storage that their users receive, greatly increasing our communities’ control over their costs.  
   
[Enforcing per-user storage quotas now available on GCP](https://2i2c.org/blog/2025/per-user-storage-quota-gcp/)

_**Thanks to** [DevSeed](https://developmentseed.org/) for collaboration on this work, in addition to the [NASA VEDA project](https://www.earthdata.nasa.gov/data/tools/veda) for funding this effort._

## Automated backups for GCP hubs

Another concern communities have is “what happens if something breaks and I lose data?” Cloud providers offer a number of ways to recover from disasters like this, and we did some work enabling this for GCP so that communities have disaster recovery options available to them.

[Announcing backups for GCP-hosted hubs!](https://2i2c.org/blog/2025/gcp-filestore-backups/)

## Deploying JupyterHub on public infrastructure

Deploying Kubernetes and JupyterHub on publicly-managed infrastructure could be an excellent way to reduce the perceived risk of depending on large tech companies for their key workflows, and potentially reduce costs by using federal infrastructure that can be paid with special grant funding. We built team expertise in deploying and running JupyterHub and BinderHub on JetStream2, and have promising results that we hope to build upon in Q2.

[Open infrastructure for collaborative geoscience with Project Pythia: Learning how to deploy a BinderHub on Jetstream2](https://2i2c.org/blog/2025/jetstream-binderhub/)

_**Thanks to** [Jetstream2](https://jetstream-cloud.org/) for an ACCESS allocation, to Julian Pistorius for technical support, to [Project Pythia](https://projectpythia.org/) (NSF award 2324302) for funding this work, and to [Andrea Zonca](https://www.zonca.dev/posts/2024-12-11-jetstream_kubernetes_magnum) for preliminary work on Kubernetes deployments on Jetstream 2._

## Upgrading to the latest JupyterHub version

We upgraded all of 2i2c’s community hubs to use JupyterHub 5.0. This brings in a bunch of security improvements, bugfixes, and enhancements. You can find links to the highlights and changelog in our blog post below.

[2i2c hubs now run JupyterHub 5.0](https://2i2c.org/blog/2025/jupyterhub5-upgrade/)

## Reproducible environments for community members

Finally, we did a bit of product brainstorming around enabling communities to bring their environments with them when they publish. We are interested in making it easy to re-use a community’s hub infrastructure to provide the reproducible environments needed for publishing or communicating their work externally. Here’s a brief brainstorm for what this could look like:

[Towards frictionless, portable, and sustainable reproducibility with Binder](https://2i2c.org/blog/2025/frictionless-reproducibility/)

## Improving the UX and flexibility of community documentation with MyST

To provide our communities with quality documentation that sits alongside their Hubs, we have been working on improving MyST to allow for a more flexible and usable document authoring experience, with improvements to landing page layouts, theming, galleries, button layouts, and project launching. We’re aiming to deliver a complete MVP covering our communities’ most requested features by the end of Q2. 

## In case you missed it

Finally, below are a few other blog posts where we’ve documented major impact stories and organizational updates:

**Community impact**

- [Harnessing Marine Open Data Science for Ocean Sustainability in Africa, South Asia and Latin America](https://2i2c.org/blog/2025/hackweek-shoutout/)  
- [NASA VEDA & 2i2c Update for Q4 2024 (Oct-Dec 2024)](https://2i2c.org/blog/2025/veda-update-q4-2024/)

**Open Source impact**

- [Chris is joining Project Jupyter's Executive Council](https://2i2c.org/blog/2025/jupyter-executive-council/)  
- [Simplifying and speeding up Binder builds with BuildKit](https://blog.jupyter.org/simplifying-and-speeding-up-binder-builds-with-buildkit-d44f96582994)  
- [2i2c joins the mybinder.org federation with a cheaper and faster way to deploy Binderhub](https://2i2c.org/blog/2025/binder-singlenode/)  
- [Designing for an ecosystem: a case study in cross-project open source contribution](https://2i2c.org/blog/2025/jupyter-book-cors/)

**Organizational updates**

- [Announcing our formal commitment to open technology](https://2i2c.org/blog/2025/community-ownership/)

## Acknowledgements

- Our strategic and organization-level work is supported by a grant from [The Navigation Fund](../../../collaborators/navigation/) and fees from [our member organizations](../../../members/).
