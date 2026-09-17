---
# Page title
title: Hubs in practice
# Page type - we want a landing page (such as a homepage)
type: landing

# Each example below is one {{< hub-example >}} block.
# The community is the subject: link to their site, use an image from their
# space, attribute it in the caption, and use *their* content for quotes or numbers.
# We want to highlight (and give attribution for) their work, not make this about us.
# See layouts/shortcodes/hub-example.html for the shortcode definition / parameters / etc.
# The jump list at the top of the page is maintained by hand: update it when you add or remove an example.
sections:
  - block: markdown
    id: examples
    content:
      title: Hubs in practice
      subtitle: What communities in our network do with their hubs.
      text: |

        <div class="hub-example-index">

        [Compute next to data](#data) ⋅ [Shared learning environments](#practice) ⋅ [Thousands of students](#scale) ⋅ [Predictable costs](#cost) ⋅ [Workshops and events](#events) ⋅ [Notebooks, RStudio, desktops](#interfaces) ⋅ [GPUs](#gpu) ⋅ [GenAI](#genai) ⋅ [Reproducible sharing](#share) ⋅ [Networks of hubs](#network) ⋅ [Right to replicate](#own)

        </div>

        {{< hub-example id="data" community="EarthScope GeoLab" url="https://www.earthscope.org/data/geolab/"
            heading="Analysis next to the data, at cluster scale"
            stat="14 months" stat_label="of satellite positioning (GNSS) data processed in 27 seconds by 12 Dask workers on GeoLab."
            image="/images/communities/earthscope-gnss-benchmark.png"
            alt="Bar chart comparing days of GNSS data processed per second from downloaded files, analysis-ready data, and analysis-ready data with a compute cluster"
            caption="Days of GNSS data processed per second, from downloaded files, from cloud-optimized data, and from cloud-optimized data with a Dask cluster. The cluster makes the biggest difference. Chart by EarthScope, from [Pancakes are the future of geophysical data processing](https://www.earthscope.org/news/pancakes-are-the-future-of-geophysical-data-processing/)." >}}
        EarthScope built GeoLab beside its cloud-optimized geodesy archive on AWS, so researchers start in a small notebook server and scale out to a [Dask cluster](/platform/#compute) from the same browser tab.
        In June 2026 EarthScope [opened GeoLab to its whole community](https://www.earthscope.org/news/geolab-cloud-compute-hub-now-open-to-all-users/) of [nearly 400 member institutions](https://www.earthscope.org/about/membership/).

        [NASA MAAP](https://www.earthdata.nasa.gov/about/maap) and [LEAP](https://leap.columbia.edu/) work the same way, with hubs beside petabytes of Earth and climate data.
        {{< /hub-example >}}

        {{< hub-example id="practice" community="CryoCloud" url="https://cryointhecloud.com/"
            heading="A shared environment a field can learn on"
            stat="500+" stat_label="scientists onboarded since 2022 through workshops, hackweeks, and open learning resources"
            image="/images/communities/cryocloud-tutorials.png"
            alt="The tutorials page of the CryoCloud Jupyter Book, listing notebooks and recordings"
            caption="[The CryoCloud book](https://book.cryointhecloud.com/): tutorials, onboarding recordings, and hub guides written by the CryoCloud community." >}}
        CryoCloud began as a hub for NASA cryosphere scientists and now serves Earth scientists more broadly.
        It runs next to NASA Earth data, with several community-maintained Python and R environments and a book of tutorials that [hackweeks](https://icesat-2.hackweek.io/) and science teams build on.
        Its leaders described the approach in [*Democratizing Science in the Cloud*](https://eos.org/opinions/democratizing-science-in-the-cloud), including 12 hackathon-style workshops on the hub at about a dollar per person per day.
        {{< /hub-example >}}

        {{< hub-example id="scale" community="University of Toronto" url="https://datatools.utoronto.ca/"
            heading="Thousands of students on one hub"
            stat=">6,000" stat_label="educators and learners using the hub in a single day"
            image="/images/communities/utoronto-datatools.png"
            alt="The University of Toronto JupyterHub landing page with Jupyter Notebook, RStudio, and JupyterLab log-in options"
            caption="The [datatools.utoronto.ca](https://datatools.utoronto.ca/) landing page, branded for the university. Students choose Notebook, RStudio, or JupyterLab and sign in with their university account." >}}
        The University of Toronto runs a Python hub, an R hub, and a high-memory hub for courses across the university, with [its own support pages](https://act.utoronto.ca/jupyterhub-support/).
        Instructors share assignments as [nbgitpuller links](https://nbgitpuller.readthedocs.io/) that open directly on the hub.
        [How the hub manages storage at that scale](../blog/2024/utoronto-storage-monitoring/index.md) is on our blog.
        {{< /hub-example >}}

        {{< hub-example id="cost" community="NASA Openscapes" url="https://openscapes.cloud/"
            heading="Predictable costs"
            stat="$0.74" stat_label="measured cost of a NASA data workflow on the Openscapes hub"
            image="/images/communities/openscapes-workflow-cost.png"
            alt="Chart of CPU and memory requested and used over three hours for a NASA Openscapes workflow, with a total cost of 74 cents"
            caption="Chart by Openscapes, from [their community call on hub cloud costs](https://openscapes.org/blog/2025-05-01-community-call-hub-cloud-costs/)." >}}
        Openscapes priced a real workflow on their hub from its usage metrics and AWS billing, then shared the result and [their tooling](https://github.com/Openscapes/jupycost) with their community.
        Every hub [reports usage](/platform/#reporting) the same way.

        EarthScope takes a different route to the same goal.
        Its open hub gives each user a [rolling 30-day usage quota](https://www.earthscope.org/data/geolab/), built on [compute quotas](../blog/2026/jupyterhub-usage-quotas/index.md) available on any hub.
        {{< /hub-example >}}

        {{< hub-example id="events" community="CIROH" url="https://hub.ciroh.org/"
            heading="Workshops for hundreds"
            stat="132" stat_label="participants a day on the CIROH workshop hub at the peak of DevCon 2026"
            image="/images/communities/ciroh-devcon-2026-usage.png"
            alt="Chart of daily active users on the CIROH hubs around DevCon 2026, with the workshop hub rising from about 20 to over 140 during the event and falling back afterward"
            caption="Chart by CIROH, from [Powering CIROH DevCon 2026: How CIROH and 2i2c Ran Cloud Computing at Scale](https://hub.ciroh.org/blog/devcon26-infra/). The workshop hub fills for the event and empties afterward." >}}
        Workshops bring hundreds of first-time users at once, for a day or two.
        CIROH ran 12 of DevCon 2026's 15 hands-on workshops on a dedicated workshop hub, nine of them on software images built for the sessions.

        NASA Openscapes mentors did the same at a larger scale.
        Their [machine learning workshop](https://openscapes.org/blog/2025-09-30-ornl-arset-workshop/) on the Openscapes hub drew 401 participants from 68 countries.
        {{< /hub-example >}}

        {{< hub-example id="interfaces" community="NASA VEDA" url="https://www.earthdata.nasa.gov/dashboard/"
            heading="Notebooks, RStudio, VS Code, web apps, or a desktop"
            image="/images/communities/veda-server-options.png"
            alt="The NASA VEDA server options page, with a Pangeo notebook environment and an NVIDIA T4 GPU option"
            caption="The launch page of the [NASA VEDA hub](https://docs.openveda.cloud/user-guide/scientific-computing/). Users pick the environment and server size each time." >}}
        NASA VEDA's launch page offers a Python environment, RStudio, or a [Linux desktop with QGIS](/platform/#desktop), with an optional [GPU](/platform/#compute), and [VEDA's docs](https://docs.openveda.cloud/user-guide/scientific-computing/) cover VS Code on the same hub.
        [Development Seed](../collaborators/devseed/index.md) and 2i2c demonstrated an [Open in QGIS button](../blog/2025/veda-update-q4-2024/index.md) that takes a layer from the VEDA dashboard straight into QGIS on the hub.

        On its own hub, [Openscapes](https://openscapes.org/blog/2023-10-17-matlab-on-openscapes/) runs MATLAB with users' own licenses.
        {{< /hub-example >}}

        {{< hub-example id="gpu" community="CloudBank Classroom" url="https://www.cloudbank.org/training/access-cloudbank-classroom"
            heading="GPUs for a classroom"
            stat="~$200" stat_label="in cloud costs for the whole GPU tutorial"
            image="/images/communities/cloudbank-gpu-workshop.png"
            alt="Line chart of GPU utilization during the workshop"
            caption="GPU load during the tutorial, taught by Eric Van Dusen and Sean Morris of UC Berkeley for CloudBank Classroom. Chart from [our write-up](../blog/2026/t4-gpu-timeslicing/index.md)." >}}
        CloudBank Classroom taught [Teaching in the AI Classroom](https://events.internet2.edu/website/89730/tutorials/) at the NAIRR annual meeting on a GPU-enabled hub.
        The cloud provider could not supply one GPU per learner, so learners shared GPUs, sized from measurements beforehand, and the tutorial ran without issues.
        [How GPU sharing works](../blog/2026/t4-gpu-timeslicing/index.md) is on our blog.
        {{< /hub-example >}}

        {{< hub-example id="genai" community="Responsible Gen-AI for NASA Earthdata" url="https://responsible-genai.hackweek.io/"
            heading="Jupyter AI and coding agents, inside the hub"
            image="/images/communities/responsible-genai-hackweek.png"
            alt="Landing page of the Responsible Gen-AI for NASA Earthdata 2026 hackweek, August 24 to 28 in Seattle"
            caption="The [hackweek site](https://responsible-genai.hackweek.io/), by the UW eScience Institute. Tutorials cover coding agents, context engineering, Model Context Protocol servers, and agent sandboxing." >}}
        In August 2026 the UW eScience Institute, NASA Earthdata, and CryoCloud ran a five-day hackweek in Seattle on using generative AI for NASA Earth data responsibly.
        Participants worked on the CryoCloud hub, where the CryoCloud team [built an image](https://github.com/CryoInTheCloud/image-cryo-python-AI) with a Jupyter AI pre-release and [a coding agent](https://github.com/2i2c-org/infrastructure/pull/8905) that runs against [open-weight models hosted by the NSF National Research Platform](https://nrp.ai/llms/).
        This is early work, and communities are still learning how to incorporate generative AI in their hubs responsibly.
        {{< /hub-example >}}

        {{< hub-example id="share" community="Project Pythia" url="https://projectpythia.org/"
            heading="Reproduce an analysis from a link"
            stat="30+" stat_label="geoscience cookbooks, each with a launch button that runs it in the browser"
            image="/images/communities/pythia-cookbook-gallery.png"
            alt="The Project Pythia cookbook gallery with cards for several cookbooks"
            caption="[The Project Pythia cookbook gallery](https://cookbooks.projectpythia.org/). Cookbooks are binderized so each can run in the cloud with one click." >}}
        Project Pythia's cookbooks are complete, re-runnable analyses.
        Each opens on a [BinderHub](/platform/#sharing), so a reader can run it without installing anything, and cookbooks that need more compute than GitHub provides are [executed on the Pythia Binder](https://projectpythia.org/cookbook-guide/) instead.
        Pythia's Binder runs on [NSF Jetstream2](https://jetstream-cloud.org/).
        [How we deployed it](../blog/2025/jetstream-binderhub/index.md) is on our blog.
        {{< /hub-example >}}

        {{< hub-example id="network" community="CloudBank Classroom" url="https://www.cloudbank.org/training/access-cloudbank-classroom"
            heading="Funded networks of hubs that share the same workflow"
            stat="~70" stat_label="hubs run from one shared configuration"
            image="/images/communities/cloudbank-hub-logos.png"
            alt="Logos of two dozen colleges and universities with CloudBank Classroom hubs"
            caption="Some of the institutions with a CloudBank Classroom hub, from California community colleges to HBCUs and research universities." >}}
        CloudBank Classroom gives colleges the same Jupyter setup Berkeley uses for [Data 8](https://data8.org/).

        NASA runs [the same hub software](https://docs.maap-project.org/en/hub/system_reference_guide/faq/ade_to_hub.html) across VEDA, the [GHG Center](https://earth.gov/ghgcenter), [MAAP](https://maap-project.org/), and Disasters.
        The [CZI](../collaborators/czi/index.md)-funded [Catalyst Project](../collaborators/catalyst/index.md) ran hubs for [19 biomedical groups in Africa and Latin America](../blog/2024/catalyst-partner-highlights/index.md).
        {{< /hub-example >}}

        {{< hub-example id="own" community="Open infrastructure" url="/open-practices/"
            heading="Your right to replicate and control"
            image="/images/communities/cloudbank-config-github.png"
            alt="The CloudBank cluster configuration folder in the public 2i2c infrastructure repository on GitHub, with a recent commit by a CloudBank engineer"
            caption="CloudBank's hub configuration in [our public infrastructure repository](https://github.com/2i2c-org/infrastructure/tree/main/config/clusters/cloudbank). The latest commit shown is by a member of the CloudBank team." >}}
        Communities own the tools they use.
        Every hub is deployed from open source and a public configuration you can fork, and you keep the [right to replicate](../right-to-replicate/index.md) it elsewhere.
        [CloudBank](https://www.cloudbank.org/)'s team now [deploys changes to their own cluster](../blog/2026/cloudbank-self-service/index.md).

        As Catalyst Project funding wound down, [CCAD](https://supercomputo.unc.edu.ar/2025/09/02/colgando-a-boogie/) in Argentina [used it to buy on-premise hardware](../blog/2025/catalyst-hardware-exchange/index.md) for its own JupyterHub.

        EarthScope, Openscapes, and CIROH run their hubs in cloud accounts they own.
        {{< /hub-example >}}

  - block: markdown
    id: join
    content:
      title: "Join our community network"
      text: |
        Many of these communities are [members](../members/index.md) or [collaborators](../collaborators/_index.md) of 2i2c.
        Longer versions of many of these stories are on [our blog](../blog/_index.md).

        {{< cta cta_text="Join our network of communities" cta_link="/join" cta_new_tab="false" >}}

---
