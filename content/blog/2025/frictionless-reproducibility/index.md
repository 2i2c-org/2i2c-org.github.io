---
date: 2024-12-16
title: Towards frictionless reproducibility with BinderHub and 2i2c
---

<style>
  figure iframe {
    margin-left: auto;
    margin-right: auto;
  }
  figure {
    display: flex;
    flex-direction: column;
    margin-left: auto;
    margin-right: auto;
    max-width: 500px;
  }
</style>

2i2c has been experimenting with ways to enable communities to share their work with one another more effectively. This post is an exploration of the basic workflow we're interested in, how it could be enabled with open technology in the Jupyter ecosystem, how it might fit in with the broader ecosystem of services around scientific communication, and how we might try to sustain it.

## The core pieces of data-driven discovery

For any individual to ask questions and create knowledge with data, they need access to a few key resources in order to do their work.

- **Data** is the raw material that drives computational ideas.
- **Computation** provides the core hardware for manipulating data with code.
- **Software** the tools that code uses to leverage data and computation for specific outcomes.
- **Code** utilizes software and computation to reproduce a computation.
- **Narrative** allows all of the above to be communicated in a compelling and understandable way.

**Jupyter**'s goal is to weave all of the above together with an ecosystem of tools that are modular, flexible, and interoperable. **2i2c**'s [community hub platform](/platform) gives community leaders the ability to integrate and customize all of these resources to be useful for particular communities in research and education. This usually comes in the form of a **Jupyter Book** to teach communtiy workflows to users, with connections to a **JupyterHub** that provides the data, compute, and software tools needed for data-driven discovery.

{{< figure src="images/discover.png" title="2i2c community hubs use Jupyter technology to help members learn community workflows, and access all the resources needed for a community's data-driven discovery.">}}

## Sharing ideas means sharing computation to reproduce them

When a community member discovers something new, they want to share it with others in their community. This is usually an ongoing process by which community members are giving information and receiving information in return to iteratively drive their exploration and development.

These ideas are driven by data and computation, and so it is critical to **share the resources needed to reproduce the computation** when sharing new ideas with community members. This allows others to reproduce the main ideas in order to validate the core claims, as well as interact with the code and software to better understand and build upon the ideas.

We can leverage cloud infrastructure to facilitate this process. At a basic level, community hubs are a good way to standardize the software and resource environment so that content produced in one user's session can be easily reproduced by another user. [nbgitpuller](https://nbgitpuller.readthedocs.io/en/latest/) is the most common tool for distributing content within a JupyterHub. As long as the content was made on a JupyterHub, and shared with another user on the same hub, they'll be able to get their own copy and interact with it.

{{< figure src="images/share.png" title="The simplest sharing workflow uses nbgitpuller to distribute content via links that community members click. Doing so will give them their own copy of the content running in the hub's environment.">}}

## Sharing computational environments means being able to (re)build them

However, many authors need more control over the environment needed to reproduce a computation. For example, they might need a _specific version_ of a software package, or they may need a non-standard library that isn't available on their community hub's base environment. How can they share their computational narratives in a way that _bundles the environment_ with the content?

This is what [**the Binder Project**](https://mybinder.org) was built for. It provides a tool called [BinderHub](https://binderhub.readthedocs.io/en/latest/), which is an **engine for sharable, reproducible computational environments**. It allows an author to package up their computational narratives and code, and share access to a cloud environment that allows readers to reproduce and interact with the computation.
Earlier this year our team has been prototyping how to [connect BinderHub services with a JupyterHub](../../2024/jupyterhub-binderhub-gesis/) and how to [deploy BinderHub services alongside each of our community hubs](../../2024/nasa-ephemeral-hubs/).
Doing so would allow community members to **build an environment needed to reproduce their computation and share it via their hub**.

{{< figure src="images/reproduce.png" title="BinderHub allows an author to package narrative, code, computational resources, and a software environment into a link that others can use to access a fully reproducible environment for their ideas.">}}

## Empowering communities to bring their own reproducibility when publishing

When community members have a big idea that they'd like to share more formally, want to **publish** rather than just **share**. Publishing is more structured, invites particular kinds of feedback, and requires more quality assurance. There's a huge ecosystem of publishers and services that support formal publishing, and they ensure things like discoverability, long-term archivability, versioning, peer review, DOI referencing, etc.

However, publishers don't have access to the core infrastructure used to make the original discovery, nor do they have the expertise to manage this kind of infrastructure. But 2i2c's community members already have a reproducible environment where they've been doing their discovery. Could we leverage this infrastructure for publishing?

2i2c has an opportunity to empower publishers to reproduce computational ideas by **allowing authors to bring their reproducible environments with them**. By leveraging the same core technologies, authors can re-use their hub infrastructure to provide the resources needed for reproducibility.

This would require treating a community's hub as an **external service for reproducibility** that could be leveraged by one of the many publishing platforms out there. For example, [Curvenote](https://curvenote.com) already builds heavily on the Jupyter and MyST ecosystems and could use a community's hub to provide interactivity to a Curvenote document. Authors could publish pre-prints on [Biorxiv](https://www.biorxiv.org/) that included Binder links back to their community hub [Binder links in arxiv has already been piloted with the Loren Frank lab and HHMI](../../2024/hhmi-spyglass-mysql/)). Larger publishers like [PLOS](https://plos.org/) could allow authors to provide metadata about BinderHubs that can reproduce their content, and weave this into their user interface for displaying publications. These are all _possible_ outcomes that haven't been realized, but I don't think they'd be that far off.

{{< figure src="images/publish.png" title="We could re-use the same tools for data-driven discovery to facilitate the reproducibility of computational narratives and publications. The same core infrastructure could be re-used to provide comptutational environments that are re-used in a variety of publishing tools and services. (note this is all hypothetical, no-such service integrations yet exist, and these are just a sample of relevant publishing organizations in this space)">}}

The best part is that the BinderHub provider could be anybody - if a community had their own capacity to manage Binder infrastructure they could do so, or they could use a service provider like [2i2c](https://2i2c.org) to manage it for them. In this way, a community could leverage its pre-existing infrastructure to provide reproducibility for published scholarly work.

There's a lot that we could do to remove the friction from workflows like the above. It should be **as easy as possible for publishing stakeholders to interface with a community's BinderHub** and integrate it into publishing services and products. This is especially true for more modern publishing platforms like [Curvenote](https://curvenote.com) that are already built on the Jupyter and MyST ecosystems. The more integrated a publisher's infrastructure is with modern computational technology, the more power they should be able to get out of an author's reproducible environment.

<figure>
<iframe width="560" height="315" src="https://www.youtube.com/embed/Y5KuIskstB4?si=XWcRsCvQiKtoxaRk" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>
<figcaption>

A demo of [interactive documents with Thebe](https://readthedocs.org/thebe/en/latest/), which is the tool that power's [Curvenote](https://curvenote.com)'s live computational documents. Services like Curvenote could power interactivity with a community-managed BinderHub service.

</figcaption>
</figure>

## How to sustain these services?

This brings up an important question: how would you sustain services like these? mybinder.org is built as an entirely free service both to build and to use environments. This is massively accessible, but is not scalable nor sustainable. Would community stakeholders pay for privileged access to BinderHubs that could reproduce and share their computational narratives? Would publishers be willing to pay a percentage of the cloud and management costs associated with reproduction?

One thing seems clear - there is an imperative to make reproducibility and interaction frictionless. This is both to ensure the scientific integrity of the work being done, and also to make computational ideas more accessible to the world. Technologies and service partnerships like these can help ensure the broader communitys right to reproduce the work of others.

Some of these ideas were recently explored in a talk recorded for [AGU 2024](https://agu.confex.com/agu/fm24/meetingapp.cgi/Paper/100644).

<figure>
<iframe width="560" height="315" src="https://www.youtube.com/embed/D5s2HbaulZw?si=GCeDPpr2WobIuu4w" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>
<figcaption>
A talk from 2i2c team member [Jim Colliander](https://2i2c.org/author/jim-colliander/) discussing the right to reproduce computational ideas, the importance of enabling frictionless reproducibility, and how we might sustain such a service.
</figcaption>
</figure>

## Concluding thoughts

Much of the above is already possible, if a little bit clunky to execute. However, given the growing interest in open infrastructure, iterative science, and improving the publishing ecosystem, I'm hopeful that we'll have opportunities to build these service connections soon. I'd love to those from the more "formal" side of scholarly publishing to understand where these ideas have holes or significant new development. I'd also love feedback on sustainability models to ensure these services can be relied on as part of the publishing ecosystem. In the meantime, hopefully these ideas serve as an inspiration for what is possible, and where we might be heading with 2i2c's service and the broader Jupyter ecosystem.