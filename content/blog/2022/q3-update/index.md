---
title: "Celebrating our progress in Q3 2022"
subtitle: ""
summary: ""
authors: ["Chris Holdgraf"]
tags: []
categories: [updates]
date: 2022-10-16
featured: false
draft: false
---

Quarter 3 of 2022 has wrapped up, and the 2i2c team has been busy making improvements across our infrastructure, organization, and operations.
This is a quick post to celebrate the work we've done over the past three months, and to briefly share what we're working on next.

Below we'll provide a brief update about major developments this quarter, broken down by functional areas of 2i2c.

{{% callout %}}
These are the main highlights from this quarter - if you'd like to check out more of the work that we've done, see:

- [All the PRs we've merged in Q3](https://github.com/pulls?q=is%3Apr+merged%3A2022-07-01..2022-10-01+org%3A2i2c-org+archived%3Afalse+sort%3Aupdated-desc+)
- [All closed issues in Q3](https://github.com/issues?page=4&q=is%3Aissue+closed%3A2022-07-01..2022-10-01+org%3A2i2c-org+sort%3Aupdated-desc)

{{% /callout %}}

## Community impact

These are a few ways in which we've collaborated with communities and demonstrated impact over the last few months.

{{% callout note %}}
If you are interested in partnering with 2i2c to have your own managed JupyterHub, please contact us at `partnerships@2i2c.org`.
We have a shared cluster on Google Cloud, with plans to deploy one on AWS soon, and dedicated clusters can be run on any major cloud provider. Please see [our service documentation](https://docs.2i2c.org/en/latest/about/service/index.html) for more details.
{{% /callout %}}

**New JupyterHubs for communities**. We've deployed JupyterHubs for several new partner communities. Here's a quick list:

- PaleoCube and PaleoHack Hubs [infrastructure#1418](https://github.com/2i2c-org/infrastructure/issues/1418)
- NeuroHackademy 2022 [infrastructure#1505](https://github.com/2i2c-org/infrastructure/issues/1505)
- Alabama Water Institute CIROH hub [infrastructure#1444](https://github.com/2i2c-org/infrastructure/issues/1444)
- OceanHackWeek 2022 [infrastructure#1515](https://github.com/2i2c-org/infrastructure/issues/1515)
- COESSING Pangeo-Style Hub [infrastructure#1516](https://github.com/2i2c-org/infrastructure/issues/1516)
- Temple University Education Hub [infrastructure#1648](https://github.com/2i2c-org/infrastructure/issues/1648)
- Callysto Hub [infrastructure#1439](https://github.com/2i2c-org/infrastructure/issues/)
- London Interdisciplinary School [infrastructure#1485](https://github.com/2i2c-org/infrastructure/issues/1485)

We also ran hubs for several **community events**:

- NeuroHackademy: [infrastructure#1300](https://github.com/2i2c-org/infrastructure/issues/1300)
- OceanHackWeek 2022 [infrastructure#1576](https://github.com/2i2c-org/infrastructure/issues/1576)
- COESSING workshop: [infrastructure#1516](https://github.com/2i2c-org/infrastructure/issues/1516)
- Eddy Symposium: [infrastructure#467](https://github.com/2i2c-org/team-compass/issues/467)
- Allen Institute Summer Workshop on the Dynamic Brain [infrastructure#1621](https://github.com/2i2c-org/infrastructure/issues/1621)

For a recap of one of these events, see our recent [blog post on the Jack Eddy symposium](https://2i2c.org/blog/2022/eddy-symposium-report).

## Organization wide updates

These are large-scale organizational and strategic efforts that impact all of 2i2c.

**We applied for a CZI Grant**: In partership with The Carpentries, CSCCE, MetaDocencia, Invest in Open Infrastructure, and OpenLifeScience, we [applied for a CZI grant to provide cloud infrastructure services to global communities](../czi-global-communities-proposal/index.md).

**We grew our team**: We've hired two new team members to lead new major efforts with 2i2c. [**James Munroe**](https://2i2c.org/author/james-munroe/) will lead efforts around _community guidance and product design_, and [**Jim Colliander**](https://2i2c.org/author/jim-colliander/) will lead efforts around _partnerships and sustainability_. We also [updated our Hiring and Candidate Search documentation](https://github.com/2i2c-org/team-compass/issues/436) in the process.

**We're refining our strategy**: We've begun a process of revisiting and refining our strategy after a year of major operations, see [our strategic update blog post for more information](../strategic-update/index.md).

**We completed the [CSCCE](https://cscce.org) community management training**. Two of our team members (James and Sarah) both completed a several-week community management course that was offered in partnership with [CZI](chanzuckerberg.org).

**Our team member Sarah began a part-time role as the JupyterHub Community Strategic Lead**. Sarah will be leading community strategy efforts within JupyterHub for the next two years thanks to a grant to the JupyterHub team from CZI. [Check out this issue to follow our progress](https://github.com/jupyterhub/team-compass/issues/536).


<!-- 
TODO: Only post this if we get our engineering salary bands questions resolved before this post goes live.

**We are hiring an engineer**: Do you know an open source cloud engineer with experience in Kubernetes and has desire make research and education more impactful, accessible, and delightful? Check out our job ad [at ].
-->

## Service improvements

We made a number of improvements to our cloud infrastructure and the processes around our service.
Here's a brief breakdown:

**We expanded our shared clusters to new cloud providers and regions**. We now have shared clusters already deployed on Google Cloud Platform on `us-central1-b` and `europe-west2`.

**We defined an incident commander process**. This will allow us to coordinate and respond to major outages in our cloud infrastructure more efficiently. See [our incident response documentation](https://team-compass.2i2c.org/en/latest/projects/managed-hubs/incidents.html) for more information.

**We improved our cloud usage monitoring infrastructure**. We've deployed [a centralized Grafana Dashboard](https://github.com/2i2c-org/infrastructure/issues/328) that aggregates cloud usage across all of our partner communities, and allows us to keep track of any unexpected behavior or outages across them all. We're also looking into setting up automatic budgets and alerts for our infrastructure.

## Thanks

Many thanks to the 2i2c team, our partner communities, our funders, and the many others that have provided us support and guidance. We hope that this update provides a helpful idea of our priorities and major efforts, and we look forward to giving you a new update in Q4!

{{% callout note %}}
If you are interested in partnering with 2i2c to have your own managed JupyterHub, please contact us at `partnerships@2i2c.org`.
We have a shared cluster on Google Cloud, with plans to deploy one on AWS soon, and dedicated clusters can be run on any major cloud provider. Please see [our service documentation](https://docs.2i2c.org/en/latest/about/service/index.html) for more details.
{{% /callout %}}