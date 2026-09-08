# Mechanical I/O Components – Strategy for Prototype 1

[Deutsch — canonical](../../de/20-hardware/mechanical-io-component-strategy.md) | **English**

> The German version is canonical. This document is a maintained English translation.

## Goal

This block addresses components that may look electrically simple but are critical to a portable consumer product: jacks, buttons, encoders, display integration, the battery interconnect, and their mechanical implementation.

For nıu.cp, these parts strongly influence user feel, repairability, lifetime, enclosure design, assembly time, and series cost at the same time.

## Guiding principle

> **For mechanical I/O components, unit price alone is not decisive. The right component reduces enclosure complexity, manual assembly, failure risk, and service cost.**

## 3.5 mm audio jacks

Separate MIC, PHONES, and TRRS headset ports remain planned.

Prototype 1 should avoid ultra-miniature smartphone-style jacks if they unnecessarily complicate manufacturing and repair. Preferred parts should be established, mechanically robust PCB jacks with documented mating-cycle ratings, mechanical detect where useful, clear manufacturer drawings for enclosure cut-outs and PCB placement, sufficient retention force, strong PCB anchoring, and assembly processes comfortable for a German contract manufacturer.

The TRRS path additionally requires CTIA/OMTP detection or switching on the electronics side. The mechanical connector itself should remain non-proprietary where possible.

### Product-level understanding

A jack is not merely an electrical contact. Every insertion and removal transfers force into the enclosure and PCB. A cheap or poorly supported connector can therefore become the dominant product failure point even when the electronics are perfect.

## USB-C

Two visible USB-C ports remain planned:

- **POWER:** external power and charging, no normal data function.
- **ACCESSORY:** USB host for USB Audio, Ethernet, HID, and other supported devices.

USB-C receptacles must be evaluated primarily for mechanical robustness, not just component price. Preferred parts include strong shell/shield anchor tabs and well-documented PCB footprints.

For a mobile beltpack, the signal contacts should not carry the mechanical cable load.

## Battery interconnect

The battery is intended as a rapidly field-replaceable complete production pack. The pack manufacturer owns cell/BMS responsibility; the Carrier owns system integration.

The electrical connection therefore needs to be keyed or polarity-safe, suitable for repeated field replacement, offer adequate current margin, support temperature/data lines of the selected pack, remain reliable under movement and vibration, and be service-replaceable without soldering.

The currently reviewed VRI BASE LINE packs use a 5-pin Molex Micro-Fit 3.0 interface. This is therefore an important reference, but not yet a final series decision.

If the battery must be replaceable within seconds, an ordinary internal cable connector may not be sufficient as the end-user interface. The battery carrier may require a guided contact mechanism while a Micro-Fit or comparable connector remains internal to the pack/carrier assembly. This should be reviewed together with VRI and the enclosure engineer.

## PTT and controls

The PTT button is expected to be the most heavily used mechanical control and should not be treated as an ordinary UI key.

Prototype 1 should validate actuation force, travel and tactile feedback, glove use, accidental activation while worn, structure-borne noise into the internal microphone, lifetime, side-load behavior, and replacement of the external actuator.

The electronics may use a standard momentary switch, but user feel is largely created by enclosure mechanics, key cap, and force path. The final PTT MPN therefore should not be selected independently from the enclosure design.

VOL+/VOL−, CH+/CH−, MENU/OK, and BACK see lower duty but should follow the same design language and provide clear tactile feedback.

## Encoder

A rotary encoder is not currently mandatory product hardware. If a later UX prototype shows a clear benefit over the planned buttons, it must be weighed against added enclosure penetration, mechanical height, sealing challenges, wear, and assembly effort.

**Capability ≠ Feature** applies here as well: GPIO or mechanical reserve for an encoder is not itself a reason to ship one.

## Display

The target remains approximately 1.3–1.5 inch, 240×240, color IPS/TFT.

Prototype 1 must validate not only the panel but its entire integration: FPC/FFC versus board module, connector and latch, panel height and window, mechanical support, light gap/dust protection, replacement without Carrier damage, and long-term sourcing.

For series architecture, a replaceable display module is generally preferable to a display permanently soldered to the Carrier if cost and space remain acceptable.

## Assembly cost

Each component should be evaluated not just by MPN price but by component cost, PCB area, enclosure geometry, hand/THT soldering, cables or intermediate connectors, manual assembly time, EOL testability, repair time, and expected mechanical lifetime.

A connector costing EUR 0.30 more can be economically superior if it removes one minute of manual assembly or prevents frequent RMA cases.

## Prototype-1 gates

Prototype 1 should demonstrate at minimum that external connectors tolerate repeated mating without PCB/enclosure damage, USB-C cable forces are transferred into the shell/enclosure rather than signal contacts, PTT can be operated reliably blind and with gloves, PTT does not create unacceptable structure-borne noise in the internal microphone, the display can be mounted and ideally replaced without damaging the main PCB, the battery can be exchanged within seconds without opening the main enclosure, battery orientation is protected against user error, and all external I/O can be electrically checked during EOL testing.

## Current status

**CANDIDATE / STRATEGY, no MPN release.**

Mechanical I/O MPNs should only be selected after PCB, enclosure, repair concept, and real-world handling have been reviewed together.
