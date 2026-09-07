---
language: en
canonical: false
translation_of: ../../../de/80-manufacturing/factory-architecture.md
translation_status: current
status: current
last_reviewed: 2026-09-07
---

# Factory and Manufacturing Architecture

[Deutsch](../../de/80-manufacturing/factory-architecture.md) | **English**

> The German version is canonical. This document is a maintained English translation.

## Scaling target

The product is designed from the outset so that a contract manufacturer can reproducibly build, program, test, and package quantities in the four- to five-digit range.

Guiding question: Can a factory worker build the device correctly 10,000 times without interpretation, and can a test station subsequently determine automatically whether it works?

## Factory Provisioning

Target sequence:

1. PCB Assembly
2. electrical bring-up
3. temporary Manufacturing Candidate Record
4. complete EOL test before identity assignment
5. atomic reservation of serial number + UUID in the Factory Registry
6. write and readback/CRC of Carrier NVM
7. generate Device Root Key inside the Secure Element
8. issue Device Certificate
9. complete the Factory Registry
10. generate no service identities
11. generate QR/label
12. cross-check QR = EEPROM = Registry = public-key binding
13. only then perform irreversible slot locks/security finalization
14. hardware Secure Boot/OTP only after separate recovery validation
15. final state `UNCLAIMED`

**DECIDED:** Nothing irreversible before complete cross-verification.

## Manufacturing design

Series design considers:

- assembly-friendly construction
- minimal manual work
- defined connectors
- test points
- Factory Test Mode
- serial number/QR
- hardware/software revisions
- automated EOL testing
- reproducible antenna placement
- controlled BOM/substitutions
- scalable provisioning, OTA, and diagnostics

## Operation Classes

- reversible: flashing, tests, temporary data, mutable EEPROM areas
- auditable/semi-permanent: serial number, UUID, certificate, label; failed identities become `SCRAPPED` and are never reused
- irreversible: Secure Element slot locks, future OTP fuses

Factory Mode must be restricted by Manufacturing State, physical/service-related conditions, and an authorized Factory Station.
