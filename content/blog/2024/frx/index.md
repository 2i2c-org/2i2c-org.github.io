---
title: "`frx-challenges`: A new tool to host data challenges for Frictionless Research Exchanges"
date: 2024-12-06
tags:
  - open-source
categories:
  - service
authors:
  - Chris Holdgraf
  - Yuvi Panda
---

2i2c is pleased to announce the `frx-challenges` project, a new open source tool to help communities host data challenges on shared infrastructure:

https://github.com/2i2c-org/frx-challenges

This project aims to make it easier for administrators to provide a service that enables users to **submit code and data** that are **evaluated on secure infrastructure with access to private data and resources**. It also provides a leaderboard that helps users compare their performance against others.

{{< figure
  src="images/leaderboard.png"
  width="75%"
  caption="An example leaderboard for a data challenge, taken from the [Cellmap Challenge](https://cellmapchallenge.janelia.org/). Users make submissions that are run against secure and private infrastructure and data, and provides feedback about the submission's performance. Learn more about the FRX challenges project here: https://2i2c.org/frx-challenges/"
>}}

It is designed to be lightweight and flexible, and can be run on a variety of shared infrastructure. For those who wish to run this project on cloud infrastructure, we've also published a [Helm Chart to help you deploy `frx-challenges` with Kubernetes](https://2i2c.org/frx-challenges-helm-chart/).

While it can be run on its own, we believe that it naturally complements other tools and services for interactive computing and data, such as **JupyterHub**, **Jupyter Book**, and **Binder**. More on that below.

Below is a brief description of the motivation behind this project.

## What are Frictionless Research Exchanges

The project is heavily inspired by David Donoho's vision of **Frictionless Research Exchanges** (FRX) as described in [_Data Science at the Singularity_](https://arxiv.org/abs/2310.00865).

In this article, Donoho describes three key pillars for Frictionless Research Exchanges:

> The three initiatives are related but separate; and all three have to come together, and in a particularly strong way, to provide the conditions for the new era. Here they are:
>
> - [FR-1: Data] datafication of everything, with a culture of research data sharing. One can now find datasets publicly available online on a bewildering variety of topics, from chest x-rays to cosmic microwave background measurements to uber routes to geospatial crop identifications.
> - [FR-2: Re-execution] research code sharing including the ability to exactly re-execute the same complete workflow by different researchers.
> - [FR-3: Challenges] adopting challenge problems as a new paradigm powering scientific research. The paradigm includes: a shared public dataset, a prescribed and quantified task performance metric, a set of enrolled competitors seeking to outperform each other on the task, and a public leaderboard. Thousands of such challenges with millions of entries have now taken place, across many fields.

We considered the landscape of tools and services, and felt that [FR-1] and [FR-2] were already well-served by a variety of tools and services for community workspace infrastructure (e.g., JupyterHub: https://jupyterhub.readthedocs.io), sharable computational environments (e.g., BinderHub: https://binderhub.readthedocs.io), authoring and reading computational narratives (e.g., Jupyter Book: https://jupyterbook.org and MyST: https://mystmd.org), and data I/O tools and standards (e.g., Zarr: https://zarr.readthedocs.io and Intake: https://intake.readthedocs.io). 

However there was a natural missing piece for **[FR-3 Challenges]**, and we could not identify any community-managed infrastructure that facilitated data challenges. This is the goal of `frx-challenges`.

## Why facilitate data challenges?

Data challenges are harder than you think! While it is simple enough to run somebody else's code locally, data challenges require a systematic, secure, and automated approach to accepting and evaluating submissions in a fair and repeatable way. Here are some of the big challenges to tackle:

- **Submissions must retain user and team identity**, which means that we must keep track of users and their submissions over time, since data challenges are designed to encourage iterative improvement and optimization.
- **Evaluations must use potentially complex resources and data** since many data challenges operate by publicly sharing a small dataset, and then running it against a much more complex dataset.
- **Evaluations must be totally secure**, so that submissions can't do nefarious things like mine cryptocurrency or extract the challenge's private data in unintended ways.
- **Evaluations must be automated**, so that running the challenge does not require extensive human intervention and can scale to many users.
- **Evaluation must be flexible**, so that the infrastructure can accept a variety of types of submissions (e.g. code, data, model weights, etc), run them with arbitrary environments designed by the organizers, and run them with the right hardware to get the job done.

These are just a few of the major challenges that we've tried to address with `frx-challenges`, and we're excited to see how it goes with our first assisted community challenge: the [Cellmap Challenge](https://cellmapchallenge.janelia.org/).

If you're interested in learning more or participating in this project, follow along at its GitHub repository:

https://github.com/2i2c-org/frx-challenges

This is still the **very early stages** of the project, and we imagine it will evolve significantly. We welcome feedback for how it can more effectively serve a variety of communities.

## Acknowledgements

Thanks to the [Howard Hughes Medical Institute](../../../collaborators/hhmi/) (HHMI) for collaborating with us on the [Cellmap Challenge](https://cellmapchallenge.janelia.org/), which led to the creation of this project.

Thanks to Kristen Ratan and [Strategies for Open Science](https://strategiesos.org/about/) (Stratos) for enabling this collaboration, and providing strategic guidance and support.