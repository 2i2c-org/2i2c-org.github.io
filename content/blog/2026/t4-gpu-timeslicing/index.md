---
title: Serving more users with fewer cheap GPUs for workshops and education
slug: "more-users-fewer-gpus"
date: 2026-05-12
categories:
  - education
tags:
  - open source
  - gpu
---

Eric Van Dusen was running [a workshop](https://events.internet2.edu/website/89730/tutorials/) titled "Teaching in the AI Classroom: Expanding Access to Interactive Computing through JupyterHub and CloudBank" at the National Artificial Intelligence Research Resource (NAIRR) Annual Meeting, showing how JupyterHub can be used to seamlessly provide access to GPU computation for teaching.

2i2c runs roughly 70 JupyterHubs with Eric and Sean Morris for [Cloudbank Classroom](https://operations.access-ci.org/node/907), and to support running this workshop we [added the first GPU enabled hub](https://github.com/2i2c-org/infrastructure/issues/7758) to this fleet!

## Serving more users with fewer GPUs

2i2c already supported running hubs with GPU on Google Cloud, so setting up the hub was trivial.
Since we didn't need very powerful GPUs, and wanted to keep costs down, we were using the cheapest GPUs available - [NVIDIA T4](https://www.nvidia.com/en-us/data-center/tesla-t4/).
However, when we tested to see if we could support ~50 users, we discovered that Google Cloud didn't have that many GPUs to give us consistently!
We could consistently get upto 25 at a time, but never once more than 30 before Google Cloud reported it was out of GPUs.

To successfully run this workshop, we had to put multiple users on the same GPU, in a way that still supported the *content* to be taught.
A nice side effect would be that we can serve more users for cheaper!

NVIDIA supports three ways to ['share' 1 GPU](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/timesharing-gpus#choose-gpu-sharing) across multiple users: [Time Slicing](https://docs.nvidia.com/datacenter/cloud-native/gpu-operator/latest/gpu-sharing.html), [Multi-instance GPU (MIG)](https://docs.nvidia.com/datacenter/cloud-native/gpu-operator/latest/gpu-operator-mig.html) and [Multi-Process Service (MPS)](https://docs.nvidia.com/deploy/mps/index.html). We had to pick what strategy to use for our particular use case, and spent a bunch of time researching them.

1. **MIG**: Offered the best end user experience, as it provides hardware level *fault isolation* - one user's mistakes won't be noticed by another user at all. However, it is only available on more expensive GPUs, so we could not use it.
2. **MPS**: Offered decent fault isolation (through software, rather than hardware), supported the GPU we wanted to use, and seemed ideal. However, it has security implications that we did not have time to properly evaluate - it required that we grant all users direct access to the host's IPC interface, and that is a security risk we weren't willing to take at that moment.
3. **Time Slicing**: This provided *no* fault isolation - one user can crash another user's process (like Windows 98!).
   However, it supported the GPU we cared about, had security boundaries we were ok with, and could be implemented very quickly.

So we settled on **using Time Slicing** for this particular workshop. Since there is no fault isolation, we needed to measure the actual GPU usage of our content to determine how many users we can reasonably put on one GPU without one user constantly 'hogging' all the GPU resources.

## Measuring GPU utilization

Google Cloud offers [built in metrics](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/timesharing-gpus#monitor) for measuring GPU utilization. They're coarse, operating at the node level rather than the user level.
But it was good enough for us to run multiple copies of the workshop content at the same time, and determine how much GPU was being used.
Sean Morris did a lot of this testing, and determined that 2 concurrent users max out 1 GPU without any negative effects on their perceived performance.

![Graph of GPU utilization (0-1.0) when we were testing our workshop material](./gpu-utilization-testing.png)

This testing allowed us to be confident that the workshop itself would go well, and users won't suffer too much from the lack of fault isolation.
If you're planning on using Time Slicing, this kind of measurement is *critical* to ensure that your users have an acceptable experience - otherwise everything may look *fine* when it's just one person testing, but fall apart when multiple users use it.

## The workshop experience

The workshop itself went without any issues, thanks to the preparation and planning described above.
In practice, we found that people's GPU utilization was even less than we had tested, so we could potentially put even more users on fewer GPUs for this kind of workshop.
However that requires us to better understand the failure condition, to see what happens when users interfere with each other's memory usage.
An exercise for another day.

![Graph of GPU utilization (0-1.0) during the workshop itself](./gpu-utilization-workshop.png)

We were able to serve everyone who signed up, without running into resource exhaustion on Google Cloud.
Overall, a big win for us and those who attended the workshop!
We also estimated that the entire workshop cost roughly ~200$, which is very affordable for what we were doing.

## Available for all 2i2c communities running on Google Cloud

We [documented this whole process](https://infrastructure.2i2c.org/howto/features/gpu/#gpu-time-sharing) as we went along, and now GPUs shared with Time Slicing is available for all 2i2c community hubs running on Google Cloud!
If your community is running on AWS and would like this feature, please [let us know](https://docs.2i2c.org/support/).

## Acknowledgements

- To Eric van Dusen, for setting up and running this workshop. Pedagogy is the hardest part of teaching, and we are grateful to work with Eric!
- To Sean Morris, for collaborating with us in a pretty deep way to make this possible.
- To April Johnson for building out our community strategy and putting it in practice over the last 6 months, enabling us to spot opportunities like this and serve our community well
- To Kirstie Whitaker (from [BIDS](../../../collaborators/bids/)), for putting together a social event that encouraged ad-hoc information exchange (our tech lead, Yuvi, was able to spend high bandwidth synchronous time with Eric at that event) that allowed us to serve [Cloudbank Classroom](../../../collaborators/cloudbank/) better
