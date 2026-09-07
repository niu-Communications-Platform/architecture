# Compute-Modul und Serienkonfiguration

**Deutsch (kanonisch)** | [English](../../en/20-hardware/compute-module.md)

## Zweck

Dieses Dokument konkretisiert die Anforderungen an das austauschbare Compute-Modul des Beltpacks und insbesondere die Zielkonfiguration des Radxa ZERO 3W.

## Architektur

**DECIDED:** Das Compute-Modul ist nicht der Device-Identity-Anker. Der Carrier trägt die Device Identity; das Compute-Modul ist austauschbare Rechen-, Storage- und Netzwerkhardware.

**CANDIDATE:** Radxa ZERO 3W auf Basis RK3566 bleibt bevorzugter Serienkandidat. Der Raspberry Pi Zero 2 W/WH bleibt Entwicklungsplattform, ist aber nicht die bevorzugte Serienbasis.

## Offizielle Konfigurationsmöglichkeiten

Radxa dokumentiert für den ZERO 3W aktuell 1/2/4/8 GB LPDDR4 und 0/8/16/32/64 GB onboard eMMC. Der Hersteller nennt eine Mindestverfügbarkeit des ZERO 3W bis September 2033.

## Zielkonfiguration

**CANDIDATE:** Für Prototype 1 und die wirtschaftliche Serienbewertung wird **2 GB LPDDR4 + 16 GB onboard eMMC** als bevorzugte Basiskonfiguration geführt.

Begründung:

- 1 GB RAM könnte für den heutigen Kern-Workload ausreichen, lässt aber wenig Reserve für PipeWire, Talkkonnect/Mumble, Device Agent, Netzwerkmanagement, UI, Diagnostik, OTA/Recovery und künftige Softwareentwicklung;
- 4 GB RAM erscheinen für die bekannte Beltpack-Aufgabe derzeit nicht notwendig und würden Kosten sowie potenziell Leistungsaufnahme ohne klaren Produktnutzen erhöhen;
- 8 GB eMMC sind für ein langlebiges Linux-Produkt mit A/B-System, Recovery, Logs, Diagnostik und Update-Reserve unnötig knapp;
- 16 GB eMMC bieten deutlich mehr Layout-/Update-/Recovery-Reserve, ohne in die für dieses Produkt voraussichtlich unnötige 32-GB-Klasse zu springen;
- zusätzlicher freier Storage reduziert nicht die Pflicht, Schreiblast zu minimieren und Hard-Power-Loss-Toleranz zu validieren.

Die Konfiguration ist **noch keine Serienfreigabe**. Prototype 1 muss die reale RAM-Nutzung, Storage-Belegung, Update-Slots, Boot-/Recovery-Verhalten, Leistungsaufnahme und Thermik messen.

## GPIO-Header

**TARGET:** Für die Serienintegration wird die Variante **ohne vorbestückten 40-Pin-Header** bevorzugt, sofern die mechanische/elektrische Carrier-Anbindung dies zulässt. Ein unnötig bestückter Standardheader kostet Bauraum, Material und Montagehöhe.

Die endgültige Verbindung zwischen ZERO 3W und Carrier muss servicefähig, reproduzierbar und serienmontagegerecht sein. Sie darf nicht allein deshalb den Maker-Header übernehmen, weil dieser im Entwicklungsboard vorhanden ist.

## Storage-Regeln

- onboard eMMC ist der normale Runtime-Storage;
- microSD ist kein Serien-Betriebsmedium;
- microSD darf für Entwicklung/Service genutzt werden, sofern die Mechanik dies sinnvoll erlaubt;
- Device Identity und nicht rekonstruierbare Factory-Daten dürfen nicht ausschließlich auf eMMC liegen;
- A/B-OTA, Rollback und Recovery müssen bei abruptem Power Loss robust bleiben;
- Logs und hochfrequente Runtime-Schreibvorgänge werden begrenzt;
- vor Serienfreigabe wird die eMMC-Ausdauer bzw. die für die konkrete SKU verwendete Storage-Qualität mit Radxa geklärt.

## Cost Gate

Das Compute-Budget beträgt derzeit **18–22 EUR pro Gerät** in der Zielserie.

**REVIEW:** Falls 2 GB + 16 GB eMMC dieses Budget bei realen 1k/5k/10k-Angeboten wesentlich überschreiten, werden nicht automatisch RAM oder Storage reduziert. Zuerst werden Hersteller-/OEM-Konditionen, Konfigurationsalternativen und der reale Nutzen bewertet.

Eine billigere 1-GB/8-GB-Konfiguration ist nur dann sinnvoll, wenn Prototype-Messungen ausreichende Reserven nachweisen und A/B-/Recovery-Anforderungen ohne künstliche Einschränkungen erfüllt werden.

## Prototype-1-Messungen

Für die Compute-Entscheidung werden mindestens erfasst:

1. RAM-Nutzung nach Boot;
2. RAM-Nutzung mit vollständigem Beltpack-Service-Stack;
3. Peak-RAM bei Netzwerkwechsel, Audio, UI, Diagnose und OTA;
4. eMMC-Belegung des Basissystems;
5. Größe beider A/B-Systemslots und Recovery-Reserve;
6. Log-/Persistenzwachstum über repräsentativen Dauerbetrieb;
7. Bootzeit und Recovery-Zeit;
8. Leistungsaufnahme Idle/Listening/TX/RX/Heavy Load;
9. thermisches Verhalten im Zielgehäuse;
10. wiederholter Hard-Power-Loss und Power Loss während OTA/Config-Write.

## Entscheidungsregel

> **Compute wird auf ausreichende Produktreserve, nicht auf maximale Spezifikation und nicht auf den niedrigsten Einkaufspreis optimiert.**

Die kleinste Konfiguration, die den vollständigen Beltpack-Stack, A/B-OTA, Recovery und realistische zukünftige Softwareentwicklung mit belastbarer Reserve trägt, gewinnt.

## Quellen

- Radxa ZERO 3W Produktseite und Dokumentation: https://radxa.com/products/zeros/zero3w/ und https://docs.radxa.com/en/zero/zero3
- Radxa ZERO 3W Product Brief: Herstellerangaben zu SKU-Konfigurationen und Mindestverfügbarkeit bis September 2033.
