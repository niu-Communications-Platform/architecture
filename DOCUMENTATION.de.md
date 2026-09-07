# Dokumentations- und Repository-Konventionen

**Deutsch — kanonisch** | [English](DOCUMENTATION.md)

Dieses Dokument definiert, wie Architekturwissen in diesem Repository organisiert wird. Die Konventionen gelten für alle Mitwirkenden und sollen sicherstellen, dass Entscheidungen, beschreibende Architektur, Validierungsarbeit und historisches Material langfristig nachvollziehbar bleiben.

> **Die öffentliche Einstiegssprache ist Englisch. Die kanonische Dokumentationssprache ist Deutsch.**

## Maßgebliche Quelle

Das Repository ist die maßgebliche Quelle für dokumentierte Architekturentscheidungen und die technische Dokumentationsstruktur.

Vor Änderungen an Navigation, Verzeichnisstruktur, ADR-Nummerierung oder Dokumentbeziehungen ist der aktuelle Stand des Repositorys zu prüfen. Solche Strukturen sollen nicht aus früheren Diskussionen, externen Notizen oder historischen Snapshots rekonstruiert werden.

Die Git-Historie bewahrt die Entwicklung der Architektur. Bestehende akzeptierte Entscheidungen werden bei einer späteren Richtungsänderung nicht stillschweigend umgeschrieben, sondern gegebenenfalls ausdrücklich durch eine neue Entscheidung ersetzt.

## Sprachen

Deutsch ist die kanonische Sprache der Architekturdokumentation.

- `README.md` ist der englische öffentliche Einstiegspunkt des Repositorys.
- `README.de.md` ist das kanonische deutsche Gegenstück und wird von `README.md` aus verlinkt.
- `DOCUMENTATION.md` ist die gepflegte englische Übersetzung dieser Konventionen.
- `DOCUMENTATION.de.md` ist die kanonische deutsche Fassung dieser Konventionen.
- `docs/de/` enthält die kanonische beschreibende Architekturdokumentation.
- `adr/de/` enthält die kanonischen Architecture Decision Records.
- `docs/en/` und `adr/en/` enthalten gepflegte englische Übersetzungen.
- Englische und deutsche Fassungen verlinken gegenseitig aufeinander.
- Bei Abweichungen ist die kanonische deutsche Fassung maßgeblich.
- Englische Übersetzungen sollen ihre deutsche Quelle und den Übersetzungsstatus in den Dokumentmetadaten ausweisen, soweit diese Konvention im jeweiligen Bereich verwendet wird.

Neue Architekturdokumentation und neue ADRs werden inhaltlich zuerst in der kanonischen deutschen Fassung erstellt. Die englische Fassung wird daraus als gepflegte Übersetzung abgeleitet.

Code, APIs, Bezeichner, Schemas und technische Schnittstellennamen bleiben grundsätzlich englisch, sofern kein sachlicher Grund dagegenspricht.

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

Ein Themenverzeichnis kann mehrere Dokumente enthalten. Die sprachbezogenen `docs/*/README.md`-Seiten navigieren primär zu diesen Themenbereichen und sollen nicht den Eindruck erwecken, dass ein Themenbereich mit einem einzelnen Dokument identisch ist.

Neue nummerierte Themenbereiche auf dieser Ebene sollen nur entstehen, wenn ein Thema nicht sinnvoll in einen bestehenden Bereich passt und voraussichtlich einen eigenständigen Bestand an Architekturdokumentation benötigt.

### `adr/`

Architecture Decision Records dokumentieren folgenreiche Architekturentscheidungen und ihre Begründung.

Ein ADR ist sinnvoll, wenn echte Alternativen bestanden und die gewählte Richtung zukünftige Architektur, Implementierung oder Produktverhalten einschränkt oder prägt.

ADR-Nummern gelten repositoryweit, werden fortlaufend vergeben und niemals für eine andere Entscheidung wiederverwendet. Vor Vergabe einer neuen ADR-Nummer ist der aktuelle Bestand der ADR-Verzeichnisse zu prüfen und die nächste freie Nummer zu verwenden.

Eine spätere Änderung einer akzeptierten Entscheidung wird durch ein neues ADR dokumentiert, das die frühere Entscheidung gegebenenfalls ausdrücklich ersetzt. Historische ADRs verbleiben im Repository.

### `validation/`

Validierungspläne, Architecture Gates, Experimente und Nachweise zur Überprüfung von Annahmen oder Designkandidaten gehören hierher.

Ein noch nicht validierter Kandidat wird nicht allein dadurch zu einer akzeptierten Architekturentscheidung, dass er in einem Validierungsdokument genannt wird.

### `archive/`

Historische Snapshots und abgelöstes konsolidiertes Material, das für die Nachvollziehbarkeit weiterhin nützlich ist, gehört hierher. Archivmaterial ist gegenüber aktuellen Inhalten in `docs/` und `adr/` nicht maßgeblich.

## Architekturdokumentation und Produkt-Repositories

Dieses Repository enthält plattformweite Architektur und Entscheidungen, die mehrere Komponenten betreffen oder das gemeinsame Produktmodell definieren.

Produktspezifische Implementierungsdetails gehören grundsätzlich in das jeweilige Produkt-Repository, sofern sie keine plattformweite Architektur festlegen oder einschränken.

## Navigation

README-Dateien dienen als menschenlesbare Navigation und nicht als duplizierte Architekturspezifikation.

Wenn ein neues Dokument hinzugefügt wird:

1. zuerst die kanonische deutsche Fassung im passenden bestehenden Themenbereich anlegen;
2. die relevante deutsche Navigation aktualisieren, wenn das Dokument von dieser Ebene aus auffindbar sein soll;
3. die gepflegte englische Übersetzung anlegen oder aktualisieren;
4. die entsprechende englische Navigation aktualisieren;
5. Verknüpfungen zwischen kanonischer Fassung und Übersetzung erhalten;
6. sicherstellen, dass die englische Fassung als Übersetzung und die deutsche Fassung als kanonisch gekennzeichnet ist.

Die Navigation muss die tatsächliche Repository-Hierarchie widerspiegeln. Einträge für Verzeichnisse verlinken auf Verzeichnisse; Einträge für einzelne Dokumente auf Dokumente.

## Dokumentstatus

Die Dokumentation soll klar zwischen festgelegter Architektur und offenen Punkten unterscheiden. Bestehende Kennzeichnungen wie `DECIDED`, `OPEN`, `P0 REVIEW`, ADR-Statusfelder und Übersetzungsstatus werden konsistent verwendet, damit Kandidaten nicht als bereits entschiedene Fakten erscheinen.

## Strukturelle Änderungen

Die Repository-Struktur ist selbst Teil der langfristigen Wartbarkeit des Projekts. Vor dem Umbenennen, Verschieben oder Umwidmen eines etablierten Verzeichnisses oder Navigationsbereichs sind bestehende Inhalte und Referenzen zu prüfen und die beabsichtigte Informationsarchitektur zu erhalten.

Ziel ist ein Repository, das verständlich bleibt, ohne auf das Gedächtnis einzelner Mitwirkender oder auf externe Gesprächsverläufe angewiesen zu sein.
