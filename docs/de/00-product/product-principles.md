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

### Zukunftsfähigkeit ohne Feature Stuffing

Günstige Hardware-Reserven werden vorgesehen, wenn sie spätere Sackgassen vermeiden. Nicht jede Reserve wird sofort als Produktfeature implementiert.

### Serienfähigkeit

Hardwareentscheidungen werden daran gemessen, ob ein Auftragsfertiger das Gerät tausend- bis zehntausendfach reproduzierbar bauen, programmieren und automatisiert testen kann.
