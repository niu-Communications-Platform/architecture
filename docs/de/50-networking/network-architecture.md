---
language: de
canonical: true
status: current
last_reviewed: 2026-09-07
translation: ../../en/50-networking/network-architecture.md
---

# Netzwerkarchitektur

**Deutsch (kanonisch)** | [English](../../en/50-networking/network-architecture.md)

## Transportklassen

Vorgesehen sind zunächst:

- `internal_wifi`
- `usb_wifi`
- `usb_ethernet`

später optional `usb_tethering` und `usb_cellular`.

Eine konzeptuelle Default-Priorität ist USB Ethernet → USB Wi-Fi → internes Wi-Fi; die tatsächliche Reihenfolge ist policy-gesteuert.

## Network Manager

Transportauswahl und Failover gehören in einen eigenen Network Manager. Talkkonnect soll nicht selbstständig konkurrierende Transportentscheidungen treffen.

Transportzustände:

`ABSENT`, `PRESENT`, `CONNECTING`, `LINKED`, `IP_READY`, `VALIDATING`, `USABLE`, optional `DEGRADED`, `FAILED`, `COOLDOWN`.

Rollen:

`NONE`, `CANDIDATE`, `PRIMARY`.

Health-Hierarchie:

LINK → IP → ROUTE → SERVER → INTERCOM.

## Handover

**DECIDED:** Make-before-break auf Transportebene; break-before-make auf Mumble-Sessionebene.

Ein neuer bevorzugter Transport wird vollständig aufgebaut und validiert, während die bestehende Mumble-Verbindung noch über PRIMARY läuft. Erst nach `USABLE` wird die alte Mumble-Session beendet, der neue Transport PRIMARY und die Intercom-Sitzung mit derselben logischen Identität neu aufgebaut.

Es darf keine zwei parallelen Mumble-Sitzungen desselben Beltpacks geben.

Nach erfolgreicher Übernahme kann der alte Transport deaktiviert werden. Bei plötzlichem Verlust eines externen Adapters erfolgt naturgemäß Break-before-make-Fallback auf internes Wi-Fi.

Konfiguration des internen Wi-Fi bleibt beim temporären Deaktivieren erhalten.
