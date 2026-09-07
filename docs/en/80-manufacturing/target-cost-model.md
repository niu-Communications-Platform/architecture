# Target Cost Model and Made-in-Germany Premise

[Deutsch — canonical](../../de/80-manufacturing/target-cost-model.md) | **English**

> The German version is canonical. This document is a maintained English translation.

## Purpose

This document defines the first economic target-cost framework for the nıu Communications Platform beltpack. It is a target-cost model, not yet a supplier quotation.

## Manufacturing premise

**DECIDED:** `Made in Germany` shall be pursued as a hard premise for series manufacturing. In particular, Carrier PCBA, enclosure manufacturing, and final assembly/EOL should be performed in Germany where economically viable.

This does not require every component to originate in Germany. SBCs, semiconductors, displays, battery cells/packs, and other components may be sourced internationally. The objective is a credible German manufacturing and value-add architecture for the finished product.

Major manufacturing steps shall not be moved abroad reflexively for cost reasons. The premise will only be reconsidered if credible German quotations demonstrate that target price, quality, and margin cannot be achieved simultaneously.

## Sales and price

**CANDIDATE:** Current target selling price is **EUR 189 net**, or **EUR 224.91 gross** at 19% German VAT.

**Direct-to-customer sales are the economic base case.** Physical retail is not a fixed product requirement. Dealer/distributor margins are therefore excluded from the primary target-cost ceiling and require a separate channel model before indirect distribution is committed.

## Margin definition

The target is at least approximately **50% gross margin** on net DTC selling price.

At EUR 189 net:

- COGS ceiling at exactly 50% gross margin: **EUR 94.50**
- this is an economic ceiling, not a sourcing target
- internal COGS target: approximately **EUR 75–80**
- EUR 80 COGS yields EUR 109 gross profit / ~57.7% gross margin
- EUR 75 COGS yields EUR 114 gross profit / ~60.3% gross margin

The headroom to EUR 94.50 is required for real-world series variation and risk.

## Preliminary target-cost BOM

The following are engineering targets for four-digit series volumes and must ultimately be replaced by RFQs.

| Cost block | Target EUR/unit | Classification |
|---|---:|---|
| Radxa ZERO 3W, suitable RAM/eMMC configuration | 18–24 | public 1GB/8GB-eMMC pricing is already around USD 22; series RFQ required |
| 2× TLV320AIC3204 | 5–7 | current distributor 1k pricing roughly EUR 2.6–3.5 each depending on packaging |
| Secure Element | 0.6–1.0 | ATECC608 family volume pricing below EUR 1 publicly visible; final TrustFLEX profile open |
| Speaker amplifier | 0.7–1.2 | TAS2505 class |
| USB hub/host control, power switching, ESD | 3–5 | exact hub/Type-C/power path open |
| Power path, charger, DC/DC, monitoring | 4–7 | high uncertainty until battery pack is fixed |
| GPIO/PWM/NVM, clocking, passives | 2–4 | engineering allowance |
| 1.3–1.5 inch display | 2–4 | production LCD, not maker module |
| internal mics, speaker, LEDs, controls | 3–5 | engineering allowance |
| audio/USB/power connectors and mechanical small parts | 3–5 | engineering allowance |
| bare Carrier PCB | 1.5–3 | RFQ required |
| German SMT/THT assembly + AOI | 4–7 | RFQ required; DFM for automation |
| ~19 Wh production battery | 12–18 | target assumption only; VRI quotation decisive |
| injection-moulded enclosure + clip/battery mechanics | 5–9 | tooling NRE separate |
| German final assembly, EOL, provisioning, packing | 5–8 | highly dependent on DFMA and test automation |
| product packaging + cardboard insert/print | 2–3 | premium but material-efficient DTC packaging |
| **Target COGS** | **approx. 75–80** | overall target; upper bounds must not simply be summed |

## Why ranges must not simply be added

This is target costing, not a finished BOM. Several positions overlap or depend on open architecture choices. At design freeze, each item will be replaced by a concrete BOM/manufacturing line and the total must be driven against the EUR 75–80 target.

## Additional economic items

Series release must additionally account for scrap/rework, incoming/EOL testing, warranty/RMA reserve, inbound freight, customs where applicable, packaging/manufacturing scrap, fulfillment where used, DTC payment fees, and transparent treatment of tooling/NRE and certification/development costs.

## Enclosure

A custom injection-moulded enclosure manufactured in Germany appears economically plausible. Public German case studies show series prices in the low single-digit euro range at meaningful volumes, with five-digit tooling costs.

Prototype/pilot and series may use different manufacturing methods. Injection moulding is released only after sufficient mechanical validation.

## Packaging

Packaging is a real COGS item. Current German public examples at around 1,000 units show custom printed cardboard packaging in roughly the EUR 1–3 range depending on construction, before any additional insert elements.

**TARGET:** approximately **EUR 2–3** for a high-quality compact largely paper/cardboard product package including insert and required printed materials.

For DTC, the separate question of whether the product package itself is shippable or requires an outer shipping carton must also be costed.

## DFMA rule for Made in Germany

Made in Germany becomes economical primarily through **Design for Manufacturing and Assembly**, not by squeezing the manufacturer later.

Architecture targets therefore include few PCBs/cables, SMT over manual work where sensible, minimal hand soldering, keyed assembly, few fasteners, integrated enclosure functions where they remove assembly, automated EOL testing and provisioning, test points/Factory Mode from the start, low variant count, and no second beltpack manufacturing line for Standard versus Extended batteries.

## Distribution rule

**DECIDED:** The product is economically planned first as a direct-sales product. Physical retail or classic distribution is not assumed.

Future dealers remain possible, but any dealer channel receives its own margin model and must not silently be funded from the same EUR 189 DTC economics.

## Next cost gates

1. Fix Radxa RAM/eMMC series configuration and obtain manufacturer/distributor RFQ.
2. Ask VRI for 1k/5k/10k price tiers for Standard and possible Extended battery family.
3. Convert Carrier architecture into real MPN-level BOM as schematics mature.
4. German EMS RFQ for 500/1k/5k/10k including material, AOI, test and box build.
5. German enclosure RFQ including tooling and 1k/5k/10k unit prices plus assembly optimization.
6. Packaging RFQ at 1k/5k/10k including insert.
7. Update target-cost model after every RFQ.

## Gate

At EUR 189 net:

> **EUR 94.50 COGS is the 50% margin ceiling. EUR 75–80 is the development target.**

The Made-in-Germany premise remains economically viable while credible series quotations demonstrate that the product can be manufactured within this corridor with sufficient quality, warranty, and sourcing reserve.
