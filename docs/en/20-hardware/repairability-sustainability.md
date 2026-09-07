# Repairability and Resource Conservation

[Deutsch — canonical](../../de/20-hardware/repairability-sustainability.md) | **English**

> The German version is canonical. This document is a maintained English translation.

## Goal

The hardware architecture shall maximize the service life of the beltpack and prevent the failure of a single component from unnecessarily requiring replacement of the entire product.

## Architecture principles

**DECIDED:** Failure of a single non-structural component should generally not require replacement of the entire beltpack.

**DECIDED:** The smallest technically, environmentally and economically reasonable functional unit shall be repaired or replaced.

**DECIDED:** Repairs should preserve Device Identity and Provisioning wherever technically possible and secure.

**DECIDED:** Component-level repair is preferred where reasonable. Module replacement is preferred where component-level repair would require disproportionate labor, energy, equipment or risk of damage.

**DECIDED:** Diagnostic and repair knowledge is not artificially treated as a manufacturer secret. Qualified independent repair should be practically possible through publicly available documentation and tools.

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

## Open diagnostics and repair documentation

The product's repairability should not merely exist by design; it should be practically usable by third parties. nıu therefore plans comprehensive, publicly available fault-analysis and repair documentation that is maintained throughout the product lifecycle.

Where appropriate and legally possible for the respective product, it includes in particular:

- opening, disassembly, and assembly instructions
- descriptions of assemblies and their functions
- schematics and relevant hardware/interface information
- connector pinouts, test points, and expected measurements
- boot, recovery, and reimaging procedures
- open diagnostic tools and hardware self-tests
- symptom-oriented troubleshooting trees
- replacement procedures for service and wear components
- board-level diagnostic and repair guidance
- calibration procedures after relevant repairs
- final functional and safety tests
- spare-part information and, where appropriate, specifications for compatible third-party components
- known failure modes and repair guidance derived from them

The Repair Knowledge Base should evolve with experience from manufacturing, RMA, and field operation. Recurring failure modes are documented with reproducible diagnostic and repair paths instead of remaining exclusively internal service knowledge.

## Shared diagnostic foundation for Factory and Repair

Where sensible, hardware self-tests and diagnostic primitives should be shared between Factory EOL, nıu RMA, and independent repair. Technical diagnostics themselves must not depend on secret Factory Credentials.

Examples include audio codec reachability, audio loopback/level tests, display and button tests, USB enumeration and VBUS tests, network diagnostics, and Secure Element reachability.

Privileged operations within the official nıu Trust Domain remain separate. A public diagnostic tool may test hardware without thereby being able to issue nıu Device Certificates, create Factory Registry entries, or produce other nıu attestations.

Principle:

> **Diagnostics are open. Trust issuance is not.**

## Repair and nıu trust status

Opening, diagnosing, repairing, or modifying a device by its owner or an independent repair shop does not by itself cause the loss of official nıu trust status.

If Carrier Identity and the cryptographic Identity Anchor remain intact and can still be reliably proven, the existing Device Identity is generally preserved. This applies, for example, to replacement of the battery, display, buttons, speaker, microphones, SBC/storage, or repairable carrier components, provided that the Identity Anchor is not affected.

If the Identity Anchor can no longer be reliably proven or must be replaced, an open recovery or repair process must not be able to create new official nıu attestations by itself. Restoring official nıu trust status then requires a controlled nıu recertification process. For the first product generation, the physical device is intended to be sent to nıu as the manufacturer for inspection and recertification.

This boundary does not restrict the owner's continued use of the device with custom software or a custom Trust Domain.

## Calibration and repair

Calibration data must not unnecessarily tie repairs to the original factory. Calibration is designed to be explicit, versioned and reproducible so that a service test station can redetermine relevant values after component replacement.

Possible calibration fields include microphone gain offsets, speaker level offsets and audio calibration versions. Only values actually required by the production product will be used.

## Sustainability goal

System modularity is not intended to maximize disassembly at any cost. The goal is a long real-world service life with low replacement granularity, reproducible repair and sensible reuse of assemblies.
