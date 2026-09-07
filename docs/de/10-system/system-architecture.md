---
language: de
canonical: true
status: current
last_reviewed: 2026-09-07
---

# Systemarchitektur

## Repository-/Komponentengrenzen

Die GitHub-Organization `nıu Communications Platform` ist die technische Projektklammer.

Geplante Haupt-Repositories:

- `architecture` — produktübergreifende Architektur, Entscheidungen, Validierung
- `beltpack` — Gerätehardware und Device Software
- `base` — lokale Appliance/Serverdienste
- `cloud` — gehostete Plattform
- `factory-tools` — Fertigungs-, EOL- und Factory-Provisioning-Werkzeuge

Weitere Repositories wie `shared`, `sdk`, `simulator` oder Apps werden erst angelegt, wenn eine tatsächliche eigenständige Verantwortung entsteht.

## Gemeinsame Architekturabstraktionen

### Capability Layer

Hardware und Betriebssystem melden tatsächliche Fähigkeiten. Profile und Provisioning konsumieren diese Fähigkeiten, statt Hardwarevarianten über CPU-Namen oder Annahmen zu erraten.

Hardwareerkennung unter Linux soll primär über Device Tree (`/proc/device-tree/model`, `compatible`) erfolgen.

Ein Capability Profile kann u. a. enthalten:

- Playback-/Capture-Kanäle
- TDM-Slots
- Split-Ear-Fähigkeit
- unabhängige Ausgänge
- USB-/Bluetooth-Audio
- Board-/PCB-Revision

Profile deklarieren Anforderungen; Provisioning Authority bzw. Device Agent validieren die Kompatibilität.

### Device Agent

Als plattformweite Gerätekomponente ist ein `niu-device-agent` vorgesehen. Verantwortungsbereiche:

- Identity
- Enrollment
- Capabilities
- Provisioning
- Health
- OTA
- Registry Heartbeat

Talkkonnect bleibt primär Intercom-Engine und soll nicht zum allgemeinen Gerätemanager werden.

## Architekturphase

Aktueller Meilenstein ist **P0 Architecture Gate**. Vor dem Prototyp werden teure Hardware-Lock-ins ausreichend geklärt; danach laufen theoretische Architektur und praktische Validierung parallel.
