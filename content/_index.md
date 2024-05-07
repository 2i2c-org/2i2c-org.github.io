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
      # cta_alt:
      #   label: Our mission
      #   url: mission
      # Optionally, add a note under the Call-To-Action button
      # cta_note:
      #   label: >-
                  
      # Add your Hero text here
      text: |-
        Our interactive computing platform gives your community a digital home to create and share knowledge, and a global network of communities to learn from.
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
      title: We give communities a home in the cloud for interactive computing.
      subtitle: 
      text: |

        Our interactive computing platform **empowers communities in research and education to design a hub for their unique workflows**. It brings together open source tools, data, and computational resources in a remotely-accessible interactive environment for creating and sharing knowledge.
                
        <style>
          img.logo {
            padding: 0 3em;
            margin-top: 1em;
          }
        </style>

        {{< figure src="/images/home/hub-diagram.png" >}}

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
    id: numbers
    content:
      title: We serve a global network of communities
      subtitle: 
      text: |

        We serve **over 80 communities across the globe** with **over 7000 active users** that are dedicated to creating and sharing knowledge. This includes **educational communities** that share knowledge within a community, **research communities** that create advances at the frontier of knowledge, and **applied knowledge communities** that use advances in knowledge to serve the public.

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

        {{< figure src="/images/home/worldmap.png" alt="2i2c map of communities" caption="A map of the rough location of communities with currently active hubs. Updated as of April 2024, [see our interactive map](https://2i2c.org/kpis/cloud/#map-of-hubs) for the latest data.">}}

        </p>

        <ul id="who-logos" class="list-inline">
            <li class="list-inline-item"><a href="https://nasa.gov" target="_blank"><img src="/images/logos/community/nasa.svg" alt="Nasa logo"></a></li>
            <li class="list-inline-item"><a href="https://www.si.edu/" target="_blank"><img src="/images/logos/community/smithsonian.svg" alt="Smithsonian logo"></a></li>
            <li class="list-inline-item"><a href="https://www.hhmi.org/" target="_blank"><img src="/images/logos/community/howard-hughes-medical-institute.svg" alt="Howard Hughes Medical Institute logo"></a></li>
            <li class="list-inline-item"><a href="https://ncas.ac.uk/" target="_blank"><img src="/images/logos/community/ncas.png" alt="NCAS logo"></a></li>
            <li class="list-inline-item"><a href="https://pangeo.io/" target="_blank"><img src="/images/logos/community/pangeo.svg" alt="Pangeo logo"></a></li>
            <li class="list-inline-item"><a href="https://www.utoronto.ca/" target="_blank"><img src="/images/logos/community/university-of-toronto.svg" alt="University of toronto logo"></a></li>
            <li class="list-inline-item"><a href="https://columbia.edu/" target="_blank"><img src="/images/logos/community/columbia-university.png" alt="Columbia University logo"></a></li>
        </ul>


  - block: markdown
    id: numbers
    content:
      title: We empower communities to share and learn.
      subtitle: Interactive computing hubs provide access to standardized workflows that make it easier for community members to teach and share with one another, and to enhance their work together.
      text: |

        {{< figure src="/images/service/community-improvements.png" alt="How communities improve with shared infrastructure.">}}


  - block: markdown
    id: numbers
    content:
      title: We make open source tools more impactful
      subtitle: 
      text: |

        Our global network gives us a unique perspective to identify high-impact improvements to open source tools. We collaborate with open source communities to make upstream enhancements, and re-deploy the improved tools to the communities in our network.

        {{< figure src="/images/home/os-lifecycle.png" alt="The lifecycle of upstream development">}}

  - block: features
    content:
      title: Grounded in open principles so communities can trust us as stewards of critical scientific workflows.
      subtitle: ""
      text: ""
      items:
        - name: Transparency
          description: Our transparent and participatory model keeps our incentives aligned with community needs.
          icon: magnifying-glass
          icon_pack: fas
        - name: Empowerment
          description: Our service gives communities agency to design the service they need, and to manage it without 2i2c if they wish.
          icon: bolt
          icon_pack: fas
        - name: Sustainability
          description: Our service should have a self-sustaining model that ensures continuity, growth, and funder independence.
          icon: dollar-sign
          icon_pack: fas

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
    id: learnplatform
    content:
      title: Learn more about our platform.
      subtitle: 
      text: |

        {{< cta cta_text="Learn about our interactive computing platform" cta_link="/platform" cta_new_tab="false" >}}

---

