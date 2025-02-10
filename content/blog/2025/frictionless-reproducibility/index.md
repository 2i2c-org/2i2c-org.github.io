---
title: "Towards frictionless, portable, and sustainable reproducibility with Binder"
date: 2025-02-10
comment: |
  Figures are here: https://docs.google.com/presentation/d/1ApnGswakl2U_OUzYxSOSis3V-DbmR8EsJhO-DZ7MuLk/edit#slide=id.g33066a3c77c_0_0
--- 

Last December I had an opportunity to discuss the current and future state of the open publishing ecosystem at a workshop hosted by [HHMI](https://www.hhmi.org). While 2i2c doesn't primarily focus on "publishing" workflows, we do support communities on a journey that often _leads to publishing_, and we make choices about technology in our [community hub platform](../../../platform/) that can support different kinds of publishing outcomes.

After listening to folks across the open science and publishing ecosystem, I noticed a common challenge:

- Publishers care about **reproducibility** of computational narratives and the **interactivity** that computation can provide.
- But they **lack the capacity to manage computational infrastructure** in a way that is flexible enough for all of their authors.

This led to a bit of brainstorming at 2i2c, and this post is a reflection on how ecosystems like Jupyter and an infrastructure provider like 2i2c could fit into a broader publishing ecosystem.

## Could Portable Computation be a service for the publishing industry?

Many of 2i2c's communities already care about reproducibility and sharing their computational narratives. That's one reason that we've [been improving reproducible environment sharing with Binder](../../2024/jupyterhub-binderhub-gesis/), [integrating Jupyter Book into our community cloud platform](../../2024/jupyter-book-2/), and [supporting the mybinder.org federation](../TODOBINDERBLOGPOSTLINK).

However, communities often want to **publish** rather than just **share**. Publishing is more structured, invites particular kinds of feedback, and requires more Quality Assurance. There's a huge ecosystem of publishers and services that support formal publishing, and they ensure things like discoverability, long-term archivability, versioning, peer review, DOI referencing, etc.

This introduces a challenge, because the reproducible environments that communities use to _do their work_ exist on _their infrastructure_, not the publisher's. This makes sense, because publishers aren't data science infrastructure providers, but it means the environments are inaccessible to publishers. For communities in 2i2c's network, **could JupyterHub and Binder allow users to bring reproducible environments with them in a way that publishers could leverage for interactivity and reproducibility?**

This would entail treating a community's hub as an **external service for reproducibility** that could be leveraged by one of the many publishing platforms out there. It would require making improvements around a few different areas of Jupyter:

- **JupyterHub** and **BinderHub** would need improved workflows around external authentication so that services could easily request kernels from a hub.
- **Jupyter Book** and **MyST** would need the ability to power computation on a page from a variety of computational back-ends, potentially defined by a user (e.g., via [Thebe](https://thebe.readthedocs.io/en/stable/) and some UI design in Jupyter Book).
- **Jupyter Lab** and other user interfaces may need improved ways for defining and sharing their environments and their content to use tools like Jupyter Book and Binder.

We'd also need **integration work** for the various publishing systems out there to leverage this technology for their infrastructure. This is a significant lift - a lot of publishers use *very old* and bespoke technology in their systems. However, there's also hope that a subset of the publishing ecosystem is ready to try things like this.

## There are many publishing organizations innovating with open source

I also learned that **there's a lot of interest in innovating around publishing workflows**, and a general interest in **building on top of open source communities and standards**. We don't need the whole industry to move at once (it won't), but we do need a critical mass of organizations who are interested in innovating. I think that enough of those organizations exist.

We recently piloted [running a BinderHub for Biorxiv publications with the Loren Frank lab and HHMI](../../2024/hhmi-spyglass-mysql/), and found this to be a nice proof-of-concept. While the "published article" lives on [Biorxiv](https://www.biorxiv.org/), the computational infrastructure and environment is provided by a BinderHub (in this case managed by 2i2c, but anybody could manage a hub in this way).

{{< figure src="images/reproduce-biorxiv.png" title="The Biorxiv Binder pilot workflow. An author used a 2i2c-managed BinderHub to generate a reproducible environment for their paper. They included a link to this environment in the abstract. Readers could click this link, and be taken to a fully interactive environment to explore the ideas in the paper and reproduce its computation.">}}

This was a nice proof-of-concept, though I think that broader adoption of this type of workflow would require a deeper connection between publisher workflows and open source communities.

A publishing platform with more immediate potential is [Curvenote](https://curvenote.com), which already builds heavily on top of the Jupyter and MyST ecosystems. Curvenote builds largely around the [MyST Markdown document engine](https://mystmd.org), which means they could more easily integrate improvements around Portable Computation in the Jupyter ecosystem. Here's a brief video of Rowan Cockett (Curvenote's CEO) discussing their platform and how it integrates with ideas of continuous, open science.

<figure>
<iframe width="560" height="315" src="https://www.youtube.com/embed/tpn7tGzFpfk?si=M06DEWfg2IQbn3CF" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>
<figcaption>

A demonstration of [Curvenote](https://curvenote.com) 's vision for continuous science and publishing at the FORCE11 2024 conference. This shows off Curvenote's use of open source tools like [MyST](https://mystmd.org) and [Thebe](https://thebe.readthedocs.io). Allowing communities to re-use their computational environments from a JupyterHub could make it easier to provide the computation and data infrastructure for demonstrations like these.
</figcaption>
</figure>

Curvenote is exceptionally good at interfacing with open source, and I hope that the broader publishing ecosystem moves in this direction as well. Because Jupyter is largely based around open standards and protocols, it should be possible for publishers to leverage the BinderHub API and the [Reproducible Execution Environment Specification](https://repo2docker.readthedocs.io/en/latest/specification.html) to integrate computation that powers their reproducible articles. 2i2c often plays a role in _bridging user communities and open source communities_ through cycles of development and collaboration, perhaps we could do the same for the publishing community. 

{{< figure src="featured.png" title="Publishers could re-use the computational environments from a community's hub, resulting in a de-duplication of infrastructure and effort, and bridging the gap between where a community does its work, and where it submits new ideas for pubication. (note these are hypothetical for now, but we think publishing platforms like these are a good starting point!)" >}}

Integrating with publishing in this way would allow communities to leverage their pre-existing infrastructure as part of their scholarly workflows. If a community had their own capacity to manage Binder infrastructure they could do so, or they could use a service provider like [2i2c](https://2i2c.org) to manage it for them. This would distribute the responsibility of infrastructure management to those who are in the best position to do so - the communities that do the work.

## How could we sustain the cost of running computation for published articles?

This raises an important question: how would you sustain services like these? Communities are already nervous about the cost of computation for their workflows. Public services like [mybinder.org](https://mybinder.org) are free and accessible, but not scalable, nor suitable for complex or mission-critical workflows[^scale]. Would community stakeholders pay for privileged access to BinderHubs that could reproduce and share their computational narratives? Would publishers be willing to pay a percentage of the cloud and management costs associated with reproduction? Could we use this to sustain a larger public service like mybinder.org?

[^scale]: The costs associated with running [mybinder.org](https://mybinder.org) have historically been shouldered by donations from organizations such has [OVH](https://ovhcloud.com), [Google](https://google.com), [GESIS](https://notebooks.gesis.org/), [Curvenote](https://curvenote.com), and now [2i2c](https://2i2c.org). These donations are not guaranteed, and do not scale directly with the number of users.

We don't have any answers yet but we're keen to try. Our colleague Jim Colliander recently explored some of these ideas in a talk recorded for [AGU 2024](https://agu.confex.com/agu/fm24/meetingapp.cgi/Paper/100644).

<figure>
<iframe width="560" height="315" src="https://www.youtube.com/embed/D5s2HbaulZw?si=GCeDPpr2WobIuu4w" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>
<figcaption>

A talk from 2i2c team member [Jim Colliander](https://2i2c.org/author/jim-colliander/) discussing the right to reproduce computational ideas, the importance of enabling frictionless reproducibility, and how we might sustain such a service.

</figcaption>
</figure>

One thing seems clear - there is an imperative to make reproducibility and interaction frictionless. This is both to ensure the scientific integrity of the work being done, and also to make computational ideas more accessible to the world. Technologies and service partnerships like these can help ensure the broader community's right to reproduce the work of others.

## Exploring Frictionless Portable Computing at 2i2c

It should be easy for communities to **bring their hub computing environments with them** to power interactive narratives in their published work, or to **integrate with publisher workflows**. Much of the above is already possible, if clunky to execute. However, given the growing interest in open infrastructure, iterative science, and improving the publishing ecosystem, I'm hopeful that we'll have opportunities to build these service connections soon. We'd like to explore some tooling improvements that lay a foundation for these workflows, and will report back on our experiments in the coming months.

**If anybody is interested in collaborating with us**, [please reach out](mailto:hello@2i2c.org). We'd love to hear from organizations from the scholarly publishing community to understand where these ideas have holes or need significant new development. I'd also love feedback on sustainability models to ensure these services can be relied on as part of the publishing ecosystem. In the meantime, hopefully these ideas serve as an inspiration for what is possible, and where we might be heading with 2i2c's service and the broader publishing ecosystem.
