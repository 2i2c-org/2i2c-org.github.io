---
title: "Allow limiting access to Dask Gateway based on group membership"
slug: "dask-gateway-membership-access"
date: 2026-06-10
authors:
  - Georgiana Dolocan
categories:
tags:
  - open-source
  - community
categories:
  - community-impact
  - upstream-impact
---

Starting with [Dask Gateway](https://gateway.dask.org/) version [v2026.3.0](https://gateway.dask.org/changelog.html#v2026-3-0), JupyterHub access scopes support has been added to Dask-Gateway.

What this means for JupyterHub users, is that hub admins can control, via JupyterHub RBAC, which hub users or groups have access to Dask-Gateway. This is especially important from the cost perspective, as it allows admins to control who can access Dask-Gateway and thus have more control over their cloud spend.

2i2c is deploying this version alongside the hubs, so all communities we serve that are using Dask-Gateway, now have access to this feature.

Checkout
  - the [Control access to Dask Gateway](https://docs.2i2c.org/admin/user-management/dask-access/) page for how to ask 2i2c to set up this feature for your hub
  - the [Dask Gateway documentation](https://gateway.dask.org/authentication.html#using-jupyterhub-s-authentication) for more details on how it works.

## Acknowledgements

- To [EarthScope](/collaborators/earthscope/) for motivating this work and providing feedback
- To [MinRK](https://github.com/minrk) for adding this feature to Dask-Gateway
- To [Yuvi](../../../authors/yuvi-panda/) for code review and guidance on the implementation
- To [Erik](../../../authors/erik-sundell/) for code review
- To our [member communities](../../../members/) for supporting us and giving us the capacity to invest in upstream open source engagement