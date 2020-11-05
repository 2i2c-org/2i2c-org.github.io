+++
title = "The Customer Right to Replicate"
date = "2018-06-28T00:00:00Z"

reading_time = false  # Show estimated reading time?
share = false  # Show social sharing links?
profile = false  # Show author profile?
comments = false  # Show comments?

+++

The Right to Replicate gives customers the right to **replicate their infrastructure in its entirety elsewhere, with or without 2i2c**.

This document describes 2i2c’s commitment to a customer’s “right to replicate”, and how this translates into specific infrastructure commitments from 2i2c.  We make these commitments because we believe that using infrastructure that follows these principles will lead to a more fair, just, equitable world. We also believe they are the right foundation for more productive and impactful research and education.

2i2c is committed to running its own infrastructure on open-source tools and vendor-agnostic infrastructure, though it does not *force* users to use only open-source tools in their own environments, code, and data. Below is a table describing how the Right to Replicate fits into 2i2c hub technology. 

(Definitions of ‘MUST’, `MUST NOT`, ‘SHOULD’, `MAY`, etc are defined in [RFC 2119](https://tools.ietf.org/html/rfc2119))

<div id="rtr-table">

|                               |                           |                                                                                                                                          |
|-------------------------------|---------------------------|------------------------------------------------------------------------------------------------------------------------------------------|
| User Code and Data            | **May** be Open Source    | We encourage adopting and producing open source code and data, but this is up to the user. <br /> e.g., licenses for user content/code   |
| User Environment              | **Should** be Open Source | Strong preference for open source tools only, although in some cases user needs may override this. <br /> e.g., Python, R, PyData stack. |
| 2i2c Infrastructure           | **Must** be Open Source   | Strong commitment to using only open source software. <br />  e.g., JupyterHub, Kubernetes, Postgresql                                   |
| Cloud Provider Infrastructure | **Must** be Portable      | See [this blog post](https://words.yuvi.in/post/oss-in-the-cloud/) for more information.                                                 |

</div>

Below we describe our commitments in our own infrastructure stack in more detail.

## How 2i2c infrastructure ensures this right

2i2c infrastructure and documentation for it MUST BE as transparent & accessible as possible, so customers can replicate our configuration without having to extract any ‘secret sauce’ from 2i2c. If they choose to, they can also inspect, audit & modify the infrastructure they are paying for and using.

To ensure the Right to Replicate to our customers, 2i2c makes the following commitments to infrastructure we build and operate:

1. We MUST use only open source software to run our infrastructure. By only using software that is available to everyone on the same terms, we can ensure that customers can replicate the infrastructure without having to negotiate licensing terms with proprietary software vendors. In addition, any changes we make to open source software will be made in public and/or contributed upstream, so customers continue to have access to them regardless of where their infrastructure is. 

2. We MUST NOT directly depend on proprietary cloud vendor specific products or APIs. Instead, we use cloud-managed open source software, or hide the dependency behind a layer of abstraction. This ensures that customers can port their infrastructure to any cloud provider of their choice, or run it on their own hardware with purely open source software.

This set of commitments acts as a business continuity plan for our customers, ensuring 2i2c will follow best practices within the open source, open education and open research ecosystems.
