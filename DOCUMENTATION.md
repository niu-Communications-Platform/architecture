# Documentation and Repository Conventions

This document defines how architecture knowledge is organized in this repository. The conventions apply to all contributors and are intended to keep decisions, descriptive architecture, validation work and historical material traceable over time.

## Source of truth

The repository is the authoritative source for documented architecture decisions and technical structure.

Before changing navigation, directory structure, ADR numbering or document relationships, contributors should inspect the current repository state rather than infer it from previous discussions, external notes or historical snapshots.

Git history preserves the evolution of the architecture. Existing accepted decisions are not silently rewritten when their underlying decision changes; they are superseded explicitly where appropriate.

## Languages

German is the canonical language for architecture documentation.

- `docs/de/` contains canonical descriptive architecture documentation.
- `adr/de/` contains canonical Architecture Decision Records.
- `docs/en/` and `adr/en/` contain maintained English translations.
- In case of discrepancies, the canonical German document prevails.
- English translations should identify their German source and translation status in document metadata where that convention is already used.

Code, APIs, identifiers, schemas and technical interface names remain English unless there is a specific reason otherwise.

## Repository areas

### `docs/`

Descriptive architecture: how the platform is structured, which responsibilities exist, and how subsystems interact.

The numbered directories are topic areas, not individual documents:

- `00-product/` — product model and architecture principles
- `10-system/` — system-level architecture and boundaries
- `20-hardware/` — platform-wide hardware architecture and cross-product hardware principles
- `30-software/` — shared software architecture, services and abstractions
- `40-audio/` — audio architecture and routing
- `50-networking/` — networking, transport selection and handover
- `60-identity-security/` — device identity, security, PKI and trust
- `70-provisioning-lifecycle/` — provisioning, ownership and lifecycle
- `80-manufacturing/` — manufacturing, factory provisioning and EOL
- `90-ux-ui/` — product interaction and UX/UI principles

A topic directory may contain multiple documents. The language-level `docs/*/README.md` pages primarily navigate these topic areas and should not imply that a topic area is identical to a single document.

New top-level numbered topic areas should only be introduced when the subject does not reasonably fit an existing area and is expected to contain a distinct body of architecture documentation.

### `adr/`

Architecture Decision Records document consequential decisions and their rationale.

Use an ADR when alternatives existed and the chosen direction constrains future architecture, implementation or product behaviour.

ADR numbers are repository-wide, sequential and never reused for another decision. Before assigning a new ADR number, inspect the current ADR directories and use the next free number.

A later change to an accepted decision is documented through a new ADR that explicitly supersedes the previous one where applicable. Historical ADRs remain in the repository.

### `validation/`

Validation plans, architecture gates, experiments and evidence used to verify assumptions or candidate designs belong here.

An unvalidated candidate should not be presented as an accepted architecture decision merely because it appears in a validation document.

### `archive/`

Historical snapshots and superseded consolidated material that remains useful for traceability belong here. Archive material is not authoritative over current `docs/` and `adr/` content.

## Architecture documentation versus product repositories

This repository contains platform-wide architecture and decisions that affect multiple components or define the common product model.

Product-specific implementation details belong in the corresponding product repository unless they establish or constrain platform-wide architecture.

## Navigation

README files serve as human-readable navigation rather than as duplicate architecture specifications.

When a new document is added:

1. place it in the appropriate existing topic area where possible;
2. update the relevant German navigation if the document should be discoverable from that level;
3. create or update the maintained English translation where appropriate;
4. update the corresponding English navigation;
5. preserve links between canonical and translated documents where metadata conventions support them.

Navigation should reflect the actual repository hierarchy. Directory-level entries should link to directories; document-level entries should link to documents.

## Document status

Documentation should distinguish between established architecture and unresolved work. Existing conventions such as `DECIDED`, `OPEN`, `P0 REVIEW`, ADR status fields and translation status should be used consistently rather than presenting candidates as settled facts.

## Structural changes

Repository structure is itself part of the project's long-term maintainability. Before renaming, moving or repurposing an established directory or navigation category, check existing content and references and preserve the intended information architecture.

The objective is a repository that remains understandable without relying on the memory of any individual contributor or on external conversation history.
