---
title: Better resource management with compute quotas and usage dashboards
slug: "jupyterhub-usage-quotas"
date: 2026-08-13
authors:
  - Jenny Wong
categories:
tags:
  - open-source
---


Compute quotas and usage dashboards are now available on 2i2c hubs 🚀

This allows hub admins to cap the amount of compute resource a user can access over a given time period, as well as providing end-users with updates on their current usage.

{{< figure src="featured.png" title="The usage dashboard can be found from the hub home page navbar under *Services > usage-quota* menu.">}}

## Compute quotas

Suppose you are running a workshop and would like to cap usage to a 4GiB RAM server for each user per day. Then with compute quotas you can apply a usage cap of 4GiB x 24 hours = 96 GiB-hours over a rolling 1 day window individually to every member of a particular [JupyterHub group](https://jupyterhub-usage-quotas.readthedocs.io/en/latest/howto/user-group-management/). Alternatively, can also apply a blanket compute usage policy to all users irrespective of JupyterHub group memberships. For more details, see the [documentation](https://jupyterhub-usage-quotas.readthedocs.io/en/latest/explanation/technical/#policy-configuration). If you would like to apply a compute usage policy for your hub, then please get in touch with our [support desk](https://docs.2i2c.org/support/).

## Usage dashboards

To accompany this new feature, we have rolled out a user-facing dashboard to keep track of usage. The home storage component is enabled by default, which shows the used versus available disk usage in a user's home directory. The compute component is enabled if a compute quota policy is applied to the hub.

## Learn more

- [2i2c Community Hub Guide documentation](https://docs.2i2c.org/admin/user-management/compute-quotas/)
- [`jupyterhub-usage-quotas` documentation](https://jupyterhub-usage-quotas.readthedocs.io/en/latest)
- [`jupyterhub-usage-quotas` GitHub repository](https://github.com/2i2c-org/jupyterhub-usage-quotas)

## Acknowledgements

- [@sarahw-earthscope](https://github.com/sarahw-earthscope) and team at the [Earthscope Consortium](../../../collaborators/earthscope/) for co-creating and funding this project
- [@sunu](https://github.com/sunu) ([Development Seed](../../../collaborators/devseed/)) for co-developing the `jupyterhub-usage-quotas` package
- [@hanbyul-here](https://github.com/hanbyul-here) and [@wildintellect](https://github.com/wildintellect) ([Development Seed](../../../collaborators/devseed/)) for early design feedback
- [@minrk](https://github.com/minrk) ([BIDS](../../../collaborators/bids/)) for making upstream improvements to JupyterHub for this feature
- Funding support for this work also came from ([NASA VEDA](../../../collaborators/nasa-veda/)), a project of the Data Systems Evolution team at NASA Marshall Space Flight Center's [Office of Data Science and Informatics (ODSI)](https://www.nasa.gov/marshall/marshall-space-flight-missions/office-of-data-science-and-informatics-odsi/). ODSI enables scientific exploration and discovery through innovative data visualization techniques and analysis capabilities that lower the barrier to entry for cloud-hosted data. 
