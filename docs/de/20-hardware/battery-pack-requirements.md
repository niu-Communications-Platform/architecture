# Anforderungen an den serienreifen Battery Pack

**Deutsch (kanonisch)** | [English](../../en/20-hardware/battery-pack-requirements.md)

## Grundsatz

**DECIDED:** nıu entwickelt weder Batteriezellen noch Battery Pack oder dessen internes BMS selbst. Eingesetzt wird ein serienreifer, dokumentierter Pack eines spezialisierten Herstellers. Der Carrier übernimmt nur die erforderliche Systemintegration.

## Produkt- und Mechanikziel

Das Beltpack ist ein professionelles mobiles IP-Intercom-/Audio-Gerät. Die bisher diskutierten ungefähr **120 × 80 × 35 mm sind eine Obergrenze, kein auszufüllender Bauraum**. Das Produkt soll bei Erhalt von Robustheit, Wartbarkeit, Thermik und Bedienbarkeit so kompakt wie sinnvoll werden.

## Rapid field-replaceable battery

**DECIDED:** Der komplette Pack ist nicht nur regulatorisch austauschbar, sondern als **rapid field-replaceable battery** ein bewusstes professionelles Produktmerkmal.

> **Nicht maximale Akkukapazität, sondern maximale Einsatzbereitschaft.**

Ziel ist ein Wechsel in wenigen Sekunden ohne Öffnen des eigentlichen Gerätegehäuses, mit robuster Verriegelung, sicherer Führung, fehlstecksicherer Kontaktierung und Schutz gegen unbeabsichtigtes Lösen. Ersatzpacks und externe Einzel-/Mehrfach-Ladelösungen sollen möglich sein.

### Kein Hot-Swap

**DECIDED:** Unterbrechungsfreier Betrieb während des Akkuwechsels wird nicht unterstützt. Ohne externe Versorgung darf das Gerät beim Entfernen des Packs ausgehen. Sekundenlange Energiepufferung oder ein zweiter Energiespeicher wird dafür nicht vorgesehen. Kleine Hold-up-Kapazitäten für elektrische Stabilität bleiben zulässig.

### Abrupte Akkuentnahme

**DECIDED:** Akkuentnahme ohne vorherigen Software-Shutdown ist ein zulässiger Betriebsfall. Das System muss wiederholten Hard Power Loss tolerieren. Kritische persistente Zustände, Provisioning und A/B-OTA müssen power-loss-sicher sein; unnötige Flash-Schreibvorgänge werden minimiert; Device Identity hängt nicht allein am SBC-Storage. Nach Neustart kehrt das Gerät selbstständig in einen definierten Zustand zurück. Dies wird praktisch wiederholt getestet.

## Kapazitätsfamilie ohne Beltpack-Varianten

**DECIDED:** Die Batterie-Schnittstelle soll nach Möglichkeit mehrere Kapazitätsklassen unterstützen, **ohne unterschiedliche Beltpack-Hardwarevarianten zu erzeugen**. Mehr Kapazität ist eine Akkuoption, keine zweite Beltpack-Variante.

Das Zielbild ist ein einziges Beltpack mit identischer Carrier-, Firmware- und Hauptgehäuse-Architektur. Ein kompakter Standardakku kann im Lieferumfang enthalten sein; ein Akku mit deutlich höherer Kapazität kann als Zubehör angeboten werden, sofern dies ohne relevante zusätzliche Systemkomplexität möglich ist.

Designziele für eine solche Packfamilie:

- gleiche elektrische Host-Schnittstelle und Pinbelegung;
- bevorzugt gleiche Spannungsklasse und gleiche grundlegende Power-Architektur;
- gleiches bzw. kompatibles Kommunikations-/Fuel-Gauge-Modell;
- gleiche mechanische Kontakt- und Verriegelungszone;
- automatische korrekte Behandlung unterschiedlicher Kapazitäten ohne Firmwarevarianten;
- keine andere Carrier-Platine und keine andere Beltpack-SKU nur wegen der Akkukapazität;
- ein größerer Pack darf nach außen stärker auftragen, statt das Hauptgerät für den größten Akku zu dimensionieren;
- **die Unterstützung eines Extended Packs darf die Abmessungen des Beltpacks bei eingesetztem Standardakku nicht unnötig erhöhen.**

**CANDIDATE:** Ein Standardpack um etwa **19 Wh** ist aufgrund seiner Kompaktheit derzeit besonders interessant. Für einen optionalen Extended Pack ist nicht automatisch die nächstgrößere 25-Wh-Klasse optimal. Eine deutlichere Kapazitätssteigerung, beispielsweise ungefähr **30–35 Wh**, kann als Zubehör produktseitig sinnvoller sein, sofern ein Hersteller eine elektrisch und mechanisch kompatible Lösung anbietet.

Die konkreten Kapazitäten sind **nicht entschieden**. Insbesondere wird keine universelle 1S/2S-Unterstützung allein für mehrere Akkuoptionen vorgesehen. Wenn unterschiedliche Kapazitäten zusätzliche Wandler, verschiedene Beltpack-Gehäuse, zusätzliche Firmwarepfade oder sonstige relevante Komplexität erfordern, ist ein einzelner optimaler Pack einer Packfamilie vorzuziehen.

## Pack-Anforderungen

Der Serienpack soll insbesondere integrierte Schutz-/BMS-Funktionen, Temperaturüberwachung, dokumentierte Lade-/Entladegrenzen, ausreichende Dauer-/Spitzenstromfähigkeit, dokumentierte Kommunikation soweit sinnvoll, Fuel-Gauge-Daten, robuste fehlstecksichere Kontakte mit geeigneter Steckzyklenzahl sowie vollständige Integrations-, Konformitäts- und Lifecycle-Dokumentation bieten. Es gibt keine künstliche Software-Paarung oder proprietäre Batteriearchitektur allein zur Kundenbindung. Nach Packwechsel werden batteriespezifische Health-/Learning-Daten korrekt neu aufgebaut.

## Betrieb und Power-Architektur

Das Beltpack unterstützt mobilen sowie dauerhaften Betrieb an externer Stromversorgung. Power-Path/Load-Sharing, Ladeverhalten, Battery Care, Vermeidung von Mikrozyklen, thermische Grenzen und Packwechselverhalten werden mit dem Hersteller abgestimmt. Pack-BMS und Carrier-System-Power haben klare Verantwortungsgrenzen.

## Laufzeit und Leistungsbudget

Die endgültige Mindestenergie ist noch nicht festgelegt. Durch den schnellen Feldwechsel muss ein einzelner Pack nicht zwingend eine maximale Schichtdauer abdecken. Die Auswahl basiert auf dem Power Budget und anschließend auf Prototypmessungen.

Aktuell ist etwa **19 Wh** als kompakte Standardklasse interessant. 25 Wh bleibt Vergleichspunkt. Parallel soll eine deutlich größere, aber schnittstellenkompatible Extended-Klasse untersucht werden.

## Referenzkandidat: vri BASE LINE

**CANDIDATE:** Die vri BASE LINE der VRI GmbH Batterie-Technik in Ellwangen ist bevorzugter Referenzkandidat. Besonders interessant sind aktuell der 1S/21700 88054 201 512 (~19,1 Wh) und als Vergleich der 2S/18650 88030 502 512 (~25,2 Wh). Die endgültige Auswahl berücksichtigt Wandlerwirkungsgrad, Lastprofil, Laufzeit, USB-Host-Reserve, Thermik, Gewicht, Bauraum, Wartbarkeit und Feldwechsel.

## Hersteller-Gespräch

Neben 1S/2S, Lastprofil, BMS-/Carrier-Verantwortung, Laden, Battery Care, Fuel Gauge, Steckzyklen, Konformität, Lifecycle, Mustern und externem Laden soll VRI ausdrücklich prüfen:

1. Ist eine Packfamilie mit einem kompakten Standardpack um etwa 19 Wh und einem deutlich größeren Extended Pack auf derselben elektrischen Host-Schnittstelle möglich?
2. Können Spannungsklasse, Pinbelegung und Kommunikationsschnittstelle gleich bleiben?
3. Kann dieselbe mechanische Kontakt-/Verriegelungszone verwendet werden, sodass der größere Pack lediglich stärker aufträgt bzw. einen größeren Batterierücken bildet?
4. Welche vorhandene BASE-LINE- oder abgeleitete Lösung läge für eine Extended-Klasse um ungefähr 30–35 Wh nahe?
5. Welche Auswirkungen hätte eine solche Packfamilie auf Zertifizierung, MOQ, Lifecycle, Ladegeräte und Ersatzteilhaltung?

## Entscheidungsregel

Der bevorzugte Standardpack ist der kleinste serienreife Pack, der mit ausreichender Reserve die realen Anforderungen erfüllt. Eine Packfamilie aus Standard- und Extended-Kapazität wird nur verfolgt, wenn sie **keine relevante zusätzliche Komplexität im Beltpack** erzeugt.

> **Battery capacity is a requirement, not a design goal. Product size, serviceability and reliable runtime are optimized together.**
