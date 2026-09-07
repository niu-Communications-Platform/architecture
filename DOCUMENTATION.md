# Documentation and Repository Conventions

**English** | [Deutsch — canonical](DOCUMENTATION.de.md)

> This is the maintained English translation. The German version is canonical.

This document defines how architecture knowledge is organized in this repository. The conventions apply to all contributors and are intended to keep decisions, descriptive architecture, validation work and historical material traceable over time.

> **The public entry language is English. The canonical documentation language is German.**

## Authoritative source

The repository is the authoritative source for documented architecture decisions and the technical documentation structure.

Before changing navigation, directory structure, ADR numbering or document relationships, the current repository state must be inspected. Such structures should not be reconstructed from earlier discussions, external notes or historical snapshots.

Git history preserves the evolution of the architecture. Existing accepted decisions are not silently rewritten when direction changes later; where appropriate, they are explicitly superseded by a new decision.

## Languages

German is the canonical language of the architecture documentation.

- `README.md` is the English public entry point of the repository.
- `README.de.md` is its canonical German counterpart and is linked from `README.md`.
- `DOCUMENTATION.md` is the maintained English translation of these conventions.
- `DOCUMENTATION.de.md` is the canonical German version of these conventions.
- `docs/de/` contains canonical descriptive architecture documentation.
- `adr/de/` contains canonical Architecture Decision Records.
- `docs/en/` and `adr/en/` contain maintained English translations.
- English and German versions visibly link to each other in both directions.
- In case of discrepancies, the canonical German version prevails.

New architecture documentation and new ADRs are written in substance first in the canonical German version. The English version is then derived from it as a maintained translation.

**Changes to canonical German documentation must update the corresponding English translation in the same change set. If this is deliberately not possible, the English version must explicitly be marked with `translation_status: outdated`.**

Code, APIs, identifiers, schemas and technical interface names remain English unless there is a specific reason otherwise.

### Required language metadata

For paired documentation pages under `docs/`:

German version:

```yaml
language: de
canonical: true
status: current
last_reviewed: YYYY-MM-DD
translation: <relative path to the English version>
```

English version:

```yaml
language: en
canonical: false
status: current
last_reviewed: YYYY-MM-DD
source: <relative path to the German version>
translation_status: current
```

ADRs use the same language/canonical model, with `date: YYYY-MM-DD` instead of `last_reviewed`. `translation_status` may be `current`, `outdated`, or `not-translated` where required.

The paths in `translation` and `source` must resolve to the actual counterpart. Both documents must additionally contain a visible Markdown link to each other; metadata alone does not replace the language link.

The workflow `.github/workflows/validate-docs.yml` runs `scripts/validate-docs.py` and checks these machine-verifiable conventions on pushes to `main` and on pull requests.

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

Architecture Decision Records document consequential architecture decisions and their rationale.

Use an ADR when real alternatives existed and the chosen direction constrains or shapes future architecture, implementation or product behaviour.

ADR numbers are repository-wide, sequential and never reused for a different decision. Before assigning a new ADR number, inspect the current ADR directories and use the next free number.

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

README files serve as human-readable navigation rather than duplicate architecture specifications.

When adding a new document:

1. create the canonical German version first in the appropriate existing topic area;
2. update the relevant German navigation if the document should be discoverable from that level;
3. create or update the maintained English translation;
4. update the corresponding English navigation;
5. add metadata and visible language links between canonical source and translation;
6. make sure the documentation validator passes.

Navigation must reflect the actual repository hierarchy. Directory-level entries link to directories; document-level entries link to documents.

## Document status

Documentation should clearly distinguish established architecture from unresolved work. Existing conventions such as `DECIDED`, `OPEN`, `P0 REVIEW`, ADR status fields and translation status should be used consistently so that candidates are not presented as settled facts.

## Structural changes

Repository structure is itself part of the project's long-term maintainability. Before renaming, moving or repurposing an established directory or navigation category, existing content and references must be checked and the intended information architecture preserved.

The objective is a repository that remains understandable without relying on the memory of any individual contributor or on external conversation history.
