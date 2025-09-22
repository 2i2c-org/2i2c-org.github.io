---
title: "Systematizing our upstream community support"
date: 2025-05-21
authors:
  - Yuvi Panda
tags:
  - open source
categories:
  - impact
---
(Edited by Chris Holdgraf)

Over the past few months we've been running an experiment to be more thoughtful about our goals, strategy, and systems for supporting upstream communities _as a team_. This is a summary of the major ideas behind our current plan. It includes a few team targets and practices that we'll pilot over the next year. We'll revisit this as we learn more. Our goal is to provide transparency about the motivations behind our actions, and also to serve as an example that other organizations might learn from in their own upstream contributions.

_**Note**: This does document is not about the upstream contributions we make as part of our own product work (e.g., implementing a feature that one of our member communities exists). It is about our work to generally make upstream communities healthier and more impactful. See this [blog post about the difference between these two kinds of upstream work](TODO: LINK TO BLOG POST)_

## Why have an institutional goal for upstream contributions?

Healthy open source communities rely on both individual and institutional contributions. 
2i2c aims to be an *excellent "upstream citizen"*, so we need a structured approach with intentional goals for what we want to achieve, and *why* it is the right use of our time.

Without a goal and plan for upstream contribution, the best outcome we can hope for is the scattered efforts of a few individuals (with all the associated pitfalls of the [Tyranny of Structurelessness](https://www.jofreeman.com/joreen/tyranny.htm)), rather than a team. The worst outcome is that our outsized ability to make contributions prevents a community from having its own momentum and direction, and turns 2i2c into the sole stakeholder that can develop and maintain an upstream project such that we functionally take it over.

By intentionally setting out our goals for upstream engagement, our stakeholder communities can hold us accountable if we're taking actions that are either contrary to, or out of scope of, our goals. Here is our current thinking:

## 2i2c's Long Term Goal for upstream engagement

With this in mind, we've chosen to use the following *outcomes*, which represent our major goals for upstream contribution:

> We want the Jupyter[^0] community to be a *multi-stakeholder*[^1], *diverse*[^2] community with very high [*bus factor*](https://en.wikipedia.org/wiki/Bus_factor), because we believe this is a critical pre-requisite for advancing [our mission and value proposition](https://compass.2i2c.org/organization/mission/).

[^0]: With a current focus on the JupyterHub subcommunity, but generally applicable to any open source community we have a strategic interest in. (TODO: Understand if myst / jb should be here)
[^1]: With different kinds and sizes of organizations (companies, non-profits, universities, etc) and individuals being stakeholders. We want to avoid a single organization monopolizing power within any community.
[^2]: Across the power spectrum - from users to bug reporters to casual contributors to maintainers to people on governance duty

We want to build team processes that help upstream communities make progress towards this goal, so everyone can (and does) equitably participate in upstream communities with the support they need. 

## Our current objectives to accomplish this goal

This is a long ranging goal, and we've adopted the following more focused objectives to have something more concrete we can work towards. We're focusing on the JupyterHub community for now, and are exploring how to adapt this for other upstream communities we participate in:

1. **Objective 1**: Increase the amount of casual but returning contributors to the JupyterHub community
2. **Objective 2**: Increase the amount of total maintainers in the JupyterHub community

We've chosen these two objectives because we believe we can meaningfully make progress on both of them, and do so by equitably changing our internal processes so 2i2c staff can meaningfully contribute within their work hours towards these goals.

## Activities that feed into these objectives

We'd like to experiment with the following 4 activities, along with associated KPIs, to try out for the next 6-9 months. 

> **Implementation note**: We will not start doing **all** these immediately! We will consult with the rest of the team, and start these 1 at a time so we can build these processes sustainably and equitably.

### Review Pull Requests from non-maintainers

Imagine two different scenarios:

1. You casually contribute a PR to some OSS project. Someone responds the next day, you have a pleasant back and forth, and it gets merged (or rejected) within a few days.
2. You casually contribute a PR to some OSS project. Nobody responds for a year. Eventually someone leaves a comment. You have forgotten everything, and don't even respond. Much later, your PR gets closed as stale.

Which experience will encourage you to come back and contribute again?

It's clearly (1). So we should try to use our institutional capacity to bring the community closer to (1).

We'll accomplish this by including the following work item in every sprint:

> **Review of N PRs by non-maintainers of JupyterHub**

We will build skills (via pairing, training, etc) inside the organization to be able to do this, as not everyone will feel comfortable reviewing pull requests for all projects nor have rights to actually merge or close PRs. We may also do additional work that helps drive this activity forward, such as new contributor drives, better documentation, and policy advocacy. We will strive to make sure this includes pull requests of all types, not just code contributions. 

#### KPIs

Two KPIs shall be measured for this activity:

1. Number of PRs merged (or closed) through our sprint planning activity.
2. Number of *returning* contributors whose PRs were reviewed by us.

### Issue Triage office hours

Issue Triage is hard for newcomers to do, as often it requires deep knowledge of various components to understand how to direct an issue or refine it. As part of our sprints, we will run regular (cadence TBD, but no less frequently than monthly) "Issue Triage" office hours focused on triaging new issues that come up. To start with, this will be focused on serving _other members of the 2i2c Team_, with a focus on upskilling them. We'll then explore how we can open these sessions up to the broader upstream community.

#### KPIs

1. Number of issues triaged by 2i2c team members

### Sponsoring and Mentoring new Maintainers

Beyond just contributions, OSS communities must also grow their _contributors_ into a pool of _maintainers_, or they will die. 

{{< figure src="https://imgs.xkcd.com/comics/dependency.png" alt="XKCD comic about dependency" link="https://xkcd.com/2347/" caption="XKCD comic about dependency" >}}

But growing new maintainers takes time and effort. Not just on behalf of the person who is trying to be the maintainer, but on existing maintainers who have to spend time mentoring and sponsoring this person. The focus on sponsorship is very imporant, for excellent reasons [laid out by Lara Hogan](https://larahogan.me/blog/what-sponsorship-looks-like/). This work also takes a long time to manifest - closer to a year than a month.

We shall build structures to identify potential maintainers, and build long term pathways for them to do work in the community to gain maintainership status. As JupyterHub doesn't have an explicit 'how to become a maintainer' pathway we could just follow, we will build our own process via these focus areas:

1. Identifying potential candidates for maintainership
2. Identifying potential community work they can do to help get involved (contributing bug fixes, code reviewing, issue triage, helping answer questions, contributing code / documentation, release management, etc)
3. Build pathways for candidates to do (2) as appropriate.
4. Continue to iteratively do these until candidates have done 'enough' work in the upstream community to gain maintainership status.

This work is essentially nebulous, but very worthwhile. We will need to co-ordinate this particular effort more closely with community leaders, and recognize this takes a long time to actualize.

In the Jupyter community, maintainership status is tied to individuals, not to organizations they work for. This means that nobody should get maintainership status *simply* because they work for any specific organization (such as 2i2c). We should look for a diverse set of candidates, ideally funded by different organizations, who are also *interested* in becoming maintainers.

> -----
> 
> 
> # [TODO: Yuvi do you want to keep this note?]
> 
> 
> ------
_**Note**: We already have at least one such person identified (Tarashish from Development Seed), and nominal acceptance from MinRK (JupyterHub community lead) for this process._

#### KPI

This measurement moves slowly, but is very clearly impactful:

1. Number of people who have become maintainers due to our concerted efforts.

### Increase bus factor and diversity of people making releases

Making releases is often a thankless task, but is important to the health of any community. It involves co-ordinating testing, writing changelogs, understanding if any special upgrade instructions need to be provided, etc. Institutions can help here, by dedicating time for people in the team to perform this task on a regular cadence. To advance the 'multi-stakeholder' and 'high bus factor' aspects of our goal, we will also make every attempt to have many different people do releases, both via mentorship and sponsorship. This will get integrated into our regular workstreams.

#### KPIs

1. Number of releases performed by 2i2c engineers
2. Number of releases performed by others with sponsorship / mentorship from 2i2c engineers

## What projects do we focus on?

Our long term goal applies to *any* upstream community that:

1. We strategically depend on to serve our communities,
2. We have a *need* to help sustain, given overall dynamics in the upstream community
3. We have the *ability* to help sustain

For example, Kubernetes satisfies (1) but not (2) or (3), while JupyterLab meets (1) and (2) but not (3) (presently). Currently this policy as-written only applies to the JupyterHub community, but that is subject to change as our organization changes.

## Team Responsibility

Implementation of this policy is a responsibility of [2i2c's Product & Services team](https://compass.2i2c.org/product-and-services/). These activities will need to be integrated into the day to day working practices of this team, so it doesn't become an external shadow process that only some team members do.

## Next steps

We're excited to experiment with a more effective and health system for upstream contribution, and are eager to learn. We'll share our experiences as we run this system, in the hopes that others can learn from (and comment on!) our process.

## Acknowledgements

Thanks to [MinRK](https://github.com/minrk) for helping review a draft of this!
