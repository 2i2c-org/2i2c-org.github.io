---
title: A few things I learned at the Responsible GenAI for NASA Earth Data Workshop
slug: "respnosible-genai-workshop"
date: 2026-09-01
tags:
  - open-source
  - community
  - jupyter
categories:
  - community-impact
featured: false
draft: false
---

I recently got back from the [2026 Responsible GenAI for NASA EarthData workshop](https://responsible-genai.hackweek.io/) in Seattle.
It was an opportunity for members across the NASA ecosystem to share their experiences experimenting and learning with Generative AI models around Earth Data.
This ranged everywhere from personal workflows to large-scale automations with non-trivial amounts of data.
I'd say it was a way to share "best practices", but I also realize that **there's no such thing as best-practices for LLMs yet**.
Everyone is still in the experimenting and seeing what happens phase, in all directions.
So I'll just say that we shared "practices" - who knows if they're the best yet :-).

This is a quick report out for what we I noticed and some things that stood out to me while I was there.

## We can make MyST documentation more useful for LLMs without any extra effort

First off, we got to do some fun hacking and experimenting while we were there.
Here's the main new thing that came out of this:

**[MySTifAI](https://responsible-genai-hackweek.github.io/MySTifAI/)** attempts to make MyST websites more useful for LLMs to parse and use as part of Retrieval-Augmented Generation workflows.

Many LLMs (especially smaller models) benefit from having real-time information loaded into their context to guide the kinds of responses they give. This is particularly useful if you need the latest, specific information from a community resources, like a documentation site. Many NASA communities use [MyST](https://mystmd.org), and this is a little experiment at using MyST's modular and machine-readable nature to turn it into a RAG-like resource for LLMs.

The [`docslice` tool](https://responsible-genai-hackweek.github.io/MySTifAI/docslice) is a CLI that indexes and searches content in a MyST site, and returns little chunks as markdown for the model to read. Check out the [evaluations page](https://responsible-genai-hackweek.github.io/MySTifAI/evaluation) where we ran it with a few different model sizes to see how it did. In short: the smaller the model, the more context you save by using a RAG-like helper like `docslice`.

## Scientists find "skills" to be a useful way to standardize LLM workflows

A lot of discussion revolved around how to use, find, and write "skill files" for LLMs that work with Earth Data.
These are little files that live in a folder like `.claude/skills/[skillname]/SKILL.md`, and they can be dynamically loaded by an LLM to learn how to do a particular thing at the moment it must be done.

The EarthData community is interested in this because there are often particular ways that datasets should be discovered, retrieved, and used.
Asking an LLM to figure that out on its own each time is noisy and costly, and skills are a way to standardize the experience across NASA scientists.

We explored a few different ways to distribute skills, because I think NASA's ecosystem is interested in co-maintaining and sharing as much as possible.
Right now it seems like the [agentskills.io](https://agentskills.io) specification and the [skills.sh](https://skills.sh) tooling are the simplest ways to distribute and use skills. However, I also learned that [you can distribute skills as pixi packages via conda-forge](https://pavel.pink/blog/pixi-skills/) and maybe even via `pypi`.

## Non-frontier models are an important design target for software and workflows

Many developers are building with the assumption that the latest and best models are available to the kinds of users they mean to serve.
A number of conversations challenged this idea, for example:

- The fanciest models are already fairly expensive for many individuals.
- The fanciest models might a lot more expensive in the future, because they are heavily subsidized.

For this reason, **it's important to buid technology that's still useful with sub-frontier model capabilities**.
For example, tools like [MySTifAI](https://responsible-genai-hackweek.github.io/MySTifAI/) (above) probably aren't necessary if you're using the latest Fable model that was trained recently.
But they're much more valuable in saving context and reducing noise for anything less sophisticated.

I suspect that, over time, there will be a bifurcation of who has access to the most cutting-edge models.
My fear is that access to models will become similar to access to scientific publications: if you happen to be at an institution with enough money to pay for a license, you're OK, but the rest of the world will be left behind.

I think we can cut against this outcome by building technology that provides value with model capabilities that are _likely to remain accessible_ in the future.

That said...

## Nobody knows what model capabilities will exist in the near future

The cone of "what's possible" for model capabilities is huge!
Nobody really knows where this field is heading.
For example, I've seen everything from:

> Fable-level capabilities will become a fraction of the cost in the future, and runaway model improvement will essentially create an infinitely better and more accessible LLM capability.

to

> Non-trivial models are going to become extremely expensive, with key features gate-kept behind enterprise plans and API costs, in order to justify the extreme costs of model training and inference.

to

> This entire ecosystem is going to collapse under its own weight because it has no financial model whatsoever.

I think all of these outcomes seem plausible! It feels like a good way to hedge against any one of them is to build technology that assumes we'll land somewhere in between.
For example, maybe it's safe to assume that today's "Haiku"-level capabilities will be massively accessible for the forseeable future. Can we build the right "skills", APIs, MCPs, etc to ensure they'll still be useful?

_To complexify this a bit: Something else I didn't consider, but seems painfully obvious in retrospect, is that many "open weights" models come from countries that the current US administration considers to be hostile to US interests. This means that for federal-adjacent communities like NASA, many open weights models simply are not an option._

## Setting up an LLM-style environment in the cloud is non-trivial!

We did some last-second environment building with [Tasha](https://github.com/tsnow03) to provide a cloud environment where users could experiment with LLMs for their hackweek projects.
This had a bunch of rough edges!
Here are a few that stood out to me:

- **Workshop administrators need clear documentation for how to connect with common inference servers and get their credentials onto the hub safely**. We had to generate credentials to run LLM inference against the [NRP inference service](https://nrp.ai/documentation/userdocs/ai/llm-managed/) via [OpenRouter](https://openrouter.ai/). It wasn't super clear how to do this, and how to insert these credentials into the hub environment properly. In some cases I'm pretty sure we inserted credentials in a way that wasn't "safe" because they were baked into the environment image, and thus available to all of the users.
- **Workshop adminsitrators need a cleaner story for how to share LLM credits across participants**. We had to use a semi-bespoke Python script to connect people's Claude accounts with the allotment of credits that the workshop provided. This felt a little bit janky, but it still worked pretty well!
- **People need guidance for generating hub configuration with LLMs.** Some of the hub configuration for this workshop was itself generated with LLMs. As a result, there was some complex stuff (see above re: credentials) that we probably could have guarded against with more guidance that an LLM could discover (either a "skill" file, or documentation about how to do this).
- **JupyterAI is relatively new and unknown to folks that would otherwise benefit from it**. We had a nice presentation from [David Qiu](https://github.com/dlqqq) who works on [Jupyter AI](https://github.com/jupyterlab/jupyter-ai). He showed off some nice capabilities leveraging arbitrary models as part of a notebook / data science workflow. Folks seemed to like it, but many had never heard about it! We could do more to surface the existence of this tool, and basic ways to integrate its workflows into the hub (especially if you've got access to managed inference servers like we had on the [NRP](https://nationalresearchplatform.org/).)
- **There's not an obvious way to programmatically trigger LLM inference on a hub**. We also realized that sometimes you want a *non-interactive* way to trigger LLM inference. For example, if you want to run an evaluation suite against your code or data and need to programmatically generate an inference query with a script. There are a few model-agnostic tools for doing this - I'm interested in learning more about Simon Willison's [LLM CLI](https://llm.datasette.io/). I think some basic guidance for hub administrators would help us solve these problems more effectively.

## It's important to have a safe space for honest conversation and respectful criticism

This is one of the first LLM events that felt like there was psychological and emotional space for both optimism and pessimism.
A recurring topic that came up was how many folks felt like conversations about LLMs created a feeling of _shame_ in themselves or in the others they spoke with.

Shame is a really powerful human emotion, and tends to have a strong dampening effect on whatever action it's connected with.
Many folks privately reported that they felt unable to talk about LLM use (for bad or for good) _at all_, because they were afraid of how the conversation would play out.

I need to reflect on this observation more, but it occurs to me that the most important thing to preserve through all of this is the sense of human connection that we've got, and the communities of people that are trying to solve problems together.
LLMs bring out strong emotions in everybody, and we need to find a way to willingly engage in this topic _as a community of diverse perspectives_ or we'll self-sort into mini-groups that share the same biases and perspectives. This will make it harder to navigate the ethical and moral questions around LLMs, and will also make it harder to effectively integrate them (or not) with scientific workflows for the most impact.

## Thanks to the organizers

I'm grateful to [Tasha Snow](https://github.com/tsnow03) for encouraging me to join this event, and to the rest of the organizing team for making it happen.
The [CryoCloud community](../../../collaborators/cryocloud/) generously let us use their hub for hacking and experimenting.
I'm also grateful to [NASA ESDS](https://www.earthdata.nasa.gov/esds) for funding the event and bringing a diverse group of people together to learn.
Finally, I was appreciative of the attendees for coming to engage in a challenging topic that is nonetheless important to reason about and learn from.
I hope to have more interactions like this in the future!