# 1S-Power-Architektur für Prototype 1

**Deutsch (kanonisch)** | [English](../../en/20-hardware/1s-power-architecture.md)

## Zweck

Dieses Dokument konkretisiert die bevorzugte 1S-Ausgangstopologie für Prototype 1. Es ist **keine Serienfreigabe einzelner ICs**. Ziel ist eine testbare Power-Architektur, die Akku, USB-C POWER, kontinuierlichen stationären Betrieb, 5-V-Systemversorgung und ACCESSORY-USB sauber trennt.

Grundlage sind das bestehende Power Budget, die 1S-vs.-2S-Bewertung und die Entscheidung für einen serienreifen Battery Pack mit eigenem Schutz/BMS.

## Verantwortungsgrenze Battery Pack ↔ Carrier

**DECIDED:** nıu entwickelt **kein Battery Pack und kein packinternes Batteriemanagementsystem (BMS)**. Das Beltpack verwendet einen serienreifen, dokumentierten Battery Pack eines spezialisierten Herstellers. Der Pack bleibt ein eigenständiges Batteriesystem mit den vom Packhersteller vorgesehenen Schutz-, Überwachungs- und Fuel-Gauge-Funktionen.

> **The Battery Pack owns battery safety and cell management. The Carrier owns system power and charging integration. The Carrier must never substitute or bypass the Battery Pack's protection functions.**

### Verantwortung des Battery Packs / Packherstellers

Insbesondere packseitig bleiben:

- Zellen und Zellverschaltung;
- packinterne Schutzschaltung / BMS;
- Über-/Unterspannungsschutz der Zelle(n);
- packinterner Überstrom- und Kurzschlussschutz;
- packinterne Temperaturüberwachung und Schutzgrenzen;
- Zell-Balancing, falls die gewählte Packtopologie dies benötigt;
- Fuel Gauge / packinterne Zustandsdaten, soweit im Serienpack vorgesehen;
- packinterne Sicherheitslogik;
- Spezifikation der zulässigen Lade-/Entladeparameter;
- Pack-Konformitäts-, Transport- und Lifecycle-Dokumentation im vereinbarten Umfang.

### Verantwortung des nıu Carriers / Beltpacks

Der Carrier übernimmt ausschließlich die Geräteintegration des serienreifen Packs, insbesondere:

- USB-C-Eingangsleistung und PD-Verhandlung;
- Power Path / Load Sharing des Gesamtgeräts;
- Erzeugung und Verteilung der Systemspannungen;
- Versorgung und Schutz des ACCESSORY-Ports;
- Laden des Packs **innerhalb der vom Packhersteller spezifizierten und freigegebenen Grenzen**;
- Reduzieren oder Pausieren des Ladestroms aufgrund verfügbarer Eingangsleistung oder Systemzustand;
- Battery-Care-Produktlogik nur innerhalb der freigegebenen Packparameter;
- Auswertung der vom Pack bereitgestellten Status-/Fuel-Gauge-/Temperaturinformationen, soweit vorhanden;
- verständliche Darstellung des Energiezustands für Nutzer und Diagnose.

### Harte Architekturgrenzen

**DECIDED:** Der Carrier darf die Schutzfunktionen des Battery Packs weder ersetzen noch umgehen. Insbesondere werden nicht vorgesehen:

- nackte Zellen als reguläre Produktkomponente;
- eigener nıu-Zellschutz oder eigenes packinternes BMS;
- eigenes Zell-Balancing;
- eigene Zell-Sicherheitsalgorithmen als Ersatz für den Packhersteller;
- Umgehung packinterner Überstrom-, Temperatur- oder Spannungsabschaltungen;
- Ladeparameter außerhalb der Herstellerfreigabe;
- proprietäre Akku-Paarung allein zur Kundenbindung.

Der Charger/Power-Path-Controller auf dem Carrier ist damit **kein Ersatz für das Pack-BMS**. Er ist die geregelte Schnittstelle zwischen externer Energie, Systemlast und dem serienreifen Battery Pack.

Die endgültige Schaltung wird erst nach Abstimmung mit dem Packhersteller eingefroren. VRI bzw. der ausgewählte Hersteller muss insbesondere Ladeendspannung, zulässigen Lade-/Entladestrom, Temperaturgrenzen, Kommunikationsschnittstelle, Packabschaltverhalten und erforderliche Host-Reaktionen bestätigen.

Für eine mögliche Standard-/Extended-Packfamilie gilt dieselbe Grenze: Unterschiedliche freigegebene Packs dürfen unterschiedliche zulässige Parameter besitzen; der Carrier kann diese erkennen und spezifikationsgemäß anwenden, ohne selbst Battery-Pack- oder BMS-Entwickler zu werden.

## Systemziele

- 1S-Standardpack um etwa 19 Wh als bevorzugter Prototype-1-Kandidat;
- POWER USB-C ausschließlich für Versorgung/Laden;
- ACCESSORY USB-C separat als USB-Host-Port;
- Radxa und wesentliche Systemlasten auf einer robusten 5-V-Systemschiene;
- ACCESSORY USB-C bis ungefähr 5 V / 1 A;
- externer Betrieb mit gleichzeitigem Laden;
- Systembetrieb auch mit entnommenem Akku bei ausreichend leistungsfähiger externer Versorgung;
- schwache Netzteile dürfen das Gerät nicht destabilisieren: Systemlast hat Vorrang, Laden wird reduziert oder pausiert;
- Akku darf abrupt entfernt werden; kein Hot-Swap-Bridge-Speicher erforderlich;
- Hardware-Hard-Off muss unabhängig von Linux möglich bleiben;
- Power+USB-Budget weiterhin 8–11 EUR als Architekturziel.

## Kandidaten-Blockarchitektur

```text
POWER USB-C
    │
    ├─ ESD / Schutz
    │
    ▼
USB-C Sink / PD Controller
    │   bevorzugt 5 V fallback + PD 9 V/12 V
    ▼
VBUS_IN
    │
    ▼
Buck-Boost Charger + NVDC Power Path
    ├──────────────► 1S Battery Pack
    │                 BMS / Fuel Gauge im Pack
    │
    ▼
SYS_BAT
    │
    ▼
Synchronous Boost 5V
    │
    ▼
5V_SYS
    ├─ Radxa ZERO 3W
    ├─ ACCESSORY USB-C VBUS via current-limited load switch
    ├─ Audio / Speaker supply as required
    └─ lokale 3V3/1V8/etc. rails
```

**CANDIDATE:** Diese funktionale Trennung wird für Prototype 1 bevorzugt: USB-C-Verhandlung, Laden/Power Path und 5-V-Systemerzeugung sind getrennte Verantwortungsblöcke. Das erleichtert Messung, Fehlersuche, Ersatz einzelner IC-Klassen und spätere Optimierung.

## USB-C POWER: PD wird funktional sinnvoll

Ein reiner 5-V-Eingang ist grundsätzlich möglich, passt aber schlecht zum kombinierten Peak- und Ladefall.

Bei 5 V / 3 A stehen nominal 15 W am Eingang zur Verfügung. Das liegt nur knapp oberhalb des aktuellen 13-W-System+USB-Designfalls und lässt nach Wandlungsverlusten praktisch keine sinnvolle Ladeleistung übrig. Bei 5 V / 1,5 A stehen nur 7,5 W zur Verfügung; dann muss der Akku Lastspitzen ergänzen und der Ladestrom entsprechend reduziert werden.

**CANDIDATE:** Der POWER-Port soll deshalb USB Power Delivery als Sink unterstützen, gleichzeitig aber einen robusten 5-V-Fallback behalten.

Bevorzugtes Nutzerverhalten:

- **USB-C 5 V, geringe Leistung:** Gerät funktioniert soweit möglich; Laden wird begrenzt oder pausiert; Batterie kann Systemlast ergänzen.
- **USB-C 5 V / 3 A:** normaler Betrieb ist möglich, Ladeleistung hängt von aktueller Systemlast ab.
- **USB-PD 9 V / 3 A oder vergleichbar:** bevorzugter Normalfall für vollen Systembetrieb plus zügiges Laden.
- **leistungsfähigeres PD-Netzteil:** Gerät fordert nur das tatsächlich vorgesehene Profil an; kein Nutzen durch unnötig hohe Leistung.

Damit wird USB-PD nicht als Feature-Selbstzweck eingeführt, sondern weil es stationären Vollbetrieb und Laden thermisch und energetisch sauber trennt.

## PD-Controller-Klasse

**CANDIDATE:** TI TPS25730A ist ein starker aktueller Referenzkandidat für den POWER-Port:

- Sink-only;
- PD3.2-zertifiziert;
- integrierter geschützter Power Path;
- Dead-Battery-Unterstützung;
- bis 20 V / 5 A Power Path;
- Konfiguration per Pin-Strapping möglich;
- kein externes EEPROM und keine eigene PD-Firmware erforderlich;
- I²C optional für Diagnose/Status.

Diese Klasse passt gut zum Produktprinzip, Komplexität intern zu absorbieren, ohne unnötige Firmware-Abhängigkeit zu erzeugen.

**Nicht entschieden:** TPS25730A ist noch kein Serien-MPN. STUSB4500, Infineon EZ-PD BCR und weitere aktive Sink-only-Lösungen bleiben Vergleichskandidaten. Auswahlkriterien sind Lifecycle, Zertifizierungsunterstützung, BOM, Package, Protection, Verfügbarkeit und Integrationsaufwand.

## Charger / Power Path

**CANDIDATE:** Ein hochintegrierter Buck-Boost-Charger mit NVDC Power Path wird gegenüber einem einfachen 5-V-Only-1S-Charger bevorzugt geprüft.

TI BQ25798 ist dafür ein Referenzkandidat, weil er:

- 1S bis 4S unterstützt;
- 3,6–24 V Eingang akzeptiert;
- bis 5 A Ladestrom unterstützt;
- Buck-Boost-Topologie nutzt;
- BATFET, Strommessung und NVDC Power Path integriert;
- Systemlast bei begrenzter Eingangsquelle durch Battery Supplement unterstützen kann;
- ADC/I²C für Diagnose bietet.

Für nıu ist dabei nicht die 1–4S-Universalität das Ziel. Relevant ist, dass derselbe Charger-Block 5-V-Fallback und höhere PD-Eingangsspannungen sauber verarbeiten und Systemlast priorisieren kann.

**Wichtig:** Die endgültigen Ladeparameter werden ausschließlich aus der Spezifikation/Freigabe des ausgewählten VRI- oder anderen Serienpacks abgeleitet. Der Charger ist System-Power-/Ladeintegration und ersetzt niemals das packinterne BMS.

## 5V_SYS

Der 1S-/NVDC-Systemknoten liegt nicht dauerhaft auf einer für Radxa und USB geeigneten stabilen 5-V-Spannung. Daher erhält das Gerät eine separate, leistungsfähige synchrone Boost-Stufe auf `5V_SYS`.

**CANDIDATE:** TPS61088 ist eine geeignete Referenzklasse:

- 2,7–12 V Eingang;
- synchroner Boost;
- hohe integrierte Schalterstromfähigkeit;
- 4,5–12,6 V Ausgang;
- einstellbare Strombegrenzung und Schaltfrequenz;
- Forced-PWM-Modus verfügbar, was für Audio-/EMI-Validierung relevant sein kann.

Der genaue Boost-Regler wird nicht vor dem Prototyp festgelegt. Neuere Alternativen wie TPS61288 bzw. Bausteine mit explizitem Load Disconnect werden mitbewertet.

### Ziel der 5-V-Schiene

Prototype 1 soll mindestens validieren:

- stabile 5 V über den gesamten vom Packhersteller zulässigen Entladebereich;
- ca. 8 W interne Designlast dauerhaft bzw. entsprechend thermischem Lastprofil;
- ca. 13 W System+Accessory-Designfall als definierter Peak-/Stressfall;
- ausreichend schnelle Lastregelung bei Radxa/Wi-Fi/USB-Transienten;
- kein hörbarer bzw. funktional relevanter Einfluss auf Analog-Audio und Codec-Clocking.

## ACCESSORY USB-C

Der ACCESSORY-Port bleibt vollständig getrennt vom POWER-Port.

```text
5V_SYS
  │
  ▼
Current-limited / reverse-blocking load switch
  │
  ▼
ACCESSORY USB-C VBUS ~5 V / 1 A target
```

Anforderungen:

- DFP/Host-Rolle;
- definierte Strombegrenzung;
- Over-Current-Erkennung;
- Reverse-Current-Schutz;
- ESD-Schutz;
- kontrolliertes Ein-/Ausschalten durch Device Agent/Power Manager;
- USB-Accessory-Fehler darf nicht die 5V_SYS-Schiene kollabieren lassen;
- Strom-/Fehlerdiagnose soll nach Möglichkeit softwareseitig sichtbar sein.

Der 5-W-Accessory-Budgetfall ist eine Designreserve, keine Laufzeitannahme für Standardbetrieb.

## Betrieb ohne Akku

**REQUIREMENT:** Bei ausreichend leistungsfähiger externer USB-C-Versorgung muss das Beltpack auch mit entnommenem Battery Pack starten und laufen können.

Prototype 1 muss deshalb den gesamten Startpfad ohne Akku prüfen:

`USB-C attach → PD/fallback → Charger/Power Path → SYS_BAT → 5V_SYS → Radxa boot`.

Dies ist für Service, stationären Dauerbetrieb und Diagnose wertvoll und verhindert, dass ein verschlissener/entnommener Akku das Gerät unnötig unbrauchbar macht.

## Verhalten schwacher Netzteile

Das Produkt darf ein unterdimensioniertes Netzteil nicht mit Boot-Loops oder instabiler Audiofunktion beantworten.

Priorität:

1. aktive Systemlast versorgen;
2. stabile 5V_SYS erhalten;
3. Accessory-Port innerhalb Policy versorgen;
4. erst verbleibende Leistung zum Laden verwenden.

Wenn die Eingangsleistung nicht reicht, reduziert der Power Manager den Ladestrom. Bei Bedarf pausiert Laden vollständig. Falls ein Akku eingesetzt ist, darf Battery Supplement kurzfristig unterstützen.

Eine spätere UI kann verständlich zwischen `External power`, `Charging`, `Slow charging / limited source` und `Battery supplement` unterscheiden, ohne dem Nutzer elektrische Details aufzuzwingen.

## Power-Off und Hardware-Grenze

Die Power-Architektur muss zur bestehenden UX passen:

- normaler POWER-Hold → Linux erhält Shutdown-Anforderung und fährt sauber herunter;
- nach bestätigtem Shutdown wird die Haupt-5-V-Schiene deaktiviert;
- langer Hardware-Hold (bestehendes Ziel ≥8 s) muss die Hauptversorgung unabhängig von Linux sicher abschalten können;
- Akkuentnahme darf jederzeit zu abruptem Power Loss führen und ist bereits als zulässiger Fall definiert.

**REVIEW:** Der konkrete Power-Button-/Latch-/Load-Switch-Baustein wird im Schaltplan festgelegt. Wichtig ist die Hardware-Eigenschaft, nicht ein bestimmter IC.

## Vorläufige Kosten

Öffentliche 1k-Preisanker zeigen derzeit ungefähr:

- BQ25798: ~2,6 EUR;
- TPS61088: ~1,3 EUR;
- PD-Sink-Controller-Klasse: grob ~1–2 EUR als früher öffentlicher Anker; TPS25730A benötigt aktuellen Serien-RFQ;
- zusätzlich Magnetics, USB-C-Schutz, Load Switches, Strommessung, Passives und ggf. lokale Regler.

Damit erscheint eine leistungsfähige 1S+PD-Architektur **weiterhin grundsätzlich innerhalb des 8–11-EUR-Power+USB-Budgets möglich**, aber nur bei disziplinierter Auswahl und ohne unnötige doppelte Funktionen.

## Was bewusst nicht gebaut wird

- kein eigener Battery Pack / kein eigenes Pack-BMS;
- kein eigener Zellschutz und kein eigenes Zell-Balancing;
- kein Umgehen packinterner Schutzfunktionen;
- kein Hot-Swap-Energiespeicher;
- kein USB-PD Source am POWER-Port;
- keine Datenfunktion am POWER-Port;
- keine universelle 1S/2S-Schaltung nur für theoretische Flexibilität;
- keine zweite 5-V-Hauptversorgung nur für ACCESSORY, wenn ein kontrollierter Abzweig von 5V_SYS ausreicht;
- keine proprietäre Netzteil- oder Akku-Kopplung.

## Prototype-1-Power-Gate

Die 1S-Architektur darf erst Richtung Serie fortgeführt werden, wenn mindestens folgende Versuche bestanden sind:

1. Boot und Dauerbetrieb mit Akku, ohne externe Versorgung;
2. Boot und Dauerbetrieb ohne Akku an externer Versorgung;
3. Umschalten externe Versorgung ↔ Akku ohne unerwünschten Reset, solange der Akku eingesetzt bleibt;
4. 5-V-Fallback mit mehreren realen USB-C-Netzteilen;
5. PD-Betrieb mit 9-V-Profil bzw. final gewähltem Profil;
6. gleichzeitiger Systembetrieb + Laden;
7. Verhalten bei 5 V / 1,5 A und anderen begrenzten Quellen;
8. Wirkungsgrad bei 3,2 / 3,8 / 5,5 / 8 / 13 W;
9. 5V_SYS-Regulation und Transienten;
10. ACCESSORY USB 0 / 0,5 / 1,0 A einschließlich Kurzschluss-/OCP-Test;
11. Low-SoC-Lasttest;
12. Thermik von Charger, Boost, Induktivitäten, Connectoren und PCB;
13. Audio-Noise/EMI bei Laden, Boost, PD und USB-Last;
14. Hard-Off unabhängig vom Linux-Zustand;
15. Akkuentnahme und anschließender definierter Neustart;
16. Nachweis, dass alle Lade-/Entlade-/Temperaturgrenzen des ausgewählten Serienpacks eingehalten werden und packinterne Schutzfunktionen wirksam bleiben.

## Aktuelle Richtung

**CANDIDATE / PREFERRED FOR PROTOTYPE 1:**

```text
USB-C POWER Sink with PD + 5V fallback
        ↓
wide-input buck-boost charger / NVDC power path
        ↔ 1S production battery pack with own BMS/protection
        ↓
dedicated synchronous 5V boost
        ↓
5V_SYS
        ├─ Compute
        └─ protected 5V/1A ACCESSORY USB host
```

Der wichtigste neue Architekturpunkt ist damit:

> **USB-PD ist für das Beltpack kein Ladegeschwindigkeits-Gimmick. Es schafft Leistungsreserve für gleichzeitigen Vollbetrieb und Laden, während 5-V-USB-C als kompatibler Fallback erhalten bleibt.**

Und die Batterie-Verantwortungsgrenze bleibt unabhängig von der konkreten Power-IC-Auswahl unverändert:

> **Der Battery Pack verantwortet Batteriesicherheit und Zellmanagement. Der Carrier verantwortet Systemstrom und spezifikationskonforme Ladeintegration.**
