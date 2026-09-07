---
status: accepted
date: 2026-09-07
---

# ADR-0004: Mumble as the native real-time voice protocol, SIP as an interoperability layer

[Deutsch — canonical](../de/0004-mumble-native-sip-interoperability.md) | **English**

> The German version is canonical. This document is a maintained English translation.

## Status

**ACCEPTED**

## Context

The nıu Communications Platform is primarily a professional intercom and group communication system, not a telephone system. Typical communication relationships are persistent between roles, groups and talkgroups; voice is routed through PTT, channels and targeted talk paths.

Mumble/Murmur and SIP-based systems are among the relevant architectural options. SIP is widely established in telephony, unified communications and professional infrastructure and provides a large ecosystem for PBX, telephone and gateway integration. Its core model, however, is primarily concerned with signalling and establishing communication sessions. Building an intercom on top of SIP would require additional components and application logic for group communication, PTT, talkgroups, routing and conferencing/matrix behaviour.

Mumble/Murmur already provides a persistently connected, low-latency group communication model with channels, ACLs and targeted voice transmission. This maps much more directly to the core behaviour of the nıu Communications Platform.

Talkkonnect is an important additional factor. Talkkonnect is a headless Mumble PTT client for hardware appliances and already provides mechanisms relevant to nıu, including PTT, hardware control, voice targets, API integration and provisioning capabilities. This allows nıu to build on an existing intercom-oriented engine instead of implementing an entire endpoint stack from scratch.

## Decision

**Mumble is the native real-time voice protocol of the nıu Communications Platform. Murmur is the preferred server foundation for native intercom communication.**

Talkkonnect is treated as an important intercom engine and integration foundation. The higher-level nıu architecture — particularly Device Identity, Ownership, Provisioning, Capability Management, Audio Routing, OTA, Health and UX — remains separate and must not become unnecessarily coupled to Talkkonnect.

**SIP is explicitly not excluded. SIP is, however, an interoperability protocol rather than the native device protocol.**

Where required, SIP integration should preferably be implemented centrally through Base, Cloud or gateway components instead of making SIP the foundation of every beltpack.

Conceptually:

```text
nıu Beltpacks / native clients
            │
       Mumble protocol
            │
     Murmur / nıu Base
            │
     interoperability
       gateway layer
       ├── SIP
       ├── RTP
       └── other external systems
```

## Rationale

Mumble fits the native nıu communication model particularly well because of:

- persistent client/server connections rather than primarily call-oriented sessions,
- low-latency voice transport,
- channels and group communication,
- ACLs and participant permissions,
- targeted voice transmission for different talk paths,
- strong suitability for PTT-based operation,
- straightforward local and self-hosted Murmur deployments,
- suitability for both Base and Cloud operation,
- the existing Talkkonnect implementation as a hardware/PTT-oriented foundation.

SIP remains strategically relevant, especially for:

- PBX integration,
- SIP phones and softphones,
- existing enterprise communications infrastructure,
- telephony,
- paging and gateway systems,
- interoperability with third-party systems.

The architecture therefore deliberately separates **native communication** from **external interoperability**.

## Consequences

### Positive

- The beltpack stack remains focused on the actual intercom problem.
- Talkkonnect can be used as an existing foundation.
- A Base can run a comparatively compact local Murmur service.
- Bare, Base and Cloud scenarios can share the same native communication model.
- SIP and other protocols can be added later without redesigning every endpoint.
- The open-source and self-hosting strategy is preserved.

### Negative / trade-offs

- Mumble does not have SIP's universal industry interoperability.
- Direct integration with existing PBX/UC environments requires gateways or bridges.
- nıu must validate the practical limits and extension points of Mumble and Talkkonnect during prototyping.
- Requirements beyond Mumble's communication model may require custom protocol, audio or routing logic.

## Architecture rule

> Mumble is the native real-time voice protocol of the nıu Communications Platform. SIP is an interoperability protocol, not the native device protocol.

This statement describes the current architecture decision; it does not require all future communication to use Mumble exclusively.

## To be validated

Before the P0 Architecture Gate, practical validation should cover at least:

- real end-to-end latency on the local production network,
- PTT latency and behaviour during rapid speaker changes,
- Voice Targets and their control through Talkkonnect,
- multiple simultaneous listen and talk paths,
- behaviour during network handover and temporary duplicate sessions,
- audio quality and Opus configuration,
- scaling to realistic participant counts,
- separation between Talkkonnect and the nıu Audio Engine,
- possible SIP/RTP gateway paths for future interoperability.
