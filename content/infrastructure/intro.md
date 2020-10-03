+++
# Homepage
type = "blank"
headless = true  # Homepage is headless, other widget pages are not.
weight = 1
title = "The 2i2c Hubs"

[design]
  columns = "1"
+++

2i2c Hubs are hosted interactive computing environments that run in the cloud and are powered by entirely open-source technology. They are flexible, customizable, powerful, and can run on a variety of cloud infrastructure. They are designed to accelerate research, enhance education, and promote collaboration. They also give you full control over your infrastructure.

<p class="highlight">2i2c believes that transformational science and education should be built on open-source, community-driven, vendor-agnostic tools.
</p>

{{% callout note %}}
Want a hub for your usecase? If you're in research and education and you'd like a 2i2c hub for your use-case, we will soon be launching pilot projects to support people like you. Check out [our contact page](https://2i2c.org/#contact) to stay in touch.
{{% /callout %}}

## 2i2c Hubs are controlled by their community

2i2c's goal is to serve research and educational communities with their own interactive computing infrastructure running in the cloud. This means that all 2i2c Hubs...

- Can be run on a variety of cloud infrastructure - even on your own cloud accounts.
- Run entirely open source tools and standards - you can take your workflows wherever you wish.
- Are customizable for your community - provide the libraries, datasets, cloud connections, and resources that fit your need.
- Are scalable and robust - the technology behind our hubs has been served for communities as small as 2 and as large as 10,000 over the years.
- Are yours to control - manage your hub yourself or even move it to another provider - you control your infrastructure.

## What is in a 2i2c Hub?

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
  figure src="/img/2i2c-hub-overview.png"
  title="2i2c Hubs build on open source tools for infrastructure and datascience"
  width="70%"
>}}

## 2i2c Hubs support other languages and interfaces too

2i2c Hubs are flexible and can provide a variety of interfaces and languages. Jupyter is a language-agnostic platform, and can supports [kernels in a variety of languages](https://github.com/jupyter/jupyter/wiki/Jupyter-kernels). 2i2c Hubs can be customized for one or more open source languages and environments.

Don't want to use a Jupyter interface? No problem - JupyterHub can serve user interfaces of many kinds - whether it is RStudio, VSCode, or even a remote desktop GUI - basically any interface that can run via a web browser can run with a 2i2c Hub.

## Benefits of using open infrastructure

Using open infrastructure has several advantages:

- Open tools are the most **powerful, flexible, and dynamic** tools for learning, research,
  and collaboration.
- Open tools give you the freedom to **run on many kinds of infrastructure**. They can
  provide quick access to fast environments, large datasets, or high-powered compute.
- Open tools **avoid vendor lock-in** - JupyterHub can be deployed anywhere, by anyone.
  The stack it powers can run on a variety of vendor infrastructure, or your own
  computer. You can run the entire 2i2c stack on your own if you wish!
- Open tools are **standards in data science**. They are ubiquitous across academia and industry,
  and using them will help you connect with the broader research and education community.
- Open tools align with the **values of research and education**. They rely on contributions
  from a broad, diverse, and large OS community that is made up of many stakeholders
  dedicated to creating public goods.
- Open tools make research and education **more accessible to all**

2i2c integrates an entirely open stack with hosted infrastructure that is tailored for research and
education, running in the cloud infrastructure of your choice. It also contributes
back to the communities that develop and grow these tools, keeping the ecosystem
healthy.

## Open tools that we use and support

2i2c believes that open source infrastructure and tools are the best choice for researchers and educators. It also believes in giving back to these tools and their communities to ensure that they continue to thrive. 2i2c provides support, maintenance, and development for the following set of tools. It is always looking for more opportunities to contribute back to the open source community.

<div class="project-figures">
{{< figure
    target="https://jupyter.org"
    src="https://jupyter.org/assets/nav_logo.svg"
    title="<p class='project-title'>Jupyter Notebooks</p><p class='project-caption'>Interactive documents for research and education.</p>"
    class="project-highlight"
>}}

{{< figure
    target="https://jupyterlab.readthedocs.io/en/stable/"
    src="https://avatars3.githubusercontent.com/u/22800682?s=400&v=4"
    title="<p class='project-title'>Jupyter Lab</p><p class='project-caption'>A customizable and extensible data science interface</p>"
    class="project-highlight"
>}}

{{< figure
    target="https://jupyter.org/hub"
    src="https://jupyter.org/assets/hublogo.svg"
    title="<p class='project-title'>JupyterHub</p><p class='project-caption'> Cloud-based computing environments for groups</p>"
    class="project-highlight"
>}}

{{< figure
    target="https://numfocus.org/sponsored-projects"
    src="/img/pydata-ecosystem.png"
    title="<p class='project-title'>The PyData Ecosystem</p><p class='project-caption'> Open Source tools for Scientific Computing</p>"
    class="project-highlight"
>}}

{{< figure
    target="https://jupyterbook.org/intro.html"
    src="https://jupyterbook.org/_static/logo.png"
    title="<p class='project-title'>Jupyter Book</p><p class='project-caption'>Interactive, beautiful books with Jupyter</p>"
    class="project-highlight"
>}}


{{< figure
    target="https://docs.dask.org/en/latest/logos.html"
    src="https://docs.dask.org/en/latest/_images/dask_horizontal.svg"
    title="<p class='project-title'>Dask</p><p class='project-caption'>Advanced parallelism for analytics</p>"
    class="project-highlight"
>}}
</div>
