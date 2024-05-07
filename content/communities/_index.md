---
# Page title
title: Our network of communities
# Page type - we want a landing page (such as a homepage)
type: landing

# Your landing page sections - add as many different content blocks as you like
sections:
  - block: markdown
    id: numbers
    content:
      title: A shared platform for global communities.
      subtitle: 
      text: |

        {{< figure src="/images/communities/map-of-communities.png" >}}

        We serve a global network of communities that create and share knowledge.
        The map above shows active communities in our network, and the size of each circle corresponds to the size of each community.
        See [our interactive map of active communities](https://2i2c.org/kpis/cloud/#map-of-hubs) for the latest data.

        <style>
        .showcase:nth-child(even) div.row {
            display: flex;
            flex-direction: row-reverse;
        }
        </style>

        <div class="row">
            <div id="stats" class="section-heading d-flex flex-wrap col-6 mb-3">
                <h2 class="mb-0">2i2c in numbers</h2>
                <div class="stat col-6">
                    <h5 class="card-title text-uppercase text-muted mb-0">Communities</h5>
                    <span class="h2 font-weight-bold mb-0">>80</span>
                </div>
                <div class="stat col-6">
                    <h5 class="card-title text-uppercase text-muted mb-0">Active users</h5>
                    <span class="h2 font-weight-bold mb-0">>6500</span>
                </div>
                <div class="stat col-6">
                    <h5 class="card-title text-uppercase text-muted mb-0">Countries</h5>
                    <span class="h2 font-weight-bold mb-0">>15</span>
                </div>
                <div class="stat col-6">
                    <h5 class="card-title text-uppercase text-muted mb-0">Upstream PRs</h5>
                    <span class="h2 font-weight-bold mb-0">>2000</span>
                </div>
            </div>
            <div class="section-heading col-6 mb-3">
                <h2 class="mb-0">Case studies</h2>
                <ul class="link-list">
                    <li><a href="#cryocloud">Distributed cryosphere research</a></li>
                    <li><a href="#data8">Data science education</a></li>
                    <li><a href="#spyglass">Communicating open science</a></li>
                    <li><a href="#catalyst">Global hubs for biomedical imaging</a></li>
                </ul>
            </div>
        </div>

        {{< cta cta_text="Join our community network" cta_link="/join" cta_new_tab="false" >}}
       
  - block: markdown
    id: cryocloud
    design:
        columns: 2
        css_class: showcase
    content:
      title: "Research community: Cryosphere research in the cloud"
      subtitle: Cryocloud is a research hub dedicated to "accelerating discovery and enhancing collaboration for NASA Cryosphere communities". They use their hub to provide access to [NASA Earthdata cloud](https://book.cryointhecloud.com/tutorials/NASA-Earthdata-Cloud-Access/1.Intro-Earthdata-Cloud.html) use a [community Jupyter Book](https://book.cryointhecloud.com) to organize training and learning within the community via community workshops.
      text: |

        {{< figure src="/images/communities/cryocloud-landing.png" >}}
        {{< figure src="/images/communities/cryocloud-data.png" >}}

        [landing page](https://cryointhecloud.com/) | [Community knowledge base](http://book.cryointhecloud.com/)


  - block: markdown
    id: data8
    design:
        columns: 2
        css_class: showcase
        

    content:
      title: "Education community: Data 8 for Community Colleges in California "
      subtitle: The [Data 8 class](https://data8.org) began as a large introductory data science class at UC Berkeley. It uses a Jupyter Book for all course materials, and uses [JupyterHub magic links](/platform/#magiclink) to distribute course content from the textbook. 2i2c is working with the Data 8 team to deploy JupyterHubs for community colleges in California that run the Data 8 course, to make the infrastructure and content broadly accessible.
      text: |

        {{< figure src="/images/communities/data8-landing.png" >}}
        {{< figure src="/images/communities/data8-textbook.png" >}}

        [landing page](https://cdss.berkeley.edu/education/courses/data-8/) | [Data 8 textbook](http://inferentialthinking.com/)

  - block: markdown
    id: catalyst
    design:
        columns: 2
        css_class: showcase
    content:
      title: "Research communities: The Catalyst Project: Serving historically marginalized communities"
      subtitle: The [Catalyst Project](https://catalystproject.cloud) serves interactive computing hubs to biomedical communities in Latin America and Africa. The project is aimed at learning about the unique challenges in serving communities in global regions that are historically under-served or under-resourced, with the goal of designing effective and sustainable interactive computing services for these communities.
      text: |

        {{< figure src="/images/communities/catalyst-landing.png" >}}
        {{< figure src="/images/communities/catalyst-training.png" >}}

        [Catalyst project page](https://catalystproject.cloud) | [Hub champion training](https://catalystproject.cloud/hub-champion-training/)


  - block: markdown
    id: spyglass
    design:
        columns: 2
        css_class: showcase
    content:
      title: "Research communication: The spyglass toolbox demonstration hub"
      subtitle: |
        [Spyglass](https://github.com/LorenFrankLab/spyglass) is a framework for reproducible and shareable neuroscience research produced by [Loren Frank's lab](https://github.com/LorenFrankLab) at the University of California, San Francisco. They recently released [a preprint about their toolbox](https://www.biorxiv.org/content/10.1101/2024.01.25.577295v3), and are using a 2i2c hub to provide accessible interactive cloud environments that demonstrate its functionality and helps researchers get started.
      text: |


        {{< figure src="/images/communities/spyglass-landing.png" >}}
        {{< figure src="/images/communities/spyglass-demo.png" >}}

        [Spyglass project page](https://lorenfranklab.github.io/spyglass/latest/) | [Biorxiv article](https://www.biorxiv.org/content/10.1101/2024.01.25.577295v1)

  - block: markdown
    id: learnmore-org
    design:
        columns: 2
    content:
      title: Learn more about our organization.
      subtitle: 
      text: |

        {{% about-hubs %}}


  - block: markdown
    id: join
    content:
      title: "Join our community network"
      subtitle: |
        
      text: |

        {{< cta cta_text="Join our network of communities" cta_link="/join" cta_new_tab="false" >}}

---