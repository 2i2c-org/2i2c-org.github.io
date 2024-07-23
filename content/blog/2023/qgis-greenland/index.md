---
title: A QGIS desktop in the cloud with JupyterHub
date: "2023-08-05"
authors: ["Yuvi Panda", "Jenny Wong"]
tags: [geoscience, open source]
categories: [impact]
featured: false
draft: false
---

![QGreenland Researcher Workshop](featured.png "The [QGreenland Researcher Workshop](https://qgreenland-workshop-2023-researcher.github.io/)")

JupyterHub is a versatile platform that can serve a desktop with Geospatial Information Systems (GIS) software in the cloud. This was demonstrated by the QGreenland Researcher Workshop that was hosted by the NASA CryoCloud hub. The hands-on workshop trained 25-30 researchers, from Germany, India, France, Canada, Poland and the United States, on how to work with geospatial data in an open science framework.

## QGreenland Overview

[QGreenland](https://qgreenland.org/) is an open-source geospatial data package designed for QGIS, a community-owned GIS platform. It focuses on Greenland, offering researchers and educators a comprehensive toolset for FAIR (findable, accessible, interoperable and reproducible) data analysis. The package integrates a variety of datasets into a single, easy-to-use data-viewing and analysis platform, supporting both offline and online use. This makes it particularly valuable for remote fieldwork and areas with limited internet access.

## Workshop Success

The QGreenland workshop demonstrated several key benefits of using JupyterHub for cloud-based GIS:

- Accessibility: Participants from across the world could access the same powerful GIS tools through a web browser, eliminating the need for complex local installations while enhancing reproducibility
- Cloud block storage: Using a JupyterHub in the cloud allowed for faster data access than a traditional NFS file store by provisioning each user with an elastic block store disk, reducing load times from 5 minutes to under 3 seconds.
- Cost Efficiency: Utilizing the CryoCloud JupyterHub instance managed by 2i2c drastically cut down setup costs and time, with only minimal cloud operating expenses of roughly $1/person/day.

## Conclusion

The success of the QGreenland workshop underscores the potential of integrating interactive software applications in JupyterHub. This approach not only democratizes access to advanced geospatial tools but also fosters a collaborative research environment. We look forward to supporting more workshops for QGreenland in the future!

*Want to know more? Check out the companion post by QGreenland on the [Jupyter Blog](https://blog.jupyter.org/desktop-gis-software-in-the-cloud-with-jupyterhub-ddced297019a)*

## Acknowledgements

- [Trey Stafford](https://cires.colorado.edu/people/trey-stafford)[(CIRES)](https://cires.colorado.edu/)
- [Matthew Fisher](https://cires.colorado.edu/people/matthew-fisher)[(CIRES)](https://cires.colorado.edu/)
- *Fisher, M., *T. Stafford, T. Moon, and A. Thurber (2023). QGreenland (v3) [software], National Snow and Ice Data Center.
- Snow, Tasha, Millstein, Joanna, Scheick, Jessica, Sauthoff, Wilson, Leong, Wei Ji, Colliander, James, Pérez, Fernando, James Munroe, Felikson, Denis, Sutterley, Tyler, & Siegfried, Matthew. (2023). [CryoCloud JupyterBook](https://book.cryointhecloud.com/intro.html) (2023.01.26). Zenodo. [10.5281/zenodo.7576602](https://doi.org/10.5281/zenodo.7576602)

\* Denotes co-equal lead authorship