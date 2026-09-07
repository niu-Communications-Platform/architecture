# Identity- und Trust-Architektur

**Deutsch (kanonisch)** | [English](../../en/60-identity-security/identity-trust-architecture.md)

## Vier Identitäten

1. **Factory/Device Identity** — physisches Beltpack, unveränderlich und Carrier-gebunden.
2. **Friendly/Provisioned Identity** — menschlicher Name, Rolle und Profile; veränderbar/übertragbar.
3. **Mumble/Intercom Identity** — Service-Identität und Zertifikate; getrennt und rotierbar.
4. **Network/Service Identity** — Hostname, IP, MAC und aktueller Transport; flüchtig.

**DECIDED:** Factory Identity lebt auf dem Carrier, nicht auf SD/eMMC oder SBC.

## Carrier Identity

Der Carrier enthält bzw. bindet:

- Device UUID
- sichtbare Seriennummer
- Secure Element
- Carrier-NVM

SBC-/Storage-Tausch erhält die physische Geräteidentität. Carrier-Tausch erzeugt ein neues physisches Gerät. Friendly Identity und Profile können im RMA-Prozess auf ein Ersatzgerät übertragen werden.

### Minimale persistente Identifikatoren

**DECIDED:** Eine neue persistente ID wird nur eingeführt, wenn sie eine eigenständige semantische Frage beantwortet, die keine bestehende ID oder ohnehin erforderliche Eigenschaft beantworten kann.

Für die Factory/Device Identity werden auf Produktebene drei unterschiedliche Größen benötigt:

- **Device UUID — who:** dauerhafte maschinenlesbare Identität des physischen Geräts.
- **Serial Number — human reference:** menschenlesbare Gerätekennung für Produktlabel, Support, Service und Dokumentation.
- **Device Root Key — proof:** kryptographischer Nachweis der behaupteten Device Identity; der private Schlüssel verbleibt im Secure Element.

Diese Größen sind nicht austauschbar und speichern nicht lediglich dieselbe Information mehrfach. Hardware Revision, Variant, Manufacturing Data, Calibration Data, MAC-Adressen, Secure-Element-Seriennummern und gegebenenfalls vorhandene NVM-Chip-UIDs sind Eigenschaften oder technische Diagnosewerte, aber keine zusätzlichen Device Identities.

**DECIDED:** Eine separate `Carrier Physical ID` wird derzeit nicht eingeführt. Sie würde im aktuellen Modell keine ausreichend eigenständige Funktion erfüllen und insbesondere keinen zusätzlichen kryptographischen Identitätsnachweis liefern.

Die bestehende Serial Number soll sinnvollerweise zusätzlich zum äußeren Produktlabel dauerhaft auf dem Carrier angebracht werden. Dadurch steht bei einer physischen Reparatur dieselbe bereits erforderliche Information auch direkt am identitätstragenden Bauteil zur Verfügung, ohne einen weiteren Identifier und eine weitere Registry-Zuordnung einzuführen.

Eine technisch ohnehin vorhandene UID eines EEPROMs/NVMs oder Secure Elements darf als Diagnose- oder Fertigungsattribut erfasst werden. Sie wird nicht allein deshalb Bestandteil des Device-Identity-Modells. Falls die spätere Fertigung eine eigenständige PCB-/Panel-Serialisierung für Traceability tatsächlich benötigt, wird diese aufgrund dieses konkreten Fertigungszwecks eingeführt und nicht vorsorglich als Security Anchor.

## Secure Element

**CANDIDATE:** Microchip ATECC608C-TFLXTLS / TrustFLEX.

Getrennte Schlüsselrollen sind vorgesehen für Device Root, Mumble/Service und Cloud/Auth. Private Schlüssel verlassen das Secure Element nicht.

Software abstrahiert Schlüsselzugriff über einen `KeyProvider`, mit Datei-Provider für Entwicklung und Hardware-Provider für Produktion.

## PKI

Device PKI, Service PKI und Firmware Signing sind strikt getrennte Trust-Bereiche.

- Device Issuing CA → langfristige Device Certificates
- Base lokale Mumble CA → lokaler Trust Domain
- Cloud Service/Mumble CA → gehosteter Trust Domain
- Firmware Signing → eigene Signaturkette

Service-Keys werden bei Enrollment erzeugt und sind rotierbar.

## Open Source und Trust Domains

**DECIDED:** Open Source gewährt Implementierungsfreiheit, aber nicht nıu-Identität oder nıu-Vertrauen.

Dritte dürfen eigene Base-/Cloud-Systeme mit eigenen Trust Roots betreiben. Ein alternatives Backend wird nur akzeptiert, wenn der Owner dessen Provisioning-/Service-Trust ausdrücklich autorisiert.

Das allgemeine Modell lautet:

`Device UUID → Owner → Deployment → Provisioning Authority → Trust Domain`

Eine höhere Provisioning-Revision ersetzt niemals fehlendes Vertrauen in den Signer.

## Offene Reparatur und offizielle nıu-Attestierung

**DECIDED:** nıu reglementiert nicht, was ein Eigentümer technisch mit seinem Gerät tun darf. Die Sicherheitsgrenze liegt bei der Frage, was die offizielle nıu Trust Domain kryptographisch attestiert.

Öffnen, diagnostizieren, reparieren, reimagen, eigene Software installieren und eigene Trust Roots oder Dienste verwenden sollen grundsätzlich möglich und dokumentierbar sein. Physischer Zugriff oder Kenntnis der offenen Implementierung berechtigen jedoch nicht zur Ausstellung oder Erneuerung offizieller nıu Device Certificates, zur Änderung der Factory Registry oder zur Erzeugung anderer nıu-Attestierungen.

Grundsatz:

> **Anyone may repair or modify the device. Only nıu may attest that a device belongs to the official nıu trust domain.**

Eine unabhängige Reparatur beendet den bestehenden Trust-Status nicht automatisch. Solange der bestehende Identity Anchor intakt ist und die Device Identity weiterhin kryptographisch zuverlässig beweisbar bleibt, besteht kein allein aus der Reparatur abgeleiteter Grund für eine neue Attestierung.

Kann der Identity Anchor nicht mehr zuverlässig bewiesen werden oder muss er ersetzt werden, wird die Wiederherstellung des offiziellen nıu-Trust-Status zu einer Identity-Recovery-/Rezertifizierungsoperation. Für die erste Produktgeneration ist vorgesehen, dass das physische Gerät hierfür an nıu als Hersteller eingesandt wird. nıu prüft Gerät und Identitätszuordnung, führt die erforderlichen Factory-/EOL- und Sicherheitsprüfungen durch und kann anschließend eine neue offizielle Attestierung ausstellen bzw. die Registry kontrolliert aktualisieren.

Die konkrete Semantik beim Austausch eines Secure Elements — insbesondere Beibehaltung oder Änderung von Device UUID, Root Key und einer möglichen Identity Epoch — wird separat entschieden und ist derzeit noch offen.

**DECIDED:** Für seltene Mehrfachausfälle wird keine zusätzliche persistente Hardware-ID allein mit dem Ziel eingeführt, die bisherige Device UUID unter allen Umständen retten zu können. Sind beispielsweise Secure Element und Carrier-NVM gleichzeitig ausgefallen, können Seriennummer, permanente Carrier-Markierung, Factory-/Manufacturing-Daten, Kalibrierungsdaten und Reparaturhistorie als forensische Evidenz dienen. Reicht die Zuordnung nicht mit ausreichender Sicherheit aus, wird die alte Device UUID nicht neu attestiert; stattdessen erhält das Gerät eine neue Device Identity und kann über den Replace-Device-Prozess wieder dem gewünschten Deployment zugeordnet werden.

Der Verlust oder Verzicht auf offiziellen nıu-Trust verhindert nicht den weiteren Betrieb des Eigentümers mit eigener Software, eigener PKI oder eigener Trust Domain.
