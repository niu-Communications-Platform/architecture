# Preliminary MPN-Level Power BOM

[Deutsch — canonical](../../de/20-hardware/power-mpn-bom.md) | **English**

> The German version is canonical. This document is a maintained English translation.

## Purpose

This document translates the preferred Prototype-1 1S power architecture into concrete component classes and reference MPNs. It is **not a production BOM or component approval**. The goal is to expose cost, functional overlap, development risk and prototype sourcing early.

The responsibility boundary remains unchanged: the production-ready Battery Pack owns its BMS/protection/fuel gauge; the Carrier owns system power and specification-compliant charging integration.

## Architecture

```text
POWER USB-C
  ↓
ESD / Type-C / PD Sink
  ↓
wide-input buck-boost charger + NVDC power path
  ↔ production-ready 1S Battery Pack with own BMS
  ↓
SYS_BAT
  ↓
dedicated synchronous boost
  ↓
5V_SYS
  ├─ Compute / Carrier
  └─ protected ACCESSORY USB-C 5 V / ~1 A
```

## Prototype-1 reference MPNs

| Function | Reference MPN | Status | public 1k anchor* | Note |
|---|---|---|---:|---|
| USB-C PD Sink / POWER port | TI TPS25730SRSMR / TPS25730A class | CANDIDATE | ~EUR 1.30 | stand-alone sink/protected power path; exact A variant/package to verify |
| Charger + NVDC Power Path | TI BQ25798RQMR | CANDIDATE | ~EUR 2.61 | used for 1S device integration, not as Pack BMS |
| 5V_SYS Boost | TI TPS61088 class | CANDIDATE | ~EUR 2.9–3.8 depending variant/tier | higher than earlier assumption; alternatives require active comparison |
| ACCESSORY VBUS current limit | TI TPS2553DBVR class | REFERENCE | ~EUR 0.47 | current limit/OCP; reverse-current requirement to verify separately |
| USB-C / ESD / CC / protection | open | ALLOWANCE | ~EUR 0.4–0.8 | final protection depends on PD/connector selection |
| Charger/boost magnetics | open | ALLOWANCE | ~EUR 0.8–1.5 | current, DCR, saturation, EMI and height matter |
| Sense/filter/power passives | open | ALLOWANCE | ~EUR 0.5–1.0 | shunts, capacitors, resistors, filtering etc. |

\* Public distributor pricing is an engineering anchor, not an RFQ or guaranteed production price.

## First cost assessment

```text
PD Sink                     ~EUR 1.3
Charger / Power Path        ~EUR 2.6
5V Boost                    ~EUR 2.9–3.8
Accessory protection        ~EUR 0.5
Protection / ESD            ~EUR 0.4–0.8
Magnetics                   ~EUR 0.8–1.5
Power passives              ~EUR 0.5–1.0
-------------------------------------
Engineering range           ~EUR 9.0–12.0
```

The first MPN-near view therefore sits **at or slightly above** the previous EUR 8–11 Power+USB target. This is not an architecture failure, but it is a real cost gate.

## Key new finding

The earlier ~EUR 1.3 TPS61088 anchor was too optimistic for currently easy-to-source standard variants. Current public tiers are closer to roughly EUR 2.9 at larger reel quantities and up to about EUR 3.8 for some variants at 1k.

**REVIEW:** The 5V_SYS converter becomes the primary cost/efficiency optimization point. Production selection shall compare TPS61088 and newer TI alternatives, established competing vendors, actual continuous/peak requirements, integrated vs external MOSFETs, efficiency at 3.2–5.5 W, low-SoC 8/13-W behavior, inductor size/height, forced-PWM/audio EMI behavior, 1k/5k/10k RFQ price and lifecycle.

Saving EUR 1–2 here matters, but not at the expense of thermal margin, audible switching noise or peak capability.

## Avoid duplicate functionality

The BOM shall explicitly avoid duplicated functions: do not duplicate the PD controller's protected power path unnecessarily; use charger measurement where sufficient; do not rebuild the Pack fuel gauge on the Carrier; never replace Pack protection; keep ACCESSORY protection proportional to the 5 V/~1 A requirement; and do not create a separate second 5 V main supply solely for ACCESSORY.

## Not yet fully included

This early BOM does not yet fully price exact USB-C connectors, exact inductors, all capacitors/derating, hardware power latch/hard-off, any required ideal-diode/reverse-blocking function, pack contact solution, PCB copper/thermal cost, VRI-specific host interface/protection, or local 3V3/1V8 rails where these belong to Carrier Core.

## Sourcing/lifecycle

BQ25798 is currently active and publicly well stocked, but distributors report manufacturer lead times of multiple months for quantities beyond stock. Production MPNs therefore require lifecycle, forecastability and manufacturer-support review in addition to unit price.

## Prototype-1 recommendation

Prototype 1 should initially use well-documented reference components even if they are not yet the cheapest production solution. It exists to validate the 1S architecture, stable 5V_SYS, PD+charging+load behavior, battery-less operation, the 13-W stress case, audio integrity and thermal performance. Production cost optimization follows only after those properties are measured.

> **Prototype 1 optimizes learning. The production BOM optimizes cost without losing the validated safety, audio and power properties.**

## Cost gate

**TARGET:** Power+USB remains ≤EUR 11 in production costing, preferably EUR 8–10.

**REVIEW:** If credible 5k/10k RFQs remain above EUR 11 after component optimization, first optimize the 5 V boost, PD/protection integration and magnetics. The Battery Pack/BMS responsibility boundary shall **not** be weakened for cost reduction.
