---
title: "2i2c’s first year, part 2: creating an infrastructure backbone."
subtitle: ""
summary: ""
authors: ["Chris Holdgraf"]
tags: []
categories: [updates]
date: 2022-01-24
featured: false
draft: true
---

## Accomplishment 1: Created a CI/CD foundation for our infrastructure

In 2021 most of our energy was spent building the first iteration of our continuous integration and deployment infrastructure for the JupyterHubs that 2i2c manages. This is the backbone that powers all of our community hubs, and centralizes their configuration and deployment. Our goal is to reduce the maintenance cost of managing multiple hubs, while still giving each the independence to use their own environments and configuration.

- We built [`2i2c-org/infrastructure/`](https://github.com/2i2c-org/infrastructure/), a centralized place where we store the configuration and deployment tooling for all of our hubs. You can find our [deployer scripts here](https://github.com/2i2c-org/infrastructure/tree/master/deployer). These are the tools we use to deploy and update each hub independently. You can find [each JupyterHub’s configuration here](https://github.com/2i2c-org/infrastructure/tree/master/config/hubs) - this is where we store the configuration for each hub independently.
- We built a [self-hosted environment image workflow](https://github.com/2i2c-org/hub-user-image-template) that builds on top of the [repo2docker GitHub Action](https://github.com/jupyterhub/repo2docker-action). This allows each community to control the environment for their hub via changes to Binder-style repositories, which makes their environment easier to read, configure, and deploy.
- We wrote the 2i2c [Right to Replicate](http://2i2c.org/right-to-replicate) document, which describes the principles that we follow in building infrastructure for our services. It defines our commitment to building and using technology that gives communities the right to replicate their infrastructure in its entirety, with or without 2i2c.

This is just the beginning for our infrastructure setup, and there is still a lot of optimization that we can do to make things more stable and less complex.

### Challenges that we faced

There were a few major challenges that we faced in building out our first iteration of cloud infrastructure.

First, we “built the ship as we were sailing it”. Because we had communities that needed hubs *now,* we began by setting up JupyterHubs to support them. However, doing things quickly and designing complex systems from scratch are often in tension with one another. As a result, we have had to dig ourselves out of some technical debt that was created by setting up early infrastructure that was not scalable.

Second, we’ve learned that it is complicated to support cloud infrastructure for communities that have restrictions in their cloud permissions. This is most common for teams that are a part of a larger organization, and who must abide by more restrictive policies around cloud access and permissions. This creates bottleneck points and encourages silos of permissions and access, and we will need to learn how to avoid boosting our maintenance costs and toil as a result.

Finally, we found it challenging to strike a balance between pre-built vs. flexible user environments. We wish to curate environments in order to relieve communities from doing this work themselves. However, communities have unique needs and the infrastructure must be flexible enough to meet those needs. Finding the right levers to expose to hub administrators, and intentionally leaving 2i2c out of the loop in some cases, will be a major focus of development effort moving forward.

### Where we’re heading next

The next iteration of our JupyterHub cloud infrastructure will be focused around a few major areas:

**Monitoring and Reporting.** One of the scariest things about using cloud infrastructure is not knowing exactly what’s going on in your deployment, especially as this pertains to your cloud bill. Moreover, running large cloud services makes you prone to abuse at some point. For this reason, we’re building infrastructure that improves our ability to monitor the activity on a hub, and report out anything that seems unexpected.

**Hub configurability and modularity.** JupyterHub is highly configurable and flexible - however, there are still some limitations that cause challenges for larger or more complex communities. If you require workflows that cut across **multiple cloud providers**, you must deal with the extra complexity of setting up a hub on each one. Moreover, if you need many environments in your hub, it can be cumbersome to maintain and select from all of them. We’d like to make improvements on both of these areas, so that JupyterHub users can have more flexibility in where they launch their sessions, and what resources are available to them when they start.

**Infrastructure robustness and optimization.** Finally, we want to audit our current cloud infrastructure setup, with the goal of optimizing it for cost effectiveness, scalability, and maintainability. This means investing in more testing and continuous deployment infrastructure, and generally giving ourselves and our communities more confidence in the stability and reliability of our services.
