# Produktprinzipien

**Deutsch (kanonisch)** | [English](../../en/00-product/product-principles.md)

## Produktmodell

Die nıu Communications Platform umfasst mehrere Betriebsmodelle:

- **Bare:** Intercom-Endgerät; Mumble/Murmur-Infrastruktur wird vom Nutzer bereitgestellt.
- **Base:** Intercom plus lokal betriebene Mumble/Murmur- und Management-Infrastruktur.
- **Cloud:** Intercom plus von nıu gehostete Mumble/Murmur- und Management-Infrastruktur.

Die Produktvarianten sollen soweit sinnvoll dieselben Geräte-, Provisioning- und Protokollgrundlagen verwenden. Unterschiede liegen primär in der Provisioning Authority, dem Trust Domain und dem Ort der Service-Infrastruktur.

## Leitprinzipien

### Nutzerkomfort

Komplexität wird im Produkt absorbiert und nicht an den Nutzer weitergegeben. Der Normalbetrieb soll kuratiert, verständlich und robust sein.

### Apple-Komfort und Entwicklerfreiheit

Es existieren drei Ebenen:

1. **Produktebene:** getestete und supportbare Standardfunktionen.
2. **Provisioning-Ebene:** Administratorprofile konfigurieren komplexere Fähigkeiten abstrahiert.
3. **Developer-Ebene:** Quellcode, Konfiguration und APIs dürfen die zugrunde liegenden Fähigkeiten freier nutzen.

**Capability ≠ Feature.** Eine technische Fähigkeit wird erst offizielles Feature, wenn sie verständlich, robust, testbar und supportbar ist.

### Offenheit

Die Plattform soll vollständig Open Source und reproduzierbar baubar sein, soweit Dritt-Lizenzen dies zulassen. Offenheit der Implementierung bedeutet nicht Offenlegung privater Trust-Schlüssel und nicht das Recht, sich als offizieller nıu-Dienst auszugeben.

### Digitale Souveränität umfasst die Hardware

Digitale Souveränität endet nicht beim Zugriff auf den Quellcode oder beim Self-Hosting. Der Eigentümer soll das Produkt verstehen, diagnostizieren, reparieren, wiederherstellen und mit eigener Software oder eigenen Trust Domains weiterbetreiben können.

Daraus folgt als Produktziel:

**Open Source → Open Hardware → Open Diagnostics → Open Repair Documentation → Open Understanding.**

nıu veröffentlicht deshalb soweit technisch und lizenzrechtlich möglich die Informationen und Werkzeuge, die eine qualifizierte unabhängige Fehleranalyse und Reparatur ermöglichen. Dazu gehören insbesondere Hardware- und Schnittstelleninformationen, Diagnoseverfahren, Reparaturanleitungen, relevante Testpunkte und Sollwerte, Kalibrierungs- und Recovery-Verfahren sowie offene Diagnosetools.

#### Open Understanding

Offene Schaltpläne und Stücklisten allein machen ein Produkt noch nicht verständlich. Die Dokumentation soll deshalb nicht nur offenlegen, **wie** das Beltpack aufgebaut ist, sondern auch erklären, **was die Baugruppen und wesentlichen Bauteile tun, warum sie benötigt werden und warum die Architektur so gewählt wurde**.

Dafür sind langfristig zwei komplementäre Dokumentationsebenen vorgesehen:

1. **Engineering & Repair Reference** – präzise technische Referenz für Elektroingenieure, professionelle Reparaturbetriebe und erfahrene Maker. Dazu gehören Schaltpläne, Stücklisten mit MPNs, Pinouts, PCB-/Signalinformationen, Testpunkte und Sollwerte, Mess- und Diagnoseverfahren, Explosionszeichnungen, Kalibrierung, Austausch- und Recovery-Prozeduren sowie relevante Factory-Tests.
2. **Inside nıu.cp** – didaktische, visuelle Dokumentation für technisch interessierte Nutzer, motivierte Amateure und Maker. Sie erklärt anhand des realen Produkts grundlegende Konzepte und verfolgt Signal-, Energie-, Daten- und Trust-Pfade durch das Gerät. Fachbegriffe werden erklärt, nicht vermieden.

`Inside nıu.cp` soll keine technisch falsche „vereinfachte Version“ der Engineering-Dokumentation sein. Ziel ist dieselbe technische Wahrheit auf einer anderen didaktischen Ebene: vom Produktnutzen über das Architekturverständnis bis zum konkreten Engineering-Detail.

Beispielthemen sind:

- Wie wird die Stimme vom Mikrofon zu digitalen Daten und wieder zurück?
- Was ist ein Audio-Codec und warum verwendet das Gerät mehrere Audiowege?
- Wie entstehen aus einer schwankenden Akkuspannung stabile Systemspannungen?
- Wie handeln USB-C und USB Power Delivery die Energieversorgung aus?
- Wie kommunizieren Chips über I²C, SPI und I²S/TDM?
- Wie gelangen Audio-Daten durch Linux, Talkkonnect, Mumble und das Netzwerk zur Gegenstelle?
- Warum existieren ESD-Schutz, Secure Element, Watchdogs, A/B-Updates und Hardware-Hard-Off?
- Welche Aufgabe hat ein scheinbar unscheinbares einzelnes Bauteil und welche Fehler verhindert es?

Die Dokumentation darf dabei ausdrücklich Neugier und Begeisterung erzeugen. Das Beltpack soll nicht als versiegelte Blackbox verstanden werden, sondern als hochwertiges Consumerprodukt, dessen Funktionsweise nachvollziehbar ist.

**Nicht jedes offene Hardwaredesign ist sinnvoll von Hand bestückbar.** Feine SMT-Packages, mehrlagige Leiterplatten, Hochgeschwindigkeits-, HF-, USB-C/PD- und rauscharme Audioanforderungen können professionelle Bestückung erforderlich machen. Open Understanding verspricht deshalb nicht, dass jeder Nutzer die komplette Carrier-PCB mit Lötkolben aufbauen kann. Wo Reparaturen, Module oder Baugruppen maker-tauglich sind, sollen sie jedoch entsprechend dokumentiert werden.

Grundsatz:

> **Open Hardware bedeutet nicht nur: Du darfst hineinsehen. Open Understanding bedeutet: Wir helfen Dir zu verstehen, was Du dort siehst.**

Die Offenheit von Diagnose und Reparatur wird strikt von der offiziellen nıu Trust Domain getrennt:

> **Diagnostics are open. Trust issuance is not.**

Eine Reparatur oder Modifikation durch den Eigentümer oder einen unabhängigen Reparaturbetrieb beendet nicht allein deshalb den offiziellen nıu-Trust-Status. Solange die bestehende kryptographische Geräteidentität weiterhin zuverlässig beweisbar ist, bleibt sie grundsätzlich erhalten. Ist der Identity Anchor nicht mehr zuverlässig beweisbar oder muss er ersetzt werden, ist für die erneute Aufnahme bzw. Bestätigung innerhalb der offiziellen nıu Trust Domain ein kontrollierter nıu-Rezertifizierungsprozess erforderlich.

### Zukunftsfähigkeit ohne Feature Stuffing

Günstige Hardware-Reserven werden vorgesehen, wenn sie spätere Sackgassen vermeiden. Nicht jede Reserve wird sofort als Produktfeature implementiert.

### Serienfähigkeit

Hardwareentscheidungen werden daran gemessen, ob ein Auftragsfertiger das Gerät tausend- bis zehntausendfach reproduzierbar bauen, programmieren und automatisiert testen kann.
