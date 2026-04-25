---
title: How regularly upgrading core infrastructure leads to upstream improvements and better infrastructure
slug: "why-upgrade-regularly"
date: "2026-04-03"
author: Yuvi Panda
categories:
  - service enhancements
tags:
  - upstream
  - devops
  - open source
---

Our collaborators at [NASA VEDA](../../../collaborators/nasa-veda/) recently asked us about the rationale behind policies for upgrading our infrastructure relatively quickly when new versions come out. Here's the explanation that we shared with them, in case it's useful for others as well.

In this case, the decision was whether to upgrade to Helm 4, and you can find our [rationale in the `/initiatives` repository](https://github.com/2i2c-org/initiatives/issues/4). Here's a brief summary from Yuvi:

Fundamentally, it helps keep moving us and the ecosystem forward, and drive improvements upstream, in both JupyterHub and Helm.

It has driven these PRs in [JupyterHub](/collaborators/jupyterhub):

- https://github.com/jupyterhub/action-k3s-helm/pull/126 (merged)
- https://github.com/jupyterhub/zero-to-jupyterhub-k8s/pull/3797 (validated, but not merged yet)

It's also driven improvements to helm itself - see this bug report that is being worked on:

- https://github.com/helm/helm/issues/31919

Upgrading helm versions can break things (and it has for some of our other communities in the past - see [this example](https://github.com/2i2c-org/infrastructure/pull/7886#issuecomment-4031310423)). So it's important we do that on a reasonable timeframe and carefully, to avoid disruptions.

We're also discovering for example that potentially the new `nginx-ingress` controller we had to move to has some issues working with older helm versions (ongoing WIP in https://github.com/2i2c-org/infrastructure/pull/7995). That feels much more tractable because we can now go 'ok, let us just apply a quick fix now, and wait for the helm 4 rollout, and try again' instead of being totally stuck.

This is similar to the other part of [/our VEDA objective] - rolling out new versions of jupyterhub. If we need to roll out security fixes, it's much easier now because we already did the hard work of being up to date:

- https://github.com/2i2c-org/infrastructure/issues/7996

This isn't the case quite yet for helm v3, as it's still supported, but it's much better to do this work earlier than wait.

If you encounter a bug in a popular open source software, often you can just 'wait' for it to be fixed. But this isn't just about time - someone somewhere has to put in the *effort* of getting it fixed, filing helpful upstream bug reports, and testing to make sure it works. This is an example of 2i2c continuing to contribute this *effort* upstream wherever we can. 
## Acknowledgements

- Thanks to [NASA VEDA](../../../collaborators/nasa-veda/) for collaborating deeply with us on infrastructure questions like this.
