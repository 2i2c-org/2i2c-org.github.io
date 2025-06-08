---
title: "Group-level resource monitoring with JupyterHub, Prometheus and Grafana"
subtitle: ""
authors: ["Jenny Wong"]
tags: ["jupyterhub", "prometheus", "grafana", "kubernetes"]
categories: ["Service"]
date: "2025-06-08"
featured: false
draft: false
---

Managing user groups in JupyterHub can be a challenging task, especially in environments with dynamic user bases and complex group structures. This post describes how we can leverage the latest group management features in JupyterHub, along with Prometheus and Grafana, to monitor group-level resource usage effectively.

![Grafana User Group Diagnostics Dashboard showing a memory usage over time with each line aggregating usage over a different user group.](./featured.png)

## Motivation

Hub admins have a strong impetus to monitor usage and costs by user groups
because it allows them to advocate for better funding and cost recovery models based on data-driven insights. Group-level resource monitoring can help them to answer questions like:

- How many people participated in our workshop group?
- How much GPU compute is our power user group using?
- Is our resource usage cost-effective for X group persona or Y group persona?

## JupyterHub and user groups

Users can access JupyterHub using a variety of authentication methods. Authentication providers like GitHub have built-in user management features that allow admins to create and manage user groups. These groups can configured in JupyterHub to authorize access to the hub, as well as control access to certain hardware profiles.

We can also leverage [authenticator-managed group membership](https://jupyterhub.readthedocs.io/en/stable/reference/authenticators.html#authenticator-managed-group-membership) to automatically pass user group memberships from the authentication layer to JupyterHub itself. This allows us to capitalize on JupyterHub's REST API to retrieve user group memberships from other services, such as exporting them as Prometheus metrics.

## Exporting user group memberships to Prometheus

The [`jupyterhub-groups-exporter`](https://github.com/2i2c-org/jupyterhub-groups-exporter) project provides a service that integrates with JupyterHub to export user group memberships as Prometheus metrics. Exposing user group data as an endpoint for Prometheus to scrape allows us to query and join groups data with a range of usage metrics to gain powerful group-level insights.

## Visualizing user group resource usage with Grafana

We made an upstream contribution to the [jupyterhub/grafana-dashboards](https://github.com/jupyterhub/grafana-dashboards) project to encapsulate the PromQL queries as Jsonnet code and represent them as Grafana Dashboard visualizations (also known as [Grafonnet](https://grafana.github.io/grafonnet/index.html)).

## Future work

We have laid the foundation for extensible group-level management with JupyterHub by encoding user group memberships in JupyterHub's database. This makes user group data readily available through the REST API endpoint to be consumed by other services.

Future directions for this work include:

- visualising cloud cost by user group in Grafana
- streamlining management of hardware profile options by user group
- introducing group-level resource quotas.

What do you think? How would you like to see JupyterHub's group management features evolve? [We welcome your feedback!](https://airtable.com/appM2L2x1uglMU0hy/pagWPJDEKTlLd7uMP/form)