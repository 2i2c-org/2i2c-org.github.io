---
title: "Protecting our hubs against the Dirty Frag kernel exploit"
slug: "dirty-frag-mitigation"
date: "2026-05-12"
categories:
  - service enhancements
tags:
  - reliability
  - devops
  - open source
  - jupyterhub
---

This week, another Linux kernel exploit "Dirty Frag" (CVE-2026-43284 and CVE-2026-43500) was disclosed to the general public. Unlike the recent [Copy Fail Linux kernel zero-day](../copyfail-mitigation/), this set of exploits was leaked ahead of the embargo period expiring, leaving insufficient time for kernel maintainers to release a patch. The Dirty Frag exploit belongs to the same bug class as Copy Fail and Dirty Pipe (CVE-2022-0847), and provides a robust mechanism for obtaining root privileges on most major Linux distributions. It does this by chaining two separate CVEs against which most Linux distributions are unlikely to be simultaneously protected.

We took a close look at our hubs to confirm whether they were exposed, confirmed that our hubs are likely not at risk, and added another layer of protection just in case.

### Are 2i2c's hubs at risk?

No - based on our testing and mitigation efforts, our hubs are not vulnerable to Dirty Frag.

### Why do we think we're not at risk?

- We tried to reproduce the exploit on a staging hub by following the [public Kubernetes proof-of-concept](https://github.com/Percivalll/Dirty-Frag-Kubernetes-PoC) on both AWS and EKS, and the exploit was unable to break out of the container.
- Existing JupyterHub hardening on Kubernetes from https://github.com/jupyterhub/kubespawner/pull/545 (originally added by Yuvi in 2021 in response to a different security issue) had already significantly reduced our risk exposure, and the exposure of anyone else running [Z2JH](https://z2jh.jupyter.org) (the standard way to deploy JupyterHub on Kubernetes).
- As an extra layer of protection, we deployed an audited version of [`block-dirtyfrag`](https://github.com/mrunalp/block-dirtyfrag) across our hubs in https://github.com/2i2c-org/infrastructure/pull/8227. It blocks the specific kernel features that Dirty Frag depends on. See [the project's explanation](https://github.com/mrunalp/block-dirtyfrag#bpf-lsm-daemonset-deployment) for how that works.

### What else did we look into

- [AL2023 security advisories](https://alas.aws.amazon.com/alas2023.html) - no patched AL2023 image is available yet, so we can't rely on a kernel-level fix from AWS for now.

## Acknowledgements

- Thanks to [Georgiana](/authors/georgiana-dolocan) for the prior work on the Copy Fail exploit patching that set the stage for this.
- Thanks to [Yuvi](/authors/yuvi-panda) for the PR that reduces JupyterHub's exposure to this back in 2021!
- Thanks to [mrunalp](https://github.com/mrunalp/) for the eBPF daemonset we deployed in Kubernetes, and to [JupyterHub](../../../collaborators/jupyterhub/) for the upstream kubespawner hardening that lowered our exposure.
