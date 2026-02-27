---
title: "Introducing Jupyter Book 2 at FOSDEM 2026"
slug: "kubernetes-cgroup-changes"
date: 2026-02-27
authors:
  - Angus Hollands
categories:
  - 
tags:
  - 
---

- Received a support query about unusual behaviour https://cryospherecloud.slack.com/archives/C04BV452D0F/p1769724776399419
  - Proactive community (tasha)
- Traced back to OOM
- Replicated OOM through simple Python NumPy demo
- Observed killing of server
- Noted remark about "usually"
- Suspected k8s upgrade
- Dug into k8s OOM killing
- Found cgroupv2 
- Why did this break on cryo?
    - AWS upgrade AL2
    - AL2 → cgroupsv2
    - k8s 1.28 changed cgroupv2
- Fix for all hubs!!

Our teammate [Angus Hollands](../../../authors/angus-hollands/) gave a talk at FOSDEM 2026: [Introducing Jupyter Book 2](https://fosdem.org/2026/schedule/event/ZY9WYD-introducing-jb-2/).

The talk shares why the Jupyter Book 2 and MyST stack was rebuilt, and how it supports open, reusable computational publishing workflows.

- [Watch the recording](https://video.fosdem.org/2026/aw1120/ZY9WYD-introducing-jb-2.mp4)
- [FOSDEM event page](https://fosdem.org/2026/schedule/event/ZY9WYD-introducing-jb-2/)

{{< figure src="featured.png" caption="Slide from the FOSDEM 2026 session introducing Jupyter Book 2." >}}

## Learn more

- [Jupyter Book 2 and the MyST Document Stack (SciPy 2025 paper)](https://proceedings.scipy.org/articles/hwcj9957)
- [Jupyter Book documentation](https://jupyterbook.org/)
- [Jupyter Book on GitHub](https://github.com/jupyter-book/jupyter-book)

## Acknowledgements

- Thanks to [Project Pythia](../../../collaborators/pythia/) and to [BIDS](../../../collaborators/bids/) for supporting deeper [foundational contributions](../../2025/foundational-contributions/) like this in Jupyter Book.
- Thanks to the [Jupyter Book](../../../collaborators/jupyter-book/) team for helping out with slide creation and doing all the work Angus spoke about here!
