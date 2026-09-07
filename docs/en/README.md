# Architecture Documentation — English translation

[Deutsch](../de/README.md) | **English**

This directory contains the maintained English translation of the **canonical German architecture documentation** in `docs/de/`. In case of discrepancies, the German version prevails.

## Documentation

- [`00-Product Principles`](00-product/product-principles.md) — product model, guiding principles, openness, Capability ≠ Feature, and manufacturability
- [`10-System Architecture`](10-system/system-architecture.md) — repository boundaries, Capability Layer, Device Agent, and architecture phase
- [`20-Repairability and Resource Conservation`](20-hardware/repairability-sustainability.md) — repair principles, repair levels, replaceable assemblies, battery, calibration, and sustainable replacement granularity
- `30-software/` — shared software architecture, services, and abstractions; currently no dedicated document
- [`40-Audio Architecture`](40-audio/audio-architecture.md) — audio endpoints, routing, additional feeds, TDM target architecture, and fallbacks
- [`50-Network Architecture`](50-networking/network-architecture.md) — transport classes, Network Manager, health model, and handover
- [`60-Identity and Trust Architecture`](60-identity-security/identity-trust-architecture.md) — device identity, Secure Element, PKI, and Trust Domains
- [`70-Provisioning, Ownership and Lifecycle`](70-provisioning-lifecycle/provisioning-lifecycle.md) — enrollment, states, reset, ownership, and Replace Device
- [`80-Factory and Manufacturing Architecture`](80-manufacturing/factory-architecture.md) — scaling, Factory Provisioning, EOL, and irreversible operations
- [`90-UX/UI Principles`](90-ux-ui/ux-ui-principles.md) — interaction model, display, buttons, power, LEDs, and diagnostics

Product-specific implementation details belong in the corresponding product repositories unless they define or affect platform-wide architecture.
