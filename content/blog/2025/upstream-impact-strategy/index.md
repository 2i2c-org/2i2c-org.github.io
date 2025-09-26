---
title: "From scattered effort to strategic impact: How we're systematizing our Foundational open source contributions"
date: 2025-09-26
authors:
  - Yuvi Panda
tags:
  - open source
categories:
  - impact
---


Over the past year we've experimented with being more strategic about supporting upstream communities _as a team_. This is a summary of the major ideas behind our current plan. It includes a few team targets and practices that we'll pilot over the next year. We'll revisit this as we learn more. 

> **Note**: This document is not about _Directed_ upstream contributions we make as part of our own product work. It is about the _Foundational_ contributions we make so that open source communities are healthier and more impactful. See this post about [Directed and Foundational contributions](../good-citizen/index.md).

## The challenge: Why scattered individual efforts aren't enough

Healthy open source communities rely on both individual and institutional contributions. 
2i2c [aims to be an *excellent "upstream citizen"*](../good-citizen/index.md), so we need a structured approach with intentional goals for what we want to achieve, and *why* it is the right use of our time.

Without a coordinated approach, we risk two problematic outcomes:

**Best case**: Scattered, individual efforts that are subject to the [Tyranny of Structurelessness](https://www.jofreeman.com/joreen/tyranny.htm). In this case, we help at the margins but not in a meaningful way.

**Worst case**: Our organizational capacity inadvertently dominates communities, making 2i2c the sole stakeholder capable of meaningful development and maintenance. In this case, we functionally take over the project.

By setting explicit goals, both our member communities and upstream projects can hold us accountable for actions that strengthen rather than undermine community health.

## Our long-term goal: Multi-stakeholder, resilient communities

With this in mind, we've chosen to use the following *outcomes*, which represent our major goals for upstream contribution:

<style>
  .pull-quote blockquote {
     font-size:1.2em;
     font-style:italic;
  }
</style>
<div class="pull-quote">

> We want the Jupyter[^0] community to be a *multi-stakeholder*[^1], *diverse*[^2] community with a very high [*bus factor*](https://en.wikipedia.org/wiki/Bus_factor), because we believe this is a critical pre-requisite for advancing [our mission and value proposition](https://compass.2i2c.org/organization/mission/).

</div>

[^0]: Currently this is particularly JupyterHub and Jupyter-wide leadership. We're [exploring how to incorporate JupyterBook into our service](../jb-for-communities/index.md) and are thus investing Foundation contributions there as well.
[^1]: With different kinds and sizes of organizations (companies, non-profits, universities, etc) and individuals being stakeholders. We want to avoid a single organization monopolizing power within any community.
[^2]: Across the power spectrum - from users to bug reporters to casual contributors to maintainers to people on governance duty

We want to build team processes that help upstream communities make progress towards this goal, so everyone can (and does) equitably participate in upstream communities with the support they need. 

## Two concrete objectives for accomplishing this goal

Starting with [JupyterHub](../../../collaborators/jupyterhub/), we've identified two objectives that will guide our work:

<div class="pull-quote">

> **Objective 1**: Increase the number of casual but returning contributors to the JupyterHub community
>
> **Objective 2**: Increase the number of total maintainers in the JupyterHub community

</div>

We've chosen these objectives because we believe that (1) they have impact, (2) we can make meaningful progress on them, and (3) we can integrate this work into our regular workflow (during work hours, not volunteer time).

For each activity below, we've brainstormed some Key Performance Indicators (KPIs) to track progress and ensure we're learning effectively.

## Four strategic activities we'll pilot

We'll experiment with these four activities[^all]:

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

But growing new maintainers takes time and effort. Not just on behalf of the person who is trying to be the maintainer, but on existing maintainers who have to spend time mentoring and sponsoring this person. The focus on sponsorship is very important, for excellent reasons [laid out by Lara Hogan](https://larahogan.me/blog/what-sponsorship-looks-like/). This work also takes a long time to manifest - closer to years than months.

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

## Criteria for upstream projects to support

Our long term goal applies to *any* upstream community that:

1. We strategically depend on to serve our communities,
2. We have a *need* to help sustain, given overall dynamics in the upstream community
3. We have the *ability* to help sustain

For example, Kubernetes satisfies (1) but not (2) or (3), while JupyterLab meets (1) and (2) but not (3) (presently). Currently this policy as-written only applies to the JupyterHub community, but that is subject to change as our organization changes.

## How we'll implement this

### Who is responsible

Implementation of this policy is a responsibility of [2i2c's Product & Services team](https://compass.2i2c.org/product-and-services/). These activities will need to be integrated into the day to day working practices of this team, so it doesn't become an external shadow process that only some team members do.

### How we'll fund this work

Foundational upstream support requires a lot of work and expertise, and we imagine funding this with a combination of two things:

- Fees from [our member communities](../../../members/). A percentage of our membership fees includes covering the cost of Foundational contributions like this.
- Targeted contributions from [some of our collaborators](../../../collaborators/). Some collaborators have funds and want to support open source at a foundational level, in some cases we use funds from these collaborators to cover our costs.

That said, we still need to explore what these efforts cost to us, as well as various mechanisms we can identify to recover those costs.

## Next step: Learning in public

We're excited to experiment with a more effective and healthy system for upstream contribution, and are eager to learn. We'll share our experiences as we run this system, in the hopes that others can learn from (and comment on!) our process.

## Acknowledgements

- [@MinRK](https://github.com/minrk) and - [@bsipocz](https://github.com/bsipocz) for helping review a draft of this!
- [@choldgraf](../../../authors/chris-holdgraf/_index.md) for feedback, guidance, and editing for this post and the team practices in it.
- [JupyterHub](../../../collaborators/jupyterhub/), [JupyterBook](../../../collaborators/jupyter-book/), and [Project Jupyter](../../../collaborators/jupyter/) for teaching us a lot about open source over the years.

