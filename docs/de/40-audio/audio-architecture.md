---
language: de
canonical: true
status: current
last_reviewed: 2026-09-07
translation: ../../en/40-audio/audio-architecture.md
---

# Audioarchitektur

**Deutsch (kanonisch)** | [English](../../en/40-audio/audio-architecture.md)

## Anforderungen

Das Beltpack soll folgende Audioendpunkte unterstützen:

- internes Mikrofon und interner Lautsprecher
- separate MIC- und PHONES-Buchsen
- TRRS-Headset mit automatischer CTIA/OMTP-Behandlung
- Bluetooth Audio
- USB Audio Class

Auf Produktebene ist genau eine Mikrofonquelle gleichzeitig aktiv. Mehrere Wiedergabeausgänge dürfen parallel aktiv sein.

## Routing

Ein globaler RX-Masterpegel liegt logisch vor der Verteilung auf die Ausgänge. Intercom und zusätzliche Feeds werden als getrennte logische Quellen behandelt.

Mögliche technische Routings umfassen u. a.:

- Intercom + PGM gemeinsam auf einem Headset
- Intercom auf USB, PGM auf PHONES
- Intercom auf TRRS, PGM auf Speaker
- Split Ear L/R bei geeigneten Endpunkten

Die freie Matrix gehört in die Developer-Ebene; die normale UI zeigt nur kuratierte Profile.

## Zusätzliche Feeds

PGM ist der erste Anwendungsfall eines generischen zusätzlichen Audiofeeds. Spätere Semantik kann IFB, Übersetzung, Producer Feed, Guide Track oder Conference Audio sein. Feeds besitzen unabhängigen Pegel und optional Ducking.

## Analog-/TDM-Zielarchitektur

**CANDIDATE:** 2× TLV320AIC3204 plus eigener digitaler Speaker-Amp auf gemeinsamem TDM-Bus.

Codec #1 / Body Audio:
- DAC L/R → PHONES
- ADCs → Internal Mic 1, separate MIC, optional Internal Mic 2, Reserve

Codec #2 / Headset:
- DAC L/R → TRRS
- ADC → TRRS-Mikrofon nach CTIA/OMTP-Umschaltung, Reserve

Speaker:
- eigener TDM-Slot → digitaler Class-D-Amp → interner Lautsprecher

TDM-Kandidat: 48 kHz, 24-bit Nutzdaten in 32-bit Slots, 8 Slots.

## Endpoint-Fallback

Gewünschtes Routing und tatsächlich verfügbares Routing werden getrennt betrachtet.

- Fällt der letzte aktive externe RX-Ausgang weg, wird nach Möglichkeit auf internen Speaker zurückgefallen und der Nutzer informiert.
- Fällt das aktive Mikrofon weg, wird nach Möglichkeit das interne Mikrofon aktiviert und informiert.

Grundsatz: **Audio remains functional when possible.**

## Interner Mic 2

Mic 2 ist eine optionale Hardwarebasis für spätere DSP-/Noise-/AEC-/Richtwirkungsfunktionen, kein Stereo-Mikrofonfeature. Engineering-/Pilot-Boards sollen ihn bestücken; Serienpopulation bleibt bis zur Nutzenvalidierung optional.
