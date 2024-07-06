---
# Page title
title: Cloud platform
# Page type - we want a landing page (such as a homepage)
type: landing
aliases:
  - /service/


# Your landing page sections - add as many different content blocks as you like
sections:
  - block: markdown
    id: numbers
    content:
      title: A shared platform for global communities
      subtitle: Our interactive computing hubs provide frictionless access to open infrastructure to connect, create, and share knowledge using data.
      text: |
        {{< servicetech >}}

        {{< cta cta_text="See how research and education communities use this platform" cta_link="/communities" cta_new_tab="false" >}}

  - block: markdown
    id: numbers
    content:
      title: Each hub integrates open tools and services to enable the lifecycle of knowledge creation
      subtitle: Hubs are a digital home that bootstraps users from learning their first workflows to making discoveries and sharing with others.
      text: |
        {{< figure src="/images/service/research-lifecycle.png" alt="The research lifecycle we enable.">}}

        <center> <strong>Open source tools we use and support in our service.</strong></center>

        {{< opensourcelogos >}}

  - block: markdown
    id: magiclink
    design:
        columns: 2
    content:
      title: Magic links let you instantly share content on a hub
      subtitle: Create and share a magic link to instantly share a copy of your content with anyone so that they can interact and explore with live code and data.
      text: |

        <figure class="videofigure">
          {{< video src="videos/magic-links.mp4">}}
          
          <figcaption>
            Powered by <a href="https://mystmd.org"><img src="/images/logos/project/myst.svg" /></a> and <a href="https://jupyterhub.readthedocs.io"><img src="/images/logos/project/jupyterhub.svg" /></a>. Example from <a href="https://www.biorxiv.org/content/10.1101/2024.01.25.577295v1">the Spyglass toolbox paper</a>.
          </figcaption>
        </figure>
  - block: markdown
    id: jupyterlab
    design:
        columns: 2
        css_class: reverse-markdown-row
    content:
      title: Flexible interfaces for data-driven discovery
      subtitle:  JupyterLab provides a flexible user interface to create and explore notebooks, interactive visualizations, and computational narratives.
      text: |

        <figure class="videofigure">
          {{< video src="videos/jupyterlab.mp4">}}

          <figcaption>
              Powered by <a href="https://jupyterlab.readthedocs.io"><img src="/images/logos/project/jupyterlab.svg" /></a> and <a href="https://mystmd.org"><img src="/images/logos/project/myst.svg" /></a>. 
          </figcaption>
        </figure>

  - block: markdown
    id: environment-choice
    design:
        columns: 2
    content:
      title: Choose a community environment, or create your own
      subtitle:  Community leaders can offer many environments for users to fit all of their workflows.
      text: |
        <figure class="videofigure">
          {{< video src="/videos/jupyterhub-environment.mp4" >}}

          <figcaption>
              Powered by <a href="https://jupyterhub.readthedocs.io"><img src="/images/logos/project/jupyterhub.svg" /></a> and <a href="https://repo2docker.readthedocs.io"><img src="/images/logos/project/repo2docker.png" /></a>. Example from <a href="https://www.earthdata.nasa.gov/esds/veda">the NASA VEDA project</a>.
          </figcaption>
        </figure>
  - block: markdown
    id: knowledge-base
    design:
        columns: 2
        css_class: reverse-markdown-row
    content:
      title: A shared knowledge base that connects with your hub
      subtitle:  Shared knowledge bases allow communities to contribute their ideas and work to a shared space that is accessible to the community.
      text: |
        <figure class="videofigure">
          {{< video src="videos/jupyterbook.mp4">}}

          <figcaption>
              Powered by <a href="https://jupyterbook.org"><img src="/images/logos/project/jupyterbook.svg" /></a> and <a href="https://mystmd.org"><img src="/images/logos/project/myst.svg" /></a>. Example from <a href="https://book.cryointhecloud.com/intro.html">the CryoCloud JupyterBook</a>.
          </figcaption>
        </figure>

  - block: markdown
    id: jupyterhub
    design:
        columns: 2
    content:
      title: JupyterHub gives your users their own digital space
      subtitle: Community leaders can manage user access to the hub, and provide each user their own workspace that persists over time.
      text: |
        <figure class="videofigure">
          {{< video src="videos/jupyterhub-admin.mp4">}}

          <figcaption>
              Powered by <a href="https://jupyterhub.readthedocs.io"><img src="/images/logos/project/jupyterhub.svg" /></a>
          </figcaption>
        </figure>

  - block: markdown
    id: desktop
    design:
        columns: 2
        css_class: reverse-markdown-row
    content:
      title: Serve linux applications via a remote desktop
      subtitle: You can provide users a full linux UI that provides access to GUI applications via the web.
      text: |

        <figure class="videofigure">
          {{< video src="videos/desktop.mp4">}}
          
          <figcaption>
              Powered by <a href="https://jupyterhub.readthedocs.io"><img src="/images/logos/project/jupyterhub.svg" /></a>. Example from <a href="https://www.earthdata.nasa.gov/esds/veda">the NASA VEDA project</a>.
          </figcaption>
        </figure>

  - block: features
    id: clouds
    content:
      title: Supported cloud providers
      subtitle: ""
      text: |
        2i2c aims to support JupyterHubs on any cloud provider that offers a managed Kubernetes service.
        To start, we are focusing on the major commercial cloud providers listed below.
        If you would like a hub hosted on a different cloud provider, please [give us your feedback](mailto:hello@2i2c.org).
        See [our Organizational Strategy and Goals](https://compass.2i2c.org/organization/strategy.html) to learn more about our plans.

      items:
        - icon: google-cloud
          icon_pack: custom
          name: Google Cloud
          description: ""
        - icon: azure 
          icon_pack: custom
          name: Microsoft Azure
          description: ""
        - icon: aws
          icon_pack: custom 
          name: Amazon Web Services
          description: ""

  - block: markdown
    id: learnmore
    design:
        columns: 2
    content:
      title: Learn more about our organization
      subtitle: 
      text: |

        {{% about-hubs %}}

  - block: markdown
    id: learncommunities
    content:
      title: Learn more about our community network
      subtitle: 
      text: |

        {{< cta cta_text="Learn about our community network" cta_link="/communities" cta_new_tab="false" >}}



---

