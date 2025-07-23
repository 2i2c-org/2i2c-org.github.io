---
title: "2i2c's submissions to JupyterCon 2025"
subtitle: ""
authors: ["The 2i2c team"]
tags: ["open source", "jupyter", "community"]
categories: ["impact"]
date: "2025-07-19"
featured: false
draft: false
---

We were excited to hear that [JupyterCon is happening again in 2025](https://jupytercon.com). The Call for Proposals just wrapped up, and our team was involved in preparing and submitting several directly from 2i2c as well as from the ecosystem in general.

> **Note**: Many of these submissions were written in collaboration with others in the open-source projects we participate in. Particularly, in [JupyterHub](https://compass.hub.jupyter.org) and [JupyterBook](https://compass.jupyterbook.org).

## JupyterHub: A multi-user server for Jupyter notebooks

This is how JupyterHub was described when it was announced in 2015, 10 years ago. The focus was on bringing Jupyter Notebooks to multiple users on shared infrastructure. The Jupyter Notebooks focus was so strong that Jupyter was even in the name of the project! Fast forward 10 years, & this is still the most common perception of JupyterHub.

However, this has not been true for a *long* time now. Instead of setting up 5 different kinds of infrastructure to support your users based on what kind of *interface* they like to use ([JupyterLab](https://jupyterlab.readthedocs.io/), [RStudio](https://posit.co/products/open-source/rstudio/), Linux Desktop tools like [QGIS](https://qgis.org/) or [Napari](https://napari.org/), [Visual Studio Code](https://code.visualstudio.com/), full `ssh` (!?), etc) for their interactive computing, you can set up a JupyterHub that supports all of those! Meet your users where they are, rather than force them to conform to using only a specific set of tools.

Come to this talk to:

- See cool demos of various popular applications running on JupyterHub seamlessly
- Understand the security model of JupyterHub & how that enables these cool demos
- Learn how you can set up your own application to run in JupyterHub
- Influence the future of how JupyterHub is marketed

## Cloudy with a Chance of Savings: Per-User Usage and Cost Monitoring for JupyterHubs in the Cloud

Cloud cost monitoring is moving beyond just preventing runaway cost explosions – it's about empowering JupyterHub administrators with the guardrails they need to run efficient, transparent, and sustainable infrastructures. A cloud cost bill can show a broad view of services and machines provisioned, but how can we provide granular insights into each user and the value they are deriving from the hub on an application level?

We've developed several open-source components towards answering this question:

- **Metric Collection** – [Prometheus](https://prometheus.io/) collects resource usage metrics (including CPU, memory, and storage) from individual user pods via standard and custom exporters.
- **Cost Estimation** – Usage is correlated with AWS cost data to estimate per-user costs.
- **Visualization** – [Grafana](https://grafana.com/) dashboards display rich, interactive views of usage and cost data, making it easy to monitor trends, identify high-cost workloads, and generate reports for funders and decision-makers.

This approach delivers cloud observability and cost transparency that can be reliably deployed using [Kubernetes](https://kubernetes.io/) and integrated with [Zero to JupyterHub](https://z2jh.jupyter.org/) distributions.

## Controlling home directory costs (with user empathy) on the cloud with jupyterhub-home-nfs

User home directories on JupyterHubs deployed in cloud providers has been a pain point for both end users and administrators. Administrators feel the pain of cloud costs for home directory storage (sometimes higher than compute!). No user wants to receive an email saying "well, this code you copy pasted downloaded 3TB of netcdf files into your home directory, and now we have used up our entire team's cloud budget for the next 2 years" (true story).

The [jupyterhub-home-nfs](https://github.com/2i2c-org/jupyterhub-home-nfs) open source project is a JupyterHub native, cloud agnostic solution to these problems. Administrators can do per user limits, tune performance, report on usage and make cloud cost conscious choices around overprovisioning. It provides users empathetic guardrails to prevent them from overuse, rather than punitive gates that zap them after the fact.

In this short talk, we will:

- Describe the core of the problem, and how it manifests for users and admins.
- Review current solutions and their limitations
- Introduce jupyterhub-home-nfs and how it moves the solution space forward
- Demo how this looks like for an end user
- Talk about future direction, and opportunities for collaboration

## Rebuilding user trust in `mybinder.org`

Have you clicked a [mybinder.org](https://mybinder.org/) link, waited for it to start and gave up after it took far too long to start? Or just failed?

Have you stopped using mybinder.org for your tutorials, repositories and presentations because you could no longer rely on it to work each time?

mybinder.org is open infrastructure run by incredible volunteers (who go above and beyond constantly) in the Jupyter community. Is 'slow fade into unreliability' just the fate of all openly run infrastructure?

But perhaps maybe, just maybe, you have tried doing that again recently, & noticed improvements! Launches are more reliable. Faster. The UI looks better. Maybe things are getting better?

This talk will go through the problems facing mybinder.org & what we are doing about it. Come to this talk to find out:

1. How is mybinder.org run?
2. What are the structural issues facing open infrastructure services like mybinder.org?
3. What sustainability experiments are we running to improve reliability and rebuild user trust?
4. Has reliability actually improved?
5. How can I help?

## Can your JupyterHub handle your workload? Performance testing with `jupyterhub-simulator`

Your JupyterHub is all set up, and you're excited to use it for your workshop of 60 students. Or your class of 600 students. Or your research group of 5 people with complex workflows.

You *feel* your infrastructure should hold up fine, but do you *know* if your infrastructure will hold up fine? Is that just excitement, or is there a little bit of nervousness in there too? Wouldn't it be nice to test and know for sure?

`jupyterhub-simulator` is an open source project that allows you to describe what you expect your users to be doing - starting servers, clicking on [nbgitpuller](https://github.com/jupyterhub/nbgitpuller) links, running notebooks, etc. Once you have described it, you can then simulate any number of users doing that workflow simultaneously, and verify that your JupyterHub can handle that workload. If it can't, tweak your infrastructure and try again until it does!

In this talk you will learn:

- What is `jupyterhub-simulator`?
- How can I describe my expected workflow?
- How can I test if N users can do this workflow all simultaneously?
- How can I visualize the performance of my infrastructure so I can tweak its configuration and try the simulation again?

## Not just for notebooks: JupyterHub in 2025

> JupyterHub: A multi-user server for Jupyter notebooks

This is how JupyterHub was described when it was announced in 2015, 10 years ago. The focus was on bringing Jupyter Notebooks to multiple users on shared infrastructure. The Jupyter Notebooks focus was so strong that Jupyter was even in the name of the project! Fast forward 10 years, & this is still the most common perception of JupyterHub.

However, this has not been true for a *long* time now. Instead of setting up 5 different kinds of infrastructure to support your users based on what kind of *interface* they like to use ([JupyterLab](https://jupyterlab.readthedocs.io/), [RStudio](https://posit.co/products/open-source/rstudio/), Linux Desktop tools like [QGIS](https://qgis.org/) or [Napari](https://napari.org/), [Visual Studio Code](https://code.visualstudio.com/), full `ssh` (!?), etc) for their interactive computing, you can set up a JupyterHub that supports all of those! Meet your users where they are, rather than force them to conform to using only a specific set of tools.

Come to this talk to:

- See cool demos of various popular applications running on JupyterHub seamlessly
- Understand the security model of JupyterHub & how that enables these cool demos
- Learn how you can set up your own application to run in JupyterHub
- Influence the future of how JupyterHub is marketed

## Introducing Jupyter Book 2.0

This is a community talk from the [Jupyter Book team](https://compass.jupyterbook.org/team), detailing the principles behind the new [MyST Document Engine](https://mystmd.org/) and [Jupyter Book 2's upcoming release](https://next.jupyterbook.org). We'll share the text when the Jupyter Book team posts it publicly.

## What 2i2c has learned while trying to build sustainable relationships with Jupyter's community.

2i2c is a non-profit organization that fosters co-creation and collaboration between science communities and open source communities. We are deeply embedded in an international network of research and education communities, as well as open source communities that underlie their infrastructure (particularly in the Jupyter ecosystem). Our technical infrastructure is built entirely with open source components that we contribute to, but do not control. This is a really hard problem to solve!

We've learned a lot in the first four years of our existence. This talk will describe how our organization approaches a healthy and productive open source relationship with the Jupyter (and broader scientific python) ecosystem. It'll cover some of the major mistakes we've made, lessons learned, and where we think we've had impact. We aim to make this talk full of practical learnings that others can follow in building sustainable open science organizations that contribute to a healthy and vibrant open source ecosystem. Our goal will be to provide inspiration to others that are interested in building on top of open source projects like Jupyter, and want to do so in a way that is healthy and sustainable. 