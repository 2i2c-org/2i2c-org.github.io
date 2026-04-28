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

To facilitate communities using JupyterHub for a workshop, we introduced the idea of a 'shared password' based authentication a few years ago.
This lets communities set a single *global* password that is handed out to all workshop attendees (instead of collecting email addresses or GitHub usernames *before* the workshop starts).
Users can login with their email and this shared global password, and get going immediately. We worked with [OpenScapes](../../../collaborators/openscapes/) (which runs a lot of workshops) in developing this method, and it's been heavily used since among other communities!

However, until now this method required us to _restrict admin access_ for all users, preventing users from using admin features like group management, accessing the JupyterHub Admin dashboard (which lets you see which other users are logged in), and using the [shared directory](https://docs.2i2c.org/user/data/filesystem/#the-shared-directory).

To mitigate these, we [contributed the SharedPasswordAuthenticator](https://github.com/jupyterhub/jupyterhub/pull/5037) upstream to the JupyterHub organization, allowing hub admins to set set *two* passwords instead of *one*.
Hub admins can now **generate a special password that can be distributed just to admins**, and that gives users these extra capabilities without giving up the simplicity of using a single password for all workshop participants!

By contributing this upstream, we made sure this feature is available for everyone to use, rather than just for communities served by 2i2c.
We're [rolling this](https://github.com/2i2c-org/infrastructure/issues/7864) out to our communities now, and many communities have already benefitted from this!

## Acknowledgements

- To [MinRK](https://github.com/minrk) for code review and merge of the pull requests!
- The [OpenScapes](../../../collaborators/openscapes/) community for collaborating with us on building features that benefit themselves and everyone else!
- Support from our [member communities](../../../members/) gives us the capacity to invest in upstream open source engagement and build relationships like this
