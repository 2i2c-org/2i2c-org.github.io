---
# Page title
title: Hub service
# Page type - we want a landing page (such as a homepage)
type: landing
aliases:
  - /hub-services/
  - /service/

sections:
  

  - block: features
    design:
      css_class: "bigtitle"
    content:
      title: Create a home with everything your community needs for data-driven discovery
      subtitle: Each community gets their own hub with access to the tools, data, and computing resources needed for their work. Behind the scenes, we operate [shared infrastructure](/membership#model) so improvements benefit everyone and flow back to open source. Your [Right to Replicate](/right-to-replicate) ensures you're never locked in.

      items:
        - icon: software
          icon_pack: custom
          name: Software & Tools
          description: "Provide easy access to community software and tools."
        - icon: compute
          icon_pack: custom
          name: Compute & Data
          description: "Provide the hardware and data resources available to your community."
        - icon: content
          icon_pack: custom
          name: Computational Content
          description: "Facilitate learning and sharing through community documentation."
  - block: markdown
    id: hub-services-intro
    content:
      title: A network of independent community hubs with shared infrastructure
      text: |
        <style>
        /* This makes the titles on the page a bit bigger to differentiate section titles */
        .bigtitle h1 {
          font-size: 2.2em;
        }
        </style>

        Each community gets their own hub, customized to their needs, while benefiting from a [common infrastructure repository](https://github.com/2i2c-org/infrastructure) that lets us deploy improvements everywhere at once. We manage and develop your hub infrastructure so you can focus on your work.

        {{< cta cta_text="Learn how our collaborative model works" cta_link="/membership#model" cta_new_tab="false" >}}


  - block: markdown
    id: hub-service-intro
    design:
      css_class: "bigtitle"
    content:
      title: Standard hub features
      subtitle: Below we outline our standard hub configuration options, which can be usually be **deployed in 1 day or less**. Should your community require a more customized approach, don't hesitate to [contact us](../join/_index.md) to discuss your specific requirements.
                
  - block: markdown
    content:
      title: Sign-in
      text: |
        We support the following authentication and authorization options:
          - **GitHub** - with support for GitHub Organization and Teams
          - **CILogon** - with support for institutional logins, Google Auth, Microsoft, and ORCID
          - **Shared Password** - simple authentication with a global shared password, ideal for workshops and webinar

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

        We can also co-locate your hub's compute next to your cloud data to improve performance and costs, with AWS and Google Cloud Platform supported out-of-the-box, and Azure configurations available on request.

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
            Powered by <a href="https://mystmd.org"><img src="/images/logos/project/myst.svg" /></a> and <a href="https://jupyterhub.readthedocs.io"><img src="/images/logos/project/jupyterhub.svg" /></a>. Example from <a href="https://www.biorxiv.org/content/10.1101/2024.01.25.577295v4">the Spyglass toolbox paper</a>.
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
      title: Community branding and white labeling
      subtitle: ""
      text: |
        Looking to customize your hub's look and feel to match your community? We can give your hub a unique look to match your message and mission, with a customizable landing page, branding, and announcements area.

  - block: markdown
    id: join
    content:
      title: "Join our community network"
      subtitle: |
        
      text: |

        {{< cta cta_text="Join our network of communities" cta_link="/join" cta_new_tab="false" >}}

---

