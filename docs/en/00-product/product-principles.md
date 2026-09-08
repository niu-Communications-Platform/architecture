# Product Principles

[Deutsch — canonical](../../de/00-product/product-principles.md) | **English**

> The German version is canonical. This document is a maintained English translation.

## Product model

The nıu Communications Platform includes several deployment models:

- **Bare:** intercom endpoint; the Mumble/Murmur infrastructure is provided by the user.
- **Base:** intercom plus locally operated Mumble/Murmur and management infrastructure.
- **Cloud:** intercom plus nıu-hosted Mumble/Murmur and management infrastructure.

Where sensible, the product variants should use the same device, provisioning, and protocol foundations. Differences primarily concern the Provisioning Authority, the Trust Domain, and the location of the service infrastructure.

## Guiding principles

### User convenience

Complexity is absorbed by the product rather than passed on to the user. Normal operation should be curated, understandable, and robust.

### Apple-like convenience and developer freedom

There are three layers:

1. **Product layer:** tested and supportable standard features.
2. **Provisioning layer:** administrator profiles configure more complex capabilities through abstractions.
3. **Developer layer:** source code, configuration, and APIs may use the underlying capabilities more freely.

**Capability ≠ Feature.** A technical capability becomes an official feature only when it is understandable, robust, testable, and supportable.

### Openness

The platform should be fully open source and reproducibly buildable wherever third-party licenses permit. Openness of implementation does not mean disclosure of private trust keys and does not grant the right to present a service as an official nıu service.

### Digital sovereignty includes the hardware

Digital sovereignty does not end with access to source code or self-hosting. The owner should be able to understand, diagnose, repair, recover, and continue operating the product with custom software or custom Trust Domains.

This leads to the following product goal:

**Open Source → Open Hardware → Open Diagnostics → Open Repair Documentation → Open Understanding.**

Where technically and legally possible, nıu therefore publishes the information and tools required for qualified independent fault analysis and repair. This includes hardware and interface information, diagnostic procedures, repair instructions, relevant test points and expected values, calibration and recovery procedures, and open diagnostic tools.

#### Open Understanding

Open schematics and bills of materials alone do not make a product understandable. Documentation should therefore explain not only **how** the beltpack is built, but also **what its subsystems and important components do, why they are needed, and why the architecture was chosen**.

Two complementary documentation layers are planned:

1. **Engineering & Repair Reference** – precise technical reference for electrical engineers, professional repair shops, and experienced makers: schematics, BOMs with MPNs, pinouts, PCB/signal information, test points and expected values, measurement and diagnostic procedures, exploded views, calibration, replacement/recovery procedures, and relevant factory tests.
2. **Inside nıu.cp** – didactic and visual documentation for technically curious users, motivated amateurs, and makers. It explains real engineering concepts through the actual product and follows signal, energy, data, and trust paths through the device. Technical terminology is explained rather than avoided.

`Inside nıu.cp` must not become a technically inaccurate simplified version of the engineering documentation. The goal is the same technical truth at a different didactic level: from product purpose through architectural understanding to concrete engineering detail.

Potential topics include how voice becomes digital data and back again; what an audio codec does; how stable system rails are generated from a changing battery voltage; how USB-C and USB Power Delivery negotiate power; how chips communicate over I²C, SPI, and I²S/TDM; how audio travels through Linux, Talkkonnect, Mumble and the network; why ESD protection, secure elements, watchdogs, A/B updates and hardware hard-off exist; and what an apparently insignificant individual component actually prevents.

The documentation may deliberately create curiosity and enthusiasm. The beltpack should not be perceived as a sealed black box, but as a high-quality consumer product whose operation can be understood.

**Not every open hardware design is sensible to assemble by hand.** Fine-pitch SMT packages, multilayer PCBs, high-speed/RF, USB-C/PD, and low-noise audio requirements may require professional assembly. Open Understanding therefore does not promise that every user can build the complete Carrier PCB with a soldering iron. Where repairs, modules, or assemblies are maker-friendly, they should be documented accordingly.

Principle:

> **Open Hardware does not only mean: you may look inside. Open Understanding means: we help you understand what you see.**

The openness of diagnostics and repair remains strictly separated from the official nıu Trust Domain:

> **Diagnostics are open. Trust issuance is not.**

A repair or modification by the owner or an independent repair shop does not by itself terminate the device's official nıu trust status. As long as the existing cryptographic device identity can still be reliably proven, it is generally preserved. If the Identity Anchor can no longer be reliably proven or has to be replaced, a controlled nıu recertification process is required for renewed admission to or attestation within the official nıu Trust Domain.

### Future-proofing without feature stuffing

Low-cost hardware reserves are included where they avoid future dead ends. Not every reserve becomes an immediate product feature.

### Manufacturability

Hardware decisions are evaluated against whether a contract manufacturer can reproducibly build, program, and automatically test the device in quantities ranging from thousands to tens of thousands.
