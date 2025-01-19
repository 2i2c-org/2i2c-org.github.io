---
title: "An experiment to support `mybinder.org` with a single node federation member"
date: "2025-01-18"
authors: ["Yuvi Panda", "Chris Holdgraf"]
tags: [open source]
categories: [impact]
featured: false
draft: false
---

{{% callout note %}}
If you're interested in supporting `mybinder.org` with cloud resources, financial resources, or human resources, please see the [Support Binder](https://mybinder.readthedocs.io/en/latest/about/support.html) page for how you can help.
{{% /callout %}}

> `tl;dr`: The 2i2c team is launching an experiment to [run a single-node BinderHub instance at `2i2c.mybinder.org`](https://github.com/jupyterhub/mybinder.org-deploy/pull/3169/). It should be much cheaper to run than auto-scaling Kubernetes clusters, and might be a good way to support `mybinder.org` more sustainably.

[mybinder.org](https://mybinder.org) is a massive public service for creating and sharing reproducible computational environments. It is managed by the JupyterHub team and [members of the `mybinder.org` federation](https://mybinder.readthedocs.io/en/latest/about/federation.html). One of the challenges running [mybinder.org](https://mybinder.org) is identifying suppliers of cloud credits or financial resources to support the service. Two years ago, [Google stopped supporting `mybinder.org` federation with cloud credits](https://medium.com/jupyter-blog/mybinder-org-reducing-capacity-c93ccfc6413f), and last month [the federation lost more capacity](https://discourse.jupyter.org/t/mybinder-org-reduced-capacity-stability/31750). This makes the `mybinder.org` service less reliable, slower, and generally less useful to the world.

While we're thinking through long-term ways to support Binder, 2i2c also wanted to provide short-term support for the project, and experiment with cheaper models for deploying Binder's reproducible environments. Making it simpler / easier to add capacity to the `mybinder.org` federation would both improve some of Binder's short-term capacity shortage, and may also provide an easier pathway for others to support the project in the future.

So we're launching an experiment to deploy a Binder federation member via the simplest and cheapest cloud solution we could identify. The Kubernetes (and in particular, [k3s](https://k3s.io/)) ecosystem has matured, and there are some interesting cloud offerings that make a _single-node kubernetes cluster_ logistically accessible for workflows like mybinder.org. We're going to deploy a single-node Kubernetes cluster running `mybinder.org` sessions, hosted on [Hetzner](https://www.hetzner.com/cloud/)[^1].

Here's the [PR to add `2i2c.mybinder.org` to the federation](https://github.com/jupyterhub/mybinder.org-deploy/pull/3169/files#diff-bbf9217a40f20b5a3a6a15a624f4f3523bcbd3b18cd71f30f5941e34c62814ed), and below is a brief explainer for what we're trying, and why.

[^1]: There's nothing special about Hetzner, other than the fact that it provides the basic tools we need for a Binder service, and that it is cheap. If this experiment works, we'd likely be able to run federation members on other cloud providers in the same way, and because of the simpler deployment model, the number of providers we could use is likely much larger.

## What if we could run a simple BinderHub federation member for cheap?

Over the last year, two things have changed:

**k3s lets us deploy and manage a very simple Kubernetes distribution**. In the last several months, we've been experimenting and developing experience in single-node Kubernetes workflows via [k3s](https://k3s.io/) (thanks to [Carl Boettiger](https://carlboettiger.info/) for collaborating on this with us!). [k3s](https://k3s.io/) is a lightweight Kubernetes distribution that is much easier to deploy and manage. It's designed for things like edge computing and low-resource environments, and it can be deployed with a single script! We think that we've got some expertise to deploy and manage this efficiently, and want to try this out as a simpler way to deploy a BinderHub instance.

**Cheaper single-VM cloud offerings have become available**. As the cloud infrastructure space continues to grow, more service providers are competing on simplicity and price, which means there are cheaper options available. One-such provider is [Hetzner](https://hetzner.com/cloud), which provides a much cheaper single-VM option than other cloud providers. We'll get into this in the next section.  

We think that running a single-node Kubernetes instance on a Hetzner VM will be a cheap and effective way to handle a lot of `mybinder.org`'s capacity needs. Because it's a single node cluster, there is no auto-scaling (one reason it is so cheap), which reduces a lot of the complexity we'll have to manage. These are acceptable tradeoffs for a service like `mybinder.org`, which runs entirely ephemeral sessions with very limited resources and no promises about uptime, persistence, etc. As long as there's a steady stream of `mybinder.org` launches (which there has been for many years now), this node should be able to handle a constant stream of Binder launches, effecively maxing out its capacity. 

## Why would it be cheaper to run a single VM?

Normally, running Kubernetes for scalable workflows is a way to _save money_. Without scaling, you'd need to provide a VM that can _always_ handle your _maximum capacity_ needs (and pay for the costs the entire time). With Kubernetes, you can request and remove nodes to grow your capacity as-needed (and save money doing so). It looks something like this:

{{< figure src="images/scalable.excalidraw.svg" caption="The cost difference between a single large VM vs scalable nodes. Given variable usage over time, kubernetes allows you to scale your cost up and down with need, which is more efficient than paying for a single VM that can withstand your maximum capacity." >}}

However, these costs assume that you're paying for VMs / nodes on the _same provider_. There's a lot of competition in the cloud infrastructure space, and often this results in providers entering a market that compete on price.

Enter [Hetzner](https://www.hetzner.com/cloud/), a cloud provider that has been around for a while. Hetzner doesn't have the bells and whistles of hyperscaling kubernetes, but they do have _very cheap_ single VMs. Using [k3s](https://k3s.io/), we can run a lightweight, single-node Kubernetes runtime on this node, and deploy a BinderHub with the same infrastructure as any other BinderHub federation member.

Single VM nodes on Hetzner are about `4x` cheaper than their respective counterparts in Google Cloud or AWS, so in this case, it might actually be cheaper to pay for a single node that is _always_ on, but _much cheaper_. The cost picture looks something like this:

{{< figure src="images/single.excalidraw.svg" caption="If your single VM is much cheaper, it might still be the cheapest option. In the case of a Hetzner VM, it has roughly the same capacity as another cloud provider's VM, but at 1/4 of the cost." >}}

In practice, the usage needs of `mybinder.org` will still usually be larger than our single Hetzner node, but we can use _other members of the Binder federation_ to provide the scaling needed to handle that extra capacity. Something like this:

{{< figure src="images/mybinder.excalidraw.svg" caption="We can use the 2i2c.mybinder.org federation member to use a single VM to handle the _persistent_ demand of mybinder.org, and use the scalable Kubernetes nodes of other members to grow the federation's capacity up and down as needed." >}}


At least, that's how it should work in theory :-)

## Let the experiment begin

Initially this is just an experiment to see how it goes, whether it's sustainable from a cloud costs and labor standpoint, and what we can learn and share for others. Here's a rough plan:

- 2i2c sponsors a max of €350 a month (with some currency conversion noise) to fund the cloud costs of a new federation member.
- We'll provide in-kind labor to run this node, and treat it as an organizational investment in learning new Kubernetes and cloud infrastructure workflows.
- In six months, we'll evaluate how much effort it was to run this node for `mybinder.org`, whether it meaningfully helped with `mybinder.org`'s capacity, and whether it was sustainable for us from a time and labor perspective.

Our rationale is that, with a cheaper cloud provider like Hetzner, we can get a pretty large node running persistently for around €350 a month. The equivalent cost on AWS would be $1,500, and on Digital Ocean it'd be about $1,000, so this is already roughly a factor of three cheaper than the previous cheapest option.

And there may be other benefits to running BinderHub on a single VM. Doing so will likely be simpler and faster to launch sessions. Moreover, because k3s can be deployed with a single command, it means that others can build their own single-node federations members with minimal effort.

## Anybody want to fund this?

For now we're going to use funds recovered from communities in our [community hub network](/platform/), along with in-kind labor to build out this experiment. If you're interested in making open science infrastructure like Binder more scalable and sustainable, we'd love to find more resources to both sustain this node and cover more development time to run this experiment.

If you're interested in supporting `mybinder.org` with cloud resources, financial resources, or human resources, please see the [Support Binder](https://mybinder.readthedocs.io/en/latest/about/support.html) page for how you can help.

We're excited to experiment with new ways to support mybinder.org, and to identify sustainable models for deploying Binder and Jupyter infrastructure for communities in a way that could benefit the wider ecosystem as well. We'll report back on how this experiment goes!


{{% callout note %}}
If you're interested in supporting `mybinder.org` with cloud resources, financial resources, or human resources, please see the [Support Binder](https://mybinder.readthedocs.io/en/latest/about/support.html) page for how you can help.
{{% /callout %}}
