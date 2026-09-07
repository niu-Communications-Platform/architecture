# Production Battery Pack Requirements

[Deutsch — canonical](../../de/20-hardware/battery-pack-requirements.md) | **English**

> The German version is canonical. This document is a maintained English translation.

## Purpose

This document defines requirements for the production-ready replaceable battery pack of the nıu Communications Platform beltpack and serves as a technical discussion brief for battery manufacturers.

**DECIDED:** nıu will not develop battery cells, the battery pack, or its internal battery management system. The product shall use a production-ready documented battery unit from a specialized manufacturer with integrated protection/battery management.

## Product context

The beltpack is a professional portable IP intercom and audio device. Major consumers are expected to include the Radxa ZERO 3W/RK3566 production candidate, internal and optional USB networking, two audio codecs, analog front ends, internal speaker/amplifier, color display, controls/RGB indicators, Secure Element, Carrier NVM, and the USB accessory host interface.

The device has a dedicated USB-C power input and a separate USB-C accessory/host port.

## Mechanical objective

The current approximately **120 × 80 × 35 mm enclosure size is a maximum envelope, not a volume to be filled**. The product shall become as compact as reasonably possible while preserving robustness, serviceability, thermal manageability, and usability.

## Rapid battery replacement as a product feature

**DECIDED:** The battery pack shall be a **rapid field-replaceable battery**, not merely regulatorily replaceable.

> **Optimize for operational availability, not maximum battery capacity.**

A compact pack with sufficient runtime may be preferable to a larger pack if an empty pack can be replaced quickly and reliably in production use. The target is replacement within a few seconds without opening the main enclosure. Exact mechanics will be defined with the selected production pack and shall consider an externally accessible compartment, robust latch, secure guidance, keyed contacts, and protection against accidental release.

The architecture shall permit spare packs and external single-/multi-pack chargers without requiring nıu to develop its own battery pack or BMS.

### No hot swap

**DECIDED:** Uninterrupted operation during battery replacement will not be supported. If the battery is removed without external power, the beltpack may power off and must be restarted after a battery is installed.

Seconds-scale energy buffering, a second internal energy store, or comparable hot-swap technology will not be added for this purpose. The operational benefit does not justify the additional volume, cost, and complexity.

Small electrical hold-up capacitance independently required for clean electrical power-down, voltage stability, or protection remains permitted and is explicitly not a hot-swap feature.

### Abrupt battery removal is an allowed operating condition

**DECIDED:** The user may remove the battery without first performing an orderly software shutdown. The system must tolerate this abrupt loss of power as a normal controlled failure condition, functionally equivalent to hard-off or other sudden power loss.

Consequences for system, storage, provisioning, and OTA architecture include:

- repeated abrupt power loss must not permanently damage or brick the device;
- critical persistent state must be updated atomically, transactionally, or otherwise power-loss safely;
- unnecessary frequent writes to eMMC/flash shall be minimized;
- interrupted OTA must not brick the device; A/B update, validation, and rollback must account for power loss;
- Factory/Device Identity must not depend solely on vulnerable SBC storage;
- after power is restored, the device must autonomously return to a defined consistent state;
- hard-power-loss tolerance shall be validated repeatedly in practice.

Orderly shutdown through POWER remains preferred, but product robustness must not depend on users performing it before every battery replacement.

## Serviceability and replacement

**DECIDED:** The complete battery pack is an end-user-replaceable functional unit. Replacement requires no soldering, heat, or solvents; uses safe keyed connection; must not be blocked by artificial software pairing; and must reset/relearn battery-specific health data appropriately. Long-term spare-pack availability is required.

## Technical battery pack requirements

The production pack should provide industrial-grade Li-ion technology, integrated protection/BMS, temperature monitoring, documented charge/discharge limits, sufficient continuous/peak current, documented communication such as SMBus/I²C where useful, suitable fuel-gauge data, a robust keyed connector with documented mating-cycle capability, and complete integration/compliance/lifecycle documentation.

## Operating requirements

The beltpack shall support mobile operation and continuous operation from external power. Power-path/load-sharing, charging behavior, Battery Care, avoidance of micro-cycling, thermal limits, transitions between external and battery power, and battery-state handling after replacement must be coordinated with the battery manufacturer. Pack BMS responsibilities and carrier system-power responsibilities remain separate.

## Runtime and power budget

Final minimum energy is not yet fixed. Rapid field replacement means one pack does not necessarily need to cover the maximum possible shift. Initial evaluation focuses particularly on approximately **19 Wh** and **25 Wh** classes. Larger packs must justify their added volume and weight through real product benefit.

## Reference candidate: vri BASE LINE

**CANDIDATE:** VRI GmbH Batterie-Technik's vri BASE LINE is the preferred reference candidate under investigation. Particularly interesting are the 1S/21700 product 88054 201 512 (~19.1 Wh) and 2S/18650 product 88030 502 512 (~25.2 Wh). The final choice must consider conversion efficiency, load profile, runtime, USB host reserve, thermal behavior, weight, volume, serviceability, and field-replacement speed rather than capacity alone.

## Manufacturer discussion

The discussion with VRI or alternatives shall cover 1S vs 2S suitability, continuous/peak loads, BMS vs carrier responsibilities, simultaneous operation/charging, Battery Care, fuel-gauge data, behavior after physical replacement, mechanical suitability and mating cycles for frequent field replacement, environmental constraints, conformity documentation, lifecycle/MOQ/pricing/spares, samples, possible adaptations, recommended field-replacement contacts, and external charging solutions.

## Decision rule

The preferred battery pack is the smallest production-ready pack that, with sufficient margin, satisfies the real electrical, thermal, runtime, serviceability, and lifetime requirements. Fast robust field replacement is part of that evaluation.

> **Battery capacity is a requirement, not a design goal. Product size, serviceability and reliable runtime are optimized together.**

> **Optimize for operational availability, not maximum battery capacity.**

## Sources / manufacturer information

Specific vri BASE LINE data must be verified against current manufacturer datasheets and direct technical coordination with VRI before a production decision. Public manufacturer information: https://www.vri-gmbh.de/en/products-solutions/vri-base-line
