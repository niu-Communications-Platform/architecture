# Vorläufiges Leistungs- und Laufzeitbudget

**Deutsch (kanonisch)** | [English](../../en/20-hardware/power-budget.md)

## Zweck und Reifegrad

Dieses Dokument ist das erste quantitative Leistungsmodell für das nıu Communications Platform Beltpack. Es dient der Vorauswahl der Batteriearchitektur und der technischen Abstimmung mit Batterie-/Power-Herstellern.

**Wichtig:** Dies ist noch kein gemessenes Serienbudget. Verifizierte Datenblattwerte werden mit ausdrücklich gekennzeichneten Engineering-Annahmen kombiniert. Alle wesentlichen Annahmen werden am Prototype 1 durch Messungen ersetzt.

## Bekannte Architektur

Berücksichtigt werden derzeit:

- Radxa ZERO 3W / RK3566 als Serienkandidat
- internes Wi-Fi
- 2× TLV320AIC3204 als Codec-Kandidat
- digitaler Class-D-Speaker-Amp, derzeit TAS2505 als Kandidat
- 1,3–1,5-Zoll-TFT, ungefähr 240×240
- USB-Hub und separater USB-C-Accessory-Host
- Secure Element, Carrier-NVM, GPIO-/LED-Peripherie
- vier RGB-Status-LEDs
- Power-Conversion und Carrier-Verluste

## Verifizierte Ankerwerte

- Radxa spezifiziert für ZERO 3W eine 5-V-/2-A-Versorgung. Das ist eine Versorgungsanforderung und **kein** typischer Verbrauchswert; 10 W dürfen daher nicht als normaler SBC-Verbrauch angesetzt werden.
- TI nennt für TLV320AIC3204 bei 48 kHz beispielhaft 4,1 mW für Stereo-DAC-Playback und 6,1 mW für Stereo-ADC-Record. Der tatsächliche Verbrauch hängt stark von PowerTune, aktivierten Blöcken und Ausgangstreibern ab.
- TI nennt für TAS2505 im 48-kHz-Speaker-Betrieb ohne Audiosignal ungefähr 35,5 mW Eigenverbrauch; die tatsächliche Leistungsaufnahme bei Lautsprecherausgabe hängt zusätzlich von Signal, Pegel und Last ab. Der Baustein kann bis zu 2,6 W Ausgangsleistung an 4 Ω liefern; dieser Maximalwert ist kein sinnvoller Daueransatz für Sprachbetrieb.
- Ein repräsentatives 1,3-Zoll-240×240-IPS-Modul liegt bei ungefähr 0,2 W; Backlight-Helligkeit und das konkrete Panel beeinflussen diesen Wert wesentlich.
- Ein repräsentativer USB-2.0-Hub-Controller kann je nach Port-/Busaktivität grob im Bereich einiger Zehntel Watt liegen. Die konkrete Hub-Auswahl ist noch offen.

## Engineering-Budget pro Verbraucher

Die folgende Tabelle ist bewusst konservativer als die Minimalwerte einzelner Datenblätter.

| Verbraucher | Typical | Heavy/Design | Kommentar |
| --- | ---: | ---: | --- |
| Radxa ZERO 3W inkl. internem Wi-Fi | 2,3 W | 4,0 W | **ASSUMPTION** bis Messung am Zielimage; größter Unsicherheitsfaktor |
| 2× Audio-Codecs + Analogpfade | 0,10 W | 0,25 W | konservativ gegenüber reinen ADC/DAC-Kernwerten |
| Display inkl. Backlight | 0,15 W | 0,25 W | PWM/Helligkeit relevant |
| USB-Hub, ohne externe Last | 0,20 W | 0,35 W | konkrete Auswahl offen |
| Secure Element, NVM, GPIO, LED-Treiber, Sensorik | 0,10 W | 0,20 W | Sammelbudget |
| 4× RGB-Status-LEDs | 0,05 W | 0,15 W | keine Dauer-Vollweiß-Annahme |
| Audio-Ausgänge / Kopfhörer | 0,10 W | 0,20 W | ohne internen Lautsprecher |
| interner Speaker-Amp + Sprachwiedergabe | +0,20 W | +0,80 W | stark pegel-/signalabhängig |
| Carrier-/Power-Verluste und Reserve | 0,20 W | 0,40 W | wird später aus Wirkungsgradmodell ersetzt |

Diese Werte sind keine Bauteilspezifikation, sondern ein Systemmodell zur Dimensionierung.

## Betriebszustände

Aus den Einzelbudgets werden zunächst folgende Zielgrößen abgeleitet:

| Betriebszustand | Vorläufige Pack-Leistung | Bedeutung |
| --- | ---: | --- |
| Listening / normaler Intercom-Empfang | **~3,2 W** | Wi-Fi/Mumble aktiv, Display, Audio bereit/Playback, kein lauter interner Speaker |
| Typical mixed use | **~3,8 W** | realistische Mischung aus RX, PTT/TX, UI und Audio |
| Heavy internal use | **~5,5 W** | hohe SBC-/Wi-Fi-Aktivität plus interne Audioausgabe |
| Design peak, ohne externe USB-Last | **~8 W** | konservative kurzzeitige Auslegungsgröße, nicht Laufzeitverbrauch |
| Design peak mit 5-V-/1-A-USB-Accessory | **~13 W** | 8 W Gerät + bis zu 5 W externe Last; kein typischer Laufzeitfall |

**REVIEW:** Das bisherige Architekturziel von bis zu ungefähr 5 V / 1 A am Accessory-Port wird als separate Leistungsreserve behandelt. Ein angeschlossenes 5-W-USB-Gerät darf nicht in die beworbene Standardlaufzeit des Beltpacks eingerechnet werden, muss aber bei Pack-, Wandler-, Leiterbahn- und Thermikdimensionierung berücksichtigt werden.

## Vorläufige Laufzeit

Für eine realistischere Vorauswahl wird nicht mit 100 % der Nennenergie gerechnet. Als erste Engineering-Annahme werden **85 % der Nennenergie** als nutzbares Systembudget angesetzt. Diese 15-%-Reserve ist noch keine finale Garantieformel; sie dient zunächst als pauschaler Abschlag für nicht vollständig nutzbare Energie, Umwandlungs-/Systemeffekte und Reserve.

### VRI-Kandidat 1S/21700 — ca. 19,1 Wh

Nutzbares Rechenbudget bei 85 %: **ca. 16,2 Wh**.

| Zustand | geschätzte Laufzeit |
| --- | ---: |
| Listening ~3,2 W | **~5,1 h** |
| Typical mixed ~3,8 W | **~4,3 h** |
| Heavy ~5,5 W | **~3,0 h** |

### VRI-Kandidat 2S/18650 — ca. 25,2 Wh

Nutzbares Rechenbudget bei 85 %: **ca. 21,4 Wh**.

| Zustand | geschätzte Laufzeit |
| --- | ---: |
| Listening ~3,2 W | **~6,7 h** |
| Typical mixed ~3,8 W | **~5,6 h** |
| Heavy ~5,5 W | **~3,9 h** |

## Konservativer Alterungsblick

Für eine spätere garantierte Produktlaufzeit muss zusätzlich Alterung berücksichtigt werden. Nur als Sensitivitätsrechnung ergibt ein Gesamtbudget von 75 % der ursprünglichen Nennenergie ungefähr:

| Pack | Listening 3,2 W | Mixed 3,8 W | Heavy 5,5 W |
| --- | ---: | ---: | ---: |
| 19,1 Wh | ~4,5 h | ~3,8 h | ~2,6 h |
| 25,2 Wh | ~5,9 h | ~5,0 h | ~3,4 h |

**REVIEW:** 75 % ist keine beschlossene End-of-Life-Grenze und keine zugesicherte Laufzeit. Die spätere Garantieformel muss Pack-Daten, Alterung, Temperatur, Entladegrenzen und gemessene Wandlerwirkungsgrade berücksichtigen.

## Elektrische Peak-Betrachtung

Bei 13 W System-/Accessory-Leistung würde ein 1S-Pack auf 3,6-V-Nennspannungsniveau idealisiert etwa 3,6 A liefern; mit Wandlerverlusten entsprechend mehr. Der derzeit betrachtete VRI-1S/21700-Pack ist laut Hersteller mit bis zu 7 A Entladestrom angegeben. Der 2S/18650-Kandidat ist mit bis zu 5 A bei 7,2 V angegeben.

Damit erscheint **keiner der beiden Packs aufgrund der bisher angenommenen Leistungspeaks offensichtlich ausgeschlossen**. Für 1S ist allerdings die effiziente Erzeugung einer belastbaren 5-V-System-/USB-Schiene bei niedriger Zellspannung ein zentraler Power-Design-Punkt. 2S reduziert Packstrom, benötigt dafür aber Step-down-Konversion für die wesentlichen Systemschienen.

Diese Aussage ist vorläufig und ersetzt weder ein reales Lastprofil noch die Abstimmung mit VRI.

## Erste Schlussfolgerung

Das Modell liefert eine wichtige Korrektur gegenüber einer rein kapazitätsgetriebenen Betrachtung:

- **19 Wh ist technisch weiterhin plausibel**, aber nach aktuellem Budget eher ein ungefähr vier- bis fünfstündiger Standardakku als ein ganzer Produktionstag.
- **25 Wh verschiebt den realistischen Bereich grob auf fünf bis sieben Stunden** und bietet mehr Reserve, kostet aber Bauraum und Gewicht.
- Durch den beschlossenen schnellen Feldwechsel muss ein einzelner Pack keine komplette lange Schicht abdecken.
- Der 19-Wh-Pack wird dadurch nicht disqualifiziert; im Gegenteil kann **kleineres Beltpack + zweiter Wechselakku** systemisch attraktiver sein als ein dauerhaft größeres Gerät.
- Vor einer Packentscheidung ist der reale Radxa-Verbrauch der mit Abstand wichtigste Messwert.

**CANDIDATE DIRECTION:** 19 Wh bleibt der Miniaturisierungsfavorit; 25 Wh bleibt der Laufzeit-/Reservefavorit. Noch keine Auswahl.

## Messplan Prototype 1

Die Annahmen werden durch Messungen am Zielsystem ersetzt. Mindestens zu messen sind:

1. Radxa booted, Wi-Fi verbunden, idle
2. Mumble verbunden, Listening
3. kontinuierlicher RX über Kopfhörer
4. kontinuierlicher TX/PTT
5. gemischtes Intercom-Lastprofil
6. interner Speaker bei mehreren praxisgerechten Pegeln
7. hohe CPU-/Wi-Fi-Last
8. Display bei typischer und maximaler Helligkeit
9. USB-Hub ohne Gerät
10. USB Audio, USB Ethernet und USB Wi-Fi
11. externe USB-Last in Stufen bis zum festgelegten Portlimit
12. vollständige Pack-Leistung inklusive Wandlerverlusten
13. Messung bei hohem und niedrigem State of Charge
14. Thermik unter Heavy Load und während gleichzeitigem Laden/Betrieb

Aus diesen Messungen wird ein reproduzierbares **Beltpack Standard Duty Cycle** definiert. Erst dieser Duty Cycle bildet die Grundlage einer später beworbenen bzw. garantierten Laufzeit.

## Quellen

- Radxa ZERO 3 documentation: https://docs.radxa.com/en/zero/zero3
- Radxa ZERO 3W Product Brief, Power Requirements: https://dl.radxa.com/zero3/docs/hw/3w/radxa_zero_3w_product_brief_Revision_1.8.pdf
- Texas Instruments TLV320AIC3204: https://www.ti.com/product/TLV320AIC3204
- Texas Instruments TAS2505: https://www.ti.com/product/TAS2505
- Texas Instruments TAS2505 Application Reference Guide: https://www.ti.com/lit/pdf/SLAU472

Die Zahlen dieses Dokuments müssen vor Serienentscheidungen gegen aktuelle Datenblätter und reale Messungen verifiziert werden.
