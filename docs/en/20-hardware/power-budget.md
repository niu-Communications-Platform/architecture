# Preliminary Power and Runtime Budget

[Deutsch — canonical](../../de/20-hardware/power-budget.md) | **English**

> The German version is canonical. This document is a maintained English translation.

## Purpose and maturity

This is the first quantitative system power model for the nıu Communications Platform beltpack. It supports battery-architecture preselection and technical discussion with battery/power suppliers.

**Important:** This is not yet a measured production budget. Verified datasheet anchors are combined with explicitly marked engineering assumptions. Prototype 1 measurements shall replace the major assumptions.

## Architecture considered

The model currently includes the Radxa ZERO 3W/RK3566 production candidate with internal Wi-Fi, 2× TLV320AIC3204 codec candidates, TAS2505-class digital speaker amplifier, 1.3–1.5-inch ~240×240 TFT, USB hub and separate USB-C accessory host, Secure Element/Carrier NVM/GPIO/LED peripherals, four RGB status LEDs, and carrier power-conversion losses.

## Verified anchor values

Radxa specifies a 5 V / 2 A supply for ZERO 3W; this is a supply requirement, **not typical consumption**. TI lists example TLV320AIC3204 core figures of 4.1 mW stereo DAC playback and 6.1 mW stereo ADC recording at 48 kHz, with actual consumption dependent on configuration and enabled blocks. TAS2505 idle/no-signal speaker operation is roughly 35.5 mW in a documented 48-kHz configuration, while actual speaker power depends strongly on signal, level, and load. Representative small 240×240 IPS displays are around a few tenths of a watt, and USB hub-controller power is likewise in the few-tenths-of-a-watt class depending on activity.

## Engineering system budget

| Consumer | Typical | Heavy/design |
| --- | ---: | ---: |
| Radxa ZERO 3W incl. internal Wi-Fi | 2.3 W | 4.0 W |
| 2× codecs + analog paths | 0.10 W | 0.25 W |
| display + backlight | 0.15 W | 0.25 W |
| USB hub, excluding external load | 0.20 W | 0.35 W |
| SE/NVM/GPIO/LED driver/sensors | 0.10 W | 0.20 W |
| four RGB status LEDs | 0.05 W | 0.15 W |
| headphone/audio outputs | 0.10 W | 0.20 W |
| internal speaker playback | +0.20 W | +0.80 W |
| carrier/power loss and reserve | 0.20 W | 0.40 W |

The Radxa values and several peripheral totals are **engineering assumptions** pending measurement, not component specifications.

## Operating states

| State | Preliminary pack power |
| --- | ---: |
| Listening / normal intercom | **~3.2 W** |
| Typical mixed use | **~3.8 W** |
| Heavy internal use | **~5.5 W** |
| Design peak without external USB load | **~8 W** |
| Design peak with 5 V / 1 A USB accessory | **~13 W** |

The up-to-5-W USB accessory allowance is treated as a separate power reserve. It affects pack/converter/thermal sizing but must not silently become part of the beltpack's advertised standard-runtime workload.

## Preliminary runtime

Using **85% of nominal energy** as an initial engineering usable-energy assumption gives:

| Pack | Listening ~3.2 W | Mixed ~3.8 W | Heavy ~5.5 W |
| --- | ---: | ---: | ---: |
| VRI 1S/21700 ~19.1 Wh | **~5.1 h** | **~4.3 h** | **~3.0 h** |
| VRI 2S/18650 ~25.2 Wh | **~6.7 h** | **~5.6 h** | **~3.9 h** |

A sensitivity case using only 75% of original nominal energy yields approximately 4.5/3.8/2.6 h for 19.1 Wh and 5.9/5.0/3.4 h for 25.2 Wh. The 75% case is **not** a decided end-of-life criterion or runtime guarantee.

## Peak consideration

At 13 W, an idealized 3.6-V 1S pack current is about 3.6 A before conversion losses. The VRI 1S/21700 candidate is currently listed up to 7 A discharge; the 2S/18650 candidate up to 5 A at 7.2 V. Neither candidate is therefore obviously excluded by the current assumed peak, but real conversion topology, low-state-of-charge behavior, transients, and thermal performance must be validated.

## First conclusion

- **19 Wh remains technically plausible**, but the current model describes it more as roughly a four-to-five-hour standard battery than an all-day pack.
- **25 Wh moves realistic operation roughly into the five-to-seven-hour range**, with greater reserve but more volume and weight.
- Rapid field replacement means a single pack does not need to cover a maximum-length shift.
- Therefore 19 Wh is not disqualified; a **smaller beltpack plus spare battery** may be a better system product than permanently carrying the larger pack.
- Real Radxa consumption is currently the single most important measurement.

**CANDIDATE DIRECTION:** 19 Wh remains the miniaturization favorite; 25 Wh remains the runtime/reserve favorite. No selection yet.

## Prototype 1 measurement plan

Measure at least: Radxa idle with Wi-Fi, connected Mumble listening, continuous RX, continuous TX/PTT, mixed duty cycle, internal speaker at practical levels, high CPU/Wi-Fi load, display brightness levels, hub idle, USB Audio/Ethernet/Wi-Fi, staged external USB loads, complete battery-side power including conversion losses, high/low state of charge, and thermal behavior during heavy use and simultaneous external-power operation.

These measurements shall define a reproducible **Beltpack Standard Duty Cycle**. Only that measured duty cycle should become the basis for advertised or guaranteed runtime.

## Sources

- Radxa ZERO 3 documentation: https://docs.radxa.com/en/zero/zero3
- Radxa ZERO 3W Product Brief: https://dl.radxa.com/zero3/docs/hw/3w/radxa_zero_3w_product_brief_Revision_1.8.pdf
- Texas Instruments TLV320AIC3204: https://www.ti.com/product/TLV320AIC3204
- Texas Instruments TAS2505: https://www.ti.com/product/TAS2505
- Texas Instruments TAS2505 Application Reference Guide: https://www.ti.com/lit/pdf/SLAU472

All figures must be verified against current datasheets and real measurements before production decisions.
