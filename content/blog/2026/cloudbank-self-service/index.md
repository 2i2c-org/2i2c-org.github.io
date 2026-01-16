---
title: Enabling CloudBank to safely manage their own cluster infrastructure
slug: "cloudbank-self-service"
date: "2026-01-20"
categories:
  - service enhancements
tags:
  - sovereignty
  - devops
  - learning
---

We recently enabled [CloudBank](/collaborators/cloudbank) to run Terraform changes for their cluster without needing to wait on 2i2c engineers for each request. The initial motivator was provisioning home-directory storage disks for new community hubs, and we wanted to empower them to solve similar problems in the future.

{{< figure src="featured.png" caption="CloudBank simplifies cloud access for computer science research and education.">}}

To do this safely, we needed to avoid granting access to shared Terraform state that could impact other communities. Following [Yuvi's suggestion](https://github.com/2i2c-org/infrastructure/pull/6797#pullrequestreview-3246004031), we migrated CloudBank's Terraform state to CloudBank’s own GCP project so that infrastructure changes from the CloudBank team are isolated to their cluster only, making this safe to try. This unblocks CloudBank to run changes like `terraform plan` and `terraform apply` themselves, meaning that CloudBank can deploy and update a hub without 2i2c engineers in the loop.

This is a good example of how we aim to balance **community autonomy** with **infrastructure safety**. CloudBank can now self-serve routine operations while our broader infrastructure remains protected.

## Learn more

- [The infrastructure issue describing this work](https://github.com/2i2c-org/infrastructure/issues/6795)
- [A hub deployed by CloudBank using this workflow](https://github.com/2i2c-org/infrastructure/pull/7339)

## Acknowledgements

- Thanks to Sean Morris and the [CloudBank](/collaborators/cloudbank) team at [UC Berkeley](/collaborators/bids) for collaborating on this workflow.
