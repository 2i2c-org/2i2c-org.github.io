---
title: Enforcing per-user storage quotas with `jupyterhub-home-nfs`
subtitle: ""
summary: ""
authors:
  - Sarah Gibson
tags:
  - open-source
  - storage
categories:
  - service
date: 2025-01-28T09:57:28+00:00
lastmod: 2025-01-28T10:10:14+00:00
featured: false
draft: false
projects:
  - nasa-veda
---

When sharing a storage disk between users, as is usually the case in a JupyterHub deployment, it is important to put in guardrails so that one user cannot eat up the whole storage capacity from the rest of the users.
To this end, 2i2c in close collaboration with [Development Seed](https://developmentseed.org) have developed the [`jupyterhub-home-nfs` project](https://github.com/2i2c-org/jupyterhub-home-nfs) which is a Helm chart that permits enforcing per-user quotas on the storage space.

{{% callout note %}}
Note that this feature is currently available to AWS hosted hubs only and will be rolled out to other cloud providers in the future.
{{% /callout %}}

Under the hood, the Helm chart runs [NFS Ganesha](https://github.com/nfs-ganesha/nfs-ganesha) as an in-cluster NFS server, backed by [XFS](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/7/html/storage_administration_guide/ch-xfs) as the underlying filesystem. Storage quota is enforced through XFS's native quota management utility `xfs_quota`.

Since this feature moves our infrastructure away from managed filesystems (such as AWS's Elastic File System) that cannot support per-user storage quotas, we have also developed monitoring and alerting mechanisms that will let us know when the disks are getting full, and automated back-ups for disaster recovery.

If you would like to try this on your 2i2c-managed hub, [please get in touch](https://docs.2i2c.org/support/).

This project can also be used with _any_ Kubernetes-based JupyterHub, as per our [Right to Replicate policy](https://2i2c.org/right-to-replicate/), so please try it out on your own deployment and let us know what you think!

## Acknowledgements

This project was developed and deployed in collaboration with [Tarashish Mishra](https://developmentseed.org/team/tarashish-mishra/) from [Development Seed](../../../collaborators/devseed/), funded through the [NASA VEDA project](../../../collaborators/nasa-veda/).
