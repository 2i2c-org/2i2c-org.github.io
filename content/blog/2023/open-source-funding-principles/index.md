---
title: "Principles and considerations for ethically accepting funding for open source"
subtitle: ""
summary: ""
authors: ["Chris Holdgraf"]
tags: ["funding", "community", "open culture", "sustainability"]
categories: [brainstorm]
date: "2023-01-10"
featured: false
draft: false
---

Over the past year the 2i2c team has focused its efforts on deploying, configuring, running, and managing cloud infrastructure that supports open source workflows in research and education. We've also done a lot of _upstream contribution_ as a part of our work.

However, we have shied away from taking direct funding for direct development work in open source projects. This is for two primary reasons:

1. Our focus has been on managing cloud infrastructure, not developing it. We want to facilitate access to open workflows in interactive computing, which is a different skillset and kind of work than _creating_ those tools.
2. While 2i2c is aligned with the interests of open communities, we are still a distinct organization with our own mission and strategy. We want to be conscious that 2i2c team members have _more than one hat_, and that their 2i2c hat is necessarily not the same thing as their open source hat. As such, we don't want to leverage our "other hats" to drive resources to 2i2c without being thoughtful about it.

In the last year we've found that running infrastructure for research and education gives us great visibility into the kinds of things that these communities want to do, and ways to improve the infrastructure. It also means we can potentially be a conduit of _resources_ from those communities into open source development workflows. For example, we recently [partnered with GESIS to make improvements in Binder and JupyterHub](../../2022/gesis-2i2c-collaboration-update/).

So, this post is a brainstorm to identify some of the major considerations that we should take before agreeing to this kind of work. Its goals is to drive policy that streamlines our ability to seek and accept funding for open source work. It tries to answer this question:

> How can a stakeholder accept funding on behalf of an open source community in a way that is inclusive, equitable, and effective.

## Some assumptions

First off I want to note that this only applies to open source projects that I'd call "Open communities". For example, those that follow [the principles of open scholarly infrastructure](https://openscholarlyinfrastructure.org/). The ideas here don't apply to open source projects that are run by single organizations or people. You can assume I'm talking about projects that:

- Have inclusive multi-stakeholder governance and operations.
- Care about having a broad contributor and leadership base, and want to follow best-practices in inclusive and equitable operations.
- Need funding to drive major new efforts, or to sustain pre-existing maintenance and community management work.

Why is this important? In short, because open projects should care about good governance, and about building sustainable and diverse multi-stakeholder communities around their operations and strategy. While it's easy to ignore these considerations and just bring in money however you can (open source is perpetually under-funded, after all), it's crucial that we think about how to do so in a way that aligns with the values of open communities, and that doesn't simply propagate a "rich get richer" dynamic. Ultimately, the unique value of open communities is not in the technology they create, but in the _way that they create it_.

## `tl;dr`: An overview of major considerations

After working with several open source projects over the years, there are a few issues that I've seen come up again and again. Here's a quick summary and I'll note each in more detail below.

- **Governance**: funding should _follow_ major decisions, not make them. It should represent the interests of the project rather than those of a single stakeholder or payer.
- **Transparency**: stakeholders that accept funding should be transparent in their _accounting_ (the sources of funding, deliverables attached with it, and operational costs), their _plans_ (the work they plan to do and how they want to do it) and in their _strategy_ (the reason they're applying for funding in the first place, and how the work fits in with their other operations).
- **Accountability**: stakeholders that accept funding should be accountable to the open communities that they are supporting. There should be mechanisms for open communities to provide feedback about and influence their operations, ideally in a powerful position like a board seat.
- **Equity**: funding should be shared with others in the project, particularly those that need it or that couldn't get funding on their own. Moreover, people should be paid for their time - if funding requires work from others, they should be compensated somehow.
- **Inclusion**: funding _opportunities_ should be shared with others in a project, particularly those from historically disadvantaged communities. Stakeholders with funding "connections" should use them to boost others in the community as _partners_, not just as contractors

Here is a more in-depth discussion of each below.

## Governance: funding should follow decisions

As a general rule, **funding should not be a decision**, it should only be fuel that helps **execute a decision that has already been made** by the community. Moreover, responsibilities attached to funding should only be given to people with the power to actually carry them out.

The most common mistake that I've seen in open communities is when funding _creates_ an unintended decision on behalf of many others.

For example, a new funder shows up with an agenda and offers it to a subset of maintainers. Those maintainers accept, implicitly making a decision to do the bidding of the funder (this could be a grant, a contract, etc). They begin doing the work, and run into resistance from _other_ maintainers who weren't on-board with these changes in the first place. This creates a stressful situation where one party has legally committed to doing some work, but they may not have the buy-in from others in the community to let it happen. This is particularly problematic when the funding commitment was not advertised publicly to others in the project early on.

Here are a few tips to ensure that funding is aligned with good governance principles:

1. **Make it clear who is allowed to accept money for a project**. First and foremost, projects should be explicit about who is allowed to accept money that involves doing open source work for them (e.g., only steering council members can approve new funding). Moreover, they should define basic policies about how that money can be used (e.g. does the project have a cap on the amount that can be paid to individuals).
2. **Tell others about your funding opportunity and get buy-in.** If a stakeholder wants to take advantage of a funding opportunity, they should first tell others on the team about the opportunity and what they hope to do. This is the bare minimum - give others an opportunity to object to your plan and/or ask for clarifications or modifications.
3. **Make decisions before funding opportunities arise**. If the community has already agreed that something is a good idea, then it is much simpler if funding simply helps _implement_ something rather than _propose_ something new.


## Transparency:  make it easy for others to see your interests and operations

Most open projects are community-led, while funding tends to be awarded to one or more stakeholders _within_ that community. At a minimum, communities should ask stakeholders to provide transparency about why they're looking for funding, what they're agreeing to do, and how they spend the money. 

Transparency is a way of building trust with other stakeholders by being clear about what you're up to. It makes it easier for others to hold you accountable, and makes it easier for others to understand whether your actions are in line with the goals and values of the community.

Here are a few tips to follow:

1. **Share your budget with the community**. Money is always a sensitive subject, but communities have a right to know if funding is being spent towards roles and operations that align with their interests. Some communities may also have policies about how much funding can be awarded to an individual person, and making this clear (even if it is in aggregate) helps others understand what you're doing with funds.
2. **Declare conflicts of interest**. We all have multiple hats when working with an open source project (unless we're paid full-time by the project itself). Any participating organization has their own mission, strategy, and interests. Some of these may be aligned with a community, and some may be aligned with a funding opportunity. It's important to declare how these interests align and where they differ, especially as it pertains to power dynamics and how funding is used.
3. **Carry out project planning and execution in public**. Dedicated staff have more time than normal to decide and act quickly. If they don't leave a paper trail for their work, it becomes difficult for those with less time to remain engaged and follow along. Make sure that you make your intentions, and the results of your actions, easily discoverable by those who do not have the same amount of time as you do to engage.

## Accountability: allow others to decide if you've done a good job

Accountability is a complement to transparency - you need to show others what you're up to, and let them tell you if you're doing a good job. At a minimum this should happen at the level of the specific funding opportunity, but ideally you should give key community members visibility and agency into your organization's broader strategy.

1. **Ask for feedback about your strategic plan and how this funding fits into it**. Tell a community about what you're up to, and why you think this funding is in both of your interests to receive. Let them know how it fits in with the big picture.
2. **Give strategic oversight to community members that work for a different stakeholder**. Give special attention to at least one community member that does not work for the same organization (for example, by creating an advisory board and briefing them on your progress and planning). This will help a more neutral perspective represent the interests of the community and avoid potential conflicts of interest.
3. **Perform an audit of your work and share it with others**. Do your best to objectively assess your own progress towards your goals, and whether you believe you've represented the community's interests in working towards them. Other community members may not have the resources to do this on their own, and you should use your dedicated funding to perform this yourself (while understandably declaring a conflict of interest in assessing your own work).

## Equity: share resources and knowledge with others

Open communities are a vehicle for building collaborations that span countries, economic situations, and use-cases. They are powerful because of their diverse and multi-stakeholder nature. However, they also exist in a society that is deeply inequitable and that perpetuates centers of wealth and power. This means that most open communities will have a subset of stakeholders with connections and resources that are unavailable to others. To ensure that we follow the principles of open culture, it is crucial that we find ways to push against this inequitable system by sharing resources with one another wherever possible.

Moreover, getting funding often means _centralizing the ability to act in a small subset of people_. This runs the risk that decision-making (see above) and organizational knowledge become centralized with those individuals. If you're paid full-time to work on an open source project, there's a good chance you will personally come to understand the codebase better than anybody else just because you have the time to learn it. This can turn into an anti-pattern where those with access to resources have an unfair power advantage in their perspective over the project.

Finally, running open source projects requires work on _both_ the creating and the receiving end. You can pay somebody to write a bunch of code, but somebody else still has to review it, lead discussions, and ultimately decide to merge. 

Here are a few tips to follow:

1. **Share funding with others.** If your work is going to require reviews and input from others, find a way to compensate them for their time (if they wish). Prioritize sharing resources with orgs from historically marginalized or disadvantaged communities. When dedicated resources are available, use them for these kinds of groups.
2. **Prioritize documentation and knowledge sharing.** It can be attractive to work on shiny new things, but it is _crucial_ that you put in the work to share knowledge with others in a community so that your funding doesn't become a source of knowledge and power centralization. Document your planning and work, and use that funding to make extra efforts to share your experience with others.
3. **Define practices for making changes that require at least two stakeholders**. This helps ensure that those funded to work on open source cannot overpower others in the community just because of their dedicated time. It also encourages healthier collaboration and communication between stakeholders.

## Inclusion: bring others along with you

A differentiating aspect of open communities is the way in which they _share power among stakeholders_. Funding is inherently tied to power, as it gives you the ability to pay people to do things. Moreover, a stakeholder that _controls_ funding also controls what it is used for. As a result, it's not enough to simply share funding with others in a project, _if that funding comes with strings attached_. It is also important to share opportunities for funding with others, and to build coalitions of equals when pursuing new funding.

Collaborators should be given agency over what they want to do with funding. They should be part of grant planning, project planning, etc. They should be seen as co-leads in discussion and announcements. Obviously any funding opportunity will come with obligations, but the important thing is who gets to decide what the team commits to in the first place, and how they plan to accomplish their goals.

Here are a few tips to follow:

1. **Invite others to participate in funding opportunities, especially if they need it**. If you identify a funding opportunity, tell others about it. Invite them to collaborate with you on a proposal, or encourage them to write their own proposal.
2. **Treat other stakeholders as partners, not contractors**. Treat collaborators as co-equals that have a say in leadership, strategy, and planning. Funding shouldn't solely come in the form of "strings attached" and contract work. It should center others as collaborators and leads that bring their own ideas to the table.
3. **Find ways to give power to those who historically do not have it**. Consider the power dynamics of who applies for funding and actively invite participation from those that need it or that wouldn't have access to these resources on their own. If you have a personal connection, use it to bring others to the table. If you're at a well-known organization, use it to boost the profile of others.

## How do I actually implement any of this?

The ideas in this post are principles and goals to strive for. They also touch on very complex subjects, and following them all perfectly is unrealistic given the state of most organizations. The point is not to define a specific roadmap of actions that must be followed, but to note a few major anti-patterns and ways to avoid them. Fundamentally, your goal should be to **build trust with a community** and to **live up to the community's mission and values**. Do what you can, and be honest and open with others in your efforts. A little bit of transparency and effort goes a long way.

As for 2i2c, we hope to use the ideas in this post to define a strategy and set of policies for how to engage with directed funding for open source. We'll share new ideas in the coming weeks.

## References and more reading

There are many resources that discuss how to equitably and inclusively seek funding as part of collaborations[^slack]. Here are a few that I found useful in writing this blog post:

- [AWID - Towards a feminist funding ecosystem guide](https://awid.org/sites/default/files/2022-02/AWID_Funding_Ecosystem_2019_FINAL_Eng.pdf)
- [The Astraea Foundation - Feminist Funding Principles](http://astraeafoundation.org/microsites/feminist-funding-principles/)
- [OpenGlobalRights - What we can learn from feminists who fund themselves](https://www.openglobalrights.org/what-we-can-learn-from-feminists-who-fund-themselves/)
- [Candid Learning for Funders - Deciding Together](https://learningforfunders.candid.org/content/guides/deciding-together/)
- [Open Research Funders Group - Open and Equitable Model Funding Program](https://www.openandequitable.org/participate)

[^slack]: And many thanks to several people in the [Invest in Open Infrastructure](https://investinopen.org), [The Turing Way](https://the-turing-way.netlify.app), [the Chan Zuckerberg Initiative](https://chanzuckerberg.com/), and [Code for Science and Society](https://codeforsociety.org) Slacks that helped me brainstorm these ideas.
