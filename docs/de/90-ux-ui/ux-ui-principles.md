---
language: de
canonical: true
status: current
last_reviewed: 2026-09-07
---

# UX-/UI-Prinzipien

## Grundsätze

- zeitkritische Funktionen funktionieren blind
- unmittelbares Feedback
- klare Trennung Home / Menü / Diagnose
- keine unnötigen Bestätigungen
- Realität schlägt Konfiguration
- Farbe = Zustand, Animation = Aktivität/Transition
- Live-Status statt Refresh
- Navigation bleibt statisch, Daten sind dynamisch
- Direct Views verändern den Navigationszustand nicht
- seltene Safety-Chords sind zulässig, tägliche Funktionen nicht
- Capability ≠ Feature
- kein normaler Expert Mode

## Display

Ziel: ca. 1,3–1,5" 240×240 Farb-IPS/TFT, dimmbar, abschaltbare Hintergrundbeleuchtung.

Home zeigt:

- eigenen Mumble-Benutzernamen
- aktives Kommunikationsziel
- Akku
- Netzwerkstatus/Signal
- aktive Sprecher
- Lock-Status

Keine reguläre Anzeige von IP, Server, Ping, Uhrzeit oder CPU-Temperatur.

## Tasten

1. PTT
2. VOL+
3. VOL−
4. CH+
5. CH−
6. MENU/OK
7. BACK
8. POWER

Navigation nutzt Views/Menu/Detail/Dialog/Overlay, keine horizontalen Seiten.

Key Lock: VOL+ + VOL− ca. 2 s. Gesperrt werden VOL/CH/MENU/BACK; PTT und POWER bleiben aktiv.

## Power

- Gerät aus: kurzer Druck ohne Aktion, 2–3 s halten → Boot
- laufend: kurz → Battery Direct View
- 2–3 s halten → graceful shutdown ohne Bestätigung
- ≥8 s → unabhängiger Hard-Off

Boot gilt als erfolgreich, wenn OS/systemd, erforderliche lokale Hardware, lokale Dienste und `niu-beltpack` READY sind. Wi-Fi/Murmur-Verbindung ist dafür nicht erforderlich.

## LEDs

Vier RGB-LEDs: PWR, NET, RX, TX. Zustände verwenden semantisch konsistente Farben; Farbe ist nie das einzige Merkmal.

NET abstrahiert den Transport: kein nutzbares Netzwerk = rot blinkend; Netzwerk vorhanden, Intercom nicht verbunden = orange blinkend; Intercom verbunden = grün.

RX/TX unterscheiden normal, mute/blocked und unmögliche Aktionen über Farbe plus Animation.

## Diagnose

Diagnosebereiche: System, Audio, Verbindungen, Intercom, Power, Ereignisse.

Event Ring Buffer: etwa 20–50 relevante Zustandsänderungen; keine PTT- oder Lautstärke-Spamlogs.
