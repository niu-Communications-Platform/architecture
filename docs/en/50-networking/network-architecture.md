---
language: en
canonical: false
status: current
last_reviewed: 2026-09-07
source: ../../de/50-networking/network-architecture.md
translation_status: current
---

# Network Architecture

[Deutsch — canonical](../../de/50-networking/network-architecture.md) | **English**

> The German version is canonical. This document is a maintained English translation.

## Transport classes

Initially planned:

- `internal_wifi`
- `usb_wifi`
- `usb_ethernet`

later optionally `usb_tethering` and `usb_cellular`.

A conceptual default priority is USB Ethernet → USB Wi-Fi → internal Wi-Fi; the actual order is policy-controlled.

## Network Manager

Transport selection and failover belong in a dedicated Network Manager. Talkkonnect should not independently make competing transport decisions.

Transport states:

`ABSENT`, `PRESENT`, `CONNECTING`, `LINKED`, `IP_READY`, `VALIDATING`, `USABLE`, optionally `DEGRADED`, `FAILED`, `COOLDOWN`.

Roles:

`NONE`, `CANDIDATE`, `PRIMARY`.

Health hierarchy:

LINK → IP → ROUTE → SERVER → INTERCOM.

## Handover

**DECIDED:** make-before-break at the transport layer; break-before-make at the Mumble session layer.

A new preferred transport is fully established and validated while the existing Mumble connection still runs over PRIMARY. Only after `USABLE` is reached is the old Mumble session terminated, the new transport made PRIMARY, and the intercom session re-established using the same logical identity.

There must never be two parallel Mumble sessions for the same beltpack.

After successful takeover, the old transport may be disabled. If an external adapter is lost unexpectedly, a break-before-make fallback to internal Wi-Fi is naturally required.

The configuration of internal Wi-Fi remains stored while it is temporarily disabled.
