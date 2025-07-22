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

We're excited to announce out-of-the-box support for [Jupyter Book 2](https://next.jupyterbook.org) for our community members. This allows communities to create and share knowledge bases together for their community workflows. This post describes the motivation behind this new functionality, and how you can learn more about the project.

> ⭐ **Members of 2i2c's community network** can use this feature in their hubs by following [our documentation and sharing guide](https://docs.2i2c.org/sharing/documentation/).

A core component of our mission to make research and education more _impactful_, _accessible_, and _delightful_ is leveraging our unique [global network of communities][network] to make meaningful improvements to the open-source tools that power their work. Learning from one community can then provide value to our entire network, e.g., [our work with PACE on speeding up their CNN model training][pace-gpu].

Central to our communities' work is the importance of sharing new findings, best practices, and community resources. Across our network, we have seen communities creating their own "books" that provide a home for this kind of content. Many of these books feature the concept of a "landing page" that welcomes new members, establishes an identity, and provides jumping-off points (or "calls to action") to more detailed resources.

Until now, each community has been required to undertake this work independently. 2i2c believes that by [building upon existing open-source tools][open-tech] like [Jupyter Book 2][jb-next], we can help communities focus on the _content_ of their home, rather than spending time worrying about its _appearance_. To that end, we have been working on [an initiative][initiative] to allow communities to rapidly build interactive starter documentation and provide users with a rich, interactive, and informative onboarding experience. Through this initiative, we have:

- Improved the user experience of launching into interactive compute environments from a Jupyter Book.
- Built components into the Jupyter Book "book theme" for low-density landing page content like call-to-action blocks.
- Extended our service to co-locate community documentation alongside community hubs (i.e., `docs.hub.2i2c.cloud`).

![Screenshot of the 2i2c Showcase Hub landing page](./landing-page.png)
(A screenshot of the 2i2c [Showcase Hub](https://docs.showcase.2i2c.cloud/) landing page, featuring a simple banner image and call-to-action.)

To take advantage of this feature, communities can use the [`2i2c-org/community-docs-template`][template] to deploy a Jupyter Book site to GitHub Pages. This template demonstrates simple usage of Jupyter Book 2 for computational content and landing page creation, and establishes the necessary CD workflows for web publication. Meanwhile, 2i2c can update our domain name management to point the `docs.hub.2i2c.cloud` nested subdomain to the newly deployed documentation.

For more information, see [our community documentation for deploying Jupyter Books][svc-guide].

Developing these new capabilities taught us a lot about what makes building "good" community documentation so difficult. A wide range of bespoke website-building tools and integration quirks previously made it challenging for communities to both keep documentation current with internal changes and keep up with necessary software updates. We also learned that by trading bespoke complexity for simplicity and readability, we could build a solution that scales to multiple communities, with a consequently reduced maintenance burden.

With these improvements, we have initiated a conversation about what a more unified "look and feel" for our network might entail, and how it might benefit our communities. Much more can be done to build on this first step, and we are eager to gather feedback on how to improve these features for users.

To learn more about this work, consider exploring a minimal example on [our Showcase Hub](https://docs.showcase.2i2c.cloud/), and check out [our service guide][svc-guide]. [Let us know](https://docs.google.com/forms/d/e/1FAIpQLSff-u-sWFuwO1-VTgk2Ir7f1nfUUlLevQk_Vkk_jnmcI1nJnw/viewform) what you think!

[pace-gpu]: ../../2024/pace-hackweek/index.md
[open-tech]: ../community-ownership/index.md
[svc-guide]: https://docs.2i2c.org/community/content/#deploy-documentation-with-jupyter-book
[network]: https://2i2c.org/communities/
[jb-next]: https://next.jupyterbook.org
[initiative]: https://github.com/2i2c-org/infrastructure/issues/5045
[template]: https://github.com/2i2c-org/community-docs-template
