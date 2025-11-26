---
title: 2i2c joins the mybinder.org federation with a cheaper and faster way to deploy Binderhub
slug: "binder-singlenode"
date: 2025-01-29
authors:
  - Yuvi Panda
  - Chris Holdgraf
tags:
  - open-source
categories:
  - upstream-impact
featured: false
draft: false
---

{{% callout note %}}
If you're interested in supporting `mybinder.org` with cloud resources, financial resources, or human resources, please see the [Support Binder](https://mybinder.readthedocs.io/en/latest/about/support.html) page for how you can help.
{{% /callout %}}

> `tl;dr`: The 2i2c team is joining the mybinder.org federation with a [single-node BinderHub instance at `2i2c.mybinder.org`](https://github.com/jupyterhub/mybinder.org-deploy/pull/3169/). It should be much cheaper to run than auto-scaling Kubernetes clusters, and might be a good way to support `mybinder.org` more sustainably. For questions or comments, join [this Jupyter Zulip thread](https://jupyter.zulipchat.com/#narrow/channel/469744-jupyterhub/topic/ANN.3A.202i2c.20joins.20mybinder.2Eorg.20federation.20with.20new.20strategy/near/496811301).

[`mybinder.org`](https://mybinder.org) is a massive public service for creating and sharing reproducible computational environments. It is managed by the JupyterHub team and [members of the `mybinder.org` federation](https://mybinder.readthedocs.io/en/latest/about/federation.html). One challenge in running [`mybinder.org`](https://mybinder.org) is identifying cloud credits or financial resources to support the cloud infrastructure that runs the service. Two years ago, [Google stopped supporting `mybinder.org` federation with cloud credits](https://medium.com/jupyter-blog/mybinder-org-reducing-capacity-c93ccfc6413f), and last month [the federation lost more capacity](https://discourse.jupyter.org/t/mybinder-org-reduced-capacity-stability/31750), leaving only [GESIS](https://www.gesis.org/en/home) and [OVH](https://us.ovhcloud.com/) as remaining federation members[^thanks]. This makes `mybinder.org` less reliable, slower, and generally less useful to the world.

[^thanks]: Many thanks to [GESIS](https://www.gesis.org/en/home) and [OVH](https://us.ovhcloud.com/) for their continued support of mybinder.org, your contributions to keeping this service running are critical!

The landscape of cloud infrastructure technology and services has changed considerably, and we think that there's a way to deploy BinderHub instances with lower costs and less complexity. We've accomplished this by deploying a **single-node Kubernetes cluster** on a VM provider that is much cheaper, now running at `2i2c.mybinder.org`. This both relieves Binder's short-term capacity shortage and may provide an easier pathway for others to support the project in the future.

Below, we'll describe what has changed to enable this, what we're deploying, and what the impact should be.

## Cloud infrastructure has become cheaper and more commodified

A key theory of mybinder.org (and 2i2c) is that commercial cloud infrastructure will be commidified over time -- what begins as cutting-edge functionality will become commonplace and offered across all cloud providers. As a result, costs will go down over time. Abstractions like [Kubernetes](https://kubernetes.io/) will allow you to easily migrate workflows and infrastructure between cloud providers. As a result, you'll be able to easily _follow those costs_ where there are better options. That's essentially what is happening here.

There are two key changes that make it much easier to deploy a BinderHub instance at a fraction of the cost:

First, **Kubernetes has matured and become easier to deploy**. When mybinder.org started, it was using the cutting-edge of Kubernetes functionality. This meant that we needed to use cloud providers that provided a _managed Kubernetes service_ to deal with this complexity. A managed Kubernetes offering tends to be expensive, offered by only a few cloud providers, and thus raises costs across-the-board for the provider that offers it.

However, this was almost a decade ago, and Kubernetes has become both more functional and more stable. There are now many more ways of running Kubernetes, especially for simpler workflows that don't require autoscaling. In the last several months, we've been experimenting with **single-node Kubernetes workflows** via [K3s](https://k3s.io/)[^carl]. [K3s](https://k3s.io/) is a lightweight Kubernetes distribution that is much easier to deploy and manage. It's designed for things like edge computing and low-resource environments, and it can be deployed with a single script!

[^carl]: thanks to [Carl Boettiger](https://carlboettiger.info/) for collaborating on this with us!
   
By running a Kubernetes cluster on a single node, we don't need a "managed Kubernetes service", which means **we can choose from a much larger pool of infrastructure / cloud providers**. If all we need is a running VM, this is something the tech industry has been doing for decades.

Second, **Managed Object Storage services have more open source options, and are more commodified and cheaper**. In addition to Kubernetes, the other thing that BinderHub needs is a way to store and retrieve images for the environments that it builds. This also used to be a fairly complex problem, and thus required managed solutions from cloud providers that charged a premium for their service. However, a number of open source object storage solutions have emerged and made it much easier for providers to support this workflow.[^minio]. Because these are open source, infrastructure providers can provide managed object storage at a fraction of the cost.

[^minio]: One example is [MinIO](https://min.io/), which is used by [Hetzner](https://hetzner.com/cloud) to provide managed object storage for their single-node VMs.

Because of these two things, we've learned that we can run a BinderHub instance on a single VM from a much larger pool of infrastructure providers. This means **we should be able to run BinderHub instances at a fraction of the cost**.[^1] 

[^1]: For example, [Hetzner](https://hetzner.com/cloud) provides a single-VM option with managed object storage that is roughly 25% of the cost of other cloud providers that also offer autoscaling Kubernetes services. There are many other infrastructure providers who could be used in this way.

## Deploying BinderHub on a single-node VM is cheaper and simpler

Last week, we [deployed 2i2c.mybinder.org](https://github.com/jupyterhub/mybinder.org-deploy/pull/3169), a single-node Kubernetes instance on [Hetzner](https://hetzner.com/cloud) cloud using [K3s](https://k3s.io/). This will run on a single node VM, with a Kubernetes instance that is entirely managed by us, and with managed object storage from Hetzner. Compared to other cloud providers, it is **around 5x cheaper per month**.

{{< figure src="featured.png" caption="Comparison of rough monthly costs across different cloud providers for similar VM instances. These are rough estimates based on cloud provider pricing pages for an on-demand VM with around 190GB RAM. Pricing pages: [Hetzner Cloud](https://www.hetzner.com/cloud) ~$300, [Microsoft Azure](https://azure.com/e/da6294b08dfa49639f74caad1630bbe4) ~$1,300, [Google Cloud Platform](https://cloud.google.com/products/calculator?hl=en&dl=CjhDaVJrWlRBeVpEUmpNQzAwTVRrMkxUUmtNalV0T0RnNU5pMHpaV1EyWlRnMFpHSXpPVE1RQVE9PRAIGiRDRTQ3QTYwQy1DNUM5LTQ3QkQtQTM3MS05MjBCQjU1QjNGRjg) ~$1,500, [Amazon Web Services](https://calculator.aws/#/estimate?id=a3bddb8bdbfa2058b941b669e408141e7fd18da4) ~$1,600." >}}

<!-- Machines for the figure above: 

  Hetzner: CCX63
  Amazon Web Services: m8g.12xlarge
  Google Cloud Platform: n2-standard-48
  Microsoft Azure: D48as v5
-->

Running a single-node Kubernetes instance will be a cheap and effective way to handle a lot of `mybinder.org`'s capacity needs. Because it's a single node cluster, there is no auto-scaling (one reason it is so cheap), which reduces a lot of the complexity we'll have to manage. These are acceptable tradeoffs for a service like `mybinder.org`, which runs entirely ephemeral sessions with very limited resources and no promises about uptime, persistence, etc.

You might be wondering: "I thought Kubernetes was supposed to _save money_." Normally, running Kubernetes for scalable workflows does save costs because you can scale infrastructure to match your capacity needs. Without scaling, you'd need to provide a VM that can _always_ handle your _maximum capacity_ needs (and pay for the costs the entire time). With Kubernetes, you can request and remove nodes to grow your capacity as-needed (and save money doing so). It looks something like this:

{{< figure src="images/scalable.excalidraw.svg" caption="The cost difference between a single large VM vs scalable nodes. Given variable usage over time, kubernetes allows you to scale your cost up and down with need, which is more efficient than paying for a single VM that can withstand your maximum capacity." >}}

However, there is a built-in cost you pay when you use a service that provides managed Kubernetes. **Managed Kubernetes services are complex and expensive**, and this is reflected across-the-board in the provider's costs. What if we could achieve the same outcome with a much simpler cloud offering like a single VM?

We did a bit of research and discovered that the Kubernetes and object storage landscape has indeed evolved significantly since the early days of mybinder.org. For example, [Hetzner](https://www.hetzner.com/cloud/) is a cloud provider that has been around for a long time. It has single-node VMs that are about `4x` cheaper than their counterparts in Google Cloud or AWS, and provides managed object storage that uses [MinIO](https://min.io/) in a cost-effective way. Using [K3s](https://k3s.io/), we can run a lightweight, single-node Kubernetes runtime on this node, and deploy a BinderHub with the same infrastructure as any other BinderHub federation member. 

By our estimate, we could fit around **400 simultaneous sessions** on `mybinder.org` (because each session uses very few cloud resources). This is already the majority of mybinder.org's capacity needs, and at a much lower cost than using a scalable Kubernetes cluster. The cost picture looks something like this:

{{< figure src="images/single.excalidraw.svg" caption="If your single VM is much cheaper, it might still be the cheapest option. In the case of a Hetzner VM, it has roughly the same capacity as another cloud provider's VM, but at 1/4 of the cost." >}}

## 2i2c.mybinder.org now serves 70% of the mybinder.org federation

About a week ago, we launched [2i2c.mybinder.org](https://2i2c.mybinder.org) running via the methodology we described above. We intended to run this as a longer experiment, but believe that it has already proven useful enough to consider "ready for production". We recently [increased 2i2c.mybinder.org's load to 70%](https://github.com/jupyterhub/mybinder.org-deploy/pull/3196) and will continue to monitor its performance over time. Here's a plot of where each mybinder.org session has been run over the past ten days - you can see the moment where we turn on `2i2c.mybinder.org` to the left:

{{< figure src="images/grafana.png" caption="Sessions launched on mybinder.org's federation over the past ten days. The yellow area represents sessions run on `2i2c.mybinder.org`. They now make up the majority of launches on mybinder.org. Prior to this, `gesis.mybinder.org` was the only remaining federation member." >}}

For now, 2i2c is sponsoring a max of €350 a month (with some currency conversion noise) to run this service. We'll provide in-kind labor to run this node, and treat it as an organizational investment in supporting open science, as well as learning new Kubernetes and cloud infrastructure workflows. We're going to use funds recovered from communities in our [community hub network](/platform/), along with in-kind labor to build out this experiment.

In six months, we'll evaluate how much effort it was to run this node for `mybinder.org`, whether it meaningfully helped with `mybinder.org`'s capacity, and whether it was sustainable for us from a time and labor perspective.

## Others can join the mybinder.org federation using this approach as well

We think that developing this single-node BinderHub workflow will make it much easier for others to join the mybinder.org federation, because it lowers the infrastructure and skills complexity needed to join. [Here is a brief guide we've written for deploying a BinderHub with K3s](https://github.com/jupyterhub/mybinder.org-deploy/blob/72a1a34509e2c43aec788f602250c58d9d849a13/docs/source/deployment/k3s.md). We are helping a few interested organizations deploy their own BinderHubs in this way in order to validate the idea, and are hopeful that this makes it much easier to grow mybinder.org's capacity via new federation members.[^2]

[^2]: We're also experimenting with a few other ways to reduce the complexity and costs of running a BinderHub even further, but will have more on that later as we learn more :-).

We're excited to experiment with new ways to support `mybinder.org`. We think this is an excellent example of how open standards and technology lead to cloud workflows with lower costs and more flexibility. We also think it's a good example of how it is valuable to have organizations aligned with open science (like 2i2c!) acting in this space. If you have any questions or comments, please join [this Jupyter Zulip thread](https://jupyter.zulipchat.com/#narrow/channel/469744-jupyterhub/topic/ANN.3A.202i2c.20joins.20mybinder.2Eorg.20federation.20with.20new.20strategy/near/496811301)

## Anybody want to fund this?

If you're interested in making open science infrastructure like Binder more scalable and sustainable, we'd love to find more resources to both sustain this node and cover more development time to run this experiment. [Feel free to reach out here](mailto:hello@2i2c.org).

If you have access to VMs and object storage, and are interested in running a mybinder.org federation member using the methods described here, check out [our brief guide for deploying a BinderHub with K3s](https://github.com/jupyterhub/mybinder.org-deploy/blob/72a1a34509e2c43aec788f602250c58d9d849a13/docs/source/deployment/k3s.md).

If you're generally interested in supporting `mybinder.org` with cloud resources, financial resources, or human resources, please see the [Support Binder](https://mybinder.readthedocs.io/en/latest/about/support.html) page for how you can help.

{{% callout note %}}
If you're interested in supporting `mybinder.org` with cloud resources, financial resources, or human resources, please see the [Support Binder](https://mybinder.readthedocs.io/en/latest/about/support.html) page for how you can help.
{{% /callout %}}

## Acknowledgements

- Thanks to the [JupyterHub community](../../../collaborators/jupyterhub/) for helping us set up this new node.
- Thanks to [our member communities](../../../members/) whose fees currently support this work.
