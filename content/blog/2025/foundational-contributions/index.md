---
title: "From scattered effort to strategic impact: How we're systematizing our Foundational open source contributions"
date: 2025-09-26
authors:
  - Yuvi Panda
tags:
  - open-source
categories:
  - upstream-impact
---


Over the past year we've experimented with being more strategic about supporting upstream communities _as a team_. This post summarizes our current plan, including team targets and practices we'll continue to pilot. We'll revisit this as we learn more. 

> **Note**: This document is about the _Foundational_ contributions we make so that open source communities are healthier and more impactful. It is not about _Directed_ upstream contributions we make as part of our own product work. See [On being a good open source citizen: supporting a healthy ecosystem through directed and foundational contributions](../good-citizen/index.md).

## The challenge: Why scattered individual efforts aren't enough

Healthy open source communities rely on both individual and institutional contributions. 
2i2c [aims to be an *excellent "upstream citizen"*](../good-citizen/index.md), so we need a structured approach with clear goals and rationale for why it's the best use of our team's time.

Without a coordinated approach, we risk two problematic outcomes:

**Best case**: Scattered, individual efforts that are subject to the [Tyranny of Structurelessness](https://www.jofreeman.com/joreen/tyranny.htm). We help at the margins but not meaningfully.

**Worst case**: Our organizational capacity inadvertently dominates communities, making 2i2c the sole stakeholder capable of meaningful development and maintenance. We _functionally take over the project_.

By setting explicit goals, both our member communities and upstream projects can hold us accountable for actions that strengthen rather than undermine community health.

## Our long-term goal: Multi-stakeholder, resilient communities

With this in mind, we've chosen the following *outcomes* as our major goals for upstream contribution:

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

We want to build team processes that help upstream communities make progress towards this goal, so everyone can equitably participate with the support they need. 

## Two key objectives

Starting with [JupyterHub](../../../collaborators/jupyterhub/), we've identified two objectives that will guide our work:

<div class="pull-quote">

> **Objective 1**: Increase the number of casual but returning contributors to the JupyterHub community
>
> **Objective 2**: Increase the number of total maintainers in the JupyterHub community

</div>

We've chosen these objectives because (1) they have impact, (2) we can make meaningful progress on them, and (3) we can integrate this work into our team's workflow.

For each activity below, we've brainstormed some Key Performance Indicators (KPIs) to track progress and ensure we're learning effectively.

## Four pilot activities

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

It's clearly (1). We should use our institutional capacity to bring the community closer to (1).

We'll accomplish this by including the following work item in every sprint:

> `Review of N PRs by non-maintainers of JupyterHub`

We will build skills (via pairing, training, etc) inside 2i2c, as not everyone will feel comfortable reviewing pull requests for all projects, nor have rights to merge or close PRs. We may also do additional work like new contributor drives, better documentation, and policy advocacy. We will include pull requests of all types, not just code contributions. 

#### KPIs

We imagine two KPIs for this activity:

1. Number of PRs merged (or closed) through our sprint planning activity.
2. Number of *returning* contributors whose PRs were reviewed by us.

### Issue Triage office hours {#issue-triage}

Issue Triage involves combing through an upstream repository's issue tracker, engaging with new issues, refining them to be actionable, and signal boosting important ones for team action.
This is hard for newcomers, as it often requires deep knowledge of various components to understand how to direct an issue or refine it.
It's also challenging for team members still learning open source community dynamics. We'd like to upskill our team members within 2i2c and our upstream open source communities.

As part of our sprints, we will run regular "Issue Triage" office hours.
We'll begin by upskilling our _own 2i2c team members_ in effective issue triaging. We'll then explore opening issue triage sessions to the broader upstream community.

#### KPIs

1. Number of issues triaged by 2i2c team members.[^triage]

[^triage]: This requires a definition of "an issue that has been triaged", and to our knowledge no such definition exists. We'd like to learn how to measure something abstract like "issue triage" - perhaps it is something specific putting it on a board for further action or applying a label, or something more abstract like "increasing how clear and actionable the issue is". We'll explore this when we start to make progress towards this objective.

### Sponsoring and Mentoring new Maintainers {#mentoring-maintainers}

OSS communities must grow their _contributors_ into _maintainers_, or they will die. 

{{< figure src="https://imgs.xkcd.com/comics/dependency.png" alt="XKCD comic about dependency" link="https://xkcd.com/2347/" caption="XKCD comic about dependency" >}}

Growing new maintainers takes time and effort from both the potential maintainer and existing maintainers who mentor and sponsor them. The focus on sponsorship is important, as [laid out by Lara Hogan](https://larahogan.me/blog/what-sponsorship-looks-like/). This work takes years, not months, to manifest.

We will build structures to identify potential maintainers and create pathways for them to gain maintainership status. As JupyterHub lacks an explicit maintainer pathway, we will build our own process via these focus areas:

1. Identifying potential candidates for maintainership
2. Identifying potential community work they can do to help get involved (contributing bug fixes, code reviewing, issue triage, helping answer questions, contributing code / documentation, release management, etc)
3. Build pathways for candidates to do (2) as appropriate.
4. Iteratively continue until candidates have done 'enough' work to gain maintainership status.

This work is nebulous but worthwhile. We will coordinate this effort closely with community leaders, recognizing it takes time to actualize.

In the Jupyter community, maintainership status is tied to individuals, not to organizations they work for. Nobody should get maintainership status *simply* because they work for a specific organization (such as 2i2c). We should look for diverse candidates, ideally funded by different organizations, who are *interested* in becoming maintainers.

> **Note**: We'd also like to start with individuals [in our **collaborator network**](../../../collaborators/_index.md). For example, we're using an engagement between [NASA VEDA](../../../collaborators/nasa-veda/) and [Development Seed](../../../collaborators/devseed/) to onboard several team members into these projects.

#### KPI

This measurement moves slowly, but is very clearly impactful:

1. Number of people who have become maintainers due to our concerted efforts.

### Increase bus factor and diversity of people making releases {#release-diversity}

Making releases is often thankless but important to community health. It involves coordinating testing, writing changelogs, and providing upgrade instructions. Institutions can help by dedicating team time to perform this task regularly. To advance the 'multi-stakeholder' and 'high bus factor' aspects of our goal, we will have many different people do releases, via mentorship and sponsorship. This will integrate into our regular workstreams.

#### KPIs

1. Number of releases performed by 2i2c engineers
2. Number of releases performed by others with sponsorship / mentorship from 2i2c engineers

## Criteria for upstream projects to support

Our long-term goal applies to upstream communities that:

1. We strategically *depend* on to serve [our member communities](../../../members/) as part of [our community hub service](../../../platform/_index.md)
2. We *need* to help sustain, given upstream community dynamics
3. We have the *ability* to help sustain

For example, Kubernetes satisfies (1) but not (2) or (3), while JupyterLab meets (1) and (2) but not (3) (presently). Currently this policy only applies to JupyterHub, but may change as our organization evolves.

## How we'll implement this

### Who is responsible

Implementation is the responsibility of [2i2c's Product & Services team](https://compass.2i2c.org/product-and-services/). These activities must integrate into the team's daily practices, not become an external shadow process for some members.

### How we'll fund this work

Foundational upstream support requires significant work and expertise. We plan to fund this through:

- Fees from [our member communities](../../../members/). A percentage of our membership fees includes covering the cost of Foundational contributions like this.
- Targeted contributions from [some of our collaborators](../../../collaborators/). Some collaborators have funds and want to support open source at a foundational level, in some cases we use funds from these collaborators to cover our costs.

We still need to explore what these efforts cost and mechanisms to recover those costs.

## Next step: Learning in public

We're excited to experiment with more effective upstream contribution and eager to learn. We'll share our experiences so others can learn from and comment on our process.

## Acknowledgements

- [@MinRK](https://github.com/minrk) and - [@bsipocz](https://github.com/bsipocz) for helping review a draft of this!
- [@choldgraf](../../../authors/chris-holdgraf/_index.md) for feedback, guidance, and editing for this post and the team practices in it.
- [JupyterHub](../../../collaborators/jupyterhub/), [JupyterBook](../../../collaborators/jupyter-book/), and [Project Jupyter](../../../collaborators/jupyter/) for teaching us a lot about open source over the years.

