---
# Page title
title: Hub services
# Page type - we want a landing page (such as a homepage)
type: landing
aliases:
  - /hub-services/


# Your landing page sections - add as many different content blocks as you like
sections:
  - block: markdown
    id: hub-services-intro
    content:
      title: Your hub, the way you want it
      text: |
        At 2i2c, we have extensive expertise in rapidly deploying custom cloud computing hubs to help research and education communities create and share knowledge.

        This page outlines our standard hub configuration options, which can be usually be deployed with a short turnaround of 1 day or less.

        However, should your community require a more customized approach, please don't hesitate to [contact us](../join/_index.md) to discuss your specific requirements.

  - block: markdown
    content:
      title: Sign-in
      text: |
        We support the following authentication and authorization options:
          - GitHub - with support for GitHub Organization and Teams
          - CILogon - with support for institutional logins, Google Auth, Microsoft, and ORCID
          - Shared Password - simple authentication with a global shared password, ideal for workshops and webinars
        <figure class="videofigure">
          {{< video src="videos/jupyterhub-admin.mp4">}}

          <figcaption>
              Powered by <a href="https://jupyterhub.readthedocs.io"><img src="/images/logos/project/jupyterhub.svg" /></a>
          </figcaption>
        </figure>      

  - block: features
    content:
      title: Compute
      subtitle: | 
        We offer a choice of CPU, Memory (from 4GB to 512GB) and GPU configurations for all types of workloads, with added support for Dask Gateway for task parallelization. 

        We can also co-locate your hub's compute next to your cloud data to improve performance and costs, with AWS and Google Cloud Platform supported out-of-the box, and Azure configurations available on request.

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
    content:
      title: Software Stack
      subtitle: ""
      text: |
        2i2c supports a number of standard community-maintained images for research and education including Pangeo Notebook, SciPy, Julia, and Rocker with RStudio.

        Additionally, hub users can configure their hubs with any existing pre-built image hosted on [Docker Hub](https://hub.docker.com/) or [quay.io](https://quay.io).

        Hub administrators can also provide their own self-maintained images, should they wish to do so.
        
        {{< softwarestacklogos >}}

  - block: markdown
    content:
      title: Storage
      subtitle: ""
      text: |
        Hubs can be configured with a choice of persistent home directories and different levels of read-write permissions (admins only, or everyone).

        Additionally, object storage can be configured for access to scratch, persistent, or pre-existing buckets, as needed.

  - block: markdown
    content:
      title: Sharing
      subtitle: ""
      text: |
        Learning and discovery through interactive cloud computing are more powerful when shared.

        You can choose to let your hub users share their fully interactive projects through ephemeral hubs generated on the fly, giving others the opportunity to experience their work in full by simply clicking on a shared link.

        <figure class="videofigure">
          {{< video src="videos/magic-links.mp4">}}

          <figcaption>
            Powered by <a href="https://mystmd.org"><img src="/images/logos/project/myst.svg" /></a> and <a href="https://jupyterhub.readthedocs.io"><img src="/images/logos/project/jupyterhub.svg" /></a>. Example from <a href="https://www.biorxiv.org/content/10.1101/2024.01.25.577295v1">the Spyglass toolbox paper</a>.
          </figcaption>
        </figure>              

  - block: markdown
    content:
      title: Reporting and quotas
      subtitle: ""
      text: |
        Our hubs come standard with Grafana access to help users and administrators keep an eye on their usage and cost analytics, which together with configurable storage quotas help ensure that cost overruns and unexpected bill shocks are a thing of the past.

        {{< figure src="/images/service/grafana.png" alt="Grafana dashboard">}}

  - block: markdown
    content:
      title: White labelling
      subtitle: ""
      text: |
        Looking to customize your hub's look and feel to match your community? We can give your hub a unique look to match your message and mission, with a customizable landing page, branding, and announcements area.
        
  - block: markdown
    id: join-us
    content:
      title: 
      subtitle: 
      text: |

        {{< cta cta_text="Ready to join our growing network of community hubs?" cta_link="/join" cta_new_tab="false" >}}
            
---