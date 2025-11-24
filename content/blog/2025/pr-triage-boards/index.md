---
title: "Yuvi on scaling maintainer intuition to facilitate PR review with PR triage boards"
slug: "pr-triage-boards"
date: "2025-11-19"
categories:
- upstream-impact
tags:
- open source
- community
- learning
featured: false
---

Yuvi has a recent post on the [Jupyter blog](https://jupyter.org) on how his "maintainer intuition" about reviewable pull requests grew into the open-source [`pr-triage-board-bot`](https://github.com/jupyter/pr-triage-board-bot), a reusable workflow that keeps GitHub Project boards curated for the JupyterHub, JupyterLab, and GeoJupyter communities. [Foundational contributions](../foundational-contributions/) are rellay important to 2i2c. This is a great example of building clever technical systems that help maintainers prioritize the social work of facilitating contributions to keep ecosystems healthy.

{{< figure src="featured.png" title="The [JupyterHub PR Triage board](https://github.com/orgs/jupyterhub/projects/4/views/9)." >}}

Our favorite quote shares the vibe and cultural principles that drive this effort:

{{< pull-quote cite="[Yuvi](../../../authors/yuvi-panda/)">}}
If the author of the PR is a newish contributor, I want to encourage them to stick around by being responsive to their gift. All PRs are gifts that we may or may not choose to accept, but should do so with grace.
{{< /pull-quote >}}

Yuvi frames the problem here:

> Reviewing PRs is a critical way that maintainers keep an open source project moving forward, but identifying PRs that can productively be merged is hard.

And notes that _human scalability_ is often a big bottleneck:

> One key bottleneck we identified in the process was Step 2. In particular, I was relying on my maintainer intuition to pick a single PR that I believe can be merged, so others in the team can do review work. I started exploring what this intuition is, and if it can be scaled.

Here's his list of "intuitions" that he uses to choose PRs to work on:

> 1. PRs that aren’t too big, and are a reasonable size that can be merged within a 2 week window
> 1. CI tests passing, so at least our automated checks haven’t caught any issues with it
Features or bug fixes that I believe add value to the project and move us in the right direction towards being able to support our users as they need (this is the hardest!)
> 1. If the author of the PR is a newish contributor, as I want to encourage them to stick around by being responsive to their gift. All PRs are gifts that we may or may not choose to accept, but should do so with grace.
> 1. How long ago the PR was opened. There is such a big difference between a response to your PR 2 days after you make it vs 2 months vs 2 years. I prioritized newer PRs.
> 1. What kind of contribution is it primarily? Different engineers on our team have different skillsets (JS, Python, etc) and I wanted to match the PR to what the engineer preferred code reviewing.

And the board essentially tries to capture many of these intuitions by signal-boosting them in one place:

> we can roughly say ‘Pick a PR that looks good to you from the top of the “First Time Contributor” or “Seasoned Contributor” list’, and that relieves me from being the bottleneck quite a bit.

Read more in the original article: [Scaling "Maintainer Intuition" with Pull Request Triage Boards](https://blog.jupyter.org/scaling-maintainer-intuition-with-pull-request-triage-boards-779f2387498b).

## Acknowledgements

- [Project Jupyter](../../../collaborators/jupyter/) for trusting us to incubate and now donate the bot code to the broader ecosystem.
- [JupyterHub](../../../collaborators/jupyterhub/) and [GeoJupyter](../../../collaborators/geojupyter/) contributors who tested the triage views and fed real maintainer workflows back into the design.
- [Jason Grout](https://github.com/jasongrout), [Raniere Silva](https://github.com/rgaiacs), and [Matt Fisher](https://github.com/mfisher87) for spotting the experiment early and helping it land across multiple orgs.
