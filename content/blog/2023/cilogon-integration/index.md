---
title: "CILogon usage at 2i2c"
subtitle: ""
summary: "The following is a summary of how CILogon is used at 2i2c, how the integration works and a celebration of the partnership."
authors: ["Georgiana Dolocan"]
tags: []
categories: [engineering, partnerships]
date: "2023-02-24"
featured: false
draft: false
---

## About CILogon

[CILogon](https://www.cilogon.org) is an open source service provider that allows users to log in against over 4000 various identity providers, including campus identity providers. The available identity providers are members of [InCommon](https://incommon.org/federation/), a federation of universities and other organizations that provide single sign-on access to various resources.

## CILogon and 2i2c

For the past year, 2i2c has been successfully using CILogon for more than fifteen of the hubs it manages.

Currently, most of the hubs that use it are hubs for communities in education that want to manage their hub access through their own institutional providers.

With using a tool like CILogon, we allow hub access to be managed both through the communities' institutional providers, but also through social providers like GitHub and Google. Because both authentication mechanisms can coexist, there's no need to provide specific credentials for 2i2c staff in order to have access to the hub. This reduces both the burden on institution's IT departments, but also the complexity of a hub deployment.

Moreover, as we migrate away from our current Auth0 setup, the number of hubs using CILogon will further increase in the following year.

## The setup

The setup that 2i2c uses, is based on two important tools, the CILogon administrative client and the JupyterHub CILogonOAuthenticator.

### The CILogon administrative client

The [2i2c administrative client](https://cilogon.github.io/oa4mp/server/manuals/dynamic-client-registration.html) provided by CILogon allowed us to automatically manage the CILogon OAuth applications needed for authenticating into the hub.

For each hub that uses CILogon, we dynamically create an OAuth [client application](https://cilogon.github.io/oa4mp/server/manuals/dynamic-client-registration.html) in CILogon and store the credentials safely, using the script at [cilogon_app.py](https://github.com/2i2c-org/infrastructure/blob/3312f373f0aa59fbc98dc1c8161aa9623b68726b/deployer/cilogon_app.py). The script can also used for `updating` the callback URLs of an existing OAuth application, `deleting` a CILogon OAuth application when a hub is removed or changes authentication methods, `getting` details about an existing OAuth application, `getting all` existing 2i2c CILogon OAuth applications.

### The JupyterHub CILogonOAuthenticator

For CILogon's integration with JupyterHub's authentication workflow, we're using the [**CILogonOAuthenticator**](https://github.com/jupyterhub/oauthenticator/blob/main/oauthenticator/cilogon.py), which is part of the [JupyterHub OAuthenticator project](https://oauthenticator.readthedocs.io/en/latest/). This is what allows JupyterHub to use common OAuth providers for authentication, and it's also a base for writing other Authenticators with any OAuth 2.0 provider.

As part of this 2i2c integration with the JupyterHub CILogonOAuthenticator some important upstream fixes and enhancements to the [`oauthenticator`](https://github.com/jupyterhub/oauthenticator) were identified and performed. For example, the [GHSA-r7v4-jwx9-wx43](https://github.com/jupyterhub/oauthenticator/security/advisories/GHSA-r7v4-jwx9-wx43) vulnerability was reported and fixed, and a [migration guide](https://oauthenticator.readthedocs.io/en/latest/how-to/migrations/upgrade-to-15.html) containing a description of the breaking changes that were made, together with a step by step guide for the users on how to update their usage of JupyterHub CILogonOAuthenticator was provided.

Read more about how CILogon is setup for use at 2i2c from [the docs](https://infrastructure.2i2c.org/hub-deployment-guide/configure-auth/cilogon.html). 


## Celebration

Thanks to the 2i2c - CILogon partnership, during this past year we were able to integrate CILogon into 2i2c's infrastructure and to observe its importance, usefulness and great support for 2i2c and the communities we server.

We are now happy to announce that the 2i2c - CILogon partnership has been expanded to another year!

**Acknowledgements**: The upstream [`jupyterhub-oauthenticator`](https://oauthenticator.readthedocs.io/en/latest) project mentioned in this post as being used at 2i2c is a JupyterHub package, kindly developed and maintained by the [JupyterHub community](https://discourse.jupyter.org/c/jupyterhub/) and the 2i2c integration described was developed by [the 2i2c engineering team](/organization/team.md). Also, this post was edited by [Jim Basney](https://jbasney.net/).
