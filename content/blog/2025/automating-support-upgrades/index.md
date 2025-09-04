---
title: Solving classes of problems, rather than just an instance of a problem (with an example)
date: "2025-06-09"
category: updates
authors:
  - Yuvi Panda
tags:
  - engineering
---

## The Problem

Two of our the communities we serve ([NMFS Openscapes](https://nmfs-openscapes.github.io/) and [CryoCloud](https://book.cryointhecloud.com)) reported issues with starting GPU nodes on their hubs. Upon investigation, I discovered that the [cluster autoscaler](https://github.com/kubernetes/autoscaler) seems to not recognize that GPUs were available in the cluster at all suddenly, and hence wasn't provisioning the nodes. A restart of the cluster-autoscaler pod fixed the issue for both these communities.

## An incomplete solution

But is that the end of the story? Not if we want to provide reliable long term infrastructure to communities with minimal [toil](https://sre.google/sre-book/eliminating-toil/) on the part of 2i2c engineers!

One of the engineering principles I'm trying to have us more intentionally and structurally embody is the idea that we don't fix individual instances of problems, but **whole classes of problems, rather than just an individual instance of the problem**. Fixing the immediate issue is *not enough* - we need to understand what **class of issues** was manifesting itself in this particular fashion, and fix *that*.

## What was the **class of issues** we could fix here?

Digging in, I realized that our version of cluster-autoscaler was a little behind and not the latest. I *presumed* this was a bug in cluster-autoscaler (given a restart fixed it, implying it is a bug about state). To me, the *class of problem* here is that we were not rolling out releases to our "supporting infrastructure" fast enough. Perhaps if we were on the most recent cluster-autoscaler release, this issue would have never happened.

Additionally, this failure to scale up was reported to us by the community rather than by an automated alert. We should change that too!

## Structured solutions

We follow a two week sprint cycle, and I love the (hard won) structure it provides us. I don't want to arbitrarily start doing work that upsets prior committed work from that structure. However, we also treat support requests seriously and try to work them into the sprint. So I timeboxed myself for one hour, and saw what I could accomplish. Turns out, a lot!

1. I [upgraded all our support components](https://github.com/2i2c-org/infrastructure/pull/6183), tested them, and rolled them out to *all* our communities! This included upgrading Grafana, Prometheus, nginx-ingress as well as the cluster-autoscaler. This also restarts the cluster-autoscaler across our clusters, fixing this issue for other communities (if any had it).
2. I [re-enabled](https://github.com/2i2c-org/infrastructure/pull/6182) the automatic once a month PR for upgrading these support tasks. We had switched to doing them on a manual sprint cadence, but clearly that was not fast enough nor automated enough. We will instead work these into the sprint once the bot opens the PR. Credit to [Erik Sundell](https://github.com/consideratio) for initially setting this up
3. Create [an issue](https://github.com/2i2c-org/infrastructure/issues/6185) to track the alert creation, and put it in our sprint backlog.
4. (In an additional fifteen minute timebox) Write this blog post, to communicate out both to the affected communities and others what we have done.

By timeboxing myself, I didn't upset our sprint cadence and was able to continue doing other work I had committed to in the sprint, while also fixing this *class of issues* to the best of my ability.

## Moving forward

While we have been *implicitly* trying to solve whole classes of issues rather than individual instances of an issue as a team for a while, I want us to *explicitly* do it from now on. Communicating this out to our communities is an important part of that, as is internal team training. This blog post is the former, and we are continually working on the latter :)
