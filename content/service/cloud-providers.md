+++
widget = "featurette"
headless = true  # This file represents a page section.
title = "Supported Cloud Providers"
weight = 90

[design]
  background.color = "white"
  spacing.padding = ["0", "0", "0", "0"]

# Showcase personal skills or business features.
# Add/remove as many `[[feature]]` blocks below as you like.
# For available icons, see: https://sourcethemes.com/academic/docs/widgets/#icons
[[feature]]
  icon = "google-cloud"
  icon_pack = "custom"
  name = "Google Cloud"
  description = ""

[[feature]]
  icon = "azure"
  icon_pack = "custom"
  name = "Microsoft Azure"
  description = ""

[[feature]]
  icon = "aws"
  icon_pack = "custom"
  name = "Amazon Web Services"
  description = ""
+++

2i2c aims to support JupyterHubs on any cloud provider that offers a managed Kubernetes service.
To start, we are focusing on the major commercial cloud providers listed below.
If you would like a hub hosted on a different cloud provider, please [give us your feedback](mailto:hello@2i2c.org).
See [our Managed Service Strategy and Goals](https://docs.2i2c.org/en/latest/about/strategy.html) to learn more about our plans.