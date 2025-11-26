---
# TO ADD A NEW COLLABORATOR
# - Create a new folder for that collaborator, keep the name short.
# - Add `index.md` with 2-3 sentences about what that collaborator does.
# - Add an image called featured.png/jpeg with their logo
# - Use `tags:` to mark them as `funder`, `member`, or `collaborator`
# - Reference the collaborator in a post like: ../../collaborators/czi/index.md

title: Our Collaborators
type: landing

sections:
  - block: markdown
    content:
      title: Our Collaborators
      text: |
        <style>
        .collaborators-explanation {
          font-size: .75em;
          text-align: left;
        }
        </style>
        These are organizations<sup><a href="#explanation">[1]</a></sup> we've acknowledged in the [2i2c blog](https://2i2c.org/blog) as part of our [commitment to collaborative practices](../open-practices). Click each logo to see a list of [impact posts](https://2i2c.org/category/impact) from that collaborator.


  - block: portfolio
    content:
      filters:
        folders:
          - collaborators
        exclude_featured: false
      count: 0
      buttons:
        - name: All
          tag: '*'
        - name: Funders
          tag: funder
        - name: Members
          tag: member
        - name: Collaborators
          tag: collaborator
    design:
      columns: '3'
      view: masonry
      flip_alt_rows: false
      css_class: collaborators-gallery
  - block: markdown
    content:
      text: |
        <style>
        .collaborators-explanation {
          font-size: .9em;
          text-align: left;
        }
        </style>
        <div class="collaborators-explanation" id="explanation">
        
        _How we define types of collaborators_.

        **Members** are part of [our member network](../members/) that contribute extra funding and time. These are for contirbutions beyond the [Foundational impact](blog/2025/good-citizen/index.md) that membership fees support.
        
        **Funders** primarily have impact by funding initiatives that we benefit from. We include funders when they directly benefit 2i2c or a project on which we collaborate, but not every funder for every member and collaborator that supports us.
        
        **Collaborators** are non-members we collaborate with for shared impact. These are often themselves made up of many organizations and individuals working together. In general, we try to highlight multi-stakeholder collaborations rather than the individual organizations within them.

        </div>
---