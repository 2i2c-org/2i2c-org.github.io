---
# Page title
title: 2i2c
# Page type - we want a landing page (such as a homepage)
type: landing

# Your landing page sections - add as many different content blocks as you like
sections:
  - block: hero
    content:
      title: Open infrastructure for research and education
      cta:
        label: How our model works
        url: /membership
      cta_alt:
        label: Join our network
        url: /join
      text: |-
        We're a non-profit that believes communities shouldn't choose between managing their own servers and vendor lock-in. We operate shared cloud infrastructure so you can focus on discovery, and we contribute to the open source tools that make it possible.
    design:
      background:
        text_color_light: true
        image:
          filename: "herobg.png"
          parallax: false
          brightness: 1

  - block: markdown
    id: service
    content:
      title: Each community gets a hub with the tools, data, and resources for their workflows
      subtitle:
      text: |

        {{< servicetech >}}

        [Membership](/membership) in our network provides access to our [hub platform](/platform) so your community can create and share knowledge with open infrastructure.

        <div class="row">
            <div id="stats" class="section-heading d-flex flex-wrap col-12 mb-3">
                <div class="stat col-3">
                    <h5 class="card-title text-uppercase text-muted mb-0">Communities</h5>
                    <span class="h2 font-weight-bold mb-0">>90</span>
                </div>
                <div class="stat col-3">
                    <h5 class="card-title text-uppercase text-muted mb-0">Active users</h5>
                    <span class="h2 font-weight-bold mb-0">>6500</span>
                </div>
                <div class="stat col-3">
                    <h5 class="card-title text-uppercase text-muted mb-0">Countries</h5>
                    <span class="h2 font-weight-bold mb-0">>15</span>
                </div>
                <div class="stat col-3">
                    <h5 class="card-title text-uppercase text-muted mb-0">Upstream PRs</h5>
                    <span class="h2 font-weight-bold mb-0">>2000</span>
                </div>
            </div>
        </div>

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
        </style>

        <ul id="who-logos" class="list-inline greyscale">
            <li class="list-inline-item"><a href="https://nasa.gov" target="_blank"><img src="/images/logos/community/nasa.svg" alt="Nasa logo"></a></li>
            <li class="list-inline-item"><a href="https://www.si.edu/" target="_blank"><img src="/images/logos/community/smithsonian.svg" alt="Smithsonian logo"></a></li>
            <li class="list-inline-item"><a href="https://www.hhmi.org/" target="_blank"><img src="/images/logos/community/howard-hughes-medical-institute.svg" alt="Howard Hughes Medical Institute logo"></a></li>
            <li class="list-inline-item"><a href="https://ncas.ac.uk/" target="_blank"><img src="/images/logos/community/ncas.png" alt="NCAS logo"></a></li>
            <li class="list-inline-item"><a href="https://pangeo.io/" target="_blank"><img src="/images/logos/community/pangeo.svg" alt="Pangeo logo"></a></li>
            <li class="list-inline-item"><a href="https://www.utoronto.ca/" target="_blank"><img src="/images/logos/community/university-of-toronto.svg" alt="University of toronto logo"></a></li>
            <li class="list-inline-item"><a href="https://columbia.edu/" target="_blank"><img src="/images/logos/community/columbia-university.png" alt="Columbia University logo"></a></li>
        </ul>

        {{< cta cta_text="Learn how membership works" cta_link="/membership" cta_new_tab="false" >}}

  - block: markdown
    id: what-is-hub
    content:
      title: What is a community hub?
      subtitle: A hub is a cloud environment where your community can access shared tools, data, and computational resources.
      text: |
        <figure class="videofigure">
          {{< video src="videos/jupyterhub-environment.mp4">}}

          <figcaption>
              Powered by <a href="https://jupyterhub.readthedocs.io"><img src="/images/logos/project/jupyterhub.svg" /></a> and <a href="https://repo2docker.readthedocs.io"><img src="/images/logos/project/repo2docker.png" /></a>.
          </figcaption>
        </figure>

        <div class="row row-cols-3 mt-4">
          <div class="col text-center"><strong>Custom environments</strong><br/>Choose from community-maintained stacks or bring your own.</div>
          <div class="col text-center"><strong>Managed access</strong><br/>Community leaders control who can use the hub.</div>
          <div class="col text-center"><strong>Scalable compute</strong><br/>From laptops to GPUs, sized for your workflows.</div>
        </div>

        {{< cta cta_text="Explore platform features" cta_link="/platform" cta_new_tab="false" >}}

  - block: features
    id: why-2i2c
    content:
      title: What makes us different
      items:
        - name: Non-profit, no vendor lock-in
          icon: lock-open
          icon_pack: fas
          description: We exist to serve research and education communities, not shareholders. Your [Right to Replicate](/right-to-replicate) means you can take your infrastructure anywhere, with or without us.
        - name: Open source collaboration
          icon: arrows-spin
          icon_pack: fas
          description: We listen to researchers and educators, then work with upstream open source projects on solutions that benefit everyone — not just our members.
        - name: Cross-community learning
          icon: people-arrows
          icon_pack: fas
          description: Our network connects communities across disciplines. When geoscientists and biologists face similar challenges, we bridge the gap through shared tools and practices.

  - block: collection
    id: posts
    content:
      title: Recent work
      subtitle: We share our progress and impact on [our blog](/blog).
      count: 3
      filters:
        folders:
          - blog
        exclude_featured: false
        exclude_future: false
        exclude_past: false
      offset: 0
      order: desc
      archive:
        enable: true
        text: View all blog posts
        link: /blog/
    design:
      view: masonry
      columns: '1'
      css_class: 'recent-posts-row'

  - block: markdown
    id: join-cta
    content:
      title: Learn more or get started
      text: |
        {{< cta cta_text="See membership options" cta_link="/join" cta_new_tab="false" >}}

---
