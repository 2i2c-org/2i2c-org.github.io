---
title: "Pilot hubs, new collaborations, and new team members - A six month update"
summary: ""
authors: ["Chris Holdgraf"]
tags: []
categories: [organization]
date: 2021-05-25
featured: false
draft: false
aliases:
 - /posts/six-month-update
---

It has been about six months since 2i2c first began operations (after receiving [funding from the Chan Zuckerberg Initiative](../czi-core-support)).
In that time we've made progress along several directions, and wish to use this blog post to provide updates about the ways in which 2i2c has evolved over the first months of its existence.

Below are a few major updates from the 2i2c community - as always, if you want to learn more about 2i2c, keep an eye [on our blog](/posts) or subscribe to the [2i2c mailing list](/#contact).

## Early pilot JupyterHub infrastructure

First off - we have been making progress building out our JupyterHub deployment infrastructure for 2i2c.
One of our major organizational goals is to build a sustainable service [managing open source cloud infrastructure](/infrastructure) for interactive computing.
This service will provide hosted, customized JupyterHubs for communities of practice in research and education.
They'll be built entirely with open source tools that are community-driven, and that [respect the customer's Right to Replicate](/right-to-replicate).

In order to accomplish this, 2i2c is running several pilots with partners and interested organizations, supported by our [funding from CZI](/posts/czi-core-support), as well as from [the JROST rapid response fund](https://investinopen.org/blog/jrost-rapid-response-fund-awardees/).
These pilots are meant to be learning opportunities to understand what kind of infrastructure and service it needs to build moving forward.

The [documentation for our pilot hubs infrastructure](https://devops.2i2c.org/en/latest/) contains information about our deployments and infrastructure.
It is served from [this `2i2c-org/pilot-hubs` repository](https://github.com/2i2c-org/pilot-hubs), a centralized location for configuring and deploying a federated network of JupyterHubs.
Each JupyterHub is independent of one another, and could be spun out from the centralized repository with minimal extra work, giving hub users the ability to [replicate their infrastructure, with or without 2i2c](/right-to-replicate).
We will continue refining the code in this repository as we learn more from our hub infrastructure pilots.

## JupyterHub for geospatial analytics - A collaboration with Pangeo

As [originally announced on the Pangeo blog](https://medium.com/pangeo/pangeo-2-0-2bedf099582d), 2i2c is forging a collaboration with [the Pangeo project](https://pangeo.io) around operating and developing cloud infrastructure for large-scale geospatial analytics!
This collaboration is funded through a grant from the Moore Foundation (via Pangeo investigator Ryan Abernathey).

Over the coming months, 2i2c plans to assume operation of infrastructure underlying the Pangeo project, allowing the Pangeo team to focus their efforts on their core scientific and development missions.
Because Pangeo's infrastructure is already running on a fully open source stack with JupyterHub, our first step will simply be to shift control over this infrastructure to 2i2c engineers.
We don't anticipate needing to make major changes to their infrastructure and deployments (part of the benefits of using open, modular tools).

Once this is complete, we'll next shift our attention to some new areas of development that support use-cases in the Pangeo community (and in the scientific community more broadly).
There's a lot of progress that we imagine making - such as [supporting publishing pipelines via the Pangeo Gallery](https://gallery.pangeo.io) or improving tools for scalable computing with [Dask Gateway](https://gateway.dask.org/).
We'll provide updates as we formally begin this collaboration and hash out a plan for our next steps.

## JupyterHub for education - A collaboration with CloudBank and UC Berkeley

In addition, we've begun a partnership with the UC Berkeley [Data Science in Undergraduate Studies program](https://data.berkeley.edu/academics/undergraduate-programs), as well as [CloudBank](http://cloudbank.org/).
This collaboration aims to provide hosted JupyterHub infrastructure for community colleges across the state of California.
It is an attempt at providing vendor-agnostic and open-source infrastructure to several institutions who would otherwise not be able to deploy this infrastructure on their own.

2i2c will provide the deployment and configuration architecture for this collaboration, working with [Sean Morris](https://its.berkeley.edu/people/sean-morris) in operating this educational infrastructure.
All of the cloud infrastructure for this pilot will be funded via CloudBank.
We will begin by offering environments that are modeled after [the Data 8 course at UC Berkeley](https://data8.org).
This is part of an effort to build a community of practice around Data Science education using open source tools.

## New team members

We've also welcomed two new members to the 2i2c core team! 🎉

These individuals will both work towards [2i2c's major projects](/projects), and collaborate together on running our 2i2c Pilot Hub infrastructure.
Here's a bit about each new team member.

- [Damián Avila](https://github.com/damianavila). Damián has been a Jupyter core team member for many years now, and has done work across many different parts of the PyData stack (in particular, [Jupyter](https://jupyter.org), [Bokeh](http://bokeh.org/), [RISE](https://rise.readthedocs.io/), and [Nikola](https://getnikola.com/)). Damián will focus his efforts on supporting JupyterHub infrastructure for the [Pangeo project](https://pangeo.io), as well as development across the [Executable Books Project](https://executablebooks.org)
- [Sarah Gibson](https://github.com/sgibson91). Sarah will join 2i2c in June, after spending several years as a Research Software Engineer at [the Turing Institute](https://www.turing.ac.uk/). She has also been involved with [the Turing Way](https://the-turing-way.netlify.app/welcome) for many years. Sarah will focus her efforts on JupyterHub development and operations for the Pangeo community.

## Governance and a code of conduct

Finally, while it's easy to get lost in technology and collaborations, 2i2c has also made important steps towards defining a stable and transparent organizational model moving forward.
2i2c now [has a Steering Council](https://team-compass.2i2c.org/en/latest/about/structure.html#steering-council) and an [early organizational structure](https://team-compass.2i2c.org/en/latest/about/structure.html).
In addition, [we've defined a one-year bootstrap strategy](https://team-compass.2i2c.org/en/latest/about/strategy.html) that we'll use to guide our path in the first year of 2i2c's existence.

Finally, one of the first acts of the Steering Council has been to [adopt a Code of Conduct](https://team-compass.2i2c.org/en/latest/code-of-conduct/index.html).
This is a set of guidelines, and a process for resolving incidents, that makes our community more inclusive, equitable, and enjoyable for all.
Creating a Code of Conduct is a crucial part of defining our organizational and community culture, and we're excited to have some explicit guidelines to support our interactions in the future!

## Keep in touch

Now that we are improving our organizational foundation, we will try to post more frequent updates and discussions about what we are up to.
We hope for 2i2c to be a model organization in participatory, collaborative, transparent operations, and we look forward to working with you all in the future on this journey.
