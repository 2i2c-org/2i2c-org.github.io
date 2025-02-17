---
title: Track and manage cloud costs using Grafana
date: 2024-11-15
authors:
  - Jenny Wong
tags: []
categories:
  - organization
featured: false
draft: false
---

![Screenshot of a graph showing total daily costs per component.](featured.png "Grafana dashboard showing cloud costs broken down by compute, storage and other components for the [Openscapes](https://openscapes.org/) hub.")

We are pleased to unveil a new feature to track cloud costs within our Grafana dashboards! Community Champions now have the ability to monitor the cost and usage of their 2i2c-managed hubs that displays up to date aggregated costs as well as detailed breakdowns for more granular reports.

{{% callout note %}}
Note that this feature is currently available to AWS hosted hubs only and will be rolled out to other cloud providers in the future.
{{% /callout %}}

## Accessing the cloud cost dashboard

Community Champions can view the Cloud Cost dashboard from their Grafana instance (please see the [Service Guide](https://docs.2i2c.org/admin/howto/monitoring/grafana-dashboards/#getting-a-grafana-account) for how to gain access).

From the main menu of Grafana, navigate to *Dashboards > Cloud cost dashboards > Cloud cost attribution* to view the dashboard.

## Understanding the cloud cost dashboard

A typical 2i2c-managed deployment comprises of a staging hub and a production hub, although some other communities may have extra hubs such as a workshop hub. By default, costs are not broken down on a per hub basis unless the community has opted in to this feature.

The dashboard is made of several panels:

- Daily costs
- Daily costs per hub (opt-in only)
- Total daily costs per component
- Daily costs per component per hub (opt-in only).

{{< video autoplay="true" loop="true" src="demo.mp4" >}}

For more detailed information on the data that each panel displays, please consult our [Service Guide](https://docs.2i2c.org/admin/howto/monitoring/cost-attribution/#understanding-the-cloud-cost-dashboard) for reference.

## Sharing cost reports

The dashboard can be shared with other community members and stakeholders so they can understand usage and cost patterns. Community Champions can export data to a CSV file, or they can generate a snapshot of the Grafana dashboard and share a public link.

For instructions on how to export data from the dashboard, please see our [Service Guide](https://docs.2i2c.org/admin/howto/monitoring/cost-attribution/#sharing-cost-reports) for reference.

## Next steps

We would love to know whether this feature is useful and how it can be improved. We will be contacting individual communities to share their feedback with us – please share your thoughts with us!

We will work on rolling out this service to GCP hosted clusters in future. Stay tuned to know when this feature is available to your community.

## Acknowledgements

Thank you to Erik for spearheading the rollout effort and to the rest of the 2i2c team for their support. We are especially grateful to the Openscapes and Cryocloud communities for providing valuable insights during the prototyping and testing phase.
