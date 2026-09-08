# Audio-MPN-BOM und Analog-I/O-Review

**Deutsch (kanonisch)** | [English](../../en/40-audio/audio-mpn-bom.md)

## Zweck

Dieses Dokument konkretisiert die bestehende Audioarchitektur auf MPN-/Kostenebene. Es bewertet insbesondere die beiden Audio-Codecs, den internen Speaker-Amp, CTIA/OMTP-Umschaltung, Jack-Detect und ESD. Es ist **keine Serienfreigabe einzelner Bauteile**.

Grundlage bleibt die bestehende Zielarchitektur mit zwei TLV320AIC3204, separatem digitalen Speaker-Amp, getrennten MIC-/PHONES-/TRRS-Buchsen und gemeinsamem TDM-Bus.

## Wichtigstes Ergebnis

Die bisherige Audioarchitektur bleibt wirtschaftlich plausibel. Die größten Kosten liegen nicht bei CTIA/OMTP oder ESD, sondern bei den **zwei Codecs selbst**.

Aktuelle öffentliche Preisanker bei etwa 1k Stück:

| Block | Kandidat / Referenz | ca. 1k-Preis | Status |
|---|---|---:|---|
| Codec #1 | TLV320AIC3204IRHBR | 2,57 EUR | CANDIDATE |
| Codec #2 | TLV320AIC3204IRHBR | 2,57 EUR | CANDIDATE |
| interner Speaker-Amp | TAS2505IRGER | 0,76 EUR | CANDIDATE |
| CTIA/OMTP + Jack-Detect | TS3A225ERTER | 0,47 EUR | CANDIDATE |
| 4-kanaliger ESD-Schutz | TPD4E05U06DQAR | 0,18 EUR | REFERENCE CLASS |

**Sichtbare Kern-Audio-ICs:** rund **6,55 EUR** bei 1k, noch ohne Analogpassive, zusätzliche ESD-Kanäle, Buchsen, Mikrofone, Lautsprecher und mechanische Integration.

Die Preisanker sind Distributionspreise, keine Serien-RFQ-Preise.

## 2× TLV320AIC3204

Der TLV320AIC3204 bleibt als Prototype-/Serienkandidat attraktiv:

- aktiver TI-Baustein;
- Stereo-ADC + Stereo-DAC;
- sechs analoge Eingänge;
- Kopfhörer-/Line-Ausgänge und Mic Bias;
- TDM/I²S/DSP-Schnittstelle;
- SPI und I²C;
- Linux-mainline-Familientreiber `tlv320aic32x4`;
- niedriger Stromverbrauch;
- 5 × 5 mm VQFN.

Aktueller Mouser-Preisanker für `TLV320AIC3204IRHBR`: ca. **2,57 EUR @1k**. Zwei Codecs liegen damit öffentlich bei rund **5,14 EUR**.

### Warum zwei Codecs weiterhin sinnvoll sind

Ein einzelner Codec wäre billiger, würde aber die aktuell gewünschte physische Trennung und Anzahl analoger Ein-/Ausgänge deutlich einschränken. Zwei Codecs ermöglichen:

- PHONES getrennt von TRRS;
- mehrere analoge Capture-Pfade;
- internes Mikrofon + separate MIC + TRRS-Mikrofon;
- optionale zweite interne Mikrofonquelle;
- unabhängige Kopfhörer-/Headset-Ausgänge;
- saubere TDM-Zuordnung.

**Cost Rule:** Ein Wechsel auf einen einzelnen Codec wird nur verfolgt, wenn dadurch mindestens etwa 2 EUR Systemkosten eingespart werden, **ohne** wichtige Audio-Endpunkte, Diagnosefähigkeit oder Routingfreiheit zu verlieren.

## Codec-Steuerung

Die bisherige SPI-Richtung bleibt sinnvoll, weil der AIC3204 eine feste I²C-Adresse besitzt und zwei identische Bausteine auf demselben I²C-Bus zusätzliche Adressierungslogik erfordern würden.

Bevorzugter Prototype-Ansatz:

```text
SPI SCLK/MOSI/MISO shared
    ├─ CODEC1_CS
    └─ CODEC2_CS
```

RESET pro Codec bleibt wünschenswert.

## Interner Speaker-Amp

**CANDIDATE:** `TAS2505IRGER`

Aktueller DigiKey-Preisanker:

- ca. 0,76 EUR @1k;
- ca. 0,71 EUR bei voller 3k-Rolle.

Relevante Eigenschaften:

- aktiv;
- digitaler Audioeingang;
- Class-D;
- bis ca. 2 W an 4 Ohm;
- I²C-Steuerung;
- Thermal Protection;
- 4 × 4 mm VQFN.

Das passt zur bisherigen Idee, den internen Speaker als eigenen digitalen/TDM-Endpunkt zu behandeln und nicht über einen zusätzlichen analogen Leistungsverstärker hinter einem Codec zu führen.

**REVIEW:** Vor Serienfreeze müssen TDM-Kompatibilität, Linux/Device-Agent-Initialisierung, Lautsprecherwirkungsgrad, akustische Ziel-Lautstärke und thermische Reserve gemeinsam getestet werden.

## CTIA/OMTP: einfacher als zunächst befürchtet

Die CTIA/OMTP-Unterstützung muss nicht als komplexe diskrete Umschaltung aufgebaut werden.

TI führt mehrere aktive spezialisierte Audio-Jack-Switches, die GND/MIC automatisch erkennen und umschalten.

### TS3A226AE

Der `TS3A226AE` unterstützt autonome Erkennung von 3-poligen und 4-poligen Headsets sowie MIC/GND-Erkennung für die beiden üblichen TRRS-Belegungen. Technisch passt er sehr gut, ist aber nur in einem sehr kleinen 1,4 × 1,4 mm DSBGA verfügbar.

**Bewertung:** Funktional attraktiv, für eine robuste, gut fertigbare Carrier-PCB aber nicht der bevorzugte Package-Startpunkt.

### TS3A225E

**CANDIDATE / PREFERRED PACKAGE FOR PROTOTYPE:** `TS3A225ERTER`

- aktiv;
- 3 × 3 mm WQFN-16;
- autonome GND/MIC-Erkennung;
- unterstützt 3-polige und 4-polige Headsets;
- manuelle I²C-Steuerung möglich;
- integrierte Codec-Sense-Funktion;
- aktuelle öffentliche Kosten etwa **0,47 EUR @1k**.

Der Baustein kostet damit nur einen kleinen Teil eines Codecs und ist gleichzeitig deutlich EMS-freundlicher als der winzige DSBGA des TS3A226AE.

### TS3A227E

Der `TS3A227E` ist ebenfalls aktiv und bietet eine umfangreichere autonome Zubehörerkennung, I²C, Key-Press-Detection und weitere Funktionen. Er ist unter anderem als VQFN verfügbar.

**REVIEW:** TS3A227E wird mit TS3A225E verglichen, falls Inline-Headset-Tasten oder detailliertere Zubehördiagnose für V1 echten Produktnutzen bieten.

## Produktentscheidung zu CTIA/OMTP

**CANDIDATE:** Für Prototype 1 wird die automatische CTIA/OMTP-Unterstützung beibehalten.

Der Mehrpreis auf IC-Ebene ist gering genug, dass eine erzwungene CTIA-only-Lösung derzeit keinen überzeugenden wirtschaftlichen Vorteil bietet.

Das passt zum Produktprinzip:

> **Kompatibilität wird intern absorbiert; der Nutzer soll nicht über Steckerbelegungen nachdenken müssen.**

Vor Serie muss dennoch geprüft werden, ob der Markt-/Supportnutzen die zusätzliche Schaltung weiterhin rechtfertigt.

## Jack Detect

Die TRRS-Erkennung soll möglichst durch den spezialisierten Headset-Switch erfolgen. Für separate MIC- und PHONES-Buchsen bleiben mechanische Detect-Kontakte an der Buchse der bevorzugte einfache Ansatz.

Damit gilt:

- TRRS: elektronische Accessory-/MIC/GND-Erkennung;
- PHONES: mechanischer Insert Detect;
- MIC: mechanischer Insert Detect;
- Software bildet daraus `connected`, `available`, `active`, `health`.

Der mechanische Detect-Kontakt ist bewusst kein Identitäts- oder Qualitätsnachweis des angeschlossenen Geräts; er ist nur Präsenzinformation.

## ESD / externe Audioanschlüsse

Jede externe Audiobuchse benötigt geeigneten ESD-Schutz. Als Preis-/Package-Referenz zeigt `TPD4E05U06DQAR`:

- 4 Leitungen;
- sehr niedrige Kapazität;
- IEC-61000-4-2-orientierte Schutzklasse;
- ca. **0,18 EUR @1k**.

Der konkrete Serien-ESD-Baustein wird anhand von Audio-Signalbereich, Package, Clamp-Verhalten und Layout gewählt. Externe Anschlüsse erhalten keine ungeschützten direkten Codec-Pins.

## Analog Front End

Noch nicht MPN-fixiert sind:

- AC-Kopplung und Filter;
- Mic-Bias-Routing;
- Schutz-/Serienwiderstände;
- ggf. Pegel-/Impedanzanpassung;
- optionale externe MIC-Bias-Schaltung;
- CTIA/OMTP-Nebenpassive;
- Pop-/Click-Verhalten;
- EMI/RF-Filter.

Frühe Kostenannahme für diese Passiv-/Analogblöcke: **ca. 1,5–2,5 EUR** insgesamt, abhängig von endgültiger Topologie.

## Mechanische Audio-Komponenten

Noch offen und daher als Engineering-Allowance zu behandeln:

| Komponente | Ziel-Allowance |
|---|---:|
| PHONES-Buchse | 0,30–0,60 EUR |
| MIC-Buchse | 0,30–0,60 EUR |
| TRRS-Buchse mit geeignetem Insert-Verhalten | 0,40–0,80 EUR |
| internes Mic 1 | 0,25–0,50 EUR |
| optionales internes Mic 2 | 0,25–0,50 EUR |
| interner Lautsprecher | 0,80–1,50 EUR |

Diese Beträge sind noch keine MPN-Preise. Insbesondere Buchsen werden nicht nur nach Stückpreis gewählt, sondern nach:

- mechanischer Lebensdauer;
- Steckzyklen;
- Zug-/Seitlast;
- PCB-Haltekräften;
- Detect-Zuverlässigkeit;
- Verfügbarkeit;
- Montageart;
- Gehäuseintegration.

## Vorläufige Audio-Kostensicht

### Kernsilizium

- 2× Codec: ~5,14 EUR
- Speaker-Amp: ~0,76 EUR
- CTIA/OMTP-Switch: ~0,47 EUR
- ESD-Referenz: ~0,18 EUR

**Subtotal:** ~6,55 EUR

### Zusätzliche Audioelektronik

- Analog-/Filter-/Bias-/Protection-Passive: ~1,5–2,5 EUR
- zusätzliche ESD-/Protection-Kanäle: ~0,2–0,5 EUR

### Mechanische Audio-I/O-Komponenten

- 3 Buchsen: ~1,0–2,0 EUR
- Mic(s): ~0,25–1,0 EUR
- Speaker: ~0,8–1,5 EUR

### Frühe Gesamtspanne Audio-Hardware

**ca. 10–14 EUR** für den kompletten Audio-Block inklusive Buchsen/Mics/Speaker, aber ohne PCB-/Bestückkostenanteil.

Das passt weiterhin grundsätzlich zum Carrier-Core+Audio-Budget von 13–17 EUR, lässt dort aber wenig Raum für zusätzliche Core-Funktionen. Deshalb dürfen Carrier-Core und Audio bei der nächsten Gesamt-BOM nicht unabhängig als jeweilige Worst-Case-Spannen addiert werden.

## Größte Kosten-/Architekturrisiken

1. **Zwei Codecs** — bereits rund 5,1 EUR öffentlich bei 1k.
2. **Mechanische Buchsen** — niedriger Stückpreis kann durch schlechte Haltbarkeit oder Montageaufwand teuer werden.
3. **Analogdetails** — Mic Bias, Schutz, Filter und CTIA/OMTP können bei zu konservativer Schaltung unnötig Passivteile akkumulieren.
4. **Interner Speaker** — Lautsprechergröße, Gehäusevolumen und akustischer Wirkungsgrad sind wichtiger als 20 Cent Bauteilersparnis.
5. **Mic 2** — nur bestücken, wenn Messungen einen echten DSP-/AEC-/Noise-Nutzen zeigen.

## Prototype-1-Audio-Gate

Prototype 1 muss mindestens validieren:

1. beide AIC3204 gleichzeitig über SPI;
2. gemeinsamer TDM-Bus auf RK3566/Radxa;
3. PHONES und TRRS gleichzeitig und unabhängig;
4. interner Speaker als eigener digitaler Endpunkt;
5. automatische CTIA- und OMTP-Erkennung mit realen Headsets;
6. 3-polige Kopfhörer am TRRS-Port;
7. mechanischer Detect für MIC/PHONES;
8. externe MIC mit und ohne Bias, soweit spezifiziert;
9. Pop/Click bei Ein-/Ausstecken und Routingwechsel;
10. ESD-/Robustheits-Vorprüfung;
11. Noise Floor, Crosstalk und THD im realen Carrier-Layout;
12. Boost-/PD-/Wi-Fi-Störeinfluss auf Analog-Audio;
13. Speaker-Lautstärke und thermische Reserve;
14. Nutzen von internem Mic 2.

## Aktuelle Richtung

**CANDIDATE / PREFERRED FOR PROTOTYPE 1:**

```text
RK3566 TDM
  ├─ AIC3204 #1 → PHONES / body microphones / MIC input
  ├─ AIC3204 #2 → TRRS L/R + headset microphone
  │                  ↕
  │             TS3A225E-class
  │             CTIA/OMTP detect/switch
  └─ TAS2505-class → internal speaker
```

Der überraschend positive Befund ist: **Automatische CTIA/OMTP-Unterstützung ist kein relevanter Kostentreiber.** Der eigentliche Audio-Kostenhebel liegt bei der Frage, ob zwei vollwertige Codecs den Produktnutzen rechtfertigen. Für Prototype 1 lautet die Antwort weiterhin: ja — messen und validieren, bevor wir dort Funktionalität wegoptimieren.
