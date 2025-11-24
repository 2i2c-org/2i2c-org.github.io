---
title: "Open infrastructure for collaborative geoscience with Project Pythia: Learning how to deploy a BinderHub on Jetstream2"
slug: "jetstream-binderhub"
date: 2025-02-12
authors:
  - Georgiana Dolocan
  - James Munroe
tags:
  - open-source
  - earth-science
categories:
  - service-enhancements
featured: false
draft: false
---

## Project Pythia and the "Jupyter notebook obsolescence" problem

[Project Pythia](https://projectpythia.org/) provides educational resources for essential software tools that enable open, reproducible and scalable geoscience, such as the [Pangeo](https://pangeo.io) stack of packages (Xarray, Dask, Jupyter). Their *Cookbooks* are crowdsourced, community-curated, and open-source collections of Jupyter notebooks that demonstrate how to use these tools for cloud-native, geoscientific workflows (see our [Project Pythia Cookoff](/content/blog/project-pythia-cookoff) blog post). However, "Jupyter notebook obsolescence" is a common problem: tutorials that were created a few years ago may no longer work due to changes in the software ecosystem and hampers the reproducibility of scientific results. A reproducible execution environment and the infrastructure to support it are essential for the long-term sustainability of these educational resources.

## Leveraging NSF-funded cyberinfrastructure for BinderHub

A [BinderHub](https://binderhub.readthedocs.io/en/latest/) allows users to dynamically create custom computing environments from [Binder-ready](https://mybinder.readthedocs.io/en/latest/introduction.html#what-is-a-binder) repositories containing computational notebooks and configuration files that describe the software environment required to run them. A public Binder service exists at [mybinder.org](https://mybinder.org/) (see our blog post about [joining the mybinder federation](../binder-singlenode/index.md) 🎉) and is a successful example of how open cloud infrastructure can accommodate reproducible execution environments.

The resources available on such a public service are limited therefore 2i2c, together with Project Pythia, have been exploring how to deploy a BinderHub backed by larger resources from the NSF-funded cloud computing platform [Jetstream2](https://jetstream-cloud.org/). This allows for larger simultaneous user loads, such as at workshops, as well as access to more powerful distributed and parallelized workflows required to process large geoscientific datasets, under a persistent resource allocation.

## Learning how to deploy on OpenStack

Jetstream2 uses [OpenStack](https://www.openstack.org) in order to manage pools of compute, storage and networking resources, and for our purposes we specifically make use of OpenStack [Magnum](https://docs.openstack.org/magnum/latest/) [Cluster API driver](https://specs.openstack.org/openstack//magnum-specs/specs/bobcat/clusterapi-driver.html) to manage Kubernetes for our deployment.

Cluster API needs a `CAPI management cluster` in order to manage other Kubernetes clusters, called workload clusters. On Jetstream2, this management cluster is gracefully created and operated by the Jetstream2 team, which means that the only task to worry about is creating and configuring the workload cluster.

For the workload cluster we used the [Openstack Terraform provider](https://registry.terraform.io/providers/terraform-provider-openstack/openstack/latest/docs) to define the cluster template, the cluster itself and the node groups in a reproducible way.

After the cluster infrastructure was successfully created on Jetstream2, thanks to the 2i2c hub infrastructure being cloud agnostic as well, deploying BinderHub to Jetstream2, was a seamless experience and it was no different than on other cloud providers that we already supported.

We also learnt about some limitations of the Openstack Magnum driver project, which were expected given it being a relatively recent project, slowly being adopted, but they were all reported upstream and hopefully will soon be fixed.

## Acknowledgements

- [Jetstream2](https://jetstream-cloud.org/): Explore ACCESS allocation and Julian Pistorius for technical support
- Thanks to [Project Pythia](../../../collaborators/pythia/) for funding and collaborating with us on this work.
- [Andrea Zonca](https://www.zonca.dev/posts/2024-12-11-jetstream_kubernetes_magnum) for preliminary work on Kubernetes deployments on Jetstream 2
