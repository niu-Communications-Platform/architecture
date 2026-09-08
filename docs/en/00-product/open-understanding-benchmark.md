# Open Understanding – Benchmark against Fairphone and Framework

[Deutsch — canonical](../../de/00-product/open-understanding-benchmark.md) | **English**

> The German version is canonical. This document is a maintained English translation.

## Purpose

This document tests the **Open Understanding** product promise against two highly relevant existing concepts: Fairphone and Framework.

The goal is explicitly not to diminish either company. Both set important benchmarks for repairability, longevity, modularity, and technical openness. For nıu.cp, the relevant questions are which parts of these approaches are already established, what we can learn from them, and where a distinct additional promise can exist.

## Starting point for nıu.cp

The nıu Communications Platform follows this chain:

**Open Source → Open Hardware → Open Diagnostics → Open Repair Documentation → Open Understanding.**

Open Understanding adds a didactic promise to classic openness:

> **Open Hardware does not only mean: you may look inside. Open Understanding means: we help you understand what you see.**

This does not mean that every subsystem must be hand-assemblable. Modern SMT packages, multilayer PCBs, USB-C/PD, high-speed signals, RF, and low-noise audio electronics may require professional manufacturing. Openness and comprehensibility remain goals regardless.

## Fairphone

### What Fairphone already does very well

Fairphone explicitly designs products for repairability and longevity. Its official repair pages guide users through diagnostics and DIY repairs. Current products are documented with short expected repair times for modular replacements, and user-performed part replacement is an explicit product concept.

Fairphone also publishes substantial open-source software and frames user control over the device as a core value. Its phrase “If you can’t open it, you don’t own it” captures that position well.

Most relevant to nıu.cp, Fairphone also publishes PCB schematics or extensive board-level information for newer products and advanced repairs. Its 2024 impact reporting explicitly presents the release of Fairphone 5 PCB schematics as enabling advanced repair. Its 2025 impact reporting continues this transparency approach with kernel/device-tree sources and schematics.

### What nıu.cp should learn from Fairphone

- Plan repairability into product architecture and mechanics from the beginning.
- Make spare parts and repair information practically available rather than merely theoretically possible.
- Design simple repairs so that users can actually perform them.
- Publish board-level information for advanced repairs wherever technically and legally possible.
- Treat software openness and long-term usability as part of device ownership.

### Difference to Open Understanding

Fairphone explains very well **how a device can be repaired** and provides advanced technical material. In the official material reviewed, however, there is no equally explicit and systematic product promise to teach the user, through the concrete product itself, how the complete device works.

Open Understanding therefore does not primarily mean “more schematics”. It adds a mediation layer between the user and the Engineering Reference:

- What does a subsystem do?
- Why does it exist?
- How does it interact with other subsystems?
- Why was this architecture chosen?
- What problem does an individual component prevent?

The distinction is gradual, not absolute. Fairphone already does significant education and community work; nıu.cp aims to make this layer explicit and systematic.

## Framework

### What Framework already does very well

Framework combines repairability with modularity and extensibility. Its official support site provides setup, upgrade, and repair guides. Components are intentionally replaceable, and users are encouraged to upgrade and modify their devices.

For developers, Framework publishes open interfaces, 2D drawings, pinouts, and reference designs. Its Expansion Card and Input Module ecosystems are particularly strong examples of turning a consumer product into a development platform.

Framework does not, however, generally publish complete Mainboard schematics publicly for everyone. Its knowledge base states that pinouts and 2D drawings are public, while full schematics and assembly drawings are made available to qualified repair shops. Public schematics and reference designs are available for Expansion Card development.

### What nıu.cp should learn from Framework

- Think of hardware not only as repairable but deliberately extensible.
- Document interfaces well enough that third parties can genuinely develop accessories and modules.
- Treat repair and upgrade guides as normal product documentation rather than exceptional service material.
- Keep developer and consumer documentation distinct but deeply cross-linked.
- Enable official extensibility through defined electrical, mechanical, and software contracts.

### Difference to Open Understanding

Framework’s especially strong promise is:

> You may modify, extend, and upgrade this device.

Open Understanding adds:

> We also explain how and why the relevant parts work.

This is especially valuable to users who are not yet electronics engineers but are curious enough to become technically capable.

## Comparison

| Dimension | Fairphone | Framework | nıu.cp target |
| --- | --- | --- | --- |
| User repair | very strong | very strong | very strong |
| Spare parts | core concept | core concept | planned |
| Modularity / upgrades | strong | very strong | targeted |
| Open-source software | strong, with vendor limits | strong/selective | core principle |
| Public hardware documentation | extensive, model-dependent | selective | as complete as possible |
| Maker extensibility | present | very strong | explicit developer goal |
| Professional repair reference | yes | yes | yes |
| Systematic explanation of device operation | partial | partial | explicit product goal |
| Device as learning platform | not primary | indirect | explicit through Inside nıu.cp |

## Distinct nıu.cp promise

nıu.cp should not claim to have invented repairability, open hardware, or maker support. That would be inaccurate and unnecessary.

The distinct positioning comes from the combination of:

- consumer comfort without requiring technical knowledge,
- real repairability,
- developer freedom,
- open technical references,
- and an additional didactic layer that can guide a user from product-level understanding to engineering detail.

This yields the following internal positioning:

- **Fairphone:** This device belongs to you – repair it.
- **Framework:** This device belongs to you – extend it.
- **nıu.cp:** This device belongs to you – and we help you understand how it works.

This comparison is an internal strategic shorthand, not a claim made by the respective manufacturers and not an advertising claim of uniqueness.

## Documentation architecture

### Engineering & Repair Reference

Audience: electrical engineers, professional repair shops, experienced makers.

Content:

- complete or maximally publishable schematics
- BOMs with MPNs
- PCB and signal information
- pinouts and interfaces
- test points and expected values
- measurement and diagnostic procedures
- calibration
- factory and EOL tests
- exploded views
- replacement and recovery procedures
- known failure modes and repair paths

### Inside nıu.cp

Audience: technically curious users, motivated amateurs, makers, students, and career changers.

Didactic rule:

**Product purpose → architectural understanding → engineering detail.**

Technical terms are explained rather than avoided. The presentation may be entertaining, visual, and curiosity-driven without sacrificing technical truth.

Example topics include how voice becomes digital data, what an audio codec does, why the Carrier uses multiple audio paths, how stable 5 V is produced, what USB Power Delivery negotiates, how I²C/SPI/I²S/TDM/USB differ, how audio travels through Linux/Talkkonnect/Mumble/the network, why ESD protection exists, why the device contains a Secure Element, and what happens if power fails during an update.

Where useful, every didactic chapter should link directly to the relevant Engineering Reference. A reader should be able to move from an accessible explanation all the way to the actual schematic of the same subsystem.

## Explainability as an architecture test

Open Understanding can also serve as a quality check for architectural decisions.

For every major subsystem, we should be able to answer three questions:

1. What does it do?
2. Why do we need it?
3. Why did we build it this way?

If the third question cannot be answered convincingly, that is a warning sign for unnecessary complexity, historical baggage, or poorly justified architecture.

Explainability does not replace engineering validation, but it provides an additional test of conceptual clarity.

## Limits of the promise

Open Understanding does not mean:

- every PCB must be hand-buildable,
- safety-critical work should be recommended without appropriate qualification,
- private trust keys or other security secrets are published,
- proprietary third-party information is disclosed against license or NDA obligations,
- every internal manufacturing detail automatically becomes public,
- or a modified device must continue to qualify as officially nıu-certified.

The separation remains:

> **Diagnostics are open. Trust issuance is not.**

## Source basis

Official Fairphone sources reviewed September 2026:

- https://www.fairphone.com/de/repairs
- https://www.fairphone.com/de/open-source
- https://www.fairphone.com/de/software-longevity
- https://www.fairphone.com/de/stories/our-2024-impact-report-is-out-here-are-the-highlights
- https://www.fairphone.com/wp-content/uploads/2026/04/Fairphone-Impact_Report-2025.pdf

Official Framework sources reviewed September 2026:

- https://frame.work/support
- https://knowledgebase.frame.work/availability-of-schematics-and-boardviews-BJMZ6EAu

## Conclusion

Fairphone and Framework demonstrate that repairability, open technical documentation, modularity, and developer freedom can be practical in high-quality consumer products.

nıu.cp should explicitly treat these concepts as references and inspiration rather than trying to rhetorically outdo them.

The distinct product promise is the additional, deliberately planned mediation layer:

> **A nıu.cp device should not only be usable, repairable, and modifiable. A curious owner should have a real opportunity to understand it.**
