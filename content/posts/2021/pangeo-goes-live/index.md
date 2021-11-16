---
title: "Pangeo Cloud goes live on 2i2c!"
subtitle: ""
summary: "2i2c are pleased to announce that the first Pangeo JupyterHub is now live on 2i2c-operated infrastructure! :tada: "
authors: ["Sarah Gibson"]
tags: [2i2c, pangeo]
categories: [updates]
date: 2021-11-16
featured: false
image:
  preview_only: true
draft: false
---

 [Pangeo Cloud](https://pangeo.io/cloud.html) is an experimental service providing public cloud-based data-science environments for data-intensive geoscience research.
We have recently finished re-creating the [Pangeo](http://pangeo.io/) community JupyterHub hosted on GCP in the [2i2c-org/infrastructure](https://github.com/2i2c-org/infrastructure) repository.
This is a huge milestone in our partnership with Pangeo to provide expertise and operations of cloud-based, vendor-agnostic Jupyter infrastructure and workflows.

For users of Pangeo Cloud, the switch should have been a smooth one!
The new hub should behave nearly identically to the old one, and will be managed by 2i2c engineers moving forward, in partnership with the Pangeo community.
It will be available at the same URL (https://us-central1-b.gcp.pangeo.io) and there's no need to worry about your home directories, they were synced to the new hub only a few days before the migration took place.
Development and operations on this hub will all be done in the open and we invite participation and feedback from others in our infrastructure work.
Please see [this Discourse thread](https://discourse.pangeo.io/t/migration-of-us-central1-b-gcp-pangeo-io-to-2i2c-infrastructure/1890) as an initial place to provide feedback.

On **22nd November 2021**, the old Pangeo GCP JupyterHub will be shut down, and the project will move forward on the new 2i2c Pangeo Hub.
Moving forward, we plan to collaborate together in order to find new pathways for development in the Jupyter ecosystem - we will share more ideas of things we will work on soon!

## History of Pangeo Cloud Hubs

Pangeo has pioneered a new model in using open source and cloud-agnostic infrastructure to support scientific research in the cloud.

The first Pangeo cloud JupyterHub (pangeo.pydata.org; now defuct) was deployed for the [2017 American Meteoroligical Society Meeting](https://annual.ametsoc.org/2017/); since then, the Pangeo community has iterated through several different versions of prototype cloud-based hubs.
This allowed for many new workflows that enabled a more open and collaborative pathway to doing world class research, and included access to datasets and computational resources that were previously unattainable.
Pangeo achieved this by working in partnership with open source communities and building technology that leveraged modular open source components for their platform.

In the last several years, Pangeo have built a thriving community of practice around this infrastructure.
However as the community has grown, so has the need for more reliable and dedicated operational and developmental support since parts of the Pangeo stack require dedicated expertise and attention to managed.
Modern scalable cloud infrastructure is one example of this. Maintaining a complex JupyterHub with many users is a difficult task, and has required significant resources from the Pangeo Project up to this point.

## The Pangeo-2i2c Partnership

[2i2c](https://2i2c.org) is a non-profit team that develops and operates cloud infrastructure for interactive computing workflows.
We have extensive experience in Jupyter workflows in the cloud and a long history of contributions to projects in this ecosystem.
We have built a cloud deployment management system that allows us to centralise and configure the deployment of many independent JupyterHubs, empowering communities to leverage the same infrastructure (and team!) for JupyterHubs running in the cloud.

Similarly to Pangeo, all of 2i2c's core infrastructure is cloud- and vendor-agnostic, and follows a model of building open source tools and giving back to those communities.
Our partnership with Pangeo began through 2i2c's core competency in these areas and the similarity between the two project's technical stacks.

We've begun a partnership whereby 2i2c will manage Pangeo's cloud infrastructure and lead efforts to develop new features, in partnership with open source communities.
We sketched out a few ideas to focus on in this [kick-off thread on Discourse](https://discourse.pangeo.io/t/notes-from-the-pangeo-2i2c-kick-off-meeting/1587).
This approach allows each community to focus on it's core strengths: Pangeo will continue to grow an open community and scientific software ecosystem around geospatial analytics, and 2i2c will oversee the development and operations of the core cloud infrastructure stack that powers Pangeo's workflows.
In some areas we are still experimenting with different collaboration models to ensure that the needs of the Pangeo community are met in a way that is also sustainable for 2i2c.
Over the coming weeks, you may see some conversations (and threads for feedback!) about different support and operations models that work best for the community.
We are excited to use this as an opportunity to learn more about how to serve more complex and diverse communities like Pangeo.

We are extremely grateful to the Pangeo project for giving us the opportunity to serve their community, and we look forward to a long partnership ahead! :rocket:
