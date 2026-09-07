---
language: de
canonical: true
status: current
last_reviewed: 2026-09-07
---

# Factory- und Fertigungsarchitektur

## Skalierungsziel

Das Produkt wird von Anfang an so entworfen, dass ein Auftragsfertiger vier- bis fünfstellige Stückzahlen reproduzierbar komplett fertigen, programmieren, testen und verpacken kann.

Leitfrage: Kann ein Fabrikmitarbeiter das Gerät 10.000-mal ohne Interpretation korrekt bauen und kann eine Teststation anschließend automatisiert feststellen, ob es funktioniert?

## Factory Provisioning

Zielreihenfolge:

1. PCB Assembly
2. elektrisches Bring-up
3. temporärer Manufacturing Candidate Record
4. vollständiger EOL-Test vor Identitätsvergabe
5. atomare Reservierung Seriennummer + UUID im Factory Registry
6. Schreiben und Readback/CRC der Carrier-NVM
7. Device Root Key im Secure Element erzeugen
8. Device Certificate ausstellen
9. Factory Registry vervollständigen
10. keine Serviceidentitäten erzeugen
11. QR/Label erzeugen
12. QR = EEPROM = Registry = Public-Key-Bindung cross-checken
13. erst dann irreversible Slot Locks/Security-Finalisierung
14. Hardware-Secure-Boot/OTP nur nach separater Recovery-Validierung
15. finaler Zustand `UNCLAIMED`

**DECIDED:** Nothing irreversible before complete cross-verification.

## Fertigungsdesign

Seriendesign berücksichtigt:

- montagefreundliche Konstruktion
- minimale Handarbeit
- definierte Steckverbinder
- Testpunkte
- Factory-Test-Modus
- Seriennummer/QR
- Hardware-/Software-Revisionen
- automatisierten EOL-Test
- reproduzierbare Antennenposition
- kontrollierte BOM/Substitutionen
- skalierbares Provisioning, OTA und Diagnose

## Operation Classes

- reversibel: Flashen, Tests, temporäre Daten, mutable EEPROM-Bereiche
- audit-/semi-permanent: Seriennummer, UUID, Zertifikat, Label; fehlgeschlagene IDs werden `SCRAPPED`, niemals wiederverwendet
- irreversibel: Secure-Element-Slot-Locks, zukünftige OTP-Fuses

Factory Mode muss durch Manufacturing State, physische/servicebezogene Bedingungen und autorisierte Factory Station eingeschränkt werden.
