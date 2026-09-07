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

## Open repair and official nıu attestation

**DECIDED:** nıu does not regulate what an owner may technically do with their device. The security boundary is what the official nıu Trust Domain cryptographically attests to.

Opening, diagnosing, repairing, reimaging, installing custom software, and using custom Trust Roots or services should generally be possible and documentable. Physical access or knowledge of the open implementation, however, does not authorize issuance or renewal of official nıu Device Certificates, modification of the Factory Registry, or creation of other nıu attestations.

Principle:

> **Anyone may repair or modify the device. Only nıu may attest that a device belongs to the official nıu trust domain.**

Independent repair does not automatically terminate existing trust status. As long as the existing Identity Anchor remains intact and the Device Identity can still be reliably proven cryptographically, the repair itself does not create a reason for new attestation.

If the Identity Anchor can no longer be reliably proven or must be replaced, restoration of official nıu trust status becomes an Identity Recovery/recertification operation. For the first product generation, the physical device is intended to be sent to nıu as the manufacturer for this purpose. nıu verifies the device and identity association, performs the required Factory/EOL and security checks, and may then issue a new official attestation or update the Registry in a controlled manner.

The specific semantics of Secure Element replacement — in particular whether the Device UUID is retained or changed, how the Root Key changes, and whether an Identity Epoch is used — will be decided separately and remain open at this time.

Loss of or opting out of official nıu trust does not prevent the owner from continuing to operate the device with custom software, a custom PKI, or a custom Trust Domain.
