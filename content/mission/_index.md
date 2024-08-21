---
# Page title
title: Our open service
# Page type - we want a landing page (such as a homepage)
type: landing
sections:
  - block: markdown
    id: mission
    content:
      text: Our mission is to make research and education more **impactful**, **accessible**, and **delightful** by developing, operating, and supporting infrastructure for interactive computing.

  - block: features
    id: goals
    content:
      title: Goals
      subtitle: "Our service goals are to help communities in research and education be more..."
      items:
        - name: Impactful
          description: Accelerate the ability to create and share interactive knowledge internally and externally. Make community workflows more productive and efficient so that users can ask questions and share results more effectively.
          icon: bolt
          icon_pack: fas
        - name: Accessible
          description: Make interactive computing accessible to a diverse range of global communities. Broaden participation in knowledge creation and sharing across the world, particularly from marginalized communities.
          icon: globe
          icon_pack: fas
        - name: Sustainable
          description: Build a financially sustainable and globally scalable service. Use our resources to support and grow the open source communities that we partner with to support a healthy open ecosystem. 
          icon: leaf
          icon_pack: fas

  - block: features
    content:
      title: Principles
      subtitle: Our service principles help communities trust us as stewards of critical scientific workflows.
      items:
        # LEAVE OUT PARTNERSHIP because this forces us to use 3 columns
        - name: Transparency
          description: Our infrastructure should be transparent and modular so that it respects the community's [Right to Replicate](/right-to-replicate).
          icon: magnifying-glass
          icon_pack: fas
        - name: Empowerment
          description: Our platform gives communities agency to design the service they need, and to manage it without 2i2c if they wish.
          icon: bolt
          icon_pack: fas
        - name: Partnership
          description: Our participatory service model ensures we maximize our impact and keeps our incentives aligned with community needs.
          icon: handshake
          icon_pack: fas
        
  - block: markdown
    id: share-learn
    content:
      title: We empower communities to share and learn.
      subtitle: Interactive computing hubs provide access to standardized workflows that make it easier for community members to teach and share with one another, and to enhance their work together.
      text: |

        {{< figure src="/images/service/community-improvements.png" alt="How communities improve with shared infrastructure.">}}


  - block: markdown
    id: numbers
    content:
      title: We build on an ecosystem of open tools, standards, and services to enable the lifecycle of knowledge creation
      subtitle: Building with flexible, modular, and open technology allows us to re-use the same components for many community workflows. This allows us to build community-centric infrastructure in a scalable way.
      text: |
        {{< figure src="/images/service/service-lifecycle.png" alt="The service lifecycle we enable.">}}

        <center> <strong>Open source tools we use and support in our service.</strong></center>

        {{< opensourcelogos >}}

  - block: markdown
    id: impactful
    content:
      title: We make open source tools more impactful for research and education
      subtitle: 
      text: |

        Our global network gives us a unique perspective to identify high-impact improvements to open source tools. We collaborate with open source communities to make upstream enhancements, and re-deploy the improved tools to the communities in our network.

        {{< figure src="/images/home/os-lifecycle.png" alt="The lifecycle of upstream development">}}

---