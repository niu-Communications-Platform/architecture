# Target-Cost-Modell und Made-in-Germany-Prämisse

**Deutsch (kanonisch)** | [English](../../en/80-manufacturing/target-cost-model.md)

## Zweck

Dieses Dokument definiert den wirtschaftlichen Zielkostenrahmen für das nıu Communications Platform Beltpack. Es ist ein Target-Cost-Modell und noch keine Lieferantenkalkulation.

## Fertigungsprämisse

**DECIDED:** `Made in Germany` wird für die Serienfertigung als hart zu verfolgende Prämisse behandelt. Ziel ist insbesondere, Carrier-PCBA, Gehäusefertigung und Endmontage/EOL soweit wirtschaftlich vertretbar in Deutschland durchführen zu lassen.

Das bedeutet nicht, dass jedes Einzelbauteil deutschen Ursprungs sein muss. SBC, Halbleiter, Display, Battery Pack und weitere Komponenten können international beschafft werden. Entscheidend ist eine belastbare deutsche Fertigungs- und Wertschöpfungsarchitektur für das Endprodukt.

Eine Verlagerung wesentlicher Fertigungsschritte ins Ausland soll nicht reflexartig aus Kostengründen erfolgen. Erst wenn belastbare deutsche Angebote zeigen, dass Zielpreis, Qualität und Marge nicht gleichzeitig erreichbar sind, wird die Prämisse neu bewertet.

## Vertrieb und Preis

**CANDIDATE:** Der bisherige Zielverkaufspreis beträgt **189 EUR netto** bzw. bei 19 % deutscher Umsatzsteuer **224,91 EUR brutto**.

**DECIDED:** Direct-to-Customer / Direktvertrieb ist der wirtschaftliche Basisfall. Stationärer Handel oder klassische Distribution werden nicht vorausgesetzt. Ein späterer indirekter Kanal erhält ein eigenes Margenmodell und darf nicht stillschweigend aus derselben 189-EUR-DTC-Kalkulation finanziert werden.

## Margendefinition und Kosten-Gates

Ziel ist mindestens ungefähr **50 % Gross Margin** auf den Nettoverkaufspreis im Direktvertrieb. Die Architektur wird jedoch nicht auf diese absolute Grenze optimiert, sondern auf einen deutlich gesünderen COGS-Korridor.

| Gate | COGS | Gross Margin bei 189 EUR netto | Bedeutung |
|---|---:|---:|---|
| **TARGET** | **≤ 75 EUR** | **≥ 60,3 %** | sehr gesund; bevorzugtes Entwicklungsziel |
| **ACCEPTABLE** | **>75 bis 80 EUR** | **57,7–60,3 %** | regulärer Zielbereich |
| **LIMIT** | **>80 bis 94,50 EUR** | **50,0–57,7 %** | wirtschaftlich möglich, aber aktive Kostenoptimierung erforderlich |
| **FAIL** | **>94,50 EUR** | **<50 %** | 189-EUR-DTC-Zielpreis nicht tragfähig |

**DECIDED:** **94,50 EUR ist die wirtschaftliche Obergrenze, nicht das Einkaufsbudget. 75–80 EUR ist der Entwicklungsbereich; ≤75 EUR ist das bevorzugte Ziel.**

## Baugruppen-Cost-Budgets

Die Gesamtzielkosten werden auf Baugruppen heruntergebrochen. Diese Budgets sind Architektur-Gates: Neue Bauteile, zusätzliche Platinen, Kabel, Steckverbinder oder manuelle Montageschritte werden nicht isoliert als „nur wenige Euro“ bewertet, sondern gegen das Budget ihrer Baugruppe und gegen die Gesamt-COGS.

| Baugruppe / Kostenblock | Zielbudget EUR/Gerät | Inhalt / Regel |
|---|---:|---|
| **Compute** | **18–22** | Radxa ZERO 3W inkl. geeigneter RAM/eMMC-Konfiguration; >22 EUR löst Review aus |
| **Carrier Core + Audio** | **13–17** | 2× Codec, Speaker-Amp, Secure Element, GPIO/PWM/NVM, Clocking, wesentliche Passives |
| **Power + USB** | **8–11** | Charger/Power-Path/DC-DC/Monitoring, USB Hub/Host-Control, VBUS-Schutz, ESD |
| **Human Interface + interne Audio-Mechanik** | **7–10** | Display, LEDs, Controls, interne Mics/Speaker, relevante Kleinteile |
| **externe Connectoren / I/O-Mechanik** | **3–5** | Audio-, USB-, Power-Buchsen und ggf. wirtschaftlich begründete I/O-Mechanik |
| **Carrier PCB + deutsche Bestückung/AOI** | **6–9** | nackte PCB plus SMT/THT-Fertigung; DFM muss Handarbeit minimieren |
| **Standard-Battery-Pack** | **12–16** | Ziel für ~19-Wh-Klasse; Hersteller-RFQ entscheidet; >18 EUR löst Architektur-/Preisreview aus |
| **Gehäuse + Clip + Akkuwechselmechanik** | **5–8** | deutsches Serienspritzguss-Ziel; Werkzeug-NRE separat |
| **deutsche Endmontage + EOL + Provisioning + Packen** | **5–7** | DFMA und Testautomatisierung sind Voraussetzung |
| **Produktverpackung** | **2–3** | hochwertige kompakte DTC-Verpackung inkl. Inlay/Drucksachen |

Die Budgets sind **keine unabhängig addierbaren Worst-Case-Spannen**. Mit zunehmendem Designstand werden sie durch reale MPN-, EMS- und Lieferantenpreise ersetzt. Überschreitungen einer Baugruppe müssen sichtbar durch Einsparungen an anderer Stelle kompensiert werden; sie dürfen nicht stillschweigend das Gesamtziel erhöhen.

## Cost-Review-Regel für Architekturentscheidungen

**DECIDED:** Kostenkontrolle ist Teil der Architektur.

Für jede neue Hardwarefunktion bzw. relevante Hardwareänderung werden mindestens folgende Fragen gestellt:

1. Welche zusätzlichen Materialkosten entstehen bei 1k/5k/10k?
2. Entstehen zusätzliche PCB-Fläche, Layer, Steckverbinder, Kabel oder mechanische Teile?
3. Entsteht zusätzliche manuelle Montagezeit in Deutschland?
4. Entsteht zusätzlicher EOL-/Kalibrier-/Serviceaufwand?
5. Erzeugt die Änderung eine neue Produkt- oder Fertigungsvariante?
6. Welches Baugruppenbudget wird belastet?
7. Welcher messbare Produktnutzen rechtfertigt diese Kosten und Komplexität?

**Capability ≠ Feature** gilt damit auch wirtschaftlich: Eine technisch mögliche Erweiterung wird nicht automatisch bestückt oder als Produktfunktion umgesetzt.

## Vorläufige Komponentenanker

Aktuelle Engineering-Anker, bis echte RFQs vorliegen:

- Radxa ZERO 3W: Ziel 18–22 EUR in Serienkonfiguration;
- 2× TLV320AIC3204: grob 5–7 EUR zusammen;
- Secure Element: grob 0,6–1,0 EUR;
- Speaker-Amp: grob 0,7–1,2 EUR;
- Standardakku: Ziel 12–16 EUR, derzeit größte Lieferantenunsicherheit;
- Verpackung: Ziel 2–3 EUR.

Die exakte Carrier-BOM wird erst mit Schaltplan und MPN-Liste belastbar. Bis dahin ist falsche Cent-Genauigkeit zu vermeiden.

## Reserve und vollständige Serienökonomie

Die Differenz zwischen Entwicklungsziel und 94,50-EUR-Grenze ist keine freie Feature-Kasse. Sie dient insbesondere als Reserve für:

- Ausschuss und Rework;
- Incoming-/EOL-Test;
- Garantierückstellungen und erwartete RMA-Kosten;
- Inbound-Fracht und ggf. Zoll;
- Verpackungs-/Fertigungsausschuss;
- reale Lieferantenpreisabweichungen und Second-Source-Effekte.

Fulfillment, DTC-Payment-Gebühren, Versandzuschüsse und vergleichbare Vertriebskosten müssen zusätzlich im Unit-Economics-Modell sichtbar bleiben, auch wenn sie bilanziell nicht in jeder Definition als Herstell-COGS geführt werden.

Werkzeuge, Zertifizierung und Entwicklung/NRE werden separat transparent geführt. Vor Serienfreigabe wird zusätzlich eine amortisierte Vollkostenansicht erstellt.

## Gehäuse

Ein kundenspezifisches Spritzgussgehäuse aus deutscher Fertigung ist wirtschaftlich grundsätzlich plausibel. Werkzeugkosten werden separat als NRE geführt. Prototype/Pilot dürfen additive Verfahren nutzen; Spritzguss wird erst nach ausreichender mechanischer Validierung freigegeben.

**DECIDED:** Das Hauptgehäuse wird nicht für einen hypothetischen größten Extended Battery Pack unnötig vergrößert. Eine spätere größere Akkukapazität muss sich soweit möglich über dieselbe Beltpack-Hardware und eine nach außen größere Pack-Geometrie integrieren.

## Verpackung

Die Verpackung ist ein echter Stückkostenposten.

**TARGET:** **2–3 EUR** für eine hochwertige, kompakte, weitgehend papier-/kartonbasierte Produktverpackung inklusive Inlay und notwendigen Drucksachen.

Da DTC Basisfall ist, wird separat kalkuliert, ob die Produktverpackung selbst versandfähig ist oder ein Versandkarton erforderlich wird.

## DFMA-Regel für Made in Germany

> **Made in Germany wird wirtschaftlich durch Design for Manufacturing and Assembly ermöglicht, nicht durch späteren Preisdruck auf den Fertiger.**

Daher gelten als Architekturziele:

- möglichst wenige PCBs und Kabelverbindungen;
- SMT statt manueller THT-/Kabelarbeit, soweit technisch sinnvoll;
- keine unnötigen Handlötprozesse;
- eindeutige, fehlstecksichere Montage;
- geringe Schrauben-/Befestigerzahl;
- Gehäusefunktionen integrieren, wenn dadurch Montage entfällt;
- automatisierter Factory-/EOL-Test;
- automatisiertes Flashing/Provisioning;
- Testpunkte und Factory Mode von Anfang an;
- Variantenarmut;
- Standardakku und möglicher Extended Pack dürfen keine zweite Beltpack-Fertigungslinie erzeugen.

## Kostenentwicklung über den Projektverlauf

Das Modell wird schrittweise von Target Costing zu Ist-Kosten überführt:

- **Architekturphase:** Baugruppenbudgets und Engineering Allowances;
- **Schaltplan/BOM:** reale MPNs und Distributor-/Herstellerstaffeln;
- **Prototype/Pilot:** reale Montagezeit, Ausschuss, Testzeit und Rework messen;
- **RFQ:** deutsche Angebote für PCB/PCBA, Gehäuse, Box Build und Verpackung;
- **Pre-Series:** landed COGS einschließlich realistischer Reserve;
- **Series Release:** DTC Unit Economics einschließlich Payment, Fulfillment, Warranty und NRE-Amortisationssicht.

## Nächste Kostengates

1. Serienkonfiguration des Radxa (RAM/eMMC) festlegen und Hersteller-/Distributor-RFQ einholen.
2. VRI: Preisstaffeln für Standardpack und mögliche Extended-Familie bei 1k/5k/10k anfragen.
3. Carrier-BOM nach Schaltplanstand auf reale MPNs herunterbrechen und gegen die Baugruppenbudgets prüfen.
4. Deutsche EMS-RFQ für 500/1k/5k/10k inklusive Material, AOI, Test und Box Build.
5. Deutsches Gehäuse-RFQ inklusive Werkzeug, Stückpreis 1k/5k/10k und Montageoptimierung.
6. Verpackungs-RFQ 1k/5k/10k inklusive Inlay und Versandkonzept.
7. Target-Cost-Modell nach jedem RFQ aktualisieren.
8. Vor Serienfreigabe vollständiges DTC Unit-Economics-Modell erstellen.

## Gate

Bei 189 EUR netto gilt:

> **TARGET ≤75 EUR. ACCEPTABLE ≤80 EUR. LIMIT 94,50 EUR. Oberhalb davon ist 189 EUR netto bei 50 % Gross Margin nicht tragfähig.**

Die Made-in-Germany-Prämisse gilt als wirtschaftlich tragfähig, solange belastbare Serienangebote zeigen, dass das Produkt mit ausreichender Qualitäts-, Garantie- und Beschaffungsreserve innerhalb dieses Korridors hergestellt werden kann.
