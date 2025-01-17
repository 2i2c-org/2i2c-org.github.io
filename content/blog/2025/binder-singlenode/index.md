---
title: "Supporting mybinder.org with a single node federation member"
date: "2025-01-18"
authors: ["Yuvi Panda", "Chris Holdgraf"]
tags: [open source]
categories: [impact]
featured: false
draft: false
---

{{% callout note %}}
If you're interested in supporting mybinder.org with cloud resources, financial resources, or human resources, please see the [Support Binder](https://mybinder.readthedocs.io/en/latest/about/support.html) page for how you can help.
{{% /callout %}}

[mybinder.org](https://mybinder.org) is a massive public service for creating and sharing reproducible computational environments. It is managed by the JupyterHub team and [members of the mybinder.org federation](https://mybinder.readthedocs.io/en/latest/about/federation.html). One of the challenges running [mybinder.org](https://mybinder.org) is identifying suppliers of cloud credits or financial resources to support the service. Two years ago, [Google stopped supporting mybinder.org federation with cloud credits](https://medium.com/jupyter-blog/mybinder-org-reducing-capacity-c93ccfc6413f), and last month [the federation lost more capacity](https://discourse.jupyter.org/t/mybinder-org-reduced-capacity-stability/31750).

While we're thinking through long-term ways to support Binder, 2i2c also wanted to provide short-term support for the project, and experiment with cheaper models for deploying Binder's reproducible environments. Making it simpler / easier to add capacity to the mybinder.org federation would both improve some of Binder's short-term capacity shortage, and may also provide an easier pathway for others to support the project in the future.

So we're launching an experiment to deploy a Binder federation member via the simplest and cheapest cloud solution we could identify. The Kubernetes (and in particular, [k3s](https://k3s.io/)) ecosystem has matured, and there are some interesting cloud offerings that make a _single-node kubernetes cluster_ logistically accessible for workflows like mybinder.org. We're going to deploy a single-node Kubernetes cluster running mybinder.org sessions, hosted on [Hetzner](https://www.hetzner.com/cloud/).

Initially this is just an experiment to see how it goes, whether it's sustainable from a cloud costs and labor standpoint, and what we can learn and share for others. Here's a rough plan:

- 2i2c sponsors a max of €300 a month (with some currency conversion noise) to fund the cloud costs of a new federation member.
- We'll provide in-kind labor to run this node, and treat it as an organizational investment in learning new Kubernetes and cloud infrastructure workflows.
- In six months, se'll evaluate how much effort it was to run this node for mybinder.org, whether it meaningfully helped with mybinder's capacity, and whether it was sustainable for us from a time and labor perspective.

Our rationale is that, with a cheaper cloud provider like Hetzner, we can get a pretty large node running persistently for around €300 a month. The equivalent cost on AWS would be $1,500, and on Digital Ocean it'd be about $1,000, so this is already roughly a factor of three cheaper than the previous cheapest option. In addition, we've been developing some experience running single-node Kubernetes workflows via [k3s](https://k3s.io/) and a collaboration with [Carl Boettiger](https://carlboettiger.info/), so we think that we've got some expertise to deploy and manage this efficiently. Finally, because it's a single node cluster, there is no auto-scaling (one reason it is so cheap), which reduces a lot of the complexity we'll have to manage. These are acceptable tradeoffs for a service like mybinder.org, which runs entirely ephemeral sessions with very limited resources and no promises about uptime, persistence, etc.

We're excited to experiment with new ways to support mybinder.org, and to identify sustainable models for deploying Binder and Jupyter infrastructure for communities in a way that could benefit the wider ecosystem as well. We'll report back on how this experiment goes!


{{% callout note %}}
If you're interested in supporting mybinder.org with cloud resources, financial resources, or human resources, please see the [Support Binder](https://mybinder.readthedocs.io/en/latest/about/support.html) page for how you can help.
{{% /callout %}}

