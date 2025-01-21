---
title: "Designing for an ecosystem: a case study in cross-project open source contribution"
date: "2025-01-21"
authors: ["Chris Holdgraf", "Angus Hollands"]
tags: [open source]
categories: [impact]
featured: false
draft: false
---

A key challenge in the open source space is that projects are often independent and autonomous, with relatively few formal ways to collaborate and coordinate efforts. While this usually isn't a big deal, it means that there is a missed opportunity to grow the impact of an ecosystem because it requires coordinated development among multiple stakeholders within it.

This is one of the reasons we created 2i2c's open community hub platform. By deploying a single platform that utilizes entirely open infrastructure that we contribute back to, we have visibility over a variety of projects along with the need to combine them together for a specific end-user outcome. One-such development scenario recently came up involving [Jupyter Book 2][jb2] and [JupyterHub](https://jupyterhub.org/).

## Allowing readers to "bring their own Binders"

We've recently been working to integrate [Jupyter Book 2][jb2] workflows with our community hubs for a more seamless experience (for example, having book pages link back to interactive cloud sessions that allow users to interact with the content). We imagine a network of Jupyter Books that all build upon the same core infrastructures (JupyterHub, Binder, etc) for cloud-based computing. Our hope is to allow a user to _bring their own Binder_ with them so that they can interact with another book's content with their own cloud infrastructure. For example:

- A student with access to `binder.myuniversity.edu` could read a Jupyter Book created by a professor at `otheruniversity.edu`.
- The Jupyter Book is defined with a [Binder specification](https://repo2docker.readthedocs.io/en/latest/specification.html) that has a recipe for re-building the environment needed to run te book's content.
- From the professor's book, the student can choose to launch an interactive Binder sessions on _their university's Binder_, allowing them to interact with the book's content on their own infrastructure.

We want a workflow like this to be as seamless and un-complicated as possible. We also want it to follow the same fundamental workflow as the [nbgitpuller-based launch buttons](https://docs.2i2c.org/community/content/). Along the way, we realized that we needed to coordinate development across [Jupyter Book 2][jb2]], [JupyterHub](https://jupyter.readthedocs.io), and [BinderHub](https://binderhub.readthedocs.io).

{{< figure src="./images/featured.png" caption="The three projects (Jupyter Book, BinderHub, and JupyterHub) that needed to work together to enable 'bring your own binderhub' workflows." >}}

## Getting Jupyter Book to discover Jupyter Hub

As we began developing this workflow, we realized that there was a blocker in the JupyterHub and BinderHub ecosystem that needed to be fixed. We needed a way to **ask a JupyterHub whether it had an unauthenticated end-point for service discovery**. Basically, a way to ask a hub "what kind of hub are you, and how can we launch an interactive session on you?" Doing this is simple-enough - JupyterHub already has a way of reporting its version and application type, which allows us to infer how to launch interactive sessions. But, we hit a snag in an HTML context.

By default, JupyterHub disallows certain kinds of [Cross-Origin Resource Sharing](https://developer.mozilla.org/en-US/docs/Web/HTTP/CORS) (CORS) requests, in order to restrict other applications from abusing a JupyterHub's API. If you hit parts of a JupyterHub API from _the command line_, things work fine. But if you do the same thing via JavaScript from a website, the request is disallowed. This was a problem if we want Jupyter Book (a web application) to be able to make requests of JupyterHub's API.

So, we realized that we needed to make an **upstream contribution in JupyterHub** in order to **enable an interaction between JupyterHub and Jupyter Book**. In this case, it was a relatively simple fix: allowing CORS requests for the specific API endpoint we needed (which is a very lightweight endpoint that is not vulnerable to security risks, and is broadly useful to make accessible)[^1]. That resulted in two PRs:

- https://github.com/jupyterhub/jupyterhub/pull/4966 allows CORS requests for the API that was needed for service discovery in JupyterHub.
- https://github.com/jupyterhub/binderhub/pull/1906 enables this workflow on a BinderHub so that its services can be discovered.
- https://github.com/jupyter-book/myst-theme/pull/503 adds new launch button functionality to [Jupyter Book 2][jb2] that allows readers to bring their own Binder / JupyterHub links for launching. (this is what necessitated the above two PRs)

[^1]: This actually required an interesting bit of team discussion that was much easier with a few 2i2c staff on the JupyterHub team. The original request from Angus was interpreted as opening up the _entire hub API_ to external requests (which is a bad idea!) but we were able to quickly discuss this with the JupyterHub team to clarify that this was only about a very specific API endpoint. This is the kind of communication loop that often goes haywire when you have people contributing to a project without historical relationships to the project's maintainers.

As a result of this upstream contribution loop, JupyterHub can now accept API requests at its "service discovery" endpoint, which means that Jupyter Book (and any other web application) can more easily learn about a hub's capabilities and version.

We wanted to share this short vignette because it's a good reflection of the kind of value that 2i2c tries to provide, given its role in helping to build and enhance networks of infrastructure, domain communities, and open source communities. In this case, we enabled a _cross-project_ workflow that required knowledge of each project, and a vision for how they could be used together in a way that exceeded the sum of their parts.

We think there's a lot more potential in these kinds of workflows, and are eager to continue our work to identify and enhance community-centric infrastructure for interactive computing.

[jb2]: https://next.jupyterbook.org/

