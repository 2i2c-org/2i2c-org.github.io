---
title: "Protecting our hubs against the CopyFail kernel exploit"
slug: "copyfail-mitigation"
date: "2026-05-04"
categories:
  - service enhancements
tags:
  - reliability
  - devops
  - open source
  - jupyterhub
---

The recently disclosed [CopyFail Linux kernel zero-day](https://copy.fail/) (CVE-2026-31431) opens up a way for code running inside a container to break out onto the underlying node.
We took a close look at our hubs to confirm whether they were exposed, confirmed that we our hubs are likely not at risk, and added another layer of protection just in case.

### Are 2i2c's hubs at risk?

No - based on our testing and mitigation efforts, our hubs are not vulnerable to CopyFail.

### Why do we think we're not at risk?

- We tried to reproduce the exploit on a staging hub by following the [public Kubernetes proof-of-concept](https://github.com/Percivalll/Copy-Fail-CVE-2026-31431-Kubernetes-PoC) on both AWS and EKS, and the exploit was unable to break out of the container.
- Existing JupyterHub hardening on Kubernetes from [kubespawner#545](https://github.com/jupyterhub/kubespawner/pull/545) had already significantly reduced our risk exposure, and the exposure of anyone else running [Z2JH](https://z2jh.jupyter.org) (the standard way to deploy JupyterHub on Kubernetes).
- As an extra layer of protection, we deployed [`copyfail-ebpf-k8s`](https://github.com/iwanhae/copyfail-ebpf-k8s) across our hubs in [infrastructure#8227](https://github.com/2i2c-org/infrastructure/pull/8227). It blocks the specific kernel feature that CopyFail depends on. See [the project's explanation](https://github.com/iwanhae/copyfail-ebpf-k8s#quick-start) for how that works.

### What else did we look into

- [Deckhouse's mitigation](https://github.com/deckhouse/d8-copy-fail-mitigation) was too platform-specific for us.
- [OVHcloud's `modprobe` blocking](https://blog.ovhcloud.com/copy-fail-cve-2026-31431-how-to-rapidly-protect-ovhcloud-mks-clusters-from-the-linux-kernel-zero-day/) likely [won't work on Amazon Linux 2023](https://github.com/aws/containers-roadmap/issues/2808), since the relevant module is built into the kernel image.
- [AL2023 security advisories](https://alas.aws.amazon.com/alas2023.html) - no patched AL2023 image is available yet, so we can't rely on a kernel-level fix from AWS for now.

## Acknowledgements

- Huge thanks to [Georgiana](/authors/georgiana-dolocan) for the deep dive into the exploit and whether we're exposed here.
- Thanks to [Yuvi](/authors/yuvi-panda) for the PR that reduces JupyterHub's exposure to this back in 2021!
- Thanks to [iwanhae](https://github.com/iwanhae/copyfail-ebpf-k8s) for the eBPF daemonset we deployed in Kubernetes, and to [JupyterHub](../../../collaborators/jupyterhub/) for the upstream kubespawner hardening that lowered our exposure.
- Thanks to our collaborators at [NASA VEDA](../../../collaborators/nasa-veda/) for the ongoing conversations about hub security.
