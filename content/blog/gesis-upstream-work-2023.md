---
# Documentation: https://wowchemy.com/docs/managing-content/

# TODO: Pick a better title, and update the file name to match
title: "All the upstream work from the GESIS grant"
subtitle: ""
summary: ""
authors: []
tags: []
categories: []
date: 2024-01-03T16:56:14-08:00
lastmod: 2024-01-03T16:56:14-08:00
featured: false
draft: true

---

TODO: Describe the Grant, and the goals we were trying to accomplish

TODO: A demo gif

TODO: Describe *what* we are trying to accomplish, *whom* we are trying to serve
Aiming for flexible components that are reusable accross many fields.

## TODO: Describe eventual architecture

JupyterHub - responsible for *running* user containers
BinderHub - responsible for *building* container images
`jupyterhub-fancy-profiles` - ties these together

## TODO: After this, describe all the work we have done in actually making this demo happen

### Standalone `binderhub-service` helm chart

The default upstream [binderhub helm-chart](https://github.com/jupyterhub/binderhub/tree/main/helm-chart) *includes* a JupyterHub as a dependency, and configures itself to be used primarily in a manner similar to [mybinder.org](https://mybinder.org). As the person who helped make that choice early on, I can tell you why it was made - for convenience! And it *was* very convenient, as it allowed us to get mybinder.org going fast. However, it makes it difficult to install a binderhub service *alongside* an existing JupyterHub, which we would need for our dynamic image building integration. To this end, we have created a standalone [binderhub helm chart](https://github.com/2i2c-org/binderhub-service/), designed to be installed *alongside* an existing JupyterHub! This allows the BinderHub instance to be used as a [JupyterHub Service](https://jupyterhub.readthedocs.io/en/stable/reference/services.html), which is what we want.

While this helm chart is currently under the 2i2c GitHub org, the hope is that it can eventually migrate to a [jupyterhub-contrib](https://github.com/jupyterhub/team-compass/issues/519) organization (once it is created), or it can become the upstream helm chart for binderhub if enough work can be put in to allow it to serve use cases like mybinder.org. Ongoing work is to be continued here.

### Allowing extending KubeSpawner's `profileList`

![A KubeSpawner profileList, allowing users to choose between various images as well as resource requirements](https://hackmd.io/_uploads/r1XKdJKmT.png)
*A KubeSpawner profileList, allowing users to choose between various images as well as resource requirements*

We identified KubeSpawner's `profileList` feature as the ideal location for implementing dynamic image building UI, making it just another 'image choice' people can choose, along with choosing the amount of resources their server needed. From an end user perspective, it was the logical place for them to specify a repository to build into an image, as they could already choose some pre-built images from here. They can also select other arbitrary resources they want (such as memory, GPU, etc) from here as well. From a developer perspective, it helped with long term maintenance too!

The implementation of `profileList` however, was not easy to extend at this point. So [this PR](https://github.com/jupyterhub/kubespawner/pull/724) was done to improve how easy it was to extend it in more complex ways, without making the implementation in KubeSpawner itself complicated. This had no visible effects for end users, but allowed us to move on to our next step!

### Implementing `unlisted_choice` feature in KubeSpawner

The profileList feature was built to allow JupyterHub *admins* to specify an explicit list of images / resources the end user can select from. It did not have a way for any image that was *not* pre-approved by the admin to be used. We had to safely add this feature to KubeSpawner in such a way that it was generally useful to everyone. Many other communities had been asking for such a feature anyway - the ability to simply 'type in' an image and have that be used.

[NASA VEDA](https://www.earthdata.nasa.gov/esds/veda) was one such community, so we partnered with [Sanjay Bhangar](https://github.com/batpad/) from [Development Seed](https://developmentseed.org/) (an organization that helps run NASA VEDA) to implement this feature. Engineers from 2i2c contributed heavily to this feature as well, and after *several* PRs ([1](https://github.com/jupyterhub/kubespawner/pull/735), [2](https://github.com/jupyterhub/kubespawner/pull/766), [3](https://github.com/jupyterhub/kubespawner/pull/773), [4](https://github.com/jupyterhub/kubespawner/pull/774) and [5](https://github.com/jupyterhub/kubespawner/pull/777)), this feature is now available for everyone to use!

![image](https://hackmd.io/_uploads/r1IquhRLp.png)


A key component of doing *sustainable* upstream work is that every addition needs to be useful by itself for a broad group of people. This change was very helpful for many communities that wanted to allow their users the freedom to pick whatever image they want to use, regardless of wether they wanted to use dynamic image building or not. The broad interest allowed us to build a coalition with other interested parties, and get the change accepted upstream more easily!

### `jupyterhub-fancy-profiles`

Once we had all these pieces in place, it was time to actually work on the frontend UI that would allow users to build images dynamically and launch them. Since this will replace the 'profileList' feature, it should also allow them to select different resources (RAM, CPU, etc) as needed, as well as type-in an existing image if they desire. So it was a full re-implementation of the profileList frontend.

This is ongoing now at the [jupyterhub-fancy-profiles](https://github.com/yuvipanda/jupyterhub-fancy-profiles) project. It is a pure frontend web application, using standard frontend tooling ([React](https://react.dev/), [webpack](https://webpack.js.org/), [Babel](https://babeljs.io/), etc) and written in JavaScript. It's gone through a few revisions, but the demo provided earlier in the blog post is its current state. Because the default profileList implementation is pure HTML / CSS with very *minimal* JS, it is limited in what kinda UX it could have. `jupyterhub-fancy-profiles` aims to be very helpful *even* when dynamic image building is not enabled on a JupyterHub. We hope to roll this out to a few JupyterHubs and improve it over time based on feedback.

### [`jupyterhub/@binderhub-client`](https://www.npmjs.com/package/@jupyterhub/binderhub-client) npm package

While building `jupyterhub-fancy-profiles`, we want to use the *same* javascript code used by BinderHub frontend to interact with the BinderHub API, instead of re-implementing it. However, the existing binderhub javascript code was not easily consumable by external projects. We refactored this, adding tests, migrating to use modern JS practices and published the [`jupyterhub/@binderhub-client` NPM package](https://www.npmjs.com/package/@jupyterhub/binderhub-client) that can be used not just by `jupyerhub-fancy-profiles` but any external project for talking to the binderhub API.

This had to be done in such a way that current binderhub installations (such as mybinder.org) do not break. That took quite a few pull requests: [1](https://github.com/jupyterhub/binderhub/pull/1689), [2](https://github.com/jupyterhub/binderhub/pull/1693), [3](https://github.com/jupyterhub/binderhub/pull/1694), [4](https://github.com/jupyterhub/binderhub/pull/1741), [5](https://github.com/jupyterhub/binderhub/pull/1742), [6](https://github.com/jupyterhub/binderhub/pull/1758), [7](https://github.com/jupyterhub/binderhub/pull/1761), [8](https://github.com/jupyterhub/binderhub/pull/1771), [9](https://github.com/jupyterhub/binderhub/pull/1773), [10](https://github.com/jupyterhub/binderhub/pull/1775), [11](https://github.com/jupyterhub/binderhub/pull/1778), [12](https://github.com/jupyterhub/binderhub/pull/1779), [13](https://github.com/jupyterhub/binderhub/pull/1781), [14](https://github.com/jupyterhub/binderhub/pull/1782), [15](https://github.com/jupyterhub/binderhub/pull/1783)

### `cryptnono` anti-abuse features

For Open Science to flourish, we need to allow access without login / paywalls wherever possible. A new menace against this has been [cryptojacking](https://www.interpol.int/en/Crimes/Cybercrime/Cryptojacking) - where attackers use up any and all available free compute to mine cryptocurrencies. This has affected *many* folks on the internet, including [GitHub Actions](https://www.bleepingcomputer.com/news/security/github-actions-being-actively-abused-to-mine-cryptocurrency-on-github-servers/) and mybinder.org, the primary public binderhub installation. mybinder.org has some extra protections against cryptojacking that aren't easily usable elsewhere, and this has unfortunately meant that the imagebuilding demos have been behind a login wall.

[cryptnono](https://github.com/yuvipanda/cryptnono) is an open source project designed to help fight cryptojacking, and as part of this grant we ported some of this functionality out of mybinder.org specific code into cryptnono, so other deployments may also benefit from it! As part of the port, we also migrated to using the super efficient [ebpf](https://ebpf.io/) Linux Kernel feature, allowing for more complex heuristics to catch a much broader range of cryptomining activity. This

## Explored pathways that were then discarded

List of things that were tried and then decided as not good pathways:

- [repo2docker-service](https://github.com/consideRatio/repo2docker-service), a separate JupyterHub service that could *only* build images. As we worked on it, we realized that it was replicating a lot of features that binderhub already has, so we pivoted to working on binderhub directly instead.
- Building off of [tljh-repo2docker](https://github.com/plasmabio/tljh-repo2docker). While this already had a nice UI, it would be hard to port it to run on a distributed kubernetes environment without it becoming a 'hard fork'.

While these did slow down the implementation of the project, it has allowed us to be very confident that the methods we have chosen are long term sustainable.

## Future work

This is not complete of course, and there is a lot of future work to be done.

1. Better UX for specifying images, including figuring out how to 'save' them for future reuse.
2. Better compatibility with mybinder.org, particularly in allowing other sources of environments (not just GitHub, but zenodo, raw git repositories, etc) and URL compatibility


> [name=Arnim Bleier]
> - binder compatible import including content using the availible build-packs and as well as enableing badges for the import.
> - Persistentce of imports as well as UI / UX user feedback incorporation, streamlining (imo from here on optional) and possible templating for branding.
> Limiting the ammount of compute provided to a user.
>> [name=Yuvi] I've incorported versions of these now, but don't think 'limiting the amount of compute provided to a user' should be here. You can already select the amount of resources, and I don't think the 'quota' notion (where we can restrict how much resources a user uses over say a month) is related to this work.


Funded by [GESIS](http://notebooks.gesis.org) in cooperation with NFDI4DS [460234259](https://gepris.dfg.de/gepris/projekt/460234259?context=projekt&task=showDetail&id=460234259&) and [CESSDA](https://www.cessda.eu).
