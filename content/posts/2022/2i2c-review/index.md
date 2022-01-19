---
title: "2i2c’s first year: accomplishments, challenges, and next steps."
subtitle: ""
summary: ""
authors: ["Chris Holdgraf"]
tags: []
categories: [updates]
date: 2022-01-19
featured: false
draft: false
---

Now that 2021 has come to an end, this also marks the end of 2i2c’s first year of operations. In this year we have grown, experimented, and accomplished a lot - we have also faced challenges and learned as a team.

**Our primary goal in 2021 was to build a strong foundation for 2i2c**. This meant doing whatever needed to be done to give ourselves a stable and reliable position to move forward.  With that in mind, we’d like to use this post to look at three major accomplishments from 2021, and reflect on how things went and where we can improve 🎉.

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

## Accomplishment 2: Turning technology into service pilots

Our cloud infrastructure is the foundation for a collection of self-sustaining services that we aim to offer. Throughout 2021 we ran several pilots to learn more about the needs of communities in research and education, and how we could build sustainable services that meet these needs.

- **We ran a university-wide hub for the University of Toronto.** This hub is used in a variety of classes throughout the university, and is made freely available to anyone with a UofT account. We hope to repeat this model for other university-wide communities, and have learned a lot about the challenges of working with particularly large educational communities.
- **We migrated Pangeo’s cloud infrastructure to be run via 2i2c.** The Pangeo Community had been operating and developing their own JupyterHub for several years, but were looking for another organization to provide more reliable/sustained operations and support for their Pangeo Cloud Service. This year we migrated the service [to run off of 2i2c’s deployment infrastructure](/posts/2021/pangeo-goes-live/).
- **We provided JupyterHubs for several hackweeks**. In addition to research and education use-cases, we also provided JupyterHubs for a number of short-term events, such as Hack Weeks. For example, the [OceanHackWeek](https://oceanhackweek.github.io/),  [PaleoHackWeek](http://linked.earth/paleoHackathon/), and [OpenScapes](https://www.openscapes.org/). These were distributed events with people from around the world, and they used a cloud-based JupyterHub as a single space for their communities to access resources and work together.

### Challenges that we faced

There are two main challenges that we’ve faced in designing services around our infrastructure:

**Balancing standard deployments, custom deployments, and scalability**. Our goal is to pool our configuration an operations infrastructure in order to reduce the maintenance burden each community hub. This will allow us to gain economies of scale and lower costs. However, there’s an inherent tension between scalability and customizability - in order to scale we must standardize the infrastructure we offer, but communities often want environments that are unique to their use-case.

**Turning services into sustainability**. We’ve learned that charging money for things does not come naturally to us. We’ve spent many years building technology and services that were offered freely to the public. This was easy to provide, but difficult to sustain. 2i2c’s goal is to offer similar services, but with a sustainability model that allows us to employ team members to do this work, and to grow in the future. Understanding how to pair the right technology, use-case, and service with a particular pricing model is an area where we must learn more.

### What’s next

Towards the end of 2021, 2i2c created its first model for a Managed JupyterHubs Service. This includes a 2-by-2 matrix of service options, and a specific price point for each. We have begun offering this service to communities, in order to learn more about the model, the pricing, and any changes that should be made. In early 2022, we hope to expand this group to more communities so that we can test this model’s ability to scale.

## Accomplishment 3: Create an organization from scratch

One of the first things that you realize when you start an organization is how much structure and process is taken for granted in pre-existing organizations. The policies, norms, practices, and organizational structure in any group tend to be created well before an individual arrives there.

The one time that this *isn’t* the case is when you’re creating the organization from scratch. This is both really scary and really exciting! You can make any choice you want, unburdened from “this is the way we’ve always done things here”. But what if you make the wrong choice?! Will you dig your organization into a hole from day one?

Perhaps our biggest accomplishment this year was **creating the foundation of a team**. What began as a free-form collection of people and GitHub repositories has slowly evolved into a more structured set of organizational practices and team norms. Here are a few major steps towards this accomplishment:

- We created [Our Team Compass](http://team-compass.2i2c.org) as the definitive source of truth for all of 2i2c’s operations. This is the best single description of “what is 2i2c, and how does it operate?”. It is both a resource for our team, as well as for the outside world to understand what we’re doing and how we do it.
- Our [Structure and Governance](https://team-compass.2i2c.org/en/latest/about/structure.html) page defined the major groups that make up 2i2c - as of the end of year 1, these are the Steering Council, Executive Director, Engineering Team, and our fiscal sponsor, [Code for Science and Society](http://codeforscience.org). In addition, our [Code of Conduct](https://team-compass.2i2c.org/en/latest/code-of-conduct/index.html) describes the behaviors that we expect out of people that participate in 2i2c spaces.
- Our [Team Practices](https://team-compass.2i2c.org/en/latest/practices/index.html) guide has information about our daily and weekly planning workflow. This describes how we coordinate and plan our actions as a distributed team.

There is a lot more in our team compass, and we invite you to give it a read to learn more about how we operate. These are living documents, and we’ll continue to improve them as we learn more.

### Challenges we faced

**Iterating in the face of uncertainty**. The biggest challenge in creating a new organization is accepting the fact that there is not a single “right” way to do things. You can investigate similar organizations from which you can draw inspiration, but there’s nobody there to tell you what is “right” or “wrong”. However, you need to start somewhere, and so we have tried to adopt a process of continual reflection and improvement rather than trying to get things perfect the first time.

**Working as a fully distributed team**.  2i2c's team is split across more than 6 time zones, and there are no times of the way when we're all in standard "working hours". This adds extra complexity in team communications, coordination, and meetings.  We have had to learn how to coordinate and plan asynchronously, usually via GitHub issues, Slack, and [our Team Compass](http://team-compass.2i2c.org). We have steadily gotten better at executing as a group, and we continue to improve and iterate!

### Where we’re heading next

In the coming year we are excited to continue refining our team processes in order to more effectively carry out the “design → implementation → deployment” loop. We’d like to improve our processes for coordinating with key open source communities around development or fundraising opportunities. We’d also like to diversify our team’s structure beyond our current engineering core, and bring on more team members with an expertise and interest in product and community management.

## Looking forward to 2022

We’re excited about all of the work that we’ve accomplished in 2021’s first year of operations, as well as all of the experience we’ve gained in taking our first steps as an organization. In 2022 we are excited to build upon this strong foundation. We’ll share more about what we’re up to as the year goes on, and look forward to connecting with others in our community along the way.
