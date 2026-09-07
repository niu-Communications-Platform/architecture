# nıu Communications Platform — Architecture

[Deutsch](README.de.md) | **English**

This repository contains the cross-cutting system architecture, product decisions, technical design principles, architectural decision records (ADRs), validation plans, and historical architecture snapshots of the nıu Communications Platform.

The **German documentation is canonical** for architecture and product decisions. The English documentation is maintained as a translation for collaboration and community exchange. In case of discrepancies, the German version prevails.

## Repository role

This repository defines the platform-wide architecture and the reasoning behind it. Product implementation lives in separate repositories such as `beltpack`, `base`, `cloud`, and `factory-tools`.

It intentionally does **not** become a catch-all monorepo for implementation code.

## Documentation model

- `docs/de/` — canonical German architecture documentation
- `docs/en/` — maintained English translation
- `adr/de/` — canonical Architecture Decision Records
- `adr/en/` — maintained English ADR translations
- `validation/` — architecture gates, open questions, and prototype validation plans
- `archive/` — historical snapshots and preserved source material

## Status

The project is currently in architecture and prototype-preparation phase. Decisions are classified explicitly as `DECIDED`, `CANDIDATE`, `OPTION`, or `OPEN` and are validated practically where necessary before hardware or production lock-in.
