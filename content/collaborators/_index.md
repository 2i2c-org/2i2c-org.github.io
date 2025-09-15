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
      subtitle: These are organizations we've acknowledged in [our impact posts](https://2i2c.org/category/impact) from the [2i2c blog](https://2i2c.org/blog). This is usually because of _funding_ or _collaborating on_ impact that 2i2c has had, as part of our [commitment to collaborative practices](../open-practices).

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
---