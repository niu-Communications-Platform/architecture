# Vorläufige kostenbewertete Product-Core-/Carrier-BOM

**Deutsch (kanonisch)** | [English](../../en/20-hardware/carrier-costed-bom.md)

## Zweck

Dieses Dokument hält die **architektonischen Kostenanker des gemeinsamen nıu Product Core** fest. Es ist keine führende Serien-BOM und kein Ersatz für die plattformspezifischen Costed BOMs im `product-development`-Repository.

Seit der Trennung in **CM-Plattform** und **Zero-Plattform** gilt:

```text
Common Product Core
+
CM-spezifischer Carrier   ODER   Zero-spezifischer Carrier
+
Compute
=
vollständiges Beltpack
```

Die führenden Szenariokosten liegen in:

- `product-development/bom/beltpack-costed-bom.de.md` — Common Core;
- `product-development/bom/beltpack-cm-platform-costed-bom.de.md` — CM;
- `product-development/bom/beltpack-zero-platform-costed-bom.de.md` — Zero.

## Gemeinsame Core-Komponenten mit Preisankern

| Funktion | Kandidat | Menge | Planwert / Anker |
|---|---|---:|---:|
| Audio Codec | TLV320AIC3204IRHBR | 2 | **ca. 5,2 EUR gesamt** |
| Speaker Amp | TAS2505IRGER | 1 | **ca. 0,8 EUR** |
| Secure Element | ATECC608C-TFLXTLS class | 1 | **1,0 EUR Allowance** |
| Carrier EEPROM | 24CS64 class | 1 | **ca. 0,3 EUR** |
| GPIO Expander | MCP23017 class | 1 | **1,0 EUR Allowance** |
| RGB LED Driver | PCA9955 class | 1 | **ca. 1,1 EUR** |

Sichtbare Core-IC-Zwischensumme: grob **9,4 EUR**. TrustFLEX-Serienpreis bleibt RFQ.

## Gemeinsame Funktionsblöcke

| Product-Core-Block | Ziel/Planwert EUR | Hinweis |
|---|---:|---|
| 2× Audio Codec | 5,2 | AIC3204 class |
| Speaker Amp | 0,8 | TAS2505 class |
| Secure Element | 1,0 | TrustFLEX class |
| NVM + GPIO + RGB PWM | 2,4 | EEPROM, Expander, LED Driver |
| Audio Analog Front End | 2,0–3,0 | Bias, Filter, Schutz, Detect/Umschaltung |
| USB-C Accessory Port Control | 1,5–2,5 | CC, VBUS limit, reverse protection, OCP, ESD |
| USB-C Power Input + Schutz | 0,8–1,5 | Connector-nahe Funktionen; Charger separat |
| Power Path / Charger / DC-DC | 4,0–6,0 | finale Dimensionierung muss CM/Zero-Peaks tragen |
| Fuel/Power/Temperature Monitoring | 0,5–1,0 | soweit nicht vollständig vom Pack bereitgestellt |
| Oscillators/Clocking | 0,3–0,7 | soweit produktweit benötigt |
| ESD/EMI/Protection | 1,0–1,8 | externe Audio-/USB-/Power-Ports |
| allgemeine Passives/Regulators/Glue | 2,0–3,0 | nur plattformneutrale Anteile |
| Testpunkte / Factory Interface | 0,5–1,0 | DFT-relevante gemeinsame Hardware |

Diese Werte sind Engineering-Anker. Die führende Common-Core-BOM im Product-Development-Repository verhindert Doppelzählung.

## Nicht mehr als gemeinsamer Carrier-Block rechnen

Folgende Positionen sind **plattformabhängig** und dürfen nicht in einem einzigen universellen Carrier-Budget versteckt werden:

- Compute Module / SBC;
- CM-B2B- beziehungsweise Zero-40-Pin-/SBC-Interconnect;
- Compute→USB-Hub-/CT7601-Datenpfad;
- Compute-spezifische Power-Einspeisung, Boot/Recovery und Level/Glue;
- Compute-Mounting und interne Keep-outs;
- Carrier-PCB;
- Carrier-PCBA/AOI;
- Zero/Pi-Zero-spezifische Storage-Deltas.

### CM-Plattform

Radxa CM3, Radxa CM4 und Raspberry Pi CM4 sollen nach Möglichkeit denselben identisch bestückten CM-Carrier über die sichere 2×100-Pin-Schnittmenge nutzen.

### Zero-Plattform

Radxa ZERO 3W und Raspberry Pi Zero 2 W bilden die Zero-Familie. Ein gemeinsamer Carrier ist Ziel, aber die elektrische Gleichheit ist noch nicht vollständig validiert; insbesondere USB und Storage unterscheiden sich.

## USB-Lifecycle-Regel

Ein aktiver USB-Hub kann je nach Plattform nötig sein. Der spezifische USB2514BI bleibt wegen **NRND** keine Serienentscheidung.

**REVIEW:** Plattformweise einen aktiven, langfristig geeigneten USB-2.0-Hub/Interconnect-Pfad definieren. Historischer Zielwert für Hub + Clock/Config: **ca. 2,0–2,8 EUR**, bis konkrete MPNs/Topologien vorliegen.

Dieser Betrag ist **kein Common-Core-Aufschlag** mehr, sondern gehört in die jeweilige Plattform-BOM.

## HMI und mechanisch belastete I/O-Komponenten

Diese Produktfunktionen bleiben grundsätzlich gemeinsam:

| Block | Planwert EUR |
|---|---:|
| 1,3–1,5 Zoll TFT | 2,0–3,5 |
| 4 RGB LEDs + Lichtführung-Anteil | 0,3–0,8 |
| PTT + Buttons/Encoder | 1,0–2,0 |
| interne Mikrofone | 0,5–1,2 |
| interner Speaker | 0,8–1,5 |
| MIC / PHONES / TRRS | 1,0–2,0 |
| sichtbare 2× USB-C Buchsen | 0,4–1,0 |

Interne Compute-Befestigung, interne Kabel/Interconnects und PCB-spezifische Mechanik gehören dagegen in CM bzw. Zero.

## PCB und deutsche Bestückung

Die bisherigen generischen Zielkorridore bleiben nur als Plausibilitätsanker:

- nackte Carrier-PCB: **1,5–3 EUR**;
- deutsche SMT/THT-Bestückung + AOI: **4–7 EUR**.

Sie werden **nicht** mehr als gemeinsamer Kostenblock addiert. CM-Carrier und Zero-Carrier werden separat geroutet, gefertigt und gequotet.

## DFMA-Regel

Jeder manuell zu lötende Draht, jedes zusätzliche Kabel, jede THT-Buchse und jede zweite Bestückungsseite ist deutsche Fertigungszeit. Deshalb wird nicht nur Bauteilpreis, sondern **Total Platform Assembly Cost** verglichen.

## Kostenziel

Gesamtziel des vollständigen Beltpacks bleibt:

- bevorzugte Gesamt-COGS: **≤75 EUR**;
- akzeptabel: **75–80 EUR**;
- >94,50 EUR aktuelles Fail-Territory.

Die frühere einfache Carrier-Summe von 36,5–52 EUR darf nicht mehr als eine plattformunabhängige Serienzahl verwendet werden; sie war ein früher breiter Architekturanker und vermischte inzwischen getrennte Common-/Platform-Blöcke.

## Wichtigste Kostenrisiken

1. **Compute + Plattformintegration** — aktuell stärkste neue Differenz zwischen CM und Zero.
2. **Power** — muss Leistungspeaks der finalen Compute-Familie tragen.
3. **USB** — insbesondere shared-carrier-tauglicher Datenpfad ohne Compute-Rework.
4. **Mechanik/Interconnect** — B2B versus SBC-Header/Kabel/Mounting.
5. **Audio-Umschaltung / CTIA-OMTP**.
6. **deutsche Montage / EOL**.

## Gate

> **Common Core gemeinsam optimieren; CM und Zero getrennt bis zum gleichen funktionalen Endpunkt kalkulieren. Kein Universal-Carrier-Budget und keine Doppelzählung.**
