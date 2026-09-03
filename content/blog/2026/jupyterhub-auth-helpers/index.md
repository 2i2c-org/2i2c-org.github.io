---
title: Building an authentication helper library for JupyterHub
slug: "buliding-jhub-authz"
date: "2026-08-26"
author: Angus Hollands
categories:
  - upstream-impact
tags:
  - upstream
  - open source
  - jupyterhub
  - auth
---

2i2c have been working with the [University of Toronto](../../../collaborators/utoronto/) to add support for Canvas as a supported identity provider for JupyterHub. Out of the box, JupyterHub implements support for _authenticating_ users (figuring out who there are) and _authorizing_ users (figuring out whether they are permitted to log into the hub) using an `Authenicator` interface. Via the separate `oauthenticator` package, JupyterHub has support for many kinds of OAuth2-based Identity Providers such as Google or GitHub, in addition to providing a _generic_ authenticator `GenericOAuthenticator` that can be used with any OAuth2 implementation.

{{< figure src="oauth-flow.png" caption="Diagram of an OAuth flow during the authentication process, taken from [the oauthenticator documentation](https://oauthenticator.readthedocs.io/en/latest/_images/JupyterHub-OAuth-external-flow.png).">}}

Our friends at UC Berkeley maintain the `CanvasOAuthenticator` project, which has performed authentication for thousands of students in-use for over the last seven years. This project provides an implementation of `GenericOAuthenticator`, which queries the Canvas REST API to determine user _identity_ (e.g. their email address), and their _authorization_ (e.g. the courses that the user is enrolled in). In the time since `CanvasOAuthenticator` was first written (with involvement from 2i2c members), the `GenericOAuthenticator` has seen significant improvements, such that it is now possible to implement Canvas authentication without maintaining an entirely separate `GenericOAuthenticator` subclass.

After recognizing that it is much easier to maintain a small set of OAuth2 rules (adaptors) for each Identity Provider (like Canvas) rather than full-blown authenticators, 2i2c built [`jupyterhub_oauthenticator_authz_helpers`](https://2i2c.org/jupyterhub-oauthenticator-authz-helpers/). This library maintains an implementation of a subset of UC Berkeley's `CanvasOAuthenticator` rules for mapping Canvas courses and groups onto JupyterHub groups. With this work, adding Canvas authentication requires only a few additional lines:

```python
from jupyterhub_oauthenticator_authz_helpers.canvas build_auth_urls

cfg = c.GenericOAuthenticator

canvas_url = "<CANVAS-URL>"

# Configure auths
cfg.authorize_url, cfg.token_url, cfg.userdata_url = build_auth_urls(canvas_url)

# Scopes that this token will need
cfg.scope = [*build_auth_urls.scopes]
```

Adding support for group population (from Canvas groups and courses) requires a little bit more config:

```python
from jupyterhub_oauthenticator_authz_helpers.canvas get_user_groups, get_course_groups, build_auth_urls

# ...

# Define a custom key for auth groups
cfg.auth_state_groups_key = "custom-groups"

# Define and inject auth state
async def auth_state_hook(authenticator, auth_state):
  if auth_state is None:
    return None

  access_token = auth_state["access_token"]
  auth_state[authenticator.auth_state_groups_key] = [
    # Populate groups from Canvas courses, using the scheme defined in get_course_groups
    *await get_course_groups(canvas_url, access_token, "course_code"),
    # Populate groups from Canvas groups, using the scheme defined in get_user_groups
    *await get_user_groups(canvas_url, access_token),
  ]
  return auth_state

cfg.modify_auth_state_hook = auth_state_hook

# Request additional scopes for the course / user group fetching
cfg.scope = [*build_auth_urls.scopes, *get_user_groups.scopes, *get_course_groups.scopes]
```

In this approach, authentication and authorization are _composed_ — each primitive that represents an operation that requires a set of permissions possesses a `.scopes` attribute that can be added to the requested token scopes, e.g. `get_course_groups` or `build_auth_urls`. Hub administrators that only wish to authorize users by course groups do not need to use `get_user_groups` or request its `.scopes`. In order to prove the generality of this approach, 2i2c have added a Mastodon implementation of these authentication and authorization primitives that restricts hub access to those users which are followed by a particular _authorizing user_.

In addition to building out this library, 2i2c hopes to foster collaboration with other users and maintainers to continue to upstream additional OAuth2 adaptors. As part of the funded initiative, 2i2c will spend time conducting gonvernance and community work upstream to establish a [jupyterhub-contrib](https://github.com/jupyterhub-contrib) organisation that provides stewardship and maintainance of this work, and future third-party projects.

## Acknowledgements

- Thanks to the [University of Toronto](../../../collaborators/utoronto/) for collaborating with us, and funding this work.
- Thanks to UC Berkeley for the prior work that inspired this project.
