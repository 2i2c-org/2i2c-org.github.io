---
title: Openscapes host a Surface Biology and Geology workshop
date: "2024-05-29"
banner:
  image: "featured.png"
authors: ["Yuvi Panda", "Jenny Wong"]
tags: [geoscience, education]
categories: [impact, updates, partnerships]
featured: false
draft: false
---

![Cover slide from the SBG Workshop](featured.png "Surface Biology and Geology: VITALS Workshop")

[Openscapes](https://nasa-openscapes.github.io/) is a value-based initiative that advocates for kinder, better science produced with open source community and program building co-developed by Julia Lowndes and Erin Robinson. 

The initiative recently supported the [Surface Biology and Geology: VITALS Workshop](https://nasa.github.io/VITALS/) hosted by NASA [Land Processes Distributed Activate Archive Center (LP DAAC)](https://lpdaac.usgs.gov/) and NASA [Jet Propulsion Laboratory (JPL)](https://www.jpl.nasa.gov/).

Hands-on exercises teaching learners how to manipluate data collected from the [ECOSTRESS](https://ecostress.jpl.nasa.gov/) and [EMIT](https://earth.jpl.nasa.gov/emit/) instruments onboard the International Space Station were delivered using the 2i2c OpenScapes Hub. [Jupyter notebooks](https://nasa.github.io/VITALS/python/01_Finding_Concurrent_Data.html) were used to demonstrate how open source tools together with cloud data and compute resources could effectively analyse the the Canopy Water Content and the Land Surface Temperature over the [Jack and Laura Dangermond Preserve](https://www.dangermondpreserve.org/), Santa Barbara, CA.

![Plot of the Canopy Water Content over the Jack and Laura Dangermond Preserve, Santa Barbara, CA.](canopy-water-content.png "Plot of the Canopy Water Content over the Jack and Laura Dangermond Preserve, Santa Barbara, CA from a [VITALS Workshop Jupyter notebook](https://nasa.github.io/VITALS/python/03_EMIT_CWC_from_Reflectance.html).")

This event was attended by around 250 participants. To facilitate a smooth hub log-in process that didn't rely on GitHub authentication, we set up a shared password that workshop organizers can hand out to learners for access. This bypassed the manual labour of sending out GitHub invitations and drastically reduces the amount of preparatory work for events at this scale, so that organizers could focus on the essential complexity of teaching data analysis rather than the accidental complexity of managing hub authorization.

One of the elements that enabled us to recognize and solve this issue effectively is our close partnership with the Openscapes team. We engage in regular [6-weekly catch-ups](https://github.com/NASA-Openscapes/2i2cAccessPolicies/issues/7) where we can learn about user requirements and how we can develop our infrastructure to co-create optimal solutions. Together with our [Product Delivery Flow](https://team-compass.2i2c.org/product/deliveryflow/#defining-our-product-delivery-flow), we were quickly able to architect the shared password solution in time for the workshop.

![Slack message from Bri Lind](slack.png "Feedback from Bri Lind (LP DAAC)")

We have documented the technical infrastructure changes required to enable a shared password for the hub in our [Infrastructure Guide](https://infrastructure.2i2c.org/hub-deployment-guide/configure-auth/shared-password/) and hope to support many future events with this mechanism.

## Acknowledgements

- [NASA OpenScapes](https://nasa-openscapes.github.io/)
- [NASA LP DAAC](https://lpdaac.usgs.gov/)
- [NASA JPL](https://www.jpl.nasa.gov/)
- [NASA ROSES funding](https://science.nasa.gov/researchers/)
