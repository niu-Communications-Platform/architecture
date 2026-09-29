---
status: accepted
date: 2026-09-29
---

# ADR-0007: Open standard and proprietary implementations are separate

[Deutsch — canonical](../de/0007-open-standard-proprietary-implementations.md) | **English**

**Status:** Accepted  
**Date:** 2026-09-29

## Context

nıu.cp is intended to develop as an open, freely implementable communications standard and as the foundation of an interoperable ecosystem. Other manufacturers are explicitly intended to be able to develop compatible products, sell them commercially, and differentiate through their own technical added value.

The shared open standard must therefore be distinguished from a specific product implementation. For example, nıu.cp may specify an audio interface and its behaviour while a manufacturer implements its own noise-cancellation function within its product. Such a product-specific added-value function does not become part of the standard merely because of that implementation.

At the same time, adaptations and further development of the published architecture and specification corpus should remain open and should in principle be able to flow back into the shared standard.

A freely implementable standard must also not become effectively closed because a normative requirement can only be implemented by using a patent for which implementers have not been granted sufficient rights.

## Decision

The official nıu.cp architecture and specification corpus is published openly and is intended to use a ShareAlike license. Adaptations of this licensed corpus that are distributed must remain available under the corresponding open terms.

Implementing an nıu.cp standard, however, does not automatically require disclosure of all implementation details or product-specific added-value features. Manufacturers may in particular develop and commercially use proprietary functionality where its mere existence does not constitute an adaptation of the licensed architecture or specification material.

Interoperable extensions of the shared standard should be openly specifiable and suitable for upstream contribution. The license alone will not be used as a mechanism to force disclosure of every independently developed technical extension of a compatible product.

nıu.cp will not include a normative requirement in the official standard whose implementation depends on a patent unless implementers are granted sufficient patent rights for the standard-essential patent claims. Proprietary or patented product innovations remain explicitly possible where they are not required to create a conformant nıu.cp implementation. A detailed contributor/patent policy may be established when external standardisation contributions begin.

The decision as to which contributions, extensions, or forks become part of the official nıu.cp standard remains with nıu.cp governance. The open-source/open-content license does not grant authority to present a derived specification as the official nıu.cp standard. Naming, trademark, conformity, and certification rights are governed separately from the copyright license.

## Rationale

An open standard should promote competition and interoperability without preventing manufacturers from differentiating through their own product innovations. A proprietary noise-cancellation algorithm, for example, is a legitimate product-level differentiator and does not need to be disclosed merely because the product implements nıu.cp.

Conversely, the shared architecture and specification corpus should not be captured through proprietary adaptations. ShareAlike keeps distributed adaptations of that corpus open and enables their reuse within the ecosystem.

The same openness objective applies at the patent layer for normative requirements: a publicly readable specification would not be freely implementable if its mandatory implementation depended on standard-essential patent claims that were not sufficiently licensed. This does not prevent nıu or other manufacturers from developing optional proprietary and patented added-value features.

Governance and trademark law solve a different problem from licensing: they determine what may be represented as the official nıu.cp standard and, where applicable, as an nıu.cp-conformant implementation.

## Consequences

- Commercial and competing implementations of the nıu.cp standard are explicitly permitted.
- Product-specific added-value functionality may remain proprietary unless a separate license applying to that implementation requires otherwise.
- Distributed adaptations of the licensed architecture/specification corpus remain open under ShareAlike.
- There is no automatic obligation to upstream every independently developed protocol or product extension.
- Normative nıu.cp requirements must not create a patent trap for implementers; sufficient rights to required standard-essential patent claims must be granted.
- Optional proprietary and patented product innovations remain permitted where they are not required for nıu.cp conformity.
- A detailed contributor/patent policy becomes necessary no later than when external parties participate in standardisation.
- Open interoperability is additionally supported through specification, governance, conformity rules, and potentially certification.
- Official adoption of an extension into nıu.cp occurs only through the defined governance process.
- Trademark and naming rights in nıu.cp are not granted by the open-content license.
- Software and hardware implementations may use separately selected licenses appropriate to their respective repositories.
