---
title: Collaborating with DevSeed to deliver cyberinfrastructure for NASA VEDA
date: "2024-07-02"
authors: ["Jenny Wong"]
tags: [geoscience, open source]
categories: [impact]
featured: false
draft: false
---

![Landing page of the public-facing NASA VEDA dashboard](featured.png "The [VEDA dashboard](https://www.earthdata.nasa.gov/dashboard/)")

The 2i2c team are proud to continue our strong working collaboration with [DevSeed](https://developmentseed.org/), following our previous work on launching the [US GHG center](blog/2023/us-ghg-center-launches/index) (also see the [DevSeed blog post](https://developmentseed.org/blog/2023-12-14-ghg-center)). Together with scientists at NASA in our regular 6-weekly sync touchpoints, we have recently delivered a tranche of improvements to [the Visualization, Exploration and Data Analysis (VEDA) project](https://www.earthdata.nasa.gov/esds/veda).

This platform is designed to thread open-source components together to consolidate GIS delivery mechanisms, processing, analysis and visualization tools, and presented in a collaborative interactive computing environment. All code repositories and associated resources stemming from this work are available on the [VEDA GitHub page](https://github.com/NASA-IMPACT/VEDA/wiki).

Over the past quarter, we have enabled the following improvements to the VEDA platform:

**Better image management and testing** – Switch to managing a single image QGIS image with a single GitHub repository using [repo2docker](https://repo2docker.readthedocs.io/en/latest/) and automated testing

**A dynamic image building user interface** – Implement the BinderHub integration developed with our [GESIS collaboration](blog/2024/jupyterhub-binderhub-gesis/index)

**Automatically pull example notebooks** – Present users with starter examples to get started with VEDA with [jupyterhub-gitpuller-init](https://github.com/NASA-IMPACT/jupyterhub-gitpuller-init)

**Allow tiered access to JupyterHub resources** – This required open infrastructure engineering work to enable an `auth_state` (see this [GitHub issue](https://github.com/2i2c-org/infrastructure/issues/4279)).

**Improve the QGIS experience** – `jupyter-remote-qgis-proxy` was developed to create a custom endpoint that accepts query parameters to open datasets in QGIS (see the deployment in this [GitHub Pull Request](https://github.com/2i2c-org/infrastructure/pull/4299)).

<!-- TBC: @jnywong Insert demo video -->

**Support workshop users** – See our related blog post [US Greenhouse Gas Center supports summer school at CIRA](blog/2024/ghg-summer-school/index))

**Integrate the MAAP/JPL Data Processing Service (DPS)** – The [pangeo-notebook-veda-image](https://github.com/NASA-IMPACT/pangeo-notebook-veda-image) was updated with the `maap-algorithms-jupyter-extension` and the `maap-dps-jupyter-extension` packages to enable the [Multi-Mission Algorithm and Analysis Platform](https://docs.maap-project.org/en/latest/getting_started/about_maap.html). Capability to launch DPS jobs from the hub is coming soon.

**Integrate with a unified auth solution** – Work is underway to provide a streamlined and central authentication system for integration with all applications across the VEDA ecosystem, enhancing security and user experience.

<!-- TBC: @yuvipanda Insert a quote from 2i2c about the collaboration -->

<!-- TBC: @yuvipanda Insert a quote from DevSeed about the collaboration -->

<!-- TBC: @yuvipanda Insert a quote from NASA about the collaboration -->

## Acknowledgements

- [Development Seed](https://developmentseed.org/)
- [NASA IMPACT](https://impact.earthdata.nasa.gov/)
