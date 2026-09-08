# Mechanical I/O Series Candidates

[Deutsch — canonical](../../de/20-hardware/mechanical-io-series-candidates.md) | **English**

> The German version is canonical. This document is a maintained English translation.

## Purpose

This document translates the mechanical I/O strategy into concrete candidate classes for Prototype 1 and later series production. It is **not a production release**. Mechanical controls and connectors are selected not only by unit price and electrical function but by lifetime, enclosure integration, repairability, assembly effort, haptics, and field-failure risk.

## For non-electrical engineers

A connector or switch can look trivial on a schematic. In the finished consumer product it is often among the most mechanically stressed parts. A good 50-cent connector can be economically better than a 20-cent connector if it simplifies enclosure design, assembly, and warranty handling.

A **mating cycle** is one complete connection and disconnection. 10,000 mating cycles are therefore a concrete durability specification.

## USB-C POWER

### Reference candidate: GCT USB4085

The USB4085 is a strong mechanical reference candidate for Prototype 1 POWER:

- USB Type-C, USB 2.0 / 16 contacts
- horizontal top mount
- through-hole/shell anchoring for strong PCB retention
- 5 A rating
- manufacturer currently specifies up to 20,000 mating cycles
- compact profile
- public drawings, footprints, and specification

POWER does not require high-speed data. A mechanically robust Type-C receptacle with only the contacts actually required is therefore preferable to unnecessary USB 3.x complexity.

**CANDIDATE:** USB4085 class for POWER. Exact variant and availability must be checked before schematic freeze.

## USB-C ACCESSORY

ACCESSORY is a real USB host port and needs at least USB 2.0 data plus 5 V supply. A 16-contact USB 2.0 Type-C port is fundamentally sufficient if DFP/host operation, CC circuitry, and electrical architecture are implemented correctly.

USB4085 is therefore also an interesting mechanical reference candidate here. Two identical receptacles could simplify BOM, footprint, procurement, and repair. The enclosure and labeling must nevertheless distinguish the ports clearly.

Whether POWER and ACCESSORY actually use the same receptacle remains an integration decision.

## 3.5 mm audio jacks

### Reference class: Kycon STX-3500 / robust PCB audio jacks

The Kycon STX-3500 family provides a useful reference level:

- 3.5 mm
- SMT
- 3/4/5-pin variants
- 5,000 mating cycles specified
- defined insertion/extraction forces
- documented contact resistance before/after durability testing

For nıu.cp, 5,000 cycles are initially a **reference, not an automatically accepted production target**. PHONES/TRRS may be connected frequently in production use, and lateral cable loads matter.

Where possible, jacks should be mechanically supported by the enclosure or strong PCB anchors. Solder joints should not alone carry the lever load of an inserted 3.5-mm plug.

Prototype testing must include mating, cable leverage, belt use, shock/drop scenarios, and wear.

## PTT

PTT is not an ordinary menu button. It is one of the primary wear and haptic components.

### Reference family: Alps Alpine SKRA

The SKRA family demonstrates that compact SMT tactile switches are available with IP6X/IPX7-like component-level specifications and very high operating life. Depending on variant, Alps Alpine specifies 100,000 to several million operations; some current variants reach 2–5 million cycles.

PTT should therefore target **at least several hundred thousand real operations**, preferably a million-cycle class where haptics, price, and mechanics permit.

A component-level IP rating does not automatically make the complete beltpack waterproof.

PTT must be validated as a system for operating force, gloves, tactile point, long holds, rapid repeats, accidental belt activation, structure-borne noise into the internal microphone, enclosure actuator/membrane behavior, aging, and left/right-hand use.

## Battery: not a normal cable connector as the user interface

The VRI reference packs use an industrial 5-pin Molex Micro-Fit interface. This may be suitable internally or pack-side, but a user changing a battery in seconds should probably **not manually grip and disconnect a small cable connector each time**.

### Preferred concept

A guided Battery Dock:

1. The battery enters a defined mechanical guide/pocket.
2. Enclosure mechanics provide alignment and keying.
3. Spring/high-cycle contacts automatically connect power and, where required, communication/temperature signals.
4. A latch carries mechanical retention; electrical contacts do not carry retention loads.
5. Removal separates contacts in a controlled way without pulling cables.

TE Connectivity offers direct-to-PCB battery terminals tested to 10,000 mating cycles; Molex also documents battery contact systems at 10,000 cycles. These classes demonstrate that a high-cycle dock is realistic.

### No premature commitment to pogo pins

A `pogo pin` is a spring-loaded pin contact. It is intuitive and potentially attractive, but we do **not** commit to it. Leaf-spring/multipoint contacts may be superior in current capability, contamination tolerance, mechanical tolerances, height, or cost.

The Battery Dock must be developed jointly with VRI and mechanical engineering. The pack manufacturer must confirm required power, NTC, SMBus/I²C, and other contacts as well as pack behavior during connection/disconnection.

### Battery Dock gates

- ≥10,000 mechanical replacement cycles as development target
- sufficient current for real worst-case and transient loads
- contact resistance and heating
- polarity safety
- no accessible-contact short-circuit hazard
- defined contact sequencing where electrically required
- tolerance compensation
- dirt/dust/sweat
- drop and vibration
- no retention loads through electrical contacts
- tool-less replacement within seconds
- battery cannot fall out accidentally
- contacts inspectable/cleanable or serviceable

## Display connection

A FFC/FPC connection remains sensible for the small TFT. **FFC/FPC** refers to a flat flexible cable and its small connector. The display should be replaceable as an assembly rather than soldered directly to the Carrier.

Selection criteria include a standard pitch where practical, connector locking, defined service-cycle count, strain-free cable routing, display replacement without Carrier rework, and service-friendly connector placement.

## Selection principle

> **We do not buy the cheapest contact. We buy a defined lifetime and integrate it so that the mechanics do not amplify its weaknesses.**

## Prototype 1 recommendation

1. Initially design POWER and ACCESSORY around robust, well-documented USB-C receptacles in the USB4085 class.
2. Source 3.5-mm jacks from a professional lifetime-specified family and mechanically test them.
3. Prototype PTT with at least two operating-force/mechanical variants; Alps SKRA as reference family.
4. Do **not** freeze the Battery Dock as manual Micro-Fit mating. Clarify requirements with VRI and mechanically prototype two contact concepts.
5. Make the display pluggable using a locking FFC/FPC connector.
6. Before production freeze, create a dedicated Mechanical I/O life test plan with automated PTT and mating-cycle testing.

## Open items

- exact 3.5-mm MPNs for MIC/PHONES/TRRS
- exact USB4085 variants and footprint integration
- complete enclosure IP/sealing concept
- PTT force and key geometry
- Battery Dock contact manufacturer and geometry
- VRI pack contact sequencing
- display MPN and FPC pinout
- 1k/5k/10k pricing and long-term availability
