# Reparierbarkeit und Ressourcenschonung

**Deutsch (kanonisch)** | [English](../../en/20-hardware/repairability-sustainability.md)

## Ziel

Die Hardwarearchitektur soll die Lebensdauer des Beltpacks maximieren und verhindern, dass der Defekt einer einzelnen Komponente unnötig zum Austausch des gesamten Produkts führt.

## Architekturprinzipien

**DECIDED:** Der Ausfall einer einzelnen nicht-strukturellen Komponente soll grundsätzlich nicht den Austausch des gesamten Beltpacks erzwingen.

**DECIDED:** Repariert oder ersetzt wird die kleinste technisch, ökologisch und wirtschaftlich sinnvolle Funktionseinheit.

**DECIDED:** Reparaturen sollen Device Identity und Provisionierung erhalten, soweit dies technisch möglich und sicher ist.

**DECIDED:** Bauteilreparatur wird bevorzugt, wenn sie sinnvoll ist. Modultausch wird bevorzugt, wenn Bauteilreparatur unverhältnismäßigen Arbeits-, Energie-, Geräte- oder Schadensaufwand verursacht.

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

## Kalibrierung und Reparatur

Kalibrierungsdaten dürfen Reparaturen nicht unnötig an die ursprüngliche Fabrik binden. Kalibrierungen werden explizit, versioniert und reproduzierbar gestaltet, sodass eine Service-Teststation relevante Werte nach einem Komponententausch neu bestimmen kann.

Mögliche Kalibrierungsfelder umfassen Mic-Gain-Offsets, Speaker-Level-Offsets und Audio-Calibration-Versionen. Nur tatsächlich erforderliche Werte werden in der Serie verwendet.

## Nachhaltigkeitsziel

Die Modularität des Systems soll nicht maximale Zerlegbarkeit um jeden Preis erzeugen. Ziel ist eine lange reale Nutzungsdauer bei niedriger Replacement Granularity, reproduzierbarer Reparatur und sinnvoller Wiederverwendung von Baugruppen.
