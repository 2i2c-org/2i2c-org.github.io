---
title: More transparency and control for your cloud infrastructure | 2i2c September 2025 Community Update
date: 2025-10-01
authors:
  - Chris Holdgraf
categories:
  - organization
tags:
  - update
---

September was a big month for giving our communities better visibility into their infrastructure. We shipped [per-user cost dashboards](https://2i2c.org/blog/2025/cloud-cost-monitoring/), launched a [status page at status.2i2c.org](https://2i2c.org/blog/2025/status-page/), and [cut baseline AWS costs](https://2i2c.org/blog/2025/aws-cost-reduction/) by switching to more efficient instance types. We also helped CCAD gain [more control over their computing infrastructure](https://2i2c.org/blog/2025/catalyst-hardware-exchange/) through a hardware exchange, and shared our thinking about [being responsible open source citizens](https://2i2c.org/blog/2025/good-citizen/). Here's what stood out:

## Enabling transparent cloud cost monitoring with user-level dashboards

We shipped dashboards that let communities monitor cloud usage and costs at a per-user level. This gives communities confidence they won't face unexpected bills and helps them understand how their usage patterns translate to cloud costs. Communities can now see exactly how their computational work translates to spending, enabling better resource planning and budget management.

<figure>
<img src="https://2i2c.org/blog/2025/cloud-cost-monitoring/featured.png" alt="Cloud cost monitoring dashboard showing user-level usage and cost breakdowns">
  <figcaption>The new cost monitoring dashboard shows per-user breakdowns of cloud usage and costs.</figcaption>
</figure>

Read more 👉 [2i2c.org/blog/2025/cloud-cost-monitoring/](https://2i2c.org/blog/2025/cloud-cost-monitoring/)

## Demonstrating our infrastructure's reliability with a hub status page for our communities

We launched a status page at status.2i2c.org that gives communities a high-level view of our infrastructure's stability. This is a single source of truth for understanding whether your hub is experiencing problems and helps us respond to outages faster—ideally before communities even notice. We're also streamlining our incident response processes to make outages less frequent and shorter when they do occur.

<figure>
<img src="https://2i2c.org/blog/2025/status-page/featured.png" alt="The 2i2c status page showing uptime status for the network of community hubs">
  <figcaption>The 2i2c Status Page gives communities a high-level view of uptime across our entire network.</figcaption>
</figure>

Read more 👉 [2i2c.org/blog/2025/status-page/](https://2i2c.org/blog/2025/status-page/)

## Reducing base infrastructure costs on AWS with smarter instance types

We reduced the baseline costs of running our AWS infrastructure by switching from older r5.xlarge instances to newer, more efficient r8i-flex.large instances. These are the core nodes that keep hubs "always available" for users. The graph below shows daily savings for one community—we're rolling this out to all new clusters and gradually migrating existing ones.

<figure>
<img src="https://2i2c.org/blog/2025/aws-cost-reduction/featured.png" alt="Graph showing EC2 cost reduction over time for one community">
  <figcaption>Daily EC2 cost savings from switching to more efficient instance types.</figcaption>
</figure>

Read more 👉 [2i2c.org/blog/2025/aws-cost-reduction/](https://2i2c.org/blog/2025/aws-cost-reduction/)

---

_Here's a list of all the blog posts we published in September 2025._

- Sep 02, 2025 - [Giving CCAD more control over data science infrastructure via a Catalyst Project hardware exchange](https://2i2c.org/blog/2025/catalyst-hardware-exchange/)
- Sep 03, 2025 - [On being a good open source citizen: supporting a healthy ecosystem through directed and foundational contributions](https://2i2c.org/blog/2025/good-citizen/)
- Sep 03, 2025 - [Sharing JupyterHub's vision for more flexible application deployment at the doepy talk series.](https://2i2c.org/blog/2025/doepy-yuvi/)
- Sep 10, 2025 - [We're going to try blogging about our work more often](https://2i2c.org/blog/2025/communications-strategy/)
- Sep 16, 2025 - [Incident report: UC Merced user throttling during class startup](https://2i2c.org/blog/2025/incident-ucmerced-user-throttling/)
- Sep 17, 2025 - [Reducing base infrastructure costs on AWS with smarter instance types](https://2i2c.org/blog/2025/aws-cost-reduction/)
- Sep 23, 2025 - [Updates from Chris' position on the Jupyter Executive Council and Foundation Board](https://2i2c.org/blog/2025/executive-council-updates/)
- Sep 23, 2025 - [Demonstrating our infrastructure's reliability with a hub status page for our communities](https://2i2c.org/blog/2025/status-page/)
- Sep 26, 2025 - [From scattered effort to strategic impact: How we're systematizing our Foundational open source contributions](https://2i2c.org/blog/2025/foundational-contributions/)
- Sep 30, 2025 - [Enabling transparent cloud cost monitoring with user-level dashboards](https://2i2c.org/blog/2025/cloud-cost-monitoring/)
