# Blog

Our blog is our primary mehcanism for recording what we do and the impact we've had. It also gives us a record of our work that we can quickly use for generating reports.

## Principles to follow

- **Blog about anything that leans into [our value proposition](https://compass.2i2c.org/organization/value-proposition/)**.
- **Shorter, imperfect, and more frequent**.
- **Communicate any time we learn something**.
- **Share attribution with collaborators**.
- **Write for [our target audience](https://compass.2i2c.org/marketing/strategy/#our-audience)**.

See the **Tags and categories** section below for inspiration about what to blog about.

## How to create a new blog post

Copy the blog post folder template at the path below:

```
content/blog/_templates/[post-type]/index.md
```

It contains an `index.md` file that you can modify. Put it in the folder for the year in which you're posting (e.g.: `content/blog/mypostfolder`).

## Tags and categories: how to choose

**One category per post** + **2-5 tags**

### Categories

_Categories are non-overlapping, every post must have one category._

#### `service-enhancements`

Hub improvements and infrastructure that benefits members

- New hub features
- Infrastructure upgrades
- Technical migrations
- Performance improvements

#### `community-impact`

Work from our collaborators and member communities that we've enabled.

- Community success stories
- Hackweeks and events
- Announcements and offers from collaborators

#### `upstream-impact`

Strengthening the open source ecosystem

- Open source contributions
- Ecosystem health

#### `organization`
2i2c strategy, team, and operations

- Strategic updates
- Team changes
- Governance updates

### Tags

_Tags are more fluid, you can add as many to a post as you like._

#### Format

- `update` - General updates and progress
- `how-to` - Explaining how to do something
- `incident-report` - Reporting on an incident report
- `announcement` - Announcing something new, a date, etc
- `report` - reporting on something that happened
- `brainstorm` - sharing unfinalized thoughts and proposals
- `incident` - when sharing an incident report
- `hiring` - for job posts

#### Themes
- `leadership` - about organizational or project-wide leadership and strategy
- `community` - about people and social systems
- `learning` - about teaching workflows or something we've learned
- `devops` - about orchestration and team process for cloud infrastructure
- `sustainability` - about funding or capacity building
- `reliability` - about infrastructure reliability
- `monitoring` - about visibility and monitoring of cloud infrastructure
- `cloud-costs` - about cloud costs
- `communication` - about communicating ideas
- `reproducibility` - about enabling reproducible computation
- `computation` - about enabling computation and scaling
- `data` - about reading and using data in the cloud
- `sovereignty` - about giving communities control and enabling Right to Replicate
- `open-source` - anything that involves upstream tools or contributions (use heavily!)

#### Technologies
- `jupyter` (for project-wide information)
- `jupyterhub` (prefer these for project-specific information)
- `jupyterbook`
- `binder`

#### Domains
- `earth-science` - (here are common ones, add new domain tags as you wish)
- `biology`

## How to write blog posts

Follow these steps:

- **Find a GitHub issue**. An issue should describe the most important points to convey in a post. Read it, and any linked material inside, to learn what it's about.
- **Choose a template**. Copy one of the `content/blog/_templates/[posttype]/` folders into the appopriate year folder, and modify the folder name. 
- **Read the template guidance**. Each template file has suggestions for its structure, as well as links to example posts - reda those posts to understand what we're going for.
- **Generate a post draft**. The post should be short, to the point, and scannable. Use quick and accessible language, keep posts around 100-300 words.
- **Add collaborator links**. Scan the post for mention of collaborating people and organizations - check the `/content/collaborators` folder to see if an entry exists for any you notice. If so, add a link to that folder entry.


### How to add a category and tags

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

We use **lowercase formatting** as well as **spaces instead of hyphens** for both tags and categories. For example, `open source`, not `open-source` and not `Open Source`.

## Hugo directives you can use in our blog

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

### Pull quotes

An example pull quote

{{% pull-quote cite="Author name"%}}
Here's a pull quote.
{{% /pull-quote %}}