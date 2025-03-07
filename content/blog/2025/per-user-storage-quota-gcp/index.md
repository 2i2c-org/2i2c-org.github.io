---
title: "Enforcing per-user storage quotas now available on GCP"
subtitle: ""
summary: ""
authors: ["Sarah Gibson"]
tags: [open-source]
categories: [impact]
date: 2025-02-25T14:18:04+00:00
lastmod: 2025-02-25T14:18:04+00:00
featured: false
draft: false

# Featured image
# To use, add an image named `featured.jpg/png` to your page's folder.
# Focal points: Smart, Center, TopLeft, Top, TopRight, Left, Right, BottomLeft, Bottom, BottomRight.
image:
  caption: ""
  focal_point: ""
  preview_only: false

# Projects (optional).
#   Associate this post with one or more of your projects.
#   Simply enter your project's folder or file name without extension.
#   E.g. `projects = ["internal-project"]` references `content/project/deep-learning/index.md`.
#   Otherwise, set `projects = []`.
projects: []
---

Building upon our previous work developing [per-user storage quotas for our AWS infrastructure](https://2i2c.org/blog/2025/per-user-storage-quota/), we are pleased to announce that this feature is now available for GCP-hosted hubs!

To provide this feature on this vendor, we have updated our infrastructure provisioning system to create persistent disks, and enable automatic backups of the disk for disaster recovery purposes. However, the systems we had already developed for AWS, such as [`jupyterhub-home-nfs`](https://github.com/2i2c-org/jupyterhub-home-nfs) and our alerting system through [Prometheus Alertmanager](https://prometheus.io/docs/alerting/latest/alertmanager/), are vendor agnostic and work right out of the box with the new architecture!

If you would like to try this feature on your 2i2c-managed JupyterHub, [please get in touch](https://docs.2i2c.org/support/).
