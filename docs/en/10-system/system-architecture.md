---
language: en
canonical: false
status: current
last_reviewed: 2026-09-07
source: ../../de/10-system/system-architecture.md
translation_status: current
---

# System Architecture

[Deutsch — canonical](../../de/10-system/system-architecture.md) | **English**

> The German version is canonical. This document is a maintained English translation.

## Repository/component boundaries

The GitHub organization `nıu Communications Platform` is the technical umbrella for the project.

Planned main repositories:

- `architecture` — cross-product architecture, decisions, validation
- `beltpack` — device hardware and device software
- `base` — local appliance/server services
- `cloud` — hosted platform
- `factory-tools` — manufacturing, EOL, and factory-provisioning tools

Additional repositories such as `shared`, `sdk`, `simulator`, or apps will only be created when a genuinely independent responsibility emerges.

## Shared architectural abstractions

### Capability Layer

Hardware and the operating system report actual capabilities. Profiles and provisioning consume these capabilities instead of inferring hardware variants from CPU names or assumptions.

Hardware detection on Linux should primarily use Device Tree (`/proc/device-tree/model`, `compatible`).

A Capability Profile may include, among other things:

- playback/capture channels
- TDM slots
- split-ear capability
- independent outputs
- USB/Bluetooth audio
- board/PCB revision

Profiles declare requirements; the Provisioning Authority or Device Agent validates compatibility.

### Device Agent

A platform-wide device component called `niu-device-agent` is planned. Areas of responsibility:

- Identity
- Enrollment
- Capabilities
- Provisioning
- Health
- OTA
- Registry Heartbeat

Talkkonnect remains primarily the intercom engine and should not become the general device manager.

## Architecture phase

The current milestone is the **P0 Architecture Gate**. Before prototyping, expensive hardware lock-ins are clarified sufficiently; after that, theoretical architecture and practical validation proceed in parallel.
