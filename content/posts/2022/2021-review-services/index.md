---
title: "2i2c’s first year, part 1: exploring Jupyter services."
subtitle: ""
summary: ""
authors: ["Chris Holdgraf"]
tags: []
categories: [updates]
date: 2022-01-25
featured: false
draft: false
---

Now that 2021 has come to an end, this marks the end of 2i2c’s first year of operations. In this year we have grown, experimented, and accomplished a lot - we have also faced challenges and learned as a team. Our primary goal in 2021 was to build a strong foundation for 2i2c.

To reflect on our work thus far, we're writing three blog posts that describe progress in major areas of work towards this foundation for 2i2c.
These three areas are:

- **Creating services for use-cases** - these are our first managed infrastructure offerings for communities in research and education.
- **Developing cloud infrastructure and tools** - this is the technical backbone that makes these services possible, built entirely on open source tools.
- **Building an organizational foundation** - this is the creation of our team structures, processes, and culture that help us carry out our mission.

This first post will focus on **services that we've created in our first year**.

Ultimately, 2i2c's mission is to facilitate use-cases in research and education via open source development and services. Throughout 2021 we ran several pilots to learn more about the needs of communities in research and education, and how we could build sustainable services that meet these needs. Here are some highlights for each major use-case we have targeted thus far:

## Educational community hubs

A primary use-case that 2i2c seeks to enable is **collaborative, distributed educational spaces for learning with data**. In 2021 we ran several pilots with educational communities:

**A university-wide hub for the University of Toronto.** This hub is used in a variety of classes throughout the university, and is made freely available to anyone with a UofT account. We hope to repeat this model for other university-wide communities, and have learned a lot about the challenges of working with particularly large educational communities.

**Several hubs for community colleges across California.** In partnership with UC Berkeley and CloudBank, we've run several hubs for nearly a dozen small community colleges teaching the [Data 8 curriculum](http://data8.org) for their students. These hubs are lightweight and offer standardized environments for their students to use, in order to lower the cost of deploying and maintaining the hubs over time.

### What we learned

The organizational context around educational use-cases is different from research communities. Compared with research groups, educucational groups have more variance in their size (classes as small as 10 people and as large as 500) and think about cost **by the student**, not as a lump sum. This means that our initial hub-based pricing model may not map cleanly onto educational contexts, and we need to improve the match of scalability and price to these communities.

Moreover, we've learned that for these communities, navigating all of the open source tools that are available for pedagogy is confusing! Everybody wants auto-grading but it's unclear what is the "right tool for the job". Tools like [nbgitpuller](https://jupyterhub.github.io/nbgitpuller/) have heavy use at "power universities" like UC Berkeley, but many others don't know that it exists! We will need to invest more time into building guides and documentation that help others leverage these tools.

## Research in the cloud

In addition to educational use-cases, we ran several pilots for research communities in order to leverage cloud infrastructure for scaling their work or collaborating more effectively.

**We migrated Pangeo’s cloud infrastructure to be run via 2i2c.** The [Pangeo Community](https://pangeo.io) had been operating and developing their own JupyterHub for several years, but were looking for another organization to provide more reliable/sustained operations and support for their Pangeo Cloud Service. This year we migrated the service [to run off of 2i2c’s deployment infrastructure](/posts/2021/pangeo-goes-live/).

**A scalable cloud hub for a SWOT satellite team**. The [MEOM research group at Grenoble](https://meom-group.github.io/projects/swot-st/) is doing work with the [NASA SWOT satellite project](https://swot.jpl.nasa.gov/). However, the datasets generated from this project are huge, and only storable via the cloud. We've set up a JupyterHub to provide cloud-based access to this data, running a Pangeo-like environment.

### What we learned

Research communities tend to have more usecase-specific needs than educational ones. While introductory courses in data science tend to be similar across institutions, research needs are much more unique to the problem and team at hand. Moreover, they tend to want infrastructure that runs via institutional cloud accounts. This is possible due to the flexible nature of Jupyter and JupyterHub, but brings extra challenges in bureacracy and access permissions, given that 2i2c engineers usually are not members of these organizations already.  

Additionally, many research use-cases are based around the **location of the data**. This is because data is the hardest thing to move from cloud to cloud. For this reason, it's important to **bring interactive sessions to the data**. Jupyter's ecosystem makes this possible, but we'd like to do more to make this easier. For example, users should be able to launch interactive sessions across many clusters or datacenters, regardless of their hub's location. They should also have more customized control over their environments.

## Distributed events and hackweeks

Finally, we had a special use-case that is a hybrid of the previous two examples. Events and hackweeks are _time-bounded_, _focused on learning and doing_, but often _with research workflows and communities_. They also tend to be more globally-distributed than a traditional research or education community.
See below for a few examples:

The [**Coastal Ocean Environment Summer School in Ghana**](https://coessing.org/) workshop is a summer school run in Ghana to share skills and workflows with researchers across Africa. It builds on workflows in the Pangeo ecosystem, and teaches attendees how to work with cloud-native data. By using a cloud-based JupyterHub for their workshop, attendees had direct access to data and compute in a way that would have been much more difficult to set up on local infrastructure.

The [**PaleoHackWeek hackathons**](http://linked.earth/paleoHackathon/) were two hackathons around paleo/climate data workflows. They brought together a distributed community and use the 2i2c hub to facilitate the use of the [paleoclim package](https://pyleoclim-util.readthedocs.io/en/master/) throughout the hackweek.

[**OpenScapes**](https://www.openscapes.org/) champions open practices in environmental science to help uncover data-driven solutions faster. They have several cohorts of scientific trainees learning more about adopting open and collaborative workflows, and use a hub managed by 2i2c to provide remote learning environments for their workshops.

### What we learned

Initially we assumed that event-based hubs would be similar to educational use-cases. However, in practice they are more complex. First, event organizers have ever-changing communities of users on their hubs. They often want to provide access to many new users in each event, and expect only a small subset to continue using the infrastructure after an event. Finally, one-off events also generate spikes in activity that are more intense than educational use-cases, and warrant more dedicated attention from our engineers.

## Challenges that we faced

As we piloted these use-cases, we also ran into a few challenges in designing services around our infrastructure.

**Balancing standard deployments, custom deployments, and scalability**. Our goal is to centralize our deployment and operations infrastructure in order to reduce the maintenance burden for each community hub. This will allow us to gain economies of scale and lower costs. However, there’s an inherent tension between scalability and customizability - in order to scale we must standardize the infrastructure we offer, but communities often want environments that are unique to their use-case.

**Turning services into sustainability**. We’ve learned that charging money for things does not come naturally to us. We’ve spent many years building technology and services that were offered freely to the public. This was easy to provide, but difficult to sustain. 2i2c’s goal is to offer similar services, but with a sustainability model that allows us to employ team members to do this work, and to grow in the future. Understanding how to pair the right technology, use-case, and service with a particular pricing model is an area where we must learn more.

## What’s next

Piloting all of these services taught us a lot about the similarities and differences between each use case. Towards the end of 2021, this led to 2i2c's first collection of "service offerings" for a Managed Jupyter Service. This includes a 2-by-2 matrix of service options, and a specific price point for each. We have begun offering this service to communities, in order to learn more about the model, the pricing, and any changes that should be made. In early 2022, we hope to expand this group to more communities so that we can test this model’s ability to scale.

Our next post in this series will focus on the underlying technology that powers the services described above, stay tuned for more!
