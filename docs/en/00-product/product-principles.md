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

### Digital sovereignty includes the hardware

Digital sovereignty does not end with access to source code or self-hosting. The owner should be able to understand, diagnose, repair, recover, and continue operating the product with custom software or custom Trust Domains.

This leads to the following product goal:

**Open Source → Open Hardware → Open Diagnostics → Open Repair Documentation.**

Where technically and legally possible, nıu therefore publishes the information and tools required for qualified independent fault analysis and repair. This includes, in particular, hardware and interface information, diagnostic procedures, repair instructions, relevant test points and expected values, calibration and recovery procedures, and open diagnostic tools.

The openness of diagnostics and repair is strictly separated from the official nıu Trust Domain:

> **Diagnostics are open. Trust issuance is not.**

A repair or modification by the owner or an independent repair shop does not by itself terminate the device's official nıu trust status. As long as the existing cryptographic device identity can still be reliably proven, it is generally preserved. If the Identity Anchor can no longer be reliably proven or has to be replaced, a controlled nıu recertification process is required for renewed admission to or attestation within the official nıu Trust Domain.

### Future-proofing without feature stuffing

Low-cost hardware reserves are included where they avoid future dead ends. Not every reserve becomes an immediate product feature.

### Manufacturability

Hardware decisions are evaluated against whether a contract manufacturer can reproducibly build, program, and automatically test the device in quantities ranging from thousands to tens of thousands.
