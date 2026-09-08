# Vorläufige MPN-Level-Power-BOM

**Deutsch (kanonisch)** | [English](../../en/20-hardware/power-mpn-bom.md)

## Zweck

Dieses Dokument übersetzt die bevorzugte 1S-Power-Architektur für Prototype 1 erstmals in konkrete Bauteilklassen und Referenz-MPNs. Es ist **keine Serien-BOM und keine Freigabe einzelner Bauteile**. Ziel ist, Kosten, Funktionsüberschneidungen, Entwicklungsrisiken und Prototype-Beschaffung früh sichtbar zu machen.

Die Verantwortung bleibt unverändert: Der serienreife Battery Pack besitzt eigenes BMS/Schutz/Fuel Gauge. Der Carrier übernimmt Systemstrom und spezifikationskonforme Ladeintegration.

## Architektur

```text
POWER USB-C
  ↓
ESD / Type-C / PD Sink
  ↓
wide-input buck-boost charger + NVDC power path
  ↔ production-ready 1S Battery Pack with own BMS
  ↓
SYS_BAT
  ↓
dedicated synchronous boost
  ↓
5V_SYS
  ├─ Compute / Carrier
  └─ protected ACCESSORY USB-C 5 V / ~1 A
```

## Referenz-MPNs für Prototype 1

| Funktion | Referenz-MPN | Status | öffentlicher 1k-Preisanker* | Bemerkung |
|---|---|---|---:|---|
| USB-C PD Sink / POWER-Port | TI TPS25730SRSMR / TPS25730A-Klasse | CANDIDATE | ~1,30 EUR | Stand-alone Sink, geschützter Power Path; genaue A-Variante/Package vor Schaltplan prüfen |
| Charger + NVDC Power Path | TI BQ25798RQMR | CANDIDATE | ~2,61 EUR | 1–4S Buck-Boost; für nıu als 1S-Integration genutzt, nicht als Pack-BMS |
| 5V_SYS Boost | TI TPS61088-Klasse | CANDIDATE | ~2,9–3,8 EUR je nach Variante/Staffel | Preisanker höher als frühere Annahme; Alternativen müssen aktiv geprüft werden |
| ACCESSORY VBUS Current Limit | TI TPS2553DBVR-Klasse | REFERENCE | ~0,47 EUR | Strombegrenzung/OCP; Reverse-Current-Anforderung separat verifizieren |
| USB-C / ESD / CC / Schutz | offen | ALLOWANCE | ~0,4–0,8 EUR | finale Protection-Architektur abhängig von PD-/Connector-Auswahl |
| Magnetics für Charger/Boost | offen | ALLOWANCE | ~0,8–1,5 EUR | Strom, DCR, Sättigung, EMI und Bauhöhe entscheidend |
| Sense-/Filter-/Power-Passives | offen | ALLOWANCE | ~0,5–1,0 EUR | Shunts, Caps, Widerstände, Gate/Filter etc. |

\* Öffentliche Distributorpreise sind Engineering-Anker, keine RFQs und keine garantierten Serienpreise.

## Erste Kostenbewertung

Mit den aktuell sichtbaren öffentlichen Preisen ergibt die funktionale Power-Kette grob:

```text
PD Sink                     ~1.3 EUR
Charger / Power Path        ~2.6 EUR
5V Boost                    ~2.9–3.8 EUR
Accessory protection        ~0.5 EUR
Protection / ESD            ~0.4–0.8 EUR
Magnetics                   ~0.8–1.5 EUR
Power passives              ~0.5–1.0 EUR
-------------------------------------
Engineering range           ~9.0–12.0 EUR
```

Damit liegt die erste MPN-nahe Betrachtung **am bzw. leicht oberhalb** des bisherigen Power+USB-Zielbudgets von 8–11 EUR. Das ist noch kein Architektur-Fail, aber ein echtes Cost-Gate.

## Wichtigste neue Erkenntnis

Der bisher verwendete Preisanker von etwa 1,3 EUR für TPS61088 war zu optimistisch für die aktuell leicht beschaffbaren Standardvarianten. Öffentliche aktuelle Staffelpreise liegen eher um etwa 2,9 EUR bei größerer Reel-Menge bzw. bis rund 3,8 EUR für bestimmte Varianten bei 1k.

**REVIEW:** Der 5V_SYS-Wandler wird deshalb zum primären Kosten-/Effizienz-Optimierungspunkt der Power-BOM. Vor Serienauswahl werden mindestens verglichen:

- TPS61088 und neuere TI-Alternativen;
- geeignete Boost-Regler anderer etablierter Hersteller;
- erforderliche reale Dauer-/Peak-Leistung statt Datenblatt-Maximalleistung;
- integrierte vs. externe MOSFETs;
- Wirkungsgrad bei 3,2–5,5 W Hauptlast;
- Low-SoC-Verhalten bei 8/13-W-Stressfall;
- Bauhöhe und Induktorgröße;
- Forced-PWM/EMI-Verhalten für Audio;
- 1k/5k/10k RFQ-Preis und Lifecycle.

Eine Einsparung von 1–2 EUR an diesem Block ist wirtschaftlich relevant, darf aber nicht durch schlechtere Thermik, hörbares Switching Noise oder zu geringe Peakreserve erkauft werden.

## Funktionsüberschneidungen vermeiden

Die BOM wird ausdrücklich auf doppelte Funktionen geprüft. Insbesondere:

- PD-Controller-Power-Path nicht zusätzlich durch unnötige externe FET-/Protection-Stufen duplizieren;
- Charger-Messfunktionen nutzen, soweit sie die Anforderungen erfüllen;
- Pack-Fuel-Gauge nicht auf dem Carrier nochmals nachbauen;
- Pack-Schutz nicht auf dem Carrier ersetzen;
- ACCESSORY-Schutz nur so komplex wie für 5 V / ~1 A und Fehlerisolation nötig;
- keine separate zweite 5-V-Hauptversorgung für ACCESSORY.

## Noch nicht enthalten

Diese frühe Power-BOM enthält noch nicht belastbar:

- konkrete USB-C-Buchsen;
- exakte Induktor-MPNs;
- alle Kondensatoren und deren Derating;
- Hardware-Power-Latch / ≥8-s-Hard-Off;
- eventuell nötige Ideal-Diode-/Reverse-Blocking-Funktion;
- konkrete Pack-Steck-/Kontaktlösung;
- PCB-Flächen-/Kupfer-/Thermikkosten;
- VRI-spezifische Host-Schnittstelle/Pull-ups/Protection;
- lokale 3V3/1V8-Regler, sofern diese nicht ohnehin dem Carrier-Core zugerechnet werden.

Diese Positionen müssen vor dem echten Schematic Cost Gate ergänzt werden.

## Beschaffungs-/Lifecycle-Hinweise

BQ25798 ist aktuell aktiv und öffentlich gut verfügbar, weist bei Distributoren aber Hersteller-Lieferzeiten im Bereich mehrerer Monate für Mengen oberhalb des Lagerbestands auf. Deshalb werden Serien-MPNs nicht nur nach Stückpreis, sondern nach Lifecycle, Second Source auf Architekturebene, Forecast-Fähigkeit und Herstellerunterstützung bewertet.

## Prototype-1-Empfehlung

Für Prototype 1 ist es sinnvoll, zunächst mit gut dokumentierten Referenzbausteinen zu arbeiten, auch wenn diese noch nicht die billigste Serienlösung sind. Ziel des ersten Prototyps ist der Nachweis der Architektur:

1. 1S-Pack funktioniert über gesamten SoC-Bereich;
2. 5V_SYS bleibt stabil;
3. PD + Laden + Systemlast funktionieren zusammen;
4. Betrieb ohne Akku funktioniert;
5. 13-W-Stressfall ist beherrschbar;
6. Audio bleibt störungsfrei;
7. Thermik ist akzeptabel.

Erst danach wird die Serien-BOM kostenoptimiert.

> **Prototype 1 optimiert Erkenntnisgewinn. Die Serien-BOM optimiert Kosten – ohne die validierten Sicherheits-, Audio- und Power-Eigenschaften wieder zu verlieren.**

## Cost Gate

**TARGET:** Power+USB weiterhin ≤11 EUR in Serienkalkulation, bevorzugt 8–10 EUR.

**REVIEW:** Wenn belastbare 5k/10k-RFQs trotz Bauteiloptimierung >11 EUR ergeben, werden zuerst 5V-Boost, PD-Controller-/Protection-Integration und Magnetics optimiert. Die Battery-Pack/BMS-Verantwortungsgrenze wird **nicht** zur Kostenreduktion aufgeweicht.
