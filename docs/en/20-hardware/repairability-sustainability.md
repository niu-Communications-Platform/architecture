---
language: en
canonical: false
status: current
last_reviewed: 2026-09-07
source: ../../../de/20-hardware/repairability-sustainability.md
translation_status: current
---

# Repairability and Resource Conservation

## Goal

The hardware architecture shall maximize the service life of the beltpack and prevent the failure of a single component from unnecessarily requiring replacement of the entire product.

## Architecture principles

**DECIDED:** Failure of a single non-structural component should generally not require replacement of the entire beltpack.

**DECIDED:** The smallest technically, environmentally and economically reasonable functional unit shall be repaired or replaced.

**DECIDED:** Repairs should preserve Device Identity and Provisioning wherever technically possible and secure.

**DECIDED:** Component-level repair is preferred where reasonable. Module replacement is preferred where component-level repair would require disproportionate labor, energy, equipment or risk of damage.

## Repair levels

### Level 1 — End User Replaceable

Components that the end user should be able, or is legally required to be able, to replace safely.

- battery
- where appropriate, belt clip and simple mechanical parts

According to ADR-0005, the battery is required to be designed as an End-User Replaceable Unit.

### Level 2 — Service Replaceable Module

Replacement after opening the device using normal service procedures, preferably through connectors rather than soldering.

Examples:

- SBC / compute module
- display
- speaker
- microphone modules
- where appropriate, mechanically stressed I/O daughterboards

### Level 3 — Board-Level Repair

Specialized repair on the carrier PCB.

Examples:

- audio codecs
- USB hub
- charging/power controllers
- jacks and connectors unless located on a daughterboard
- Secure Element
- carrier NVM

### Level 4 — Carrier Replacement

The complete nıu carrier is replaced only where board-level repair is technically or economically unreasonable. Replacing the carrier has specific implications for Factory/Device Identity and requires a controlled Replace Device process.

### Level 5 — Refurbishment / Recycling

Replaced modules are not automatically discarded. Where reasonable, they are diagnosed, repaired, erased, retested and reused as service/refurbished parts. Parts that cannot reasonably be repaired are sent to appropriate material recycling.

## Compute module

CPU, RAM and eMMC are not integrated directly into the nıu carrier PCB; they reside on a replaceable SBC module. In normal service, failure of eMMC/RAM/SoC therefore results in replacement of the compute module rather than replacement of the complete beltpack.

Component-level rework on the SBC remains a task for specialized repair partners and is not a normal RMA path.

The carrier/software architecture should allow a future compatible SBC replacement where interfaces and product requirements permit it.

## Mechanically stressed connectors

**OPEN / P0 REVIEW:** Evaluate whether connectors particularly exposed to mechanical failure, such as TRRS, PHONES, MIC and the external USB-C ports, should be moved to one or more small replaceable I/O boards.

The advantage would be a smaller replacement assembly in the event of mechanical damage. This must be balanced against additional PCBs, cable/flex connections, connectors, assembly effort, material use and potential failure points.

The decision shall be based on actual mechanics, space requirements, BOM, assembly and expected failure probability; modularity is not an end in itself.

## Battery

The battery is an expected wear component and must not determine the service life of the product.

Requirements according to ADR-0005 include in particular:

- the end user can replace the complete battery
- no soldering
- no disassembly requiring heat or solvents
- commonly available tools are sufficient
- polarity-safe connector
- no software pairing that obstructs compatible replacement batteries
- Battery Learning/Health State can be correctly reinitialized after replacement

## Calibration and repair

Calibration data must not unnecessarily tie repairs to the original factory. Calibration is designed to be explicit, versioned and reproducible so that a service test station can redetermine relevant values after component replacement.

Possible calibration fields include microphone gain offsets, speaker level offsets and audio calibration versions. Only values actually required by the production product will be used.

## Sustainability goal

System modularity is not intended to maximize disassembly at any cost. The goal is a long real-world service life with low replacement granularity, reproducible repair and sensible reuse of assemblies.
