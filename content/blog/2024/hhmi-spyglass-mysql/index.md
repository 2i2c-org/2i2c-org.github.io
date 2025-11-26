---
title: Enabling neuroscience in the cloud with HHMI Spyglass and MySQL on JupyterHub
slug: "hhmi-spyglass-mysql"
date: 2024-07-05
authors:
  - Yuvi Panda
  - James Munroe
  - Jenny Wong
tags:
  - biology
  - open-source
categories:
  - community-impact
featured: false
draft: false
---

![HHMI Spyglass tutorial](featured.png "The [HHMI Spyglass tutorial](https://spyglass.hhmi.2i2c.cloud/)")

## Spyglass

[Spyglass](https://github.com/LorenFrankLab/spyglass) is a framework for reproducible and shareable neuroscience research produced by [Loren Frank’s lab](https://github.com/LorenFrankLab) at the University of California, San Francisco. Check out our [blog post about the release of their preprint](../hhmi-spyglass/index.md) to read more about the methods.

This post focuses on the complex data storage needed for the project, which can be difficult to set up locally or at scale in the cloud. In particular, the analysis needed a MySQL database for reproducibility. This is a fairly common task across many fields. The aim of 2i2c is to enable researchers to focus on the essential complexity of what they were doing, i.e. the science, without managing the accidental complexity of how to do it -- in this case, setting up databases.

We describe how you can do this too for your own JupyterHubs. Since 2i2c commits to running our infrastructure in line with open-source values as much as possible, you can also directly see the [configuration for the hub](https://github.com/2i2c-org/infrastructure/blob/99071c38712ef8e6bed6609117ca4b894b89ae5c/config/clusters/hhmi/spyglass.values.yaml#L76) referenced in the paper.

## What is a "sidecar container"?

The Kubernetes definition of a [sidecar container](https://kubernetes.io/docs/concepts/workloads/pods/sidecar-containers/) is

> Sidecar containers are the secondary containers that run along with the main application container within the same Pod. These containers are used to enhance or to extend the functionality of the primary app container by providing additional services, or functionality such as logging, monitoring, security, or data synchronization, without directly altering the primary application code.

In this case, the *primary* app container is the JupyterLab instance where people are interactively running code and doing science. We want to provide a MySQL database as a sidecar so that each user server gets their own independent MySQL server instance (that is not accessible to anyone else). We can then run code such as

```
%%bash
mysql -h 127.0.0.1 -u root --password=tutorial < path-to-sql-file-with-data
```

to load data into the database. Note the IP address `127.0.0.1` - the MySQL server is listening on localhost, even though it is not running in the *same container*! Thanks to the magic of [Linux Network Namespaces](https://lwn.net/Articles/580893/), the sidecar and main app container can share `127.0.0.1`. This allows you to write code that works **in the exact same way** on a user's local computers as on the JupyterHub, making transitions and replication easier.

## Setting up sidecars in JupyterHub on Kubernetes

We're leveraging multiple tools from the open-source ecosystem - JupyterHub, Kubernetes, Linux as well as MySQL itself.

Since this is a *Kubernetes* feature, we can pass through config to it. There are
two layers here, which are

1. [singleuser.extraContainers](https://z2jh.jupyter.org/en/latest/resources/reference.html#singleuser-extracontainers) in [z2jh](https://z2jh.jupyter.org/en/stable/) configuration
2. [KubeSpawner.extra_containers](https://jupyterhub-kubespawner.readthedocs.io/en/latest/spawner.html#kubespawner.KubeSpawner.extra_containers) in [KubeSpawner](https://jupyterhub-kubespawner.readthedocs.io/en/latest/spawner.html) configuration

The hub configuration looks like

```yaml
  singleuser:
    extraContainers:
      - name: mysql
        image: datajoint/mysql:8.0 # following the spyglass tutorial at https://lorenfranklab.github.io/spyglass/latest/notebooks/00_Setup/#existing-database
        ports:
          - name: mysql
            containerPort: 3306
        resources:
          limits:
            # Best effort only. No more than 1 CPU, and if mysql uses more than 4G, restart it
            memory: 4Gi
            cpu: 1.0
          requests:
            # If we don't set requests, k8s sets requests == limits!
            # So we set something tiny
            memory: 64Mi
            cpu: 0.01
        env:
          # Configured using the env vars documented in https://lorenfranklab.github.io/spyglass/latest/notebooks/00_Setup/#existing-database
          - name: MYSQL_ROOT_PASSWORD
            value: "tutorial"
```

By setting this up, we allow users to insert the code snippet above

```
%%bash
mysql -h 127.0.0.1 -u root --password=tutorial < path-to-sql-file-with-data
```

into their [Jupyter Notebooks](https://github.com/LorenFrankLab/spyglass-demo/blob/main/notebooks/00_HubQuickStart.ipynb), which gives access to their MySQL database in the hub!

However, this configuration does not include permanently store the database itself between hub server sessions. Thanks to a pilot in a prior collaboration with University of Texas, Austin, we do have [some documentation](https://github.com/2i2c-org/infrastructure/blob/main/docs/howto/features/per-user-db.md) on how you can enable that as well!

## Acknowledgements

- [Howard Hughes Medical Institute](../../../collaborators/hhmi/)
- National Institute of Mental Health (NIMH), grant number RF1MH130623
- [kubespawner](https://github.com/jupyterhub/kubespawner)
- [zero-to-jupyterhub-k8s](https://github.com/jupyterhub/zero-to-jupyterhub-k8s/) and the [JupyterHub community](../../../collaborators/jupyterhub/)
