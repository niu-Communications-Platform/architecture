# Production Battery Pack Requirements

[Deutsch — canonical](../../de/20-hardware/battery-pack-requirements.md) | **English**

> The German version is canonical. This document is a maintained English translation.

## Purpose

This document defines the requirements for the production-ready, replaceable battery pack of the nıu Communications Platform beltpack and serves as a technical discussion brief for battery manufacturers.

**DECIDED:** nıu will not develop the battery cells, battery pack, or its internal battery management system. The product shall use a production-ready, documented battery unit from a specialized manufacturer, suitable for the application and including integrated protection/battery management.

The carrier integrates the battery pack into the overall system. Charging, power-path, measurement, and system functions required outside the pack will only be defined after pack selection and technical coordination with the battery manufacturer.

## Product context

The beltpack is a professional portable IP intercom and audio device for live production, events, and comparable mobile applications.

Expected major consumers include:

- ARM SBC; production candidate Radxa ZERO 3W / RK3566
- internal and potentially additional USB Wi-Fi or USB Ethernet
- two audio codecs and analog audio front ends
- internal speaker and amplifier
- color display
- controls and RGB status indicators
- Secure Element, Carrier NVM, and additional peripherals
- USB host interface for USB Audio, Ethernet, HID, and other supported devices

The device has a dedicated USB-C power input and a separate USB-C accessory/host port.

## Mechanical objective

The current enclosure target of approximately **120 × 80 × 35 mm is a maximum envelope, not a volume to be filled**.

**DECIDED:** While preserving robustness, serviceability, thermal manageability, and good usability, the product should become as compact as reasonably possible. A smaller battery pack is therefore explicitly desirable if the required runtime and power reserve can still be achieved.

The battery should not unnecessarily dictate the product's external dimensions. Energy content is optimized against volume, weight, electrical efficiency, and real operating time; maximum capacity is not a goal in itself.

## Serviceability and replacement

**DECIDED:** The complete battery pack is an end-user-replaceable functional unit.

Requirements include:

- no soldering for battery replacement
- no heat or solvents
- safe mechanical access
- keyed/polarity-safe connection
- no software pairing that artificially prevents use of a compatible replacement battery
- full restoration of normal device operation after replacement
- defined reset or relearning of battery-related health/learning data so a new battery does not inherit the aging state of its predecessor
- long-term availability of replacement packs or a robust spare-parts strategy

The product shall not use a proprietary battery architecture merely to create customer lock-in.

## Technical battery pack requirements

The production pack should preferably provide:

- industrial-grade lithium-ion battery unit
- integrated protection and battery management functions
- temperature monitoring
- protection against relevant over-/undervoltage, overcurrent, and short-circuit conditions
- documented charge and discharge limits
- sufficient continuous and peak current capability for the beltpack including the defined USB host load
- documented system communication, preferably via an established interface such as SMBus or I²C where this does not create unnecessary proprietary dependency
- suitable status/fuel-gauge information for state of charge, health, and diagnostics
- production-grade locking and keyed connector
- documented lifetime and temperature ranges
- complete documentation required for integration, transport, and product conformity
- long-term production and spare-part availability

A Smart Battery protocol is not a goal in itself. The relevant requirement is that the interface is documented, robust, and usable long-term and does not artificially bind battery replacement to a single cryptographically paired pack.

## Operating requirements

The beltpack shall support both mobile operation and continuous operation from external power.

Topics to clarify with the battery manufacturer include:

- permitted pack behavior while the device is operating and charging simultaneously
- required system architecture for true power-path/load-sharing operation
- appropriate charging characteristics and maximum charging currents
- behavior during extended external-power operation
- Battery Care or reduced charge limits for lifetime optimization
- avoidance of unnecessary micro-cycling during stationary operation
- charging and discharging temperature limits
- safe transitions between external power and battery operation
- appropriate interpretation of State of Charge, State of Health, and cycle information after pack replacement

The pack's internal BMS and the beltpack power architecture shall have clear responsibility boundaries. Pack protection functions are not unnecessarily reimplemented; required system-power functions on the carrier remain separate.

## Runtime and power budget

The final minimum energy requirement in Wh has not yet been defined.

**REVIEW:** The objective is useful professional shift runtime with the smallest reasonable device. Selection shall be based on a realistic power budget followed by measurements on the Radxa/carrier prototype, not on maximizing battery capacity.

For initial evaluation, two classes are particularly interesting:

- approximately **19 Wh** as an especially compact class
- approximately **25 Wh** as a compact class with additional runtime reserve

Larger packs remain possible but must justify their additional volume and weight through real product benefit.

## Reference candidate: vri BASE LINE

**CANDIDATE:** The vri BASE LINE from VRI GmbH Batterie-Technik in Ellwangen is being evaluated as the preferred reference candidate.

Based on currently published manufacturer information, two variants are particularly relevant:

### 1S/21700 — product 88054 201 512

- 3.60 V
- 5.30 Ah / approximately 19.1 Wh
- 79 × 22.50 mm
- SMBus
- 5-pin Molex Micro-Fit
- maximum charging current 5.15 A
- maximum discharge current 7.00 A
- NTC
- second protection
- 800 cycles at DOD 80% according to the manufacturer
- manufacturer lists UN38.3, IEC62133:2017, and UL62133

### 2S/18650 — product 88030 502 512

- 7.20 V
- 3.50 Ah / approximately 25.2 Wh
- 73 × 37.30 × 18.80 mm
- I²C
- 5-pin Molex Micro-Fit
- maximum charging current 3.38 A
- maximum discharge current 5.00 A
- NTC
- second protection
- 800 cycles at DOD 80% according to the manufacturer
- manufacturer lists UN38.3, IEC62133:2017, and UL62133

The final 1S versus 2S choice will explicitly not be based on capacity alone. Overall system power-conversion efficiency, required conversion topology, real load profiles, runtime, USB-host power reserve, thermal behavior, weight, volume, and serviceability must be evaluated together.

## Questions for the manufacturer discussion

The first technical discussion with VRI or another battery pack manufacturer should clarify at least the following:

1. Which existing standard pack is best suited to a long-lived portable communications product with our load profile?
2. Is 1S/21700 or 2S/18650 preferable at system level for this application, and why?
3. Which realistic continuous and peak load profiles does the manufacturer recommend or permit?
4. Which responsibilities are fully handled by the pack BMS and which charging/power-path functions must remain on the carrier?
5. How should simultaneous operation and charging be implemented electrically?
6. Which strategy does VRI recommend for frequent or continuous external-power operation and maximum battery lifetime?
7. Can reduced charge limits/Battery Care be implemented sensibly, and through which interface?
8. Which fuel-gauge/health/cycle data are available via SMBus or I²C and how are they documented?
9. How does the pack behave toward the host after physical replacement; are pairing, initialization, or special learning procedures required?
10. Is the existing pack mechanically suitable for regular end-user replacement, especially regarding connector, cable, strain relief, and mating cycles?
11. What requirements apply to mechanical mounting, shock/vibration protection, ventilation, and thermal environment?
12. Which complete test, transport, and conformity documents are supplied for integration into our end product?
13. What production availability, product-lifecycle commitments, MOQ, and volume pricing are possible?
14. How can spare-part availability be ensured over the required regulatory and commercial lifetime?
15. Can samples of the 1S/21700 and 2S/18650 variants be supplied for mechanical and electrical prototype testing?
16. If a standard pack is close but not ideal, which adaptations are possible without unnecessarily losing the advantages of an already developed and certified BASE LINE solution?

## Decision rule

The preferred battery pack is not the pack with the highest capacity. It is the smallest production-ready pack that, with sufficient margin, satisfies the beltpack's real electrical, thermal, runtime, serviceability, and lifetime requirements.

> **Battery capacity is a requirement, not a design goal. Product size, serviceability and reliable runtime are optimized together.**

## Sources / manufacturer information

The specific vri BASE LINE data must be verified against the current manufacturer datasheets and direct technical coordination with VRI before a production decision. Public product page: https://www.vri-gmbh.de/en/products-solutions/vri-base-line
