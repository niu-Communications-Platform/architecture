# Preliminary Costed Product-Core / Carrier BOM

[Deutsch — canonical](../../de/20-hardware/carrier-costed-bom.md) | **English**

> The German version is canonical. This document is a maintained English translation.

## Purpose

This document preserves the **architectural cost anchors of the shared nıu Product Core**. It is not the leading production BOM and does not replace the platform-specific costed BOMs in `product-development`.

With the split into **CM platform** and **Zero platform**, the model is now:

```text
Common Product Core
+
CM-specific carrier   OR   Zero-specific carrier
+
Compute
=
complete beltpack
```

Leading scenario costs live in:

- `product-development/bom/beltpack-costed-bom.md` — Common Core;
- `product-development/bom/beltpack-cm-platform-costed-bom.md` — CM;
- `product-development/bom/beltpack-zero-platform-costed-bom.md` — Zero.

## Shared core components with cost anchors

| Function | Candidate | Qty | Plan / anchor |
|---|---|---:|---:|
| Audio Codec | TLV320AIC3204IRHBR | 2 | **approx. EUR 5.2 total** |
| Speaker Amp | TAS2505IRGER | 1 | **approx. EUR 0.8** |
| Secure Element | ATECC608C-TFLXTLS class | 1 | **EUR 1.0 allowance** |
| Carrier EEPROM | 24CS64 class | 1 | **approx. EUR 0.3** |
| GPIO Expander | MCP23017 class | 1 | **EUR 1.0 allowance** |
| RGB LED Driver | PCA9955 class | 1 | **approx. EUR 1.1** |

Visible core-IC subtotal: roughly **EUR 9.4**. TrustFLEX production pricing remains RFQ.

## Shared functional blocks

| Product-Core block | Target/plan EUR | Note |
|---|---:|---|
| 2× Audio Codec | 5.2 | AIC3204 class |
| Speaker Amp | 0.8 | TAS2505 class |
| Secure Element | 1.0 | TrustFLEX class |
| NVM + GPIO + RGB PWM | 2.4 | EEPROM, expander, LED driver |
| Audio Analog Front End | 2.0–3.0 | bias, filtering, protection, detect/switching |
| USB-C Accessory Port Control | 1.5–2.5 | CC, VBUS limit, reverse protection, OCP, ESD |
| USB-C Power Input + protection | 0.8–1.5 | connector-side functions; charger separate |
| Power Path / Charger / DC-DC | 4.0–6.0 | final sizing must support CM/Zero peaks |
| Fuel/Power/Temperature Monitoring | 0.5–1.0 | where not fully provided by pack |
| Oscillators/Clocking | 0.3–0.7 | where product-wide |
| ESD/EMI/Protection | 1.0–1.8 | external audio/USB/power ports |
| general passives/regulators/glue | 2.0–3.0 | platform-neutral portion only |
| Test points / Factory interface | 0.5–1.0 | shared DFT hardware |

These are engineering anchors. The leading Common-Core BOM in product-development prevents double counting.

## No longer costed as one shared carrier block

The following are **platform-dependent** and must not be hidden inside one universal carrier budget:

- Compute Module / SBC;
- CM B2B or Zero 40-pin/SBC interconnect;
- compute→USB-hub/CT7601 data path;
- compute-specific power feed, boot/recovery and level/glue;
- compute mounting and internal keep-outs;
- carrier PCB;
- carrier PCBA/AOI;
- Zero/Pi-Zero-specific storage deltas.

### CM platform

Radxa CM3, Radxa CM4 and Raspberry Pi CM4 should, where possible, use the same identically populated CM carrier over the safe 2×100-pin intersection.

### Zero platform

Radxa ZERO 3W and Raspberry Pi Zero 2 W form the Zero family. A shared carrier is the target, but electrical identity is not fully validated yet; USB and storage differ in particular.

## USB lifecycle rule

An active USB hub may be required depending on platform. The specific USB2514BI remains unsuitable for a new production design because it is **NRND**.

**REVIEW:** Define an active, long-term-suitable USB2 hub/interconnect path per platform. Historical target for hub + clock/config: **about EUR 2.0–2.8** until concrete MPNs/topologies exist.

This amount is **no longer a Common-Core add-on**; it belongs in the corresponding platform BOM.

## HMI and mechanically stressed I/O

These product functions remain fundamentally shared:

| Block | Plan EUR |
|---|---:|
| 1.3–1.5 inch TFT | 2.0–3.5 |
| 4 RGB LEDs + light-guide share | 0.3–0.8 |
| PTT + buttons/encoder | 1.0–2.0 |
| internal microphones | 0.5–1.2 |
| internal speaker | 0.8–1.5 |
| MIC / PHONES / TRRS | 1.0–2.0 |
| visible 2× USB-C receptacles | 0.4–1.0 |

Internal compute mounting, internal cables/interconnect and PCB-specific mechanics belong in CM or Zero.

## PCB and German assembly

The previous generic targets remain only as plausibility anchors:

- bare carrier PCB: **EUR 1.5–3**;
- German SMT/THT assembly + AOI: **EUR 4–7**.

They are **not** added as a common cost block anymore. CM carrier and Zero carrier are routed, manufactured and quoted separately.

## DFMA rule

Every hand-soldered wire, extra cable, THT connector and second assembly side is German manufacturing time. Therefore compare not only part price but **Total Platform Assembly Cost**.

## Cost target

Complete-beltpack target remains:

- preferred total COGS: **≤EUR 75**;
- acceptable: **EUR 75–80**;
- >EUR 94.50 current fail territory.

The old simple carrier sum of EUR 36.5–52 must no longer be used as a platform-independent production number; it was an early broad architecture anchor that mixed blocks now separated into Common and Platform costs.

## Main cost risks

1. **Compute + platform integration** — now the strongest new difference between CM and Zero.
2. **Power** — must support peaks of the final compute family.
3. **USB** — especially a shared-carrier data path without compute rework.
4. **Mechanics/interconnect** — B2B versus SBC header/cable/mounting.
5. **Audio switching / CTIA-OMTP**.
6. **German assembly / EOL**.

## Gate

> **Optimize the Common Core jointly; cost CM and Zero separately to the same functional endpoint. No universal-carrier budget and no double counting.**
