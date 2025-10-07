---
title: Impact
type: landing

# Your landing page sections - add as many different content blocks as you like
sections:
  - block: markdown
    id: numbers
    content:
      title: We enable open science and open source communities to have global impact.
      subtitle: 
      text: |

        <style>
        figure.map {
          margin-bottom: 0;
        }

        figure.map img {
          border: none;
          width: 66%;
        }
        figure.map figcaption {
          margin: 1em auto;
        }

        .showcase:nth-child(even) div.row {
            display: flex;
            flex-direction: row-reverse;
        }
        </style>

        <figure class="map">
          {{< figure src="/images/communities/map-of-communities.png" >}}

          <figcaption>
            Active communities in our network.
            See <a href="https://2i2c.org/kpis/cloud/#geographic-map-of-community-locations">our interactive map of active communities</a> for the latest data.
          </figcaption>
        </figure>

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

        <div class="cta-group" class="margin: 0 auto;">

        </div>
        

  - block: portfolio
    id: posts
    content:
      title: Stories of our impact
      subtitle: We use [the 2i2c blog](https://2i2c.org/blog) to share all of our impact stories.
      text: ''
      # Choose how many pages you would like to display (0 = all pages)
      count: 5
      # Filter on criteria
      filters:
        # The folders to display content from
        folders:
          - blog
        # These are the tags that will show up in the list
        tags: ["earth-science", "biology", "education", "open source"]
        author: ""
        publication_type: ""
        featured_only: false
        exclude_featured: false
        exclude_future: false
        exclude_past: false
      # Choose how many pages you would like to offset by
      # Useful if you wish to show the first item in the Featured widget
      offset: 0
      # Field to sort by, such as Date or Title
      sort_by: 'Date'
      sort_ascending: false
      buttons:
        - name: All
          tag: '*'
        - name: Earth Science
          tag: earth-science
        - name: Biology
          tag: biology
        - name: Education
          tag: education
        - name: Open Source
          tag: open-source
    design:
      # Choose a listing view
      view: masonry
      # Choose single or dual column layout
      columns: '1'
      css_class: "home-stories"

  - block: markdown
    id: join
    content:
      title: "Become a member community"
      subtitle: |
        
      text: |

        {{< cta cta_text="Join our network of communities" cta_link="/join" cta_new_tab="false" >}}

---