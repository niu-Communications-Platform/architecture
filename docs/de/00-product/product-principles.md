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

**Open Source → Open Hardware → Open Diagnostics → Open Repair Documentation.**

nıu veröffentlicht deshalb soweit technisch und lizenzrechtlich möglich die Informationen und Werkzeuge, die eine qualifizierte unabhängige Fehleranalyse und Reparatur ermöglichen. Dazu gehören insbesondere Hardware- und Schnittstelleninformationen, Diagnoseverfahren, Reparaturanleitungen, relevante Testpunkte und Sollwerte, Kalibrierungs- und Recovery-Verfahren sowie offene Diagnosetools.

Die Offenheit von Diagnose und Reparatur wird strikt von der offiziellen nıu Trust Domain getrennt:

> **Diagnostics are open. Trust issuance is not.**

Eine Reparatur oder Modifikation durch den Eigentümer oder einen unabhängigen Reparaturbetrieb beendet nicht allein deshalb den offiziellen nıu-Trust-Status. Solange die bestehende kryptographische Geräteidentität weiterhin zuverlässig beweisbar ist, bleibt sie grundsätzlich erhalten. Ist der Identity Anchor nicht mehr zuverlässig beweisbar oder muss er ersetzt werden, ist für die erneute Aufnahme bzw. Bestätigung innerhalb der offiziellen nıu Trust Domain ein kontrollierter nıu-Rezertifizierungsprozess erforderlich.

### Zukunftsfähigkeit ohne Feature Stuffing

Günstige Hardware-Reserven werden vorgesehen, wenn sie spätere Sackgassen vermeiden. Nicht jede Reserve wird sofort als Produktfeature implementiert.

### Serienfähigkeit

Hardwareentscheidungen werden daran gemessen, ob ein Auftragsfertiger das Gerät tausend- bis zehntausendfach reproduzierbar bauen, programmieren und automatisiert testen kann.
