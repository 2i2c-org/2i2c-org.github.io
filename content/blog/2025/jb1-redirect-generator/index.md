---
title: "Creating a re-usable redirect generator for Jupyter Book 1 migrations"
slug: "jb1-redirect-generator"
date: "2025-11-12"
authors:
  - Chris Holdgraf
categories:
- upstream-impact
tags:
- learning
- open-source
- jupyterbook
---

When migrating documentation from [Jupyter Book](/collaborators/jupyter-book/) 1 to Jupyter Book 2, URL structures change dramatically and break external links. We spent some time createing a re-usable tool to solve this problem across multiple projects.

You can check out the tool below:

https://github.com/jupyter-book/jb1-redirect-generator

It's designed to be run in a self-contained way by putting the dependencies in `script` metadata at the top.
This means you can run it like this:

```bash
uv run https://raw.githubusercontent.com/jupyter-book/jb1-redirect-generator/main/generate_redirects.py
```

This let's you generate redirects from JB1 -> JB2 URL structures and dump them in a `_build/html` folder with your JB2 built pages.

We tested this out by converting the [Jupyter Governance docs](https://jupyter.org/governance) to Jupyter Book 2 and running it there.
You can find a noxfile that runs these commands here:

https://github.com/jupyter/governance/blob/bcdae30efdecbe75bc4751ef1fe1e602fe82ee10/noxfile.py#L25-L37

And its use in a GitHub Workflow here:

https://github.com/jupyter/governance/blob/bcdae30efdecbe75bc4751ef1fe1e602fe82ee10/.github/workflows/deploy.yml#L39-L44

## Learn more

- [jb1-redirect-generator repository](https://github.com/jupyter-book/jb1-redirect-generator)
- [Jupyter governance PR using the new script](https://github.com/jupyter/governance/pull/307)

