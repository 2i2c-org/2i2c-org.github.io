---
title: "Hello World"
subtitle: ""
summary: ""
authors: ["Chris Holdgraf"]
tags: [meta]
categories: [organization]
date: 2020-11-10
featured: false
draft: false
aliases:
 - /posts/hello-world
---

👋 hey everyone!

We'd like to announce the creation of a new non-profit organization[^1] that we call **2i2c**.

[^1]: **EDIT 08-2021: We are now a fiscally-sponsored project of [Code for Science and Society](https://codeforscience.org) and ICSI is no longer our host organization. We are leaving this section here for archival purposes, and to give credit to ICSI for their help in launching 2i2c**. 2i2c's host organization is the [International Computer Science Institute](http://www.icsi.berkeley.edu/), a 501(c)(3) charitable organization. We thank ICSI for its collaboration and leadership in launching 2i2c! 


2i2c stands for **The International Interactive Computing Collaboration**. It is a non-profit dedicated to making open tools for interactive computing more accessible and more powerful for the research and education communities.

This is a short post about why we created 2i2c, what we hope that it will do, and what we are up to next. If you'd prefer to watch a video instead of read a blog post, check out [this talk about 2i2c](https://cfp.jupytercon.com/2020/schedule/presentation/209/2i2c-sustaining-open-source-through-hosted-jupyter-infrastructure-for-research-and-education/) at JupyterCon 2020:

{{< youtube YjonPLxDiwM >}}

## Why create 2i2c?

The founding team of 2i2c has spent the last several years running projects that use interactive computing for research and education, including [bringing data science education to thousands of students](/founders#datahub), connecting [geospatial researchers with large datasets and computational resources in the cloud](/founders#pangeo), and providing [federated online environment hubs to schools across Canada](/founders#syzygy), to name a few.

Over time we realized that, while infrastructure for interactive computing could be a huge benefit to research and education, it also required a fair amount of expertise to configure, deploy, and develop. We wished for other organizations to enjoy the same success that we had found, but learned that for many, deploying their own infrastructure was a non-starter to adoption. Instead, many were turning to proprietary or vendor-specific tooling.

We created 2i2c so that these organizations can use entirely open-source tools without hiring and training their own dev-ops and infrastructure talent, and so that _development_ and _support_ of open tools for interactive computing continues to represent the interests of research and education.

## Why a non-profit?

It may sound strange to create a non-profit initiative when there are many VC-funded startups and large tech companies offering notebook services these days. However, we think that a non-profit organization is the right approach to balance the interests of all the stakeholders that we wish to serve. We hope that 2i2c will be a partner to:

- **Research and educational communities**, who can rely on 2i2c to provide them cutting-edge infrastructure for interactive computing that is 💯 open source.
- **Researchers and educators who need development**, who can rely on 2i2c as a collaborator that offers development and expertise in open-source infrastructure to push the cutting edge of interactive computing in the cloud.
- **Open source communities**, who can count on 2i2c support and grow the communities that underlie the tools that we deploy.
- **Cloud providers**, who wish to help the research and educational community via their infrastructure.
- **Supporters of open source** who wish to support interactive computing for research and education via a non-profit dedicated to exactly this mission.

As a non-profit initiative, 2i2c is dedicated to supporting an ecosystem of tools and stakeholders across the open source community, and to ensuring that those tools are well-suited for research and education. We believe strongly in mission-driven work, and non-profit status will ensure that the work that we do is always aligned with our mission and values.

## What are we going to do?

With all of that in mind, what is 2i2c actually going to do? We are still working out the details, but here's a rough picture:

Offer [**hosted interactive computing environments on cloud infrastructure**](/infrastructure). These will [be entirely open source](/right-to-replicate) and vendor-neutral, and customizable for the communities that are using them. They'll be offered either as a fee-for-service model and/or subsidized through grants and donations. We wish to build upon the success of JupyterHub as a gateway to computational resources and environments, learning environments, and communities of users. For more information about the vision and values of our hosted infrastructure, see [the 2i2c **Right to Replicate** document](/right-to-replicate).

Provide [**collaboration and development for interactive computing in research and education**](/infrastructure#research-development-hubs). Beyond providing hub infrastructure, there are many ways in which solving problems in research and education can lead to better tools, infrastructure, and workflows in the open source community. For example - how can we generalize a community's solution to scalable computing so that it can be useful for other use-cases as well? We hope that 2i2c can be an aggregator and integrator of many perspectives in research and education, and build tools that are maximally useful across communities.

Provide [**core development and community support**](/open-source) for open source projects that we use. While many organizations *use* Jupyter technology in their projects, it is also crucial that they *give back* to those tools in order to keep the ecosystem healthy. As a mission-driven non-profit, 2i2c has a core goal in not only deploying and customizing open source tools, but also providing core support for them.

## Next steps

2i2c is a young organization, but we already have a few exciting ideas to work towards in the coming months. Here's an idea of what we'll be up to next.

Our first step is to **understand how interactive computing can best-serve the research and education communities**. We know that interactive computing tools work in our specific use-cases, but how do these generalize to other domains or types of organizations? Moreover, how can we improve the open source tools to make them even more customizable for each community?

We'll begin answering this question through several focused JupyterHub pilots aimed at different use-cases across research and education:

1. **A "Hubs for All" pilot for education**. This will focus on making standard educational environments via JupyterHub accessible to a broad range of educational institutions, in particular, traditionally under-resourced institutions such as community colleges, state colleges, and HBCUs.
2. **Research-focused hubs for earth analytics**. Research requires more complex and customized infrastructure than education, and so we are piloting hub infrastructure for a few specific research communities to understand how we can meet their needs. We will use this to better-understand how 2i2c and support a diverse research community in the future.
3. **JupyterHub development for the Pangeo Project**. Pangeo has been a collaborator of 2i2c since day one, and we love its vision for large-scale earth analytics via cloud infrastructure. We plan to work closely with Pangeo leadership to work on early development of tools aimed at facilitating scalable computing for research on Pangeo infrastructure. More information about this to come soon.

We'll also use these pilots to **develop an organizational sustainability model** around this infrastructure. It takes expertise to manage and develop cloud infrastructure, and 2i2c wishes to pay market rates for its engineers. How can 2i2c offer services and development in a way that is sustainable both for itself and for other institutions? We'll use these pilots to create a plan for both sustaining and scaling 2i2c's ability to serve institutions and teams.

## What do we need?

As a non-profit initiative, 2i2c has a long road ahead of it. We cannot take venture capital funding, so we have to raise funds the old-fashioned way. This means that:

- If you are at an organization interested in purchasing hosted JupyterHub environments from 2i2c, please [send us an email <i class="fas fa-envelope"></i>](mailto:hello@2i2c.org).
- If you are a funder or are otherwise interested in supporting 2i2c with a donation or grant, please [send us an email <i class="fas fa-envelope"></i>](mailto:hello@2i2c.org).
- If you have experience in sustaining service-based organizations such as 2i2c, and wish to offer your expertise or guidance, please [send us an email <i class="fas fa-envelope"></i>](mailto:hello@2i2c.org).

Moreover, we'll likely be hiring in the coming months for open source engineers, with a  focus on data science, interactive computing, and the cloud. If you're interested in working for an organization like 2i2c, please [send us an email <i class="fas fa-envelope"></i>](mailto:hello@2i2c.org), and keep an eye on this space as we will post more information soon.

## Get involved

If you'd like to get involved with the 2i2c team and community, we recommend two pathways for doing so.

[Subscribe to our mailing list](https://docs.google.com/forms/d/e/1FAIpQLSdW_bhVrXfgRYa9Ct6w399KQPILbU_3nKUF_tgnGZJbs91SXg/viewform?usp=sf_link). We'll use this to periodically send updates about what 2i2c is up to.

[Join the 2i2c Slack](https://forms.gle/f3rmHZCijK3bYAaA8). We use Slack for team conversation, as well as for real-time conversations about tools, practices, and ideas around interactive computing for research and education.

You can also say hello to us on Twitter at [@2i2c_org](https://twitter.com/2i2c_org).

## Wrapping up

We are excited about 2i2c, and believe that it is the right kind of organization to create to support research and education, as well as open source communities in interactive computing. The road ahead is a difficult one, but we're confident that we will hit our stride quickly. Stay tuned for more updates to come.
