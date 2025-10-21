---
title: "TIL: A few ways to track web traffic for open source projects"
date: "2025-10-19"
authors:
  - Chris Holdgraf
categories:
- learning
tags:
- community
- open-source
---

Understanding how people discover and navigate your project's web presence is valuable for open source communities, but there are a lot of options out there and many maintainers may not know about them. Recently Chris did some research to improve the web analytics for [Jupyter](https://jupyter.org), and learned about several options for tracking web traffic[^1]. Here's a quick report of what stood out. 

[^1]: Chris has been [serving on the Jupyter Executive Council](../executive-council-updates/) as a [Foundational contribution](../foundational-contributions/). This was related to that effort!

## Three analytics tools we found helpful

**[Plausible.io](https://plausible.io/)** - A privacy-friendly, GDPR-compliant analytics service
- Clean interface with public dashboards (see [Jupyter's dashboard](https://plausible.io/jupyter.org))
- Paid service but offers 15% discount for open source projects
- Cost scales with traffic volume. It can get expensive for a project as big as Jupyter!
- This is the service we ultimately ended up using...

**[ReadTheDocs Analytics](https://docs.readthedocs.com/platform/stable/traffic-analytics.html)** - Built-in traffic tracking for documentation sites
- Available as a free add-on for ReadTheDocs projects, it provides traffic data specific to documentation pages.
- There's no additional cost if already using ReadTheDocs, though if you're on a business plan you may need to pay for it.
- The analytics are a bit barebones, but quite useful for learning where your readers are navigating.
- Enable in `Settings` > `Addons` > `Analytics`.

**[GitHub Repository Analytics](https://docs.github.com/en/repositories/viewing-activity-and-data-for-your-repository/viewing-traffic-to-a-repository)** - Native analytics in GitHub.
- Shows clones, views, and referring sites. This is also fairly barebones, but it's really useful to see who is actually looking at your repository.
- Free for all GitHub repositories.
- Access via `Insights` > `Traffic` on any repository.

## Learn more

- [GitHub issue coordinating Jupyter's analytics work](https://github.com/jupyter/jupyter.github.io/issues/815)
- [Plausible.io public dashboard for jupyter.org](https://plausible.io/jupyter.org) (this might be down for now, but we're working to bring it back up)
- [ReadTheDocs Analytics documentation](https://docs.readthedocs.com/platform/stable/traffic-analytics.html)
- [GitHub Traffic Analytics API](https://docs.github.com/en/rest/metrics/traffic?apiVersion=2022-11-28)

## Acknowledgements

Thanks in particular to [Jason Grout](https://github.com/jasongrout) from the [Jupyter Executive Council](/collaborators/jupyter/) for collaborating on this investigation and helping test these tools.
