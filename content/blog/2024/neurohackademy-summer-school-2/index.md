---
title: NeuroHackademy Summer School Reflections
date: "2024-08-19"
authors: ["Ariel Rokem", "Jenny Wong"]
tags: [bioscience, education]
categories: [impact]
featured: false
draft: false
---

_Thank you to Ariel Rokem for guest writing this blog post!_

![Landing page of the NeuroHackademy Summer School website](featured.png "[NeuroHackademy Summer School](https://NeuroHackademy.org/)")

## What is NeuroHackademy?

NeuroHackademy is a summer school hosted by the [University of Washington eScience Institute](http://escience.washington.edu/). The school is aimed at providing students with skills to work with open source tools and workflows for analyzing human neuroscience data in an effort to make scientific analysis and results shareable, reproducible, and accessible.

## Global and inclusive

The hybrid format of the summer school that allows the participation of students from all backgrounds. This aspect plays an important part in building a global and inclusive community of practice. See the paper [Hands-On Neuroinformatics Education at the Crossroads of Online and In-Person: Lessons Learned from NeuroHackademy](https://pubmed.ncbi.nlm.nih.gov/38763989/) to read more on this subject.

## Collaboration with 2i2c

### Previous years

2i2c has operated a JupyterHub for the last X years that provides an interactive computing platform for learners (see [blog post](blog/2024/NeuroHackademy-summer-school/index.md) announcing support for this year's event).

In terms of the software environment, the following tools and features that have benefited the event over the years include

- [`nbgitpuller`](https://github.com/jupyterhub/nbgitpuller) allows students to synchronise lesson content with an organizational GitHub repository that is collaboratively maintained by the lesson instructors.
- [Shared data file storage](https://docs.2i2c.org/user/topics/data/sharing/) with read-only access for learners and read-write access for instructors
- Access to an abundance of neuroimaging data hosted in cloud object storage
  - [The Human Connectome Project](https://www.humanconnectome.org/)
  - [The Natural Scenes Dataset](https://naturalscenesdataset.org/)
  - [OpenNeuro](https://openneuro.org/)

### This year

This year 2i2c supported the following tools and features for NeuroHackademy

- A "Bring your own image" option where users can pull any image hosted on a container registry into the hub. See our [Integrating BinderHub with JupyterHub: Empowering users to manage their own environments](blog/2024/jupyterhub-binderhub-gesis) blog post for more details
- [`repo2docker`](https://github.com/jupyterhub/repo2docker) and GitHub actions to build and prototype images from a repository
- The support services provided by 2i2c and the ability for instructors to [open pull requests on 2i2c infrastructure](https://infrastructure.2i2c.org/contributing/community-partner/) for speedy resolution
- GPU instances to support more compute intensive workloads for machine learning.

### Next year

We are pleased that learners have made great progress in making use of cloud-native, open-source workflows for analyzing human neuroscience data. We are keen to benefit from lessons learned this year and are looking forward to collaborating with 2i2c once again to deliver the NeuroHackademy Summer School in 2025.

One thing we have learned is that 2i2c automatically [shuts down a user server after one hour of inactivity](https://docs.2i2c.org/admin/howto/control-user-server/#stop-user-servers-after-inactivity) by default to ensure efficient resource usage and limit runaway cloud costs. Naturally, we are seeing increasing demand from learners for longer and more complex analyses. In response to this, we are keen to explore how the [`jupyter-keepalive`](https://github.com/minrk/jupyter-keepalive) extension can keep the server alive for long-running processes.

Watch this space next year!

## Acknowledgements

Funded by grant [R25MH112480](https://pubmed.ncbi.nlm.nih.gov/38763989/) from the US National Institute of Mental Health awarded to [Ariel Rokem](https://arokem.org/) and [Noah Benson](https://nben.net/).

The NeuroHackademy Summer School is sponsored by

- [University of Washington eScience Institute](http://escience.washington.edu/)
- [Gordon and Betty Moore Foundation](http://www.moore.org/)
- [Alfred P. Sloan Foundation](http://sloan.org/)
- [University of Washington](http://www.washington.edu/)
- [The University of Texas at Austin](https://www.utexas.edu/)
- [National Institute of Mental Health](https://www.nimh.nih.gov/)
- [National Science Foundation](https://www.nsf.gov/).

## References

- [NeuroHackademy2024 GitHub Organization](https://github.com/NeuroHackademy2024)
- [Hands-On Neuroinformatics Education at the Crossroads of Online and In-Person: Lessons Learned from NeuroHackademy](https://pubmed.ncbi.nlm.nih.gov/38763989/)