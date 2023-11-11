---
title: "Community update: October 2023"
subtitle: ""
summary: ""
authors: ["Chris Holdgraf"]
tags: []
categories: ["updates"]
date: 2023-11-10
featured: false
draft: false
---

Over the past few months we've been investigating ways to improve our reporting both internally and externally.
We've decided to experiment with a **monthly community update** to create a regular cadence of transparency and highlights from 2i2c for our broader community.
This is the first-such update, so bear with us as we work out the kinks!

Our goal in these updates is to share what stands out at 2i2c - what we've learned, what we're proud of, where we've struggled, and where we've had impact.
We hope this can be a historical record of "what stands out" to our team, and that it is useful for our broader community to see.
We also want this to be relatively short and to-the-point in order to make this sustainable to both write and read.

**We'd love feedback** on what else you'd like to see.
If you have any ideas, please send an e-mail to `hello@2i2c.org`.

## Rough numbers

First off, a few numbers on the scale and status of our interactive computing hub service:

We are currently running around **73 JupyterHubs** that are collectively averaging more than **4000 average monthly users**.
We have several communities in the educational sector, and so October was a peak in the Fall semester of activity.

We're recovering roughly **40% of our monthly staffing costs through recurring service revenue**.
The remainder we're making up with a combination of grants and more focused development contracts.

Assuming minimal growth in our service and fundraising, our **runway is roughly until August 2025** - however we anticipate this to shrink in the short-term once we make critical new hires in the coming months.

## Organization updates

_This section describes some major organization-wide efforts we've started or progressed over the last month._

### Improving our quarterly sprints and goals

This month our team kicked off the second round of our new quarterly sprints and goals process.
This is an attempt at focusing our team around a few goals and sub-teams that are dedicated to them throughout each quarter.
Our hope is that this allows us to make strategic "pushes" in directions that feel important for 2i2c's operations and the communities that we serve.

This quarter we incorporated a lot of learning that took place after our first iteration in Q3 2023.
We are hoping to sharpen up the timing of events throughout the process, including communicating internally and externally about our status (thus, this blog post series).

In the next quarter, we aim to build off of this work, and to identify where our future new hires of [Delivery Manager / Interrim Chief of Staff](/jobs/2023/delivery-manager.md) and our [Product Lead](/jobs/2023/product-lead.md) will fit in.

### Three new jobs posted

In October we began a short hiring push in order to address many of the organizational challenges noted in [our organizational structure and strategy audit](../organizational-report/).
We'll aim to have each of these positions filled by the end of the year, and begin incorporating new team members into our organization.
Here's a list of the three job postings:

- [Delivery Manager / Interrim Chief of Staff](/jobs/2023/delivery-manager.md)
- [Product Lead](/jobs/2023/product-lead.md)
- [Open Source Infrastructure Engineer: Cloud engineering](https://2i2c.org/jobs/2023/23qq4-open-source-infrastructure-engineer/)

### Product strategy work

We kicked off a collaboration with [Richard Pope](https://richardpope.org/) to provide us some short-term product strategy work.
In Q3, our team took stock of the many different kinds of services and technology that we deploy, with the goal of refining this into a long-term product model.

Richard will join us for several months in order to take these outputs and help us craft them into a model for where 2i2c is delivering value that we can build upon for the coming years.
We'll provide more updates for the community as this work continues.

### Continued onboarding communities in our Catalyst Project collaboration

We continued onboarding communities onto infrastructure managed by 2i2c as part of a [CZI-funded project to serve communities in Latin America and Africa](../../2022/czi-global-communities-announcement/).
The grant team began its operations last April, and spent the first several months creating an onboarding pipeline and rubric for identifying and connecting with communities.
As of October we've onboarded our first few communities - there is still a lot of content, training material, and documentation to create, and we will begin iterating on this in collaboration with our early-adopted communities in Q42023 and Q12024.

## Partnerships and impact

_This section describes notable new partnerships and developments with communities in our interactive computing hub service._

We began several new partnerships with communities in the research space this month.

The [NASA Visualization, Exploration, and Data Analysis (VEDA)](https://www.earthdata.nasa.gov/esds/veda) project is an open-source science cyberinfrastructure for data processing, visualization, exploration, and geographic information systems (GIS) capabilities.

The [US Greenhouse Gas Center](https://us-ghg-center.github.io/ghgc-docs/) provides a cloud-based system for exploring and analyzing U.S. government and other curated greenhouse gas datasets.

In addition, we've celebrated considerable growth in one of our partner communities: [CryoCloud](https://cryointhecloud.com/).
This community focuses its work around studying the Cryosphere using satellite imagery data.
They've grown their community hub to roughl 300 users in a year, and have piloted several novel interfaces for data analysis in a JupyterHub context., such as using [QGIS](https://qgis.org/) via a Linux desktop browser.

2i2c team members also gave several talks in October, and you can find links to each of these below:

- [Chris Holdgraf on 2i2c's overall purpose and operations thus far](https://www.youtube.com/watch?v=coKoUoUzLPk), delivered at the [Policy Simulation Library demo day](https://pslmodels.org/index.html).
- [Jim Colliander on the impact 2i2c wishes to have and what it means for open science](https://www.youtube.com/watch?v=SHUSoXgRAho), delivered to [the ESIP community](https://wiki.esipfed.org/Main_Page) 

## What we've learned and what stood out

_These are things that we've learned in the past month that we're using to improve our service moving forward_.

**Communities like to define and select their own environments**.
We began rolling out new functionality to allow communities to **define their user environments on-the-fly**.
This brings mybinder.org-style environment creation into a JupyterHub, and gives both more control and more visibility into the environments that communities used.
We noticed that this also begins to blue the line between different workflows and types of communities that can be served on a single hub.
It means that a hub is no longer strictly tied to a small number of user environments created for it.
We'll explore the implications of this in the coming months.

**We need to improve our billing and invoicing infrastructure**.
This month we began going through another backlog of cloud infrastructure invoices to send out to communities.
For many communities, 2i2c pays a cloud bill on their behalf and passes through costs directly to them.
This allows them to know exactly what they're paying for.
However, it is also starting to generate a lot of work!
We aim to explore ways to automate and standardize this process in the future.

**Digital Public Goods is a concept that resonates with many community leaders**.
Jim and Chris both gave talks that leaned heavily into the notion of open tools and services as "Digital Public Goods".
As public goods, it is important that they remain "driven by the public" and that they have sustainable and scalable models to grow the value that these goods provide.
We've noted that this topic resonates heavily with people across the research and education spectrum, and we're considering how to lean into these values more heavily in 2i2c.
