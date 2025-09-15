---
title: "Our product goals for Q1 2025"
authors: ["Chris Holdgraf", "Giuliano Maccioci"]
tags: [open source]
categories: [organization]
date: 2025-02-01
---

*This quarterly post is coming out a little bit late - our goal was to post this in early January, but the year has been more complicated than we bargained for :-)*

Over the past year, 2i2c has made team-wide efforts to improve our product planning and delivery. A key part of this is re-organizing an integrated [Product and Services team](https://compass.2i2c.org/product-and-services/) that brings our strategic planning, engineering, and service delivery closer together. We've also built systems for planning and measuring progress within the P&S team, and a product initiatives system for planning major work.

Our goal is to **organize our product work around a small set of core themes** to help us focus and prioritize. As part of this, we’d like to share platform enhancement goals for roughly each quarter. These are not guarantees, but we share them to be transparent about where we think we can be the most impactful in the next few months. Here are the major areas we hope to improve 2i2c’ platform in Q1 2025.

## Expand access to cloud providers and improve data safety

One of 2i2c's goals is to showcase the ability of open infrastructure to be deployed on a variety of infrastructure proiders. This includes user-facing features, as well as guardrails and safety measures.

**In Q1 2025** we are working to bring closer feature parity between hub deployments on AWS and GCP, while enabling disaster recovery with automated home directory backups. 

## Explore deploying on public infrastructure providers

Many communities in research and education are interested in leveraging publicly-owned infrastructure providers like [JetStream 2](https://jetstream-cloud.org/index.html) and the [National Research Platform](https://nationalresearchplatform.org/). While 2i2c has historically focused on commercial cloud due to their highly-reliable Kubernetes platforms, we think it is important to explore publicly-owned infrastructure providers as well.

**In Q1 2025** we'll begin this expansion by deploying JupyterHubs and BinderHubs on JetStream 2, which will give communities access to publicly-funded computing resources. We will use this experience to decide whether it's sustainable for us to deploy on this and other publicly-owned infrastructure providers.

## Enable enhanced community knowledge bases with Jupyter Book 2

A key theme we aim to enable is **sharing** within and between community hubs. This is a critical part of the data science workflow because it allows people to collaborate on the same ideas, and build on top of one another's ideas. An early target for this is to facilitate lightweight sharing of computational content so that community members can learn from one another more effectively.

**In Q1 2025** we want to help get [Jupyter Book 2's beta](https://next.jupyterbook.org) released, and provide an out-of-the-box configuration for our communities to use it with their hubs. This includes adding landing pages and better integration with JupyterHub via launch buttons to create a more seamless experience between documentation and interactive computing.

## Enable sharing reproducible environments on a hub

Another key aspect of sharing is **sharing the computational environment as well**. This would allow communities to not only sheir their content, but also live infrastructure that allows others to reproduce and interact with their work. We think that investing more time into imiproving and deploying [BinderHubs](https://binderhub.readthedocs.io/en/latest/) (the technology behind [mybinder.org](https://mybinder.org)) will help us learn more about how to make this a reality.

**In Q1 2025** we plan to grow our capacity to deploy BinderHubs across multiple cloud providers. This will allow hub users to build their own Binder environments on the fly and make it possible to share these environments with others, enabling better reproducibility and collaboration within communities.

## Give communities more visibility and control over their hub setup and costs

Perhaps the biggest perceived risk to using cloud infrastructure is the possibility of **runaway costs**. Community leaders are often nervous that something unexpected will happen and they'll have to foot a giant bill at the end of the month. We think that reducing this risk is a key way to make cloud infrastructure safer and more useful for research and education communities.

**In Q1 2025** we are aim to add more **visibility into hub usage** and **more controls over resources via quotas**. This will allow more fine control over resource budgets such as CPU, memory, and storage. We'll also work on **assigning users to groups**, allowing communities greater control over resource allocation across large user bases.

## Standardize our hub service menu of options and prices

A key goal of our [Navigation Fund grant](../2024/funding-navigation/index.md) is to streamline ourselves into a few repeatable, scalable service offerings at different price points. This will allow us to more easily support new communities and provide a more consistent experience for users.

**In Q1 2025** we'd like to define a starting point that we can begin to iterate on. We'll define a new set of pricing based around a tiered service model, and decide on an initial set of features and services to include with each. Our goal will be to have something defined quickly so that we can iterate a few times with community feedback before the quarter is over.

## Standardize our community support services

Finally, we've audited our ongoing support practices and realized that we aren't always delivering them in an efficient way. We often share the same information one-on-one conversations, and aren't effectively leveraging our community network to support and learn from one another. We'd like to standardize and boost the scalability of our support services.

**In Q1 2025** we want to explore how we can more scalably and efficiently provide hands-on guidance, expert co-creation, and support to communities. Our goal is to define a starting point for these services so that we can offer this support in a sustainable way and begin to learn from our experiences. We also want to build a mechanism for scoping (and pricing) additional capacity that is needed beyond standard community services.

## Another update coming in Q2

Our aim is to use this blog post as a guide for the quarter, and to make progress in as many areas above as we can. As part of our Q2 planning process, we'll provide a retrospective on the accomplishments we've made towards this effort, and will provide an update for our community on our progress. Stay tuned for more!

## Acknowledgements

- Our strategic and organization-level work is supported by a grant from [The Navigation Fund](../../../collaborators/navigation/) and fees from [our member organizations](../../../members/).
