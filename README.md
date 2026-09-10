# nıu Communications Platform — Architecture

[Deutsch](README.de.md) | **English**

This repository contains the cross-cutting system architecture, product decisions, technical design principles, Architecture Decision Records (ADRs), validation plans and historical architecture snapshots of the nıu Communications Platform.

The **German documentation is canonical** for architecture and product decisions. The English documentation is maintained as a translation for collaboration and community exchange. In case of discrepancies, the German version prevails.

## What is the nıu Communications Platform?

The nıu Communications Platform (`nıu.cp`) is an open communication platform for professional live production, broadcast and event environments. Its first product is a portable intercom/IP-audio beltpack using **Mumble as the native real-time voice system** with SIP as an interoperability layer.

The platform is designed around three operating models:

- **Bare** — beltpack with user-provided Mumble/Murmur infrastructure;
- **Base** — beltpack plus local nıu Base providing Mumble/Murmur and management;
- **Cloud** — beltpack plus nıu-operated service infrastructure.

Guiding idea:

> **Open Source → Open Hardware → Open Diagnostics → Open Repair Documentation → Open Understanding.**

Open implementation and the official nıu trust domain remain deliberately separate. Third parties may operate compatible systems and their own trust domains; private nıu trust roots are not part of the open-source distribution.

## Current architecture picture

### Already decided / captured in ADRs

- **Carrier = physical device-identity anchor** — [ADR-0001](adr/en/0001-carrier-is-device-identity-anchor.md)
- **Network handover separates transport and Mumble-session transitions** — [ADR-0002](adr/en/0002-network-handover-session-model.md)
- **Open source and trust domains are separate** — [ADR-0003](adr/en/0003-open-source-trust-domains.md)
- **Mumble native, SIP as interoperability layer** — [ADR-0004](adr/en/0004-mumble-native-sip-interoperability.md)
- **Battery is end-user replaceable** — [ADR-0005](adr/en/0005-end-user-replaceable-battery.md)

### Active architecture validation

These items already influence the physical product, but are **not yet accepted architecture decisions**:

- **Compute platform:** replaceable Radxa/Raspberry compute modules; the carrier retains identity, audio, power and product-specific hardware.
- **Compute-independent USB audio:** CT7601CH and XMOS XU316 are being validated as a common USB-audio boundary.
- **Secondary Sub-GHz / LoRa resilience:** an independent MCU-based radio path for small presence, status, call/alarm, tally and recovery messages is a serious V1 hardware candidate. Continuous audio remains IP-based. Product-development work currently favors a local **Direct-LoRa star between Beltpacks and Base** as the strongest protocol candidate; LoRaWAN remains a comparison option. **No ADR yet.** See [`Q-006`](https://github.com/niu-Communications-Platform/product-development/blob/main/%281%29%20questions/Q-006-secondary-sub-ghz-resilience-radio.md).
- **Physical beltpack architecture:** a 105 × 70 mm Core Body with a side-mounted partially recessed replaceable battery and a free Core rear for the belt clip is the current working model; real balance, dock and RF validation remain pending.

Detailed questions, experiments, findings, supplier responses and rejected approaches intentionally live in the separate [`product-development`](https://github.com/niu-Communications-Platform/product-development) repository and are promoted here only once the evidence supports stable architecture or an ADR.

## Start here

- **[Architecture documentation — English](docs/en/README.md)**
- **[Architecture documentation — German / canonical](docs/de/README.md)**
- **[Architecture Decision Records (ADRs) — English](adr/en/README.md)**
- **[Architecture Decision Records (ADRs) — German / canonical](adr/de/README.md)**
- **[Validation and architecture gates](validation/)**
- **[Historical snapshots and source material](archive/)**

## Repository role

This repository defines the platform-wide architecture and the reasoning behind it. Product implementation lives in separate repositories such as `beltpack`, `base`, `cloud` and `factory-tools`.

It intentionally does **not** become a catch-all monorepo for implementation code.

## Documentation model

- [`docs/de/`](docs/de/README.md) — canonical German architecture documentation
- [`docs/en/`](docs/en/README.md) — maintained English translation
- [`adr/de/`](adr/de/README.md) — canonical Architecture Decision Records
- [`adr/en/`](adr/en/README.md) — maintained English ADR translations
- [`validation/`](validation/) — architecture gates, open questions and prototype validation plans
- [`archive/`](archive/) — historical snapshots and preserved source material

## Decision status

Architecture decisions and technical options are classified explicitly:

- `DECIDED` — agreed; change requires deliberate reassessment
- `CANDIDATE` — preferred solution, but not yet sufficiently validated
- `OPTION` — deliberately retained capability or later possibility
- `OPEN` — not yet decided

Documentation also distinguishes theoretical verification from practical prototype validation.

## Current phase

The project is transitioning from functional architecture into **practical architecture validation and physical product architecture**. The goal is not a complete Product Freeze before the first prototype, but an Architecture Gate that removes expensive hardware lock-ins and predictable dead ends before series-oriented development.
