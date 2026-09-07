# Reparierbarkeit und Ressourcenschonung

**Deutsch (kanonisch)** | [English](../../en/20-hardware/repairability-sustainability.md)

## Ziel

Die Hardwarearchitektur soll die Lebensdauer des Beltpacks maximieren und verhindern, dass der Defekt einer einzelnen Komponente unnötig zum Austausch des gesamten Produkts führt.

## Architekturprinzipien

**DECIDED:** Der Ausfall einer einzelnen nicht-strukturellen Komponente soll grundsätzlich nicht den Austausch des gesamten Beltpacks erzwingen.

**DECIDED:** Repariert oder ersetzt wird die kleinste technisch, ökologisch und wirtschaftlich sinnvolle Funktionseinheit.

**DECIDED:** Reparaturen sollen Device Identity und Provisionierung erhalten, soweit dies technisch möglich und sicher ist.

**DECIDED:** Bauteilreparatur wird bevorzugt, wenn sie sinnvoll ist. Modultausch wird bevorzugt, wenn Bauteilreparatur unverhältnismäßigen Arbeits-, Energie-, Geräte- oder Schadensaufwand verursacht.

**DECIDED:** Diagnose- und Reparaturwissen wird nicht künstlich als Herstellergeheimnis behandelt. Qualifizierte unabhängige Reparatur soll durch öffentlich verfügbare Dokumentation und Werkzeuge praktisch möglich sein.

## Reparaturebenen

### Level 1 — End User Replaceable

Komponenten, deren Austausch der Endnutzer sicher selbst durchführen können soll bzw. rechtlich können muss.

- Akku
- ggf. Gürtelclip und einfache mechanische Teile

Der Akku ist gemäß ADR-0005 verbindlich als End-User Replaceable Unit auszulegen.

### Level 2 — Service Replaceable Module

Austausch nach Öffnen des Geräts mit üblichen Servicearbeiten, vorzugsweise über Steckverbinder statt Löten.

Beispiele:

- SBC / Compute-Modul
- Display
- Speaker
- Mikrofonmodule
- gegebenenfalls mechanisch belastete I/O-Tochterplatinen

### Level 3 — Board-Level Repair

Spezialisierte Reparatur auf dem Carrier-PCB.

Beispiele:

- Audio-Codecs
- USB-Hub
- Lade-/Power-Controller
- Buchsen, soweit nicht auf Tochterplatine
- Secure Element
- Carrier-NVM

### Level 4 — Carrier Replacement

Der komplette nıu Carrier wird nur ersetzt, wenn Board-Level-Reparatur technisch oder wirtschaftlich nicht sinnvoll ist. Ein Carrier-Tausch hat besondere Auswirkungen auf die Factory/Device Identity und benötigt einen kontrollierten Replace-Device-Prozess.

### Level 5 — Refurbishment / Recycling

Ausgetauschte Module werden nicht automatisch entsorgt. Wo sinnvoll werden sie diagnostiziert, repariert, gelöscht, neu getestet und als Service-/Refurbished-Part wiederverwendet. Nicht reparierbare Teile werden materialgerecht dem Recycling zugeführt.

## Compute-Modul

CPU, RAM und eMMC werden nicht direkt in das nıu Carrier-PCB integriert, sondern befinden sich auf einem austauschbaren SBC-Modul. Ein Defekt von eMMC/RAM/SoC führt im normalen Service daher zum Austausch des Compute-Moduls, nicht zum Austausch des gesamten Beltpacks.

Bauteil-Rework auf dem SBC bleibt spezialisierten Reparaturpartnern vorbehalten und ist kein regulärer RMA-Pfad.

Die Carrier-/Softwarearchitektur soll einen zukünftigen kompatiblen SBC-Tausch ermöglichen, soweit Schnittstellen und Produktanforderungen dies erlauben.

## Mechanisch belastete Anschlüsse

**OPEN / P0 REVIEW:** Es ist zu prüfen, ob besonders ausfallgefährdete Steckverbinder wie TRRS, PHONES, MIC und die externen USB-C-Ports auf eine oder mehrere kleine austauschbare I/O-Platinen ausgelagert werden sollen.

Vorteil wäre eine kleinere Austauschbaugruppe bei mechanischem Schaden. Dem stehen zusätzliche Leiterplatten, Kabel/Flex-Verbindungen, Steckverbinder, Montageaufwand, Material und potenzielle Fehlerstellen gegenüber.

Die Entscheidung ist anhand realer Mechanik, Platzbedarf, BOM, Montage und erwartbarer Ausfallwahrscheinlichkeit zu treffen; Modularisierung ist kein Selbstzweck.

## Akku

Der Akku ist eine erwartbare Verschleißkomponente und darf die Lebensdauer des Produkts nicht begrenzen.

Anforderungen gemäß ADR-0005 umfassen insbesondere:

- Endnutzer kann den vollständigen Akku austauschen
- kein Löten
- keine Demontage mittels Wärme oder Lösungsmitteln
- handelsübliche Werkzeuge genügen
- verpolungssicherer Stecker
- kein Software-Pairing, das kompatible Ersatzakkus behindert
- Battery-Learning-/Health-State kann nach Austausch korrekt neu initialisiert werden

## Offene Diagnose- und Reparaturdokumentation

Die Reparierbarkeit des Produkts soll nicht nur konstruktiv vorhanden, sondern für Dritte praktisch nutzbar sein. nıu plant deshalb eine ausführliche, öffentlich verfügbare und über die Produktlebensdauer gepflegte Fehleranalyse- und Reparaturdokumentation.

Soweit für das jeweilige Produkt sinnvoll und rechtlich möglich, umfasst sie insbesondere:

- Öffnungs-, Demontage- und Montageanleitungen
- Beschreibung der Baugruppen und ihrer Funktionen
- Schaltpläne und relevante Hardware-/Schnittstelleninformationen
- Steckerbelegungen, Testpunkte und erwartete Messwerte
- Boot-, Recovery- und Reimaging-Verfahren
- offene Diagnosewerkzeuge und Hardware-Selbsttests
- symptomorientierte Fehlersuchbäume
- Austauschverfahren für Service- und Verschleißkomponenten
- Board-Level-Diagnose- und Reparaturhinweise
- Kalibrierungsverfahren nach relevanten Reparaturen
- abschließende Funktions- und Sicherheitstests
- Ersatzteilinformationen und, wo sinnvoll, Spezifikationen kompatibler Drittanbieterkomponenten
- bekannte Fehlerbilder und daraus gewonnene Reparaturhinweise

Die Repair Knowledge Base soll mit den Erfahrungen aus Fertigung, RMA und Feldbetrieb weiterentwickelt werden. Wiederkehrende Fehlerbilder werden mit reproduzierbaren Diagnose- und Reparaturpfaden dokumentiert, statt ausschließlich internes Servicewissen zu bleiben.

## Gemeinsame Diagnosebasis für Factory und Repair

Hardware-Selbsttests und Diagnoseprimitiven sollen soweit sinnvoll gemeinsam für Factory EOL, nıu RMA und unabhängige Reparatur verwendet werden. Die technische Diagnose selbst ist nicht an geheime Factory Credentials zu koppeln.

Beispiele sind die Erreichbarkeit von Audio-Codecs, Audio-Loopback-/Pegeltests, Display- und Tastenprüfung, USB-Enumeration und VBUS-Prüfung, Netzwerkdiagnose sowie die Erreichbarkeit des Secure Elements.

Privilegierte Operationen innerhalb der offiziellen nıu Trust Domain bleiben davon getrennt. Ein öffentliches Diagnosetool darf Hardware prüfen, ohne dadurch nıu Device Certificates, Factory-Registry-Einträge oder andere nıu-Attestierungen erzeugen zu können.

Grundsatz:

> **Diagnostics are open. Trust issuance is not.**

## Reparatur und nıu-Trust-Status

Das Öffnen, Diagnostizieren, Reparieren oder Modifizieren eines Geräts durch seinen Eigentümer oder einen unabhängigen Reparaturbetrieb führt nicht allein zum Verlust des offiziellen nıu-Trust-Status.

Bleiben Carrier Identity und kryptographischer Identity Anchor intakt und zuverlässig beweisbar, bleibt die bestehende Device Identity grundsätzlich erhalten. Dies gilt beispielsweise für den Austausch von Akku, Display, Tasten, Speaker, Mikrofonen, SBC/Storage oder reparierbaren Carrier-Komponenten, sofern der Identity Anchor nicht betroffen ist.

Ist der Identity Anchor nicht mehr zuverlässig beweisbar oder muss er ersetzt werden, darf ein offener Recovery- oder Reparaturprozess nicht selbstständig neue offizielle nıu-Attestierungen erzeugen. Die Wiederherstellung des offiziellen nıu-Trust-Status erfordert dann einen kontrollierten nıu-Rezertifizierungsprozess. Für die erste Produktgeneration ist vorgesehen, dass das physische Gerät hierfür an nıu als Hersteller eingesandt und geprüft wird.

Diese Grenze beschränkt nicht die weitere Nutzung des Eigentümers mit eigener Software oder eigener Trust Domain.

## Kalibrierung und Reparatur

Kalibrierungsdaten dürfen Reparaturen nicht unnötig an die ursprüngliche Fabrik binden. Kalibrierungen werden explizit, versioniert und reproduzierbar gestaltet, sodass eine Service-Teststation relevante Werte nach einem Komponententausch neu bestimmen kann.

Mögliche Kalibrierungsfelder umfassen Mic-Gain-Offsets, Speaker-Level-Offsets und Audio-Calibration-Versionen. Nur tatsächlich erforderliche Werte werden in der Serie verwendet.

## Nachhaltigkeitsziel

Die Modularität des Systems soll nicht maximale Zerlegbarkeit um jeden Preis erzeugen. Ziel ist eine lange reale Nutzungsdauer bei niedriger Replacement Granularity, reproduzierbarer Reparatur und sinnvoller Wiederverwendung von Baugruppen.
