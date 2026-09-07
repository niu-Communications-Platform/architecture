# Dokumentations- und Repository-Konventionen

**Deutsch — kanonisch** | [English](DOCUMENTATION.md)

Dieses Dokument definiert, wie Architekturwissen in diesem Repository organisiert wird. Die Konventionen gelten für alle Mitwirkenden und sollen sicherstellen, dass Entscheidungen, beschreibende Architektur, Validierungsarbeit und historisches Material langfristig nachvollziehbar bleiben.

> **Die öffentliche Einstiegssprache ist Englisch. Die kanonische Dokumentationssprache ist Deutsch.**

## Maßgebliche Quelle

Das Repository ist die maßgebliche Quelle für dokumentierte Architekturentscheidungen und die technische Dokumentationsstruktur.

Vor Änderungen an Navigation, Verzeichnisstruktur, ADR-Nummerierung oder Dokumentbeziehungen ist der aktuelle Stand des Repositorys zu prüfen. Die Git-Historie bewahrt die Entwicklung der Architektur. Bestehende akzeptierte Entscheidungen werden bei einer späteren Richtungsänderung nicht stillschweigend umgeschrieben, sondern gegebenenfalls ausdrücklich durch eine neue Entscheidung ersetzt.

## Sprachen

Deutsch ist die kanonische Sprache der Architekturdokumentation.

- `README.md` ist der englische öffentliche Einstiegspunkt des Repositorys.
- `README.de.md` ist das kanonische deutsche Gegenstück.
- `DOCUMENTATION.md` ist die gepflegte englische Übersetzung dieser Konventionen.
- `DOCUMENTATION.de.md` ist die kanonische deutsche Fassung.
- `docs/de/` enthält die kanonische beschreibende Architekturdokumentation.
- `adr/de/` enthält die kanonischen Architecture Decision Records.
- `docs/en/` und `adr/en/` enthalten gepflegte englische Übersetzungen.
- Englische und deutsche Fassungen verlinken sichtbar und gegenseitig aufeinander.
- Bei Abweichungen ist die deutsche Fassung maßgeblich.

Neue Architekturdokumentation und neue ADRs werden inhaltlich zuerst auf Deutsch erstellt. Die englische Fassung wird daraus als gepflegte Übersetzung abgeleitet. Bei Änderungen an einem deutschen Dokument soll die zugehörige englische Übersetzung mitgepflegt werden.

Die Repository-Struktur trägt die Sprachinformation bereits eindeutig. Deshalb werden `language`, `canonical`, `translation`, `source` und `translation_status` nicht zusätzlich als Metadaten geführt.

Auch ein generischer Dokumentstatus wie `status: current` und ein manuell gepflegtes `last_reviewed` werden für beschreibende Dokumentation nicht verwendet. Der aktuelle Repository-Zustand und seine Änderungshistorie ergeben sich aus Git.

Code, APIs, Bezeichner, Schemas und technische Schnittstellennamen bleiben grundsätzlich englisch, sofern kein sachlicher Grund dagegenspricht.

## ADR-Metadaten

ADRs dürfen Metadaten führen, wenn diese eigenständige fachliche Information enthalten. Insbesondere sind sinnvoll:

```yaml
---
status: accepted
date: YYYY-MM-DD
---
```

`status` beschreibt den Entscheidungsstatus, beispielsweise `proposed`, `accepted`, `superseded` oder `rejected`. `date` bezeichnet das Entscheidungsdatum und nicht das Änderungsdatum der Datei.

## Validierung

Der Workflow `.github/workflows/validate-docs.yml` führt `scripts/validate-docs.py` aus.

Der Validator prüft ausschließlich robuste Invarianten, die sich objektiv aus dem aktuellen Repository-Zustand bestimmen lassen:

- jedes deutsche Dokument unter `docs/` und `adr/` besitzt ein englisches Gegenstück;
- jedes englische Dokument besitzt ein deutsches Gegenstück;
- beide Fassungen verlinken sichtbar und gegenseitig aufeinander;
- ADR-Nummern sind innerhalb einer Sprache eindeutig;
- deutsche und englische ADR-Dateinamen stimmen paarweise überein;
- ADRs enthalten einen fachlichen `status` und ein gültiges `date`.

Der Validator versucht nicht festzustellen, ob zwei Sprachfassungen semantisch exakt denselben Inhalt haben. Die Pflege der Übersetzung ist eine redaktionelle Verantwortung.

## Repository-Bereiche

### `docs/`

Beschreibende Architektur: Aufbau der Plattform, Verantwortlichkeiten und Zusammenspiel der Subsysteme.

Die nummerierten Verzeichnisse sind Themenbereiche und keine einzelnen Dokumente:

- `00-product/` — Produktmodell und Architekturprinzipien
- `10-system/` — Systemarchitektur und Systemgrenzen
- `20-hardware/` — plattformweite Hardwarearchitektur und produktübergreifende Hardwareprinzipien
- `30-software/` — gemeinsame Softwarearchitektur, Dienste und Abstraktionen
- `40-audio/` — Audioarchitektur und Routing
- `50-networking/` — Netzwerk, Transportauswahl und Handover
- `60-identity-security/` — Geräteidentität, Sicherheit, PKI und Trust
- `70-provisioning-lifecycle/` — Provisioning, Ownership und Lifecycle
- `80-manufacturing/` — Fertigung, Factory Provisioning und EOL
- `90-ux-ui/` — Produktbedienung und UX-/UI-Prinzipien

Ein Themenverzeichnis kann mehrere Dokumente enthalten. Neue nummerierte Themenbereiche auf dieser Ebene sollen nur entstehen, wenn ein Thema nicht sinnvoll in einen bestehenden Bereich passt und voraussichtlich einen eigenständigen Bestand an Architekturdokumentation benötigt.

### `adr/`

Architecture Decision Records dokumentieren folgenreiche Architekturentscheidungen und ihre Begründung.

Ein ADR ist sinnvoll, wenn echte Alternativen bestanden und die gewählte Richtung zukünftige Architektur, Implementierung oder Produktverhalten einschränkt oder prägt.

ADR-Nummern gelten repositoryweit, werden fortlaufend vergeben und niemals für eine andere Entscheidung wiederverwendet. Vor Vergabe einer neuen ADR-Nummer ist der aktuelle Bestand zu prüfen und die nächste freie Nummer zu verwenden.

Eine spätere Änderung einer akzeptierten Entscheidung wird durch ein neues ADR dokumentiert, das die frühere Entscheidung gegebenenfalls ausdrücklich ersetzt. Historische ADRs verbleiben im Repository.

### `validation/`

Validierungspläne, Architecture Gates, Experimente und Nachweise zur Überprüfung von Annahmen oder Designkandidaten gehören hierher. Ein noch nicht validierter Kandidat wird nicht allein dadurch zu einer akzeptierten Architekturentscheidung, dass er in einem Validierungsdokument genannt wird.

### `archive/`

Historische Snapshots und abgelöstes konsolidiertes Material, das für die Nachvollziehbarkeit weiterhin nützlich ist, gehört hierher. Archivmaterial ist gegenüber aktuellen Inhalten in `docs/` und `adr/` nicht maßgeblich.

## Architekturdokumentation und Produkt-Repositories

Dieses Repository enthält plattformweite Architektur und Entscheidungen, die mehrere Komponenten betreffen oder das gemeinsame Produktmodell definieren. Produktspezifische Implementierungsdetails gehören grundsätzlich in das jeweilige Produkt-Repository, sofern sie keine plattformweite Architektur festlegen oder einschränken.

## Navigation

README-Dateien dienen als menschenlesbare Navigation und nicht als duplizierte Architekturspezifikation.

Wenn ein neues Dokument hinzugefügt wird:

1. zuerst die kanonische deutsche Fassung im passenden bestehenden Themenbereich anlegen;
2. die relevante deutsche Navigation aktualisieren, wenn nötig;
3. die gepflegte englische Übersetzung anlegen;
4. die entsprechende englische Navigation aktualisieren;
5. sichtbare Sprachlinks zwischen beiden Fassungen setzen;
6. den Dokumentations-Validator erfolgreich durchlaufen lassen.

Die Navigation muss die tatsächliche Repository-Hierarchie widerspiegeln.

## Dokumentstatus

Die Dokumentation soll fachlich klar zwischen festgelegter Architektur und offenen Punkten unterscheiden. Kennzeichnungen wie `DECIDED`, `OPEN` und `P0 REVIEW` werden im Text dort verwendet, wo sie tatsächlich eine fachliche Aussage treffen.

## Strukturelle Änderungen

Die Repository-Struktur ist selbst Teil der langfristigen Wartbarkeit des Projekts. Vor dem Umbenennen, Verschieben oder Umwidmen eines etablierten Verzeichnisses oder Navigationsbereichs sind bestehende Inhalte und Referenzen zu prüfen und die beabsichtigte Informationsarchitektur zu erhalten.

Ziel ist ein Repository, das verständlich bleibt, ohne auf das Gedächtnis einzelner Mitwirkender oder auf externe Gesprächsverläufe angewiesen zu sein.
