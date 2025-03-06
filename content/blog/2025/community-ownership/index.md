---
title: Announcing our formal commitment to open technology
date: 2025-01-15
authors:
  - Yuvi Panda
  - Chris Holdgraf
tags:
  - open source
categories:
  - organization
featured: false
draft: false
---

In this post, we're sharing our [Commitment to Open Technology](../../../open-technology/index.md). It is focused on _software licenses_ for reasons we'll describe below. We hope that it clarifies what kind of licenses we'll use, and assures our communities that we will not change our stance towards open source technology in the future. This ensures 2i2c's long-term commitment to community-owned and open infrastructure.

Being a platform and service provider gives us a lot of power, and also introduces a potential source of _lock-in_ for our member communities. While 2i2c's organizational mission and culture are strongly aligned with open infrastructure, we believe it's important to encode commitments like these in a formal way to provide both transparency and accountability to our member communities.

## Our commitment to open technology

Below we copy the original language of this policy from our [Commitment to Open Technology](../../../open-technology/index.md):

<!-- TODO: When we switch to MyST, we should embed this rather than copy/paste -->

_Definitions of MUST, MUST NOT, SHOULD, MAY, etc are defined in [RFC 2119](https://tools.ietf.org/html/rfc2119)_

1. All engineering artifacts (code, documentation, etc) produced by 2i2c's engineering team MUST be licensed under an open source license approved by a non-profit organization that is not 2i2c.
2. Open Source Projects originating at 2i2c, or stewarded by 2i2c, MUST NOT require a [Contributor Licensing Agreement](https://en.wikipedia.org/wiki/Contributor_License_Agreement) that includes Copyright Assignment to 2i2c. 
3. The list of external organizations that define licenses we accept are
    1. [the Open Source Initiative](https://opensource.org/)
    2. the [Organization for Ethical Source](https://ethicalsource.dev/). 
4. Modifying (1), (2), or (3) MUST be done through a 2/3 majority vote of 2i2c staff. 

## What does this commitment mean?

In plain language, here's what this commitment means:

1. We'll only use open source licenses that have been approved by standard non-profits that are broadly recognized by the tech industry.
2. For anything we build, we won't require contributors to give up the rights to their contributions via CLAs, so that it is much harder for 2i2c to change our licenses in the future.
3. Changing this policy will require organization-wide agreement, and in the future we'll give authority over this policy to a group of people representing our member communities.

## Why are licenses and CLAs important? 

Many organizations claim to be committed to open infrastructure, while retaining the ability to _change this commitment in the future when it is in their interests_. A classic example of this is a "bait and switch" that looks something like this:

1. A company releases software under an open source license and professes to build an open source community around it.
2. However, they retain the rights to all of the code in their projects through a [Contributor License Agreement](https://en.wikipedia.org/wiki/Contributor_License_Agreement) (CLA) with copyright assignment. This generally means that contributors must _give up the rights to their contribution_ in order to make that contribution.
3. Once their product has gained traction and it is in their interests, the company can _change the license_ to whatever they wish (even one that is not open source) because they retain the rights to all contributions in the codebase.
4. They then leverage this new position as owners of a proprietary project to extract business value or grow their position in a market.

Think this sounds unlikely? Here are just a few recent examples of companies that have switched their license after many years of releasing their technology under an open source license:

- [Redis](https://redis.io/blog/redis-adopts-dual-source-available-licensing/)
- [Hashicorp / Terraform](https://www.hashicorp.com/blog/hashicorp-adopts-business-source-license)
- [Elastic Search](https://en.wikipedia.org/wiki/Elasticsearch#Licensing_changes)

We want to ensure our communities that 2i2c is not headed down this path, in order to give them confidence in treating us as a long-term service partner.

## What does this change about 2i2c's open source commitment?

In short: nothing. These are already the principles that 2i2c was committed to from its inception, and already implied via our [Right to Replicate](../../../right-to-replicate/). However, we wanted to make these commitments more formally in order to give ourselves more accountability to sticking with them, and to provide more transparency for our community members and stakeholders.

## Who is this for?

We imagine three audiences for this policy:

1. **2i2c present and future staff** who want to ensure that their organization remains committed to our open principles. This document provides a sense of psychological safety to have bold discussions about structuring our approach to open source.
2. **Member communities and 2i2c stakeholders** who need to have an understanding of the guarantees that we provide in order to trust 2i2c as a service developer and provider. This is similar to the effect our [Right to Replicate](/right-to-replicate) has.
3. **Open source communities** who need to understand our long-term commitment and goals around open technology in order to trust as a peer and collaborator within open source communities.

## We'd love feedback

We hope that these ideas both clarify our intent and the reason that we think it's important. We'd love feedback about early refinements to these principles in order to make them more effective, as well as ways that we can provide more community oversight and participation in evolving these policies moving forward. If you have any thoughts to share, please send feedback via e-mail [hello@2i2c.org](mailto:hello@2i2c.org).

---

**Acknowledgements**: _The creation of this policy and the rationale behind it was led by [Yuvi Panda](../../../authors/yuvi-panda/) with feedback from 2i2c's team. This blog post was co-written with [Chris Holdgraf](../../../authors/chris-holdgraf)._
