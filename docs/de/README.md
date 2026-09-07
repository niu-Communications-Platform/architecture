# Architekturdokumentation — Deutsch (kanonisch)

Diese Verzeichnisstruktur ist die kanonische technische und produktbezogene Dokumentation der nıu Communications Platform.

## Struktur

- `00-product/` — Produktvision, Philosophie, Varianten und Grundprinzipien
- `10-system/` — Gesamtsystem, Komponenten, Grenzen und gemeinsame Modelle
- `20-hardware/` — plattformweite Hardwareprinzipien und produktübergreifende Hardwareentscheidungen
- `30-software/` — gemeinsame Softwarearchitektur, Dienste und Abstraktionen
- `40-audio/` — Audioarchitektur, Routing- und Endpoint-Modelle
- `50-networking/` — Transport-, Failover- und Netzwerkarchitektur
- `60-identity-security/` — Identität, PKI, Trust Domains, Secure Element, Secure/Verified Boot
- `70-provisioning-lifecycle/` — Enrollment, Provisioning, Ownership, RMA und Gerätelebenszyklus
- `80-manufacturing/` — Factory Architecture, EOL, Fertigungsidentität und Skalierungsprinzipien
- `90-ux-ui/` — produktübergreifende UX-/UI-Prinzipien und Capability-Layer

Produktspezifische Implementierungsdetails gehören in die jeweiligen Produkt-Repositories. Hier werden sie nur dokumentiert, wenn sie eine plattformweite Architekturentscheidung darstellen oder andere Komponenten beeinflussen.
