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

A Capability Profile may include playback/capture channels, TDM slots, split-ear capability, independent outputs, USB/Bluetooth audio, and board/PCB revision. Profiles declare requirements; the Provisioning Authority or Device Agent validates compatibility.

### Device Agent

A platform-wide `niu-device-agent` is planned for Identity, Enrollment, Capabilities, Provisioning, Health, OTA, and Registry Heartbeat. Talkkonnect remains primarily the intercom engine and should not become the general device manager.

## Hard power-loss tolerance

**DECIDED:** Abrupt loss of power is an allowed operating and failure condition, particularly for rapid removal of the replaceable battery, hard-off, and unexpected supply loss.

The system must be designed so repeated hard power loss does not permanently damage device identity or critical configuration and the device autonomously returns to a consistent state on the next boot.

This requires power-loss-safe persistent state changes, minimized unnecessary flash/eMMC writes, A/B OTA with validation and rollback even when interrupted, no exclusive storage of indispensable Factory/Identity data on SBC storage, defined recovery paths for damaged runtime/cache data, and repeated practical power-cut testing including adverse timing during configuration and update operations.

Orderly shutdown remains the normal path, but product integrity must not depend on it.

## Architecture phase

The current milestone is the **P0 Architecture Gate**. Before prototyping, expensive hardware lock-ins are clarified sufficiently; after that, theoretical architecture and practical validation proceed in parallel.
