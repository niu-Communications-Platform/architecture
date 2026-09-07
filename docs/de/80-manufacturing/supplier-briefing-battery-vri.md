# Lieferantenbriefing – Battery Pack / VRI

**Deutsch (kanonisch)** | [English](../../en/80-manufacturing/supplier-briefing-battery-vri.md)

## Zweck

Dieses Dokument bereitet das technische und kommerzielle Erstgespräch mit **VRI GmbH Batterie-Technik, Ellwangen** für das nıu Communications Platform Beltpack vor. Es ist kein Lastenheft und keine Bestellung. Ziel ist, früh gemeinsam mit dem Batteriehersteller eine serienreife Standardlösung bzw. möglichst gering angepasste Packfamilie zu identifizieren.

## Projekt in einem Satz

nıu entwickelt ein professionelles, kompaktes, tragbares IP-Intercom-/Audio-Beltpack mit schnell im Feld wechselbarem Akku, USB-C-Stromversorgung und einer geplanten vier- bis fünfstelligen Skalierbarkeit.

## Grundprämissen

- nıu entwickelt **keinen eigenen Battery Pack und kein packinternes BMS**.
- Gesucht wird eine serienreife, dokumentierte und langfristig verfügbare Herstellerlösung.
- `Made in Germany` ist für das Gesamtprodukt eine hart zu verfolgende Prämisse; ein in Deutschland entwickelter/gefertigter Pack ist daher besonders attraktiv.
- Der Pack ist durch den Endnutzer in wenigen Sekunden wechselbar.
- Kein Hot-Swap: Akkuentnahme darf das Beltpack ausschalten.
- Das Beltpack selbst soll möglichst klein bleiben; ca. 120 × 80 × 35 mm ist eine Obergrenze, kein Zielvolumen.
- Ein Standardpack um ~19 Wh ist derzeit bevorzugter Kandidat, aber noch nicht ausgewählt.
- Ein optionaler Extended Pack ist interessant, wenn er dieselbe Beltpack-Hardware und Schnittstelle nutzen kann.

## Aktuelle Referenz

Besonders interessant erscheint aktuell die vri BASE LINE und darin ein kompakter 1S/21700-Pack um ~19 Wh. Ein 2S-Pack bleibt als Architekturvergleich relevant. VRI soll ausdrücklich nicht lediglich diese Vorauswahl bestätigen, sondern aus Herstellersicht die beste bestehende bzw. seriennah ableitbare Lösung empfehlen.

## Elektrisches Lastprofil – aktueller Engineering-Stand

Das Power Budget ist noch vor Prototype-1-Messung und daher ausdrücklich vorläufig:

| Betriebszustand | Systemleistung |
|---|---:|
| Listening / normales Intercom | ~3,2 W |
| typischer Mischbetrieb | ~3,8 W |
| hohe interne Last | ~5,5 W |
| Design Peak ohne externes USB-Zubehör | ~8 W |
| Design Peak inkl. bis zu ~5 W USB-Zubehör | ~13 W |

Der externe USB-Accessory-Peak ist kein Dauerlastmodell für die beworbene Akkulaufzeit, muss aber bei Pack, Wandlern, Leitungen und Thermik berücksichtigt werden.

## Laufzeit-Zielbild

Mit einem ~19,1-Wh-Pack ergibt das bisherige Engineering-Modell bei 85 % nutzbarer Nominalenergie ungefähr:

- ~5,1 h Listening bei 3,2 W;
- ~4,3 h typischer Mischbetrieb bei 3,8 W;
- ~3,0 h hohe interne Last bei 5,5 W.

Diese Werte sind keine Produktzusage. Prototype 1 muss die reale Leistungsaufnahme messen. Durch schnellen Akkuwechsel wird maximale Einsatzbereitschaft gegenüber maximaler Einzelpack-Laufzeit priorisiert.

## Mechanische Anforderungen

Der komplette Pack soll:

- vom Endnutzer ohne Öffnen des Hauptgehäuses in wenigen Sekunden wechselbar sein;
- eine robuste, fehlstecksichere Kontaktierung besitzen;
- für regelmäßige Feldwechsel ausreichend viele Kontakt-/Steckzyklen unterstützen;
- mechanisch sicher geführt und gegen unbeabsichtigtes Lösen geschützt sein;
- keine proprietäre Spezialwerkzeug-Anforderung erzeugen;
- möglichst eine Kontakt-/Verriegelungszone erlauben, die auch für eine größere Kapazitätsvariante verwendet werden kann.

VRI soll beraten, ob der Standardstecker eines BASE-LINE-Packs für häufigen Feldwechsel geeignet ist oder ob Pack und Gerät besser eine robuste Dock-/Kontaktlösung erhalten, während der interne Packanschluss unverändert bleibt.

## Standard + Extended

Produktseitig bevorzugtes Zielbild:

- **Standard Battery:** ungefähr 19 Wh, möglichst kompakt;
- **Extended Battery:** deutlich mehr Kapazität, grob 30–35 Wh als Untersuchungsbereich;
- gleiche Spannungsklasse, wenn technisch sinnvoll;
- gleiche Host-Pinbelegung;
- gleiche oder kompatible BMS-/Fuel-Gauge-Kommunikation;
- gleiche Kontakt-/Verriegelungszone;
- größere Kapazität darf nach außen stärker auftragen;
- keine zweite Carrier-Platine, Firmwarevariante oder grundlegende Power-Architektur.

Wenn dies relevante Systemkomplexität erzeugt, wird ein einzelner optimaler Standardpack bevorzugt.

## Fragen an VRI – Technik

1. Welchen bestehenden BASE-LINE-Pack empfiehlt VRI für dieses Lastprofil und warum?
2. Ist 1S für unsere 5-V-System-/USB-Architektur sinnvoll oder empfiehlt VRI 2S?
3. Welche realistischen Dauer- und Spitzenströme sollen bei niedrigem SoC und über den Temperaturbereich angesetzt werden?
4. Welche Pack-internen Schutzfunktionen und welche Second-Level-Protection sind vorhanden?
5. Welche Temperaturmessung steht dem Host zur Verfügung?
6. Welche BMS-/Fuel-Gauge-Daten sind über SMBus/I²C verfügbar und wie ist die Schnittstelle dokumentiert?
7. Wie soll der Host einen neu eingesetzten Pack bzw. dessen Health-/Learning-Zustand behandeln?
8. Welche Ladecharakteristik und welche Carrier-seitige Charger-/Power-Path-Architektur empfiehlt VRI?
9. Unterstützt bzw. empfiehlt VRI einen reduzierten Ladezustand/Charge Limit für stationären Dauerbetrieb und Battery Care?
10. Welche thermischen Randbedingungen gelten bei gleichzeitigem Betrieb und Laden?
11. Welche Kontakte/Stecker empfiehlt VRI für regelmäßigen Endnutzer-Akkuwechsel?
12. Welche garantierte bzw. empfohlene Steck-/Kontaktzyklenzahl ist erreichbar?
13. Gibt es eine geeignete vorhandene mechanische Pack-/Gehäuselösung oder sollte nıu die äußere Akkuaufnahme selbst konstruieren?
14. Kann eine ~19-Wh-Standard- und ~30–35-Wh-Extended-Familie mit derselben Host-Schnittstelle und Kontaktzone realisiert werden?
15. Welche externe Einzel- und Mehrfach-Ladelösung empfiehlt VRI für Ersatzpacks?

## Fragen an VRI – Zulassung und Lifecycle

16. Welche Zertifizierungen/Nachweise liegen für den empfohlenen Pack bereits vor (insbesondere UN 38.3, IEC 62133 und ggf. weitere relevante Nachweise)?
17. Welche davon bleiben bei einer mechanisch oder elektrisch geringfügig angepassten Variante bestehen bzw. welche Prüfungen werden neu erforderlich?
18. Welche Unterlagen erhält nıu für Geräte-Zulassung, Transport, technische Dokumentation und EU-Batterieanforderungen?
19. Wie lange ist der Pack bzw. die zugrunde liegende Zell-/BMS-Plattform planbar verfügbar?
20. Wie werden Zellwechsel/Obsoleszenz innerhalb einer Pack-Artikelnummer gehandhabt und kommuniziert?
21. Welche PCN/EOL-Prozesse bietet VRI für Serienkunden?
22. Kann eine langfristige Ersatzteil-/Spare-Pack-Versorgung vertraglich geplant werden?

## Fragen an VRI – Kommerziell

Für den empfohlenen Standardpack und einen möglichen Extended Pack benötigen wir möglichst getrennt:

- Muster-/Prototype-Preis und Verfügbarkeit;
- MOQ;
- Preis bei 100 Stück als Pilotindikator;
- Preis bei **1.000 / 5.000 / 10.000 Stück**;
- mögliche Rahmenvertrags-/Abrufmodelle;
- Lieferzeit und typische Forecast-Anforderungen;
- NRE bei erforderlicher Anpassung;
- Werkzeugkosten bei mechanischer Anpassung;
- Zertifizierungs-/Prüfkosten;
- Kosten einer passenden Einzel-/Mehrfach-Ladelösung;
- Verpackungs-/Transportvorgaben für Pack-Lieferung und Ersatzteilvertrieb.

## Target Cost

Für das Beltpack gilt derzeit:

- Gesamt-COGS Entwicklungsziel: 75–80 EUR;
- Standard-Battery-Pack Cost Budget: **12–16 EUR** in relevanter Serienmenge;
- **>18 EUR** für den Standardpack löst einen Kosten-/Architekturreview aus.

Das Cost Budget ist ein internes Engineering Target, kein Anspruch auf einen bestimmten Lieferantenpreis. Qualität, Lifecycle, Zertifizierungsaufwand und Systemkomplexität werden gemeinsam mit dem Stückpreis bewertet.

## Was wir VRI ausdrücklich nicht vorgeben sollten

Das Gespräch soll nicht mit einer künstlich fertigen Batteriekonstruktion beginnen. Insbesondere nicht vorschnell festlegen:

- 1S versus 2S;
- exakte Zelle;
- exakte BMS-Implementierung;
- exakte Pack-Kapazität;
- exakte Kontaktlösung;
- dass zwingend eine Extended-Variante existieren muss.

Wir geben Systemanforderungen und Zielökonomie vor und wollen die Herstellerkompetenz nutzen.

## Gewünschtes Ergebnis des Erstgesprächs

Nach dem Gespräch sollen idealerweise feststehen:

1. ein bevorzugter vorhandener oder seriennaher Standardpack-Kandidat;
2. 1S/2S-Empfehlung mit Begründung;
3. mechanisches Konzept für regelmäßigen Feldwechsel;
4. Machbarkeit einer kompatiblen Extended-Variante;
5. empfohlene Lade-/Power-Path-Schnittstelle;
6. verfügbare BMS-/Fuel-Gauge-Dokumentation;
7. Zertifizierungs- und Lifecycle-Status;
8. Musterverfügbarkeit;
9. MOQ, NRE und indikative 1k/5k/10k-Preise;
10. konkrete nächste technische Schritte und Ansprechpartner.

## Gesprächseinstieg

> Wir entwickeln ein professionelles IP-Intercom-Beltpack, das langfristig in Deutschland gefertigt werden soll. Der Akku soll vom Anwender in wenigen Sekunden als kompletter zertifizierter Pack gewechselt werden können. Wir möchten bewusst keinen eigenen Akku und kein eigenes BMS entwickeln, sondern eine serienreife VRI-Lösung sauber in unser Produkt integrieren. Aktuell erscheint uns ein kompakter Pack um 19 Wh interessant; wir möchten aber zuerst Ihre Empfehlung hören, bevor wir die Power- und Mechanikarchitektur darauf festlegen.
