---
title: "Community learning: Hub config to pass oauth tokens into user environments"
slug: "communities-learning-from-one-another"
date: 2025-11-06
authors:
  - Chris Holdgraf
categories:
  - community-impact
tags:
  - open-source
  - community
  - learning
  - jupyterhub
---

One of our favorite things to see: communities learning from and building on each other's work!

[MAAP](https://ops.maap-project.org/) recently [contributed infrastructure configuration](https://github.com/2i2c-org/infrastructure/pull/7068) inspired by [EarthScope's approach](https://github.com/2i2c-org/infrastructure/blob/0046e14a68d7af9e353c494ee6ad39beb0ce970a/config/clusters/earthscope/common.values.yaml#L29) to handling authentication tokens. Both communities need to pass OAuth tokens into user environments so their SDKs can access protected data - and MAAP adapted EarthScope's pattern to fit their needs.

This is the kind of peer-to-peer knowledge sharing we hope to foster with our [open infrastructure model](https://github.com/2i2c-org/infrastructure). When infrastructure is open and communities can see each other's solutions, they can adapt and build on proven approaches rather than starting from scratch.

## Learn more

- [MAAP's PR](https://github.com/2i2c-org/infrastructure/pull/7068) adapting the configuration
- [EarthScope's original config](https://github.com/2i2c-org/infrastructure/blob/0046e14a68d7af9e353c494ee6ad39beb0ce970a/config/clusters/earthscope/common.values.yaml#L29)
- [Our infrastructure repository](https://github.com/2i2c-org/infrastructure) where all community configurations live

## Acknowledgments

- [MAAP team](https://ops.maap-project.org/) for adapting and contributing this configuration
- [EarthScope Consortium](/collaborators/earthscope/) for the original implementation
