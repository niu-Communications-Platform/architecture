# Mechanische I/O-Serienkandidaten

**Deutsch (kanonisch)** | [English](../../en/20-hardware/mechanical-io-series-candidates.md)

## Zweck

Dieses Dokument übersetzt die mechanische I/O-Strategie in konkrete Kandidatenklassen für Prototype 1 und die spätere Serie. Es ist **keine Serienfreigabe**. Bei mechanischen Bedienelementen und Steckverbindern zählen nicht nur Stückpreis und elektrische Funktion, sondern Lebensdauer, Gehäuseintegration, Reparierbarkeit, Montageaufwand, Haptik und Feldausfallrisiko.

## Für Nicht-Elektroingenieure

Ein Steckverbinder oder Taster ist aus Sicht des Schaltplans oft banal. Im fertigen Consumerprodukt gehört er jedoch zu den mechanisch am stärksten belasteten Teilen. Ein guter 50-Cent-Stecker kann wirtschaftlich sinnvoller sein als ein 20-Cent-Stecker, wenn er Gehäuse, Montage und Reklamationen vereinfacht.

**Mating cycle / Steckzyklus** bedeutet einmaliges vollständiges Ein- und Ausstecken. 10.000 Steckzyklen sind daher eine konkrete Lebensdauerangabe und keine Marketingformulierung.

## USB-C POWER

### Referenzkandidat: GCT USB4085

Der USB4085 ist für Prototype 1 ein starker mechanischer Referenzkandidat für den POWER-Port:

- USB Type-C, USB 2.0 / 16 Kontakte
- horizontale Top-Mount-Bauform
- Durchsteck-/Shell-Verankerung für hohe mechanische PCB-Anbindung
- 5 A Stromrating
- Herstellerangabe aktuell bis 20.000 Steckzyklen
- kompakte Bauhöhe
- öffentliche Zeichnungen, Footprints und Spezifikation

Für POWER benötigen wir keine Hochgeschwindigkeitsdaten. Deshalb ist ein mechanisch robuster USB-C-Anschluss mit nur den tatsächlich benötigten Kontakten attraktiver als ein unnötig komplexer USB-3.x-Port.

**CANDIDATE:** USB4085-Klasse für POWER. Exakte Variante und Lieferfähigkeit vor Schematic Freeze prüfen.

## USB-C ACCESSORY

ACCESSORY ist ein echter USB-Hostport und muss mindestens USB 2.0 Daten + 5-V-Versorgung unterstützen. Auch hier ist ein 16-poliger USB-2.0-Type-C-Port grundsätzlich ausreichend, solange DFP/Host-Funktion, CC-Beschaltung und die elektrische Architektur korrekt umgesetzt sind.

Der USB4085 ist deshalb auch hier ein interessanter mechanischer Referenzkandidat. Zwei identische Buchsen könnten BOM, Footprint, Einkauf und Reparatur vereinfachen. Die beiden Ports müssen am Gehäuse und in der Beschriftung dennoch eindeutig unterscheidbar sein.

**Prüfpunkt:** Ob POWER und ACCESSORY tatsächlich dieselbe Buchse erhalten, wird erst nach PCB-/Gehäuseintegration entschieden.

## 3,5-mm-Audiobuchsen

### Referenzklasse: Kycon STX-3500 / robuste PCB-Audiobuchsen

Die Kycon-STX-3500-Serie zeigt eine brauchbare Größenordnung für professionelle 3,5-mm-PCB-Buchsen:

- 3,5 mm
- SMT
- 3/4/5-polige Varianten
- Herstellerangabe 5.000 Steckzyklen
- definierte Ein-/Aussteckkräfte
- dokumentierte Kontaktwiderstände vor/nach Lebensdauertest

Für nıu.cp ist 5.000 Zyklen zunächst ein **Referenzwert, kein automatisch akzeptiertes Serienziel**. Gerade PHONES/TRRS können im Produktionsalltag häufig gesteckt werden. Zusätzlich müssen seitliche Kräfte auf Stecker und Kabel betrachtet werden.

### Mechanisches Ziel

Wo möglich bevorzugen wir Buchsen mit guter mechanischer Abstützung gegen das Gehäuse oder belastbaren PCB-Ankern. Die Lötstellen sollen nicht allein die Hebelkräfte eines eingesteckten 3,5-mm-Steckers aufnehmen.

Für MIC, PHONES und TRRS dürfen unterschiedliche elektrische Kontaktkonfigurationen nötig sein; mechanisch ähnliche Familien sind dennoch vorteilhaft.

**Prototype Gate:** Stecken, Ziehen, Kabelhebel, Gürtelbetrieb, Fall-/Stoßszenarien und Verschleiß praktisch testen.

## PTT

PTT ist kein gewöhnlicher Menüknopf. Es ist eines der primären Verschleiß- und Haptikbauteile des Produkts.

### Referenzfamilie: Alps Alpine SKRA

Die SKRA-Familie zeigt, dass kompakte SMT-Taster mit IP6X/IPX7-ähnlicher Einzelbauteil-Spezifikation und sehr hoher Betätigungslebensdauer verfügbar sind. Je nach Variante nennt Alps Alpine 100.000 bis mehrere Millionen Betätigungen; einzelne aktuelle Varianten liegen bei 2 bis 5 Millionen Zyklen.

Für PTT sind deshalb **mindestens mehrere hunderttausend reale Betätigungen** anzustreben; bevorzugt eine Klasse im Millionenbereich, sofern Haptik, Preis und Mechanik passen.

Wichtig: Die IP-Angabe eines einzelnen Schalters macht das gesamte Beltpack nicht automatisch wasserdicht.

### PTT muss als Gesamtsystem getestet werden

- Betätigungskraft mit bloßer Hand und Handschuh
- eindeutiger Druckpunkt
- lange Haltezeiten
- schnelle wiederholte Betätigung
- versehentliche Aktivierung am Gürtel
- Geräusch/Körperschall in internes Mikrofon
- Betätigung über Gehäusetaste/Membran
- Alterung der Haptik
- Bedienung mit links/rechts

Der konkrete Taster wird erst zusammen mit dem Gehäuse- und Tastenkappenmechanismus ausgewählt.

## Batterie: kein normaler Kabelstecker als Nutzerinterface

Die VRI-Referenzpacks verwenden einen industriellen 5-poligen Molex-Micro-Fit-Anschluss. Dieser kann für interne oder packseitige elektrische Schnittstellen sinnvoll sein. Für den geplanten Akkuwechsel in wenigen Sekunden sollte der Nutzer jedoch voraussichtlich **nicht jedes Mal einen kleinen Kabelstecker greifen und lösen müssen**.

### Bevorzugtes Konzept

Ein geführtes Battery Dock:

1. Akku wird mechanisch in eine definierte Bahn/Tasche eingesetzt.
2. Gehäusemechanik übernimmt Ausrichtung und Fehlsteckschutz.
3. Federnde oder hochzyklenfeste Kontakte stellen automatisch Power und ggf. Kommunikation/Temperatursignal her.
4. Eine Verriegelung hält den Akku mechanisch; die Kontakte tragen nicht die Haltekräfte.
5. Entnahme löst die Kontakte kontrolliert und ohne Zug an Kabeln.

TE Connectivity bietet beispielsweise Direct-to-PCB-Batteriekontakte mit nachgewiesenen 10.000 Steckzyklen; Molex dokumentiert ebenfalls Batterie-Kontaktsysteme mit 10.000 Zyklen. Solche Komponentenklassen zeigen, dass ein hochzyklenfestes Dock technisch realistisch ist.

### Noch keine Festlegung auf Pogo Pins

`Pogo Pin` bezeichnet einen federnden Stiftkontakt. Er ist anschaulich und prinzipiell attraktiv, aber wir legen uns **nicht** darauf fest. Blattfeder-/Mehrpunktkontakte können bei Stromtragfähigkeit, Verschmutzung, Toleranzen, Bauhöhe oder Kosten besser sein.

Das Battery Dock muss gemeinsam mit VRI und dem Mechanical Engineering entwickelt werden. Der Packhersteller muss bestätigen, welche Power-, NTC-, SMBus/I²C- und sonstigen Kontakte benötigt werden und wie sich der Pack beim Kontaktieren/Trennen verhält.

### Battery-Dock-Gates

- ≥10.000 mechanische Wechselzyklen als Entwicklungsziel
- ausreichend Strom für den realen Worst Case einschließlich transienter Lasten
- Kontaktwiderstand und Erwärmung
- keine Verpolung
- kein Kurzschluss durch zugängliche Kontakte
- definierte Kontaktreihenfolge, falls elektrisch erforderlich
- Toleranzausgleich
- Schmutz/Staub/Schweiß
- Fall und Vibration
- keine Lastkräfte über elektrische Kontakte
- werkzeugloser Wechsel in wenigen Sekunden
- Akku darf nicht versehentlich herausfallen
- Kontakte müssen inspizierbar/reinigbar bzw. servicefähig sein

## Display-Verbindung

Für das kleine TFT ist eine FFC/FPC-Verbindung weiterhin sinnvoll. **FFC/FPC** bezeichnet ein flaches flexibles Leiterkabel und den zugehörigen kleinen Steckverbinder. Das Display soll damit als austauschbare Baugruppe behandelt werden können, statt direkt auf den Carrier gelötet zu werden.

Auswahlkriterien:

- möglichst Standard-Pitch (z. B. 0,5 mm, abhängig vom Display)
- Verriegelung am Stecker
- definierte Anzahl Montage-/Servicezyklen
- Kabel nicht unter mechanischer Spannung
- einfacher Displaytausch ohne Carrier-Rework
- Steckverbinder so positionieren, dass Service nicht unnötig andere Baugruppen demontieren muss

## Auswahlprinzip

Für alle extern belasteten I/O-Komponenten gilt:

> **Wir kaufen nicht den billigsten Kontakt. Wir kaufen eine definierte Lebensdauer und integrieren ihn so, dass die Mechanik seine Schwächen nicht verstärkt.**

## Prototype-1-Empfehlung

1. POWER und ACCESSORY zunächst mit robusten, gut dokumentierten USB-C-Buchsen der USB4085-Klasse auslegen.
2. 3,5-mm-Buchsen aus einer professionellen, lebensdauerdefinierten Familie beschaffen und mechanisch testen.
3. PTT mit mindestens zwei unterschiedlichen Betätigungskräften/Mechaniken prototypisieren; Alps SKRA als Referenzfamilie.
4. Battery Dock **nicht** als fertigen Micro-Fit-Handsteckvorgang einfrieren. Mit VRI Anforderungen klären und zwei Kontaktkonzepte mechanisch prototypisieren.
5. Display steckbar über verriegeltes FFC/FPC.
6. Vor Serienfreeze einen eigenen Mechanical-I/O-Life-Testplan mit automatisierten PTT- und Steckzyklen erstellen.

## Offene Punkte

- exakte 3,5-mm-MPNs für MIC/PHONES/TRRS
- genaue USB4085-Varianten und Footprint-Integration
- IP-/Dichtkonzept des Gesamtgehäuses
- PTT-Kraft und Tastengeometrie
- Battery-Dock-Kontakthersteller und Geometrie
- Kontaktreihenfolge des VRI-Packs
- Display-MPN und FPC-Pinout
- Preise 1k/5k/10k und Langzeitverfügbarkeit
