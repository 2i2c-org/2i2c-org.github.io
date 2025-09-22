---
title: "From scattered effort to strategic impact: How we're systematizing our Foundational open source contributions"
date: 2025-09-20
authors:
  - Yuvi Panda
tags:
  - open source
categories:
  - impact
---


Over the past few months we've been running an experiment to be more thoughtful about our goals, strategy, and systems for supporting upstream communities _as a team_. This is a summary of the major ideas behind our current plan. It includes a few team targets and practices that we'll pilot over the next year. We'll revisit this as we learn more. 

> **Note**: This document is not about "Directed" upstream contributions we make as part of our own product work. It is about the Foundational contributions we make so that open source communities are healthier and more impactful. See this post about [Directed and Foundational contributions](../good-citizen/index.md).

## Why have an institutional goal for upstream contributions?

Healthy open source communities rely on both individual and institutional contributions. 
2i2c [aims to be an *excellent "upstream citizen"*](../good-citizen/index.md), so we need a structured approach with intentional goals for what we want to achieve, and *why* it is the right use of our time.

Without a goal and plan for upstream contribution, the best outcome we can hope for is the scattered efforts of a few individuals (with all the associated pitfalls of the [Tyranny of Structurelessness](https://www.jofreeman.com/joreen/tyranny.htm)), rather than a team. The worst outcome is that our outsized ability to make contributions prevents a community from having its own momentum and direction, and turns 2i2c into the sole stakeholder that can develop and maintain an upstream project such that we functionally take it over.

By intentionally setting our goals for upstream engagement, our member communities and open source communities can hold us accountable if we're taking actions that are either contrary to, or out of scope of, our goals. Here is our current thinking:

## 2i2c's Long Term Goal for upstream engagement

With this in mind, we've chosen to use the following *outcomes*, which represent our major goals for upstream contribution:

<style>
  .pull-quote blockquote {
     font-size:1.2em;
     font-style:italic;
  }
</style>
<div class="pull-quote">

> We want the Jupyter[^0] community to be a *multi-stakeholder*[^1], *diverse*[^2] community with very high [*bus factor*](https://en.wikipedia.org/wiki/Bus_factor), because we believe this is a critical pre-requisite for advancing [our mission and value proposition](https://compass.2i2c.org/organization/mission/).

</div>

[^0]: Currently this is particularly JupyterHub and Jupyter-wide leadership. We're [exploring how to incorporate JupyterBook into our service](../jb-for-communities/index.md) and are thus investing Foundation contributions there as well.
[^1]: With different kinds and sizes of organizations (companies, non-profits, universities, etc) and individuals being stakeholders. We want to avoid a single organization monopolizing power within any community.
[^2]: Across the power spectrum - from users to bug reporters to casual contributors to maintainers to people on governance duty

We want to build team processes that help upstream communities make progress towards this goal, so everyone can (and does) equitably participate in upstream communities with the support they need. 

## Our current objectives to accomplish this goal

This is a long-term goal, and we've adopted a few objectives to work towards. We're focusing on the JupyterHub community for now, and are exploring how to adapt this for other upstream communities we participate in:

<div class="pull-quote">

> **Objective 1**: Increase the number of casual but returning contributors to the JupyterHub community
>
> **Objective 2**: Increase the number of total maintainers in the JupyterHub community

</div>

We've chosen these two objectives because we believe we can meaningfully make progress on both of them, and do so by equitably changing our internal processes so 2i2c staff can meaningfully contribute _within their work hours_ towards these goals.

Below, we'll define a few activities that fall into these objectives. We'll also define a few **Key Performance Indicators** (KPIs) for each type of activity. We believe it's important to have a definition and a measure of progress to help us understand if we're on the right track and learning the right things.

## Activities that feed into these objectives

We'd like to experiment with the following 4 activities to try[^all]:

- [**Review pull requests from non-maintainers**](#review-prs)
- [**Issue Triage office hours**](#issue-triage)
- [**Sponsoring and Mentoring new Maintainers**](#mentoring-maintainers)
- [**Increase bus factor and diversity of people making releases**](#release-diversity)

[^all]: **Implementation note**: We will not start doing **all** these immediately! We will consult with the rest of the team, and start these 1 at a time so we can build these processes sustainably and equitably.

### Review Pull Requests from non-maintainers {#review-prs}

Imagine two different scenarios:

1. You casually contribute a PR to some OSS project. Someone responds the next day, you have a pleasant back and forth, and it gets merged (or rejected) within a few days.
2. You casually contribute a PR to some OSS project. Nobody responds for a year. Eventually someone leaves a comment. You have forgotten everything, and don't even respond. Much later, your PR gets closed as stale.

Which experience will encourage you to come back and contribute again?

It's clearly (1). So we should try to use our institutional capacity to bring the community closer to (1).

We'll accomplish this by including the following work item in every sprint:

> `Review of N PRs by non-maintainers of JupyterHub`

We will build skills (via pairing, training, etc) inside 2i2c to be able to do this, as not everyone will feel comfortable reviewing pull requests for all projects, nor have rights to actually merge or close PRs. We may also do additional work that helps drive this activity forward, such as new contributor drives, better documentation, and policy advocacy. We will strive to make sure this includes pull requests of all types, not just code contributions. 

#### KPIs

We're imagining two KPIs for this activity:

1. Number of PRs merged (or closed) through our sprint planning activity.
2. Number of *returning* contributors whose PRs were reviewed by us.

### Issue Triage office hours {#issue-triage}

Issue Triage is the process of combing through an upstream repository's issue tracker, engaging productively with new issues, refining them to be high-quality and actionable, and choosing to signal boost important ones for team action.
This is hard for newcomers, as it often requires deep knowledge of various components to understand how to direct an issue or refine it.
It's also challenging for many on our own team who are still learning the dynamics of working with open source communities. We'd like to learn how to upskill our team members within 2i2c and inside our upstream open source communities.

As part of our sprints, we will run regular (cadence `TBD`) "Issue Triage" office hours focused on triaging new issues that come up.
We'll begin by using this to upskill our _own 2i2c team members_ in more effectively triaging issues, and learn how to most-effectively do this. We'll then use our learning to explore how we can open up issue triage sessions to the broader upstream community so that others can learn as well.

#### KPIs

1. Number of issues triaged by 2i2c team members.[^triage]

[^triage]: This requires a definition of "an issue that has been triaged", and to our knowledge no such definition exists. We'd like to learn how to measure something abstract like "issue triage" - perhaps it is something specific putting it on a board for further action or applying a label, or something more abstract like "increasing how clear and actionable the issue is". We'll explore this when we start to make progress towards this objective.

### Sponsoring and Mentoring new Maintainers {#mentoring-maintainers}

Beyond just contributions, OSS communities must also grow their _contributors_ into a pool of _maintainers_, or they will die. 

{{< figure src="https://imgs.xkcd.com/comics/dependency.png" alt="XKCD comic about dependency" link="https://xkcd.com/2347/" caption="XKCD comic about dependency" >}}

But growing new maintainers takes time and effort. Not just on behalf of the person who is trying to be the maintainer, but on existing maintainers who have to spend time mentoring and sponsoring this person. The focus on sponsorship is very important, for excellent reasons [laid out by Lara Hogan](https://larahogan.me/blog/what-sponsorship-looks-like/). This work also takes a long time to manifest - closer to a year than a month.

We shall build structures to identify potential maintainers, and build long term pathways for them to do work in the community to gain maintainership status. As JupyterHub doesn't have an explicit 'how to become a maintainer' pathway we could just follow, we will build our own process via these focus areas:

1. Identifying potential candidates for maintainership
2. Identifying potential community work they can do to help get involved (contributing bug fixes, code reviewing, issue triage, helping answer questions, contributing code / documentation, release management, etc)
3. Build pathways for candidates to do (2) as appropriate.
4. Continue to iteratively do these until candidates have done 'enough' work in the upstream community to gain maintainership status.

This work is essentially nebulous, but very worthwhile. We will need to coordinate this particular effort more closely with community leaders, and recognize this takes a long time to actualize.

In the Jupyter community, maintainership status is tied to individuals, not to organizations they work for. This means that nobody should get maintainership status *simply* because they work for any specific organization (such as 2i2c). We should look for a diverse set of candidates, ideally funded by different organizations, who are also *interested* in becoming maintainers.

_**Note**: We'd also like to start with individuals [in our **collaborator network**](../../../collaborators/_index.md). For example, we're using an engagement between [NASA VEDA](../../../collaborators/nasa-veda/) and [Development Seed](../../../collaborators/devseed/) to onboard several team members into these projects._

#### KPI

This measurement moves slowly, but is very clearly impactful:

1. Number of people who have become maintainers due to our concerted efforts.

### Increase bus factor and diversity of people making releases {#release-diversity}

Making releases is often a thankless task, but is important to the health of any community. It involves coordinating testing, writing changelogs, understanding if any special upgrade instructions need to be provided, etc. Institutions can help here, by dedicating time for people in the team to perform this task on a regular cadence. To advance the 'multi-stakeholder' and 'high bus factor' aspects of our goal, we will also make every attempt to have many different people do releases, both via mentorship and sponsorship. This will get integrated into our regular workstreams.

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

## How will we fund this?

Foundational upstream support requires a lot of work and expertise, and we imagine funding this with a combination of two things:

- Fees from [our member communities](../../../members/). A percentage of our membership fees includes covering the cost of Foundational contributions like this.
- Targeted contributions from [some of our collaborators](../../../collaborators/). Some collaborators have funds and want to support open source at a foundational level, in some cases we use funds from these collaborators to cover our costs.

That said, we still need to explore what these efforts cost to us, as well as various mechanisms we can identify to recover those costs.

## Next steps

We're excited to experiment with a more effective and healthy system for upstream contribution, and are eager to learn. We'll share our experiences as we run this system, in the hopes that others can learn from (and comment on!) our process.

## Acknowledgements

- [@MinRK](https://github.com/minrk) and - [@bsipocz](https://github.com/bsipocz) for helping review a draft of this!
- [JupyterHub](../../../collaborators/jupyterhub/), [JupyterBook](../../../collaborators/jupyter-book/), and [Project Jupyter](../../../collaborators/jupyter/) for teaching us a lot about open source over the years.

