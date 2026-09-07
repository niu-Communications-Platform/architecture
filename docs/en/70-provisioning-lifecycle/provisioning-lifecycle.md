---
language: en
canonical: false
status: current
last_reviewed: 2026-09-07
source: ../../de/70-provisioning-lifecycle/provisioning-lifecycle.md
translation_status: current
---

# Provisioning, Ownership and Lifecycle

[Deutsch — canonical](../../de/70-provisioning-lifecycle/provisioning-lifecycle.md) | **English**

> The German version is canonical. This document is a maintained English translation.

## Principle

Factory Identity, Ownership, Provisioned Identity, and Service Identities are separate layers.

A factory-new device has a Device Identity but no owner, Friendly Name, role, network, or service account yet.

## Enrollment

The target process includes:

1. Discovery
2. cryptographic device authentication
3. physical claim proof
4. admin authorization
5. Owner/Deployment binding
6. Capability validation
7. generation of service keys/certificates
8. signed declarative Provisioning Document
9. transactional apply, Health Check, and commit/rollback

Provisioning documents include, among other things, target UUID, schema/config revision, name, profiles, network, intercom, audio, and system parameters. The device validates signer/Trust Domain, target UUID, schema, Capabilities, and revision.

## States

Target states:

`MANUFACTURED → UNCLAIMED → DISCOVERED → AUTHENTICATED → CLAIMED → PROVISIONED → READY`

Additional error/degraded/offline/blocked/released/retired states are planned.

## Reset and Ownership

Factory Reset never deletes UUID, serial number, or Device Root Key.

- Soft Reset → user settings
- Config Reset → network/Mumble/profile/Friendly Name, Root Identity remains
- Ownership Release → remove or revoke Owner/service binding; return to `UNCLAIMED`

## Replace Device

Replacing the carrier creates a new Factory Identity. Friendly Identity, role, profiles, network/audio/intercom assignments may be transferred in a controlled way to the replacement device. New service keys and certificates are generated; the old device is marked as replaced/blocked in the Registry.

Principle:

**Factory Identity immutable. Provisioned Identity transferable. Service Identities rotatable. Runtime Identity ephemeral.**
