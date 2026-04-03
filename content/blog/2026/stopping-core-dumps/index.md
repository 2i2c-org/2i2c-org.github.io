---
title: Benefitting all our communities
slug: "benefit-all-communities"
date: 2026-03-11
categories:
  - upstream impact
tags:
  - open source
  - jupyterhub
  - community
---

Scott Henderson [noticed](https://github.com/2i2c-org/infrastructure/issues/3321) [core dump files](https://en.wikipedia.org/wiki/Core_dump) appearing on home directories
and taking up space when a program crashes in one of the hubs we run for the [CryoCloud community](https://cryointhecloud.com/).
While core dump files can be useful in some circumstances, they are almost never useful on a hub. They can also
be *huge*, costing real cloud spend. Ian Caroll [noticed
this](https://github.com/2i2c-org/infrastructure/issues/3321#issuecomment-3191672965)
happening again on both the CryoCloud and the
[openscapes](https://openscapes.org/) hubs as well. Ian also [pointed out a fix](https://github.com/2i2c-org/infrastructure/issues/3321#issuecomment-3191672965),
but it would need to be adapted to run on kubernetes. 2i2c is a small organization, and at that moment
[we did not have the capacity](https://github.com/2i2c-org/infrastructure/issues/3321#issuecomment-3514101956)
to do that work.

Separately, [Alex Mandel](http://github.com/wildintellect) from [Development Seed](https://developmentseed.org/),
working for the NASA VEDA project *also* noticed this in their hubs in late 2025, as part of their
efforts to audit home directory usage and control costs. They were able to build on top of the work from the other
communities we supported, and with help from [Chuck Daniels](https://github.com/chuckwondo) and [Tarashish Mishra](https://developmentseed.org/team/tarashish-mishra/) (also from Development Seed), they were able to:

1. Clean up all core dumps in their communities, and reclaim 171G of space
2. [Operationalize](https://github.com/2i2c-org/infrastructure/pull/7588) the kubernetes setup needed to disable core
   dumps on an ongoing basis.

We were able to roll this out to all our communities, and saved communities [a lot of space](https://github.com/2i2c-org/infrastructure/issues/3321#issuecomment-4028227976). In particular,
the CryoCloud community was saved 717G, which translates to a lot of money! Also poignant that they were the first community to
notice the problem.

We're also working on contributing this upstream to zero to jupyterhub, as this is valuble to everyone running
a JupyterHub, not just us.

## 2i2c's Value

This is a loop of value that we intentionally try to encourage and bring about at 2i2c:

1. Community A notices a problem for them
2. We recognize this is a general problem affecting a lot of communities, but just observed in Community A
3. We informally put together a collection of communities that can contribute different things to solve the problem - observations,
   engineering time, validation, etc.
4. We solve the problem for *everyone*, including the folks who didn't know they had a problem!

This is a generalization of the overall loop of open source software adding value to the world, and I'm excited to see
it play out in a way that's organizationally supported by 2i2c.