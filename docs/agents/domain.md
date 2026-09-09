# Documentation rules

**English** | [Deutsch — canonical](domain.de.md)

## Entry points and storage

Read `README.de.md`, `DOCUMENTATION.de.md`, and `docs/de/README.md` first; maintained English counterparts are available. Then read relevant documents under `docs/de/`, `adr/de/`, and `validation/`. Descriptive architecture stays under `docs/de/` with translations under `docs/en/`; ADRs stay under `adr/de/` and `adr/en/`. Assign new ADR numbers from the current inventory. Explicitly supersede accepted decisions with a new ADR when direction changes. Historical documents in `archive/` do not override current decisions. Run the existing check `python scripts/validate-docs.py` when making changes.

## Context and decisions

Treat each repository as one context. If `CONTEXT.md` exists, read it before domain work and use its terminology. Existing documentation remains the entry point when that file is absent. Do not create an extra context map or parallel ADR directory solely for skill setup.

Read relevant existing decisions before making changes. Explicitly identify conflicts with sources and rationale rather than silently overriding decisions. Distinguish research findings, candidates, and accepted architecture. Prefer links to authoritative documents over duplicating their contents as a second source of truth.

## Repository responsibilities

`product-development` records questions, experiments, and findings. `architecture` contains supported architecture and ADRs. `.github` contains the public presentation. Configuration in one repository does not automatically apply to others; each receives its own configuration.
