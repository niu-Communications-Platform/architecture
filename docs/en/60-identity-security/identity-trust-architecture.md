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

### Minimal persistent identifiers

**DECIDED:** A new persistent ID is introduced only if it answers a distinct semantic question that cannot be answered by an existing ID or an already required property.

At product level, Factory/Device Identity requires three distinct values:

- **Device UUID — who:** permanent machine-readable identity of the physical device.
- **Serial Number — human reference:** human-readable device identifier for the product label, support, service, and documentation.
- **Device Root Key — proof:** cryptographic proof of the claimed Device Identity; the private key remains in the Secure Element.

These values are not interchangeable and do not merely store the same information multiple times. Hardware Revision, Variant, Manufacturing Data, Calibration Data, MAC addresses, Secure Element serial numbers, and any NVM chip UIDs are properties or technical diagnostic values, not additional Device Identities.

**DECIDED:** A separate `Carrier Physical ID` is not introduced at this time. In the current model it would not serve a sufficiently distinct function and, in particular, would not provide an additional cryptographic proof of identity.

The existing Serial Number should also be permanently marked on the carrier in addition to the external product label. This makes the same already-required information directly available on the identity-bearing component during physical repair without introducing another identifier and another Registry mapping.

A UID inherently provided by an EEPROM/NVM or Secure Element may be recorded as a diagnostic or manufacturing attribute. Its existence alone does not make it part of the Device Identity model. If future manufacturing actually requires separate PCB/panel serialization for traceability, it will be introduced for that concrete manufacturing purpose rather than preemptively as a Security Anchor.

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

**DECIDED:** No additional persistent hardware ID is introduced solely to preserve the previous Device UUID under every possible rare multiple-failure scenario. If, for example, both the Secure Element and Carrier NVM have failed, the serial number, permanent carrier marking, Factory/Manufacturing Data, Calibration Data, and repair history may serve as forensic evidence. If these do not establish continuity with sufficient confidence, the old Device UUID is not re-attested; instead, the device receives a new Device Identity and may be reassociated with the intended Deployment through the Replace Device process.

Loss of or opting out of official nıu trust does not prevent the owner from continuing to operate the device with custom software, a custom PKI, or a custom Trust Domain.
