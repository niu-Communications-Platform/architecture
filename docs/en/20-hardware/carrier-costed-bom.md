# Preliminary Costed Carrier BOM

[Deutsch — canonical](../../de/20-hardware/carrier-costed-bom.md) | **English**

> The German version is canonical. This document is a maintained English translation.

## Purpose

This document provides the first quantitative check whether the planned beltpack Carrier architecture is plausible within the target-cost model. It is **not yet a released production BOM**. Some MPNs are candidates; open functions use engineering allowances.

## Result in one sentence

**The planned Carrier architecture appears economically plausible.** The core ICs with currently visible pricing are not the main cost driver. The largest risks are power/USB, mechanics/connectors, PCB/assembly and still-open detail components.

## Scope

Included: Carrier electronics, Carrier PCB and German assembly/AOI. Excluded: Radxa compute module, battery pack, main enclosure, product packaging and German box-build final assembly.

## Core components with current price anchors

| Function | Candidate | Qty | Public price anchor | Plan/unit |
|---|---|---:|---:|---:|
| Audio Codec | TLV320AIC3204IRHBR | 2 | approx. EUR 2.57 each at 1k | **EUR 5.2** |
| Speaker Amp | TAS2505IRGER | 1 | approx. USD 0.87 at 1k at DigiKey | **EUR 0.8** |
| Secure Element | ATECC608C-TFLXTLS | 1 | production variant requires RFQ; generic ATECC608B family roughly EUR 0.65–0.85 publicly | **EUR 1.0 allowance** |
| Carrier EEPROM | 24CS64 class | 1 | around EUR 0.3 even in low quantity | **EUR 0.3** |
| GPIO Expander | MCP23017 class | 1 | around EUR 1.45 single quantity; volume open | **EUR 1.0 allowance** |
| RGB LED Driver | PCA9955BTWJ or equivalent | 1 | approx. EUR 1.08 at 1k | **EUR 1.1** |

Visible core-IC subtotal: approximately **EUR 9.4**.

TrustFLEX production pricing requires RFQ. Generic ATECC608 pricing is only a plausibility anchor, not a quotation for the provisioned TrustFLEX device.

## USB architecture lifecycle warning

USB 2.0 hub controllers in the USB2514B cost class are only a few euros, but the specific USB2514BI is listed **NRND (Not Recommended for New Designs)** and is therefore not adopted as a production decision.

**REVIEW:** Select an active, long-term-suitable USB 2.0 hub controller for Prototype 1/series. Target for hub controller plus required clock/config components: **≤EUR 2.5** at production volume.

## Functional blocks and engineering allowances

| Carrier block | Target/plan EUR | Content |
|---|---:|---|
| 2× Audio Codec | 5.2 | AIC3204 class |
| Speaker Amp | 0.8 | TAS2505 class |
| Secure Element | 1.0 | TrustFLEX class, RFQ open |
| NVM + GPIO + RGB PWM | 2.4 | EEPROM, expander, LED driver |
| Audio Analog Front End | 2.0–3.0 | bias/filter/protection/switching/detect/CTIA-OMTP as required |
| USB Hub + Clock/Config | 2.0–2.8 | final active hub open |
| USB-C Accessory Port Control | 1.5–2.5 | DFP/CC, VBUS current limit, reverse protection, OCP, ESD |
| USB-C Power Input + protection | 0.8–1.5 | connector-side functions; charger separate |
| Power Path / Charger / DC-DC | 4.0–6.0 | strongly dependent on final 1S/2S battery architecture |
| Fuel/Power/Temperature Monitoring | 0.5–1.0 | where not provided by pack |
| Oscillators/Clocking | 0.3–0.7 | as required |
| ESD/EMI/Protection total | 1.0–1.8 | external audio/USB/power ports |
| Passives/Regulators/Level Shifting/Glue | 2.0–3.0 | aggregate allowance |
| Test points/Factory interface/small connectors | 0.5–1.0 | DFT hardware |

### Electronics subtotal

Current anchors and allowances produce an engineering range of roughly **EUR 24–30** for Carrier electronics excluding display, mechanical controls, acoustic transducers, external connectors and PCB manufacturing.

## Human interface and mechanically stressed I/O

| Block | Plan EUR |
|---|---:|
| 1.3–1.5 inch TFT | 2.0–3.5 |
| 4 RGB LEDs + light-guide share | 0.3–0.8 |
| PTT + buttons + encoder | 1.0–2.0 |
| internal microphones | 0.5–1.2 |
| internal speaker | 0.8–1.5 |
| MIC / PHONES / TRRS jacks | 1.0–2.0 |
| 2× USB-C receptacles | 0.4–1.0 |
| other internal connectors | 0.5–1.0 |

Current broad range: **EUR 6.5–13**.

## PCB and German assembly

Current gate: bare Carrier PCB **EUR 1.5–3**, German SMT/THT assembly + AOI **EUR 4–7**, combined target **EUR 6–9**. Real quotation requires stackup, dimensions, assembly sides, component count and THT content.

DFMA matters because every hand-soldered wire, additional THT connector and second assembly side costs German manufacturing time as well as BOM money.

## Consolidated Carrier view

1. Core Carrier Electronics: **EUR 24–30** engineering estimate.
2. HMI / Audio Mechanics / External Connectors: **EUR 6.5–13**.
3. Carrier PCB + German PCBA: **EUR 6–9** target.

Simple broad sum: **EUR 36.5–52**. The upper end exceeds the previous aggregate target and therefore identifies where the architecture now needs concrete optimization. It is not an alarm: several upper bounds are conservative allowances and overlap will be resolved by the schematic.

## Schematic-phase target

- Carrier Electronics incl. Power/USB/Audio/Security: **≤EUR 27**;
- HMI + Audio Mechanics + External Connectors: **≤EUR 10**;
- PCB + German PCBA/AOI: **≤EUR 8**;
- Carrier-adjacent hardware total: **≤EUR 45**, preferably **≤EUR 42**.

## Main cost risks

1. **Power architecture:** 1S vs 2S, simultaneous charge/use, 5V system rail and 5V/1A USB host materially affect converters, thermal design and BOM.
2. **USB:** universal external host must not become a collection of redundant controllers.
3. **Audio switching / CTIA-OMTP:** flexibility may cost more in switches/detection/protection than the codecs themselves.
4. **Mechanical connectors and assembly:** low component prices can hide substantial mounting, cable and manual-labor cost.
5. **Variants:** unpopulated reserves are cheap; product variants are expensive.

## What is surprisingly inexpensive

Two audio codecs are only about a EUR 5 volume block. Secure Element, EEPROM, GPIO expander and RGB LED driver are also not economic showstoppers.

> **Do not damage good audio, identity or diagnostic architecture to save cents. Optimize the large and labor-intensive blocks first.**

## Next steps

1. VRI discussion/RFQ to narrow pack voltage class.
2. Compare 1S and 2S power trees at block/BOM level.
3. Select an active USB hub candidate; no NRND component for a new production architecture.
4. Define USB-C host power/CC architecture.
5. Define audio jack/CTIA/OMTP circuit.
6. Convert display, controls, mics, speaker and connectors to real MPNs.
7. Check first KiCad BOM against **≤EUR 42–45 Carrier-adjacent hardware**.
8. Prepare German EMS RFQ.

## Gate

> **The architecture is currently cost-plausible, but the Carrier has no unlimited reserve. From now on every additional hardware feature must justify its budget.**
