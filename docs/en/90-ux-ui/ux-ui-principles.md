---
language: en
canonical: false
translation_of: ../../../de/90-ux-ui/ux-ui-principles.md
translation_status: current
status: current
last_reviewed: 2026-09-07
---

# UX/UI Principles

[Deutsch](../../de/90-ux-ui/ux-ui-principles.md) | **English**

> The German version is canonical. This document is a maintained English translation.

## Principles

- time-critical functions work blindly
- immediate feedback
- clear separation of Home / Menu / Diagnostics
- no unnecessary confirmations
- reality beats configuration
- color = state, animation = activity/transition
- live status instead of Refresh
- navigation remains static, data is dynamic
- Direct Views do not change navigation state
- rare safety chords are acceptable; daily functions are not
- Capability ≠ Feature
- no regular Expert Mode

## Display

Target: approx. 1.3–1.5" 240×240 color IPS/TFT, dimmable, backlight can be turned off.

Home shows:

- own Mumble username
- active communication target
- battery
- network status/signal
- active speakers
- lock status

No regular display of IP, server, ping, time, or CPU temperature.

## Buttons

1. PTT
2. VOL+
3. VOL−
4. CH+
5. CH−
6. MENU/OK
7. BACK
8. POWER

Navigation uses Views/Menu/Detail/Dialog/Overlay, not horizontal pages.

Key Lock: VOL+ + VOL− for approx. 2 s. VOL/CH/MENU/BACK are locked; PTT and POWER remain active.

## Power

- device off: short press does nothing, hold 2–3 s → boot
- running: short press → Battery Direct View
- hold 2–3 s → graceful shutdown without confirmation
- ≥8 s → independent Hard-Off

Boot is considered successful when OS/systemd, required local hardware, local services, and `niu-beltpack` are READY. Wi-Fi/Murmur connectivity is not required for this.

## LEDs

Four RGB LEDs: PWR, NET, RX, TX. States use semantically consistent colors; color is never the only indicator.

NET abstracts the transport: no usable network = blinking red; network available, intercom not connected = blinking orange; intercom connected = green.

RX/TX distinguish normal, mute/blocked, and impossible actions through color plus animation.

## Diagnostics

Diagnostic areas: System, Audio, Connections, Intercom, Power, Events.

Event Ring Buffer: around 20–50 relevant state changes; no PTT or volume spam logs.
