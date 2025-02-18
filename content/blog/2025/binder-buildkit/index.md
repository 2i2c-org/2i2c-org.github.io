---
title: Simplifying and speeding up Binder builds with BuildKit
date: 2025-02-18
authors:
  - Yuvi Panda
  - Chris Holdgraf
tags:
  - open source
category:
  - impact
--- 

The Binder Project allows users to build reproducible, sharable environments for interactive computing. To accomplish this, Binder uses a tool called [repo2docker](https://repo2docker.readthedocs.io/) to generate an executable Docker image using the [Reproducible Execution Environment Specification](https://repo2docker.readthedocs.io/en/latest/specification.html).

The first time a repository is launched on Binder, repo2docker must build the reproducible environment for it. This process can take a long time because of all the dependencies that need to be installed and turned into the image. As a result, Binder launches can feel slow and clunky, which is a poor UX for workflows that are designed around quick interactive sessions.

repo2docker was built several years ago, and followed patterns that were common place at the time. However, in the past few years the Docker community has made significant advances in optimizing the image building process. One-such improvement is the creation of [BuildKit](https://docs.docker.com/build/buildkit/), a replacement for Docker's historical build system that is much more sophisticated. BuildKit is built by the Docker community, and was recently made the default option for Docker. However, repo2docker hasn't leveraged these improvements because it was still using the original Docker Build system.

So, we've decided to spend a few cycles modernizing repo2docker's image building logic by using the more modern BuildKit API (via 'docker buildx build'). This allows for optimizations like build parallelization, better build caching, and supporting some `Dockerfile` features that Binder didn't support earlier (particularly, `COPY --chown`). It also lays a foundation for significantly simplifying the repo2docker build infrastructure and leveraging more of BuildKit's paralellization functionality. For eample, we'd like to [leverage BuildKit's Kubernetes driver](https://docs.docker.com/build/builders/drivers/kubernetes/) which distributes builds much more efficiently and in parallel.

Authors of Binder repositories won't need to take any action[^1], and they'll simply notice that mybinder.org (and any other community-run BinderHub instance) will be a bit snappier at building images.

If you'd like to learn more about the changes that enabled this, [check out this mybinder.org pull request](https://github.com/jupyterhub/mybinder.org-deploy/pull/3225) which has links to the repo2docker pull requests that added this functionality. We're excited to support the Binder project, and are hopeful that this makes the experience of using mybinder.org and community Binders a little bit better.

[^1] Unless they were relying on undocumented implementation details of the old builder - in particular, the presence of a `/.dockerenv` file to detect if you are running in repo2docker https://github.com/scikit-learn/scikit-learn/pull/30835 has an example.