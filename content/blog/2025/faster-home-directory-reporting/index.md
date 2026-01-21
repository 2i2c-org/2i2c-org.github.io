---
title: "Faster reporting of user home directory sizes"
slug: "faster-home-directory-reporting"
date: "2025-12-09"
categories:
- service enhancements
tags:
- monitoring
- reliability
- devops
- open source
---

Storage quotas help users avoid running out of space unexpectedly and give administrators visibility into capacity planning. However, storage usage can change rapidly, and it's important to have quick information so that administrators know whether they are close to hitting limits.

We've improved how quickly hub administrators can see user home directory sizes across our JupyterHubs. This makes monitoring more responsive and adds quota limit visibility that wasn't possible before.

## Using `jupyterhub-home-nfs` for near-instant disk usage metrics

Our existing storage monitoring tool, [`prometheus-dirsize-exporter`](https://github.com/2i2c-org/prometheus-dirsize-exporter), deliberately runs slowly to avoid excessive disk I/O. This meant home directory metrics could be **hours out of date** on systems with many users or large directories. Plus, there was no way to report user quota limits at all.

Our home directory storage is managed by [`jupyterhub-home-nfs`](https://github.com/2i2c-org/jupyterhub-home-nfs/), which enforces per-user quotas. It could also expose usage and limit information as Prometheus metrics using data from the underlying filesystem quota system. Because this information is already tracked by the filesystem, it's available immediately without scanning individual files.

We made two key improvements:

1. **Make disk usage reporting almost instantaneous**. We made `jupyterhub-home-nfs` export `total_size_bytes` and `hard_limit_bytes` metrics to Prometheus for near-instant reporting. We used the same metric names and namespace as `prometheus-dirsize-exporter` for compatibility. See https://github.com/2i2c-org/jupyterhub-home-nfs/pull/76

2. **Allow this to be used upstream in JupyterHub Grafana Dashboards** so that it can support both types of disk usage reporting. This means users of the upstream [JupyterHub Grafana dashboards](https://github.com/jupyterhub/grafana-dashboards) get the same useful view about home directory usage, regardless of whether the metric comes from `prometheus-dirsize-exporter` or `jupyterhub-home-nfs`. See https://github.com/2i2c-org/prometheus-dirsize-exporter/pull/29

These changes were [deployed across all our communities](https://github.com/2i2c-org/infrastructure/pull/7261), so administrators can now access current home directory information **within minutes** regardless of directory size.

{{< figure src="featured.png" title="Home Directory Usage dashboard showing total size metrics from jupyterhub-home-nfs and other data from prometheus-dirsize-exporter">}}

## Try it out

2i2c member organizations can try this out now. If you have access to your hub's Grafana instance, you can see these new metrics in the _Home Directory Usage_ dashboard:

1. Open your hub's [Grafana dashboard](https://docs.2i2c.org/admin/monitoring/grafana-dashboards/).
2. Go to `Dashboards` -> `JupyterHub Default Dashboards` -> `Home Directory Usage`.
3. Check the table for up-to-date *total size* and *quota limit* values.

For more details, see our [docs on filesystem and disk dashboards](https://docs.2i2c.org/admin/monitoring/disk-usage/).

## Coming next

We'd like to build on this work to enable **alerting when individual users near their disk quotas**. This will make it easier to more reliably track user disk usage across a community. See this issue for tracking: https://github.com/2i2c-org/infrastructure/issues/7166

## Acknowledgements

- This was a directed contribution supported by [NASA VEDA](../../../collaborators/nasa-veda/) to enable more proactive monitoring and alerting for hub administrators.
