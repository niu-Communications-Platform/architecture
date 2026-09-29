# Contributing to nıu.cp Architecture

**English (public entry language)** | [Deutsch — canonical](CONTRIBUTING.de.md)

Contributions to the nıu Communications Platform (`nıu.cp`) architecture are welcome. The project is intended to be openly implementable, interoperable, and suitable for independent and competing implementations.

This repository contains the shared architecture, specifications, Architecture Decision Records (ADRs), validation material, and related documentation. A contribution being proposed or published does **not** make it part of the official nıu.cp standard. Official adoption requires acceptance through nıu.cp governance.

## Ways to contribute

Useful contributions include:

- reporting ambiguities, inconsistencies, or technical errors;
- providing technical evidence, measurements, references, or reproducible experiments;
- proposing architecture or specification changes;
- proposing or reviewing ADRs;
- improving interoperability or implementation guidance;
- improving documentation or translations;
- submitting pull requests for concrete changes.

Small corrections, translation fixes, references, and clarifications normally do not require an ADR.

## Architecture changes

Substantial architecture or interoperability changes should follow the project's evidence-oriented decision process:

**Question → Evidence / Experiment → Finding → ADR → Decision**

Not every proposal needs to pass through every stage formally. The purpose of this process is to keep normative decisions traceable and to distinguish hypotheses, candidates, and validated architecture.

For a substantial proposal, please explain at least:

1. the problem or interoperability gap;
2. the proposed change;
3. the available evidence or validation;
4. compatibility and migration implications;
5. relevant security, privacy, reliability, or operational implications;
6. known alternatives and trade-offs;
7. any known patent claims that may be required to implement the proposal.

## Governance

Anyone may propose changes. Acceptance into this repository or discussion in an issue does not by itself define the official nıu.cp standard.

The nıu.cp governance decides which contributions, extensions, and ADRs are accepted into the official architecture and specification corpus. Governance may evolve as the project and contributor community grow.

Forks and independent implementations are explicitly permitted under the applicable licenses. The project license does not grant a right to represent a fork or derived specification as the official nıu.cp standard, nor does it grant trademark, certification, or conformity rights.

See [ADR-0007](adr/en/0007-open-standard-proprietary-implementations.md) for the architectural separation between the open standard, proprietary implementations, patents, and governance.

## Licensing of contributions

Unless a file or directory states otherwise, architecture, specifications, ADRs, and documentation in this repository are licensed under **Creative Commons Attribution-ShareAlike 4.0 International (CC BY-SA 4.0)** as described in [LICENSE.md](LICENSE.md).

By submitting a contribution, you represent that you have the right to submit it and agree that the contribution may be distributed under the license applicable to the material you are contributing to.

Do not submit material that you do not have the right to license, including confidential information, third-party proprietary documentation, credentials, private keys, production certificates, or other secrets.

Software, firmware, hardware design files, and tools may use separate licenses where explicitly stated.

## Patents and normative requirements

nıu.cp is intended to remain freely implementable, including by commercial competitors.

If you know that implementing a proposed **normative** requirement would require patent rights, disclose that fact when proposing the change. Do not knowingly propose a patented mechanism as a mandatory part of the standard while withholding known patent dependencies relevant to implementation.

The current architectural principle is that nıu.cp will not adopt a normative requirement that depends on a patent unless implementers are granted sufficient rights to the relevant standard-essential patent claims. Optional proprietary or patented product features remain possible where they are not required for nıu.cp conformity.

A more detailed contributor and patent policy may be adopted when external standardisation participation requires it.

## Language model

English is the public entry language. German is canonical for architecture and product decisions unless a document explicitly states otherwise.

Where a German/English document pair exists, substantive changes should keep both versions synchronized. In case of discrepancy, the German canonical version prevails.

## Security issues

Please do not disclose exploitable security vulnerabilities, credentials, private keys, production certificates, or comparable sensitive operational information in public issues or pull requests.

A dedicated security reporting policy is maintained separately in `SECURITY.md`.

## Before submitting

Please keep contributions focused and traceable. Distinguish clearly between established facts, experimental findings, proposals, and decisions. Preserve historical ADRs rather than silently rewriting past decisions; if an accepted decision changes materially, supersede it through a new ADR or an explicit reassessment.

The goal is not consensus for its own sake, but an architecture whose decisions remain understandable, testable, and implementable by independent parties.
