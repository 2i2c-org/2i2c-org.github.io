---
# Ensure this never gets built
_build:
  list: 'never'
  render: 'never'
---

Our goal is to make blogging as short and quick as we can, so we can blog often.
See [the template blog post](./_template-post/index.md) for an example template to use.

## How to write blog posts

Follow these steps:

- Copy the `content/blog/_template-post` folder into the appopriate year folder, and modify the folder name. 
- Modify `index.md` to fit your post. Do these things:
  - Generate post content using the linked posts in `_template-post/index.md` as inspiration.
  - The post should be short, to the point, and scannable. Use quick and accessible language, keep posts below 200 words.
  - If there are links in the issue, scan their content to learn more before you write the post.
- Make sure to add an acknowledgements section at the bottom. Do these things:
  - check the `/content/collaborators` folder to see if an entry exists for that collaborator, and link them if so.


### Example from Yuvi's doepy talk

Here's an example from a recent talk that Yuvi gave:

- Example GitHub issue: https://github.com/2i2c-org/2i2c-org.github.io/issues/470
- The blog post that followed: ../../content/blog/2025/doepy-yuvi/index.md

### Example incident report

Incident reports are a way to provide transparency about what happened and what we learned as we run infrastructure. We create incident reports at https://github.com/2i2c-org/incident-reports so blog post GitHub issues don't need to have any content other than a link to the report.

- Example incident report issue: https://github.com/2i2c-org/2i2c-org.github.io/issues/482
- The blog post that followed: ../../content/blog/2025/incident-ucmerced-throttling
## How to write our Hugo directives

Here are a few example Hugo directives for quick reference.

### Figures

An example figure directive:

{{< figure src="images/staging-hub-matrix.png" title="Our staging and support hub job matrix tells GitHub Actions to deploy staging and support upgrades that act as canaries and stop production deploys if they fail.">}}

### Videos

From YouTube:

{{< youtube YjonPLxDiwM >}}

Local Videos:

{{< video src="videos/jupyterhub-admin.mp4">}}

### Callouts and admonitions

An example admonition / callout:

{{% callout %}}

Here's some markdown in my callout!

{{% /callout %}}


## How to add a category and tags

Each post has one category and multiple tags. Categories describe the post's intent, and tags cover its main themes or topics. You add them to the frontmatter of posts like so:

```markdown
---
title: Post title
date: "2025-01-01"
categories:
- updates
tags:
- open source
- geoscience
---
```

## How to use categories and tags

We use **lowercase formatting** as well as **spaces instead of hyphens** for both tags and categories. For example, `open source`, not `open-source` and not `Open Source`.

### Common categories

We try to keep the number of categories small, and non-overlapping in their meaning. [Here's a list of all our categories](https://2i2c.org/categories/), but we try to keep it only to the ones below:

- `impact` - telling stories of impact that 2i2c has had, either via contributors to a domain / open source community, or via communities we've enabled with our service.
- `service` - updates about our service and work we've recently done for it.
- `organization` - updates about our organization that isn't directly related to our service

### Common tags

We have a lot of tags, so don't worry about creating a new one if you don't think your tag has been covered yet. [Here's a list of all our tags](https://2i2c.org/tags/).
