# nıu Communications Platform — Architektur

**Deutsch** | [English](README.md)

Dieses Repository enthält die produktübergreifende Systemarchitektur, Produktentscheidungen, technischen Gestaltungsprinzipien, Architecture Decision Records (ADRs), Validierungspläne und historische Architektur-Snapshots der nıu Communications Platform.

Die **deutsche Dokumentation ist die kanonische Quelle** für Architektur- und Produktentscheidungen. Die englische Dokumentation wird als gepflegte Übersetzung für Austausch, Zusammenarbeit und eine spätere internationale Community geführt. Bei Abweichungen gilt die deutsche Fassung.

## Aufgabe dieses Repositories

Dieses Repository beschreibt die plattformweite Architektur und insbesondere die Gründe hinter den Entscheidungen. Die konkrete Implementierung der Produkte liegt später in eigenen Repositories wie `beltpack`, `base`, `cloud` und `factory-tools`.

`architecture` soll ausdrücklich **kein Sammel-Monorepo für Implementierungscode** werden.

## Dokumentationsmodell

- `docs/de/` — kanonische deutsche Architekturdokumentation
- `docs/en/` — gepflegte englische Übersetzung
- `adr/de/` — kanonische Architecture Decision Records
- `adr/en/` — gepflegte englische ADR-Übersetzungen
- `validation/` — Architecture Gates, offene Fragen und Prototyp-Validierung
- `archive/` — historische Snapshots und erhaltenes Quellenmaterial

## Entscheidungsstatus

Architekturentscheidungen und technische Optionen werden ausdrücklich klassifiziert:

- `DECIDED` — beschlossen; Änderung erfordert bewusste Neubewertung
- `CANDIDATE` — bevorzugte Lösung, aber noch nicht ausreichend validiert
- `OPTION` — bewusst vorgesehene Fähigkeit oder spätere Möglichkeit
- `OPEN` — noch nicht entschieden

Zusätzlich soll festgehalten werden, ob eine Aussage nur theoretisch verifiziert wurde oder praktisch im Prototyp validiert werden muss.

## Aktuelle Phase

Das Projekt befindet sich in der Architektur- und Prototyp-Vorbereitungsphase. Ziel ist kein vollständiger Product Freeze vor dem ersten Prototyp, sondern ein **Architecture Gate**, das teure Hardware-Lock-ins und vorhersehbare Sackgassen vor Beginn der praktischen Entwicklung beseitigt.
