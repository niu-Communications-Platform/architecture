# Battery-Systemtopologie: 1S vs. 2S

**Deutsch (kanonisch)** | [English](../../en/20-hardware/battery-topology-1s-vs-2s.md)

## Zweck

Dieses Dokument vergleicht 1S- und 2S-Li-Ion-Battery-Packs als Systemarchitektur für das Beltpack. Es ist noch keine Auswahlentscheidung. Der Vergleich umfasst Pack, Laden, Systemversorgung, USB-Host, Wirkungsgrad, Strom, Bauraum, Kosten und Produktvarianten.

## Bekannte Systemanforderungen

Vorläufiges Power Budget:

- Listening / normal intercom: ~3,2 W
- Typical mixed use: ~3,8 W
- Heavy internal use: ~5,5 W
- Design peak ohne externes USB-Accessory: ~8 W
- Design peak mit bis zu ~5 W USB-Accessory: ~13 W
- Radxa/System benötigt eine robuste 5-V-Versorgung.
- ACCESSORY USB-C soll als Host bis ungefähr 5 V / 1 A nutzbar sein.
- POWER USB-C ist getrennt und dient externer Versorgung/Laden.
- Stationärer Betrieb mit Power Path/Load Sharing ist Produktanforderung.
- Akku ist rapid field-replaceable; Hot-Swap wird nicht verlangt.

## Referenzpacks

### 1S/21700 VRI 88054 201 512

- 3,60 V nominal
- 5,30 Ah
- ~19,1 Wh
- 79 × 22,5 mm
- max. Entladestrom 7 A
- max. Ladestrom 5,15 A
- SMBus

### 2S/18650 VRI 88030 502 512

- 7,20 V nominal
- 3,50 Ah
- ~25,2 Wh
- 73 × 37,3 × 18,8 mm
- max. Entladestrom 5 A
- max. Ladestrom 3,38 A
- I²C

Beide sind Referenzkandidaten, nicht ausgewählt.

## 1S-Architektur

Ein 1S-Pack arbeitet grob zwischen leerer und voller Einzelzellenspannung. Für das Beltpack bedeutet dies, dass die zentrale 5-V-Systemschiene aus dem Akku **hochgesetzt** werden muss.

Ein moderner 1S-Charger/Power-Path-Baustein kann Laden, BATFET, System-Power-Path und teilweise einen leistungsfähigen Boost-/OTG-Pfad hoch integrieren. TI BQ25638 ist ein aktuelles Beispiel: 1S, bis 5 A Ladestrom, NVDC Power Path, I²C/ADC und Boost-Ausgang bis 9,6 V mit programmierbarer Strombegrenzung bis 3,2 A. Das ist kein final ausgewähltes Bauteil, zeigt aber, dass die erforderliche Funktionsklasse hoch integriert verfügbar ist.

### Vorteile

- aktuell kleinster und mechanisch attraktivster VRI-Referenzpack;
- ~19 Wh passen zum Konzept „kleines Standardgerät + schneller Ersatzakku“;
- nur eine Zelle in Serie: keine Zellbalance zwischen seriellen Zellen erforderlich;
- sehr gut verfügbare hochintegrierte portable 1S-Power-Path-/Charger-ICs;
- ein geeigneter Boost-Pfad kann 5 V für Compute und USB-Host aus derselben Grundtopologie bereitstellen;
- niedrige Packspannung vereinfacht grundsätzlich manche Safety-/Packaspekte.

### Nachteile / kritische Punkte

- hohe Packströme: 13 W entsprechen idealisiert bereits ~3,6 A bei 3,6 V; bei niedriger Zellspannung und Wandlungsverlusten deutlich mehr;
- 5-V-Rail ist im Akkubetrieb vollständig von einem leistungsfähigen Boost-Wandler abhängig;
- Boost-Induktor, Schaltströme, Layout, EMI und thermische Verluste werden kritisch;
- gleichzeitiger Compute-Peak + USB-Accessory muss bei niedriger State of Charge validiert werden;
- Wirkungsgrad des 1S→5V-Pfads beeinflusst Laufzeit unmittelbar.

## 2S-Architektur

Ein 2S-Pack liegt nominal bei 7,2 V. Die zentrale 5-V-Systemschiene wird im Akkubetrieb daher **heruntergesetzt**.

Für 2S existieren ebenfalls integrierte Charger/Power-Path-Lösungen. TI BQ25883 ist ein Beispiel für einen 2S-Boost-Charger mit Power Path und I²C; TI nennt 93,4 % Ladeeffizienz bei 5-V-Eingang, 7,6-V-Batterie und 1 A. Für die 5-V-Systemschiene ist bei 2S typischerweise zusätzlich ein leistungsfähiger Buck-Pfad erforderlich. Das konkrete Design ist offen.

### Vorteile

- deutlich geringerer Batteriestrom bei gleicher Systemleistung;
- 13 W entsprechen idealisiert ~1,8 A bei 7,2 V;
- 5-V-Systemrail kann aus dem Akku effizient per Buck erzeugt werden;
- geringere Ströme können Leitungsverluste, Connector-/Trace-Belastung und thermische Anforderungen reduzieren;
- mehr elektrische Reserve für hohe Lastspitzen.

### Nachteile / kritische Punkte

- aktuelle VRI-2S-Referenzpacks sind mechanisch deutlich größer als 1S/21700;
- das kompakte Standardgerät würde wahrscheinlich größer oder dicker;
- Laden eines 2S-Packs aus 5-V-USB-C erfordert einen Boost-Charger oder alternativ höhere USB-PD-Eingangsspannung;
- zusätzliche 5-V-Buck-Stufe kann gegenüber einer gut integrierten 1S-Lösung zusätzliche BOM/Fläche erzeugen;
- zwei Zellen in Serie erhöhen Pack-/BMS-Komplexität; diese liegt zwar beim Packhersteller, bleibt aber Teil des Gesamtsystems;
- eine gemeinsame Standard-/Extended-Packfamilie kann schwieriger werden.

## Stromvergleich

Idealisiert, ohne Wandlungsverluste:

| Systemleistung | 1S @ 3,6 V | 2S @ 7,2 V |
|---|---:|---:|
| 3,2 W | 0,89 A | 0,44 A |
| 3,8 W | 1,06 A | 0,53 A |
| 5,5 W | 1,53 A | 0,76 A |
| 8 W | 2,22 A | 1,11 A |
| 13 W | 3,61 A | 1,81 A |

Bei niedriger State of Charge und realem Wirkungsgrad steigt insbesondere der 1S-Strom deutlich. Das muss gemessen und gegen Pack, Connector, Schutzschaltung und Wandler ausgelegt werden.

## Wirkungsgrad und Laufzeit

Die reine 1S-vs.-2S-Frage entscheidet die Laufzeit nicht. Entscheidend sind Packenergie und die Wirkungsgradkurve der realen Wandler über das Lastprofil.

Ein 19,1-Wh-1S-Pack kann trotz höherer Ströme produktseitig besser sein, wenn die 5-V-Wandlung effizient ist und die kleinere Geometrie einen wesentlich kompakteren Beltpack ermöglicht. Ein 25,2-Wh-2S-Pack hat rund 32 % mehr nominelle Energie und wird deshalb unabhängig von der Topologie länger laufen; das darf nicht fälschlich als Topologieeffizienz interpretiert werden.

Prototype 1 muss deshalb Pack-seitige Eingangsleistung und 5-V-Systemleistung gleichzeitig messen und reale Wirkungsgradkurven bestimmen.

## Kosten

Die Topologie wird gegen das bestehende Power+USB-Budget von **8–11 EUR** bewertet.

Aktuelle öffentliche Preisanker zeigen, dass ein moderner hochintegrierter 1S-Charger/Power-Path wie BQ25638 bei 1k ungefähr 2,20 EUR kostet. Die IC-Kosten allein entscheiden die Frage daher nicht. Magnetics, MOSFETs soweit extern, USB-C/PD, Schutz, Messung, PCB-Fläche, Thermik und eine ggf. zusätzliche 5-V-Wandlerstufe müssen gemeinsam gerechnet werden.

**Cost Gate:** Die Wahl 2S darf nicht allein wegen theoretisch niedrigerer Ströme eine deutlich komplexere und teurere Power-Architektur erzwingen. Umgekehrt darf 1S nicht allein wegen des kleineren Packs gewählt werden, wenn eine robuste 13-W-Peakversorgung dadurch unverhältnismäßig schwierig wird.

## USB-C POWER

Die Eingangsspannungsstrategie bleibt offen. Das Produkt soll mit marktüblichen USB-C-Netzteilen komfortabel funktionieren.

Zu prüfen sind mindestens:

- 5-V-only Eingang als einfachster Nutzerfall;
- USB-C Current Advertisement ohne vollständiges USB-PD;
- USB-PD mit 9 V oder höher, wenn dadurch Laden/Thermik/Power Path substanziell verbessert werden;
- Verhalten mit schwachen Netzteilen: Systemlast priorisieren, Ladestrom reduzieren;
- Betrieb mit entnommenem oder leerem Akku an externer Versorgung.

USB-PD wird nicht allein deshalb eingeführt, weil es technisch möglich ist.

## Mechanik und Produktstrategie

Hier hat 1S derzeit den größten systemischen Vorteil. Der VRI-1S/21700-Referenzpack ist nur etwa 22,5 mm dick/breit und unterstützt die Miniaturisierungsstrategie deutlich besser als der aktuelle 2S/18650-Referenzpack.

Die Entscheidung wird deshalb nicht als „welche elektrische Topologie ist eleganter?“ getroffen, sondern als Produktoptimierung aus:

**Gerätegröße + Laufzeit + Feldwechsel + Power-Integrität + Thermik + BOM + Hersteller-Packfamilie.**

## Vorläufige Bewertung

| Kriterium | 1S | 2S |
|---|---|---|
| Standard-Pack-Kompaktheit | **stark** | schwächer |
| niedrige Batteriestromstärke | schwächer | **stark** |
| 5-V-Systemversorgung | Boost erforderlich | Buck erforderlich |
| 5-V-USB-C-Laden | **einfacher** | Boost-Charger erforderlich |
| integrierte Portable-Power-ICs | **sehr stark** | gut |
| 13-W-Peakreserve | kritisch zu validieren | **komfortabler** |
| Standardgerät möglichst klein | **stark** | schwächer |
| Kostenpotenzial | **gut** | gut, aber ggf. mehr Stufen |
| Extended-Pack-Familie | mit VRI klären | mit VRI klären |

## Aktuelle Richtung

**CANDIDATE / PREFERRED FOR PROTOTYPE VALIDATION:** 1S soll als bevorzugte Ausgangstopologie für Prototype 1 behandelt werden, weil sie mit dem ~19-Wh-VRI-Pack die stärkste Miniaturisierung ermöglicht und moderne integrierte Power-Path-/Boost-Lösungen die erforderliche Leistung grundsätzlich plausibel erscheinen lassen.

Das ist **keine Serienentscheidung**.

1S wird verworfen bzw. neu bewertet, wenn Prototype/RFQ zeigt, dass mindestens einer der folgenden Punkte nicht mit vernünftiger Reserve erreichbar ist:

1. stabile 5-V-Systemschiene bei niedriger Packspannung;
2. ~8 W interner Design-Peak;
3. ~13 W kurzfristiger System+USB-Accessory-Designfall;
4. akzeptable Wandler-/PCB-Temperatur;
5. akzeptabler EMI-/Audio-Noise-Einfluss;
6. Power+USB-BOM innerhalb des 8–11-EUR-Budgets;
7. sinnvoller Wirkungsgrad im realen 3,2–5,5-W-Hauptlastbereich;
8. ausreichende VRI-Freigabe für Lastprofil und Steck-/Kontaktkonzept.

## Prototype-1-Messgate

Für 1S sind mindestens zu messen:

- 5-V-Regulation über gesamten zulässigen Packspannungsbereich;
- Wirkungsgrad bei 3,2 / 3,8 / 5,5 / 8 / 13 W;
- Packstrom bei niedrigem SoC;
- Lastsprünge Compute/Wi-Fi/Audio/USB;
- USB-Accessory 0 / 0,5 / 1,0 A;
- gleichzeitiges Laden + Systemlast;
- thermische Hotspots;
- Audio-Störgeräusche/EMI bei Boost-Betrieb;
- Verhalten bei Akkuentnahme, externer Versorgung und Wiederanlauf.

Erst danach wird 1S oder 2S für die Serienarchitektur festgelegt.
