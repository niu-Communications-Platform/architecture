# Documentation and Repository Conventions

**English** | [Deutsch — canonical](DOCUMENTATION.de.md)

> This is the maintained English translation. The German version is canonical.

This document defines how architecture knowledge is organized in this repository. The conventions apply to all contributors and are intended to keep decisions, descriptive architecture, validation work and historical material traceable over time.

> **The public entry language is English. The canonical documentation language is German.**

## Authoritative source

The repository is the authoritative source for documented architecture decisions and the technical documentation structure.

Before changing navigation, directory structure, ADR numbering or document relationships, the current repository state must be inspected. Git history preserves the evolution of the architecture. Existing accepted decisions are not silently rewritten when direction changes later; where appropriate, they are explicitly superseded by a new decision.

## Languages

German is the canonical language of the architecture documentation.

- `README.md` is the English public entry point of the repository.
- `README.de.md` is its canonical German counterpart.
- `DOCUMENTATION.md` is the maintained English translation of these conventions.
- `DOCUMENTATION.de.md` is the canonical German version.
- `docs/de/` contains canonical descriptive architecture documentation.
- `adr/de/` contains canonical Architecture Decision Records.
- `docs/en/` and `adr/en/` contain maintained English translations.
- English and German versions visibly link to each other in both directions.
- In case of discrepancies, the German version prevails.

New architecture documentation and new ADRs are written in substance first in German. The English version is then derived from it as a maintained translation. When a German document changes, its English translation should be maintained alongside it.

The repository structure already carries the language information unambiguously. Therefore `language`, `canonical`, `translation`, `source`, and `translation_status` are not duplicated as metadata.

Likewise, descriptive documentation does not use a generic `status: current` or a manually maintained `last_reviewed`. The current repository state and its change history are provided by Git.

Code, APIs, identifiers, schemas and technical interface names remain English unless there is a specific reason otherwise.

## ADR metadata

ADRs may carry metadata when it represents independent domain information. In particular, these fields are useful:

```yaml
---
status: accepted
date: YYYY-MM-DD
---
```

`status` describes the decision state, for example `proposed`, `accepted`, `superseded`, or `rejected`. `date` is the decision date, not the file modification date.

## Validation

The workflow `.github/workflows/validate-docs.yml` runs `scripts/validate-docs.py`.

The validator checks only robust invariants that can be determined objectively from the current repository state:

- every German document under `docs/` and `adr/` has an English counterpart;
- every English document has a German counterpart;
- both versions visibly link to each other;
- ADR numbers are unique within each language;
- German and English ADR filenames match pairwise;
- ADRs contain a domain-relevant `status` and a valid `date`.

The validator does not try to determine whether the two language versions are semantically identical. Maintaining the translation is an editorial responsibility.

## Repository areas

### `docs/`

Descriptive architecture: how the platform is structured, which responsibilities exist, and how subsystems interact.

The numbered directories are topic areas rather than individual documents:

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

A topic directory may contain multiple documents. New numbered top-level topic areas should only be introduced when the subject does not reasonably fit an existing area and is expected to contain a distinct body of architecture documentation.

### `adr/`

Architecture Decision Records document consequential architecture decisions and their rationale.

Use an ADR when real alternatives existed and the chosen direction constrains or shapes future architecture, implementation or product behaviour.

ADR numbers are repository-wide, sequential and never reused for a different decision. Before assigning a new ADR number, inspect the current ADR set and use the next free number.

A later change to an accepted decision is documented through a new ADR that explicitly supersedes the previous one where applicable. Historical ADRs remain in the repository.

### `validation/`

Validation plans, architecture gates, experiments and evidence used to verify assumptions or candidate designs belong here. An unvalidated candidate does not become an accepted architecture decision merely because it appears in a validation document.

### `archive/`

Historical snapshots and superseded consolidated material that remains useful for traceability belong here. Archive material is not authoritative over current `docs/` and `adr/` content.

## Architecture documentation versus product repositories

This repository contains platform-wide architecture and decisions that affect multiple components or define the common product model. Product-specific implementation details belong in the corresponding product repository unless they establish or constrain platform-wide architecture.

## Navigation

README files serve as human-readable navigation rather than duplicate architecture specifications.

When adding a new document:

1. create the canonical German version first in the appropriate existing topic area;
2. update the relevant German navigation if needed;
3. create the maintained English translation;
4. update the corresponding English navigation;
5. add visible language links between both versions;
6. make sure the documentation validator passes.

Navigation must reflect the actual repository hierarchy.

## Document status

Documentation should clearly distinguish established architecture from unresolved work. Markers such as `DECIDED`, `OPEN`, and `P0 REVIEW` are used in the text where they carry an actual domain meaning.

## Structural changes

Repository structure is itself part of the project's long-term maintainability. Before renaming, moving or repurposing an established directory or navigation category, existing content and references must be checked and the intended information architecture preserved.

The objective is a repository that remains understandable without relying on the memory of any individual contributor or on external conversation history.
