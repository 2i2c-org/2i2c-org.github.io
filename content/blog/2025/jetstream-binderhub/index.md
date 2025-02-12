---
title: "Open infrastructure for collaborative geoscience with Project Pythia: Learning how to deploy a BinderHub on Jetstream2"
date: "2025-02-12"
authors: ["Georgiana Dolocan", "James Munroe"]
tags: [open source, geoscience]
categories: [impact]
featured: false
draft: false
---

## Project Pythia and the "Jupyter notebook obsolescence" problem

[Project Pythia](https://projectpythia.org/) provides educational resources for essential software tools that enable open, reproducible and scalable geoscience, such as the [Pangeo](https://pangeo.io) stack of packages (Xarray, Dask, Jupyter). Their *Cookbooks* are crowdsourced, community-curated, and open-source collections of Jupyter notebooks that demonstrate how to use these tools for cloud-native, geoscientific workflows (see our [Project Pythia Cookoff](/content/blog/2024/project-pythia-cookoff/index.md) blog post). However, "Jupyter notebook obsolescence" is a common problem: tutorials that were created a few years ago may no longer work due to changes in the software ecosystem and hampers the reproducibility of scientific results. A reproducible execution environment and the infrastructure to support it are essential for the long-term sustainability of these educational resources.

## Leveraging NSF-funded cyberinfrastructure for BinderHub

A [BinderHub](https://binderhub.readthedocs.io/en/latest/) allows users to dynamically create custom computing environments from [Binder-ready](https://mybinder.readthedocs.io/en/latest/introduction.html#what-is-a-binder) repositories containing computational notebooks and configuration files that describe the software environment required to run them. A public Binder service exists at [mybinder.org](https://mybinder.org/) (see our blog post about [joining the mybinder federation](../binder-singlenode/index.md) 🎉) and is a successful example of how open cloud infrastructure can accommodate reproducible execution environments.

The resources available on such a public service are limited therefore 2i2c, together with Project Pythia, have been exploring how to deploy a BinderHub backed by larger resources from the NSF-funded cloud computing platform [Jetstream2](https://jetstream-cloud.org/). This allows for larger simultaneous user loads, such as at workshops, as well as access to more powerful distributed and parallelized workflows required to process large geoscientific datasets, under a persistent resource allocation.

## Learning how to deploy on OpenStack

Jetstream2 uses [OpenStack](https://www.openstack.org) in order to manage pools of compute, storage and networking resources, and for our purposes we specifically make use of OpenStack [Magnum](https://docs.openstack.org/magnum/latest/) [Cluster API driver](https://specs.openstack.org/openstack//magnum-specs/specs/bobcat/clusterapi-driver.html) to manage Kubernetes for our deployment.

*More technical details to follow here @GeorgianaElena*

## Acknowledgements

- [Jetstream2](https://jetstream-cloud.org/): Explore ACCESS allocation and Julian Pistorius for technical support
- [Project Pythia](https://projectpythia.org/) (NSF award 2324302)