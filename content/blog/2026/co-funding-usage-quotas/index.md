---
title: How co-funding from EarthScope brought usage quotas to every 2i2c hub
slug: "co-funding-usage-quotas"
date: 2026-11-09
authors:
  - Chris Holdgraf
categories:
  - community impact
tags:
  - sustainability
  - open source
  - jupyterhub
---

One of 2i2c's goals is to support ecosystems of research communities by operating and improving the same set of shared infrastructure.
Our hope is that by doing so, we'll be able to use the needs and resources of one community to improve a shared good that benefits all.
This is a short post describing this loop for one of our recent product initiatives as an example of how [our co-funding model](../../../about/funding/index.md) is supposed to work.

## What happened

In August, we [released compute quotas and usage dashboards](../jupyterhub-usage-quotas/index.md) for 2i2c hubs.
This was co-funded work from the [EarthScope Consortium](../../../collaborators/earthscope/), who covered the cost of both developing this technology and deploying it into production for our community network.
Here's roughly how it worked:

- EarthScope runs its GeoLab platform on a 2i2c hub, and needed a way to control compute costs by capping how much each user can run. They had some resources for this, and so we decided to scope a project that was appropriately-scoped to those resources.
- Together, we wrote a [Statement of Work](https://2i2c.org/statements-of-work/sow/compute-usage-quotas/) that described and estimated each deliverable up front[^1].
- We tracked the work in [a public initiative](https://github.com/2i2c-org/initiatives/issues/23) so that others could follow-along with our efforts, and got to work.
- We met with the EarthScope team about every month to share demos, flag blockers, and get feedback from their team. We deployed any new changes onto their hub to facilitate these cycles of testing and feedback.
- All the technology we built went into the open source package, [`jupyterhub-usage-quotas`](https://github.com/2i2c-org/jupyterhub-usage-quotas). This work was led by [Jenny Wong](https://github.com/jnywong), with help from [Development Seed](../../../collaborators/devseed/).
- The work also led to a lot of upstream fixes in JupyterHub along the way. For example, [@minrk](https://github.com/minrk) [added a `SpawnException`](https://github.com/jupyterhub/jupyterhub/pull/5464) so that JupyterHub can tell if a server was *intentionally* rejected (e.g., when a user exceeded their quota).
- After completing this initiative, we deployed usage quotas into production for EarthScope, and began rolling it out for our other communities as well. This was relatively little extra effort, because everybody runs the same standardized set of infrastructure.

[^1]: Note, you can find more statements of work like this here: https://2i2c.org/statements-of-work/

## Building for one community can benefit the whole network

We think this is a good example of how the needs of one community can be met in a way that feeds into a broader ecosystem.
In this case, EarthScope paid for a feature that it needed, but the result wasn't exclusively useful to their hub.
Any 2i2c community can now [turn on compute quotas](https://docs.2i2c.org/admin/user-management/compute-quotas/), and anyone running JupyterHub can [use the `usage-quotas` tool in their own hub](https://jupyterhub-usage-quotas.readthedocs.io/en/latest).
This is the cycle we are aiming for: one community invests in a shared need, and everyone benefits as a result.

## Acknowledgements

- [Sarah Wilson](https://github.com/sarahw-earthscope), Sophia Parafina, Robert Weekly, and Alex Hamilton from [EarthScope](../../../collaborators/earthscope/) for co-funding, testing, and championing this work with us
- [NASA VEDA](../../../collaborators/nasa-veda/) for co-funding the user-facing storage dashboard
- [Development Seed](../../../collaborators/devseed/) and [BIDS](../../../collaborators/bids/) for development and upstream contributions throughout the process
