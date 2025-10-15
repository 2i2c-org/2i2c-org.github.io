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

While updating our [quarterly Binder impact report](../binder-report-q3/), we discovered the archive index page had stopped updating. The analytics publisher was writing index files to temporary storage before uploading to Google Cloud Storage, but for some reason the upload step stopped working. We [deployed a fix](https://github.com/jupyterhub/mybinder.org-deploy/pull/3462) that eliminates the temporary files entirely - the code now generates the HTML index as a string in memory and uploads directly.


{{< figure src="./featured.png" title="The [mybinder.org analytics archive](https://archive.analytics.mybinder.org) shows a list of daily usage reports that anybody can download.">}}

Fortunately, we didn't lose any data! Thanks to some smart design decisions, the daily analytics files were being collected properly the entire time, only the index page listing them was broken. You can find [the full archive here](https://archive.analytics.mybinder.org).


## Learn more

- [Pull request with the fix](https://github.com/jupyterhub/mybinder.org-deploy/pull/3462)
- [mybinder.org usage dashboards](https://hub.jupyter.org/binder-data/)
- The [`binder-data/` repository](https://github.com/jupyterhub/binder-data) is where we aggregate and publish archive data to be more accessible.
- [Our quarterly impact report from mybinder.org](../binder-report-q3/)

## Acknowledgements

- Thanks to the [JupyterHub community](../../../collaborators/jupyterhub/) for their collaboration on mybinder.org infrastructure
