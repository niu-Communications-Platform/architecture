---
status: accepted
date: 2026-09-28
---

# ADR-0006: Murmur Virtual Servers form the cloud tenant boundary

[Deutsch — canonical](../de/0006-cloud-tenant-boundary-murmur-virtual-server.md) | **English**

> The German version is canonical. This document is a maintained English translation.

## Status

**ACCEPTED**

## Context

nıu.cp is designed in the Bare, Base, and Cloud variants. In the Cloud variant, nıu operates the Mumble/Murmur infrastructure for multiple independent customers or tenants.

Murmur supports multiple virtual servers within one process. Within a virtual server, channels, groups, and ACLs are available for structure and access control.

nıu.cp therefore requires a clear technical boundary at which tenants are separated from each other. Separating multiple customers only by channel passwords, tokens, or ACLs inside the same virtual server would make tenant isolation depend on the correct configuration of individual channel permissions. Conversely, assigning a dedicated Murmur process or container to every standard tenant would fail to use Murmur's intended virtual-server abstraction and would unnecessarily increase operational overhead.

## Decision

In **nıu.cp Cloud, a Murmur Virtual Server is the standard technical tenant boundary**.

The mapping is:

- **Tenant / customer → Murmur Virtual Server**
- **Project / production / workspace → channel or channel tree within the Virtual Server**
- **Role / function → Murmur Group and ACL**
- **User / device → authenticated identity within the assigned tenant**

A single Murmur process may host multiple virtual servers and therefore multiple nıu.cp Cloud tenants.

The nıu.cp Control Plane maintains at least the following mapping:

`tenant → Murmur node → virtual server`

The concrete Murmur topology is an internal implementation layer. Clients and beltpacks are mapped to their target service and role through provisioning and do not need to manage the physical node assignment themselves.

Murmur Ice or an equivalent administrative management interface is **not a direct tenant interface**. It remains exclusively part of the internal Control Plane. Tenant administration is performed through nıu.cp-owned, tenant-authorized management functions.

A dedicated Murmur process, container, or host remains a permitted higher isolation level, for example for specific Enterprise, compliance, SLA, or operational requirements. This stronger isolation is not the default and does not change the logical tenant abstraction.

## Rationale

The Murmur Virtual Server is the appropriate intermediate layer between channel permissions and full process/host isolation.

This creates clear responsibilities:

- Channels and ACLs structure one tenant instead of separating tenants from each other.
- Virtual Servers isolate standard tenants at the Murmur layer designed for that purpose.
- Processes, containers, and hosts provide additional operational and isolation boundaries when required.
- The nıu.cp Control Plane remains authoritative for tenant assignment, provisioning, and administration.

The architecture can therefore start small and later scale across multiple Murmur nodes without changing the tenant model.

## Consequences

- The Cloud Control Plane requires a persistent mapping of Tenant, Murmur Node, and Virtual Server ID.
- Creating a Cloud tenant creates or uniquely assigns a Virtual Server.
- Projects and productions of one tenant do not normally create separate Murmur Virtual Servers; they are structured within the tenant server.
- Channel passwords, tokens, groups, and ACLs must not be used as the primary tenant boundary.
- Administrative Murmur interfaces must not be exposed directly to tenants.
- Monitoring, backup, migration, and capacity planning must treat the Virtual Server as the tenant unit.
- A tenant must remain migratable between Murmur nodes without losing its logical nıu.cp identity.
- Base and Bare remain decoupled from this Cloud operations decision: Base may run one or more Virtual Servers locally; Bare may use any compatible Mumble/Murmur infrastructure.

## Dependencies

- ADR-0003: Open source and trust domains are separate.
- Provisioning Authority / Control Plane must be able to distribute tenant assignment and service parameters securely.
- The future `cloud` repository must implement this tenant abstraction without unnecessarily leaking Murmur-specific details into device or user interfaces.

## To be validated

Before production Cloud operation, practical validation must cover:

- automatic creation, configuration, and removal of Virtual Servers,
- secure tenant-specific administration exclusively through the nıu.cp Control Plane,
- isolation of user, channel, and configuration data between two test tenants,
- behavior on Murmur node failure and restart,
- backup/restore and migration of an individual tenant to another node,
- capacity limits of a Murmur process or node for later scheduling of new tenants.
