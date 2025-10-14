---
title: Fixing the mybinder.org usage analytics archive
date: 2025-10-14
authors:
  - Yuvi Panda
categories:
  - upstream-impact
tags:
  - open-source
  - binder
  - reliability
  - data
---

The analytics archive at `archive.analytics.mybinder.org` powers the [mybinder.org usage dashboards](https://hub.jupyter.org/binder-data/) and provides a [daily-published dataset](https://github.com/jupyterhub/binder-data) that researchers and communities use to understand how Binder is being used across different domains and scientific communities.

We recently discovered the archive was down while updating our [quarterly Binder impact report](../binder-report/), then [identified the issue and deployed a fix](https://github.com/jupyterhub/mybinder.org-deploy/pull/3462), ensuring that it continues to deploy usage data about mybinder.org for the public to use.
Fortunately, the design of the analytics archive meant that we didn't lose any data in the process! You can find [the full archive here](https://archive.analytics.mybinder.org).

{{< figure src="./featured.png" title="The mybinder.org analytics archive shows a list of daily usage reports that anybody can download.">}}

This is a key resource for Binder to demonstrate its transparency and impact, and to be a useful for others to understand how Binder is used for open science.

## Learn more

- [Pull request with the fix](https://github.com/jupyterhub/mybinder.org-deploy/pull/3462)
- [mybinder.org usage dashboards](https://hub.jupyter.org/binder-data/)
- The [`binder-data/` repository](https://github.com/jupyterhub/binder-data) is where we aggregate and publish archive data to be more accessible.
- [Our quarterly impact report from mybinder.org](../binder-report-q3/)

## Acknowledgements

- Thanks to the [JupyterHub community](../../../collaborators/jupyterhub/) for their collaboration on mybinder.org infrastructure
