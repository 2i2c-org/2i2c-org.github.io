+++
weight = 25
[design]
  columns = "1"
+++
# What is in a 2i2c Hub?

A 2i2c Hub a collection of open source tools that provide interactive computing environments in the cloud. JupyterHub is the lynchpin that ties everything together. It handles user accounts, provides the interactive environment, and connects users with computational and data resources.

JupyterHub is both powerful and flexible, and can be used to provide a variety of environments to users. Here is the most common environment that 2i2c Hubs provide:

- **[Jupyter Interfaces](https://jupyter.org)** (Jupyter Lab and Notebook) are the primary interface provided for users. These offer interactive notebook environments with rich data science and visualization capabilities.
- **The [PyData Ecosystem](https://numfocus.org/sponsored-projects)** provides the core environment in which users do their work. This ecosystem of projects is the most popular open source data science stack used across academia and industry.
- **Domain-specific packages** are installed in a 2i2c Hub alongside the core data science libraries. These allow the hub environment to be customized for a particular use-case or set of users.
- **Data and compute** are provided by the cloud on which the 2i2c Hub is deployed. It is possible to connect user sessions to hardware and data source that are otherwise very difficult to access (such as a 10TB dataset in Amazon S3).
- **User content** (notebooks, scripts, text files, etc) is hosted in online code repositories (e.g., GitHub) and can be dynamically pulled into the 2i2c Hub when a session is launched or when users click a link.

Every 2i2c Hub is tailored for the community that uses it. 2i2c Hubs can run on almost any kind of cloud infrastructure (or even your own local hardware), and they are built with 100% open source and community-driven software.

Below is a diagram showing off some of the major components of a 2i2c Hub.

{{<
  figure src="/media/2i2c-hub-overview.png"
  title="2i2c Hubs build on open source tools for infrastructure and datascience"
  width="70%"
>}}

## 2i2c Hubs support other languages and interfaces too

2i2c Hubs are flexible and can provide a variety of interfaces and languages. Jupyter is a language-agnostic platform, and can supports [kernels in a variety of languages](https://github.com/jupyter/jupyter/wiki/Jupyter-kernels). 2i2c Hubs can be customized for one or more open source languages and environments.

Don't want to use a Jupyter interface? No problem - JupyterHub can serve user interfaces of many kinds - whether it is RStudio, VSCode, or even a remote desktop GUI - basically any interface that can run via a web browser can run with a 2i2c Hub.
