---
title: A guardrail based approach to cloud cost management
date: "2024-11-15"
banner:
  image: "featured.png"
authors: ["Yuvi Panda"]
tags: []
categories: [organization]
featured: false
draft: false
---

> It's called 'the AWS Console' because you need consoling after you look at your AWS Bill

-- Ancient Proverb

Shock cloud bills are one of the biggest fears of people trying to do science in the cloud. This is a very legitimate fear! Cloud bills are based on usage, but what counts as 'usage' is not necessarily transparent to science users or admins. The trope of _'our student did not realize what they were doing and was costing the group 6,000$ a month'_ is a realistic scenario and a systemic issue to be overcome (rather than the fault of the student). Directly giving scientists access to commercial cloud has proven to be an administrative burden that requires working knowledge of APIs and web services. For example cloud providers require a credit card upfront for covering charges: this exposes the bill payer to runaway costs, may not comply with institutional policies, and may unfairly disadvantage scientists without access to a business credit card.

## Control usage to control costs

Cloud bills are *based on usage*, and embracing this relationship is the key to controlling cost on the cloud. Control how much your users use, and you control how much money you spend!

JupyterHubs are a flexible way to give users access to compute in a user friendly and controlled fashion. Users can get their science done without deciphering AWS IAM permission errors or firewall misconfigurations that allow a cryptomining attack, and administrators can implement guardrails that strikes the right balance for their users.

In our experience, users do *not* want to accidentally cause cost overruns. Guardrails, carrots, and then sticks - in that order - are needed to encourage best practices.

In this blog post, we will describe the philosophy 2i2c is approaching this problem in a way that considers user friendliness together with financial constraints using a guardrail based approach.

## What costs money?

Given our experience serving many kinds of scientific and educational communities across all major cloud providers, we have documented in detail [What exactly do cloud providers charge us for?](https://infrastructure.2i2c.org/topic/billing/chargeable-resources/). For the purpose of this blog post, we will tackle the following three topics:

1. Storage
2. Compute
3. Network

These are the primary factors to manage for successfully controlling the bulk of cloud costs.

### Storage

Home directories are familiar to most users, and many tools rely on them to function. Users store code, notebooks, configurations, etc in this location. While object storage should be used to store intermediate and final data outputs that are large in size, many tools (and users!) can be cumbersome. Home directories are a vital structure to meet users where they are in terms of organizing their workflows.

Controlling cost here is conceptually simple - each user recieves a quota for their home directory and can not exceed that limit. The problem is that none of the 'managed' network file systems (NFS) on the major cloud providers can enforce this on a user-level. The representative approach of giving each user their own disk with a quota ends up being far more expensive than using a shared NFS store for all users on a hub.

What do we do here? 2i2c deploys JupyterHubs with a shared NFS store for all user home direcotories and complements this with a two-pronged approach:

1. **Reporting**, with a [Prometheus exporter](https://github.com/yuvipanda/prometheus-dirsize-exporter) and a [Grafana dashboard](https://github.com/jupyterhub/grafana-dashboards) allows admins to identify and notify users who are using a substantial amount of home directory storage. Automatic alerts can also be set up via Grafana. See our [Service Guide](https://docs.2i2c.org/admin/howto/monitoring/) on Usage Monitoring for more details.
2. **Development**, by expanding on our partnership with Development Seed and NASA VEDA, we are building a mechanism to [enforce quotas](https://github.com/NASA-IMPACT/veda-jupyterhub/issues/41). We will move away from cloud managed NFS implementations, but still be able to have a single disk shared across all users on a hub. Best of both worlds, with a slight increase in complexity that is worth the tradeoff.

When complete, this will allow us to make storage costs for home directories *deterministic* and *fair*!

We also work with educating folks in moving away from using home directories for data storage and towards using object stores. There is a lot of inertia here, but also a lot of excitement in the use cases that object stores enable, such as adjacency to data archives.

### Compute

Users don't always need super heavy compute to do their work. However, ask a scientist 'how much RAM do you need to do that?' and you are more often than not likely to get blank expressions in return. Resource usage is an accidental complexity that does not directly relate to the science being done, and users often need help with picking and choosing resources appropriate for their task.

2i2c offers the following features for a simplified user experience:

1. Profile lists that allow drop down selections of available hardware.
2. 2i2c handles resource allocations that trade-off startup time with allocating users on the same cluster in cost appropriate ways.
3. Profile options based on group membership, e.g. allow only certain groups access to more expensive GPU compute
4. Enhancing group functionality overall in JupyterHub. See our [oauthenticator PR](https://github.com/jupyterhub/oauthenticator/pull/735), [jupyterhub PR](https://github.com/jupyterhub/jupyterhub/pull/4822), our own code that [we will upstream](https://github.com/2i2c-org/infrastructure/issues/4021), [veda work](https://github.com/NASA-IMPACT/veda-jupyterhub/issues/44).
5. Idle culling behavior to prevent users from accidentally leaving servers running when they are not in use
6. Grafana Dashboards that track CPU and RAM utilization.

Future work:

1. Display live resource usage directly in the user interface, so that users are empowered to self-moderate. `jupyter-resource-usage` was upstreamed to `jupyterlab-contrib` by 2i2c, and we could prioritize similar work in the future.
2. Reporting capabilities so that admins can make decisions on who who has access to what resources based on group membership.
3. Contribution to other Jupyter adjacent projects (such as kbatch and dask-gateway).
4. Impose per-user monthly quotas on compute.
5. Further idle culling customizations to accommodate lengthy compute jobs.

### Network

Commercial cloud providers often do not charge you for uploading data into the clouds (data ingress), but charge you a **lot** for transferring data out (data egress). This is the most common 'surprise bill' that cloud users can receive. The EU recently introduced the [Data Act](https://digital-strategy.ec.europa.eu/en/factpages/data-act-explained) to remove these heavy penalties and anti-competitive practices. However, it remains to be seen whether other regions will follow suit and how thoroughly providers will comply.

This has not been a real problem so far, because we lock this down. But if it does become a problem, we have mechanisms to control this. Egress is what causes major problems, and we have mybinder.org experience in handling that when needed. As long as your work is contained within the hub, there is no need pay excessive egress charges.

Additionally 2i2c offers cryptomining protection for public-facing hubs using `cryptnono` by default, therefore preventing costs incurred from such activities.

## Summary

Our mantra for cloud cost management is

> Control how much your users use, and you control how much money you spend!

Usage reports grant visibility into the amount of consumed resources that have a direct relationship to cost. In order to control these costs we focus our guardrails on three key areas: storage, compute and network. Over time we will keep improving usage reports as we continue to understand the individual needs of each of our communities better.

We are also working with integrating various tools cloud providers give us to gain insight into the actual \$\$\$ numbers are for each hub on a cluster. These tools do not provide visibility into costs on a *per-user* basis, but combining this with usage monitoring (which *can* be done per user) from Grafana, we can build a meaningful picture of overall cost that can allow researchers take financial control of their hub in the cloud.
