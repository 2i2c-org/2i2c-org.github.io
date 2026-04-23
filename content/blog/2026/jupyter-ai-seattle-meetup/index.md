---
title: "Report from the Jupyter and AI community meetup"
slug: "jupyter-ai-seattle-meetup"
date: 2026-04-23
authors:
  - Harold Campbell
categories:
  - upstream-impact
tags:
  - jupyter
  - open-source
  - community
---

A small group of [Jupyter](/collaborators/jupyter/) community members recently met in Seattle to demo Jupyter workflows augmented with AI tools and discuss what's next. This is a quick report-out about what stood out.

The conversations focused on what agentic workflows could unlock for researchers and students - with broad acknowledgement that deployment, security, authorization, and ethics still have a lot to be worked out.

Here are a few highlights from the demos.

## Jupyter AI and the Agent Client Protocol

[Jupyter AI](https://github.com/jupyterlab/jupyter-ai) v3 is adding support for the [Agent Client Protocol (ACP)](https://agentclientprotocol.com/), enabling multi-agent collaboration within JupyterLab. We saw how a single request could be split across multiple specialized agents based on each one's skills, similar to [this demo from JupyterCon 2025](https://www.youtube.com/watch?v=hyzPC6moEJ0).

Some things still to figure out:

- **No tool isolation yet** - agents aren't scoped by user role or security group.
- **Manual configuration required** - agents running locally need to be registered by hand.
- A future goal is for JupyterLab to auto-detect locally installed agents, or for LLM providers to contribute integrations directly.

The Jupyter AI team also shared a new "Personas" abstraction that lets you define a skill-specific agent in just a few lines of Python. Personas open the door to domain-specific agents or agents with crafted "personalities". They are written in a few lines of Python, though we discussed the possibility of using markdown instead. This seems to be evolving rapidly!

[Jupyter AI v3.0.0 has since been released](https://github.com/jupyterlab/jupyter-ai/releases/tag/v3.0.0).

## Notebook CLI

[`nb-cli`](https://github.com/jupyter-ai-contrib/nb-cli) is a Rust-based tool for interacting with notebooks from the command line - changing cells, running them, checking errors, and rendering the notebook in the console. It can also connect to remote JupyterLab instances, making it useful for headless workflows like CI pipelines or batch grading.

## Sidebar comments and Real-time collaboration

A demo showed Google Docs-style side-panel comments for `.ipynb` files. Previous collaboration efforts used [Conflict-free Replicated Data Types (CRDTs)](https://en.wikipedia.org/wiki/Conflict-free_replicated_data_type) for multi-cursor editing, but the team felt that approach may not have hit the mark. Side-panel comments felt more natural, though how this extends to `.py` files is still an open question.

## Opportunities for 2i2c

The meeting helped us understand the role we _could_ play in this space.
We think there's opportunity to help facilitate the use of agents on shared infrastructure, particularly around the upstream control planes for deployment, administration, and authorization. We can also help facilitate community conversations about the ethics and impact of AI tools on open science.

## Acknowledgements

- The [Jupyter Foundation](https://jupyterfoundation.org) for supporting the event.
- [Zach Sailer](https://www.linkedin.com/in/zach-sailer-8a1472151) (Apple), for organizing this meetup.
- [Chris Holdgraf](/authors/chris-holdgraf) for editing and adapting the original content for this post.
