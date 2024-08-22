---
# Page title
title: 2i2c
# Page type - we want a landing page (such as a homepage)
type: landing

# Your landing page sections - add as many different content blocks as you like
sections:
  - block: hero
    content:
      title: A global network of community hubs for interactive learning and discovery
      # image:
      #   # Reference an image in your `assets/media/` folder
      #   filename: hero-academic.png
      # Add your Call-To-Action (CTA) button and optional icon
      cta:
        label: Learn about our interactive computing platform
        url: /platform
        #icon_pack: fas
        #icon: download
      # Optionally, add an alternative CTA link
      cta_alt:
        label: Join our network
        url: /join
      # Optionally, add a note under the Call-To-Action button
      # cta_note:
      #   label: >-
                  
      # Add your Hero text here
      text: |-
        Our interactive computing platform gives research and education communities a digital home to create and share knowledge with a global network of communities to learn from.
    design:
      # Choose an optional background color, gradient, image, or video
      background:
        text_color_light: true
        image:
          filename: "herobg.png"
          parallax: false
          brightness: 1

  - block: markdown
    id: service
    content:
      title: We help communities build their own interactive computing hub in the cloud with open infrastructure
      subtitle: 
      text: |

        {{< servicetech >}}

        2i2c's [community hub platform and consultancy services](/platform) ensure your community makes the best use of open infrastructure for interactive computing in the cloud.

        We serve **over 90 communities across the globe** with **over 7000 active users** dedicated to creating and sharing knowledge. See [our community impact stories](/communities) for inspiration.

        <style>
          #who-logos {
            display: flex;
            flex-wrap: wrap;
            align-items: center;
            gap: 1em;
          }
          .list-inline-item {
            flex: 1
          }

          .list-inline-item img {
            filter: grayscale(100%); /* Desaturates the image completely */
          }
        </style>

        <ul id="who-logos" class="list-inline">
            <li class="list-inline-item"><a href="https://nasa.gov" target="_blank"><img src="/images/logos/community/nasa.svg" alt="Nasa logo"></a></li>
            <li class="list-inline-item"><a href="https://www.si.edu/" target="_blank"><img src="/images/logos/community/smithsonian.svg" alt="Smithsonian logo"></a></li>
            <li class="list-inline-item"><a href="https://www.hhmi.org/" target="_blank"><img src="/images/logos/community/howard-hughes-medical-institute.svg" alt="Howard Hughes Medical Institute logo"></a></li>
            <li class="list-inline-item"><a href="https://ncas.ac.uk/" target="_blank"><img src="/images/logos/community/ncas.png" alt="NCAS logo"></a></li>
            <li class="list-inline-item"><a href="https://pangeo.io/" target="_blank"><img src="/images/logos/community/pangeo.svg" alt="Pangeo logo"></a></li>
            <li class="list-inline-item"><a href="https://www.utoronto.ca/" target="_blank"><img src="/images/logos/community/university-of-toronto.svg" alt="University of toronto logo"></a></li>
            <li class="list-inline-item"><a href="https://columbia.edu/" target="_blank"><img src="/images/logos/community/columbia-university.png" alt="Columbia University logo"></a></li>
        </ul>

        {{< cta cta_text="Join our network of community hubs" cta_link="/join" cta_new_tab="false" >}}

  - block: markdown
    id: jupyterhub
    design:
        columns: 2
    content:
      title: Manage and monitor resources and users
      subtitle: Community leaders can manage user access to the hub, and provide each user their own workspace that persists over time.
      text: |
        <figure class="videofigure">
          {{< video src="videos/jupyterhub-admin.mp4">}}

          <figcaption>
              Powered by <a href="https://jupyterhub.readthedocs.io"><img src="/images/logos/project/jupyterhub.svg" /></a>
          </figcaption>
        </figure>

  - block: markdown
    id: jupyterlab
    design:
        columns: 2
        css_class: reverse-markdown-row
    content:
      title: Design interactive interfaces for data-driven discovery
      subtitle:  JupyterLab provides a flexible user interface to create and explore notebooks, interactive visualizations, and computational narratives.
      text: |

        <figure class="videofigure">
          {{< video src="videos/jupyterlab.mp4">}}

          <figcaption>
              Powered by <a href="https://jupyterlab.readthedocs.io"><img src="/images/logos/project/jupyterlab.svg" /></a> and <a href="https://mystmd.org"><img src="/images/logos/project/myst.svg" /></a>. Example from <a href="https://github.com/google/neuroglancer"> Neuroglancer-JupyterLab</a>.
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
      title: Share workflows with a community knowledge base.
      subtitle:  Shared knowledge bases allow communities to contribute their ideas and work to a shared space that is accessible to the community.
      text: |
        <figure class="videofigure">
          {{< video src="videos/jupyterbook.mp4">}}

          <figcaption>
              Powered by <a href="https://jupyterbook.org"><img src="/images/logos/project/jupyterbook.svg" /></a> and <a href="https://mystmd.org"><img src="/images/logos/project/myst.svg" /></a>. Example from <a href="https://book.cryointhecloud.com/intro.html">the CryoCloud JupyterBook</a>.
          </figcaption>
        </figure>

  - block: markdown
    id: magiclink
    design:
        columns: 2
    content:
      title: Share content and interactive links to a hub
      subtitle: Create and share a magic link to instantly share a copy of your content with anyone so that they can interact and explore with live code and data.
      text: |

        <figure class="videofigure">
          {{< video src="videos/magic-links.mp4">}}
          
          <figcaption>
            Powered by <a href="https://mystmd.org"><img src="/images/logos/project/myst.svg" /></a> and <a href="https://jupyterhub.readthedocs.io"><img src="/images/logos/project/jupyterhub.svg" /></a>. Example from <a href="https://www.biorxiv.org/content/10.1101/2024.01.25.577295v1">the Spyglass toolbox paper</a>.
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
    id: learnplatform
    content:
      title: Learn more about our platform.
      subtitle: 
      text: |

        {{< cta cta_text="Learn about our interactive computing platform" cta_link="/platform" cta_new_tab="false" >}}

  - block: markdown
    id: learnmore
    design:
        columns: 2
    content:
      title: Learn more about our organization.
      subtitle: 
      text: |

        {{% about-hubs %}}

---

