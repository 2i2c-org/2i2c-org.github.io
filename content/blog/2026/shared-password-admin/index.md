---
title: Supporting JupyterHub admins on workshop hubs with shared passwords
slug: "shared-password-admin"
date: 2026-04-27
categories:
  - upstream impact
tags:
  - open source
  - jupyterhub
---

As part of making it easier for our communities to run workshops, we introduced the idea of a 'shared password' based authentication a few years ago. The idea is that instead of collecting email addresses or GitHub usernames *before* a time bound workshop to give them access to a JupyterHub, we instead set a simple *global* password that is handed out to all workshop attendees. They can login with their email and this shared global password, and get going immediately. We worked with [OpenScapes](../../../collaborators/openscapes/) (which runs a lot of workshops) in developing this method, and it's been heavily used since among other communities!

However, since the user can use any username, this meant you aren't able to use a few other features of JupyterHub - particularly, group management and admin access. In particular, the lack of admin access meant no access to the JupyterHub dashboard (which lets you see which other users are logged in), and no ability to use the [shared](https://docs.2i2c.org/user/data/filesystem/#the-shared-directory) directory (since only admins can write to this).

To mitigate these, we contributed the [SharedPasswordAuthenticator](https://github.com/jupyterhub/jupyterhub/pull/5037) upstream to
JupyterHub, allowing setting *two* passwords instead of *one*. A special, longer password that can be distributed just to admins
allows for admin users to exist in JupyterHub without giving up the simplicity of being able to hand out a simpler password to all your
workshop participants! By contributing this upstream, we made sure this feature is available for everyone to use, rather than just for
communities served by 2i2c.

We're [rolling this](https://github.com/2i2c-org/infrastructure/issues/7864) out to our communities now, and many communities have already benefitted from this!

## Acknowledgements

- To [MinRK](https://github.com/minrk) for code review and merge of the pull requests!
- The [OpenScapes](../../../collaborators/openscapes/) community for collaborating with us on building features that benefit themselves and everyone else!
- Support from our [member communities](../../../members/) gives us the capacity to invest in upstream open source engagement and build relationships like this
