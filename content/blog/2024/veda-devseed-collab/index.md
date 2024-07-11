---
title: Collaborating with Development Seed to deliver cyberinfrastructure for NASA VEDA
date: "2024-07-02"
authors: ["Jenny Wong"]
tags: [geoscience, open source]
categories: [impact]
featured: false
draft: false
---

![Landing page of the public-facing NASA VEDA dashboard](featured.png "The [VEDA dashboard](https://www.earthdata.nasa.gov/dashboard/)")

The 2i2c team are proud to continue our strong working collaboration with [Development Seed](https://developmentseed.org/), following our previous work on launching the [US GHG center](blog/2023/us-ghg-center-launches/index) (also see the [Development Seed blog post](https://developmentseed.org/blog/2023-12-14-ghg-center)). Together with scientists at NASA in our regular sync touchpoints, we have recently delivered a tranche of improvements to [the Visualization, Exploration and Data Analysis (VEDA) project](https://www.earthdata.nasa.gov/esds/veda).

This platform is designed to thread open-source components together to consolidate GIS delivery mechanisms, processing, analysis and visualization tools, and presented in a collaborative interactive computing environment. All code repositories and associated resources stemming from this work are available on the [VEDA GitHub page](https://github.com/NASA-IMPACT/VEDA/wiki).

In the spirit of fully open development, you can [see the objectives](https://github.com/NASA-IMPACT/veda-jupyterhub/issues?q=is%3Aissue+jh+is%3Aclosed+label%3A%22PI+24.3%22+)
the combined 2i2c and Development Seed team had for the last quarter. In this blog post, we will describe some of the significant ones!


## Better image management and testing

[repo2docker-action](https://github.com/jupyterhub/repo2docker-action) is a GitHub action simplifying image building and testing for use with JupyterHub, using either a `Dockerfile` or just the various [configuration files](https://repo2docker.readthedocs.io/en/latest/config_files.html) (like `requirements.txt`, `environment.yml`, etc) supported by [repo2docker](https://github.com/jupyterhub/repo2docker). We migrated our image building pipeline from a somewhat homegrown solution to this upstream action, making image updates and testing *much* easier. In particular, it has allowed us to [automatically run test notebooks](https://github.com/NASA-IMPACT/pangeo-notebook-veda-image/pull/4) on every change we make to the image! This way, we can easily catch any breaking changes in library versions or other image changes without impact to our users. We also debugged and [contributed upstream](https://github.com/jupyterhub/repo2docker-action/pull/124) fixes to the testing infrastructure so everyone could benefit from this, rather than just us.

## Automatically pulling example notebooks on startup

When a user logs into a JupyterHub, it is very helpful if we could have a bunch of example notebooks and other content pre-populated for them so they can get started right away. [nbgitpuller](https://nbgitpuller.readthedocs.io/) is heavily used for this particular use case. However, it requires that nbgitpuller is installed inside the image the user is using - and not all images have it installed. In particular, we wanted to continue using the (wonderful) [rocker images](https://rocker-project.org/) for R users, and they do not have nbgitpuller installed. So we ended up building [jupyterhub-gitpuller-init](https://github.com/NASA-IMPACT/jupyterhub-gitpuller-init), which can be used as an [init container](https://kubernetes.io/docs/concepts/workloads/pods/init-containers/) to pre-populate user content on persistent home directories regardless of the image used. We also made sure to build this in a way that *anyone* can use it, and it is not tied into either 2i2c or VEDA infrastructure!

## Opening specific visualizations in QGIS via URL

**Improve the QGIS experience** – `jupyter-remote-qgis-proxy` was developed to create a custom endpoint that accepts query parameters to open datasets in QGIS (see the deployment in this [GitHub Pull Request](https://github.com/2i2c-org/infrastructure/pull/4299)).

<figure>
  {{< video autoplay="true" loop="true" src="qgis.mp4" >}}
  <figcaption>Launching QGIS on a Linux desktop served by the VEDA JupyterHub</figcaption>
</figure>

## Better Profile Selection

**A dynamic image building user interface** – Implement the BinderHub integration developed with our [GESIS collaboration](blog/2024/jupyterhub-binderhub-gesis/index)

## Home Directory Reporting

## Supporting workshops

End users benefiting from our work is what ultimately gives meaning to our work. To that end, we were very happy to support running workshops -
- see our related blog post [US Greenhouse Gas Center supports summer school at CIRA](blog/2024/ghg-summer-school/index))


Delivering on these objectives in a timely way heavily depended on the success of the team collaboration. [Sanjay Bhangar](https://developmentseed.org/team/sanjay-bhangar) of Development Seed commented

> Working closely with the 2i2c team on growing features to support users on the VEDA and GHG Center hubs has been absolutely amazing. With 2i2c’s deep experience in the Jupyter ecosystem, we have been able to implement some fairly complex features quite easily, and their strong open-source roots have ensured that whatever we work on is broadly useful to the wider Jupyter and scientific computing communities.

## Acknowledgements

- [Development Seed](https://developmentseed.org/)
- [NASA IMPACT](https://impact.earthdata.nasa.gov/)
