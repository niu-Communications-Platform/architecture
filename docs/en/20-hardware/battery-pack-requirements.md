# Production Battery Pack Requirements

[Deutsch — canonical](../../de/20-hardware/battery-pack-requirements.md) | **English**

> The German version is canonical. This document is a maintained English translation.

## Principle

**DECIDED:** nıu will not develop battery cells, the battery pack, or its internal BMS. The product shall use a production-ready documented pack from a specialized manufacturer. The carrier only provides the required system integration.

## Product and mechanical objective

The beltpack is a professional portable IP intercom/audio device. The previously discussed approximately **120 × 80 × 35 mm is a maximum envelope, not a volume to be filled**. The product shall become as compact as reasonably possible while preserving robustness, serviceability, thermal manageability, and usability.

## Rapid field-replaceable battery

**DECIDED:** The complete pack is not merely regulatorily replaceable but is intentionally designed as a **rapid field-replaceable battery** and professional product feature.

> **Optimize for operational availability, not maximum battery capacity.**

The target is replacement within a few seconds without opening the main enclosure, using a robust latch, secure guidance, keyed contacts, and protection against accidental release. Spare packs and external single-/multi-pack charging solutions shall be possible.

### No hot swap

**DECIDED:** Uninterrupted operation during battery replacement is not supported. Without external power, the device may power off when the pack is removed. Seconds-scale energy buffering or a second energy store will not be added for this purpose. Small hold-up capacitance for electrical stability remains permitted.

### Abrupt battery removal

**DECIDED:** Battery removal without prior software shutdown is an allowed operating condition. The system must tolerate repeated hard power loss. Critical persistent state, provisioning, and A/B OTA must be power-loss safe; unnecessary flash writes are minimized; Device Identity does not depend solely on SBC storage. After restart the device autonomously returns to a defined state. This shall be validated repeatedly in practice.

## Capacity family without beltpack variants

**DECIDED:** Where practical, the battery interface shall support multiple capacity classes **without creating different beltpack hardware variants**. More capacity is a battery option, not a second beltpack variant.

The target is one beltpack with identical carrier, firmware, and main-enclosure architecture. A compact standard battery may be included with the product; a substantially higher-capacity battery may be offered as an accessory if this can be achieved without relevant additional system complexity.

Design objectives for such a pack family:

- same electrical host interface and pinout;
- preferably the same voltage class and fundamental power architecture;
- same or compatible communication/fuel-gauge model;
- same mechanical contact and latch zone;
- automatic correct handling of different capacities without firmware variants;
- no different carrier PCB or beltpack SKU merely because of battery capacity;
- a larger pack may protrude further rather than forcing the main device to be sized for the largest battery;
- **supporting an Extended Pack must not unnecessarily increase beltpack dimensions when the Standard Pack is installed.**

**CANDIDATE:** A standard pack around **19 Wh** is currently particularly interesting because of its compactness. The next larger 25 Wh class is not automatically the optimal optional Extended Pack. A more substantial capacity increase, for example approximately **30–35 Wh**, may provide clearer product value if a manufacturer can offer an electrically and mechanically compatible solution.

The actual capacities are **not decided**. In particular, universal 1S/2S support will not be introduced merely to enable multiple battery options. If multiple capacities require additional converters, different beltpack enclosures, additional firmware paths, or other relevant complexity, one optimal pack is preferred over a pack family.

## Pack requirements

The production pack should provide integrated protection/BMS functions, temperature monitoring, documented charge/discharge limits, sufficient continuous/peak current capability, documented communication where useful, fuel-gauge data, robust keyed contacts with suitable mating-cycle capability, and complete integration, conformity, and lifecycle documentation. Artificial software pairing or a proprietary battery architecture solely for customer lock-in is not permitted. Battery-specific health/learning data shall be correctly rebuilt after replacement.

## Operation and power architecture

The beltpack supports mobile and continuous external-power operation. Power-path/load-sharing, charging behavior, Battery Care, avoidance of micro-cycling, thermal limits, and pack-replacement behavior shall be coordinated with the manufacturer. Pack BMS and carrier system-power responsibilities remain clearly separated.

## Runtime and power budget

Final minimum energy is not yet fixed. Rapid field replacement means one pack does not necessarily need to cover the maximum possible shift. Selection is based on the power budget followed by prototype measurements.

Approximately **19 Wh** is currently interesting as a compact standard class. 25 Wh remains a comparison point. In parallel, a substantially larger but interface-compatible Extended class shall be investigated.

## Reference candidate: vri BASE LINE

**CANDIDATE:** VRI GmbH Batterie-Technik's vri BASE LINE is the preferred reference candidate. Particularly interesting are the 1S/21700 88054 201 512 (~19.1 Wh) and, for comparison, the 2S/18650 88030 502 512 (~25.2 Wh). Final selection considers conversion efficiency, load profile, runtime, USB-host reserve, thermal behavior, weight, volume, serviceability, and field replacement.

## Manufacturer discussion

In addition to 1S/2S, load profile, BMS/carrier responsibilities, charging, Battery Care, fuel gauge, mating cycles, conformity, lifecycle, samples, and external charging, VRI shall explicitly be asked:

1. Can a pack family provide a compact standard pack around 19 Wh and a substantially larger Extended Pack on the same electrical host interface?
2. Can voltage class, pinout, and communication interface remain the same?
3. Can the same mechanical contact/latch zone be used so that the larger pack merely protrudes further or forms a larger battery back?
4. Which existing BASE LINE or derived solution would be suitable for an Extended class around approximately 30–35 Wh?
5. What effects would such a pack family have on certification, MOQ, lifecycle, chargers, and spare-parts inventory?

## Decision rule

The preferred Standard Pack is the smallest production-ready pack that satisfies the real requirements with sufficient margin. A Standard/Extended capacity family will only be pursued if it creates **no relevant additional complexity in the beltpack**.

> **Battery capacity is a requirement, not a design goal. Product size, serviceability and reliable runtime are optimized together.**
