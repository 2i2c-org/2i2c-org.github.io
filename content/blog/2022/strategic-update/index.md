---
title: "Updating our strategy after a year of operations"
subtitle: ""
summary: ""
authors: ["Chris Holdgraf"]
tags: []
categories: [organization]
date: 2022-09-05
featured: false
draft: false
---

Around a year ago [we began our pilot JupyterHubs project](http://localhost:1313/blog/2021/six-month-update/) to learn more about our biggest challenges and opportunities in making interactive computing more accessible and useful for research and education. Since then we have served more than 35 communities with community-centric infrastructure via the cloud.

One goal of this process was to identify a strategy that should guide the service and 2i2c's actions moving forward. This blog post is a short brainstorm and summary of what our strategy currently looks like. It is a combination of reflecting on our current actions and priorities, as well as anticipating what these will look like in the near future. Its goal is to sharpen these ideas, and generate some discussion from our team and the broader community.

## The problem we wish to solve

There has been an explosion in open source tools for scientific analysis. There's been growth in low-level tools like CPython and NumPy, mid-level tools like Pandas and XArray, and domain-specific tools like GeoPandas. These tools are produced by communities and may be used freely, which makes scientific workflows much more accessible and powerful.

In addition, advances in cloud services make it possible to leverage scalable and flexible cloud machinery in a way that can potentially boost the effectiveness of these tools, and connect them with workflows that were not possible on an individual machine. There are hundreds of services around the data lifecycle, often called the [Modern Data Stack](https://future.com/emerging-architectures-modern-data-infrastructure/).

However, there are still many barriers to leveraging this stack for scientific computing:

1. **Integrating these tools and services for specific scientific workflows**. Different problems require different tools to solve them. There are hundreds of open source tools and cloud services available to choose from - how can we reduce the cost of making this decision, and how can we encourage standardization around scientific workflows to let researchers more easily collaborate with each other?
2. **Making these workflows easily and reliably accessible**. Many of these workflows require ongoing services to keep infrastructure running and highly available. For example, interactive computing sessions, databases, and scalable computing infrastructure. Most scientific researchers do not have cloud infrastructure expertise, and finding this expertise is costly and difficult in every industry.
3. **Learning how to use this stack for modern cloud-based data workflows**. Many open source workflows are novel to researchers, especially those that leverage cloud infrastructure for use-cases that weren't possible a few years ago. In addition to needing _access_ to infrastructure, they also need guidance to identify a pathway to use it effectively in a way that they can share with their colleagues.

An extra challenge is that the scientific community is _extremely heterogeneous_ in where and how it works.
For this reason, our scientific workflows must be built on open and community-driven technology that is not controlled or tied to any single vendor or cloud provider.
Many cloud services tackle parts of this problem, but they tend to orient themselves towards enterprise customers, and build on proprietary or unilaterally-controlled technology which increases the chance of vendor lock-in and a lack of flexibility.

Finally, the scientific community is also built on values of **open collaboration** and **knowledge sharing**, and services designed for this community should embody and support these values.
For this reason we believe that a non-profit and community-centric organization such as 2i2c is in an excellent position to bring the scientific community into the cloud and empower their workflows with open infrastructure.

## How we wish to achieve impact

With this in mind, we hope to resolve these challenges and support research and education communities in the following ways:

> - **Integrate** open source tools and services that are optimized for scientific workflows and communities
> - **Manage** this infrastructure to make them accessible to a large and global community
> - **Guide** communities in using these tools to do their work more effectively and collaboratively.

We should do this in a way that aligns with our organizational values around community agency, equity and inclusion, and reciprocity.

## Our most important actions to take

Accomplishing this requires blending aspects of cloud infrastructure management, domain and workflow expertise, and collaborative service design. As we move forward, these are the biggest challenges to overcome in developing this service further:

1. **Build a top-notch global Site Reliability Engineering Team**. First and foremost, the infrastructure that we manage must be reliable and scalable. If you ask communities to do their work in the cloud, they must be confident that it will be stable and highly available. If you wish to serve a global community, then you must build systems management capacity on a global level. This means investing heavily in our asynchronous coordination and communication processes, and building team skills in the modern cloud infrastructure stack and dev-ops practices.
2. **Define two or three scientific workflows to focus on and integrate the right tools and services into a distribution for each**. We must identify a few scientific workflows to focus on, as well as the infrastructure stack that will be most-useful to the communities that require these workflows. We must integrate this infrastructure into a distribution that any community could pick up, but that has enough flexibility for each to solve their "last-mile problem" with customizations.
3. **Identify a service delivery model that is participatory while being sustainable**. We believe that community-centric infrastructure should be transparent and participatory, and provide agency to communities in shaping their service. On the other hand, we wish to serve many different communities, and thus we must minimize the amount of labor associated with serving any particular community. As a result we must build a collaborative model of roles and expectations around our services that balances participation from communities against our ability to act quickly to ensure the best service possible.
4. **Identify a cost-recovery model that is accessible and scalable**. We wish to serve a large and global collection of communities with our services, and so we must identify a way to recover our costs such that we are not restricted to serving only the wealthiest communities in the world, and such that "cost vs. resources generated" gives us the flexibility to grow to serve a large global community.

There are many other issues we must tackle, but these are issues that we've identified as being crucial to 2i2c accomplishing its mission. Over the coming months we will continue to refine our practices and service model. As we learn more, we'll update our understanding of 2i2c's situation and potential for impact, and our strategy for accomplishing our mission.

We hope that this framing helps others understand our position relative to the communities we wish to serve, and the impact we wish to have. We welcome any feedback or suggestions about how we can refine these ideas to better-serve our communities.
