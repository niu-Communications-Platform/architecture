---
language: en
canonical: false
status: current
last_reviewed: 2026-09-07
source: ../../de/60-identity-security/identity-trust-architecture.md
translation_status: current
---

# Identity and Trust Architecture

[Deutsch — canonical](../../de/60-identity-security/identity-trust-architecture.md) | **English**

> The German version is canonical. This document is a maintained English translation.

## Four identities

1. **Factory/Device Identity** — the physical beltpack, immutable and bound to the carrier.
2. **Friendly/Provisioned Identity** — human-readable name, role, and profiles; mutable/transferable.
3. **Mumble/Intercom Identity** — service identity and certificates; separate and rotatable.
4. **Network/Service Identity** — hostname, IP, MAC, and current transport; ephemeral.

**DECIDED:** Factory Identity lives on the carrier, not on SD/eMMC or the SBC.

## Carrier Identity

The carrier contains or binds:

- Device UUID
- visible serial number
- Secure Element
- Carrier NVM

Replacing the SBC/storage preserves the physical device identity. Replacing the carrier creates a new physical device. Friendly Identity and profiles may be transferred to a replacement device during the RMA process.

## Secure Element

**CANDIDATE:** Microchip ATECC608C-TFLXTLS / TrustFLEX.

Separate key roles are planned for Device Root, Mumble/Service, and Cloud/Auth. Private keys never leave the Secure Element.

Software abstracts key access through a `KeyProvider`, with a file provider for development and a hardware provider for production.

## PKI

Device PKI, Service PKI, and Firmware Signing are strictly separated trust domains.

- Device Issuing CA → long-lived Device Certificates
- Base local Mumble CA → local Trust Domain
- Cloud Service/Mumble CA → hosted Trust Domain
- Firmware Signing → separate signing chain

Service keys are generated during enrollment and are rotatable.

## Open source and Trust Domains

**DECIDED:** Open source grants implementation freedom, but not nıu identity or nıu trust.

Third parties may operate their own Base/Cloud systems using their own Trust Roots. An alternative backend is accepted only if the owner explicitly authorizes its provisioning/service trust.

The general model is:

`Device UUID → Owner → Deployment → Provisioning Authority → Trust Domain`

A higher provisioning revision never compensates for missing trust in the signer.
