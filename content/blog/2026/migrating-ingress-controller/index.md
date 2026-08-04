---
title: Migrating from one ingress controller to another
slug: "migrating-ingress-controllers  "
date: 2026-07-31
categories:
    - service enhancements
tags:
  - reliability
  - devops
  - open source
---

# What we learned

Migrating from one ingress controller to another is not a trivial task!

# Context

The news that the best-effort maintenance of the Ingress NGINX Controller would end in [the first quarter of 2026](https://www.kubernetes.dev/blog/2025/11/12/ingress-nginx-retirement/) sparked a considerable amount of [discussion](https://github.com/2i2c-org/infrastructure/issues/7106) among the community about what the best replacement for this controller is.

Because "what the best replacement is" depends on the specifics and maturity levels of the infrastructure stack, for the near future, 2i2c has decided to migrate to the [official NGINX Ingress Controller](https://docs.nginx.com/nginx-ingress-controller/install/helm/open-source/). However, this choice will have to be challenged in the future, because the Kubernetes Ingress API itself was frozen when the INGRESS NGINX Controller was sunset, with the Kubernetes project [recommending the Gateway API instead](https://kubernetes.io/docs/concepts/services-networking/ingress-controllers/). So, we may need/want to migrate to the Gateway API down the road.

# Migration

Our [migration plan](https://infrastructure.2i2c.org/howto/migrate-ingress/) has all the technical details about the steps we took towards the actual controller migration, so this blog post will not go into those aspects. Instead, it will describe the approach we took to achieve the least amount of downtime for our communities, as well as list the challenges that we couldn't anticipate during the planning phase.

## Least amount of downtime

In our initial setup, we were using the `LoadBalancer` service provided by the ingress controller. This meant that migrating from one controller to another, meant updating _all_ DNS records to point to the new controller's LB. During this time, the cluster infrastructure would have been unavailable to users.

So, in order to minimize the downtime, we have introduced a new `LoadBalancer` ingress service, independent of the ingress controller. This service provides a static external IP address _(the entrypoint into each cluster)_ that points to the ingress controller `ClusterIP` service. This allows us to simply point this LB at a new service pod whenever we need to switch to the new controller/gateway.

## Challenges

The [tracking issue](https://github.com/2i2c-org/infrastructure/issues/7743) on our infrastructure repo tracks almost all the tasks (both expected and unexpected) related to the migration. But here is a summary of the ones that took us by surprise:

1. On one hub, the reverse proxy was unable to communicate with `binderhub-service`. This resulted in 502 errors. This also pointed us to identify a websocket failure between the frontend and the user server due to missing ingress annotations. The problem and solution are described in the [incident report](
https://github.com/2i2c-org/incident-reports/blob/main/reports/2026-03-09-BinderHub-URL-responds-Bad-GatewayforProjectPythia.pdf).

2. Manually updating all DNS records is, of course, error-prone. So, we ended up missing one. The full [incident report](https://github.com/2i2c-org/incident-reports/blob/main/reports/2026-03-12-LIS-hub-unreachable-after-ingress-migration.pdf) is available to be checked-out.

3. The F5 NGINX Ingress controller came with an unexpected behaviour. When certificates needed to be renewed, it was trying to create (new) temporary ingress objects. This caused issues with multiple ingresses sharing the same host. So, we had to update all ingress objects needing TLS, to allow `cert-manager` to mutate the ingress via `edit-in-place`. More about it in this [incident report](https://github.com/2i2c-org/incident-reports/blob/main/reports/2026-03-31-unable-to-provision-new-tls-certs.pdf).

4. Renewing certificates was still failing
  - Even though ingress objects were updated to allow `cert-manager` to `edit-in-place`, this did not trigger the update of the certificate itself, which meant that `nginx-ingress` still tried to create temporary ingresses. Manually reconciling the Certificate resource with the Ingress fixed this. More in the [incident report](https://github.com/2i2c-org/incident-reports/blob/main/reports/2026-04-15-TLS%20certificates%20expired%20for%20two%202i2c%20hubs.pdf) and this [discussion](https://github.com/2i2c-org/infrastructure/issues/8063).
  - Our Prometheus instances were being authenticated at the ingress controller level. This made the ACME challenge resolution during renewal encounter `HTTP 401` responses. So we had to move the authentication from the ingress controller level to the Prometheus service itself. Although a beneficial change, this generated more work and more integrations to fix https://github.com/2i2c-org/infrastructure/issues/8123.

## Acknowledgements

- To [MinRK](https://github.com/minrk) for adding this feature to Dask-Gateway and [Yuvi](../../../authors/yuvi-panda/) for brainstorming the best migration approach
- To [Angus](../../../authors/angus-hollands/) for helping with the migration and troubleshooting the issues