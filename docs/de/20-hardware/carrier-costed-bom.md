# Vorläufige kostenbewertete Carrier-BOM

**Deutsch (kanonisch)** | [English](../../en/20-hardware/carrier-costed-bom.md)

## Zweck

Dieses Dokument prüft erstmals quantitativ, ob die geplante Carrier-Architektur des Beltpacks innerhalb des Target-Cost-Modells plausibel ist. Es ist **noch keine freigegebene Serien-BOM**. Konkrete MPNs sind teils Kandidaten; offene Funktionen werden als Engineering Allowance geführt.

## Ergebnis in einem Satz

**Die geplante Carrier-Architektur erscheint kostenmäßig grundsätzlich tragfähig.** Die bisher konkret recherchierbaren Kern-ICs sind nicht der Kostentreiber. Das größte Kostenrisiko liegt derzeit in Power/USB, Mechanik/Connectoren, PCB/Bestückung und noch offenen Detailbauteilen — nicht in den zwei Audio-Codecs oder dem Secure Element.

## Abgrenzung

Enthalten sind Carrier-Elektronik, Carrier-PCB und deutsche Bestückung/AOI. Nicht enthalten sind Radxa Compute Module, Battery Pack, Hauptgehäuse, Produktverpackung und deutsche Box-Build-Endmontage.

## Kernbauteile mit aktuellem Preisanker

| Funktion | Kandidat | Menge | aktueller öffentlicher Preisanker | Planwert/Gerät |
|---|---|---:|---:|---:|
| Audio Codec | TLV320AIC3204IRHBR | 2 | ca. 2,57 EUR/Stk. bei 1k; Full-Reel teils niedriger | **5,2 EUR** |
| Speaker Amp | TAS2505IRGER | 1 | ca. 0,87 USD/Stk. bei 1k bei DigiKey | **0,8 EUR** |
| Secure Element | ATECC608C-TFLXTLS | 1 | Serienvariante RFQ; generische ATECC608B-Familie öffentlich ca. 0,65–0,85 EUR | **1,0 EUR Allowance** |
| Carrier EEPROM | 24CS64-Klasse | 1 | öffentlich etwa 0,3 EUR in Kleinmenge | **0,3 EUR** |
| GPIO Expander | MCP23017-Klasse | 1 | öffentlich etwa 1,45 EUR in Einzelmenge; Serienpreis offen | **1,0 EUR Allowance** |
| RGB LED Driver | PCA9955BTWJ oder funktional äquivalent | 1 | ca. 1,08 EUR bei 1k | **1,1 EUR** |

Zwischensumme dieser sichtbaren Core-ICs: **ca. 9,4 EUR**.

Wichtig: Der TrustFLEX-Serienpreis muss per RFQ ermittelt werden. Die generischen ATECC608-Preise dienen nur als Plausibilitätsanker und dürfen nicht als Angebot für den provisionierten TrustFLEX-Typ interpretiert werden.

## USB-Architektur: Kostenwarnung und Lebenszyklusregel

Ein USB-2.0-Hub-Controller der USB2514B-Klasse liegt öffentlich ungefähr im Bereich weniger Euro, der konkrete USB2514BI ist jedoch als **NRND (Not Recommended for New Designs)** gelistet und wird deshalb **nicht** als Serienentscheidung übernommen.

**REVIEW:** Für Prototype 1 und Serie ist ein aktiver, langfristig geeigneter USB-2.0-Hub-Controller auszuwählen. Preisziel für Hub-Controller einschließlich notwendiger Clock-/Konfigurationsbauteile: **≤ 2,5 EUR** bei Serienmenge.

## Funktionsblöcke und Engineering Allowances

| Carrier-Block | Ziel/Planwert EUR | Inhalt |
|---|---:|---|
| 2× Audio Codec | 5,2 | AIC3204-Klasse |
| Speaker Amp | 0,8 | TAS2505-Klasse |
| Secure Element | 1,0 | TrustFLEX-Klasse, RFQ offen |
| NVM + GPIO + RGB PWM | 2,4 | EEPROM, Expander, LED Driver |
| Audio Analog Front End | 2,0–3,0 | Bias, Filter, Schutz, Umschaltung/Detect, CTIA/OMTP-Funktion soweit erforderlich |
| USB Hub + Clock/Config | 2,0–2,8 | finaler aktiver Hub-Typ offen |
| USB-C Accessory Port Control | 1,5–2,5 | DFP/CC, VBUS current limit, reverse protection, OCP, ESD |
| USB-C Power Input + Schutz | 0,8–1,5 | Connector-nahe Schutz-/Detect-Funktionen; Charger separat |
| Power Path / Charger / DC-DC | 4,0–6,0 | stark abhängig von finalem 1S/2S Battery Pack und externer Versorgung |
| Fuel/Power/Temperature Monitoring | 0,5–1,0 | soweit nicht vollständig vom Pack bereitgestellt |
| Oscillators/Clocking | 0,3–0,7 | soweit benötigt |
| ESD/EMI/Protection gesamt | 1,0–1,8 | externe Audio-, USB-, Power- und sonstige Ports |
| Passives/Regulators/Level Shifting/Glue | 2,0–3,0 | aggregierte Allowance |
| Testpunkte/Factory Interface/kleine Steckverbinder | 0,5–1,0 | DFT-relevante Hardware |

### Elektronik-Zwischenergebnis

Aus den derzeitigen Preisankern und Allowances ergibt sich für die **Carrier-Elektronik ohne Display, mechanische Bedienelemente, Audio-Wandler, externe Buchsen und PCB-Fertigung** ein Engineering-Korridor von grob:

> **ca. 24–30 EUR**

Der obere Bereich ist bewusst konservativ, solange Power-Topologie, USB-Hub und Audio-Umschaltung nicht als Schaltplan vorliegen.

## Human Interface und mechanisch belastete I/O-Komponenten

Diese Komponenten sitzen funktional am Carrier bzw. werden mit ihm verbunden, sind im Target-Cost-Modell aber separat sichtbar:

| Block | Planwert EUR |
|---|---:|
| 1,3–1,5 Zoll TFT | 2,0–3,5 |
| 4 RGB LEDs + Lichtführung-Anteil | 0,3–0,8 |
| PTT + Bedienbuttons + Encoder | 1,0–2,0 |
| interne Mikrofone | 0,5–1,2 |
| interner Speaker | 0,8–1,5 |
| MIC / PHONES / TRRS Audio-Buchsen | 1,0–2,0 |
| 2× USB-C Buchsen | 0,4–1,0 |
| sonstige interne Steckverbinder | 0,5–1,0 |

Diese Gruppe liegt damit grob bei **6,5–13 EUR**. Sie muss durch konkrete mechanische Auswahl deutlich enger werden.

## PCB und deutsche Bestückung

Aktuelles Cost Gate:

- nackte Carrier-PCB: **1,5–3 EUR**;
- deutsche SMT/THT-Bestückung + AOI: **4–7 EUR**;
- zusammen: **6–9 EUR Zielbereich**.

Die tatsächliche Fertigung darf erst nach PCB-Stackup, Abmessungen, Bestückungsseiten, Bauteilanzahl und THT-Anteil seriös kalkuliert werden.

**DFMA:** Jeder manuell zu lötende Draht, jede zusätzliche THT-Buchse und jede zweite Bestückungsseite ist nicht nur BOM-, sondern deutsche Fertigungszeit. Deshalb wird die BOM nicht isoliert vom Montageprozess optimiert.

## Konsolidierte Carrier-Sicht

Für die wirtschaftliche Bewertung sind drei Ebenen zu unterscheiden:

1. **Core Carrier Electronics:** derzeit ca. **24–30 EUR** Engineering Estimate.
2. **HMI / Audio Mechanics / External Connectors:** derzeit ca. **6,5–13 EUR**, noch hohe mechanische Unsicherheit.
3. **Carrier PCB + German PCBA:** **6–9 EUR** Target.

Die einfache Summe ergibt aktuell grob **36,5–52 EUR** für die breite, noch unfertige Carrier-nahe Hardware. Das überschreitet am oberen Ende das bisherige aggregierte Ziel und zeigt, wo die Architektur jetzt konkretisiert werden muss.

Das ist **kein Alarm**, weil die obere Grenze mehrere konservative Allowances und noch nicht optimierte Überlappungen enthält. Es ist aber der erste quantitative Hinweis, dass wir nicht beliebig weitere Hardware ergänzen dürfen.

## Ziel für Schaltplanphase

Bis zum Carrier-Schematic-Freeze soll gelten:

- **Carrier Electronics inkl. Power/USB/Audio/Security:** Ziel **≤ 27 EUR**;
- **HMI + Audio Mechanics + External Connectors:** Ziel **≤ 10 EUR**;
- **PCB + deutsche PCBA/AOI:** Ziel **≤ 8 EUR**;
- **Carrier-nahe Hardware gesamt:** Ziel **≤ 45 EUR**, bevorzugt **≤ 42 EUR**.

Dies ist mit dem Gesamt-COGS-Ziel von 75–80 EUR vereinbar, wenn Compute, Battery, Enclosure, Endmontage und Verpackung ihre jeweiligen Budgets halten.

## Wichtigste Kostenrisiken

### 1. Power-Architektur

Größter offener Elektronikblock. Die Wahl 1S vs. 2S und die Anforderungen an gleichzeitiges Laden/Betrieb, 5-V-Systemrail und 5-V/1-A-USB-Host beeinflussen Wandlerzahl, Leistungsklasse, Thermik und BOM erheblich.

**Regel:** Keine Power-Topologie finalisieren, bevor VRI-Pack und reale Lastmessungen ausreichend bekannt sind.

### 2. USB

Der externe Universal-Host ist ein wichtiges Produktmerkmal, darf aber nicht zu einer Sammlung redundanter Controller werden. Hub, Type-C-Role/CC, VBUS-Switch und Schutz werden als zusammenhängender Block optimiert.

### 3. Audio-Umschaltung / CTIA-OMTP

Die gewünschte Anschlussflexibilität kann mehr Analogschalter, Detect-Schaltung und Schutz benötigen als die Codecs selbst kosten. Erst der konkrete Schaltplan zeigt, ob die derzeitige Allowance reicht.

### 4. Mechanische Buchsen und Montage

Die nominellen Bauteilpreise sind klein, aber robuste Buchsen, Befestigung, Kabel und Handarbeit können die reale Serienkostenwirkung vervielfachen. Die Entscheidung über eine I/O-Daughterboard-Architektur muss deshalb Kosten, Reparierbarkeit und Montage gemeinsam betrachten.

### 5. Varianten

Nicht bestückte Reserven sind billig, separate Produktvarianten teuer. Future-proofing bevorzugt Pads, Testpunkte, Busreserven und Softwarefähigkeit statt zusätzliche serienmäßig bestückte Hardware ohne V1-Nutzen.

## Was überraschend günstig ist

Die zwei Audio-Codecs sind zusammen im Volumen nur ungefähr ein 5-EUR-Block. Secure Element, EEPROM, GPIO Expander und RGB-LED-Treiber sind ebenfalls keine wirtschaftlichen Showstopper.

Daraus folgt:

> **Wir sollten keine gute Audio-, Identity- oder Diagnosearchitektur für Centbeträge kaputtsparen. Optimiert werden zuerst die großen und arbeitsintensiven Blöcke.**

## Nächste Schritte

1. VRI-Gespräch/RFQ zur Festlegung der realistischen Pack-Spannungsklasse.
2. Power-Tree für 1S- und 2S-Kandidat auf Blockebene vergleichen und BOM-Differenz berechnen.
3. aktiven USB-Hub-Kandidaten auswählen; keine NRND-Komponente für neue Serienarchitektur.
4. USB-C Host-Power-/CC-Architektur konkretisieren.
5. Audio-Jack-/CTIA-/OMTP-Schaltung konkretisieren.
6. Display, Buttons/Encoder, Mics, Speaker und Buchsen auf reale MPNs herunterbrechen.
7. erste KiCad-BOM gegen **≤42–45 EUR Carrier-nahe Hardware** prüfen.
8. anschließend deutsche EMS-RFQ vorbereiten.

## Gate

> **Die Architektur ist aktuell kostenmäßig plausibel, aber der Carrier hat keine unbegrenzte Reserve. Ab jetzt muss jede zusätzliche Hardwarefunktion ihr Budget rechtfertigen.**
