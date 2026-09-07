---
status: accepted
date: 2026-09-07
---

# ADR-0003: Open source and trust domains are separate

[Deutsch — canonical](../de/0003-open-source-trust-domains.md) | **English**

> The German version is canonical. This document is a maintained English translation.

**Status:** Accepted  
**Date:** 2026-09-07

## Context

The entire platform should be open source and self-hostable. At the same time, official nıu devices, firmware, Provisioning Authorities and cloud services must remain cryptographically authenticatable. Publishing the source code must not make it possible to present an unrelated service as an official nıu service.

## Decision

The implementation is open; trust roots and private operational/signing keys are not.

Official nıu builds and services use nıu trust domains. Third parties may operate the same implementation using their own Device PKIs, Service PKIs, firmware-signing keys and Provisioning Authorities.

A device accepts an alternative trust domain only after authorized trust configuration by the owner or through the intended Developer/Custom Trust policy.

## Rationale

This preserves self-hosting, forks, repairability and continued operation independently of the manufacturer without sacrificing the authenticity of official nıu services.

## Consequences

- Trust stores and signers must be abstracted.
- Device PKI, Service PKI and Firmware Signing remain separate.
- Trademark rights and software licensing are handled separately.
- Base/Cloud protocols must not rely on security by obscurity.
