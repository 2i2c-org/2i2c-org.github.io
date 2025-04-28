---
title: "Offering Jetstream2-powered hub support at 2i2c"
date: 2025-02-12
authors:
  - Georgiana Dolocan
tags:
  - open source
categories:
  - service
featured: false
draft: false
---

When we first committed to offer Jetstream2 support at 2i2c, Jetstream2, Magnum, OpenStack, ClusterAPI were all new concepts to the team and we hadn't used them before.
And although, the initial exercise of reading about each of them independently was confusing, learning how they actually glued together was the key.
This post is about Jetstream2, 2i2c persistent hub offerings, and the learning that took place in the process.

## Context
At 2i2c, we want to be able to deploy k8s clusters on different cloud providers. And for this we use:

- `Infrastructure as code` to describe, deploy and manage the actual physical infrastructure from the cloud providers
- Cloud specific CLI to authenticate to this infrastructure
- `Helm` to deploy and manage k8s resources onto this infrastructure
- And finally `kubectl` to interact will of these k8s resources

![image](./2i2c-generic-infra.png)
(Main tools used at 2i2c to deploy and manage k8s clusters on different cloud providers)

On cloud providers like GCP, AWS, Azure, the Kubernetes support feels like an atomic feature of the cloud provider and it's something that just *is*. But on Jetstream2, k8s support is not an opaque feature anymore.

## Jetstream2 Kubernetes support stack

Jetstream2 is a few super computers that are part of the Access cyberinfrastructure. This ACCESS infrastructure groups together super computers like Jetstream2 (but not limited to it), into a mesh that creates the impression of a single, virtual system that scientists can openly access and interactively use.

It offers Infrastructure as a Service (IaaS), that allows users to deploy VMs and manage environments dynamically. And the piece that enables this Infrastructure as a Service feature is Openstack.

### OpenStack and Magnum

OpenStack is an open source platform made of multiple projects that help build and manage both private and public cloud infrastructure.

For our use-case, one of the most relevant Openstack sub-project is Magnum. Magnum offers container orchestration engines for deploying and managing containers, like Kubernetes, but not limited to it.

Initially, Kubernetes support was provided through something called a HEAT driver. However that has proven harder to manage, and maintain and was extremely hard to upgrade a cluster. So, they’ve migrated towards a new driver called Cluster API magnum driver, which offers a more native k8s integration.

### Cluster API and CAPI helm driver
CAPI itself is k8s project that allows declaring k8s clusters in an easy way.

The helm driver on the other hand is what acts like a bridge between OpenStack’s Magnum and Kubernetes’ Cluster API (CAPI). It’s main goal is to to manage the lifecycle (create, scale, upgrade, destroy) of Kubernetes-conformant clusters using a declarative API.

In order to do this, Cluster API provides an API for being able to manage the various components of a Kubernetes cluster. This conceptually looks like a Kubernetes cluster managing other Kubernetes clusters; the former, named the ‘CAPI management cluster’, is the one providing the API for managing the latter workload clusters.

### Decomposing the previous atomic feature

![image](./Jetstream2-and-tent.png)
(Comparison between Jetstream2 and other cloud providers when it comes to k8s support)

Magnum is part of the Openstack tent and it’s the first layer on top of Jetstream2 towards achieving k8s support.

The CAPI helm driver is what’s offering CAPI support. This is the last piece that’s needed to link a k8s cluster down to the hardware where it’s deployed, on Jetstream2.

## Challenges

The Jetstream2-OpenStack stack is not a simple one. It’s a complex stack of technologies and each of the connection points can be challenging to debug and fix when something doesn't work. Especially when you are one of the first ones that pilots this new magnum driver setup.

So, it was expected that we faced some issues along the way. However, we were able to go around them and add Jetstream2 to our service menu.


- We have to create terraform resource in sequence which takes longer because of a race condition that makes concurrent nodegroups creation requests to fail
- The role and labels of the nodegroups don't get propagated to the actual nodes, so we cannot put our own labels on nodes at once
- The node count and min node count cannot be set to 0 and each nodegroup has to have at least 1 node, which is not cost efficient
- A default-worker is created apart from the default-controlplane nodegroup is created and we cannot delete it due to the same issue as in 2.
- Latest CAPI helm chart version causes autoscaling to stop working in a persistent hub setup, so we had to downgrade it to a previous version

## Conclusion

Leaving the challenges apart, the experience was a nice one and the outcome was positive -> 2i2c is now able to deploy both mybinder.org-like hubs as well as persistent storage hubs on Jetstream2 hardware, from the same cloud-agnostic infrastructure.

The biggest plus, which is the people. We got support from Julian along the way which was extremely useful. Also, going thought the Jetstream2 support process was also a pleasant experience because they were super prompt in answering and they were very nice.

Jetstream2 has a big plus over the other cloud providers which it’s openness thought the ACCESS program. This is something very handy to researchers and less costly than other cloud provides. Us being able to offer hubs though this ACCESS program makes things more accessible to more researchers and more cost efficient. 

Higher complexity comes also with more control over the infrastructure which has its advantages. But we’re not yet there to enjoy them, especially since we want this uniformization of providers to one infrasdtructure managing multiple cloud providers.

And last but mot least, even though I felt frustrated during while adding the jetstream2 support, at the same time I enjoyed being challenged like this. And this learning journey was a great opportunity to grow in a practical way.



