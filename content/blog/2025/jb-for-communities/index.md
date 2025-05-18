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

A core component of our mission to make research and education more _impactful_, _accessible_, and _delightful_ is leveraging our unique [global network of communities][network] to help us make meaningful improvements to the open-source tools that power their work. In this way, our experience of learning from one community can be used to provide value to our entire network e.g. [our work with PACE on speeding up their CNN model training][pace-gpu].

At the heart of the work that our communities perform is the fundamental importance of sharing new findings, best-practice, and community resources. Across our network, we have seen communities creating their own "books" that provide a home for this kind of content. Replicated across many of these books is the concept of a "landing page" that welcomes new members, establishes an identity, and provides jumping off points (or "calls to action") into more detailed resources.

Until now, each community has been required to understake this work themselves. 2i2c believes that by [building upon existing open-source tools][open-tech] like [Jupyter Book 2][jb-next], we can help communities to focus on the _content_ of their home, without having to spend so much time worrying about how to make that content look _good_. To that effect, we have been working on [an initiative][initiative] to allow communities to more rapidly build interactive starter documentation and provide their users with a rich, interactive and informative onboarding experience. Through this initiative, we have:

- Improved the user experience of launching into interactive compute environments from a Jupyter Book.
- Built components into the Jupyter Book "book theme" for low-density landing page content like call-to-action blocks.
- Extended our service to co-locate community documentation alongside community hubs (i.e. `docs.hub.2i2c.cloud`).

![Screenshot of the 2i2c Showcase Hub landing page](./landing-page.png)
(A screenshot of the 2i2c [Showcase Hub](https://docs.showcase.2i2c.cloud/) landing page, featuring a simple banner image and call to action.)

In order to take advantage of this feature, communities can use the [`2i2c-org/community-docs-tmeplate`][template] to deploy a Jupyter Book site to GitHub Pages. This template demonstrates some simple usage of Jupyter Book 2 for working with computational content and building a landing page, and establishes the necessary CD workflows to publish the book to the web. Meanwhile, 2i2c can update our domain name management to point the `docs.hub.2i2c.cloud` nested subdomain to the newly deployed documentation.

Through building these new capabilities, we learned a lot about what makes building "good" community documentation so difficult. Between a wide range of bespoke tools for building websites, and quirks in integrating them together, it has previously been a lot of work for communities to both keep the documentation up-to-date with changes from within the community, and keep-up with the necessary updates to the software underlying that documentation. We also learned that by trading bespoke complexity for simplicity and readability, we could build a solution that scales to multiple communities, with a consequentially reduced maintenance burden.

With these improvements, we have tried to start a conversation around what a more unified "look and feel" to our network might look like, and how it might benefit our communities. There is much that can be done to take this first step further, and we are keen to garner feedback on how we can make these features work better for users.

To learn more about this work, why not take a look at a very thin example on [our Showcase Hub](https://docs.showcase.2i2c.cloud/), and check out [our service guide][svc-guide]. [Let us know](https://airtable.com/appM2L2x1uglMU0hy/pagWPJDEKTlLd7uMP/form) what you think!

[svc-guide]: https://docs.2i2c.org/community/content/#deploy-documentation-with-jupyter-book
[network]: https://2i2c.org/communities/
[pace-cpu]: https://2i2c.org/blog/2024/pace-hackweek/#managing-shared-memory-on-2i2c-hubs
[initiative]: https://github.com/2i2c-org/infrastructure/issues/5045
[open-tech]: https://2i2c.org/blog/2025/community-ownership/
[jb-next]: https://next.jupyterbook.org
[template]: https://github.com/2i2c-org/community-docs-template
