---
title: Announcing backups for GCP-hosted hubs!
subtitle: ""
summary: ""
authors:
  - Sarah Gibson
tags:
  - open-source
categories:
  - service-enhancements
date: 2025-02-07T13:08:22+00:00
lastmod: 2025-02-07T13:10:14+00:00
featured: false
draft: false
projects: []
---

2i2c are pleased to announce the development and deployment of automated backups of home directories on GCP-hosted hubs!

We have developed the [`gcp-filestore-backups` project](https://github.com/2i2c-org/gcp-filestore-backups) that regularly creates backups of JupyterHub home directories for disaster recovery purposes. The project is a Python wrapper around the [`gcloud` tool](https://cloud.google.com/sdk/gcloud) to regularly request backups be made of the Filestore hosting JupyterHub's user home directories, by default on a daily basis. The script also manages retention of these backups by checking how recently the last backup was made, and the age of existing backups, by default deleting any backup older than 5 days.

Having these backups enabled means that, in the unlikely and unfortunate case of data loss or corruption, we can reinstate the home directories of the hub to a relatively recent state that is at a maximum of 1 day prior to the incident.

We have deployed `gcp-filestore-backups` to all our GCP hubs presently running, with a retention period of 2 days. If you would like to discuss this further with us, [please get in touch!](https://docs.2i2c.org/support)

As ever, this project has been developed openly in line with our [Right to Replicate](https://2i2c.org/right-to-replicate/) so you can deploy it against your own infrastructure!
