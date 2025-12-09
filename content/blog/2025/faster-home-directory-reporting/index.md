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

## Using native filesystem data to drastically speed up disk usage

Our existing storage monitoring tool, [`prometheus-dirsize-exporter`](https://github.com/2i2c-org/prometheus-dirsize-exporter), deliberately runs slowly to avoid excessive disk I/O. This meant home directory metrics could be **hours out of date** on systems with many users or large directories. Plus, there was no way to report user quota limits at all.

Most of our storage server already use [XFS](https://en.wikipedia.org/wiki/XFS) as the underlying filesystem. XFS project quotas track directory usage at the filesystem level, providing instant size information without scanning individual files. We weren't exposing this data to our monitoring system, so we had to rely on slower scanning methods instead.

We made two key improvements:

1. **Make disk usage reporting almost instantaneous**. We added code to export `total_size_bytes` and `hard_limit_bytes` metrics from XFS quotas to Prometheus for near-instant reporting. We used the same metric names and namespace as `prometheus-dirsize-exporter` for compatibility. See https://github.com/2i2c-org/jupyterhub-home-nfs/pull/76

2. **Allow this to be used upstream in JupyterHub Grafana Dashboards** so that it can support both types of disk usage reporting. This means users of the upstream [JupyterHub Grafana dashboards](https://github.com/jupyterhub/grafana-dashboards) get the same useful view about home directory usage, regardless of whether the metric comes from `prometheus-dirsize-exporter` or `jupyterhub-home-nfs`. See https://github.com/2i2c-org/prometheus-dirsize-exporter/pull/29

These changes were [deployed across all our communities](https://github.com/2i2c-org/infrastructure/pull/7261), so administrators can now access current home directory information **within minutes** regardless of directory size.

{{< figure src="featured.png" title="Home Directory Usage dashboard showing total size metrics from jupyterhub-home-nfs and other data from prometheus-dirsize-exporter">}}

## Coming next

We'd like to build on this work to enable **alerting when individual users near their disk quotas**. This will make it easier to more reliably track user disk usage across a community. See this issue for tracking: https://github.com/2i2c-org/infrastructure/issues/7166
