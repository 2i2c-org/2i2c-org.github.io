---
title: "Celebrating our progress in Q1 2022"
subtitle: ""
summary: ""
authors: ["Chris Holdgraf"]
tags: []
categories: [updates]
date: 2022-04-04
featured: false
draft: false
---

Quarter 1 of 2022 just wrapped up, and the 2i2c team has been busy making improvements across our infrastructure, organization, and operations.
This is a quick post to celebrate the work we've done over the past three months, and to briefly share what we're working on next.

These are the main highlights from this quarter - if you'd like to check out more of the work that we've done, see:

- [All the PRs we've merged in Q1](https://github.com/pulls?q=is%3Apr+merged%3A%3E2022-01-01+org%3A2i2c-org+archived%3Afalse+sort%3Aupdated-desc+)
- [All closed issues in Q1](https://github.com/issues?page=4&q=is%3Aissue+closed%3A%3E2022-01-01+org%3A2i2c-org+sort%3Aupdated-desc)


## Infrastructure improvements

This quarter we did a deep dive into a number of core infrastructure improvements for our [Managed JupyterHubs Service](https://2i2c.org/service/).
Here are a few highlights:

- **Infrastructure reliability and efficiency**. We [improved the resiliency, reliability, and efficiency of our deployment infrastructure](https://github.com/2i2c-org/infrastructure/issues/879). For example, we refactored our hub configuration so that each community is better-able to track it, we implemented validation steps to ensure that we don't accidentally push incorrect config to the hubs, and we've significantly improved our CI/CD pipeline to push deployments out to our hubs more efficiently.
- **Automatic deployments to commercial cloud**. With the ICESat hackweek as a test-case for AWS, we've finished automating the deployment of clusters and hubs to each major commercial cloud. (there's not a specific issue for this as it has been a multi-month effort over many PRs and issues!)
- **CILogon authentication**. [CILogon](https://cilogon.org/) is a non-profit organization that provides "single-sign on" authentication services for the same communities that 2i2c serves. We've partnered with them to [prototype using CILogon for 2i2c's hubs](https://github.com/2i2c-org/infrastructure/pull/1089), which should make it much easier for communities to user their own institutional sign-ons.

## Communities we've served and lessons learned

As described in [our Managed Hub Services strategy](https://compass.2i2c.org/en/latest/organization/strategy.html), our goals for this phase of our organization are to balance _serving communities of practice_ and _learning where we can improve our infrastructure and practices_.
With that in mind, here are a few highlights of communities we've served, and what we've learned from it:

- **We grew a hub for [the University of Toronto](https://jupyter.utoronto.ca/) to around 4000 monthly users**. This has taught us a lot about where our support and operations can and cannot scale, and where we have gaps in our sustainability / pricing model.
- **We deployed CILogon on a hub for [a class at Australian National University](https://anu.pilot.2i2c.cloud/)**. This gives us an opportunity to work out any UX issues and improvements to be made before a deeper CILogon integration.
- **We deployed a dedicated database per user for [a databases course at UT Austin](https://utexas.pilot.2i2c.cloud/)**. This is helping us learn more about how to pair slightly more customized per-user infrastructure with our standard hub setups, as well as how our [Right to Replicate model](https://2i2c.org/right-to-replicate) could be followed for more complex setups like a database.
- **We ran an event hub for [the ICESat2 HackWeek](https://twitter.com/scotty_h_q/status/1508557909751320577) at the University of Washington**. This helped refine our infrastructure and expertise with AWS, as well as improved our event "ready mode" practices.
- **We deployed a new hub for [the LEAP project](https://leap-stc.github.io/intro.html)**. This has given us an opportunity to prototype new processes for pass-through cloud costs to simplify our deployments.

**Organizational improvements**

Beyond our technical and community impact work, we've made a lot of significant organizational improvements as well.

- **We designed a [new role in Product and Community Management](https://2i2c.org/blog/2022/job-product-community-lead/)**. We're excited for this new hire to spearhead efforts in guiding and developing relationships with the communities we serve, as well as guiding and collaborating with our engineering team in developing our services. 
- **We designed [a new Project Manager role](https://github.com/2i2c-org/team-compass/issues/382)**. Our engineering team had been operating as a largely autonomous and independent group, but we've realized that we would benefit from someone to help coordinate our actions and plans, especially as we balance more operations/support issues in addition to new development. This new role is an experiment at growing this capacity within our team, in the hopes that we can dedicate a team member to it in the future.

## What's next

We are still working out our major priorities for the oncoming quarter, but have a few major projects in the works that we're hopeful to make progress on quickly.
Here are a few major examples:

- **Improve our process and operations around supporting our users**. We are [discussing first- and second-line support processes](https://github.com/2i2c-org/infrastructure/issues/1068) to make our team more responsive and effective at resolving incidents.
- **Improve our invoicing and contracting process**. We are [discussing how to reduce toil associated with invoicing](https://github.com/2i2c-org/team-compass/issues/355) in order to make this practice more reliable and efficient, along with our fiscal sponsor [Code for Science and Society](https://codeforscience.org).
- **Improving our reporting and monitoring infrastructure**. We'd like to boost our ability to [monitor activity on each of our hubs](https://github.com/2i2c-org/infrastructure/issues/328) in order to identify when something abnormal is happening and get ahead of any potential problems (e.g., to avoid unintentionally large cloud bills). We'd also like to improve our usage reporting to more create more accurate cloud bills for hubs running on multi-tenant clusters.

There is a lot more planned for 2i2c, and if you're curious to see what we're up to, we invite you to [check out our team compass](https://compass.2i2c.org) to learn about our practices, and [watch our activity on GitHub](https://github.com/2i2c-org/) to see our work.

Many thanks to the amazing 2i2c team, and the multiple open source and scholarly communities that we collaborate with to make all of this possible. In addition, we are grateful to [our funders](/organization/funding.md) for making this possible. We are looking forward to Q2! 🎉
