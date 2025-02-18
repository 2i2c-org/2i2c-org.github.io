---
title: "2024 impact report: new team structure, new funding, and growth in our network"
date: 2024-12-08
authors:
  - Chris Holdgraf
tags:
  - report
categories:
  - organization
featured: false
draft: false
---

2024 has been a busy year for 2i2c, with many highs and lows, a lot of impact, and significant organizational change. As the year comes to an end, I want to reflect on the work we've done in 2024, and where we aim to go in 2025.

In 2024, 2i2c reached the point in an organization's lifecycle when a team has grown enough in size and complexity that you must change the ways that you organize. The informal ways that worked as a small group don't suffice anymore, and you have to put more effort into aligning and coordinating everyone to ensure you have the same impact.

I call this the "$1M to $2M budget jump", because organizations seem to hit this point around when your annual budget goes from `$1M` to `$2M`. Getting to the other side of this gap with an intact runway and team is hard, and I suspect that 2i2c's fully distributed nature means that we hit these scaling milestones earlier than many organizations. For us, this has been a major focus of effort all year, and has involved taking a top-to-bottom look at our plans and ways of working as a team. Read on for more details about major updates, challenges, and impact that our team had in 2024.

## Organizational updates

At an organizational level, this year had a lot of introspection and planning, a few new roles, a few departing team members, a funding crunch, a successful effort to dig out of it, and a new system of work organizing our team. We'll share more about all of this later, but here are the major implications for our team:

**We've raised another $2.2M in funding** to support our efforts in scaling and sustaining our network of community hubs. This gives us roughly another 2 years of projected runway (with some assumptions about revenue from contracts and grants). Below are two posts that describe two major awards we were awarded in Q3 and Q4 of this year:

- **[A one-year award from the Chan Zuckerberg Initiative](/blog/2024/funding-czi/)**.
- **[A two-year award from The Navigation Fund](/blog/2024/funding-navigation/)**.

**We've designed and hired several strategic and systems-level roles** to give our team support and direction as it grows. Here's a brief summary:

- **[Head of Product, Giuliano Maciocci](/authors/giuliano-maciocci/)**. Giuliano leads our efforts to define and steward our value proposition and the roadmap of development for products and services that feeds into it. Giuliano has 10+ years experience driving growth in companies, was the ex-Chief Product Officer at Ex Ordo, ex-head of Product at eLife Sciences where he led the open science product [Executable Research Article](https://elifesciences.org/collections/d72819a9/executable-research-articles), and contributed significantly to mobile design and innovation at Adobe.
- **[Chief of Staff and Delivery Manager, Harold Campbell](/authors/harold-campbell/)**. Harold leads our delivery and operations efforts, and stewards our system of work and coordination around it to ensure we deliver on our commitments efficiently and reliably. Harold has 15+ years of industry experience spanning companies in Africa and Jamaica, and 10+ years experience in agile consulting and coaching in technical and product teams.
- **[People Lead, April Johnson](/authors/april-johnson/)**. April leads and stewards our system to support our team as individuals, ensuring that we provide the guidance and support needed to grow our team members in their careers and skills. April has 20+ years growing and guiding technology organizations. She is the ex-Global Head of Transformation at Thoughtworks (Europe, Latin America, India, North America, and Asia), with expertise in human-centered design, agility, people leadership, change, leading remote and asynchronous agile teams, coaching, and non-profit development.

**We've re-organized our team into separate product and business development teams**, in order to focus on _providing an excellent technical platform and a collection of services that maximizes community impact_, as well as _sustaining this service for our communities_. This has allowed us to more effectively coordinate our service enhancement and development efforts, and increases our ability to deliver improvements to our communities and to upstream projects.

As a result, our organization has a much stronger foundation to build upon as we continue to grow and refine our sustainability model in 2025. It has positioned us to more effectively deal with the challenges in reaching our next milestones for scale and impact, and gives us the tools to be more adaptive and responsive to community needs.

Along the way, we also generated a lot of impact through our collaborations with communities in our network, and in the upstream projects that we support. For more details about our impact, see the summaries below.

## Community impact

2i2c's core mission is to support its network of communities that create and share knowledge with open infrastructure. Here are the highlights of how our community network has grown and had impact.

First, we've grown our network of hubs and users through several new partnerships. We **grew the number of active hubs from ~75 to ~105**, and **grew our end-of-year Monthly Active Users (MAUs) from ~6000 to ~8000**.

{{< figure
  src="images/maus.png"
  width="75%"
  caption="You can see an interactive version of these numbers in our platform usage dashboard: https://2i2c.org/kpis/cloud/"
>}}

Beyond the numbers, we also re-focused our team on reporting impact stories from our collaborations with community members, and have published these into a (growing) list of posts on our blog:

{{< figure
  src="images/impact-gallery.gif"
  width="75%"
  caption="Our impact gallery is a new place to share stories of our impact with user research communities as well as open source communities: https://2i2c.org/category/impact/"
>}}

Here are a few community highlights from this year:

- We served around 20 communities from Latin America and Africa for the [**Catalyst project**](https://2i2c.org/blog/2024/catalyst-partner-highlights/)
- Our community partner [**Openscapes** were invited to the White House](https://openscapes.org/events/2024-09-26-openscapes-whitehouse/) to discuss the importance of open science
- The [**NeuroHackademy** used our infrastructure](http://2i2c.org/blog/2024/neurohackademy-summer-school-reflections/) to support their annual summer school
- We enabled [ephemeral and sharable interactive computing environments for the **Amerigeo workshop**](http://2i2c.org/blog/2024/amerigeo-workshop/) in the geospatial community
- We ran a [pilot for an **HHMI-affiliated open source project called Spyglass**](https://2i2c.org/blog/2024/hhmi-spyglass-mysql/) for reproducing their pre-print with a live interactive environment using BinderHub to support publishing infrastructure
- We began a [collaboration with **Development Seed** around the **NASA VEDA** project](https://2i2c.org/blog/2024/veda-devseed-collab/), to support them with interactive cloud environments for geospatial research
- Several members in our community network [showed off their work at **AGU 2024**](https://2i2c.org/blog/2024/agu/)
- We [co-organized a workshop alongside **Project Pythia**](https://2i2c.org/blog/2024/project-pythia-cookoff/) to create computational narrative content for geospatial analytics, and upgrade their stack to Jupyter Book 2.0

## Open source technology enhancements

Our second pillar of impact is to improve the ecosystem of open infrastructure and the open science workflows it enables. We use collaborations with our community partners to drive new cycles of development in open source tools that we support. Here's a brief overview of our impact across the open source ecosystem this year.

In 2024, 2i2c team members [authored **over 500 pull requests**](https://github.com/search?q=author%3Acholdgraf+author%3Aharoldcampbell+author%3Aaprilmj+author%3Acolliand+author%3Ajmunroe+author%3Ajnywong+author%3AGman0909+author%3AconsideRatio+author%3Ageorgianaelena+author%3Asgibson91+author%3Ayuvipanda+author%3Aagoose77+org%3Ajupyter+org%3Ajupyter-server+org%3Ajupyterhub+org%3Ajupyterlab+org%3Abinder-examples+org%3Aexecutablebooks+org%3Acryptnono+org%3Adask+org%3Apydata+org%3Arocker-org+org%3Apangeo-data+org%3Ajupyter-book+is%3Apr+merged%3A%3E%3D2024-01-01&type=pullrequests) that were merged in our key open source communities communities. Find our list of key open source communities here:

https://compass.2i2c.org/open-source/key-communities/

Here are a few highlights where we focused our effort this year - each of these efforts required both development with and for our community network, as well as upstream contributions and support:

- We released [**JupyterHub Fancy Profiles**](https://2i2c.org/blog/2024/jupyterhub-fancy-profiles-rollout/), which allows for a more flexible and modern interface to launch environments with JupyterHub.

- We used this to allow users to [**build and launch custom environments in JupyterHub**](https://2i2c.org/blog/2024/nasa-ephemeral-hubs/) in a way that users can also share with others.

- We've added a Grafana dashboard for [**resource and cost monitoring with JupyterHub**](https://2i2c.org/blog/2024/aws-cost-attribution/) to give communities more visibility over their projected cloud costs.

- We began [**incorporating Jupyter Book 2.0 workflows into our community hubs**](https://2i2c.org/blog/2024/project-pythia-cookoff/) and laid a foundation for enabling our communuty networks to communicate with one another more effectively using the new MyST document engine. Read more in our [blog post about Jupyter Book 2.0](https://2i2c.org/blog/2024/jupyter-book-2/).

- We built [**`frx-challenges`**](https://2i2c.org/blog/2024/frx/), a tool to help communities host data challenges with secure, automated evaluation of submissions. This was built in collaboration with the [**HHMI Cellmap Challenge**](https://cellmapchallenge.janelia.org/) competition.


## Looking to next year

2025 is going to be a critical year for 2i2c to build upon the work we began in 2024 to achieve a more sustainable and scalable community model. Here are the main areas that will guide our work in the new year and into 2026, pulled from our [recent proposal from The Navigation Fund](/blog/2024/funding-navigation/index.md):

- **Goal #1: Delivery**. Develop the operating structure and team skills to
efficiently scale our product and service delivery.
- **Goal #2: Product**. Develop a product system that continuously improves and
delivers value and impact at scale.
- **Goal #3: Sustainability**. Build a business model that is competitive and gives
us resources to sustain and scale our service.

These are the key goals 2i2c must achieve in order to ensure that its service remains impactful, sustainable, scalable, and accessible. We believe that we've laid a strong foundation to get there, and are excited to begin work next year.

Overall, 2024 has been a challenging, but also a rewarding year for our team. We've encountered and successfully worked thorugh a number of scaling challenges, and we've made significant progress at laying a foundation on which we can build for the years to come.

I'm incredibly proud of 2i2c's team for all of their hard work this year, and also honored to be working with a network of communities that care about open infrastructure and its value for creating and sharing knowledge with the world. Here's to another year of impact!

