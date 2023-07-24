---
title: "Community update Q1 2023: Growing our community partner network and our team"
subtitle: ""
summary: ""
authors: ["Chris Holdgraf"]
tags: []
categories: ["updates"]
date: 2023-04-28
featured: false
draft: false
---

It's a month after the end of Q1 2023, and we'd like to share a belated update about what we were up to in the first quarter of this year (we have good excuses for being late, including new tiny humans, I promise).

This quarter we grew our engineering team significantly, and started to refine our team processes and structures to accommodate this extra complexity.
We expanded our managed cloud service with new community partners, and made a number of improvements to our technical infrastructure and organizational processes for managing this service.

Read on below to learn more about what we've been up to!

## New community partnerships

We added several new community partnerships to our managed hub service.
We've deployed new hub infrastructure for each of the following groups:

- Our [University of Toronto Jupyter service](https://act.utoronto.ca/jupyterhub-support/) now has a dedicated R hub.
- We ran an event hub for the [Drakkar Ocean project](https://www.drakkar-ocean.eu/)
- We deployed a hub for the [NASA Visuaslization Exploration and Data Analysis (VEDA) project](https://www.earthdata.nasa.gov/esds/veda).
- We deployed a hub for the [QuantifiedCarbon](https://www.linkedin.com/company/quantifiedcarbon/about/) organization.
- We ran an event hub for [OceanHackWeek 2023](https://oceanhackweek.org/).
- We onboarded several new community colleges to our "JupyterHubs Education in Community Colleges" collaboration with [CloudBank](https://www.cloudbank.org/welcome-cloudbank) and [UC Berkeley CDSS](https://data.berkeley.edu/).

## Service improvements

Below are a few highlights for ways in which we improved our [Managed Cloud Service](https://docs.2i2c.org) for our partner communities.

### We simplified our authentication workflow with CILogon

Authentication services allow us to identify a user when they log onto a hub, which determines their ability to access hub resources.
Previously we had used a combination of [Auth0](https://auth0.com/), [CILogon](https://www.cilogon.org/), or [GitHub](https://infrastructure.2i2c.org/hub-deployment-guide/configure-auth/github-orgs.html) for authentication.

However, over the past year we've been happy with our use of CILogon so far, especially because of its non-profit status and alignment with many research and education institutions that we work with.
This quarter, we decided to streamline our authentication process by dropping the use of Auth0 and grow our partnership with CILogon.

💡 _Learn more_

- See [CILogon's write up about it's partnership with 2i2c](https://www.ncsa.illinois.edu/security-made-simple-with-ncsas-cilogon/)
- See [our blog post about our use of CILogon](https://2i2c.org/blog/2023/cilogon-integration/)

### We exposed user activity dashboards in JupyterHub so communities know how many people are using the service

We tend to work with _leaders_ of communities that utilize our service and infrastructure for many others in their network.
For example, a teacher with a classroom of students, or a researcher with a global network of collaborators.

In these cases, it's useful to track how many users are actively using a platform over various metrics of time.
This can tell you whether your community finds a service useful, and whether this is growing or shrinking.

We use [Grafana](https://grafana.com/) to automatically generate dashboards of activity for all of our community hubs and clusters.
However, tracking **daily, weekly, and monthly active users** was not part of JupyterHub's core functionality.

So, we decided to upstream this functionality into JupyterHub and expose it via [the JupyterHub Grafana project](https://github.com/jupyterhub/grafana-dashboards).
All 2i2c hubs now track daily, weekly, and monthly unique active users.
And importantly, anybody else deploying the [Zero to JupyterHub for Kubernetes](https://z2jh.jupyter.org) can use this feature now too.

💡 _Learn more_

See [Yuvi's blog post about this feature](https://blog.jupyter.org/accurately-counting-daily-weekly-monthly-active-users-on-jupyterhub-6fbec6c6ce2f).

### We made our support process more structured with a new support widget

We've added a support widget to our [service documentation site](https://docs.2i2c.org).
This will allow users to provide structured support requests directly to our team, allowing us to triage and respond more quickly.

Here's our support button and widget in action:

{{< figure src="support-button.png" width=500 title="Our fancy new support button!" >}}


### We upgraded Kubernetes across all of our AWS clusters

[Kubernetes](https://kubernetes.org) is at the core of our cloud infrastructure and scalability.
We use either a shared or a dedicated Kubernetes cluster for each of our community partners, and it is the foundation upon which all of their Jupyter infrastructure rests.

One of the biggest challenges with managing an ongoing cloud service is keeping the underlying infrastructure upgraded.
This brings in new stability and functionality, but also often involves manual steps and toil.
This quarter, we upgraded each of our AWS JupyterHubs to [Kubernetes 1.24](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.24.md) and will continue this effort with other providers in the coming quarters.

### We streamlined our hub uptime checks to be more efficient

The best kinds of failures are ones that your operations team recognizes and solves before any users run into the problem themselves.
We use the [Google Cloud Platform HTTP uptime checker](https://cloud.google.com/monitoring/uptime-checks) to [run regular uptime checks for each of the community hubs that we use](https://infrastructure.2i2c.org/topic/monitoring-alerting/uptime-checks.html#simple-https-uptime-checks).
This allows us to get quick alerts if any of our community hubs is down for some reason.

We made several optimizations to this process so that we can more efficiently monitor hub uptime and trigger alerts to our engineering team if action is needed.

## Organizational updates

We made a number of broader improvements to our team processes and policies, and even got a shout-out from a few community partners!

### We defined organizational principles around engaging in healthy ways with open source communities

2i2c interacts with many open source communities throughout its work, due to the fact that the majority of the improvements we make are done via **upstream contributions**.
We define [several key open source communities](https://compass.2i2c.org/organization/mission/#key-stakeholders) that we interact with, and we needed a philosophy and set of practices to ensure that our relationship with them remains healthy and supportive.

💡 _Learn more_

Check out _[Principles and considerations for ethically accepting funding for open source](https://2i2c.org/blog/2023/open-source-funding-principles/)_ for our first take on this, and [our Open Source Strategy](https://compass.2i2c.org/open-source/strategy/) page for our current team policies around this.

### We responded to a NASA RFI on "Scientific Data and Computing Architecture to Support Open Science"

NASA recently put out a Request for Information around open science and open source infrastructure: [NASA RFI NNH23ZDA005L: Scientific Data and Computing Architecture to Support Open Science](https://nspires.nasaprs.com/external/solicitations/summary.do?solId=%7B78AA81B6-A7B9-D934-20F8-7B3151DA59A2%7D&path=&method=init).
We responded with some of our ideas around how to build more open, inclusive, collaborative scientific communities with cloud infrastructure and open source tools.

💡 _Learn more_

[Check out our submission, "Building the open source stack"](https://zenodo.org/record/7662828#.ZFEROBXMKrN).

### We added two new team members and a new team role

Our [Open Engineering Team](https://2i2c.org/organization/#faces) continues to grow!
We added a new team member to improve and manage our cloud infrastructure service: [Erik Sundell](https://2i2c.org/author/erik-sundell/).
As our team has grown, we have also had to manage more complexity in communicating and coordinating across a globally-distributed team of engineers.
To help us manage this system, we've [created a new Engineering Manager Role](https://compass.2i2c.org/engineering/roles/engineering-manager/) and promoted [Damian Avila](https://2i2c.org/author/damian-avila/) as our team's first engineering manager.

### OpenScapes wrote up a blog post about our cloud service collaboration

We got a nice shout-out from Luis Lopez at the OpenScapes project, describing the benefits of the cloud service that we run for their communities.
Check out his blog post: [The why, what, and how of our NASA Openscapes cloud infrastructure: 2i2c JupyterHub and corn environment](https://www.openscapes.org/blog/2022/11/17/nasa-earthdata-cloud-infrastructure/#cloud-optimized-data-formats).

## Onward to Q2

Many thanks to the 2i2c team, our partner communities, our funders, and the many others that have provided us support and guidance.
We hope that this update provides a helpful idea of our priorities and major efforts, and we look forward to giving you a new update in Q2!

{{% about-us %}}
