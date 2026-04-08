---
title: "Report from the Jupyter Security Working Group security tooling sprint"
slug: "jupyter-security-sprint"
date: 2026-04-08
authors:
  - Jenny Wong
categories:
  - upstream impact
tags:
  - open source
  - jupyter
  - security
  - community
  - report
---

The [Jupyter Security Working Group](https://github.com/jupyter/security) recently held a Security Tooling Sprint.
It was a timely event given the [recent spate](https://blog.pypi.org/posts/2026-04-02-incident-report-litellm-telnyx-supply-chain-attack/) of software supply chain attacks across the tech world.

The sprint covered two main areas:

- **Governance and strategy** — conversations about responsibility and accountability in the face of AI, with emphasis on ensuring humans are ultimately responsible for code committed to [Jupyter](/collaborators/jupyter/) subprojects. The group also discussed how security could benefit from working group members regularly attending subproject meetings like the [JupyterHub](/collaborators/jupyterhub/) Collaboration Cafes.
- **Automation and tools** — the group evaluated several tools for improving security posture across the Jupyter ecosystem. Here are a few that stood out:
  - [Semgrep](https://semgrep.dev/) as an alternative vulnerability scanner to CodeQL
  - [Grype](https://github.com/anchore/grype), [Checkov](https://www.checkov.io/), and [Kubescape](https://kubescape.io/) for cloud infrastructure misconfiguration checks
  - [Schemathesis](https://github.com/schemathesis/schemathesis) and [restler-fuzzer](https://github.com/microsoft/restler-fuzzer) for API fuzz testing

One challenge we discussed was how blindly running security scanning tools generates many false positives. There's real effort needed to tune these tools for each project's edge cases before they're useful in automation. On a related note, we discussed the increase in AI-generated (or AI-assisted) vulnerability and security reports, and the challenges associated with sifting through all of those pieces of information.

## Acknowledgements

- Thanks to [the jupyter security working group](https://github.com/jupyter/security) for providing leadership and organizing, in particular Joe Lucas!
- Thanks to the [Jupyter Foundation](https://jupyterfoundation.org) for funding community meetings like these.
