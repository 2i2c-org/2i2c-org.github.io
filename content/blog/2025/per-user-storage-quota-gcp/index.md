---
title: Enforcing per-user storage quotas now available on GCP
subtitle: ""
summary: ""
authors:
  - Sarah Gibson
tags:
  - open-source
categories:
  - service-enhancements
date: 2025-02-25T14:18:04+00:00
lastmod: 2025-02-25T14:18:04+00:00
featured: false
draft: false
image:
  caption: ""
  focal_point: ""
  preview_only: false
projects: []
---

Building upon our previous work developing [per-user storage quotas for our AWS infrastructure](https://2i2c.org/blog/2025/per-user-storage-quota/), we are pleased to announce that this feature is now available for GCP-hosted hubs!

To provide this feature on this vendor, we have updated our infrastructure provisioning system to create persistent disks, and enable automatic backups of the disk for disaster recovery purposes. However, the systems we had already developed for AWS, such as [`jupyterhub-home-nfs`](https://github.com/2i2c-org/jupyterhub-home-nfs) and our alerting system through [Prometheus Alertmanager](https://prometheus.io/docs/alerting/latest/alertmanager/), are vendor agnostic and work right out of the box with the new architecture!

If you would like to try this feature on your 2i2c-managed JupyterHub, [please get in touch](https://docs.2i2c.org/support).

## Acknowledgements

This project was developed and deployed in collaboration with [Tarashish Mishra](https://developmentseed.org/team/tarashish-mishra/) from [Development Seed](../../../collaborators/devseed/), funded through the [NASA VEDA project](../../../collaborators/nasa-veda/).