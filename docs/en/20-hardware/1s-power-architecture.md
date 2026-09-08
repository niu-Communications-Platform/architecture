# 1S Power Architecture for Prototype 1

[Deutsch — canonical](../../de/20-hardware/1s-power-architecture.md) | **English**

> The German version is canonical. This document is a maintained English translation.

## Purpose

This document turns the preferred 1S direction for Prototype 1 into a testable power architecture. It is **not a series approval of individual ICs**. The architecture separates the production battery pack, USB-C POWER input, continuous stationary operation, regulated 5 V system power, and the ACCESSORY USB host port.

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

**CANDIDATE:** TI TPS25730A is a strong current reference candidate:

- sink-only;
- USB-IF PD3.2 certified;
- integrated protected power path;
- dead-battery support;
- up to 20 V / 5 A power path;
- pin-strap configuration;
- no external EEPROM or custom PD firmware required;
- optional I²C for status/diagnostics.

It is not yet the selected production MPN. STUSB4500, Infineon EZ-PD BCR and other active sink-only controllers remain comparison candidates.

## Charger / power path

**CANDIDATE:** A highly integrated wide-input buck-boost charger with NVDC power path shall be evaluated ahead of a simple 5 V-only 1S charger.

TI BQ25798 is a reference candidate because it supports 1S–4S, 3.6–24 V input, up to 5 A charging, integrated buck-boost conversion, BATFET/current sensing/NVDC power path, battery supplement, and ADC/I²C diagnostics.

For nıu, universal 1S–4S support is not the objective. The relevant capability is handling both 5 V fallback and higher PD input voltages while prioritizing the system load.

Final charge settings must come from the selected production pack manufacturer's specification/approval. nıu does not develop a pack BMS.

## 5V_SYS

The 1S/NVDC node does not remain at a stable Radxa/USB-compatible 5 V. A separate high-power synchronous boost stage therefore generates `5V_SYS`.

**CANDIDATE:** TPS61088 is a useful reference class: 2.7–12 V input, synchronous boost, high switch-current capability, 4.5–12.6 V output, adjustable current limit/frequency, and forced-PWM mode for EMI/audio evaluation. Newer alternatives such as TPS61288 and parts with explicit load disconnect are also evaluated.

Prototype 1 shall validate stable 5 V across the allowed pack range, ~8 W internal design load, the ~13 W system+accessory stress case, load transients, thermal behavior, and audio/EMI impact.

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

Prototype 1 must therefore validate the complete no-battery startup path:

`USB-C attach → PD/fallback → charger/power path → SYS_BAT → 5V_SYS → Radxa boot`.

This improves serviceability, stationary operation, and diagnostics.

## Weak-source behavior

Undersized supplies must not cause boot loops or unstable audio. Priority is:

1. active system load;
2. stable 5V_SYS;
3. ACCESSORY port according to policy;
4. remaining power goes to charging.

Charging current is reduced or paused as required. With a battery installed, temporary battery supplement may support load peaks.

## Power-off boundary

The architecture must support graceful Linux shutdown as the normal path, then disable the main 5 V rail after shutdown. A long hardware hold (existing target ≥8 s) must still be able to remove main power independently of Linux. Abrupt battery removal remains a valid hard-power-loss case.

The exact latch/power-button/load-switch IC is deferred to schematic design; the hardware property is the requirement.

## Preliminary cost

Current public 1k anchors are approximately:

- BQ25798: ~EUR 2.6;
- TPS61088: ~EUR 1.3;
- PD sink controller class: roughly EUR 1–2 as an early public anchor; TPS25730A needs a current series RFQ;
- plus magnetics, USB-C protection, load switches, current sensing, passives, and local regulators.

A capable 1S+PD architecture therefore still appears fundamentally compatible with the EUR 8–11 Power+USB target if duplicate functionality is avoided.

## Deliberately not included

- no custom battery pack/BMS;
- no hot-swap bridge energy storage;
- no PD source function on POWER;
- no data on POWER;
- no universal 1S/2S circuit merely for theoretical flexibility;
- no second main 5 V supply just for ACCESSORY if a protected branch from 5V_SYS is sufficient;
- no proprietary charger lock-in.

## Prototype-1 power gate

The 1S direction is only allowed to progress toward series after validating at least: battery-only boot/run; battery-less external-power boot/run; external-power↔battery transitions without unintended reset while battery remains installed; real-world 5 V fallback supplies; PD operation; simultaneous load+charge; limited-source behavior; efficiency at 3.2/3.8/5.5/8/13 W; 5V_SYS regulation/transients; ACCESSORY 0/0.5/1.0 A including OCP/short tests; low-SoC operation; thermal hotspots; audio/EMI under charging/boost/PD/USB load; hardware hard-off; and abrupt battery removal followed by defined reboot.

## Current direction

**CANDIDATE / PREFERRED FOR PROTOTYPE 1:**

```text
USB-C POWER Sink with PD + 5V fallback
        ↓
wide-input buck-boost charger / NVDC power path
        ↔ 1S production battery pack
        ↓
dedicated synchronous 5V boost
        ↓
5V_SYS
        ├─ Compute
        └─ protected 5V/1A ACCESSORY USB host
```

> **USB-PD is not a charging-speed gimmick for the beltpack. It creates power headroom for simultaneous full operation and charging while preserving 5 V USB-C as a compatible fallback.**
