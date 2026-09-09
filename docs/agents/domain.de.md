# Dokumentationsregeln

**Deutsch (maßgeblich)** | [English](domain.md)

## Einstieg und Ablage

Zuerst `README.de.md`, `DOCUMENTATION.de.md` und `docs/de/README.md` lesen. Danach die relevanten Dokumente unter `docs/de/`, `adr/de/` und `validation/` lesen. Beschreibende Architektur bleibt unter `docs/de/` mit Übersetzungen unter `docs/en/`; ADRs bleiben unter `adr/de/` und `adr/en/`. Neue ADR-Nummern anhand des aktuellen Bestands vergeben. Akzeptierte Entscheidungen bei Richtungsänderungen ausdrücklich durch einen neuen ADR ablösen. Historische Dokumente in `archive/` haben keinen Vorrang vor aktuellen Entscheidungen. Bei Änderungen den vorhandenen Prüfer `python scripts/validate-docs.py` ausführen.

## Kontext und Entscheidungen

Jedes Repository wird als ein Kontext behandelt. Falls `CONTEXT.md` vorhanden ist, vor fachlicher Arbeit lesen und dessen Begriffe verwenden. Die bestehende Dokumentation bleibt der Einstieg, wenn diese Datei fehlt. Keine zusätzliche Kontextkarte oder parallele ADR-Ablage allein für die Skill-Einrichtung erzeugen.

Vor Änderungen die relevanten bestehenden Entscheidungen lesen. Widersprüche ausdrücklich mit Quelle und Begründung benennen, statt Entscheidungen still zu überschreiben. Forschungsergebnisse, Kandidaten und beschlossene Architektur klar unterscheiden. Links auf die maßgeblichen Dokumente bevorzugen, statt deren Inhalt als zweite Wahrheit zu duplizieren.

## Zusammenarbeit der Repositorys

`product-development` hält Fragen, Experimente und Erkenntnisse fest. `architecture` enthält die begründete Architektur und ADRs. `.github` enthält die öffentliche Darstellung. Die Einrichtung in einem Repository gilt nicht automatisch für andere Repositorys; jedes erhält seine eigene Konfiguration.
