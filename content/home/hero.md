+++
# Hero widget.
widget = "hero"  # See https://sourcethemes.com/academic/docs/page-builder/
headless = true  # This file represents a page section.
active = true  # Activate this widget? true/false
weight = 100  # Order that this section will appear.

title = "The International Interactive Computing Collaboration"

# Hero image (optional). Enter filename of an image in the `static/img/` folder.
hero_media = "logo.png"

[design.background]
  # Apply a background color, gradient, or image.
  #   Uncomment (by removing `#`) an option to apply it.
  #   Choose a light or dark text color by setting `text_color_light`.
  #   Any HTML color name or Hex value is valid.

  # Background color.
  # color = "navy"

  # Background gradient.
  gradient_start = "#F37726"  # jupyter orange
  gradient_end = "#f29f68"  # lighter jupyter

  # Background image.
  #image = "logo.png"  # Name of image in `static/img/`.
  # image_darken = 0.6  # Darken the image? Range 0-1 where 0 is transparent and 1 is opaque.
  # image_size = "contain"
  # image_position = "right"  # Options include `left`, `center` (default), or `right`.
  # image_parallax = true  # Use a fun parallax-like fixed background effect? true/false

  # Text color (true=light or false=dark).
  text_color_light = true

# Call to action links (optional).
#   Display link(s) by specifying a URL and label below. Icon is optional for `[cta]`.
#   Remove a link/note by deleting a cta/note block.
[cta]
  url = "#contact"
  label = "Contact"
  icon_pack = "fas"
  icon = "envelope"

# Note. An optional note to show underneath the links.
[cta_note]
  label = '2i2c provides open-source infrastructure for interactive computing at institutions of research and education.'
+++

infrastructure for interactive computing in science and education.
