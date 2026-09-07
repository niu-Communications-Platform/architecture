# Architecture Snapshot v0.1

**Datum:** 2026-09-07  
**Status:** Historischer konsolidierter Stand  
**Sprache:** Deutsch, kanonisch  
**Zweck:** Sicherung des bis zu diesem Datum erarbeiteten Architekturstands der nıu Communications Platform vor Beginn der breiten Prototyp-Validierung.

## 1. Produktmodell

Die nıu Communications Platform ist als offene, modular aufgebaute Kommunikationsplattform für Intercom- und weitere IP-Audio-Anwendungen konzipiert.

Geplante Produktvarianten:

- **Bare** — reines Intercom-Endgerät ohne lokal gehosteten Mumble/Murmur-Server.
- **Base** — Intercom plus lokal betriebene Mumble/Murmur-Infrastruktur und lokale Verwaltung.
- **Cloud** — Intercom plus von nıu gehostete Mumble/Murmur- und Verwaltungsdienste; wiederkehrende Gebühr ist grundsätzlich Bestandteil des Modells.

Die GitHub-Organization `nıu Communications Platform` bildet die technische Projektklammer. Implementierungen sollen langfristig in getrennten Monorepositories liegen, insbesondere `beltpack`, `base`, `cloud` und `factory-tools`. Dieses Repository `architecture` enthält die produktübergreifenden Architekturentscheidungen und ihre Begründung.

## 2. Leitprinzipien

### 2.1 Nutzerkomfort vor sichtbarer Komplexität

Die Plattform soll sich im Normalbetrieb möglichst selbstverständlich und kuratiert verhalten. Technische Komplexität wird innerhalb des Systems absorbiert, nicht auf den Nutzer abgewälzt. Ziel sind Details, die den Eindruck erzeugen: „Daran wurde auch gedacht.“

### 2.2 Apple-Komfort, Entwicklerfreiheit darunter

Drei Ebenen werden unterschieden:

1. **Produkt-/Apple-Ebene:** einfache, robuste, getestete Standardbedienung.
2. **Provisioning-Ebene:** Administratorprofile abstrahieren Routing, Feeds, Pegel, Ducking, Endpunkte und Fähigkeiten.
3. **Developer-Ebene:** Quellcode, Konfiguration und APIs erlauben wesentlich freiere Nutzung der Hardware- und Softwarefähigkeiten.

Grundsatz: **Capability ≠ Feature.** Eine technische Fähigkeit ist noch kein offizielles Produktfeature. Sie wird erst dazu, wenn sie verständlich, robust, testbar und supportbar ist.

### 2.3 PCB möglichst unveränderlich, Software veränderbar

Die Leiterplatte soll einfach bleiben, zugleich aber vorhersehbare Sackgassen vermeiden. Teure Hardware-Lock-ins sollen vor dem Prototyp erkannt werden. Günstige Reserven wie GPIOs, TDM-Slots, Testpunkte, Buszugänge und Identitäts-/Security-Bausteine werden bewusst vorgesehen.

### 2.4 Offenheit und Vertrauen trennen

Die Plattform soll vollständig Open Source und reproduzierbar baubar werden: Hardware/PCB, Geräte-Software, Base/Cloud, Provisioning/Management und Protokolle, soweit Dritt-Lizenzen dies erlauben.

Grundsatz: **Open Source grants implementation freedom, not identity or trust.**

nıu-spezifische Trust Roots und private Schlüssel bleiben private Betriebsgeheimnisse. Dritte dürfen dieselbe Software mit eigenen Trust Domains, PKIs und Signaturschlüsseln betreiben.

## 3. Beltpack-Zielbild

### 3.1 Gehäuse und Einsatz

Zielgröße ca. **120 × 80 × 35 mm plus Gürtelclip**. Das Gerät soll täglich tragbar, gleichzeitig gut montierbar, wartbar und für Serienfertigung geeignet sein.

Das Gerät ist primär mobil, soll aber echten stationären Dauerbetrieb unterstützen: Power-Path/Load-Sharing, unterbrechungsfreier Wechsel externe Versorgung ↔ Akku, Temperaturüberwachung, Charge-Limit/Battery-Care und kein permanentes Mikrozyklieren.

### 3.2 SBC-Strategie

- Entwicklungsplattform: **Raspberry Pi Zero 2 W/WH**.
- Serienkandidat: **Radxa ZERO 3W / RK3566**.
- Der SBC bleibt ein fertiges Modul auf einem eigenen Carrier-/Control-/Audio-Board. CPU und RAM werden nicht auf der nıu-Platine integriert.

Begründung: Pi Zero 2 W ist für frühe Softwareentwicklung ausreichend, aber der Mainline-`bcm2835-i2s`-Treiber ist für echte 4-in/4-out-TDM-Nutzung ungeeignet. RK3566/Rockchip I²S/TDM unterstützt hingegen bis zu 8 Playback-/Capture-Kanäle und passt besser zum geplanten Audio-Backbone.

## 4. Audioarchitektur

### 4.1 Physische Endpunkte

Geplant sind:

- internes Mikrofon
- interner Lautsprecher
- separate 3,5-mm-MIC-Buchse
- separate 3,5-mm-PHONES-Buchse
- 3,5-mm-TRRS-Headsetbuchse mit automatischer CTIA/OMTP-Erkennung
- Bluetooth Audio
- USB Audio Class über separaten USB-C-Host-Port

Apple-/Produktebene: exakt **eine aktive Mikrofonquelle gleichzeitig**. Mehrere Ausgänge dürfen parallel aktiv sein.

### 4.2 Codec-Kandidat

Aktueller Favorit: **2× TI TLV320AIC3204**.

Gründe:

- aktives Bauteil
- 2 ADC / 2 DAC pro Codec
- 6 analoge Eingänge, 4 analoge Ausgänge
- Mic Bias, Digital Mic, TDM/I²S/DSP-Schnittstellen
- Linux Mainline ASoC-Treiber `tlv320aic32x4`
- niedrige Leistungsaufnahme

Wichtiger Lock-in: feste I²C-Adresse 0x18. Für zwei Codecs ist daher **SPI-Steuerung** bevorzugt. Audio läuft unabhängig davon über TDM.

Nicht als entschieden behandeln, bevor 2× AIC3204 + TDM + SPI + RK3566 praktisch validiert wurden.

### 4.3 TDM-Zielbild

Kandidat:

- 48 kHz
- 24-bit Audio in 32-bit Slots
- 8 Slots
- ca. 12,288 MHz BCLK

Beispiel Playback:

- Slot 0–1: Codec #1 DAC L/R → PHONES
- Slot 2–3: Codec #2 DAC L/R → TRRS
- Slot 4: digitaler Mono-Speaker-Amp
- Slot 5–7: Reserve

Capture: bis zu vier ADC-Kanäle mit separater Slot-Zuordnung.

### 4.4 Interner Lautsprecher

Da 2× AIC3204 insgesamt vier unabhängige DAC-Kanäle bereitstellen, der interne Speaker aber ein fünfter unabhängiger Wiedergabeendpunkt sein soll, ist ein eigener digitaler TDM-Class-D-Verstärker vorgesehen.

Kandidat: **TI TAS2505**. Architektur wichtiger als konkrete Bauteilwahl.

### 4.5 Zweites internes Mikrofon

Mic 2 ist kein Stereo-Feature. Es dient als spätere Hardwarebasis für Geräusch-/Umgebungsreferenz, Richtwirkung, Wind-/Noise-Erkennung, Echo-/Sprachverarbeitung und ähnliche DSP-Funktionen.

Engineering-/Pilot-Boards sollen Mic 2 bestücken; Serien-V1-Population bleibt optional, bis ein belastbarer Kundennutzen belegt ist.

### 4.6 Zusätzliche Audiofeeds / PGM

Neben Intercom soll mindestens ein weiterer logischer Audiofeed unterstützt werden, zunächst als PGM. Dieser Feed ist unabhängig pegelbar und kann optional Ducking auslösen.

Die Architektur ist absichtlich generisch: spätere Labels können PGM, IFB, Übersetzung, Producer Feed, Guide Track, Conference Audio usw. sein.

USB- und Bluetooth-Audio sind eigenständige digitale Endpunkte und verbrauchen keine analogen DAC-Kanäle.

## 5. USB- und Netzwerkarchitektur

### 5.1 Zwei USB-C-Rollen

- **POWER:** Laden/Versorgung, keine reguläre Datenfunktion.
- **ACCESSORY/USB:** universeller Host/DFP für USB Audio, USB Ethernet, USB Wi-Fi, HID und spätere unterstützte Geräte.

Der SBC wird intern aus `5V_SYS` versorgt. Sein USB-Datenpfad führt zu einem USB-2-Hub auf dem Carrier. Der externe USB-C-Port benötigt echte Host-/DFP-CC-Logik, geschaltetes und geschütztes VBUS, Strombegrenzung, Reverse Blocking und ESD.

Ziel: etwa 5 V / 1 A nutzbar, Schutzgrenze ggf. höher.

### 5.2 Netzwerktransporte

Erste Transportklassen:

- `internal_wifi`
- `usb_wifi`
- `usb_ethernet`

später ggf. `usb_tethering`, `usb_cellular`.

Konzeptuelle Priorität: Ethernet → USB-Wi-Fi → internes Wi-Fi, aber policy-gesteuert.

### 5.3 Handover-Grundsatz

**Make-before-break auf Transportebene; break-before-make auf Mumble-Sessionebene.**

Eine neue Netzwerkverbindung wird vollständig aufgebaut, IP-konfiguriert und validiert, bevor sie PRIMARY wird. Die alte Mumble-Sitzung bleibt bis dahin aktiv. Anschließend wird die alte Sitzung beendet, der neue Transport übernommen und mit derselben Geräteidentität neu verbunden. Es sollen niemals zwei gleichzeitige Mumble-Sitzungen desselben Beltpacks existieren.

Transportzustände:

`ABSENT → PRESENT → CONNECTING → LINKED → IP_READY → VALIDATING → USABLE`, optional `DEGRADED`, `FAILED`, `COOLDOWN`.

Rollen: `NONE`, `CANDIDATE`, `PRIMARY`.

Health-Hierarchie: LINK → IP → ROUTE → SERVER → INTERCOM.

## 6. Geräteidentität, Security und Trust

### 6.1 Vier Identitätsebenen

1. **Factory/Device Identity:** physisches Beltpack, unveränderlich, an Carrier gebunden.
2. **Friendly/Provisioned Identity:** Name/Rolle/Profile, z. B. `CAM-1`, änderbar bzw. übertragbar.
3. **Mumble/Intercom Identity:** Service-Zugang und Zertifikat, getrennt und rotierbar.
4. **Network/Service Identity:** Hostname, IP, MAC, PRIMARY-Transport; flüchtig.

Grundsatz: je tiefer im Runtime-Stack, desto flüchtiger die Identität.

### 6.2 Carrier als Identitätsanker

Der Carrier ist die physische Geräteidentität. SBC und eMMC/Storage sind austauschbare Compute-/Runtime-Komponenten.

Vorgesehen:

- unveränderliche UUID
- sichtbare Seriennummer, z. B. `NIU-BP-00001247`
- Secure Element
- Carrier-NVM/EEPROM

Ein SBC- oder Storage-Tausch darf die Device Identity nicht verändern. Ein Carrier-Tausch bedeutet dagegen neues physisches Gerät. Friendly Identity/Profile können per „Replace Device“ übertragen werden.

### 6.3 Secure Element

Favorit: **Microchip ATECC608C-TFLXTLS / TrustFLEX**.

Ziel:

- Hardware-geschützter Device Root Key
- weitere getrennte Service-/Mumble-/Cloud-Schlüssel
- private Schlüssel verlassen den Chip nicht
- Hardwarebeweis der Geräteidentität
- spätere Unterstützung für Signatur-/Boot-/Counter-Funktionen

Softwareabstraktion: `KeyProvider`, mit File-Provider für Entwicklung und Hardware-Provider für Produktion.

TrustFLEX-Konfiguration ist teilweise irreversibel; Slot-/Lock-Policy muss vor Serienbestellung über TPDS versioniert und praktisch validiert werden.

### 6.4 PKI-Trennung

Geplante Trust-Architektur:

- Device PKI → dauerhafte Device Certificates
- Service PKI → Base-/Cloud-/Mumble-Zertifikate
- Firmware Signing → strikt separate Signaturidentität

Device- und Service-Identität sind nicht dasselbe. Servicezertifikate werden bei Enrollment erzeugt und sind rotierbar.

## 7. Persistenz und Carrier-NVM

Grundsatz:

**Identity lives on carrier. Configuration belongs to deployment. Runtime state belongs to SBC.**

- Secure Element: Schlüssel, Security-Counter, geschützte Secrets.
- Carrier-NVM: Factory-Metadaten, Kalibrierung, Bootstrap/Recovery-Information.
- eMMC: OS, A/B-Slots, lokale Konfigurationscaches, Wi-Fi/Profile, Logs, Runtime.
- Base/Cloud: autoritative Provisionierung, Ownership, Profile und Service-Credential-Status.

Kandidat Carrier-EEPROM: **Microchip 24CS64** (8 KB I²C). Separate Regionen für Factory Header, Manufacturing, Calibration, Recovery Bootstrap und Reserve, jeweils versioniert und mit CRC.

Keine Runtime-Logs, PTT-Historien oder unverschlüsselten Wi-Fi-Passwörter in Carrier-NVM.

## 8. Provisioning und Ownership

Factory Identity und Ownership sind getrennt.

Factory-Neugerät besitzt UUID, Seriennummer, Root Key, Device Certificate und Hardware-Revision, aber noch keinen Besitzer, Friendly Name, Netzwerk-/Mumble-/Base-/Cloud-Account.

Enrollment umfasst:

1. Discovery
2. kryptographische Geräteauthentisierung über Secure Element
3. physischen Claim-Nachweis, z. B. QR/Code
4. Admin-Autorisierung
5. Bindung an Owner/Deployment
6. Profile/Netzwerk/Intercom/Audio-Konfiguration
7. Erzeugung separater Servicekeys und Zertifikate
8. signiertes deklaratives Provisioning Document

Gerätezustände:

`MANUFACTURED → UNCLAIMED → DISCOVERED → AUTHENTICATED → CLAIMED → PROVISIONED → READY`

sowie Fehler-/Offline-/Blocked-/Released-/Retired-Zustände.

Factory Reset löscht niemals UUID, Seriennummer oder Device Root Key. Ownership Release entfernt Owner-/Servicebindung und führt zurück zu UNCLAIMED.

## 9. Fertigung

Das Produkt soll von Anfang an auf vier- bis fünfstellige Stückzahlen skalierbar gedacht werden, ohne die erste Serie unnötig zu verteuern.

Ziel ist vollständige, reproduzierbare Fertigung durch einen Auftragsfertiger inklusive Programmierung, Test und Verpackung.

Factory-Provisioning-Reihenfolge:

1. PCB Assembly
2. elektrisches Bring-up
3. temporärer Manufacturing Candidate Record
4. vollständiger EOL-Test im Factory Mode **vor** Identitätsvergabe
5. atomare Reservierung von Seriennummer + UUID im Factory Registry
6. Schreiben/Verifizieren Carrier-NVM
7. Erzeugen Device Root Key im Secure Element
8. Ausstellen Device Certificate
9. Registry vervollständigen
10. noch keine Serviceidentitäten
11. QR/Label erzeugen
12. QR ↔ EEPROM ↔ Registry ↔ Public Key cross-check
13. erst jetzt irreversible Slot Locks/Security-Finalisierung
14. RK3566 OTP Secure Boot nur nach separat validiertem Recovery-/Factory-Prozess
15. finaler Zustand `UNCLAIMED`, Anzeige sinngemäß „Bereit zur Einrichtung“

Grundregel: **Nothing irreversible before complete cross-verification.**

## 10. Secure/Verified Boot und OTA

Ziel V1:

- signierte OTA-Updates
- A/B-Rootfs
- automatische Rollback-Fähigkeit
- Factory-/Service-Recovery

Produkt-Level-READY entscheidet, ob ein neuer Slot „good“ markiert wird. READY setzt Linux/systemd, lokale Hardware und erforderliche nıu-Dienste voraus, nicht jedoch Wi-Fi/Murmur-Verbindung.

RAUC ist ein starker Kandidat, noch nicht entschieden.

Verified Boot ist für V1 vorgesehen. Voller RK3566-Hardware-Secure-Boot über OTP ist architektonisch vorzubereiten und zu validieren, aber nicht vorschnell irreversibel zu aktivieren.

## 11. UX/UI

Display-Ziel: ca. 1,3–1,5" 240×240 IPS/TFT, dimmbar, Backlight-Timeout etwa 15/30/60/Always-on.

Home zeigt nur betriebsrelevante Informationen:

- eigener Mumble-Name
- aktives Kommunikationsziel
- Akku
- Netzstatus/Signal
- aktive Sprecher
- Lock-Status

Keine reguläre Anzeige von IP, Serveradresse, Ping, CPU-Temperatur oder Uhrzeit.

Tasten:

1. PTT
2. VOL+
3. VOL−
4. CH+
5. CH−
6. MENU/OK
7. BACK
8. POWER

Kein Seitenkarussell; Views, Menüs, Details, Dialoge und Overlays. Zeitkritische Funktionen sollen blind bedienbar sein.

Key Lock: VOL+ + VOL− ca. 2 s; sperrt VOL/CH/MENU/BACK, PTT/POWER bleiben aktiv.

POWER:

- aus: kurz keine Aktion, 2–3 s Boot
- an: kurz Battery Direct View
- 2–3 s: graceful shutdown ohne Bestätigung
- ≥8 s: unabhängiger Hard-Off

Vier RGB-LEDs: PWR, NET, RX, TX mit semantisch konsistenten Zuständen. Farbe ist nicht einziges Informationsmerkmal; Animation beschreibt Aktivität/Transition.

Event Ring Buffer: ca. 20–50 relevante Zustandsänderungen; keine PTT-/Volume-Spamlogs.

## 12. Talkkonnect-Integration

Talkkonnect V4 bietet bereits konfigurierbare GPIOs, MCP23017, Rotary Encoder, I²C-OLED, Statusausgänge, PTT, Simplex-with-Mute und XML-Autoprovisioning.

Talkkonnect soll möglichst wenig verändert werden. nıu-spezifische Logik wird isoliert, damit MPL-2.0-Dateien und eigene nıu-Komponenten klar getrennt bleiben.

Für Hardware-gesicherte TLS-Identitäten ist ein kleiner Integrationspatch erforderlich: statt ausschließlich `tls.LoadX509KeyPair` soll eine Identity-Provider-Abstraktion einen `crypto.Signer` aus Datei oder Secure Element bereitstellen.

## 13. Open-Source-/Lizenzmodell

- Mumble/Murmur: permissive BSD-3-Clause-artige Lizenz, kommerziell nutzbar; Copyright-/Lizenz-/Disclaimer-Hinweise erhalten.
- Talkkonnect: MPL 2.0; kommerziell nutzbar. Modifizierte MPL-Dateien bleiben bei Distribution MPL und müssen im Source verfügbar gemacht werden; separat entwickelte nıu-Dateien werden dadurch nicht automatisch MPL.

Markenrechte sind von Softwarelizenzen getrennt. Offenlegung des Codes erlaubt Dritten nicht, sich als offizieller nıu-Dienst oder nıu-Hardware auszugeben.

## 14. Aktuelle Entscheidungsgrenze: P0 Architecture Gate

Nicht das gesamte Produkt soll vor dem Prototyp theoretisch fertig geplant werden. Vor Prototyp 1 müssen insbesondere diejenigen Entscheidungen ausreichend feststehen, deren spätere Änderung teuer wäre:

- SBC-/Carrier-Grundarchitektur
- Power-Path
- USB-Topologie
- Audio/TDM-Grundarchitektur
- GPIO-/Bus-Reserven
- Secure Element und Carrier-NVM
- Geräteidentität
- Factory-/Recovery-Grundsätze
- Software-Komponentengrenzen

Danach laufen Theorie und Prototyping parallel.

## 15. Wichtigste offene praktische Validierungen

- Radxa ZERO 3W + 2× AIC3204 auf gemeinsamem TDM-Bus
- SPI-Steuerung beider AIC3204 unter Linux ASoC
- vier unabhängige Capture-/Playback-Kanäle und Slot-Mapping
- TAS2505 bzw. alternativer digitaler Speaker-Amp am gemeinsamen TDM
- mechanisch/elektrische Jack Detection und automatische CTIA/OMTP-Umschaltung
- USB-C-DFP/VBUS-/Hub-Topologie unter realer Last
- USB Audio + USB Ethernet/Wi-Fi parallel
- Network Handover und messbare Mumble-Unterbrechung
- Power-Path, Battery-Care, Thermik und Laufzeit
- ATECC608C TrustFLEX Slot-/Lock-Profil und Linux-Integration
- A/B OTA + Produkt-Level-READY + Rollback
- RK3566 Maskrom-Recovery und später Secure-Boot-/OTP-Prozess
- PTT-Latenz, Audioqualität, interne Speaker/Mic-Rückkopplung und UX im Feld

## 16. Nächster Architekturpunkt

Nach diesem Snapshot ist als nächstes die **RMA-/Repair-Architektur auf Komponentenebene** zu definieren: Welche Austauschkomponenten erhalten die Device Identity und ab welchem Austausch entsteht kryptographisch und administrativ ein neues Beltpack?
