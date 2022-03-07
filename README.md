# 2i2c brochure

This is a brochure website for the International Interactive Computing Collaboration (2i2c).
It is built from the [academic hugo theme].

## Where the website is hosted

This website is **hosted** by GitHub Pages, and we use Netlify to display previews of the website from PRs.

## Build this website locally

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

## Blog post feed

Our blog post feed is at https://2i2c.org/posts/, and contains a feed of posts from 2i2c team members.

This feed contains both **internal** and **external** blog posts.
In general, when team members do work associated with other open source projects, we should write those posts in other spaces and cross-link them from the 2i2c blog.

### Make an internal blog post

The way to make a regular blog post is by following the standard Hugo documentation for internal blog posts. Check out [the WowChemy theme documentation](https://wowchemy.com/docs/content/blog-posts/) for one way to do this.

### Make an external blog post

To make an external blog post, follow these steps:

- Generate a blog post folder and include a markdown file similarly to how you'd generate an internal blog post.
- Add an `external_link` metadata parameter at the top of the file. The value of this parameter will be the external link the post should point to.
- All other metadata can be the same, and will be used to share the post author, published order, etc.

### Featured images in blog posts

Featured images are displayed to the right of each post in our post feed.
By default, you can add a featured image directly to the blog post's folder by adding an image called `featured*`. For example, `featured.jpg`, `featured-image.png`, etc.

If you'd like to re-use another image on the site, you can create a **symbolic link** from the post folder to the image you'd like to re-use. This helps us save space and load time.

### Social media preview images

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

## Add a job post

We have some custom Hugo templates created for posting new jobs and a summary of open jobs.

- The `content/jobs/` folder contains all content related to job postings and an overview of working at 2i2c.
- The `/jobs/_index.md` file is a "landing page" for our jobs (what is at 2i2c.org/jobs).
  - It contains a custom Hugo shortcode defined at `layouts/shortcodes/open_jobs.html` that will list all jobs in the `jobs/` folder that have `open: true` in the page metadata.
- Every other page in `/jobs/` is a job posting. The YAML metadata at the top contains several important pieces of information for the job, and is used to populate job posting cards.
  - Use previous job postings as a reference for the information that should be used.
  - To mark a job as "open", make sure to put `open: true` in the posting metadata.
  - There's also a special shortcode to display relevant job metadata for a posting. This is at `layouts/shortcodes/job_details.html`.

## This website's theme

We are using the latest version of the [Wowchemy theme](https://wowchemy.com/docs/) (used to be the "Academic Theme"). See its documentation for information about customization and usage.
