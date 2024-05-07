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
      title: A shared platform for global communities.
      subtitle: An interactive computing platform for communities that create and share knowledge.
      text: |

        {{< figure src="/images/service/shared-infrastructure.png" alt="Serving multiple communities with the same infrastructure.">}}

        {{< cta cta_text="Learn about our community network" cta_link="/communities" cta_new_tab="false" >}}
        
  - block: markdown
    id: numbers
    content:
      title: The research lifecycle we enable.
      subtitle: Interactive computing hubs provide tools that facilitate the entire knowledge creation and sharing lifecycle.
      text: |

        {{< figure src="/images/service/research-lifecycle.png" alt="The research lifecycle we enable.">}}

  - block: markdown
    id: magiclink
    design:
        columns: 2
    content:
      title: Magic links let you instantly share content on a hub.
      subtitle:  Clicking a magic link to instantly give a user their own copy of your content so that they can interact and explore in a live environment.
      text: |

        {{< video src="videos/magic-links.mp4">}}

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

  - block: markdown
    id: environment-choice
    design:
        columns: 2
    content:
      title: Choose a community environment, or create your own.
      subtitle:  Community leaders can offer many environments for users to fit all of their workflows.
      text: |

        {{< figure src="/images/service/server-choices.png" >}}

  - block: markdown
    id: knowledge-base
    design:
        columns: 2
        css_class: reverse-markdown-row
    content:
      title: A shared knowledge base that connects with your hub.
      subtitle:  Shared knowledge bases allow communities to contribute their ideas and work to a shared space that is accessible to the community.
      text: |

        {{< video src="videos/jupyterbook.mp4">}}

  - block: markdown
    id: jupyterhub
    design:
        columns: 2
        css_class: reverse-row
    content:
      title: JupyterHub gives your users their own digital space.
      subtitle: Community leaders can manage user access to the hub, and provide each user their own workspace that persists over time.
      text: |

        {{< video src="videos/jupyterhub-admin.mp4">}}


  - block: features
    id: clouds
    content:
      title: Supported cloud providers.
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
      title: Learn more about our organization.
      subtitle: 
      text: |

        {{% about-hubs %}}

  - block: markdown
    id: learncommunities
    content:
      title: Learn more about our community network.
      subtitle: 
      text: |

        {{< cta cta_text="Learn about our community network" cta_link="/communities" cta_new_tab="false" >}}



---

