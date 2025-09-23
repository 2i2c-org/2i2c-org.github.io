---
title: "Demonstrating our infrastructure's reliability with a hub status page for our communities"
subtitle: ""
tags: ["reliability"]
categories: ["service"]
date: "2025-09-23"
featured: false
draft: false
---

One of 2i2c's goals is to **make the cloud safe for science**.
A big part of this is making the black box of commercial cloud infrastructure more predictable and reliable, while running a network of community hubs that all operate autonomously.

As part of this effort, we've created a **status page for 2i2c's network of community hubs**. This is a source of truth to provide a high-level picture of the stability of our infrastructure, and to give us a heads up when things aren't working as expected. You can check it out at:

👉 [**`status.2i2c.org`**](https:status.2i2c.org)

{{< figure src="featured.png" caption="The 2i2c Status Page gives communities a high-level view of the uptime for our entire network of community hubs.">}}

As part of this process, we've also [streamlined our incident response processes](https://github.com/2i2c-org/team-compass/pull/1021) in order to more quickly respond to outages when they occur (ideally, before a community has even noticed!).

There are still plenty of improvements we'd like to make: for example, we're focusing on major outages right now, but would like to extend some level of reporting for _degraded_ service, like unexpectedly slow start times.

## Learn more

- 👉 [The status page](https://2i2c-hubs.trust.pagerduty.com/posts/dashboard)
- 👉 [The status page documentation](https://docs.2i2c.org/admin/reliability/status-page/)
- 👉 [Our new process for incident response](https://github.com/2i2c-org/team-compass/pull/1021)
- 👉 Follow an [in-progress initiative to improve the reliability of our infrastructure](https://github.com/2i2c-org/infrastructure/issues/6417)
