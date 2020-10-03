# 2i2c brochure

This is a brochure website for the International Interactive Computing Collaboration (2i2c).
It is built from the [academic hugo theme].

## Building this website locally

* Install the Hugo extended version from [the latest releases page](https://github.com/gohugoio/hugo/releases)
  - Ensure that you have the *extended version*
* Clone this repository locally:

  ```
  git clone https://github.com/2i2c-org/2i2c-brochure
  cd 2i2c-brochure
  ```
* The content for this site lives in `content/`. Each folder inside is a **page**.
* These folders have a collection of markdown snippets that are stitched into a single page.
  - Their order is determined by the `weight:` metadata on each page.
* Preview the site locally with:

  ```
  hugo serve -D
  ```
* Push your changes to the repository and Netlify will automatically update the website.

## This website's theme

We are using the latest version of the [Wowchemy theme](https://wowchemy.com/docs/) (used to be the "Academic Theme"). See its documentation for information about customization and usage.
