# Beiträge zur nıu.cp-Architektur

[English](CONTRIBUTING.md) | **Deutsch (kanonisch)**

Beiträge zur Architektur der nıu Communications Platform (`nıu.cp`) sind willkommen. Das Projekt soll offen implementierbar, interoperabel und ausdrücklich auch für unabhängige und konkurrierende Implementierungen geeignet sein.

Dieses Repository enthält die gemeinsame Architektur, Spezifikationen, Architecture Decision Records (ADRs), Validierungsunterlagen und zugehörige Dokumentation. Ein vorgeschlagener oder veröffentlichter Beitrag wird **nicht** allein dadurch Bestandteil des offiziellen nıu.cp-Standards. Die offizielle Aufnahme erfordert die Annahme durch die nıu.cp-Governance.

## Möglichkeiten zur Mitwirkung

Sinnvolle Beiträge sind insbesondere:

- Hinweise auf Unklarheiten, Inkonsistenzen oder technische Fehler;
- technische Evidenz, Messungen, Quellen oder reproduzierbare Experimente;
- Vorschläge für Architektur- oder Spezifikationsänderungen;
- Vorschläge oder Reviews von ADRs;
- Verbesserungen von Interoperabilität oder Implementierungshinweisen;
- Verbesserungen an Dokumentation oder Übersetzungen;
- Pull Requests mit konkreten Änderungen.

Kleine Korrekturen, Übersetzungsverbesserungen, Quellen und Klarstellungen benötigen normalerweise keinen ADR.

## Architekturänderungen

Wesentliche Änderungen an Architektur oder Interoperabilität sollen dem evidenzorientierten Entscheidungsprozess des Projekts folgen:

**Question → Evidence / Experiment → Finding → ADR → Decision**

Nicht jeder Vorschlag muss jede Stufe formal durchlaufen. Der Prozess dient dazu, normative Entscheidungen nachvollziehbar zu halten und Hypothesen, Kandidaten und validierte Architektur voneinander zu unterscheiden.

Bei einem wesentlichen Vorschlag sollten mindestens erläutert werden:

1. das Problem oder die Interoperabilitätslücke;
2. die vorgeschlagene Änderung;
3. vorhandene Evidenz oder Validierung;
4. Auswirkungen auf Kompatibilität und Migration;
5. relevante Auswirkungen auf Security, Datenschutz, Zuverlässigkeit oder Betrieb;
6. bekannte Alternativen und Trade-offs;
7. bekannte Patentansprüche, die für die Implementierung des Vorschlags erforderlich sein könnten.

## Governance

Jeder darf Änderungen vorschlagen. Die Aufnahme in dieses Repository oder die Diskussion in einem Issue definiert für sich genommen nicht den offiziellen nıu.cp-Standard.

Die nıu.cp-Governance entscheidet, welche Beiträge, Erweiterungen und ADRs in den offiziellen Architektur- und Spezifikationsbestand aufgenommen werden. Die Governance kann sich mit dem Projekt und der Contributor-Community weiterentwickeln.

Forks und unabhängige Implementierungen sind unter den jeweils geltenden Lizenzen ausdrücklich zulässig. Die Projektlizenz verleiht kein Recht, einen Fork oder eine abgeleitete Spezifikation als offiziellen nıu.cp-Standard auszugeben, und räumt keine Marken-, Zertifizierungs- oder Konformitätsrechte ein.

Siehe [ADR-0007](adr/de/0007-open-standard-proprietary-implementations.md) zur architektonischen Trennung zwischen offenem Standard, proprietären Implementierungen, Patenten und Governance.

## Lizenzierung von Beiträgen

Soweit eine Datei oder ein Verzeichnis nichts anderes bestimmt, stehen Architektur, Spezifikationen, ADRs und Dokumentation dieses Repositories unter **Creative Commons Attribution-ShareAlike 4.0 International (CC BY-SA 4.0)** gemäß [LICENSE.md](LICENSE.md).

Mit dem Einreichen eines Beitrags erklärst du, dass du berechtigt bist, ihn einzureichen, und stimmst zu, dass der Beitrag unter der Lizenz verbreitet werden darf, die für das Material gilt, zu dem du beiträgst.

Reiche kein Material ein, das du nicht entsprechend lizenzieren darfst. Dazu gehören insbesondere vertrauliche Informationen, proprietäre Dokumentation Dritter, Zugangsdaten, private Schlüssel, Produktionszertifikate oder andere Secrets.

Software, Firmware, Hardware-Designdateien und Tools können ausdrücklich gekennzeichnete separate Lizenzen verwenden.

## Patente und normative Anforderungen

nıu.cp soll frei implementierbar bleiben, ausdrücklich auch durch kommerzielle Wettbewerber.

Wenn dir bekannt ist, dass die Implementierung einer vorgeschlagenen **normativen** Anforderung Patentnutzungsrechte erfordern würde, lege dies bei deinem Vorschlag offen. Ein patentierter Mechanismus soll nicht wissentlich als zwingender Bestandteil des Standards vorgeschlagen werden, während bekannte, für die Implementierung relevante Patentabhängigkeiten verschwiegen werden.

Der derzeitige Architekturgrundsatz lautet, dass nıu.cp keine normative Anforderung aufnimmt, die von einem Patent abhängt, sofern Implementierern nicht ausreichende Rechte an den relevanten standardessentiellen Patentansprüchen eingeräumt werden. Optionale proprietäre oder patentierte Produktfunktionen bleiben möglich, wenn sie für nıu.cp-Konformität nicht erforderlich sind.

Eine detailliertere Contributor- und Patent-Policy kann eingeführt werden, sobald externe Standardisierungsbeteiligung sie erforderlich macht.

## Sprachmodell

Englisch ist die öffentliche Einstiegssprache. Deutsch ist für Architektur- und Produktentscheidungen kanonisch, soweit ein Dokument nichts anderes bestimmt.

Wo ein deutsch/englisches Dokumentpaar existiert, sollen inhaltliche Änderungen beide Fassungen synchron halten. Bei Abweichungen gilt die deutsche kanonische Fassung.

## Sicherheitsprobleme

Bitte veröffentliche ausnutzbare Sicherheitslücken, Zugangsdaten, private Schlüssel, Produktionszertifikate oder vergleichbare sensible Betriebsinformationen nicht in öffentlichen Issues oder Pull Requests.

Eine eigene Richtlinie für Security-Meldungen wird separat in `SECURITY.md` geführt.

## Vor dem Einreichen

Beiträge sollen fokussiert und nachvollziehbar bleiben. Unterscheide klar zwischen gesicherten Fakten, experimentellen Findings, Vorschlägen und Entscheidungen. Historische ADRs sollen erhalten bleiben und nicht stillschweigend umgeschrieben werden; ändert sich eine akzeptierte Entscheidung wesentlich, soll sie durch einen neuen ADR oder eine ausdrückliche Neubewertung abgelöst werden.

Ziel ist nicht Konsens um seiner selbst willen, sondern eine Architektur, deren Entscheidungen für unabhängige Parteien verständlich, überprüfbar und implementierbar bleiben.
