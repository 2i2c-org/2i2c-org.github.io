---
title: "Allow limiting access to Dask Gateway based on group membership"
slug: "dask-gateway-membership-access"
date: 2026-06-10
authors:
  - Georgiana Dolocan
tags:
  - open-source
  - community
categories:
  - community-impact
  - upstream-impact
---

Starting with [Dask Gateway](https://gateway.dask.org/) version [v2026.3.0](https://gateway.dask.org/changelog.html#v2026-3-0), JupyterHub access scopes support has been added to Dask-Gateway.

That means hub admins can now set, via JupyterHub role-based access control (RBAC), which hub users or groups have access to Dask-Gateway. This is especially important from a cost perspective, as it allows admins to control who can access Dask-Gateway and thus have more control over their cloud spend.

If your community is part of the 2i2c member network, you can take advantage of this feature now. 2i2c is deploying the new Dask-Gateway version alongside our hubs, so all communities we serve that are using Dask-Gateway now have access to this feature. 

Want to know more, or set this up on your hub? Check out:
  - the [Control access to Dask Gateway](https://docs.2i2c.org/admin/user-management/dask-access/) page for how to ask 2i2c to set up this feature for your hub
  - the [Dask Gateway documentation](https://gateway.dask.org/authentication.html#using-jupyterhub-s-authentication) for more details on how it works.

## Acknowledgements

- To [EarthScope](/collaborators/earthscope/) for motivating this work and providing feedback
- To [MinRK](https://github.com/minrk) for adding this feature to Dask-Gateway
- To [Yuvi](../../../authors/yuvi-panda/) for code review and guidance on the implementation
- To [Erik](../../../authors/erik-sundell/) for code review
- To our [member communities](../../../members/) for supporting us and giving us the capacity to invest in upstream open source engagement