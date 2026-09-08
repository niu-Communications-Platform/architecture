# 1S Power Architecture for Prototype 1

[Deutsch — canonical](../../de/20-hardware/1s-power-architecture.md) | **English**

> The German version is canonical. This document is a maintained English translation.

## Purpose

This document turns the preferred 1S direction for Prototype 1 into a testable power architecture. It is **not a series approval of individual ICs**. The architecture separates the production battery pack, USB-C POWER input, continuous stationary operation, regulated 5 V system power, and the ACCESSORY USB host port.

## Battery Pack ↔ Carrier responsibility boundary

**DECIDED:** nıu does **not** develop the Battery Pack or its internal Battery Management System (BMS). The beltpack uses a production-ready, documented battery pack from a specialist manufacturer. The pack remains an independent battery system with the protection, monitoring and fuel-gauge functions intended by its manufacturer.

> **The Battery Pack owns battery safety and cell management. The Carrier owns system power and charging integration. The Carrier must never substitute or bypass the Battery Pack's protection functions.**

The Battery Pack/manufacturer owns the cells and cell configuration, internal protection/BMS, cell over/undervoltage protection, pack over-current/short-circuit protection, internal temperature monitoring and protection limits, balancing where required, fuel-gauge/state data where provided, pack safety logic, allowed charge/discharge limits, and agreed pack compliance/transport/lifecycle documentation.

The nıu Carrier owns only device-side integration: USB-C input power and PD negotiation, system power path/load sharing, generation/distribution of system rails, ACCESSORY-port supply/protection, charging **within manufacturer-specified and approved limits**, reduction or pausing of charging based on available input/system state, battery-care product policy within approved limits, evaluation of pack-provided status/fuel-gauge/temperature information, and user/diagnostic presentation.

**DECIDED:** The Carrier must not replace or bypass pack protection. No bare cells as the regular product component, custom nıu cell protection/BMS, custom balancing, replacement cell-safety algorithms, bypass of pack over-current/temperature/voltage shutdowns, charge parameters outside manufacturer approval, or proprietary battery pairing merely for lock-in are part of the architecture.

The Carrier charger/power-path controller is therefore **not a substitute for the Pack BMS**. It is the controlled interface between external energy, system load, and the production battery pack.

The schematic is frozen only after pack-manufacturer coordination. VRI or the selected manufacturer must confirm charge termination voltage, allowed charge/discharge current, temperature limits, communications, pack shutdown behavior, and required host reactions. The same boundary applies to a Standard/Extended pack family: the Carrier may recognize approved packs and apply their approved parameters without becoming a battery-pack/BMS developer.

## System goals

- ~19 Wh 1S Standard Pack as preferred Prototype-1 candidate;
- POWER USB-C for power/charging only;
- separate ACCESSORY USB-C host port;
- robust regulated 5 V system rail for Radxa and major loads;
- ACCESSORY USB-C target around 5 V / 1 A;
- external operation while charging;
- operation without battery when external power is sufficient;
- weak supplies must not destabilize the product: system load takes priority and charging is reduced or paused;
- abrupt battery removal remains valid; no hot-swap bridge energy store;
- hardware hard-off independent of Linux;
- Power+USB architecture target remains EUR 8–11.

## Candidate block architecture

```text
POWER USB-C
    │
    ├─ ESD / protection
    ▼
USB-C Sink / PD Controller
    │   preferred: 5 V fallback + PD 9 V/12 V
    ▼
VBUS_IN
    │
    ▼
Buck-Boost Charger + NVDC Power Path
    ├──────────────► 1S Battery Pack
    │                 Pack BMS / Fuel Gauge
    ▼
SYS_BAT
    │
    ▼
Synchronous Boost 5V
    │
    ▼
5V_SYS
    ├─ Radxa ZERO 3W
    ├─ ACCESSORY USB-C VBUS via current-limited load switch
    ├─ Audio / speaker supply as required
    └─ local 3V3/1V8/etc. rails
```

**CANDIDATE:** Prototype 1 prefers this functional separation: USB-C negotiation, charging/power path, and regulated 5 V generation remain distinct responsibilities.

## USB-C POWER: PD is functionally justified

A 5 V-only input is possible but poorly matched to the simultaneous peak-load and charging case.

5 V / 3 A provides 15 W nominal input power, only slightly above the current ~13 W system+USB design case, leaving little practical charge headroom after conversion losses. 5 V / 1.5 A provides only 7.5 W, requiring battery supplement and reduced or paused charging under heavier loads.

**CANDIDATE:** The POWER port shall therefore support USB Power Delivery as a sink while retaining a robust 5 V fallback.

Preferred user behavior:

- **low-power 5 V USB-C:** operate as far as possible; charge rate limited or paused; battery may supplement;
- **5 V / 3 A:** normal operation possible, charge rate depends on system load;
- **USB-PD 9 V / 3 A or comparable:** preferred normal case for full operation plus useful charging power;
- **higher-power PD supply:** device requests only the profile it actually needs.

PD is therefore not introduced as a charging-speed gimmick, but to create clean headroom for full stationary operation plus charging.

## PD controller class

**CANDIDATE:** TI TPS25730A is a strong current reference candidate: sink-only, USB-IF PD3.2 certified, integrated protected power path, dead-battery support, up to 20 V / 5 A power path, pin-strap configuration, no external EEPROM or custom PD firmware required, and optional I²C diagnostics. It is not yet the selected production MPN.

## Charger / power path

**CANDIDATE:** A highly integrated wide-input buck-boost charger with NVDC power path shall be evaluated ahead of a simple 5 V-only 1S charger. TI BQ25798 is a reference candidate because it can handle 5 V fallback and higher PD input voltages while prioritizing system load.

Final charge settings must come exclusively from the selected production pack manufacturer's specification/approval. The charger is system-power/charging integration and never replaces the pack-internal BMS.

## 5V_SYS

The 1S/NVDC node does not remain at a stable Radxa/USB-compatible 5 V. A separate high-power synchronous boost stage therefore generates `5V_SYS`.

**CANDIDATE:** TPS61088 is a useful reference class. Prototype 1 shall validate stable 5 V across the allowed pack range, ~8 W internal design load, the ~13 W system+accessory stress case, load transients, thermal behavior, and audio/EMI impact.

## ACCESSORY USB-C

The ACCESSORY port remains electrically and functionally separate from POWER:

```text
5V_SYS
  │
  ▼
Current-limited / reverse-blocking load switch
  │
  ▼
ACCESSORY USB-C VBUS ~5 V / 1 A target
```

Requirements include host/DFP role, controlled current limit, over-current detection, reverse-current and ESD protection, software control/diagnostics where practical, and fault containment so a USB accessory cannot collapse the 5V_SYS rail.

## Battery-less operation

**REQUIREMENT:** With adequate external USB-C power, the beltpack must boot and operate with the battery removed.

## Weak-source behavior

Undersized supplies must not cause boot loops or unstable audio. Priority is active system load, stable 5V_SYS, ACCESSORY port according to policy, then remaining power to charging. Charging is reduced or paused as required.

## Power-off boundary

The architecture must support graceful Linux shutdown as the normal path and a long hardware hold (existing target ≥8 s) that can remove main power independently of Linux. Abrupt battery removal remains a valid hard-power-loss case.

## Preliminary cost

A capable 1S+PD architecture remains fundamentally compatible with the EUR 8–11 Power+USB target if duplicate functionality is avoided.

## Deliberately not included

- no custom battery pack/BMS;
- no custom cell protection or balancing;
- no bypass of pack-internal protection functions;
- no hot-swap bridge energy storage;
- no PD source function on POWER;
- no data on POWER;
- no universal 1S/2S circuit merely for theoretical flexibility;
- no second main 5 V supply just for ACCESSORY if a protected branch from 5V_SYS is sufficient;
- no proprietary charger or battery lock-in.

## Prototype-1 power gate

The 1S direction may only progress toward series after validating battery-only and battery-less operation, external-power/battery transitions, real-world 5 V fallback and PD supplies, simultaneous load+charge, efficiency and 5V_SYS regulation, ACCESSORY OCP, low-SoC behavior, thermal behavior, audio/EMI, hardware hard-off, abrupt battery removal/recovery, and **compliance with all charge/discharge/temperature limits of the selected production pack while preserving pack-internal protection functions**.

## Current direction

**CANDIDATE / PREFERRED FOR PROTOTYPE 1:**

```text
USB-C POWER Sink with PD + 5V fallback
        ↓
wide-input buck-boost charger / NVDC power path
        ↔ 1S production battery pack with own BMS/protection
        ↓
dedicated synchronous 5V boost
        ↓
5V_SYS
        ├─ Compute
        └─ protected 5V/1A ACCESSORY USB host
```

> **USB-PD is not a charging-speed gimmick for the beltpack. It creates power headroom for simultaneous full operation and charging while preserving 5 V USB-C as a compatible fallback.**

The battery responsibility boundary remains unchanged regardless of the specific power IC selection:

> **The Battery Pack owns battery safety and cell management. The Carrier owns system power and specification-compliant charging integration.**
