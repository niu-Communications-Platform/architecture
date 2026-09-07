# Audio Architecture

[Deutsch — canonical](../../de/40-audio/audio-architecture.md) | **English**

> The German version is canonical. This document is a maintained English translation.

## Requirements

The beltpack should support the following audio endpoints:

- internal microphone and internal speaker
- separate MIC and PHONES jacks
- TRRS headset with automatic CTIA/OMTP handling
- Bluetooth audio
- USB Audio Class

At product level, exactly one microphone source is active at a time. Multiple playback outputs may be active in parallel.

## Routing

A global RX master level is logically located before distribution to the outputs. Intercom and additional feeds are treated as separate logical sources.

Possible technical routings include, among others:

- Intercom + PGM together on one headset
- Intercom on USB, PGM on PHONES
- Intercom on TRRS, PGM on Speaker
- Split Ear L/R on suitable endpoints

The unrestricted matrix belongs to the Developer layer; the normal UI exposes only curated profiles.

## Additional feeds

PGM is the first use case of a generic additional audio feed. Later semantics may include IFB, translation, Producer Feed, Guide Track, or Conference Audio. Feeds have independent level and optional ducking.

## Analog/TDM target architecture

**CANDIDATE:** 2× TLV320AIC3204 plus a dedicated digital speaker amp on a shared TDM bus.

Codec #1 / Body Audio:
- DAC L/R → PHONES
- ADCs → Internal Mic 1, separate MIC, optional Internal Mic 2, reserve

Codec #2 / Headset:
- DAC L/R → TRRS
- ADC → TRRS microphone after CTIA/OMTP switching, reserve

Speaker:
- dedicated TDM slot → digital Class-D amp → internal speaker

TDM candidate: 48 kHz, 24-bit payload in 32-bit slots, 8 slots.

## Endpoint fallback

Desired routing and actually available routing are considered separately.

- If the last active external RX output disappears, the system falls back to the internal speaker where possible and informs the user.
- If the active microphone disappears, the internal microphone is activated where possible and the user is informed.

Principle: **Audio remains functional when possible.**

## Internal Mic 2

Mic 2 is an optional hardware basis for later DSP/noise/AEC/directional functions, not a stereo microphone feature. Engineering/pilot boards should populate it; population in series production remains optional until its value has been validated.
