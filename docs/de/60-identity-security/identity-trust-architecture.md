---
language: de
canonical: true
status: current
last_reviewed: 2026-09-07
---

# Identity- und Trust-Architektur

## Vier Identitäten

1. **Factory/Device Identity** — physisches Beltpack, unveränderlich und Carrier-gebunden.
2. **Friendly/Provisioned Identity** — menschlicher Name, Rolle und Profile; veränderbar/übertragbar.
3. **Mumble/Intercom Identity** — Service-Identität und Zertifikate; getrennt und rotierbar.
4. **Network/Service Identity** — Hostname, IP, MAC und aktueller Transport; flüchtig.

**DECIDED:** Factory Identity lebt auf dem Carrier, nicht auf SD/eMMC oder SBC.

## Carrier Identity

Der Carrier enthält bzw. bindet:

- Device UUID
- sichtbare Seriennummer
- Secure Element
- Carrier-NVM

SBC-/Storage-Tausch erhält die physische Geräteidentität. Carrier-Tausch erzeugt ein neues physisches Gerät. Friendly Identity und Profile können im RMA-Prozess auf ein Ersatzgerät übertragen werden.

## Secure Element

**CANDIDATE:** Microchip ATECC608C-TFLXTLS / TrustFLEX.

Getrennte Schlüsselrollen sind vorgesehen für Device Root, Mumble/Service und Cloud/Auth. Private Schlüssel verlassen das Secure Element nicht.

Software abstrahiert Schlüsselzugriff über einen `KeyProvider`, mit Datei-Provider für Entwicklung und Hardware-Provider für Produktion.

## PKI

Device PKI, Service PKI und Firmware Signing sind strikt getrennte Trust-Bereiche.

- Device Issuing CA → langfristige Device Certificates
- Base lokale Mumble CA → lokaler Trust Domain
- Cloud Service/Mumble CA → gehosteter Trust Domain
- Firmware Signing → eigene Signaturkette

Service-Keys werden bei Enrollment erzeugt und sind rotierbar.

## Open Source und Trust Domains

**DECIDED:** Open Source gewährt Implementierungsfreiheit, aber nicht nıu-Identität oder nıu-Vertrauen.

Dritte dürfen eigene Base-/Cloud-Systeme mit eigenen Trust Roots betreiben. Ein alternatives Backend wird nur akzeptiert, wenn der Owner dessen Provisioning-/Service-Trust ausdrücklich autorisiert.

Das allgemeine Modell lautet:

`Device UUID → Owner → Deployment → Provisioning Authority → Trust Domain`

Eine höhere Provisioning-Revision ersetzt niemals fehlendes Vertrauen in den Signer.
