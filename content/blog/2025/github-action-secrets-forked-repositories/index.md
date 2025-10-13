---
title: "TIL: GitHub Action secrets are only available from non-forked repositories"
date: "2025-10-08"
authors:
  - Chris Holdgraf
categories:
- upstream-impact
tags:
- learning
- how-to
- open-source
---

If you've worked with GitHub Actions in open source projects, you might encounter a hard-to-debug error where repository secrets are simply _empty_. That's probably because the PR is from a forked repository! Here's a little learning we had after losing a bunch of time figuring this out:

## Our PR from a fork was using empty strings for repository secrets

[`github-activity`](https://github.com/executablebooks/github-activity) is a tool we help maintain for [generating changelogs from a wider variety of contributions](https://github-activity.readthedocs.io/en/latest/#how-we-define-contributors-in-the-reports) than GitHub's defaults. We needed to set a secret to raise the API rate limits for the tool's tests. These tests pull data from repositories outside of the `github-activity` repository itself, which quickly hit GitHub's rate limits without authentication.

The problem seemed straightforward at first: we added the secret, but the workflow was acting as if the secret didn't exist at all. After updating the code to explicitly check for empty strings, we discovered the authentication token was actually _an empty string_, even though it had been set.

After some debugging, we uncovered the root cause: **the PR was opened from a fork of `github-activity`**. GitHub intentionally [makes secrets appear as empty strings when a PR originates from a forked repository](https://docs.github.com/en/actions/how-tos/write-workflows/choose-what-workflows-do/use-secrets). This is a security measure to prevent unauthorized access to sensitive credentials.

## A quick fix: re-open the PR from the base repository

The immediate fix was simple: re-open the PR from a branch in the base repository rather than from the fork. This worked perfectly, but it's not a sustainable solution for open source projects that rely on community contributions from forks.
We don't want to create a dynamic where maintainers have different PR workflows because they're operating on the base repository.

## How use secrets with forked repositories in a safe-ish way

If you need to make secrets available to PRs from forks, there are a few approaches we learned about, each with security trade-offs:

### The `pull_request_target` workflow

GitHub provides a [`pull_request_target` workflow](https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/enabling-features-for-your-repository/managing-github-actions-settings-for-a-repository#controlling-changes-from-forks-to-workflows-in-public-repositories) that can access secrets even when triggered by forked PRs. In this case, GitHub will **always run the test suite on `main`**, instead of any changes your PR introduces.

**Why this is dangerous**: malicious actors could add _code_ to a PR that exfiltrates your secrets (for example, Python code that prints `os.environ["MY_SECRET"]`).

As a result, **only use secrets that you're OK with being public**. In this case, we generated a read-only token with restricted permissions. However, this is still kinda risky so use at your own peril.

If your repository workflows _require_ a secret that _absolutely cannot be public_ (e.g., a publishing key for a package repository), try a method like the following:

### Using GitHub Environments for granular control

A safer approach is to use [GitHub Environments](https://docs.github.com/en/actions/how-tos/deploy/configure-and-manage-deployments/manage-environments), which let you restrict which secrets are available to specific jobs. This way, you can ensure that only non-critical secrets (like those needed for testing) are available to jobs that run on forked PRs, while keeping sensitive secrets (like PyPI publishing tokens) restricted to trusted contexts.

This is the approach we implemented in `github-activity`, and it provides a good balance between security and community contribution workflows. We created a separate environment for publishing to PyPI so that its secret is never available to the job that runs with `pull_request_target`.

## We hope this saves you time!

Hopefully this learning is useful to others who run into the same confusing behavior. We've added a few improvements to `github-activity` to more reliably check for empty strings to surface this kind of condition, but knowing the basic behavior of GitHub environments and forked PRs is even better.

## Learn more

- [GitHub documentation on controlling changes from forks to workflows](https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/enabling-features-for-your-repository/managing-github-actions-settings-for-a-repository#controlling-changes-from-forks-to-workflows-in-public-repositories)
- [GitHub Environments for deployment](https://docs.github.com/en/actions/how-tos/deploy/configure-and-manage-deployments/manage-environments)
