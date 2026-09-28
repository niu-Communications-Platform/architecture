# Systemarchitektur

**Deutsch (kanonisch)** | [English](../../en/10-system/system-architecture.md)

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

### Cloud-Mandantentopologie

Für nıu.cp Cloud ist der **Murmur Virtual Server die technische Standard-Mandantengrenze**. Ein Murmur-Prozess darf mehrere virtuelle Server und damit mehrere Cloud-Tenants betreiben.

Die logische Zuordnung lautet:

- Tenant / Kunde → Murmur Virtual Server
- Projekt / Produktion / Arbeitsbereich → Channel bzw. Channel Tree
- Rolle / Funktion → Murmur Group und ACL
- Benutzer / Gerät → authentifizierte Identität

Die Cloud Control Plane verwaltet die Zuordnung `tenant → Murmur node → virtual server`. Administrative Murmur-Schnittstellen bleiben intern und werden nicht direkt an Mandanten exponiert. Eigene Prozesse, Container oder Hosts können bei besonderen Isolationsanforderungen zusätzlich eingesetzt werden.

Verbindliche Architekturentscheidung: [ADR-0006: Murmur Virtual Server bilden die Cloud-Mandantengrenze](../../../adr/de/0006-cloud-tenant-boundary-murmur-virtual-server.md).

## Hard-Power-Loss-Toleranz

**DECIDED:** Abrupter Verlust der Versorgung ist ein zulässiger Betriebs- und Fehlerfall. Das gilt insbesondere für die schnelle Entnahme des austauschbaren Akkus sowie für Hard-Off und unerwarteten Spannungsverlust.

Das System muss so entworfen werden, dass wiederholter Hard Power Loss weder die Geräteidentität noch kritische Konfiguration dauerhaft beschädigt und das Gerät beim nächsten Start selbstständig in einen konsistenten Zustand zurückkehrt.

Daraus folgen insbesondere:

- power-loss-sichere persistente Zustandsänderungen;
- Minimierung unnötiger Flash-/eMMC-Schreibvorgänge;
- A/B-OTA mit Validierung und Rollback auch bei Unterbrechung während des Updates;
- keine ausschließliche Ablage unverzichtbarer Factory-/Identity-Daten auf SBC-Storage;
- definierte Recovery-Pfade für beschädigte Runtime-/Cache-Daten;
- praktische wiederholte Power-Cut-Tests einschließlich ungünstiger Zeitpunkte während Konfigurations- und Updatevorgängen.

Ein geordneter Shutdown bleibt der Normalfall. Die Integrität des Produkts darf jedoch nicht von ihm abhängen.

## Architekturphase

Aktueller Meilenstein ist **P0 Architecture Gate**. Vor dem Prototyp werden teure Hardware-Lock-ins ausreichend geklärt; danach laufen theoretische Architektur und praktische Validierung parallel.
