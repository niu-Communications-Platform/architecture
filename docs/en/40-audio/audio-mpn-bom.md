# Audio MPN BOM and Analog I/O Review

[Deutsch — canonical](../../de/40-audio/audio-mpn-bom.md) | **English**

> The German version is canonical. This document is a maintained English translation.

## Purpose

This document turns the current audio architecture into an MPN-/cost-level review. It focuses on the dual codec concept, internal speaker amplifier, CTIA/OMTP switching, jack detection, and ESD. It is **not a production approval of individual parts**.

## Main result

The current audio architecture remains economically plausible. The dominant cost is not CTIA/OMTP or ESD; it is the **two audio codecs**.

Current public price anchors around 1k units:

| Block | Candidate / reference | approx. 1k price | Status |
|---|---|---:|---|
| Codec #1 | TLV320AIC3204IRHBR | EUR 2.57 | CANDIDATE |
| Codec #2 | TLV320AIC3204IRHBR | EUR 2.57 | CANDIDATE |
| Internal speaker amp | TAS2505IRGER | EUR 0.76 | CANDIDATE |
| CTIA/OMTP + jack detect | TS3A225ERTER | EUR 0.47 | CANDIDATE |
| 4-channel ESD protection | TPD4E05U06DQAR | EUR 0.18 | REFERENCE CLASS |

Visible core audio silicon is therefore roughly **EUR 6.55 @1k** before analog passives, further ESD, jacks, microphones, speaker, and mechanical integration.

## 2× TLV320AIC3204

The TLV320AIC3204 remains a strong Prototype/production candidate due to its stereo ADC/DAC, multiple analog inputs, headphone/line outputs, mic bias, TDM/I2S/DSP interface, SPI/I2C, Linux-family driver support, low power, and 5 × 5 mm VQFN package.

Current public Mouser anchor for `TLV320AIC3204IRHBR` is about **EUR 2.57 @1k**; two codecs are therefore about **EUR 5.14**.

Two codecs continue to provide meaningful product value: separate PHONES and TRRS outputs, multiple analog capture paths, internal mic + separate MIC + TRRS mic, optional second internal mic, and clean TDM allocation.

**Cost rule:** a one-codec redesign is only worth pursuing if it saves roughly EUR 2 or more at system level **without** losing important endpoints, diagnostics, or routing freedom.

## Codec control

SPI remains preferred because two identical AIC3204 devices on a shared I2C bus would require additional addressing logic.

```text
SPI SCLK/MOSI/MISO shared
    ├─ CODEC1_CS
    └─ CODEC2_CS
```

Separate reset per codec remains desirable.

## Internal speaker amplifier

**CANDIDATE:** `TAS2505IRGER`

Current DigiKey anchor is about **EUR 0.76 @1k** and roughly EUR 0.71 at a full 3k reel. The part is active, Class-D, digitally controlled, supports around 2 W into 4 ohms, and is available in a 4 × 4 mm VQFN.

This fits the current architecture where the internal speaker is its own digital/TDM endpoint rather than an analog power stage behind one codec.

## CTIA/OMTP: less expensive than initially feared

Automatic CTIA/OMTP support does not require a large discrete switching network. TI continues to list active specialized headset switches that detect and route MIC/GND automatically.

### TS3A226AE

The `TS3A226AE` functionally fits well but is only available in a tiny 1.4 × 1.4 mm DSBGA package. It is therefore not the preferred manufacturability starting point.

### TS3A225E

**CANDIDATE / PREFERRED PACKAGE FOR PROTOTYPE:** `TS3A225ERTER`

- active;
- 3 × 3 mm WQFN-16;
- autonomous MIC/GND detection;
- 3-pole and 4-pole headset support;
- optional manual I2C control;
- integrated codec-sense functionality;
- current public cost about **EUR 0.47 @1k**.

This is only a small fraction of codec cost while being much more EMS-friendly than the DSBGA TS3A226AE.

### TS3A227E

The `TS3A227E` adds more accessory-detection functionality, I2C, key-press detection, and is available in VQFN. It remains a review candidate if headset button support or richer accessory diagnostics creates real V1 value.

## CTIA/OMTP product direction

**CANDIDATE:** Prototype 1 retains automatic CTIA/OMTP support.

The silicon cost is too small for a forced CTIA-only design to provide a compelling economic benefit today.

> **Compatibility should be absorbed inside the product; users should not have to think about headset wiring standards.**

## Jack detection

Preferred model:

- TRRS: electronic accessory/MIC/GND detection through the specialized headset switch;
- PHONES: mechanical insertion detect;
- MIC: mechanical insertion detect;
- software maps these into `connected`, `available`, `active`, `health`.

Mechanical detect is presence information only, not identity or quality assurance.

## ESD / external audio interfaces

Every external audio connector requires suitable ESD protection. `TPD4E05U06DQAR` is a useful cost/package reference with four channels, very low capacitance, and a public price around **EUR 0.18 @1k**.

The exact production ESD device will be selected based on signal range, clamp behavior, package, and layout. No external jack should connect directly to unprotected codec pins.

## Analog front end

Still not MPN-locked:

- AC coupling and filtering;
- mic-bias routing;
- protection/series resistors;
- optional level/impedance adaptation;
- optional external MIC bias support;
- CTIA/OMTP support passives;
- click/pop behavior;
- EMI/RF filtering.

Early allowance: roughly **EUR 1.5–2.5** for these analog/passive blocks in total.

## Mechanical audio components

Early engineering allowances only:

| Component | Target allowance |
|---|---:|
| PHONES jack | EUR 0.30–0.60 |
| MIC jack | EUR 0.30–0.60 |
| TRRS jack | EUR 0.40–0.80 |
| Internal mic 1 | EUR 0.25–0.50 |
| Optional internal mic 2 | EUR 0.25–0.50 |
| Internal speaker | EUR 0.80–1.50 |

Jacks must be selected for mechanical lifetime, insertion cycles, side-load robustness, PCB retention, detect reliability, availability, assembly method, and enclosure integration—not unit price alone.

## Preliminary audio cost view

Core silicon:

- 2× codec: ~EUR 5.14
- speaker amp: ~EUR 0.76
- CTIA/OMTP switch: ~EUR 0.47
- ESD reference: ~EUR 0.18

**Subtotal:** ~EUR 6.55

Additional audio electronics: ~EUR 1.7–3.0.

Mechanical audio I/O: ~EUR 2.1–4.5 depending on second mic and component choices.

**Early complete audio-hardware range:** roughly **EUR 10–14**, excluding PCB/assembly share.

This remains broadly compatible with the Carrier Core + Audio budget of EUR 13–17 but leaves limited room for other core functions, so subsystem worst-case ranges must not simply be added together.

## Main cost / architecture risks

1. Two codecs—already ~EUR 5.1 publicly at 1k.
2. Mechanical jacks—cheap parts can create expensive durability or assembly problems.
3. Analog detail creep—bias/filter/protection networks can accumulate unnecessary BOM.
4. Internal speaker—acoustic efficiency and enclosure volume matter more than small component savings.
5. Mic 2—populate in production only if DSP/AEC/noise measurements demonstrate real value.

## Prototype-1 audio gate

Prototype 1 shall validate dual AIC3204 SPI control; shared TDM on RK3566/Radxa; independent PHONES and TRRS; digital internal speaker endpoint; real CTIA and OMTP headset detection; 3-pole headphones; mechanical MIC/PHONES detect; external MIC behavior; click/pop; ESD/robustness pre-tests; noise floor/crosstalk/THD on real carrier layout; boost/PD/Wi-Fi interference; speaker loudness/thermal margin; and the value of Mic 2.

## Current direction

**CANDIDATE / PREFERRED FOR PROTOTYPE 1:**

```text
RK3566 TDM
  ├─ AIC3204 #1 → PHONES / body microphones / MIC input
  ├─ AIC3204 #2 → TRRS L/R + headset microphone
  │                  ↕
  │             TS3A225E-class
  │             CTIA/OMTP detect/switch
  └─ TAS2505-class → internal speaker
```

The positive finding is that **automatic CTIA/OMTP support is not a meaningful cost driver**. The actual audio cost lever is whether two full codecs justify their product value. For Prototype 1, the answer remains yes: validate first, optimize later.
