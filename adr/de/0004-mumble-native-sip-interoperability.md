---
language: de
canonical: true
status: accepted
date: 2026-09-07
translation: ../../en/0004-mumble-native-sip-interoperability.md
---

# ADR-0004: Mumble als natives Echtzeit-Sprachprotokoll, SIP als Interoperabilitätsschicht

## Status

**ACCEPTED**

## Kontext

Die nıu Communications Platform ist primär ein professionelles Intercom- und Gruppenkommunikationssystem und keine Telefonanlage. Typische Kommunikationsbeziehungen bestehen dauerhaft zwischen Rollen, Gruppen und Talkgroups; Sprache wird über PTT, Channels und gezielte Sprechziele geroutet.

Für diese Architektur kommen insbesondere Mumble/Murmur und SIP-basierte Systeme in Betracht. SIP ist in Telefonie, Unified Communications und vielen professionellen Infrastrukturen weit verbreitet und bietet ein großes Ökosystem für PBX-, Telefon- und Gateway-Integration. Sein Grundmodell ist jedoch stärker auf Signalisierung und den Aufbau von Kommunikationssitzungen ausgerichtet. Für ein Intercom wären zusätzliche Komponenten und eigene Logik für Gruppenkommunikation, PTT, Talkgroups, Routing und Konferenz-/Matrixfunktionen erforderlich.

Mumble/Murmur stellt dagegen bereits ein dauerhaft verbundenes, latenzarmes Gruppenkommunikationsmodell mit Channels, ACLs und gezielten Voice Targets bereit. Dieses Modell entspricht dem Kernverhalten der nıu Communications Platform deutlich unmittelbarer.

Ein wesentliches zusätzliches Argument ist Talkkonnect. Talkkonnect ist ein headless Mumble-PTT-Client für Hardware-Appliances und bringt bereits zahlreiche für nıu relevante Mechanismen mit, darunter PTT, Hardwaresteuerung, Voice Targets, API-Anbindung und Provisionierungsfunktionen. Dadurch kann nıu auf einer bestehenden Intercom-nahen Engine aufbauen, statt einen vollständigen Endpoint-Stack neu zu entwickeln.

## Entscheidung

**Mumble ist das native Echtzeit-Sprachprotokoll der nıu Communications Platform. Murmur ist die bevorzugte Serverbasis für die native Intercom-Kommunikation.**

Talkkonnect wird als wichtige Intercom-Engine bzw. Integrationsbasis betrachtet. Die darüberliegende nıu-Architektur – insbesondere Device Identity, Ownership, Provisioning, Capability Management, Audio Routing, OTA, Health und UX – bleibt davon getrennt und darf nicht unnötig an Talkkonnect gekoppelt werden.

**SIP wird ausdrücklich nicht ausgeschlossen. SIP ist jedoch ein Interoperabilitätsprotokoll und nicht das native Geräteprotokoll.**

SIP-Anbindung soll bei Bedarf vorzugsweise zentral über Base-, Cloud- oder Gateway-Komponenten erfolgen, statt SIP zur Grundlage jedes Beltpacks zu machen.

Konzeptionell:

```text
nıu Beltpacks / native clients
            │
       Mumble protocol
            │
     Murmur / nıu Base
            │
     interoperability
       gateway layer
       ├── SIP
       ├── RTP
       └── weitere externe Systeme
```

## Begründung

Mumble passt zum nativen nıu-Kommunikationsmodell insbesondere durch:

- dauerhafte Client-Server-Verbindungen statt primär anruforientierter Sitzungen,
- latenzarme Sprachübertragung,
- Channels und Gruppenkommunikation,
- ACLs und Teilnehmerrechte,
- gezielte Voice Targets für unterschiedliche Sprechwege,
- gute Eignung für PTT-basierte Bedienung,
- einfache lokale und selbst gehostete Murmur-Instanzen,
- Eignung für Base- und Cloud-Betrieb,
- die vorhandene Talkkonnect-Implementierung als Hardware-/PTT-nahe Basis.

SIP bleibt gleichzeitig strategisch relevant, insbesondere für:

- PBX-Integration,
- SIP-Telefone und Softphones,
- bestehende Enterprise-Kommunikationsinfrastruktur,
- Telefonie,
- Paging- und Gateway-Systeme,
- Interoperabilität mit Fremdsystemen.

Die Architektur trennt daher bewusst **native Kommunikation** von **externer Interoperabilität**.

## Konsequenzen

### Positiv

- Der Beltpack-Stack bleibt auf das eigentliche Intercom-Problem zugeschnitten.
- Talkkonnect kann als bestehende, erprobte Grundlage genutzt werden.
- Base kann mit Murmur vergleichsweise kompakt lokal betrieben werden.
- Bare-, Base- und Cloud-Szenarien können auf demselben nativen Kommunikationsmodell aufbauen.
- SIP und weitere Protokolle können später ergänzt werden, ohne alle Endgeräte umzubauen.
- Die Open-Source- und Self-Hosting-Strategie bleibt erhalten.

### Negativ / Trade-offs

- Mumble besitzt nicht die universelle Industrie-Interoperabilität von SIP.
- Direkte Integration in bestehende PBX-/UC-Umgebungen erfordert Gateways oder Bridges.
- nıu muss die Grenzen und Erweiterungsmöglichkeiten des Mumble-Protokolls sowie Talkkonnect im Prototyp intensiv validieren.
- Bei Anforderungen, die über Mumbles Kommunikationsmodell hinausgehen, kann eigene Protokoll-, Audio- oder Routinglogik erforderlich werden.

## Architekturregel

> Mumble is the native real-time voice protocol of the nıu Communications Platform. SIP is an interoperability protocol, not the native device protocol.

Diese Aussage beschreibt die aktuelle Architekturentscheidung, nicht die Verpflichtung, sämtliche zukünftige Kommunikation ausschließlich über Mumble abzuwickeln.

## Zu validieren

Vor dem P0 Architecture Gate sind insbesondere praktisch zu prüfen:

- reale End-to-End-Latenz im lokalen Produktionsnetz,
- PTT-Latenz und Verhalten bei schnellen Sprecherwechseln,
- Voice Targets und deren Steuerung über Talkkonnect,
- mehrere gleichzeitige Hör- und Sprechwege,
- Verhalten bei Netzwerk-Handover und kurzzeitigen Mehrfachsessions,
- Audioqualität und Opus-Konfiguration,
- Skalierung auf realistische Teilnehmerzahlen,
- Trennung zwischen Talkkonnect und nıu Audio Engine,
- mögliche SIP-/RTP-Gateway-Pfade für spätere Interoperabilität.
