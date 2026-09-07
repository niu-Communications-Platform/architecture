# Supplier Briefing – Battery Pack / VRI

[Deutsch — canonical](../../de/80-manufacturing/supplier-briefing-battery-vri.md) | **English**

> The German version is canonical. This document is a maintained English translation.

## Purpose

This document prepares the initial technical and commercial discussion with **VRI GmbH Batterie-Technik, Ellwangen** for the nıu Communications Platform beltpack. It is not a final specification or purchase order. The goal is to identify a production-ready standard solution or minimally adapted battery family together with the battery manufacturer.

## Project in one sentence

nıu is developing a professional, compact portable IP intercom/audio beltpack with a rapid field-replaceable battery, USB-C external power and planned scalability into four- to five-digit unit volumes.

## Core premises

- nıu does **not** develop its own battery pack or pack-internal BMS.
- A production-ready, documented, long-term manufacturer solution is required.
- `Made in Germany` is a hard premise to pursue for the overall product; a German-developed/manufactured pack is particularly attractive.
- The complete pack is end-user replaceable within seconds.
- No hot-swap: battery removal may switch the beltpack off.
- The beltpack should remain as small as practical; approximately 120 × 80 × 35 mm is a maximum envelope, not a target volume.
- A Standard Pack around ~19 Wh is the current preferred candidate class, but not selected.
- An optional Extended Pack is attractive only if the same beltpack hardware and interface can be used.

## Current reference

The vri BASE LINE appears particularly interesting, including a compact 1S/21700 pack around ~19 Wh. A 2S pack remains relevant as an architecture comparison. VRI should explicitly recommend the best existing or production-near solution rather than merely confirm nıu's preliminary choice.

## Electrical load profile – current engineering state

The power budget is pre-Prototype-1 and therefore preliminary:

| Operating state | System power |
|---|---:|
| Listening / normal intercom | ~3.2 W |
| typical mixed use | ~3.8 W |
| heavy internal use | ~5.5 W |
| design peak without external USB accessory | ~8 W |
| design peak incl. up to ~5 W USB accessory | ~13 W |

The USB accessory peak is not the continuous load model for advertised battery runtime, but pack, converters, wiring and thermal design must accommodate it.

## Runtime direction

With a ~19.1 Wh pack and the current 85% usable-energy engineering model: approximately 5.1 h Listening at 3.2 W, 4.3 h typical mixed use at 3.8 W, and 3.0 h heavy internal use at 5.5 W. These are not product claims; Prototype 1 must measure actual consumption. Rapid battery replacement prioritizes operational availability over maximum single-pack runtime.

## Mechanical requirements

The complete pack should be end-user replaceable within seconds without opening the main enclosure; use robust keyed contact; support sufficient mating cycles for regular field replacement; be mechanically guided and protected against accidental release; require no proprietary specialist tool; and preferably support a common contact/latch zone for a larger capacity option.

VRI should advise whether a standard BASE-LINE connector is appropriate for frequent field replacement or whether the pack/device should use a robust docking/contact solution while retaining the internal pack connection.

## Standard + Extended

Preferred product direction: Standard Battery around 19 Wh; Extended Battery materially larger, roughly 30–35 Wh as an investigation range; same voltage class where sensible; same host pinout; same or compatible BMS/fuel-gauge communication; same contact/latch zone; larger pack may protrude farther; no second Carrier PCB, firmware variant or fundamental power architecture. If this creates meaningful system complexity, one optimal Standard Pack is preferred.

## Questions for VRI – technical

1. Which existing BASE-LINE pack does VRI recommend for this load profile, and why?
2. Is 1S sensible for the 5-V system/USB architecture or does VRI recommend 2S?
3. What continuous and peak currents should be assumed at low SoC and across temperature?
4. Which internal protection and second-level protection functions are present?
5. Which temperature information is available to the host?
6. Which BMS/fuel-gauge data is available through SMBus/I²C and how is it documented?
7. How should the host handle a newly inserted pack and health/learning state?
8. Which charging and Carrier-side charger/power-path architecture does VRI recommend?
9. Does VRI support/recommend charge limiting for stationary continuous operation and battery care?
10. Which thermal limits apply during simultaneous operation and charging?
11. Which contacts/connectors does VRI recommend for regular end-user replacement?
12. Which mating-cycle capability can be specified?
13. Is there an existing mechanical pack/enclosure solution, or should nıu design the outer battery receptacle?
14. Can a ~19 Wh Standard and ~30–35 Wh Extended family share host interface and contact zone?
15. Which external single/multi-pack charging solution does VRI recommend?

## Questions for VRI – compliance and lifecycle

16. Which certifications/evidence already exist for the recommended pack, especially UN 38.3, IEC 62133 and other relevant evidence?
17. What remains valid after minor mechanical/electrical adaptation and what must be retested?
18. Which documentation is supplied for device certification, transport, technical documentation and EU battery requirements?
19. What is the planned availability horizon of the pack/cell/BMS platform?
20. How are cell substitutions/obsolescence managed within a pack part number?
21. Which PCN/EOL processes are offered to series customers?
22. Can long-term spare-pack supply be contractually planned?

## Questions for VRI – commercial

For the recommended Standard and possible Extended Pack: sample/prototype pricing and availability; MOQ; 100-unit pilot indication; pricing at **1,000 / 5,000 / 10,000 units**; framework/call-off models; lead time and forecast requirements; adaptation NRE; tooling; certification/test costs; suitable single/multi-pack charger costs; and packaging/transport requirements for pack supply and spare-part sales.

## Target Cost

Current beltpack economics: total COGS development target EUR 75–80; Standard Battery Pack budget **EUR 12–16** at relevant series volume; **>EUR 18** triggers a cost/architecture review. This is an internal engineering target, not a supplier price entitlement. Quality, lifecycle, certification effort and system complexity are evaluated together with unit price.

## What should deliberately remain open

Do not prematurely prescribe 1S vs 2S, exact cell, exact BMS implementation, exact capacity, exact contact solution, or a mandatory Extended variant. nıu provides system requirements and target economics and wants to use the manufacturer's expertise.

## Desired outcome of the first discussion

Ideally establish: preferred existing/production-near Standard Pack; justified 1S/2S recommendation; mechanical concept for regular field replacement; feasibility of compatible Extended option; recommended charging/power-path interface; available BMS/fuel-gauge documentation; certification/lifecycle status; sample availability; MOQ/NRE/indicative 1k/5k/10k prices; and concrete next technical steps/contact persons.

## Suggested opening

> We are developing a professional IP intercom beltpack intended for long-term manufacturing in Germany. The complete certified battery pack should be replaceable by the user within seconds. We deliberately do not want to develop our own battery or BMS; instead, we want to integrate a production-ready VRI solution properly. A compact pack around 19 Wh currently looks interesting, but we want to hear your recommendation before fixing the power and mechanical architecture around it.
