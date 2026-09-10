# nıu Communications Platform — Architektur

**Deutsch** | [English](README.md)

Dieses Repository enthält die produktübergreifende Systemarchitektur, Produktentscheidungen, technischen Gestaltungsprinzipien, Architecture Decision Records (ADRs), Validierungspläne und historische Architektur-Snapshots der nıu Communications Platform.

Die **deutsche Dokumentation ist die kanonische Quelle** für Architektur- und Produktentscheidungen. Die englische Dokumentation wird als gepflegte Übersetzung für Austausch, Zusammenarbeit und eine spätere internationale Community geführt. Bei Abweichungen gilt die deutsche Fassung.

## Was ist die nıu Communications Platform?

Die nıu Communications Platform (`nıu.cp`) ist eine offene Kommunikationsplattform für professionelle Liveproduktion, Broadcast und Events. Das erste Produkt ist ein tragbares Intercom-/IP-Audio-Beltpack mit **Mumble als nativem Echtzeit-Sprachsystem** und SIP als Interoperabilitätsschicht.

Die Plattform ist auf drei Betriebsmodelle ausgelegt:

- **Bare** — Beltpack mit vom Nutzer bereitgestellter Mumble/Murmur-Infrastruktur;
- **Base** — Beltpack plus lokale nıu Base für Mumble/Murmur und Management;
- **Cloud** — Beltpack plus von nıu betriebene Service-Infrastruktur.

Leitidee:

> **Open Source → Open Hardware → Open Diagnostics → Open Repair Documentation → Open Understanding.**

Offene Implementierung und offizielle nıu-Trust-Domain bleiben bewusst getrennt. Dritte dürfen kompatible Systeme und eigene Trust Domains betreiben; private nıu-Trust-Roots sind nicht Teil der Open-Source-Distribution.

## Aktuelles Architekturbild

### Bereits entschieden / in ADRs festgehalten

- **Carrier = physischer Geräteidentitätsanker** — [ADR-0001](adr/de/0001-carrier-is-device-identity-anchor.md)
- **Network-Handover trennt Transport und Mumble-Session** — [ADR-0002](adr/de/0002-network-handover-session-model.md)
- **Open Source und Trust Domains sind getrennt** — [ADR-0003](adr/de/0003-open-source-trust-domains.md)
- **Mumble nativ, SIP als Interoperabilitätsschicht** — [ADR-0004](adr/de/0004-mumble-native-sip-interoperability.md)
- **Akku durch Endnutzer austauschbar** — [ADR-0005](adr/de/0005-end-user-replaceable-battery.md)

### Aktive Architekturvalidierung

Diese Punkte sind wichtig genug, dass sie das physische Produkt bereits beeinflussen, aber noch **keine akzeptierten Architekturentscheidungen** sind:

- **Compute-Plattform:** austauschbare Radxa-/Raspberry-Compute-Module; Carrier behält Identität, Audio, Power und produktspezifische Hardware.
- **Compute-unabhängiges USB Audio:** CT7601CH und XMOS XU316 werden als gemeinsame USB-Audio-Grenze validiert.
- **Secondary Sub-GHz / LoRa Resilience:** ein unabhängiger, MCU-basierter Funkpfad für kleine Presence-, Status-, Call-/Alarm-, Tally- und Recovery-Nachrichten ist ein ernsthafter V1-Hardwarekandidat. Kontinuierliches Audio bleibt IP-basiert. In der Produktentwicklung ist ein lokaler **Direct-LoRa-Star Beltpack ↔ Base** derzeit der stärkste Protokollkandidat; LoRaWAN bleibt Vergleichsoption. **Noch kein ADR.** Siehe [`Q-006`](https://github.com/niu-Communications-Platform/product-development/blob/main/%281%29%20questions/Q-006-secondary-sub-ghz-resilience-radio.de.md).
- **Physische Beltpack-Architektur:** 105 × 70 mm Core Body mit seitlichem, teilversenktem Wechselakku und freier Core-Rückseite für den Beltclip ist das aktuelle Arbeitsmodell; reale Balance-, Dock- und RF-Validierung steht noch aus.

Die detaillierten Fragen, Experimente, Findings, Supplier-Antworten und verworfenen Wege liegen bewusst im separaten [`product-development`](https://github.com/niu-Communications-Platform/product-development)-Repository und werden erst bei ausreichender Evidenz hierher als stabile Architektur bzw. ADR überführt.

## Direkt einsteigen

- **[Architekturdokumentation — Deutsch / kanonisch](docs/de/README.md)**
- **[Architecture documentation — English](docs/en/README.md)**
- **[Architecture Decision Records (ADRs) — Deutsch / kanonisch](adr/de/README.md)**
- **[Architecture Decision Records (ADRs) — English](adr/en/README.md)**
- **[Validierung und Architecture Gates](validation/)**
- **[Historische Snapshots und Quellenmaterial](archive/)**

## Aufgabe dieses Repositories

Dieses Repository beschreibt die plattformweite Architektur und insbesondere die Gründe hinter den Entscheidungen. Die konkrete Implementierung der Produkte liegt später in eigenen Repositories wie `beltpack`, `base`, `cloud` und `factory-tools`.

`architecture` soll ausdrücklich **kein Sammel-Monorepo für Implementierungscode** werden.

## Dokumentationsmodell

- [`docs/de/`](docs/de/README.md) — kanonische deutsche Architekturdokumentation
- [`docs/en/`](docs/en/README.md) — gepflegte englische Übersetzung
- [`adr/de/`](adr/de/README.md) — kanonische Architecture Decision Records
- [`adr/en/`](adr/en/README.md) — gepflegte englische ADR-Übersetzungen
- [`validation/`](validation/) — Architecture Gates, offene Fragen und Prototyp-Validierung
- [`archive/`](archive/) — historische Snapshots und erhaltenes Quellenmaterial

## Entscheidungsstatus

Architekturentscheidungen und technische Optionen werden ausdrücklich klassifiziert:

- `DECIDED` — beschlossen; Änderung erfordert bewusste Neubewertung
- `CANDIDATE` — bevorzugte Lösung, aber noch nicht ausreichend validiert
- `OPTION` — bewusst vorgesehene Fähigkeit oder spätere Möglichkeit
- `OPEN` — noch nicht entschieden

Zusätzlich wird festgehalten, ob eine Aussage nur theoretisch verifiziert wurde oder praktisch im Prototyp validiert werden muss.

## Aktuelle Phase

Das Projekt befindet sich im Übergang von funktionaler Architektur zu **praktischer Architekturvalidierung und physischer Produktarchitektur**. Ziel ist kein vollständiger Product Freeze vor dem ersten Prototyp, sondern ein Architecture Gate, das teure Hardware-Lock-ins und vorhersehbare Sackgassen vor Seriennähe beseitigt.
