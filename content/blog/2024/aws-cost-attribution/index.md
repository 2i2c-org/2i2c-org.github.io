---
title: Track and manage cloud costs using Grafana
date: "2024-11-11"
banner:
  image: "featured.png"
authors: ["Jenny Wong"]
tags: []
categories: [organization]
featured: false
draft: false
---

![Screenshot of a graph showing total daily costs per component.](featured.png "Grafana dashboard showing cloud costs broken down by compute, storage and other components for the [Openscapes](https://openscapes.org/) hub.")

We are pleased to unveil a new feature to track cloud costs within our Grafana dashboards! Community Champions now have the ability to monitor the cost and usage of their 2i2c-managed hubs that displays up to date aggregated costs as well as detailed breakdowns for more granular reports.

{{% callout note %}}
Note that this feature is currently available to AWS hosted hubs only and will be rolled out to other cloud providers in the future.
{{% /callout %}}

## Accessing the cloud cost dashboard

Community Champions can view the Cloud Cost dashboard from their Grafana instance (please see the [Service Guide](https://docs.2i2c.org/admin/howto/monitoring/) for how to gain access).

From the main menu of Grafana, navigate to *Dashboards > Cloud cost dashboards > Cloud cost attribution* to view the dashboard.

## Understanding the cloud cost dashboard

A typical 2i2c-managed deployment comprises of a staging hub and a production hub, although some other communities may have extra hubs such as a workshop hub. By default, costs are not broken down on a per hub basis unless the community has opted in to this feature.

The dashboard is made of several panels:

- Daily costs
- Daily costs per hub (opt-in only)
- Total daily costs per component
- Daily costs per component per hub (opt-in only).

{{< video autoplay="true" loop="true" src="demo.mp4" >}}

For more detailed information on the data that each panel displays, please consult our Service Guide for reference.

## Sharing cost reports

The dashboard can be shared with other community members and stakeholders so they can understand usage and cost patterns. Community Champions export data to a CSV file, or they can generate a snapshot of the Grafana dashboard and share a public link.

For instructions on how to export data from the dashboard, please see our Service Guide for reference.

## Next steps

We would love to know whether this feature is useful and how it can be improved. Please share your feedback with us!

We are working on rolling out this service to GCP hosted clusters as well. Stay tuned to know when this feature is available to your community.
