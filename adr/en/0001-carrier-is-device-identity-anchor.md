---
language: en
canonical: false
status: accepted
date: 2026-09-07
source: ../de/0001-carrier-is-device-identity-anchor.md
translation_status: current
---

# ADR-0001: The carrier is the anchor of physical device identity

[Deutsch — canonical](../de/0001-carrier-is-device-identity-anchor.md) | **English**

> The German version is canonical. This document is a maintained English translation.

**Status:** Accepted  
**Date:** 2026-09-07

## Context

The SBC, eMMC/storage and software must be replaceable or recoverable in the field without administratively turning a beltpack into a new physical device. At the same time, cloning a storage medium must not be sufficient to duplicate a device identity.

## Decision

The immutable Factory/Device Identity is bound to the carrier. The carrier contains the Secure Element and carrier NVM and is linked in the Factory Registry to the Device UUID and serial number.

Replacing the SBC or storage preserves the Factory Identity. Replacing the carrier creates a new Factory Identity.

## Rationale

The carrier is the long-lived physical unit of the product, while compute and storage may be service or wear components. This separation enables repair, reimaging and zero-touch recovery without losing device identity and prevents identity cloning by copying storage alone.

## Consequences

- Secure Element and carrier NVM are V1 hardware components.
- Provisioning and Base/Cloud address devices primarily via Device UUID/Registry rather than IP/MAC.
- RMA requires an explicit Replace Device process when the carrier is replaced.
- Friendly/Provisioned Identity must remain separate from Factory Identity.

## Validation required

The specific Secure Element/EEPROM components and their factory provisioning/locking process must be validated practically.
