---
title: Combating tcp scanning on mybinder.org with the tcpflowkiller
slug: "mybinder-antiabuse-scanning"
date: 2025-10-08
authors:
  - Yuvi Panda
categories:
  - upstream-impact
tags:
  - open-source
  - binder
  - reliability
---

We've deployed a new tool to `mybinder.org` that automatically detects and stops port scanning activity, helping us maintain service reliability while being responsible citizens of the internet.

Port scanning is a common part of network-based exploits, and many server hosts prohibit this activity (including Hetzner, where the 2i2c `mybinder.org` infrastructure lives). We developed a little tool called [tcpflowkiller](https://github.com/cryptnono/cryptnono/pull/46) as part of the [cryptnono](https://github.com/cryptnono/cryptnono) project (our anti-abuse set of tools for hosted JupyterHub and Binder infrastructure) to automatically kill processes that exhibit port scanning behavior. This reduces the likelihood of triggering our server host's abuse policies and helps keep `mybinder.org` running reliably.

## Why this matters

As providers of public compute, it's our responsibility to make sure people can't use our infrastructure to abuse others. This is part of being responsible citizens of the internet. It also saves us time in dealing with outages because cloud providers (understandably) block access when they suspect there is abuse.

Hetzner and similar hosts have many benefits (including [significant cost savings](../binder-singlenode/)), and tools like tcpflowkiller help keep hubs and binders running smoothly on such hosts, which have different abuse policies than the big commercial cloud providers.

AWS and other cloud providers have proprietary ways to combat abuse (like [AWS GuardDuty](https://docs.aws.amazon.com/guardduty/latest/ug/what-is-guardduty.html)). We could have spent our time investing in developing rules there. Instead, contributing to cryptnono helps provide the same set of features in a cloud-agnostic way, in line with [our principles](https://2i2c.org/open-practices/) of supporting open infrastructure that gives communities control over their infrastructure.

This tool [has now been deployed to mybinder.org](https://github.com/jupyterhub/mybinder.org-deploy/pull/3436), and we'll monitor its effectiveness over time. We may roll this out to 2i2c public BinderHubs in the future based on patterns we observe.

## Learn more

- [tcpflowkiller pull request](https://github.com/cryptnono/cryptnono/pull/46)
- [mybinder.org deployment](https://github.com/jupyterhub/mybinder.org-deploy/pull/3436)
- [Port scanning on Wikipedia](https://en.wikipedia.org/wiki/Port_scanner)

## Acknowledgements

- Thanks to [GESIS](../../../collaborators/gesis/) for their continued support of `mybinder.org` and to [Raniere Silva](https://github.com/rgaiacs) for collaborating on this deployment with us.
