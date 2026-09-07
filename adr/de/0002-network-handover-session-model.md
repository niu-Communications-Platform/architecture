---
language: de
canonical: true
status: accepted
date: 2026-09-07
translation: ../en/0002-network-handover-session-model.md
---

# ADR-0002: Netzwerk-Handover trennt Transport- und Mumble-Sessionwechsel

**Deutsch (kanonisch)** | [English](../en/0002-network-handover-session-model.md)

**Status:** Accepted  
**Datum:** 2026-09-07

## Kontext

Das Beltpack kann internes Wi-Fi, USB-Wi-Fi und USB-Ethernet besitzen. Ein Wechsel soll möglichst geringe Unterbrechung verursachen, darf aber nicht zu zwei gleichzeitigen Mumble-Sitzungen derselben Beltpack-Identität führen.

## Entscheidung

**Make-before-break auf Netzwerktransportebene; break-before-make auf Mumble-Sessionebene.**

Ein Kandidatentransport wird vollständig aufgebaut und validiert. Die bestehende Mumble-Session bleibt bis dahin auf PRIMARY. Nach erfolgreicher Validierung wird die alte Mumble-Session beendet, der Kandidat PRIMARY und die Session über den neuen Transport neu aufgebaut.

## Begründung

Damit wird die unvermeidbare Intercom-Unterbrechung auf den Session-Reconnect begrenzt, ohne doppelte logische Clients zu erzeugen. Netzwerkverfügbarkeit kann vor dem eigentlichen Wechsel geprüft werden.

## Konsequenzen

- Network Manager und Talkkonnect/Intercom Engine haben getrennte Verantwortlichkeiten.
- Interfaces dürfen während der Kandidatenprüfung parallel IP-Konnektivität besitzen.
- Gleiche IP/MAC darf nicht parallel auf zwei Interfaces verwendet werden.
- Handover-Unterbrechung wird ein messbarer Prototype-KPI.

## Validierungsbedarf

Praktische Messung mit internem Wi-Fi, USB-Wi-Fi und USB-Ethernet sowie unterschiedlichen Mumble-Netzbedingungen.
