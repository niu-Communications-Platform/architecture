# Target Cost Model and Made-in-Germany Premise

[Deutsch — canonical](../../de/80-manufacturing/target-cost-model.md) | **English**

> The German version is canonical. This document is a maintained English translation.

## Purpose

This document defines the economic target-cost framework for the nıu Communications Platform beltpack. It is a target-cost model, not yet a supplier quotation.

## Manufacturing premise

**DECIDED:** `Made in Germany` shall be pursued as a hard premise for series manufacturing. Carrier PCBA, enclosure manufacturing, and final assembly/EOL should in particular be performed in Germany where economically viable. Individual components may be sourced internationally. Major manufacturing steps shall only be reconsidered after credible German quotations demonstrate that target price, quality, and margin cannot be achieved simultaneously.

## Sales and price

**CANDIDATE:** Current target selling price is **EUR 189 net**, or **EUR 224.91 gross** at 19% German VAT.

**DECIDED:** Direct-to-customer sales are the economic base case. Physical retail and classic distribution are not assumed. Any later indirect channel requires its own margin model.

## Margin definition and cost gates

| Gate | COGS | Gross margin at EUR 189 net | Meaning |
|---|---:|---:|---|
| **TARGET** | **≤ EUR 75** | **≥60.3%** | preferred development target |
| **ACCEPTABLE** | **>75 to 80** | **57.7–60.3%** | normal target range |
| **LIMIT** | **>80 to 94.50** | **50.0–57.7%** | economically possible, active optimization required |
| **FAIL** | **>94.50** | **<50%** | EUR 189 DTC target is not viable |

**DECIDED:** EUR 94.50 is the economic ceiling, not the sourcing budget. EUR 75–80 is the development range; ≤EUR 75 is preferred.

## Subsystem cost budgets

| Subsystem / cost block | Target EUR/unit | Rule |
|---|---:|---|
| **Compute** | **18–22** | Radxa ZERO 3W incl. suitable RAM/eMMC; >22 triggers review |
| **Carrier Core + Audio** | **13–17** | 2× codec, speaker amp, Secure Element, GPIO/PWM/NVM, clocking, major passives |
| **Power + USB** | **8–11** | charger/power path/DC-DC/monitoring, USB hub/host control, VBUS protection, ESD |
| **Human Interface + internal audio mechanics** | **7–10** | display, LEDs, controls, internal mics/speaker and related small parts |
| **External connectors / I/O mechanics** | **3–5** | audio, USB and power connectors plus justified I/O mechanics |
| **Carrier PCB + German assembly/AOI** | **6–9** | bare PCB plus SMT/THT manufacturing; DFM minimizes manual work |
| **Standard battery pack** | **12–16** | target for ~19 Wh class; supplier RFQ decisive; >18 triggers review |
| **Enclosure + clip + battery mechanics** | **5–8** | German production injection-moulding target; tooling NRE separate |
| **German final assembly + EOL + provisioning + packing** | **5–7** | requires DFMA and automated test |
| **Product packaging** | **2–3** | high-quality compact DTC packaging incl. insert/print |

These budgets are not independent worst-case ranges to be summed. They will progressively be replaced by real MPN, EMS, and supplier prices. A subsystem overrun must be visibly compensated elsewhere rather than silently increasing total COGS.

## Architecture cost-review rule

**DECIDED:** Cost control is part of architecture.

Every new hardware feature or relevant hardware change shall answer at least: incremental material cost at 1k/5k/10k; added PCB area/layers/connectors/cables/mechanics; added German manual assembly time; added EOL/calibration/service effort; whether it creates another product/manufacturing variant; which subsystem budget it consumes; and what measurable product value justifies the cost and complexity.

**Capability ≠ Feature** therefore also applies economically.

## Preliminary component anchors

Until RFQs are available: Radxa ZERO 3W target EUR 18–22; two TLV320AIC3204 roughly EUR 5–7 combined; Secure Element roughly EUR 0.6–1.0; speaker amp roughly EUR 0.7–1.2; Standard battery target EUR 12–16; packaging EUR 2–3. False cent-level precision is avoided until the schematic and MPN BOM exist.

## Reserve and complete series economics

Headroom between development target and the EUR 94.50 ceiling is not a free feature budget. It covers scrap/rework, test, warranty/RMA reserve, inbound freight/customs where relevant, manufacturing/packaging scrap, supplier variance, and second-source effects.

Fulfillment, DTC payment fees, shipping subsidies and similar selling costs remain visible in the unit-economics model even where accounting definitions do not classify all of them as manufacturing COGS. Tooling, certification and development/NRE are tracked separately, with an amortized full-cost view before series release.

## Enclosure

German custom injection moulding remains economically plausible; tooling is separate NRE. Prototype/pilot may use additive methods.

**DECIDED:** The main enclosure shall not be enlarged merely to accommodate a hypothetical largest Extended Battery Pack. Additional battery capacity should use the same beltpack hardware and, where possible, a pack geometry that protrudes farther externally.

## Packaging

**TARGET:** EUR 2–3 for a high-quality compact mostly paper/cardboard product package including insert and required printed materials. DTC shipping packaging is costed separately where required.

## DFMA rule for Made in Germany

> **Made in Germany becomes economical through Design for Manufacturing and Assembly, not by squeezing the manufacturer later.**

Architecture targets include few PCBs/cables, SMT over manual work where sensible, minimal hand soldering, keyed assembly, few fasteners, integrated enclosure functions where they eliminate assembly, automated EOL/provisioning, test points and Factory Mode from the start, low variant count, and no second beltpack manufacturing line for Standard versus Extended batteries.

## Cost maturity through the project

The model evolves from target costing to actual cost: architecture budgets → real schematic/MPN BOM → measured prototype/pilot assembly/test/rework → German supplier RFQs → pre-series landed COGS → series-release DTC unit economics including payment, fulfillment, warranty and an NRE-amortization view.

## Next cost gates

1. Fix Radxa RAM/eMMC series configuration and obtain manufacturer/distributor RFQ.
2. Ask VRI for 1k/5k/10k pricing for Standard and possible Extended battery family.
3. Convert Carrier architecture into a real MPN BOM and check it against subsystem budgets.
4. German EMS RFQ for 500/1k/5k/10k including material, AOI, test and box build.
5. German enclosure RFQ including tooling and 1k/5k/10k pricing plus assembly optimization.
6. Packaging RFQ at 1k/5k/10k including insert and shipping concept.
7. Update target-cost model after each RFQ.
8. Build complete DTC unit economics before series release.

## Gate

At EUR 189 net:

> **TARGET ≤EUR 75. ACCEPTABLE ≤EUR 80. LIMIT EUR 94.50. Above that, EUR 189 net is not viable at 50% gross margin.**

The Made-in-Germany premise remains economically viable while credible series quotations demonstrate manufacturing within this corridor with sufficient quality, warranty, and sourcing reserve.
