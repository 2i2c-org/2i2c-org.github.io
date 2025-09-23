---
title: "Incident report: UC Merced user throttling during class startup"
date: "2025-09-16"
categories:
- incident-report
tags:
  - cloud
  - open-source
---

On August 29, 2025 our cloud infrastructure team experienced an incident with the UC Merced community hub when students tried to login simultaneously at the start of class. For more detailed technical information about this incident, see our [full incident report](https://github.com/2i2c-org/incident-reports/blob/main/reports/2025-08-29-ucmerced-too-many-users-throttled.pdf).

## What happened

- Students experienced issues when trying to login to the hub at the same time during the start of class.
- The concurrent spawn limit was reached quickly due to the large number of users starting up simultaneously.
- New nodes had to be brought up by the autoscaler, which took roughly 10 minutes from start to end.
- Users who tried again after 1 minute weren't guaranteed to get their servers started immediately since new nodes were still spinning up.
- This was an "expected" scale-up event but the lack of clear messaging caused users to interpret it as instability.

## What we learned

- We need better communication so users understand when infrastructure slowness is "expected" vs. "unstable".
- We need better alerting for concurrent user startup throttling - we found out about this issue from users rather than automated monitoring.
- We learned that JupyterHub's metrics don't properly expose `429 status` codes in our dashboards.
- This will happen again if we don't have proper scaling limits and node provisioning strategies for sudden user influxes.

## Resolution

We implemented several fixes:
- Increased the concurrent spawn limit from 64 to 100.
- Put UC Merced users on larger nodes to reduce the number of node spinups needed. this will cost more in cloud but result in fewer scale-up events.
- Created action items to improve logging, alerting, and monitoring for similar incidents

## Acknowledgements

- Thanks to UC Merced students and instructors for reporting the issue through our support system.
