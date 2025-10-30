---
title: "2022 in review: growing our partner communities and expanding our operations"
subtitle: ""
summary: ""
authors:
  - Chris Holdgraf
tags:
  - report
categories:
  - organization
date: 2023-01-04
featured: false
draft: false
---

2022 was a busy year for 2i2c - we not only grew our operations as well as our organization, but also grew our understanding of our mission and where we can have impact.
This is a brief reflection on this experience, and an attempt to identify our opportunities for impact and growth in 2023.

## Our major goals in 2022

We wrapped up 2021 with two major new changes.
We had just finished [moving fiscal sponsors](https://2i2c.org/blog/2021/q3-update/) and had just finished a prototype of our [alpha service offerings](https://docs.2i2c.org/).

{{< figure
  src="service-offerings.png"
  width="75%"
  caption="Our 2x2 matrix of service offerings and prices created at the end of 2021. See [the documentation](https://docs.2i2c.org/) for more details."
>}}

Our biggest challenge in 2022 was to **identify the bottlenecks in this service model**, and to begin **building the infrastructure to operate and scale it**.
This included team infrastructure, technical infrastructure, and administrative infrastructure.

Let's see what we did to accomplish this goal.

## Highlights from 2022

In 2022, we **thoughtfully grew the number of communities we worked with**, and used this to make iterative improvements in our model.
As a result, we learned some important things and made significant improvements to our service model and infrastructure.
Here are a few highlights.

### We grew the number of our partner communities

As noted above, we needed to grow the number and diversity of communities we worked with to understand where our model needed to change.
At the end of 2022, we now have **43 community partner hubs across 17 clusters** (and at least one on AWS, Azure, and Google Cloud).
This amounts to roughly **~2,500 active users** each week.
We also ran more dedicated infrastructure for more than **11 workshops and events**.

### We grew our revenue from community partnerships

One of our goals is to reach self-sustainability without requiring grant funding for most of the communities we serve.
In 2022 we built administrative infrastructure to more efficiently recover monthly costs, and were able to bring in funding for our team from community partnerships.
Here's a plot of our monthly non-grant revenue over the last several months:

{{< figure
  src="monthly-revenue.png"
  width="75%"
  caption="Our monthly non-grant revenue over the last several months. June is much larger because we filled a backlog of invoices from previous months that weren't billed yet."
>}}

### We got grant funding to serve communities in Latin America and Africa

We also learned that some partnerships may _require_ subsidization from a third party, such as historically marginalized communities and those without dedicated resources.
To explore sustainable ways to serve these communities, we applied for and received a new grant to serve communities in Latin America and Africa!
Here's the [blog post announcing this grant](../../2022/czi-global-communities-announcement/) and our [open grant narrative from the proposal](../../2022/czi-global-communities-proposal/).

### We improved our continuous integration and deployment system

Our ability to sustainably grow our service requires being able to _technically_ serve many communities from a relatively small team.
We centralized and standardized configuration and operations of many community hubs in one transparent space for all of our partner communities. 
This allowed us to more easily grow the number of communities we served from one repository.
You can [read a write-up about these improvements in this blog post](https://2i2c.org/blog/2022/ci-cd-improvements/).

### We defined a Shared Responsibility Model

Our goal is to frame each community hub as a partnership with a clear breakdown of responsibility to give communities more agency over the infrastructure and service.
The Shared Responsibility Model provides a framework for assigning responsibility for various tasks with our partner communities.
See [our Shared Responsibility Model docs here](https://docs.2i2c.org/community-lead/about/shared-responsibility).

### We defined a formal Incident Response process

Cloud infrastructure inevitably degrades over time, and running ongoing services is largely about quickly responding to issues and resolving them quickly.
To do so, we need clear processes to follow in order to quickly identify and respond to major incidents in the infrastructure.
Our Incident Response process defines formal team roles and alerting mechanisms that are served by [PagerDuty](https://www.pagerduty.com/), following best-practices in industry.
This will make our service more reliable and make our processes more transparent for our partner communities.
[Here's our current incident response process](https://compass.2i2c.org/projects/managed-hubs/incidents).

### We expanded our service offerings to include community and workflow guidance

We recognized that many communities need more than just infrastructure running in the cloud - they will also benefit from usecase and community guidance.
We're exploring a new range of roles that we could fill, starting with hiring a new team member to help us lead these efforts.
[Here's a blog post about the Product and Community Lead](https://2i2c.org/blog/2022/job-product-community-lead/).

### We began a collaboration with GESIS to develop environment building in JupyterHub

This marks our first efforts into _development-focused work_ as opposed to operating cloud infrastructure.
We will use this experience to learn how to pair focused development with cloud operations (more on that below).
It will also make it more likely that we can implement often-requested improvements to the JupyterHub / BinderHub ecosystems.
[Here's a blog post about this collaboration](https://2i2c.org/blog/2022/gesis-2i2c-collaboration-update/).

### We helped maintain several upstream open source projects

We made a number of contributions to key open source communities as part of our organizational mission.
These spanned technical improvements as well as organizational and community efforts.
One highlight is that several team members have participated in [JupyterHub's latest round of Outreachy interns](https://blog.jupyter.org/introducing-jupyterhubs-outreachy-interns-december-2022-cohort-23aaf4613556).  
See [the JupyterHub community strategy](https://jupyterhub-team-compass.readthedocs.io/en/latest/resources/community-strategy.html) page for more information.

As a brief summary, here is a plot of the issues in key open source repositories that were closed in 2022 that were authored by a 2i2c team member.

{{< figure
  src="upstream-contributions.png"
  width="75%"
  caption="Upstream issues opened by a team member that were closed in 2022."
>}}

### We refined our organizational strategy

Finally, the experience from this year gave us a lot to think about regarding our role and potential for impact in the research and education ecosystem and the open source community.
We [updated our strategy](https://2i2c.org/blog/2022/strategic-update/) in order to focus on a more holistic and collaborative approach to the work with our partner communities.
We'll continue to refine this strategy moving forward.

## Things to accomplish in 2023

We're excited about all of the progress we made in 2022, and to continue that progress in 2023.
Here are a few areas where we wish to focus our efforts as we begin the new year to keep this momentum going.

### Sharpen our Shared Responsibility Model

Our Shared Responsibility Model is in a kind of "alpha" phase right now. We have some of the high-level skeleton there, but there's a lot of detail to fill in. Thus far, communities have really liked the idea but we need to make it clearer how we break-down specific jobs and how to decide when to give more or less responsibility to another community.
We'd also like to define more intersection points with our partner communities at the level of strategic and service planning so that our communities have a say in our vision and strategic plan.

### Grow our community support operations

We've begun exploring how to support communities in their _usage_ of cloud infrastructure, but still have a long way to go to understand what role we should play here.
For example, how can we assist communities in cloud workflows without becoming domain experts ourselves?
How can we guide communities in a sustainable and scalable way?
How can we recover the costs of doing this work?
We hope to use our experiences in [our upcoming project to serve communities in Latin America and Africa](../../2022/czi-global-communities-announcement/) to explore these questions.

### Define a cost recovery model that balances sustainability and accessibility

Our current cost recovery model is intentionally very simple - we charge a fixed monthly cost for human time, and pass-through cloud costs directly.
We charge a bit more for more complex deployments and use-cases.

However, we've learned that this is both too expensive for simple deployments, and too cheap for really complex deployments.
It's also inaccessible to organizations that do not have the resources to pay, which correlates heavily with historically marginalized communities.
We'll need to refine this model to be both scalable and sustainable, but also accessible to the variety of communities we want to serve.
  
### Incorporate a dedicated software development practice that aligns with open values

In 2022 we learned that our position in _running_ infrastructure in the cloud gives us visibility into the ways that researchers and educators want open source tools to be _improved_.
In some cases our partner organizations are also willing to contribute resources to help make this happen, or we can identify third parties to fund development work.

Thus far we have focused our efforts on _deploying and managing_ cloud infrastructure.
We do make improvements to software as a part of this, but there's a big difference between running a cloud service and making significant _enhancements_ to software.

We'd like to use our position to help funnel more resources into open source development, but there are a few tricky things to figure out.
For example: How can we accept funding to do open source work in a way that doesn't effectively make us sole decision-makers or gatekeepers for doing development? How can we incorporate software development team practices into a team that has thus-far focused on operating cloud infrastructure?

Thanks for reading this update about our work in 2022.
We're excited about what we've accomplished thus far, as well how we hope to expand our impact in the near future.

## Acknowledgments

- Support for organizational and strategic work like this is provided by a grant from [CZI](../../../collaborators/czi/) and fees from [our Member Communities](../../../members/).