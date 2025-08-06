# 2i2c brochure

This is a brochure website for the International Interactive Computing Collaboration (2i2c).
It is built from the [academic hugo theme](https://github.com/HugoBlox).

## Where the website is hosted

This website is **hosted** by GitHub Pages, and we use Netlify to display previews of the website from PRs.

## How to edit, build, and preview this website

See [the Team Compass blog documentation](https://compass.2i2c.org/communication/blog/) for more information.

## Website-specific features

### Automatic GitHub link shortening

This theme will automatically shorten GitHub links and add a little GitHub icon to the front. For example, see the [Jack Eddy Symposium blog post](https://2i2c.org/blog/2022/eddy-symposium-report/).

### How to add an external blog post

We can link to blog posts that were written by the 2i2c team but published in other locations. These show up in our blog roll but are just pointers to other websites.

To add an external blog post to our blog, create a blog post with an `external_link:` metadata field like, and a body that _summarizes_ the post. For example:

```
---
title: "An external post title"
date: 2025-03-03
external_link: https://your-post-url.org
tags:
  - upstream
  - open source
categories:
  - impact
---

This content will be displayed as a summary of the post in the blog landing page.
```

Note that all other metadata fields are the same as any other blog post.
See [this blog post as an example](content/blog/2025/binder-buildkit/index.md).

### Broken link checking

We have [a GitHub workflow to check for broken links](.github/workflows/linkcheck.yml).
This runs each week and will open an issue if it finds any broken links.

### Force a website re-build

To force a website re-build, [trigger a `workflow dispatch` here](https://github.com/2i2c-org/2i2c-org.github.io/actions/workflows/linkcheck.yml).


### Social media preview images

For text-based pages, we generate social media previews by automatically adding page title text to an image template.
The template is defined [in this Figma board](https://www.figma.com/file/EYFRCag2gfYGdEZGFrXgzv/2i2c-Logos?node-id=1101%3A2&t=KjO3JB6Jx4dRnGfa-0) and we use Hugo image filters to add text to it.
See [the hugo partial template we use](layouts/partials/ogimage.html) for details and links.

The Featured Image will also be used to generate previews in social media.
You can generate an image designed specifically for social media (similar to GitHub social media link previes).
To do so, follow these steps:

1. Go to [this Figma project for a template](https://www.figma.com/file/EYFRCag2gfYGdEZGFrXgzv/2i2c-Logos?node-id=117%3A67).
2. Find the "Twitter Summary Community Update" frame.
3. Update the text to match the title of what you'd like to post.
4. Export the frame to PNG (at `1x` size).
5. Place the PNG in the same folder as the relevant website page.
6. Rename the image so that it is "featured" for that page (see above)
7. Prevent the image from showing up on the page by adding the following to that page's YAML metadata:

   ```yaml
   image:
     preview_only: true
   ```

The image will now be used to generate a social media preview!

### Check the spelling of any pages

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

## Add a job post

We have some custom Hugo templates created for posting new jobs and a summary of open jobs.

- The `content/jobs/` folder contains all content related to job postings and an overview of working at 2i2c.
- The `/jobs/_index.md` file is a "landing page" for our jobs (what is at 2i2c.org/jobs).
  - It contains a custom Hugo shortcode defined at `layouts/shortcodes/open_jobs.html` that will list all jobs in the `jobs/` folder that have `open: true` in the page metadata.
- Every other page in `/jobs/` is a job posting. The YAML metadata at the top contains several important pieces of information for the job, and is used to populate job posting cards.
  - Use previous job postings as a reference for the information that should be used.
  - To mark a job as "open", make sure to put `open: true` in the posting metadata.
  - There's also a special shortcode to display relevant job metadata for a posting. This is at `layouts/shortcodes/job_details.html`.

## Install pre-commit hooks

This repository uses [pre-commit hooks](https://pre-commit.com/) to run a few processes any time a commit is made. To initialize pre-commit, run the following:

```shell
pip install pre-commit
```

Initialize pre-commit locally with the following:

```shell
pre-commit install
```

The next time you make a commit, pre-commit will run if necessary.

## This website's theme

We are using the latest version of the [Hugo Blox theme](https://hugoblox.com/docs/) (used to be the "Wowchemy Academic Theme"). See its documentation for information about customization and usage.
