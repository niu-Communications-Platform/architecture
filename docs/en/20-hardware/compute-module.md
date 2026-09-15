# Compute Platforms and Production Configuration

[Deutsch — canonical](../../de/20-hardware/compute-module.md) | **English**

> The German version is canonical. This document is a maintained English translation.

## Purpose

This document defines the stable hardware boundary between the nıu Product Core and replaceable compute hardware. The concrete production platform remains open; two platform families are actively compared.

## Architecture

**DECIDED:** Compute is not the Device Identity anchor. The nıu carrier owns Device Identity, Secure Element, audio, power, HMI, resilience RF and product-specific hardware. Compute remains replaceable processing, storage and networking hardware.

**DECIDED:** Two active compute/carrier families are used for production evaluation:

```text
nıu Product Core
        │
        ├── CM carrier
        │   ├── Radxa CM3
        │   ├── Radxa CM4
        │   └── Raspberry Pi CM4
        │
        └── Zero carrier
            ├── Radxa ZERO 3W
            └── Raspberry Pi Zero 2 W
```

It is **not yet decided** which family and which concrete standard module will win production.

## Standard-SKU rule

**DECIDED:** Production architecture uses only regular, unmodified standard SKUs.

Excluded as required production prerequisites are:

- customer-specific compute modules;
- vendor special variants created only for nıu;
- resistor/solder rework on purchased SBCs;
- compute-specific changes that undermine repairability and open procurement.

## CM platform

Candidates:

- Radxa CM3;
- Radxa CM4;
- Raspberry Pi CM4.

**TARGET:** One identically populated CM carrier should support all three modules through the verified safe 2×100-pin intersection.

Rules:

- use only F-015-verified common pins for mandatory functions;
- the third Radxa connector carries no mandatory nıu baseline function;
- compute-specific BSPs, device trees and recovery procedures are acceptable;
- compute-specific carrier population variants should be avoided.

Radxa CM3 has a written vendor availability commitment through at least September 2033. Raspberry Pi CM4 is announced through at least January 2034. Lifecycle alone therefore does not currently decide between those two candidates.

## Zero platform

Candidates:

- Radxa ZERO 3W;
- Raspberry Pi Zero 2 W.

Both belong to the 65×30-mm Zero class with a 40-pin expansion footprint/class. This defines a common platform family but does not yet establish full electrical drop-in compatibility.

**TARGET:** One shared Zero carrier with as much identical population as practical.

Still to validate:

- mechanical hole/keep-out compatibility;
- safe shared 5 V/GPIO/I²C/SPI/UART intersection;
- USB interconnect;
- storage/recovery;
- power/shutdown;
- actual carrier-BOM identity.

On Radxa ZERO 3W, the 40-pin USB2 route must not be assumed as a production solution when it requires board rework. Raspberry Pi Zero 2 W normally exposes USB OTG through Micro-USB. The Zero platform therefore needs a standard-SKU-compatible shared USB strategy.

## Storage

### CM

Depending on the standard SKU, onboard eMMC is available and is generally preferred for a long-lived Linux product with A/B OTA, recovery and diagnostics.

### Radxa ZERO 3W

Onboard eMMC is available in standard SKUs and remains the preferred runtime-storage path for this candidate.

### Raspberry Pi Zero 2 W

Pi Zero 2 W has no onboard eMMC and normally uses microSD. If it remains a production candidate, this becomes its own architecture gate:

- qualified production-grade microSD **or** alternative external storage;
- A/B OTA, rollback and recovery;
- hard-power-loss tolerance;
- write-load/endurance strategy.

The prior blanket rule “microSD is not a production runtime medium” therefore no longer applies across all platforms without validation; for the Pi-Zero subvariant it must be confirmed or changed based on evidence.

## RAM / compute rule

Compute is optimized for sufficient product headroom, not maximum specification and not minimum purchase price.

At minimum measure:

1. RAM after boot;
2. RAM with the full Talkkonnect/PipeWire/nıu service stack;
3. peak RAM during network switching, audio, UI, diagnostics and OTA;
4. storage occupancy and A/B/recovery reserve;
5. boot/recovery time;
6. idle/listening/TX/RX/heavy-load power;
7. target-enclosure thermals;
8. hard power loss including cuts during OTA/config writes.

Special gates:

- 1-GB CM configurations;
- ZERO 3W 1/2-GB tradeoff;
- Raspberry Pi Zero 2 W with **512 MB** RAM.

## Cost model

There is no longer one abstract shared compute unit cost. Production economics are calculated per platform to the same functional endpoint:

```text
Common Product Core
+
CM-specific carrier/interconnect/PCB/PCBA
+
CM candidate
```

versus

```text
Common Product Core
+
Zero-specific carrier/interconnect/PCB/PCBA
+
Zero candidate
```

The authoritative scenario-cost source is `product-development/bom/`.

## Decision rule

> **First choose the better platform family; then, within that family, choose the smallest standard SKU that credibly satisfies functionality, headroom, lifecycle, repairability and supply requirements.**

A universal PCB carrying both CM and Zero footprints is not the goal. The target is two possible carrier variants with a maximally shared Product Core.

## Links

- Product-development Q-002: CM versus Zero platform
- Product-development Q-005 / F-015: CM shared-carrier compatibility
- Product-development Q-007: Zero shared-carrier compatibility
- Product-development BOM: Common Core + CM platform + Zero platform
