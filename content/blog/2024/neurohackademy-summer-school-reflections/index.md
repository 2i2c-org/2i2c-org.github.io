---
title: NeuroHackademy Summer School Reflections
date: "2024-08-19"
authors: ["Ariel Rokem", "Noah Benson", "Jenny Wong"]
tags: [bioscience, education]
categories: [impact]
featured: false
draft: false
---

_Thank you to Ariel Rokem for guest writing this blog post!_

![Group photo from NeuroHackademy 2024](featured.png "Group photo from NeuroHackademy 2024")

## What is NeuroHackademy?

Part summer school, part free-wheeling hackathon, all focused on the use of data science methods in neuroscience, NeuroHackademy is an event that was recently hosted by the [University of Washington eScience Institute](http://escience.washington.edu/) in Seattle, WA, USA. This event, that has been running annually since 2016, aims to provide early-career researchers in Psychology, Medicine, Neuroscience, and other related fields with the skills and knowledge that they need to effectively and rigorously work with open source tools and workflows for analyzing human neuroscience data. This supports the effort to make scientific analysis and results shareable, reproducible, and accessible.

## Global and inclusive

In 2020, the event had to rapidly pivot to an online format, and this format was also used in 2021. Through this experience, the organizers ([Ariel Rokem](https://arokem.org/) and [Noah Benson](https://nben.net/)) realized that many participants preferred the online format. For example, participants who could not afford to travel to Seattle, or participants who had care-taking responsibilities that precluded them from participating in a two-week event away from their homes.  In 2022, the event pioneered a hybrid format, where half of the participants are present in-person and half join the event via zoom, slack, GitHub, and of course through a dedicated 2i2c JupyterHub. Taken together, this format allows the participation of students from a larger range of backgrounds and locations. This aspect plays an important part in building a global and inclusive community of practice. See the paper [Hands-On Neuroinformatics Education at the Crossroads of Online and In-Person: Lessons Learned from NeuroHackademy](https://pubmed.ncbi.nlm.nih.gov/38763989/) to read more on this subject.

## Collaboration with 2i2c

### Previous years

NeuroHackademy has been an early adopter of the cloud-based JupyterHub model, setting up its first hub using the zero-to-jupyterhub guide in 2018. NeuroHackademy partnered with 2i2c as soon as it was founded, and 2i2c has operated a JupyterHub for the last 3 years. The hub provides an interactive computing platform for learners, and implements the "digital watering hole" for practical and immediate access to a range of cloud-based datasets in human neuroscience (see [blog post](blog/2024/NeuroHackademy-summer-school/index.md) announcing support for this year's event).

In terms of the software environment, the following tools and features that have benefited the event over the years include

- [`nbgitpuller`](https://github.com/jupyterhub/nbgitpuller) allows students to synchronise lesson content with an organizational GitHub repository that is collaboratively maintained by the lesson instructors.
- [Shared data file storage](https://docs.2i2c.org/user/topics/data/sharing/) with read-only access for learners and read-write access for instructors
- Access to an abundance of neuroimaging data hosted in cloud object storage
  - [The Human Connectome Project](https://www.humanconnectome.org/)
  - [The Natural Scenes Dataset](https://naturalscenesdataset.org/)
  - [OpenNeuro](https://openneuro.org/)
    - [The Healthy Brain Network](https://fcp-indi.s3.amazonaws.com/index.html#data/Projects/HBN/)
    - And more.
### This year

This year 2i2c supported the following tools and features for NeuroHackademy

- A "Bring your own image" option where users can pull any image hosted on a container registry into the hub. See our [Integrating BinderHub with JupyterHub: Empowering users to manage their own environments](blog/2024/jupyterhub-binderhub-gesis) blog post for more details.
- [`repo2docker`](https://github.com/jupyterhub/repo2docker) and GitHub actions to build and prototype images from a repository.
- The support services provided by 2i2c and the ability for instructors to [open pull requests on 2i2c infrastructure](https://infrastructure.2i2c.org/contributing/community-partner/) for speedy resolution.
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