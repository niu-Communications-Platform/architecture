# P0 Architecture Gate

**Status:** OPEN  
**Ziel:** Ausreichende Sicherheit für Prototype 1, ohne einen vollständigen Product Freeze vorzutäuschen.

## Vor P0 ausreichend festzulegen

- SBC-/Carrier-Grundarchitektur
- Power-Path und Shutdown-Control
- USB-Topologie und externer Host-Port
- Audio-/TDM-Grundarchitektur
- GPIO-/Bus-Reserven und Testpunkte
- Secure Element und Carrier-NVM
- Factory/Device Identity
- Factory-/Recovery-Grundsätze
- zentrale Software-Komponentengrenzen

## Praktisch zu validieren

- [ ] Radxa ZERO 3W + 2× TLV320AIC3204 auf gemeinsamem TDM-Bus
- [ ] SPI-Steuerung beider AIC3204 unter Linux ASoC
- [ ] mindestens 4 unabhängige Capture-/Playback-Kanäle und korrektes Slot-Mapping
- [ ] digitaler Speaker-Amp (TAS2505 oder Alternative) am TDM
- [ ] Jack Detection und automatische CTIA/OMTP-Umschaltung
- [ ] USB-C DFP + Hub + VBUS-Schutz unter realer Last
- [ ] paralleles USB Audio + USB Ethernet/Wi-Fi
- [ ] Network Handover mit Messung der Intercom-Unterbrechung
- [ ] Power-Path / Battery Care / Thermik / Laufzeit
- [ ] ATECC608C TrustFLEX Profil, KeyProvider und Lock-Policy
- [ ] A/B OTA, READY-Markierung und automatischer Rollback
- [ ] RK3566 Maskrom Recovery
- [ ] PTT-Latenz und Audioqualität
- [ ] internes Speaker/Mic-Verhalten ohne unakzeptable Rückkopplung
- [ ] Display-/Button-/LED-UX im physischen Prototyp

## Noch nicht P0-blockierend

- vollständige Cloud-Skalierungsarchitektur
- vollständige Manufacturing SOPs
- detaillierte RMA-Arbeitsanweisungen
- vollständiger Zertifizierungs-Testplan
- endgültige Developer-Mode-/Custom-Trust-UX
- endgültige Auswahl jedes passiven Bauteils

## Gate-Kriterium

P0 ist erreicht, wenn die verbliebenen Unsicherheiten Prototype 1 nicht mehr mit hoher Wahrscheinlichkeit zu einem vermeidbaren Carrier-/PCB-Redesign zwingen und die offenen Kandidaten einen klaren Validierungsplan besitzen.
