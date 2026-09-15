# Compute-Plattformen und Serienkonfiguration

**Deutsch (kanonisch)** | [English](../../en/20-hardware/compute-module.md)

## Zweck

Dieses Dokument beschreibt die stabile Hardwaregrenze zwischen nıu-Product-Core und austauschbarer Compute-Hardware. Die konkrete Serienplattform ist noch offen; aktiv verglichen werden zwei Plattformfamilien.

## Architektur

**DECIDED:** Compute ist nicht der Device-Identity-Anker. Der nıu-Carrier trägt Device Identity, Secure Element, Audio, Power, HMI, Resilience-RF und produktspezifische Hardware. Compute bleibt austauschbare Rechen-, Storage- und Netzwerkhardware.

**DECIDED:** Für die Serienbewertung existieren zwei aktive Compute-/Carrier-Familien:

```text
nıu Product Core
        │
        ├── CM-Carrier
        │   ├── Radxa CM3
        │   ├── Radxa CM4
        │   └── Raspberry Pi CM4
        │
        └── Zero-Carrier
            ├── Radxa ZERO 3W
            └── Raspberry Pi Zero 2 W
```

Noch **nicht entschieden** ist, welche Familie und welches konkrete Standardmodul die Serie gewinnt.

## Standard-SKU-Regel

**DECIDED:** Die Serienarchitektur basiert ausschließlich auf regulären, unveränderten Standard-SKUs.

Ausgeschlossen als notwendige Serienvoraussetzung sind:

- kundenspezifische Compute-Module;
- Hersteller-Sondervarianten nur für nıu;
- Widerstands-/Löt-Rework am gekauften SBC;
- Compute-spezifische Änderungen, die Reparierbarkeit und freie Beschaffung unterlaufen.

## CM-Plattform

Kandidaten:

- Radxa CM3;
- Radxa CM4;
- Raspberry Pi CM4.

**TARGET:** Ein identisch bestückter CM-Carrier soll alle drei Module über die verifizierte sichere 2×100-Pin-Schnittmenge aufnehmen können.

Regeln:

- nur in F-015 verifizierte gemeinsame Pins für Pflichtfunktionen verwenden;
- der dritte Radxa-Connector trägt keine Pflichtfunktion der nıu-Baseline;
- compute-spezifische BSPs, Device Trees und Recovery-Abläufe sind zulässig;
- compute-spezifische Carrier-Bestückungsvarianten sollen vermieden werden.

Radxa CM3 besitzt eine schriftliche Herstellerzusage zur Verfügbarkeit bis mindestens September 2033. Raspberry Pi CM4 ist bis mindestens Januar 2034 angekündigt. Lifecycle allein entscheidet daher derzeit nicht zwischen diesen beiden Kandidaten.

## Zero-Plattform

Kandidaten:

- Radxa ZERO 3W;
- Raspberry Pi Zero 2 W.

Beide gehören zur 65×30-mm-Zero-Klasse mit 40-Pin-Erweiterung.

**DOCUMENTED / VALIDATION PENDING:** F-029 hat alle 40 physischen Header-Positionen 1:1 verglichen und auf der Low-Speed-Ebene **keine harte elektrische Kollision** gefunden. Die gemeinsame Basis ist damit deutlich belastbarer als die reine Formfaktor-Annahme:

- 5 V / 3,3 V / GND auf gemeinsamen Positionen;
- User-I²C auf Pins 3/5;
- SPI MOSI/MISO/CLK/CS0 auf 19/21/23/24;
- PCM/I²S BCLK/LRCK/DIN/DOUT auf 12/35/38/40;
- übrige Signalpositionen grundsätzlich als 3,3-V-GPIO nutzbar, aber mit unterschiedlichen Nummern/Alt-Funktionen/Pulls;
- UART 8/10 ist beim ZERO 3W Default-U-Boot-Console und deshalb keine bevorzugte Pflichtschnittstelle;
- Pins 27/28 werden als HAT-ID-I²C oder DNC behandelt;
- Pin 26 bleibt wegen widersprüchlicher Radxa-Dokumentation bis zur Klärung/Bench-Validierung außerhalb der Pflicht-Baseline.

**TARGET:** Ein gemeinsamer Zero-Carrier mit möglichst identischer Bestückung nutzt nur diese konservative, verifizierte Low-Speed-Schnittmenge.

Noch zu validieren:

- mechanische Header-Pitch-/Hole-/Keep-out-Kompatibilität;
- reale 5-V-Power-/Backfeed-Auslegung;
- USB-Interconnect;
- Storage/Recovery;
- Power/Shutdown;
- Bench-Test der gemeinsamen GPIO-/Bus-Schnittmenge;
- reale Carrier-BOM-Gleichheit.

Beim Radxa ZERO 3W darf der USB2-Pfad über 40-Pin nicht als Serienlösung vorausgesetzt werden, weil dafür Board-Rework erforderlich ist. Raspberry Pi Zero 2 W führt USB-OTG regulär über Micro-USB. **USB gehört deshalb ausdrücklich nicht zur gemeinsamen Zero-40-Pin-Baseline.** Die Zero-Plattform benötigt einen Standard-SKU-konformen, board-spezifischen kurzen USB-Interconnect zu einer gemeinsamen Carrier-USB-Topologie.

Der aktuelle Radxa ZERO 3W Product Brief Rev. 1.11 nennt Mindestverfügbarkeit bis **September 2030**. Dies ist von der direkten CM3-Zusage bis mindestens September 2033 zu trennen.

## Storage

### CM

Je nach Standard-SKU ist onboard eMMC verfügbar und für ein langlebiges Linux-Produkt mit A/B-OTA, Recovery und Diagnose grundsätzlich bevorzugt.

### Radxa ZERO 3W

Onboard eMMC ist in Standard-SKUs verfügbar und bleibt der bevorzugte Runtime-Storage-Pfad für diesen Kandidaten.

### Raspberry Pi Zero 2 W

Der Pi Zero 2 W besitzt keinen onboard eMMC und nutzt regulär microSD. Falls er Serienkandidat bleibt, ist dies ein eigenes Architektur-Gate:

- qualifizierte production-grade microSD **oder** alternative externe Storage-Lösung;
- A/B-OTA, Rollback und Recovery;
- Hard-Power-Loss-Toleranz;
- Schreiblast-/Lebensdauerstrategie.

Die bisherige allgemeine Regel „microSD ist kein Serien-Betriebsmedium“ gilt deshalb nicht mehr ungeprüft plattformübergreifend; sie muss für die Pi-Zero-Untervariante evidenzbasiert bestätigt oder geändert werden.

## RAM-/Compute-Regel

Compute wird auf ausreichende Produktreserve, nicht maximale Spezifikation und nicht den niedrigsten Einkaufspreis optimiert.

Zu messen sind mindestens:

1. RAM nach Boot;
2. RAM mit vollständigem Talkkonnect/PipeWire/nıu-Service-Stack;
3. Peak-RAM bei Netzwerkwechsel, Audio, UI, Diagnose und OTA;
4. Storage-Belegung und A/B-/Recovery-Reserve;
5. Boot-/Recovery-Zeit;
6. Idle/Listening/TX/RX/Heavy-Load-Power;
7. Thermik im Zielgehäuse;
8. Hard-Power-Loss und Power Loss während OTA/Config-Write.

Besondere Gates:

- 1-GB-CM-Konfigurationen;
- ZERO 3W 1/2-GB-Abwägung;
- Raspberry Pi Zero 2 W mit **512 MB** RAM.

## Kostenmodell

Es gibt keinen gemeinsamen abstrakten Compute-Stückpreis mehr. Die Serienwirtschaftlichkeit wird je Plattform bis zum gleichen funktionalen Endpunkt gerechnet:

```text
Common Product Core
+
CM-spezifischer Carrier/Interconnect/PCB/PCBA
+
CM-Kandidat
```

gegen

```text
Common Product Core
+
Zero-spezifischer Carrier/Interconnect/PCB/PCBA
+
Zero-Kandidat
```

BOM-Quelle für diese Szenariorechnung ist `product-development/bom/`.

## Entscheidungsregel

> **Zuerst gewinnt die bessere Plattformfamilie; danach gewinnt innerhalb dieser Familie die kleinste Standard-SKU, die Funktion, Reserve, Lifecycle, Reparierbarkeit und Supply-Anforderungen belastbar erfüllt.**

Ein Universal-PCB, das gleichzeitig CM- und Zero-Footprints trägt, ist nicht das Ziel. Ziel sind zwei mögliche Carrier-Varianten mit maximal gemeinsamem Product Core.

## Verknüpfungen

- Product-development Q-002: CM versus Zero platform
- Product-development Q-005 / F-015: CM shared-carrier compatibility
- Product-development Q-007 / F-029: Zero shared-carrier compatibility / full 40-pin audit
- Product-development BOM: Common Core + CM platform + Zero platform
