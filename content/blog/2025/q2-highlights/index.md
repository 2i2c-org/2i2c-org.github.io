---
authors:
- Giuliano Maciocci
- Chris Holdgraf
- April Johnson
date: 2025-07-21
category: service
title: Product and team highlights from Q2 2025
---


This post highlights what stood out to us from last quarter and reflects on the [targets we set at the start of the quarter](https://2i2c.org/blog/2025/q2-product-goals/).

This quarter, our team learned the importance of shipping iteratively and inviting feedback frequently. In some cases, we learned this the hard way - having spent multiple cycles developing without feedback from community representatives. In other cases, we made rapid progress by working in collaboration with community members in our network. This quarter, we are leaning into this approach as we work towards **building a more standardized and sustainable service** for our community network.

Here's what stood out from the quarter:

## Group-level resource monitoring

Building on our previous work delivering [usage monitoring using Prometheus and Grafana](https://2i2c.org/blog/2024/aws-cost-attribution/), we've released [jupyterhub-groups-exporter](https://2i2c.org/blog/2025/jupyterhub-groups-exporter/), allowing hub administrators to leverage the latest group management features in JupyterHub to monitor group-level resource usage effectively, making it easier to identify usage patterns across teams and departments.

> ⭐ Members of 2i2c's community network can learn how to use this in [our user guide to usage monitoring](https://docs.2i2c.org/admin/howto/monitoring/grafana-dashboards/#getting-a-grafana-account). See this [blog post announcing `jupyterhub-groups-exporter`](https://2i2c.org/blog/2025/jupyterhub-groups-exporter/).

## Improve creating and sharing custom environments

Last year we introduced [customizable servers via profile lists](https://2i2c.org/blog/2024/jupyterhub-fancy-profiles-rollout/). We're building on that - servers can now be configured to [allow users to dynamically specify, build, and share their own custom environment images](https://docs.2i2c.org/user/topics/dynamic-imagebuilding/) without the need for a hub administrator. This will allow community champions with diverse user bases to give their users greater flexibility to support a wide variety of custom computational workflows, accelerating knowledge discovery and sharing. Look out for a blog post on this development in the coming weeks and months.

> ⭐ Members of 2i2c's community network can learn how to use this in our **[dynamic image building quick start guide](https://docs.2i2c.org/user/topics/dynamic-imagebuilding/)**.

## Co-located narrative content with out-of-the-box Jupyter Book support

Central to our communities' work is sharing new findings, best practices, and community resources. To facilitate that, we've added support for [Jupyter Book 2](http://next.jupyterbook.org) for all of our member communities. Our communities can rapidly build interactive starter documentation and provide users with a rich, interactive, and informative onboarding experience. With a suite of customizable landing-page layouts, colour themes, and component galleries ready to match a community's branding, it's now easier than ever to couple a hub with its own co-located narrative content.

> ⭐ Members of 2i2c's community network can learn how to use this in [our user guide to documentation and sharing](https://docs.2i2c.org/admin/howto/monitoring/cost-attribution/). See [this blog post for an announcement](https://2i2c.org/blog/2025/jb-for-communities/).

## A better onboarding experience for our communities

We have been working on a streamlined onboarding experience for communities, smoothing out the process of gathering requirements, customizing a hub for the community's specific needs, and delivering new hubs more rapidly. We will be rolling out this process in the next few weeks for new communities onboarding the 2i2c network, and aim to continue learning and refining this process to deliver a faster, smoother onboarding experience for everyone.

> ⭐ Members of 2i2c's community network will see **changes to our process** over the coming months that increase the speed and ease of hub delivery.

## Efforts to improve and formalize the services we deliver to our communities

As 2i2c has grown over the past few years, it organically developed internal processes for handling common tasks such as the management, rollout and maintenance of hubs, as well as expect consulting to help our communities get the most value out of their hubs. Earlier in the year, we realised it was time to review and refine these processes to better serve our growing community network. As a result of this exercise, we now have tighter service definitions and best practices which clarify what service levels our communities can expect, and how we can internally meet those expectations. We will be publishing our service definitions in the coming months as they are finalized, to ensure full transparency with our communities.

> ⭐ You can learn more about our efforts to standardize and scale our services by [following the 2i2c blog](http://2i2c.org/blog), where we'll share our work as it stabilizes.

## Another update coming in Q3

We'll be announcing the focus for our next quarter in a follow-up post, so stay tuned for our next roadmap update, and don't forget to [let us know what you think](https://docs.google.com/forms/d/e/1FAIpQLSfo6JFr9L5gEFpk_QjoR23YZ9GHXYaO-3WZWZV3qRz8pj7dbg/viewform?usp=dialog) of our direction - we welcome your feedback!
