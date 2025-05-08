---
title: "Launching Jupyter Book for 2i2c Communities"
date: 2025-05-08
authors:
  - Angus Hollands
tags:
  - jupyter book
categories:
  - service
featured: false
draft: false
---

A core component of our mission to make research and education more _impactful_, _accessible_, and _delightful_ is leveraging our unique [global network of communities][network] to help us make impactful improvements to the open-source tools that powers their work. In this way, our experience of learning from one community can be used to provide value to our entire network e.g. [our work with PACE on speeding up their CNN model training][pace-gpu]. 

At the heart of the work that our communities perform is the fundamental importance of sharing new findings, best-practice, and community resources. Across our network, we have seen communities creating their own "books" of that provide a home for this kind of content. Replicated across many of these resources is the concept of a "landing page" that welcomes new members, establishes an identity, and provides jumping off points (or "calls to action") into more detailed resources. 

Until now, each community has been required to understake this work themselves. 2i2c believes that by [building upon existing open-source tools][open-tech] like [Jupyter Book 2][jb-next], we can help communities to focus on the _content_ of their home, and spending less time on what it _looks like_. To that effect, we have been working on [an initiative][initiative] to allow communities to build interactive starter documentation and provide their users with a rich, interactive and informative onboarding experience. Through this initiative, we have:

- Improved the user experience of launching into interactive compute environments from a Jupyter Book.
- Built components into the Jupyter Book "book theme" for low-density landing page content like call-to-action blocks.
- Extended our service to co-locate community documentation alongside community hubs (i.e. `docs.hub.2i2c.cloud`).

With these improvements, we have tried to start a conversation around what a more unified "look and feel" to our network might look like, and how it might benefit our communities. There is much that can be done to take this first step further, and we are keen to garner feedback on how we can make these features work better for users.

A very thin example of what this community landing page _might_ look like can be seen at [2i2c's Showcase Hub](https://docs.showcase.2i2c.cloud/)


[network]: https://2i2c.org/communities/
[pace-cpu]: https://2i2c.org/blog/2024/pace-hackweek/#managing-shared-memory-on-2i2c-hubs
[initiative]: https://github.com/2i2c-org/infrastructure/issues/5045
[open-tech]: https://2i2c.org/blog/2025/community-ownership/
[jb-next]: https://next.jupyterbook.org
