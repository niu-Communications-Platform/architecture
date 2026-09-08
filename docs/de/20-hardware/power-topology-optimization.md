# Power-Topologie: Konsolidierung und Serienoptimierung

**Deutsch (kanonisch)** | [English](../../en/20-hardware/power-topology-optimization.md)

## Zweck

Dieses Dokument prüft, ob die aktuelle Prototype-1-Power-Architektur

```text
PD Sink → Buck-Boost Charger / Power Path → Battery/System Node → separater 5-V-Boost → 5V_SYS
```

für die Serie unnötig viele Leistungsstufen enthält oder ob sie trotz scheinbarer Redundanz die robusteste Lösung bleibt.

Die Battery-Pack/BMS-Verantwortungsgrenze bleibt unverändert: Pack-Sicherheit und Zellmanagement gehören zum serienreifen Battery Pack; der Carrier übernimmt ausschließlich Systemstrom und spezifikationskonforme Ladeintegration.

## Ausgangslage

Für das Beltpack gelten insbesondere:

- 1S-Pack als bevorzugte Prototype-1-Richtung;
- robuste `5V_SYS` für Compute und Audio;
- ACCESSORY USB-C bis ungefähr 5 V / 1 A;
- Betrieb mit und ohne eingesetzten Akku an externer Versorgung;
- USB-C-PD als sinnvoller Weg für Vollbetrieb plus Laden;
- schwache Quellen dürfen Laden begrenzen, aber das System nicht destabilisieren;
- Akkuentnahme ohne Shutdown ist zulässig;
- Power+USB-Zielbudget 8–11 EUR;
- hohe Audio-/EMI-Anforderungen.

## Erkenntnis zum BQ25798

Der BQ25798 besitzt zwei unterschiedliche für uns relevante Versorgungsknoten:

- `SYS` folgt im Wesentlichen der Batteriespannung oberhalb `VSYSMIN` und ist daher bei 1S **keine feste 5-V-Schiene**;
- `PMID` liegt im normalen Vorwärtsbetrieb ungefähr auf Eingangsspannung und kann im Backup-/OTG-Betrieb aus der Batterie auf eine geregelte Spannung, z. B. 5 V, gebracht werden.

Damit kann der BQ25798 zwar prinzipiell aus der 1S-Batterie selbst eine geregelte 5-V-Backup-Spannung erzeugen, er kann aber nicht gleichzeitig in allen Betriebsarten einfach als universeller fester 5-V-Systemausgang betrachtet werden. Insbesondere würde bei einem 9-V-PD-Eingang `PMID` im Vorwärtsbetrieb ungefähr 9 V führen.

**Konsequenz:** Die separate 5-V-Regelung ist nicht bloß aufgrund eines Missverständnisses vorhanden.

## Variante A — aktuelle Architektur: SYS → separater Boost auf 5V_SYS

```text
USB-C PD
  ↓
PD Controller
  ↓
BQ25798
  ↔ Battery
  ↓ SYS (~battery domain)
5-V Boost
  ↓
5V_SYS
```

### Vorteile

- `5V_SYS` ist in allen Betriebsarten derselbe logisch definierte Ausgang;
- Betrieb aus Akku und externer Versorgung wird für Compute/Audio entkoppelt;
- externe 5-V-, 9-V- und ggf. 12-V-Eingänge ändern die Systemrail nicht;
- Battery Supplement/Power Path des Chargers bleibt nutzbar;
- sauber mess- und validierbare Funktionsblöcke;
- weniger Betriebsmodi auf der 5-V-Systemschiene;
- guter Prototype-1-Ansatz für Debugging, Thermik und EMI-Messung.

### Nachteile

- bei externer PD-Versorgung kann Energie zunächst auf den Battery/System-Domain-Niveau gewandelt und anschließend wieder auf 5 V geboostet werden;
- dadurch zusätzliche Wandlungsverluste im stationären Betrieb;
- zusätzlicher Regler, Induktor, Passives, PCB-Fläche und BOM;
- aktueller Kostenanker der Boost-Stufe ist signifikant.

## Variante B — PMID als 5-V-Systemschiene

Im Batteriebetrieb könnte BQ25798 Backup/OTG nutzen, um `PMID` auf 5 V zu regeln. Bei 5-V-Eingang wäre `PMID` ebenfalls ungefähr 5 V.

Das erscheint zunächst elegant, scheitert für unser Zielbild aber an mehreren Punkten:

1. Bei 9-V-PD-Eingang liegt `PMID` im Vorwärtsbetrieb ungefähr auf 9 V, nicht auf 5 V.
2. Das würde entweder PD auf 5 V beschränken oder eine weitere Abwärtsstufe verlangen.
3. 5 V / 3 A bietet nur 15 W Eingangsleistung und damit für unseren 13-W-Stressfall kaum Lade- und Verlustreserve.
4. Backup Mode erfordert definierte Host-/Rearm-Logik und ist damit kein völlig autonomer universeller Rail-Ersatz.
5. Die Systemarchitektur würde stärker vom Betriebsmodus des Chargers abhängen.

**Bewertung:** Für die aktuelle Zielsetzung nicht bevorzugt.

## Variante C — externer 5-V-Pfad bei Netzbetrieb, Boost nur bei Akku

```text
                  ┌─ Buck 9V→5V ──────────┐
USB-C PD ─────────┤                        ├─ ideal power mux / OR → 5V_SYS
                  └─ Charger → Battery ─ Boost 1S→5V ─┘
```

Diese Architektur könnte im stationären 9-V-PD-Betrieb den Umweg über den Battery-Domain vermeiden.

### Potenzielle Vorteile

- höhere stationäre Effizienz;
- weniger Verlustwärme im Charger-/Battery-Pfad bei Netzbetrieb;
- Batterie kann unabhängig geladen werden;
- 5-V-Boost läuft im Idealfall nur bei Akku-/Supplement-Betrieb.

### Nachteile

- zusätzliche 9-V→5-V-Buck-Stufe;
- Power-Mux-/Ideal-Diode-/ORing-Logik erforderlich;
- schwierigeres nahtloses Umschalten und Transientenverhalten;
- mehr FETs/Controller/Schutzpfade;
- mehr Failure Modes und mehr EOL-Testfälle;
- höhere PCB-/Layout-Komplexität;
- Gefahr, die durch einen eingesparten Regler erhofften Kosten an anderer Stelle wieder zu verbrauchen.

**Bewertung:** Als Serienoptimierung interessant, aber nicht automatisch billiger oder einfacher.

## Variante D — ein einzelner echter System-Buck-Boost hinter einer geeigneten Power-Path-Architektur

Eine theoretisch attraktive Lösung wäre ein Systemwandler, der sowohl einen externen PD-Domain-Eingang als auch den 1S-Batteriepfad auf feste 5 V abbildet.

Das setzt jedoch einen passenden Power-Mux bzw. einen Charger voraus, dessen Systemknoten die erforderliche Spannungsdomäne sinnvoll bereitstellt. Ein einzelner Wandler allein ersetzt die Lade-/Power-Path-Funktion nicht.

**Bewertung:** Für die Serie prüfen, sobald reale Last- und Wirkungsgraddaten vorliegen; derzeit kein klarer Beweis, dass dadurch BOM, Fläche und Komplexität tatsächlich sinken.

## Wichtige neue Schlussfolgerung

**CANDIDATE / PREFERRED FOR PROTOTYPE 1:** Die bestehende Drei-Block-Struktur bleibt für Prototype 1 bestehen:

```text
PD Controller
    ↓
Buck-Boost Charger / NVDC Power Path
    ↔ production Battery Pack
    ↓
dedicated regulated 5V stage
    ↓
5V_SYS
```

Der Grund ist nicht Konservatismus, sondern Messbarkeit und einheitliches Systemverhalten.

Prototype 1 soll zuerst beantworten:

- wie hoch der reale Verlust der doppelten Wandlung bei externer PD-Versorgung ist;
- wie oft und wie lange das Produkt real stationär mit Netzteil läuft;
- wie viel Wärme tatsächlich im Charger und 5-V-Regler entsteht;
- wie hoch der reale Mehrpreis des separaten Boost-Pfads bei Serien-RFQ ist;
- ob eine Alternative mit Buck + Boost + Power-Mux in Summe wirklich weniger kostet;
- ob der zusätzliche Moduswechsel einer optimierten Architektur Audio-, EMI- oder Zuverlässigkeitsnachteile erzeugt.

## Optimierungs-Gate nach Prototype 1

Eine komplexere Dual-Path-/Bypass-Architektur wird nur eingeführt, wenn sie gegenüber der Prototype-Architektur **messbar** mindestens zwei der folgenden Vorteile bringt, ohne andere P0-Anforderungen zu verschlechtern:

1. mindestens ca. 1 EUR reale Serien-BOM-Ersparnis;
2. relevante PCB-Flächenreduktion;
3. deutlich bessere stationäre Effizienz;
4. relevante thermische Entlastung;
5. geringere Bauteilanzahl oder höhere Zuverlässigkeit;
6. einfachere Beschaffung / bessere Second-Source-Situation.

Eine bloß theoretisch „elegantere“ Schaltung reicht nicht.

## Architekturregel

> **Minimize power stages only when the complete system becomes simpler. Fewer converter blocks are not a goal by themselves.**

Für das Beltpack gilt außerdem:

> **A single stable 5V_SYS behavior across battery, weak USB-C and PD operation is more valuable than saving one converter on paper.**

## Serienrichtung

Noch keine finale Serienentscheidung.

- Prototype 1: bestehende Drei-Block-Struktur aufbauen und messen.
- Parallel: aktuelle Boost-Alternativen und mögliche Dual-Path-/Power-Mux-Lösungen beobachten.
- Nach Messdaten: stationäre und mobile Wirkungsgradkurven gegeneinanderstellen.
- Erst dann entscheiden, ob die Serie die Prototype-Topologie unverändert übernimmt oder eine belegbar bessere Konsolidierung erhält.
