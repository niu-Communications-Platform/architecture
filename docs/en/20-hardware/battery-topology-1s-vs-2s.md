# Battery System Topology: 1S vs. 2S

[Deutsch — canonical](../../de/20-hardware/battery-topology-1s-vs-2s.md) | **English**

> The German version is canonical. This document is a maintained English translation.

## Purpose

This document compares 1S and 2S Li-ion battery packs as system architectures for the beltpack. It is not yet a selection decision. Pack, charging, system power, USB host, efficiency, current, mechanics, cost and product variants are considered together.

## Known system requirements

Preliminary power budget: ~3.2 W listening, ~3.8 W mixed use, ~5.5 W heavy internal use, ~8 W internal design peak and ~13 W including up to ~5 W external USB accessory load. The Radxa/system requires a robust 5-V rail; ACCESSORY USB-C targets approximately 5 V/1 A host capability; POWER USB-C is separate; stationary power-path/load-sharing operation is required; battery replacement is rapid but not hot-swapped.

## Reference packs

VRI 1S/21700 88054 201 512: 3.60 V, 5.30 Ah, ~19.1 Wh, 79 × 22.5 mm, 7 A maximum discharge, SMBus.

VRI 2S/18650 88030 502 512: 7.20 V, 3.50 Ah, ~25.2 Wh, 73 × 37.3 × 18.8 mm, 5 A maximum discharge, I²C.

Both are reference candidates, not selected.

## 1S architecture

The central 5-V system rail must be boosted from the battery. Modern integrated 1S charger/power-path devices can combine charging, BATFET, NVDC power path and a substantial boost/OTG path. TI BQ25638 is a current example with up to 5-A charging, NVDC, I²C/ADC and boost output up to 9.6 V with programmable current limit up to 3.2 A. It is an architecture example, not a selected part.

Advantages: smallest current VRI reference pack; ~19 Wh fits the small-device-plus-spare-pack concept; no series-cell balancing; strong availability of integrated portable 1S power ICs; potentially one core boost topology for compute and USB host.

Risks: high battery current; 13 W is already ~3.6 A at nominal 3.6 V before losses; the complete 5-V rail depends on a high-performance boost stage; inductor/switch currents, layout, EMI and thermal performance are critical; low-SoC peak operation must be validated.

## 2S architecture

The 5-V rail is stepped down from the battery. Integrated 2S charger/power-path solutions also exist; TI BQ25883 is one example, with TI quoting 93.4% charging efficiency for 5-V input to a 7.6-V battery at 1 A. A substantial buck stage is normally also needed for the 5-V system rail.

Advantages: roughly half the battery current for equal power; comfortable peak-current reserve; efficient buck conversion to 5 V; lower current can reduce conductor and thermal stress.

Risks: current VRI 2S reference packs are materially larger; charging 2S from 5-V USB requires boost charging or a higher USB-PD input; an additional 5-V buck stage may add BOM and area; series-cell complexity remains part of the pack system; a common Standard/Extended family may be harder.

## Idealized current comparison

| System power | 1S @ 3.6 V | 2S @ 7.2 V |
|---|---:|---:|
| 3.2 W | 0.89 A | 0.44 A |
| 3.8 W | 1.06 A | 0.53 A |
| 5.5 W | 1.53 A | 0.76 A |
| 8 W | 2.22 A | 1.11 A |
| 13 W | 3.61 A | 1.81 A |

Low state of charge and conversion losses increase these currents, particularly for 1S.

## Efficiency and runtime

Topology alone does not determine runtime. Pack energy and the real converter efficiency curve over the actual duty cycle matter. The 25.2-Wh 2S reference pack has about 32% more nominal energy than the 19.1-Wh 1S pack; any runtime comparison must not mislabel this capacity difference as topology efficiency.

Prototype 1 shall measure pack-side input power and 5-V system power simultaneously.

## Cost

The topology is evaluated against the existing **EUR 8–11 Power+USB budget**. Current public pricing places a modern highly integrated BQ25638-class 1S charger/power-path IC around EUR 2.20 at 1k, so IC price alone does not decide the topology. Magnetics, external switches where required, USB-C/PD, protection, measurement, PCB area, thermal design and any additional 5-V converter stage must be costed together.

## USB-C POWER

The input-voltage strategy remains open. Evaluate 5-V-only operation, Type-C current advertisement without full PD, and USB-PD at 9 V or higher only if it materially improves charging, thermal or power-path behavior. Weak adapters must cause charge-current reduction before compromising system load. Operation from external power with an empty or removed battery is required.

USB-PD shall not be added merely because it is technically possible.

## Product-level comparison

| Criterion | 1S | 2S |
|---|---|---|
| Standard-pack compactness | **strong** | weaker |
| low battery current | weaker | **strong** |
| 5-V system rail | boost | buck |
| charging from 5-V USB-C | **simpler** | boost charger required |
| integrated portable power IC ecosystem | **very strong** | good |
| 13-W peak reserve | validation-critical | **more comfortable** |
| smallest standard beltpack | **strong** | weaker |
| cost potential | **good** | good, possibly more stages |
| Extended-pack family | ask VRI | ask VRI |

## Current direction

**CANDIDATE / PREFERRED FOR PROTOTYPE VALIDATION:** 1S is the preferred starting topology for Prototype 1 because the ~19-Wh VRI pack provides the strongest miniaturization opportunity and modern integrated power-path/boost solutions make the required performance fundamentally plausible.

This is **not a series decision**.

1S is reconsidered if prototype/RFQ work cannot achieve with reasonable margin: stable 5-V operation at low battery voltage; ~8-W internal peak; ~13-W system+USB design case; acceptable thermal behavior; acceptable EMI/audio noise; Power+USB BOM within EUR 8–11; useful efficiency across the main 3.2–5.5-W load range; and VRI approval for load/contact behavior.

## Prototype-1 measurement gate

Measure at minimum: 5-V regulation across pack voltage; efficiency at 3.2/3.8/5.5/8/13 W; low-SoC pack current; compute/Wi-Fi/audio/USB load steps; USB accessory at 0/0.5/1.0 A; simultaneous charging and system load; thermal hotspots; audio noise/EMI during boost operation; battery removal, external-power operation and restart behavior.

Only after these measurements is 1S or 2S selected for series architecture.
