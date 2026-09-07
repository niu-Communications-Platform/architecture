# ADR-0002: Network handover separates transport switching from Mumble session switching

**Status:** Accepted  
**Date:** 2026-09-07

## Context

The beltpack may provide internal Wi-Fi, USB Wi-Fi and USB Ethernet. Switching between them should cause as little interruption as possible, but must not result in two simultaneous Mumble sessions using the same beltpack identity.

## Decision

**Make-before-break at the network transport layer; break-before-make at the Mumble session layer.**

A candidate transport is fully established and validated first. The existing Mumble session remains on PRIMARY until then. After successful validation, the old Mumble session is terminated, the candidate becomes PRIMARY and the session is re-established over the new transport.

## Rationale

This limits the unavoidable intercom interruption to the session reconnect without creating duplicate logical clients. Network availability can be verified before the actual switch.

## Consequences

- Network Manager and Talkkonnect/Intercom Engine have separate responsibilities.
- Interfaces may have IP connectivity in parallel while a candidate transport is being validated.
- The same IP/MAC must not be used simultaneously on two interfaces.
- Handover interruption becomes a measurable prototype KPI.

## Validation required

Practical measurements with internal Wi-Fi, USB Wi-Fi and USB Ethernet under different Mumble network conditions.

---

[Canonical German version](../de/0002-network-handover-session-model.md)
