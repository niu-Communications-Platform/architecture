# Architecture Decision Records (ADR) — Deutsch

**Deutsch** | [English](../en/README.md)

Die ADRs dokumentieren einzelne Architekturentscheidungen und vor allem deren Begründung. Die **deutsche Fassung ist kanonisch**.

## Inhaltsverzeichnis

- [`ADR-0001:` Der Carrier ist der Anker der physischen Geräteidentität](0001-carrier-is-device-identity-anchor.md)
- [`ADR-0002:` Netzwerk-Handover trennt Transport- und Mumble-Sessionwechsel](0002-network-handover-session-model.md)
- [`ADR-0003:` Open Source und Trust Domain sind getrennt](0003-open-source-trust-domains.md)
- [`ADR-0004:` Mumble als natives Echtzeit-Sprachprotokoll, SIP als Interoperabilitätsschicht](0004-mumble-native-sip-interoperability.md)
- [`ADR-0005:` Der Akku ist durch den Endnutzer austauschbar](0005-end-user-replaceable-battery.md)
- [`ADR-0006:` Murmur Virtual Server bilden die Cloud-Mandantengrenze](0006-cloud-tenant-boundary-murmur-virtual-server.md)

## Schema

```text
ADR-XXXX: Titel
Status: Proposed | Accepted | Superseded | Rejected
Datum: YYYY-MM-DD

Kontext
Entscheidung
Begründung
Konsequenzen
Abhängigkeiten
Validierungsbedarf
Ersetzt / ersetzt durch
```

Eine akzeptierte Entscheidung darf später geändert werden. Die Historie wird dabei nicht überschrieben: Eine neue ADR ersetzt die alte ausdrücklich.
