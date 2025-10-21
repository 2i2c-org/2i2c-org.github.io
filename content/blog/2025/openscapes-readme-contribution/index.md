---
title: A helpful contribution to our JupyterHub SSH README from OpenScapes
date: 2025-10-21
categories: community-impact
tags:
  - open-source
  - foundational-contribution
---

We love when collaborators contribute back to the tools we maintain! Andy Teucher from [OpenScapes](../../../collaborators/openscapes/) recently [fixed a documentation issue](https://github.com/yuvipanda/jupyter-sshd-proxy/pull/11) in `jupyter-sshd-proxy` that benefits everyone using the tool.

[`jupyter-sshd-proxy`](https://github.com/yuvipanda/jupyter-sshd-proxy) is a tool originally created by Yuvi to help 2i2c communities connect to their JupyterHub instances via SSH. Andy ran into an issue when using it with the VS Code fork that uses the [`open-remote-ssh`](https://github.com/jeanp413/open-remote-ssh) extension - it failed unless double quotes were used around the authorization token in the `ProxyCommand`.

Through experimentation, Andy figured out the fix and [contributed it back to the README](https://github.com/yuvipanda/jupyter-sshd-proxy/pull/11). Now everyone using this tool will have clearer documentation.

While small, we think this is a nice example of a ["Foundational contributions"](../foundational-contributions/index.md) from a community:

- 2i2c creates and maintains open source tools to help our communities
- Our communities use those tools and run into issues
- They debug, figure out solutions, and contribute improvements back
- Everyone benefits from the improvements

This is exactly how we want 2i2c to help our communities - by making it easy for them to contribute back to the ecosystem and strengthen the tools everyone relies on.

## Acknowledgements

- Thanks to [Andy Teucher](https://github.com/ateucher) for the contribution and debugging!
- Thanks to [OpenScapes](../../../collaborators/openscapes/) for being great collaborators places where can work with people like Andy
