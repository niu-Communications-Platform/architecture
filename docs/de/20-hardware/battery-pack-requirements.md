# Anforderungen an den serienreifen Battery Pack

**Deutsch (kanonisch)** | [English](../../en/20-hardware/battery-pack-requirements.md)

## Zweck

Dieses Dokument beschreibt die Anforderungen an den serienreifen, austauschbaren Battery Pack des nıu Communications Platform Beltpacks und dient zugleich als technische Gesprächsgrundlage für Batteriehersteller.

**DECIDED:** nıu entwickelt weder die Batteriezellen noch den Battery Pack oder dessen internes Batteriemanagement selbst. Eingesetzt werden soll eine serienreife, dokumentierte und für das Produkt geeignete Batterieeinheit eines spezialisierten Herstellers mit integriertem Schutz-/Batteriemanagement.

Der Carrier integriert den Battery Pack in das Gesamtsystem. Welche Lade-, Power-Path-, Mess- und Systemfunktionen außerhalb des Packs erforderlich sind, wird erst nach Auswahl und technischer Abstimmung des Packs festgelegt.

## Produktkontext

Das Beltpack ist ein professionelles, tragbares IP-Intercom- und Audio-Gerät für Live-Produktion, Veranstaltungen und vergleichbare mobile Anwendungen.

Wesentliche Verbraucher sind voraussichtlich:

- ARM-SBC; Serienkandidat Radxa ZERO 3W / RK3566
- internes und gegebenenfalls zusätzliches USB-WLAN bzw. USB-Ethernet
- zwei Audio-Codecs und analoge Audio-Frontends
- interner Lautsprecher und Verstärker
- Farbdisplay
- Bedienelemente und RGB-Statusanzeigen
- Secure Element, Carrier-NVM und weitere Peripherie
- USB-Host-Schnittstelle für USB Audio, Ethernet, HID und weitere unterstützte Geräte

Das Gerät besitzt einen separaten USB-C-Power-Eingang und einen davon getrennten USB-C-Accessory-/Host-Port.

## Mechanische Zielsetzung

Die bisherige Gehäusegröße von ungefähr **120 × 80 × 35 mm ist eine Obergrenze und kein auszufüllender Bauraum**.

**DECIDED:** Das Produkt soll bei Erhalt von Robustheit, Wartbarkeit, thermischer Beherrschbarkeit und guter Bedienbarkeit so kompakt wie sinnvoll werden. Ein kleinerer Battery Pack ist daher ausdrücklich erwünscht, wenn die erforderliche Laufzeit und Leistungsreserve erreicht werden.

Die Batterie darf die möglichen Außenabmessungen des Produkts nicht unnötig bestimmen. Energieinhalt wird gegen Bauraum, Gewicht, elektrische Effizienz und reale Einsatzdauer optimiert; maximale Kapazität ist kein Selbstzweck.

## Wartbarkeit und Austausch

**DECIDED:** Der komplette Battery Pack ist eine vom Endanwender austauschbare Funktionseinheit.

Erforderlich sind insbesondere:

- kein Löten beim Batteriewechsel
- kein Einsatz von Wärme oder Lösungsmitteln
- sicherer mechanischer Zugang
- verpolungssicherer bzw. fehlstecksicherer Anschluss
- keine Software-Paarung, die einen kompatiblen Ersatzakku künstlich verhindert
- nach dem Wechsel vollständige Wiederherstellung des normalen Gerätebetriebs
- definierter Reset bzw. Neuaufbau batteriebezogener Lern-/Health-Daten, sodass ein neuer Akku nicht den Alterungszustand seines Vorgängers erbt
- langfristig verfügbare Ersatzpacks bzw. eine belastbare Ersatzteilstrategie

Das Produkt soll keine proprietäre Batteriearchitektur allein zur Kundenbindung erhalten.

## Technische Anforderungen an den Pack

Der Serienpack soll möglichst folgende Eigenschaften bereitstellen:

- industrietaugliche Lithium-Ionen-Batterieeinheit
- integrierte Schutz- und Batteriemanagementfunktionen
- Temperaturüberwachung
- Schutz gegen relevante Über-/Unterspannungs-, Überstrom- und Kurzschlusszustände
- dokumentierte Lade- und Entladegrenzen
- ausreichende Dauer- und Spitzenstromfähigkeit für das Beltpack einschließlich definierter USB-Host-Last
- dokumentierte Systemkommunikation, bevorzugt über eine etablierte Schnittstelle wie SMBus oder I²C, sofern dies keine unnötige proprietäre Abhängigkeit erzeugt
- geeignete Status-/Fuel-Gauge-Informationen für Batteriestand, Health und Diagnose
- serienfähiger, verriegelbarer und fehlstecksicherer Steckverbinder
- dokumentierte Lebensdauer und Temperaturbereiche
- vollständige für Integration, Transport und Produktkonformität erforderliche Dokumentation
- langfristige Serien- und Ersatzteilverfügbarkeit

Ein Smart-Battery-Protokoll ist kein Selbstzweck. Entscheidend ist, dass die Schnittstelle dokumentiert, robust und langfristig nutzbar ist und den Batteriewechsel nicht künstlich an einen einzelnen kryptographisch gepaarten Pack bindet.

## Betriebsanforderungen

Das Beltpack soll sowohl mobil als auch dauerhaft an externer Stromversorgung betrieben werden können.

Zu klären sind gemeinsam mit dem Batteriehersteller insbesondere:

- zulässiges Verhalten des Packs bei gleichzeitigem Gerätebetrieb und Laden
- erforderliche Systemarchitektur für echtes Power-Path-/Load-Sharing
- geeignete Ladecharakteristik und maximale Ladeströme
- Verhalten bei längerer externer Stromversorgung
- Möglichkeiten für Battery Care bzw. reduzierte Ladegrenzen zur Lebensdaueroptimierung
- Vermeidung unnötiger Mikrozyklen im stationären Betrieb
- Temperaturgrenzen für Laden und Entladen
- sichere Übergänge zwischen externer Versorgung und Batteriebetrieb
- sinnvolle Interpretation von State of Charge, State of Health und Zykleninformationen nach einem Packwechsel

Das interne BMS des Packs und die Power-Architektur des Beltpacks sollen klare Verantwortungsgrenzen besitzen. Schutzfunktionen des Packs werden nicht unnötig neu entwickelt; erforderliche System-Power-Funktionen auf dem Carrier bleiben davon getrennt.

## Laufzeit und Leistungsbudget

Die endgültige Mindestenergie in Wh ist noch nicht festgelegt.

**REVIEW:** Ziel ist eine für professionelle Einsätze sinnvolle Schichtlaufzeit bei möglichst kleinem Gerät. Die Auswahl soll auf einem realistischen Leistungsbudget und anschließend auf Messungen am Radxa-/Carrier-Prototyp beruhen, nicht auf maximal möglicher Akkukapazität.

Für die Vorauswahl sind insbesondere zwei Klassen interessant:

- etwa **19 Wh** als besonders kompakte Klasse
- etwa **25 Wh** als kompakte Klasse mit zusätzlicher Laufzeitreserve

Größere Packs bleiben möglich, müssen ihren zusätzlichen Bauraum und ihr Gewicht jedoch durch einen realen Produktnutzen rechtfertigen.

## Referenzkandidat: vri BASE LINE

**CANDIDATE:** Die vri BASE LINE der VRI GmbH Batterie-Technik in Ellwangen wird als bevorzugter Referenzkandidat untersucht.

Nach öffentlich verfügbaren Herstellerangaben sind derzeit insbesondere interessant:

### 1S/21700 — Produkt 88054 201 512

- 3,60 V
- 5,30 Ah / ca. 19,1 Wh
- 79 × 22,50 mm
- SMBus
- Molex Micro-Fit, 5-polig
- maximaler Ladestrom 5,15 A
- maximaler Entladestrom 7,00 A
- NTC
- Second Protection
- 800 Zyklen bei DOD 80 % laut Hersteller
- Hersteller nennt UN38.3, IEC62133:2017 und UL62133

### 2S/18650 — Produkt 88030 502 512

- 7,20 V
- 3,50 Ah / ca. 25,2 Wh
- 73 × 37,30 × 18,80 mm
- I²C
- Molex Micro-Fit, 5-polig
- maximaler Ladestrom 3,38 A
- maximaler Entladestrom 5,00 A
- NTC
- Second Protection
- 800 Zyklen bei DOD 80 % laut Hersteller
- Hersteller nennt UN38.3, IEC62133:2017 und UL62133

Die endgültige Wahl zwischen 1S und 2S erfolgt ausdrücklich nicht allein nach Kapazität. Zu bewerten sind Gesamtwirkungsgrad der Systemversorgung, notwendige Power-Conversion, reale Lastprofile, Laufzeit, USB-Host-Leistungsreserve, Thermik, Gewicht, Bauraum und Wartbarkeit.

## Fragen für das Hersteller-Gespräch

Für ein erstes technisches Gespräch mit VRI bzw. einem alternativen Pack-Hersteller sollen insbesondere folgende Punkte geklärt werden:

1. Welcher bestehende Standardpack ist für ein dauerhaft produziertes mobiles Kommunikationsgerät mit unserem Lastprofil am sinnvollsten?
2. Ist für die Anwendung 1S/21700 oder 2S/18650 systemisch vorzuziehen und warum?
3. Welche realen Dauer- und Spitzenlastprofile empfiehlt bzw. erlaubt der Hersteller?
4. Welche Aufgaben übernimmt das Pack-BMS vollständig und welche Lade-/Power-Path-Funktionen müssen auf dem Carrier verbleiben?
5. Wie soll gleichzeitiger Betrieb und Laden elektrisch realisiert werden?
6. Welche Strategie empfiehlt VRI für häufigen bzw. dauerhaften Netzbetrieb und maximale Batterielebensdauer?
7. Lassen sich reduzierte Ladegrenzen/Battery-Care sinnvoll realisieren und über welche Schnittstelle?
8. Welche Fuel-Gauge-/Health-/Cycle-Daten sind über SMBus bzw. I²C verfügbar und wie sind sie dokumentiert?
9. Wie verhält sich der Pack nach physischem Austausch gegenüber dem Host; sind Pairing, Initialisierung oder spezielle Lernvorgänge erforderlich?
10. Ist der bestehende Pack mechanisch für regelmäßigen Endanwenderwechsel geeignet, insbesondere hinsichtlich Stecker, Kabel, Zugentlastung und Steckzyklen?
11. Welche Anforderungen stellt der Hersteller an mechanische Befestigung, Stoß-/Vibrationsschutz, Belüftung und thermische Umgebung?
12. Welche vollständigen Prüf-, Transport- und Konformitätsunterlagen werden für die Integration in unser Endprodukt bereitgestellt?
13. Welche Serienverfügbarkeit, Product-Lifecycle-Zusagen, MOQ und Preisstaffeln sind möglich?
14. Wie wird eine Ersatzteilversorgung über die regulatorisch und kommerziell erforderliche Lebensdauer sichergestellt?
15. Können Muster der 1S/21700- und 2S/18650-Varianten für mechanische und elektrische Prototypentests bereitgestellt werden?
16. Falls ein Standardpack nahezu, aber nicht vollständig passt: Welche Anpassungen sind möglich, ohne die Vorteile einer bereits entwickelten und zertifizierten BASE-LINE-Lösung unnötig aufzugeben?

## Entscheidungsregel

Der bevorzugte Battery Pack ist nicht der Pack mit der höchsten Kapazität, sondern der kleinste serienreife Pack, der mit ausreichender Reserve die realen elektrischen, thermischen, Laufzeit-, Wartbarkeits- und Lebensdaueranforderungen des Beltpacks erfüllt.

> **Battery capacity is a requirement, not a design goal. Product size, serviceability and reliable runtime are optimized together.**

## Quellen / Herstellerinformationen

Die konkreten Daten der vri BASE LINE sind vor einer Serienentscheidung anhand der jeweils aktuellen Herstellerdatenblätter und der direkten technischen Abstimmung mit VRI zu verifizieren. Öffentlich zugängliche Produktseite: https://www.vri-gmbh.de/produkte-loesungen/vri-baseline
