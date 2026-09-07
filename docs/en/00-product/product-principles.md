---
language: en
canonical: false
status: current
last_reviewed: 2026-09-07
source: ../../de/00-product/product-principles.md
translation_status: current
---

# Product Principles

[Deutsch — canonical](../../de/00-product/product-principles.md) | **English**

> The German version is canonical. This document is a maintained English translation.

## Product model

The nıu Communications Platform includes several deployment models:

- **Bare:** intercom endpoint; the Mumble/Murmur infrastructure is provided by the user.
- **Base:** intercom plus locally operated Mumble/Murmur and management infrastructure.
- **Cloud:** intercom plus nıu-hosted Mumble/Murmur and management infrastructure.

Where sensible, the product variants should use the same device, provisioning, and protocol foundations. Differences primarily concern the Provisioning Authority, the Trust Domain, and the location of the service infrastructure.

## Guiding principles

### User convenience

Complexity is absorbed by the product rather than passed on to the user. Normal operation should be curated, understandable, and robust.

### Apple-like convenience and developer freedom

There are three layers:

1. **Product layer:** tested and supportable standard features.
2. **Provisioning layer:** administrator profiles configure more complex capabilities through abstractions.
3. **Developer layer:** source code, configuration, and APIs may use the underlying capabilities more freely.

**Capability ≠ Feature.** A technical capability becomes an official feature only when it is understandable, robust, testable, and supportable.

### Openness

The platform should be fully open source and reproducibly buildable wherever third-party licenses permit. Openness of implementation does not mean disclosure of private trust keys and does not grant the right to present a service as an official nıu service.

### Future-proofing without feature stuffing

Low-cost hardware reserves are included where they avoid future dead ends. Not every reserve becomes an immediate product feature.

### Manufacturability

Hardware decisions are evaluated against whether a contract manufacturer can reproducibly build, program, and automatically test the device in quantities ranging from thousands to tens of thousands.
