---
# Page type - we want a landing page
type: landing

sections:
  - block: markdown
    id: intro
    content:
      title: Our open practices
      subtitle: How we build trust through openness
      text: |
        We believe open science requires open practices. We make specific commitments to ensure our infrastructure remains open, portable, and community-controlled. See [our open source strategy](https://compass.2i2c.org/open-source/strategy/#upstream-first) for the full details.

  - block: markdown
    id: right-to-replicate
    design:
      columns: 2
    content:
      title: Right to Replicate
      text: |
        Your infrastructure is yours. Our [Right to Replicate](/right-to-replicate) gives communities the right to replicate their infrastructure in its entirety elsewhere, with or without 2i2c. We run our infrastructure on open source tools and vendor-agnostic cloud services so this is always possible.

  - block: markdown
    id: open-technology
    design:
      columns: 2
    content:
      title: Open Technology
      text: |
        All engineering artifacts produced by 2i2c are licensed under approved open source licenses. Our [commitment to open technology](/open-technology) ensures licensing practices that prevent negative outcomes for communities and protect against bait-and-switch relicensing.

  - block: markdown
    id: co-create
    design:
      columns: 2
    content:
      title: Upstream contributions
      text: |
        We take an [upstream first](https://compass.2i2c.org/open-source/strategy/#upstream-first) approach — improvements we build flow back to the open source projects they came from. We provide both [directed and foundational contributions](blog/2025/good-citizen/index.md) and [track our upstream impact](https://2i2c.org/kpis/upstream/) publicly.

  - block: markdown
    id: transparent
    design:
      columns: 2
    content:
      title: Transparency
      text: |
        We do our work openly. We are transparent about [organizations that support and fund us](../about/funding/index.md), communicate [in-progress work on our blog](blog/2025/communications-strategy/index.md), and publish [our roadmap](https://2i2c.org/roadmap) and [collaborators](/collaborators) for anyone to see.

  - block: markdown
    id: projects
    content:
      title: Open source projects we use and support
      text: |
        <style>
        .project-figures img {
          border: none !important;
          box-shadow: none !important;
        }
        </style>

        Below are a few tools and projects that we are particularly involved with, though the list of open source projects to which we contribute is much larger.

        <div class="project-figures">
        {{< figure
            target="https://jupyter.org"
            src="https://jupyter.org/assets/logos/rectanglelogo-greytext-orangebody-greymoons.svg"
            title="<p class='project-title'>Jupyter Notebooks</p><p class='project-caption'>Interactive documents for research and education.</p>"
            class="project-highlight"
        >}}

        {{< figure
            target="https://jupyterlab.readthedocs.io/en/stable/"
            src="https://avatars3.githubusercontent.com/u/22800682?s=400&v=4"
            title="<p class='project-title'>Jupyter Lab</p><p class='project-caption'>A customizable and extensible data science interface</p>"
            class="project-highlight"
        >}}

        {{< figure
            target="https://jupyter.org/hub"
            src="https://jupyter.org/assets/homepage/hublogo.svg"
            title="<p class='project-title'>JupyterHub</p><p class='project-caption'> Cloud-based computing environments for groups</p>"
            class="project-highlight"
        >}}

        {{< figure
            target="https://numfocus.org/sponsored-projects"
            src="/media/pydata-ecosystem.png"
            title="<p class='project-title'>The PyData Ecosystem</p><p class='project-caption'> Open Source tools for Scientific Computing</p>"
            class="project-highlight"
        >}}

        {{< figure
            target="https://jupyterbook.org/intro.html"
            src="/images/logos/project/jupyterbook.svg"
            title="<p class='project-title'>Jupyter Book</p><p class='project-caption'>Interactive, beautiful books with Jupyter</p>"
            class="project-highlight"
        >}}

        {{< figure
            target="https://docs.dask.org/en/latest/logos.html"
            src="https://docs.dask.org/en/latest/_images/dask_horizontal.svg"
            title="<p class='project-title'>Dask</p><p class='project-caption'>Advanced parallelism for analytics</p>"
            class="project-highlight"
        >}}
        </div>
---
