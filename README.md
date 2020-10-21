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

## Check the spelling of any pages

This repository is configured with [the pyspelling package](https://facelessuser.github.io/pyspelling/). It will analyze all of the markdown files in `content/` and tell you if there are any un-recognized words.

To use `pyspelling`, first install it:

```
pip install pyspelling
```

Then install the `aspell` package:

```
sudo apt-get install aspell
```

Finally, you can run `pyspelling` on the repository like so:

```
pyspelling
```

Note that pyspelling may find some errors that are simply un-recognized, but correct, words. For example, HTML elements. To make these errors pass, you can add them to the list of custom spelling words here:

`.custom-dictionary.txt`.

For more information, see [the `pyspelling` documentation](https://facelessuser.github.io/pyspelling/).


## This website's theme

We are using the latest version of the [Wowchemy theme](https://wowchemy.com/docs/) (used to be the "Academic Theme"). See its documentation for information about customization and usage.
