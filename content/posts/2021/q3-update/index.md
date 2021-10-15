---
title: "Community update Q3 2021: A new fiscal sponsor, improving our infrastructure, nearing an alpha launch."
subtitle: ""
summary: ""
authors: ["Chris Holdgraf"]
tags: []
categories: [updates]
date: 2021-10-10
featured: false
draft: false
---

> This is a (roughly) quarterly update for the 2i2c community, with the goal of providing transparency about what we've been up to, sharing what we are working on and where we have struggled, and discussing what we're up to next. In addition, almost all of the work we do is public and discoverable across [our GitHub repositories](https://github.com/2i2c-org/), and is tracked by GitHub issues. [Here's a list of issues we've closed in ~Q3](https://github.com/search?q=org:2i2c-org+type:issue+is:closed+closed:2021-06-01..2021-10-01+-label:%22type:+team-sync%22+is:issue&type=issues).

It is amazing how quickly 4 months goes by when you're building an organization from scratch! It seems like only a few weeks ago that we were recapping the beginning of the year in [our last community update](../six-month-update). Since then, we have been hard at work to make 2i2c's organizational and infrastructure more robust and sustainable.

There are several major strategic areas where 2i2c aims to have impact, and we've split this community update along each of these major areas below. We'll cover major highlights, challenges we've faced, and where we're going next.

## Highlights

### Managed JupyterHub Service

Our Managed JupyterHub Service will be a sustainable, scalable, and participatory service to provide cloud-based DevOps around JupyterHub for communities of practice in research and education. For the past several months, we have been running individual JupyterHubs for many organizations as a pilot, in order to learn more about the challenges we'll face, and give ourselves an opportunity to build centralized infrastructure around the service.

We focused on a few major areas for work, outlined below:

- **Automation across cloud providers**. We wish to serve communities that run on any of the major commercial cloud providers. We can standardize some of our infrastructure through abstractions like Kubernetes, but must still create cloud-specific deployment infrastructure as well (that Kubernetes cluster has to come from somewhere first!). In the last four months we've worked on automating Kubernetes and JupyterHub deployments on [AWS](https://github.com/2i2c-org/pilot-hubs/issues/627) as well as [Azure](https://github.com/2i2c-org/pilot-hubs/issues/512) to complement our Google Cloud deployments. We would soon like to run more hubs on this infrastructure to test how well it scales.
- **Monitoring and reporting infrastructure**. We have worked on the JupyterHub [`grafana-dashboards` project](https://github.com/jupyterhub/grafana-dashboards) to improve dashboarding around JupyterHub deployments in general, and will soon automatically deploy Grafana dashboards for our hubs so that communities have insight into what is going on in their hubs. 
- **User environment management**. We want communities to have control over the environments that are available on their hubs. We also want to encourage that our communities follow community standards for reproducible environments that can be re-used elsewhere. For this reason, we've improved the [repo2docker GitHub action](https://github.com/jupyterhub/repo2docker-action) to work with more image registries, and created a [2i2c user image template repository](https://github.com/2i2c-org/hub-user-image-template) for users to re-use for their hubs. See [the User Environment docs](https://docs.2i2c.org/en/latest/admin/howto/environment.html#bring-your-own-docker-image) for more information.
- **Support and collaboration roles**. In addition to technology changes, we have developed an alpha-level support and collaboration model for the communities we serve. Most relevant for our communities is the **community representative** role, who acts as the main point of contact with 2i2c engineers, and leads administrators on the hub to guide its customization for the community it serves. See [the user roles documentation](https://docs.2i2c.org/en/latest/about/roles.html) for more information. We have also begun prototyping a [FreshDesk support model](https://docs.2i2c.org/en/latest/admin/howto/support.html) and team processes around monitoring our support channels and responding to requests and incidents.

### Pangeo

We are working with **the Pangeo Community** to migrate the Pangeo JupyterHub deployments to utilize 2i2c's centralized infrastructure, with the goal of 2i2c taking over the development and operation of Pangeo hubs moving forward. We have spent the last few months re-creating the Pangeo hub environment from scratch on a new cloud project controlled by Columbia University, and are nearly ready to begin migration from the "old" Pangeo hub to the new one. After this, we will focus our attention on re-creating the Pangeo BinderHub and AWS hub. Follow along with this work [in this GitHub Project](https://github.com/orgs/2i2c-org/projects/16).

### Executable Books / Jupyter Book

We are nearing the final year of a grant from the Sloan Foundation to support development on the [Executable Books Project](https://executablebooks.org). As such, we have begun shifting our attention to [create a strategy for sustaining the project's community beyond this grant](https://github.com/executablebooks/meta/issues/493). In the coming months we plan on prioritizing improving our documentation (both for users and developers), as well as improving the general maintainability and quality of our codebases.

### JupyterHub community support

We recently collaborated with the JupyterHub community to [apply for two CZI EOSS awards](https://github.com/jupyterhub/team-compass/issues/380). Last month, we were notified that [our application to support a Community Strategic Lead](https://chanzuckerberg.com/eoss/proposals/jupyterhub-community-strategic-lead/) was funded! This role will fund Sarah Gibson's time to focus some of her thinking on building community structures and dynamics that are inclusive and sustainable. We'll update with more information as this project starts moving.

### Organizational foundations

Finally, in addition to our major development and projects, we have also made a lot of progress at an organizational level.

We **began [a fiscal sponsorship with Code for Science and Society](https://2i2c.org/posts/2021/css-announce/)**. This provides a new organizational and legal home for 2i2c after spending nearly a year receiving [critical strategic and start-up support](https://www.icsi.berkeley.edu/icsi/news/2021/08/2i2c-new-chapter) from our previous host, [ICSI](https://icsi.berkeley.edu). We are excited to work with CS&S to create the business infrastructure that will power our managed JupyterHubs service.

The 2i2c team has also been **improving our team planning and coordination processes**, so that we can more effectively execute on our mission. As a distributed team, we have the challenge of building processes for team communication, coordination, and planning that are distributed and asynchronous. If you're curious, you can learn more about our coordination processes in [our Team Compass](https://team-compass.2i2c.org/en/latest/practices/development.html).

We have **improved our organization-wide documentation** in order to make it easier to navigate between 2i2c's various sources of information. We hope that this provides more transparency into what 2i2c is up to and how it is structured, and that it allows us to build more connections between our projects and the broader community. Check out the new documentation landing site at [docs.2i2c.org](https://docs.2i2c.org).

## What's next

In addition to making iterative improvements around the projects described above, we have a few major goals for the final quarter of 2021.

We wish to **polish and finish the alpha-level deployment infrastructure** across each of the major cloud providers. Our end goal is to be able to _deploy a Kubernetes cluster and a JupyterHub on that cluster with minimal human effort_. This will allow us to serve more communities with fewer human effort per community. This includes migrating JupyterHubs for key communities, such as the Pangeo project.

We wish to **define and begin an alpha-level service**. This means defining a few specific "products" that 2i2c can offer, as well as a pricing model for each product. Our goals will still be to learn about how this service should evolve, but we'll have a bit more specificity about ways that others can engage with us. It will also be an opportunity to scale modestly so that we can improve our infrastructure as-needed.

We wish to **define a longer-term vision** for our Managed JupyterHubs Service, and create a plan for new workflows that we wish to enable via new development. We wish to use our experience in managing JupyterHubs to understand where new open source development would significantly help the communities we serve, and will shift our attention in this direction once we have finished the early stages of making our infrastructure more robust.

Stay tuned for some more updates about this service, coming soon!

## Challenges we've faced

Finally, we want to recognize that there are plenty of challenges along with successes when it comes to having impact! Here are a few of the unexpected challenges that we've faced along the way.

**Developing and operating multi-cloud infrastructure is a complex process**. Automating the creation and operation of Kubernetes clusters across each of the major cloud providers has proven to be a lot of work! While it has been necessary to use our pre-existing hubs to provide the opportunity to build this infrastructure, it is a challenge to both *build* and *operate* infrastructure at the same time. This has lengthened our timelines for when we expect the alpha version of the service to be ready.

**Coordinating among a distributed team takes time**. Each of our team members has been used to working asynchronously with open source communities for many years, and we under-estimated how complex it would be to port this workflow to a distributed team that must coordinate with each other much more closely on a daily basis. Deciding what to work on, how to work on it, and how to help one another take a lot of work when you only share a few hours awake at the same time. For this reason, we have spent a lot of extra energy in our first months as a team to work out [team processes for coordination and collaboration](https://team-compass.2i2c.org/en/latest/practices/development.html).

**How to design cloud services as a non-profit?** Finally, we've learned that there is no clear roadmap for how to build a sustainable cloud service like the one we describe here. 2i2c is somewhere in-between a traditional SaaS company (which tends to provide access to proprietary technology) and a bespoke consultancy (which is more hands-on and custom than we are). Our best explanation for what 2i2c wishes to do is "Open source operations/dev-ops as a service", which doesn't quite fit into either category. This means that we have more "unknown unknowns" about what kind of service and pricing model we should develop. We hope to begin answering some of these questions in our alpha-level service launch. Stay tuned for more to come!

## Get involved

Thanks for your interest in 2i2c and the mission that it hopes to accomplish.
We hope that this update has been informative and interesting, and we welcome feedback about any of the information provided. If you'd like to help with any of the challenges or efforts described above, we welcome all forms of collaboration, and are happy to chat. Please drop us a line at [`hello@2i2c.org`](mailto:hello@2i2c.org) or [contact us about joining our Slack community](https://2i2c.org/#contact). Thanks for reading!




