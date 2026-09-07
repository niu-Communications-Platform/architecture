# Architekturdokumentation — Deutsch (kanonisch)

**Deutsch** | [English](../en/README.md)

Diese Verzeichnisstruktur ist die **kanonische technische und produktbezogene Dokumentation** der nıu Communications Platform. Die englischen Dokumente werden als gepflegte Übersetzungen geführt; bei Abweichungen gilt die deutsche Fassung.

## Dokumentation

- [`00-Produktprinzipien`](00-product/product-principles.md) — Produktmodell, Leitprinzipien, digitale Souveränität, Offenheit, Open Diagnostics/Open Repair, Capability ≠ Feature und Serienfähigkeit
- [`10-Systemarchitektur`](10-system/system-architecture.md) — Repository-Grenzen, Capability Layer, Device Agent und Architekturphase
- [`20-Hardware`](20-hardware/) — plattformweite Hardwareprinzipien und produktübergreifende Hardwareentscheidungen
  - [`Reparierbarkeit und Nachhaltigkeit`](20-hardware/repairability-sustainability.md) — Reparaturgranularität, Ressourcenschonung sowie offene Fehleranalyse- und Reparaturdokumentation
  - [`Anforderungen an den serienreifen Battery Pack`](20-hardware/battery-pack-requirements.md) — Herstellerpack statt Eigenentwicklung, Austauschbarkeit, Kompaktheit, Betriebsanforderungen und aktuelle VRI-Referenzkandidaten
- `30-software/` — gemeinsame Softwarearchitektur, Dienste und Abstraktionen; derzeit noch ohne eigene Fachseite
- [`40-Audioarchitektur`](40-audio/audio-architecture.md) — Audioendpunkte, Routing, zusätzliche Feeds, TDM-Zielarchitektur und Fallbacks
- [`50-Netzwerkarchitektur`](50-networking/network-architecture.md) — Transportklassen, Network Manager, Health-Modell und Handover
- [`60-Identity- und Trust-Architektur`](60-identity-security/identity-trust-architecture.md) — Geräteidentität, Secure Element, PKI, Trust Domains sowie Grenze zwischen offener Reparatur und offizieller nıu-Attestierung
- [`70-Provisioning, Ownership und Lifecycle`](70-provisioning-lifecycle/provisioning-lifecycle.md) — Enrollment, Zustände, Reset, Ownership und Replace Device
- [`80-Factory- und Fertigungsarchitektur`](80-manufacturing/factory-architecture.md) — Skalierung, Factory Provisioning, EOL und irreversible Operationen
- [`90-UX-/UI-Prinzipien`](90-ux-ui/ux-ui-principles.md) — Bedienlogik, Display, Tasten, Power, LEDs und Diagnose

Produktspezifische Implementierungsdetails gehören in die jeweiligen Produkt-Repositories. Hier werden sie nur dokumentiert, wenn sie eine plattformweite Architekturentscheidung darstellen oder andere Komponenten beeinflussen.
