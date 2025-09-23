---
# THIS IS A TEMPORARY FIX SO THAT THE PAGE DOESN'T BREAK BECAUSE REDIRECTS DON'T WORK
title: "On being a good open source citizen: supporting a healthy ecosystem through directed and foundational contributions"
date: 2099-09-03
authors:
  - Yuvi Panda
  - Chris Holdgraf
tags:
  - open source
categories:
  - impact
aliases:
  - /blog/2025/good-citizen/
---

Any organization building on open source faces a fundamental tension: how do you serve the needs of your organizational stakeholders while also acting as a responsible steward of the upstream projects you depend on?
This is harder than it looks - simply "making PRs" leaves a number of open source needs unaddressed, and can burn out both your team members and the open source maintainers. We think about this a lot at 2i2c, and want to share our framework to navigate this challenge intentionally.

Here are a few questions we've been grappling with:

- How do we tie general upstream maintenance to value delivered to our user communities?
- How can we scope upstream support so that it doesn't detract from our service needs and product strategy?
- How can we encourage team members to work on the most impactful aspects of upstream support?
- How can we intentionally and equitably support open source communities as a team, rather than a collection of individuals?

Along the way, we realized there are **two very different kinds of upstream contributions**:

1. **Directed Contributions**: A contribution driven by the needs of our member communities and product roadmap. We call these "Directed" contributions because they address a targeted need driven by one stakeholder (us!).
2. **Foundational contributions**: A contribution driven by the needs of the upstream community. We call these "Foundational contributions" because they're meant to provide the healthy foundation on which a community can operate and grow.

Historically we have conflated these types of contributions, but we think it's key that we treat them differently.

## Everybody has an open source hat and a stakeholder hat

Open source teams[^inclusive] are usually two kinds of teams that overlap heavily:

[^inclusive]: By "open source" we are focusing on multi-stakeholder open source projects with participatory and inclusive leadership and contributions. This wouldn't apply to an organization- or person-specific open source project.

1. A collection of _stakeholders working together_ on the open source project, each with their own goals and interests.
2. An _open source team_ with a shared goal and strategy for the open source project.

In this case, stakeholders can be individuals or companies. They use and contribute to the open source project because it advances their own interests. For example, an enthusiast contributing to a project because it brings them joy, or a company contributing to a project because they build a product that depends on the open source technology.

However, for open source projects to be successful they also need their own unique identity, goals, strategy for impact, and system of work. This allows a diverse collection of stakeholders to _work together effectively_ and _create impactful technology_. This team is made up of the same stakeholders described above, but with a responsibility to lead and support the open source team, rather than just serve their individual interests as stakeholders.

Thus, any open source stakeholder has two hats: they are both _representatives of a stakeholder_ and _members of an open source team_. While it's possible to _align the interests_ of these two groups, we think it's still important to _distinguish between them_.

## Directed Contributions benefit the stakeholder you represent

A _Directed Contribution_ is primarily driven by the needs of a stakeholder in an open source project. To use 2i2c as an example, let's take a quote from 2i2c's value proposition:

> 2i2c serves a global network of community hubs for interactive learning and discovery

*Community* here does **not** refer to open source upstream software provider communities (like JupyterHub or Kubernetes), but instead to downstream _user communities_ (like [CryoCloud](../../collaborators/cryocloud/), [Openscapes](https://openscapes.org), or [NASA VEDA](https://www.earthdata.nasa.gov/data/tools/veda)).

When 2i2c makes a Directed Contribution, it means we are trying to _deliver value to one or more of our member communities_ by making an upstream contribution.

Satisfying community needs often involves directly working on the software they use. Driven by our [right to replicate](https://2i2c.org/right-to-replicate/) principles, this means we mostly work on software that is not proprietary to 2i2c nor solely owned by us permanently - but by contributing to an upstream software community. These are all Directed Contributions.

Some illustrative examples:

1. [Allow login to be gated on OAuth2 granted scopes](https://github.com/jupyterhub/oauthenticator/pull/719) was a feature we added to support one of our communities' auth flow ([EarthScope](../../collaborators/earthscope/))
2. [Changing how `.pyc` files are kept in images](https://github.com/pangeo-data/pangeo-docker-images/pull/426) was work we did as a result of a support ticket investigating spawn timeout issues in the [LEAP](https://leap.columbia.edu/) hub.
3. [Adding landing pages functionality to Jupyter Book and MyST](https://github.com/jupyter-book/myst-theme/pull/531) was work we did to support member communities like [CryoCloud](../../collaborators/cryocloud/) and [Project Pythia](../../../collaborators/pythia/).

The fact that these are open source contributions is *incidental*. We are _primarily_ doing this work to deliver value to _our community network_. 

### We plan Directed Contributions according to our roadmap and member feedback

Directed Contributions naturally align with 2i2c's overall goals and strategy, so we use our [product processes](https://compass.2i2c.org/product-and-services/) for planning and delivering on them. However, we also want to provide transparency to upstream communities so that they understand who is driving the contributions that we're making.

With that in mind, here are a few ways that Directed Contributions relate to our practices:

- Directed Contributions should be defined by our product roadmap and prioritization processes.
- We allocate engineering time for these upstream contributions as part of our product lifecycle, _including the extra coordination and communication work needed to work at the pace of the upstream community_.
- We cross-link 2i2c product initiatives to upstream issues and pull-requests wherever we can to provide transparency about why we're making a contribution.
- We communicate this work via our blog so that 2i2c's member communities know about the contributions we've made on their behalf.

## Foundational Contributions support a healthy open source community

However, contributions can't always be driven by a stakeholder's needs or the open source team will not have an identity or support structure of its own. Here's another excerpt from our value proposition:

> We need infrastructure services that are driven by community needs and values, that follow the same open source science practices we wish to see in others, and that believe in the power of shared community resources and knowledge.

Being a "healthy upstream citizen" is core to 2i2c's mission, and is also a way to help communities we rely on remain healthy. Some of our contributions should be _Foundational_ rather than _Directed_. This means doing things that keep the overall ecosystem healthy even if it does not *directly* address a specific member community need. The *presence* of a healthy open source ecosystem is a value to our member communities in-and-of itself.

Defining "Foundational" needs is difficult, because open source teams tend to have less structure and formally-stated goals and needs than most organizations. In 2i2c's case, we focus our Foundational Contributions around *maintaining the health of the open source ecosystem*.

It includes things like:

1. Grow and guide new contributors to grow team capacity
1. Help making releases
1. Provide code review
1. Fix broken CI
1. Write documentation and tutorials
1. Manage and run meetings
1. Align open source teams on goals and strategy

However, the real point is that these actions need to be driven by _the upstream project's goals and needs_, not by 2i2c's needs.

Here are a few common examples of contributions that are _not considered_ Foundational for our team:

1. Opening a PR to add a major feature to an upstream project.
2. Creating a brand new project in an open source organization in order to scratch your own itch.
3. Engaging in reactive open-source work that isn't driven by a clear strategy or goal (e.g., randomly responding to the last few GitHub issue comments you happened to notice)

### We plan Foundational Contributions alongside our engineering roadmap

Foundational Contributions are important to 2i2c both for strategic and tactical reasons. However, when left as unstructured time (as we have historically), it runs into all the problems of unstructured work - it happens in non-strategic ways, it isn't evenly balanced across team members, it is more or less accessible depending on your personal comfort level and skills, etc.

With that in mind, here are a few ways that Foundational Contributions relate to our practices:

- We need to _own Foundational Contributions as a team_, rather than asking individuals to identify and do this work on their own.
- We need to define team _goals_ and _strategy_ to define the impact we want to have, and what kind of work leads to that impact.
- We need a team system for identifying and prioritizing the most impactful Foundational Contributions to perform.
- This system must spread the responsibility of Foundational Contributions across our whole product team.
- It means we need to give people support and training to do this effectively. For example, helping team members grow into roles that involve upstream work, rotating certain types of contributions across team members, etc.

To ensure this work is intentional and equitable across our team, we encourage Foundational contributions to happen within this framework. Contributions that falls outside of it is treated as a valued, but separate, personal contribution.

## What's next

By distinguishing between Directed and Foundational contributions, we can align and balance our immediate product needs with our long-term commitment to community health. We believe this framework allows organizations like ours to be better partners. We'd love feedback about this process, how we can improve it, and what others have learned along the way.
