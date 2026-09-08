# Mechanische I/O-Komponenten – Strategie für Prototype 1

**Deutsch (kanonisch)** | [English](../../en/20-hardware/mechanical-io-component-strategy.md)

## Ziel

Dieser Block betrachtet die Bauteile, die elektrisch oft unspektakulär wirken, aber für ein tragbares Consumerprodukt entscheidend sind: Buchsen, Taster, Encoder, Display-Anbindung, Batterie-Stecksystem und deren mechanische Integration.

Für nıu.cp sind diese Teile besonders wichtig, weil sie gleichzeitig Benutzergefühl, Reparierbarkeit, Lebensdauer, Gehäusekonstruktion, Montagezeit und Serienkosten bestimmen.

## Leitprinzip

> **Bei mechanischen I/O-Komponenten ist nicht der Stückpreis allein entscheidend. Das richtige Bauteil reduziert Gehäusekomplexität, manuelle Montage, Ausfallrisiko und Servicekosten.**

## 3,5-mm-Audiobuchsen

Vorgesehen sind weiterhin getrennte Anschlüsse für MIC, PHONES und TRRS-Headset.

Für Prototype 1 sollen keine extrem kleinen Smartphone-Buchsen gewählt werden, wenn dadurch Fertigung und Reparatur unnötig erschwert werden. Bevorzugt werden etablierte, mechanisch robuste PCB-Buchsen mit:

- definiertem Steckzyklen-Rating,
- mechanischem Detect-Kontakt, wo sinnvoll,
- klarer Herstellerzeichnung für Gehäuseausschnitt und Leiterplattenlage,
- ausreichender Haltekraft,
- belastbarer Verankerung auf der PCB,
- möglichst normaler SMT-/THT-Verarbeitung bei einem deutschen Fertiger.

Der TRRS-Port benötigt zusätzlich CTIA/OMTP-Erkennung bzw. Umschaltung auf der Elektronikseite. Der mechanische Port selbst soll nicht unnötig proprietär sein.

### Produktverständnis

Die Buchse ist nicht nur ein elektrischer Kontakt. Bei jedem Ein- und Ausstecken wirken Kräfte auf das Gehäuse und die Leiterplatte. Eine billige oder schlecht abgestützte Buchse kann deshalb trotz perfekter Elektronik zum häufigsten Ausfallpunkt des Produkts werden.

## USB-C

Es bleiben zwei sichtbare USB-C-Ports vorgesehen:

- **POWER:** Energieversorgung und Laden, keine reguläre Datenfunktion.
- **ACCESSORY:** USB-Host für USB Audio, Ethernet, HID und weitere unterstützte Geräte.

USB-C-Buchsen sollen mechanisch stärker bewertet werden als nach dem reinen Bauteilpreis. Bevorzugt werden Ausführungen mit zusätzlichen Gehäuse-/Shield-Lötankern und gut dokumentierter PCB-Footprint-Geometrie.

Für ein mobiles Beltpack ist zu vermeiden, dass die eigentlichen Signalpins die mechanische Last des Kabels tragen.

## Batterie-Stecksystem

Das Batteriesystem ist als schnell wechselbare komplette Produktionseinheit vorgesehen. Der Packhersteller besitzt die Verantwortung für Zellen/BMS; das Carrierdesign übernimmt die Systemintegration.

Die elektrische Verbindung muss daher:

- verpolungssicher bzw. mechanisch codiert sein,
- für häufige Feldwechsel geeignet sein,
- ausreichend Stromreserve bieten,
- Temperatur-/Datenleitungen des gewählten Packs unterstützen,
- auch bei Vibration und Bewegung zuverlässig bleiben,
- und im Service ohne Lötarbeit ersetzbar sein.

VRI BASE LINE verwendet bei den derzeit betrachteten Packs Molex Micro-Fit 3.0 in 5-poliger Ausführung. Das ist deshalb ein relevanter Referenzpunkt, aber noch keine endgültige Serienentscheidung.

Wichtig: Wenn der Akku innerhalb weniger Sekunden wechselbar sein soll, genügt ein normaler interner Kabelstecker allein möglicherweise nicht als Nutzerinterface. Der mechanische Batterieträger kann einen separaten, geführten Kontaktmechanismus benötigen, während ein Micro-Fit- oder vergleichbarer Stecker innerhalb der Pack-/Carrier-Baugruppe verwendet wird. Das wird mit VRI und dem Gehäuseentwickler geklärt.

## PTT und Bedienelemente

Der PTT-Taster ist das am häufigsten betätigte mechanische Bedienelement und deshalb kein gewöhnlicher UI-Taster.

Prototype 1 soll insbesondere validieren:

- Betätigungskraft,
- Hub und taktiles Feedback,
- Bedienung mit Handschuhen,
- Fehlbetätigung beim Tragen,
- Geräuschübertragung in internes Mikrofon,
- Lebensdauer,
- seitliche Krafteinleitung,
- Austauschbarkeit des äußeren Betätigungsteils.

Die Elektronik kann einen Standard-Momenttaster verwenden, aber das Nutzergefühl entsteht wesentlich durch Gehäusekinematik, Tastenkappe und Kraftweg. Deshalb darf der endgültige PTT-MPN nicht isoliert vom Gehäusedesign festgelegt werden.

VOL+/VOL−, CH+/CH−, MENU/OK und BACK sind weniger hoch belastet, sollen aber dieselbe Designsprache und nachvollziehbares taktiles Feedback besitzen.

## Encoder

Ein Drehencoder ist derzeit keine zwingende Produkthardware. Falls er in einem späteren UX-Prototyp einen klaren Vorteil gegenüber den vorgesehenen Tasten zeigt, muss er gegen folgende Nachteile abgewogen werden:

- zusätzliche Gehäusedurchführung,
- mechanische Höhe,
- mögliche Dichtigkeitsprobleme,
- Verschleiß,
- zusätzliche Montagearbeit.

**Capability ≠ Feature** gilt auch hier: Platz oder GPIO-Reserve für einen Encoder ist nicht automatisch ein Grund, einen Encoder ins Serienprodukt zu übernehmen.

## Display

Ziel bleibt ungefähr 1,3–1,5 Zoll, 240×240, farbiges IPS/TFT.

Für Prototype 1 ist nicht nur das Panel relevant, sondern die gesamte mechanische und elektrische Integration:

- FPC/FFC versus direktes Board-Modul,
- Steckverbinder und Verriegelung,
- Displayhöhe und Sichtfenster,
- mechanische Abstützung,
- Lichtspalt/Staubschutz,
- Ersatzbarkeit ohne Carrier-Tausch,
- Beschaffbarkeit des Panels über die Produktlaufzeit.

Für die Serienarchitektur ist ein austauschbares Displaymodul grundsätzlich attraktiver als ein fest mit dem Carrier verlötetes Display, sofern Kosten und Bauraum vertretbar bleiben.

## Montagekosten

Bei diesen Komponenten muss jede Auswahl nicht nur mit dem MPN-Preis bewertet werden, sondern mit:

1. Bauteilpreis,
2. benötigter PCB-Fläche,
3. zusätzlicher Gehäusegeometrie,
4. THT-/Handlötbedarf,
5. Kabeln oder Zwischensteckern,
6. manueller Montagezeit,
7. EOL-Testbarkeit,
8. Reparaturzeit,
9. erwarteter mechanischer Lebensdauer.

Ein um 0,30 EUR teurerer Steckverbinder kann wirtschaftlicher sein, wenn er eine Minute manuelle Montage oder häufige RMA-Fälle verhindert.

## Prototype-1-Gates

Prototype 1 soll vor einer Serienentscheidung mindestens zeigen:

- alle externen Buchsen überstehen wiederholtes Stecken ohne PCB-/Gehäuseschäden,
- USB-C-Kabelkräfte werden mechanisch in Gehäuse/Shield-Verankerung und nicht in Signalpins eingeleitet,
- PTT kann zuverlässig blind und mit Handschuhen bedient werden,
- PTT erzeugt keine unvertretbaren Körperschallartefakte im internen Mikrofon,
- Display kann montiert und idealerweise ersetzt werden, ohne die Hauptplatine zu beschädigen,
- Batterie lässt sich in wenigen Sekunden ohne Öffnen des Hauptgehäuses wechseln,
- der Batterieanschluss bleibt gegen Fehlorientierung geschützt,
- alle außenliegenden I/O-Komponenten sind im EOL-Test elektrisch prüfbar.

## Aktueller Status

**CANDIDATE / STRATEGY, keine MPN-Freigabe.**

Die mechanischen I/O-MPNs werden erst nach gemeinsamem Abgleich von PCB, Gehäuse, Reparaturkonzept und realer Handhabung festgelegt.
