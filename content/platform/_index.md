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
    design:
        columns: 2
    content:
      title: A shared platform for global communities
      subtitle: Our interactive computing platform helps communities create a digital home for data-driven discovery with open tools and services.
      text: |

        {{< figure src="/images/service/shared-infrastructure.png" alt="Serving multiple communities with the same infrastructure.">}}

        {{< cta cta_text="Learn about our community network" cta_link="/communities" cta_new_tab="false" >}}
        
  - block: markdown
    id: numbers
    content:
      title: Hubs enable the research lifecycle with open tools and services
      subtitle: Interactive computing hubs integrate open tools and services to provide a digital home that bootstraps users from learning their first workflows to making discoveries and sharing with others.
      text: |

        {{< figure src="/images/service/research-lifecycle.png" alt="The research lifecycle we enable.">}}

        <center> <strong>Open source tools we use and support in our service. See below for some of the workflows these tools enable.</strong></center>

        <div class="container logos">
            <div class="row justify-content-center">
                <div class="section-heading d-flex flex-wrap justify-content-center col-12 mb-3 text-center">
                    <img class="logo col-6 col-md-4" src="/images/logos/project/jupyterlab.svg" alt="Jupyter Lab logo">
                    <img class="logo col-6 col-md-4" src="/images/logos/project/jupyterhub.svg" alt="Jupyter Hub logo">
                    <img class="logo col-6 col-md-4" src="/images/logos/project/jupyterbook.svg" alt="Jupyter Book logo">
                    <img class="logo col-6 col-md-4" src="/images/logos/project/jupyter.svg" alt="Jupyter logo">
                    <img class="logo col-6 col-md-4" src="/images/logos/project/myst.svg" alt="MyST logo">
                    <img class="logo col-6 col-md-4" src="/images/logos/project/binder.svg" alt="Binder logo">
                </div>
            </div>
        </div>

  - block: markdown
    id: magiclink
    design:
        columns: 2
    content:
      title: Magic links let you instantly share content on a hub
      subtitle: Create and share a magic link to instantly share a copy of your content with anyone so that they can interact and explore with live code and data.
      text: |

        {{< video src="videos/magic-links.mp4">}}
        
        <p class="figcaption">
          Powered by <a href="https://mystmd.org"><img src="/images/logos/project/myst.svg" /></a> and <a href="https://jupyterhub.readthedocs.io"><img src="/images/logos/project/jupyterhub.svg" /></a>
        </p>
  - block: markdown
    id: jupyterlab
    design:
        columns: 2
        css_class: reverse-markdown-row
    content:
      title: Flexible interfaces for data-driven discovery
      subtitle:  JupyterLab provides a flexible user interface to create and explore notebooks, interactive visualizations, and computational narratives.
      text: |

        {{< video src="videos/jupyterlab.mp4">}}

        <p class="figcaption">
          Powered by <a href="https://jupyterlab.readthedocs.io"><img src="/images/logos/project/jupyterlab.svg" /></a> and <a href="https://mystmd.org"><img src="/images/logos/project/myst.svg" /></a> 
        </p>

  - block: markdown
    id: environment-choice
    design:
        columns: 2
    content:
      title: Choose a community environment, or create your own
      subtitle:  Community leaders can offer many environments for users to fit all of their workflows.
      text: |

        {{< figure src="/images/service/server-choices.png" >}}

        <p class="figcaption">
          Powered by <a href="https://jupyterhub.readthedocs.io"><img src="/images/logos/project/jupyterhub.svg" /></a> and <a href="https://repo2docker.readthedocs.io"><img src="/images/logos/project/repo2docker.png" /></a>
        </p>
  - block: markdown
    id: knowledge-base
    design:
        columns: 2
        css_class: reverse-markdown-row
    content:
      title: A shared knowledge base that connects with your hub
      subtitle:  Shared knowledge bases allow communities to contribute their ideas and work to a shared space that is accessible to the community.
      text: |

        {{< video src="videos/jupyterbook.mp4">}}

        <p class="figcaption">
          Powered by <a href="https://jupyterbook.org"><img src="/images/logos/project/jupyterbook.svg" /></a> and <a href="https://mystmd.org"><img src="/images/logos/project/myst.svg" /></a>
        </p>

  - block: markdown
    id: jupyterhub
    design:
        columns: 2
        css_class: reverse-row
    content:
      title: JupyterHub gives your users their own digital space
      subtitle: Community leaders can manage user access to the hub, and provide each user their own workspace that persists over time.
      text: |

        {{< video src="videos/jupyterhub-admin.mp4">}}

        <p class="figcaption">
          Powered by <a href="https://jupyterhub.readthedocs.io"><img src="/images/logos/project/jupyterhub.svg" /></a>
        </p>

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

