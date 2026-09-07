---
language: de
canonical: true
status: accepted
date: 2026-09-07
translation: ../en/0003-open-source-trust-domains.md
---

# ADR-0003: Open Source und Trust Domain sind getrennt

**Deutsch (kanonisch)** | [English](../en/0003-open-source-trust-domains.md)

**Status:** Accepted  
**Datum:** 2026-09-07

## Kontext

Die gesamte Plattform soll Open Source und selbst betreibbar sein. Gleichzeitig müssen offizielle nıu-Geräte, Firmware, Provisioning Authorities und Cloud-Dienste kryptographisch authentifizierbar bleiben. Offenlegung des Quellcodes darf keine Möglichkeit schaffen, einen fremden Dienst als offiziellen nıu-Dienst auszugeben.

## Entscheidung

Die Implementierung ist offen, Trust Roots und private Betriebs-/Signaturschlüssel sind es nicht.

Offizielle nıu-Builds und -Dienste verwenden nıu Trust Domains. Dritte dürfen dieselbe Implementierung mit eigenen Device PKIs, Service PKIs, Firmware-Signing-Schlüsseln und Provisioning Authorities betreiben.

Ein Gerät akzeptiert einen alternativen Trust Domain nur nach autorisierter Vertrauenskonfiguration durch den Owner bzw. die vorgesehene Developer-/Custom-Trust-Policy.

## Begründung

Damit bleiben Selbsthosting, Forks, Reparierbarkeit und Fortbetrieb unabhängig vom Hersteller möglich, ohne die Authentizität offizieller nıu-Dienste aufzugeben.

## Konsequenzen

- Trust Stores und Signer müssen abstrahiert werden.
- Device PKI, Service PKI und Firmware Signing bleiben getrennt.
- Markenrechte und Softwarelizenzen werden getrennt behandelt.
- Base/Cloud-Protokolle dürfen nicht auf Security by Obscurity beruhen.
