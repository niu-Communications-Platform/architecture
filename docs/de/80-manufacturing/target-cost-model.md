# Target-Cost-Modell und Made-in-Germany-Prämisse

**Deutsch (kanonisch)** | [English](../../en/80-manufacturing/target-cost-model.md)

## Zweck

Dieses Dokument definiert den ersten wirtschaftlichen Zielkostenrahmen für das nıu Communications Platform Beltpack. Es ist ein Target-Cost-Modell und noch keine Lieferantenkalkulation.

## Fertigungsprämisse

**DECIDED:** `Made in Germany` wird für die Serienfertigung als hart zu verfolgende Prämisse behandelt. Ziel ist insbesondere, Carrier-PCBA, Gehäusefertigung und Endmontage/EOL soweit wirtschaftlich vertretbar in Deutschland durchführen zu lassen.

Das bedeutet nicht, dass jedes Einzelbauteil deutschen Ursprungs sein muss. SBC, Halbleiter, Display, Batteriezellen bzw. Battery Pack und weitere Komponenten können international beschafft werden. Entscheidend ist eine belastbare deutsche Fertigungs- und Wertschöpfungsarchitektur für das Endprodukt.

Eine Verlagerung wesentlicher Fertigungsschritte ins Ausland soll nicht reflexartig aus Kostengründen erfolgen. Erst wenn belastbare deutsche Angebote zeigen, dass Zielpreis, Qualität und Marge nicht gleichzeitig erreichbar sind, wird die Prämisse neu bewertet.

## Vertrieb und Preis

**CANDIDATE:** Der bisherige Zielverkaufspreis beträgt **189 EUR netto** bzw. bei 19 % deutscher Umsatzsteuer **224,91 EUR brutto**.

Derzeit wird **Direct-to-Customer / Direktvertrieb als wirtschaftlicher Basisfall** modelliert. Stationärer Handel ist keine festgelegte Produktanforderung. Händler-/Distributor-Margen werden deshalb nicht in die primäre Target-Cost-Grenze eingerechnet, müssen aber separat bewertet werden, bevor ein indirekter Vertriebskanal zugesagt wird.

## Margendefinition

Ziel ist mindestens ungefähr **50 % Gross Margin** auf den Nettoverkaufspreis im Direktvertrieb.

Bei 189 EUR netto ergibt das:

- maximale COGS bei exakt 50 % Gross Margin: **94,50 EUR**
- diese Grenze ist eine wirtschaftliche Obergrenze, kein Beschaffungsziel
- internes COGS-Ziel: **ca. 75–80 EUR**
- bei 80 EUR COGS: 109 EUR Gross Profit bzw. ca. **57,7 % Gross Margin**
- bei 75 EUR COGS: 114 EUR Gross Profit bzw. ca. **60,3 % Gross Margin**

Die Differenz zur 94,50-EUR-Grenze dient als notwendige Reserve für reale Serienabweichungen.

## Vorläufige Target-Cost-BOM

Die folgenden Werte sind Engineering Targets für eine vierstellige Serienfertigung und müssen durch RFQs ersetzt werden.

| Kostenblock | Target EUR/Gerät | Einordnung |
|---|---:|---|
| Radxa ZERO 3W, geeignete RAM/eMMC-Konfiguration | 18–24 | öffentliches 1GB/8GB-eMMC-Preisniveau liegt bereits um ~22 USD; Serienangebot erforderlich |
| 2× TLV320AIC3204 | 5–7 | Distributorpreise bei 1k aktuell grob 2,6–3,5 EUR je nach Packaging |
| Secure Element | 0,6–1,0 | ATECC608-Familie öffentlich deutlich unter 1 EUR bei Volumen; finales TrustFLEX-Profil offen |
| Speaker-Amp | 0,7–1,2 | TAS2505-Klasse |
| USB-Hub-/Host-Control, Power-Switching, ESD | 3–5 | exakter Hub/Type-C/Power-Path noch offen |
| Power-Path, Charger, DC/DC, Monitoring | 4–7 | hoher Unsicherheitsanteil bis Battery Pack festgelegt ist |
| GPIO/PWM/NVM, Clocking, Passives | 2–4 | Engineering Allowance |
| Display 1,3–1,5 Zoll | 2–4 | Serien-LCD, kein Maker-Modul |
| interne Mics, Speaker, LEDs, Controls | 3–5 | Engineering Allowance |
| Audio-/USB-/Power-Buchsen und Mechanik-Kleinteile | 3–5 | Engineering Allowance |
| nackte Carrier-PCB | 1,5–3 | RFQ erforderlich |
| deutsche SMT/THT-Bestückung + AOI | 4–7 | RFQ erforderlich; DFM auf automatisierte Bestückung optimieren |
| 19-Wh-Serienakku | 12–18 | derzeit reine Target-Annahme; VRI-Angebot entscheidend |
| Spritzgussgehäuse + Clip/Akkumechanik | 5–9 | Werkzeug-NRE separat; deutsche Referenzen zeigen niedrige einstellige bis ~10-EUR-Stückkosten als plausibel |
| Endmontage, EOL, Provisioning, Verpacken in Deutschland | 5–8 | stark von montagegerechtem Design und Testautomatisierung abhängig |
| Produktverpackung + Karton-Inlay/Drucksachen | 2–3 | hochwertige, aber materialeffiziente DTC-Verpackung |
| **Target COGS** | **ca. 75–80** | Zielwert; Einzelranges dürfen nicht einfach als Worst-Case summiert werden |

## Warum die Einzelranges nicht addiert werden dürfen

Die Tabelle ist Target Costing und keine fertige BOM. Mehrere Positionen überlappen funktional oder hängen von noch offenen Bauteilentscheidungen ab. Die Summe aller oberen Grenzen würde einen künstlichen Worst Case erzeugen. Beim Design Freeze wird jede Position durch eine konkrete BOM- oder Fertigungsposition ersetzt und die Gesamtsumme muss gegen das 75–80-EUR-Ziel geführt werden.

## Kosten, die nicht in der einfachen Stück-BOM verschwinden dürfen

Für die wirtschaftliche Serienfreigabe werden zusätzlich berücksichtigt:

- Ausschuss und Rework
- Incoming-/EOL-Testkosten
- Garantierückstellungen und erwartete RMA-Kosten
- Inbound-Fracht der Komponenten
- Zoll, soweit relevant
- Verpackungs- und Fertigungsausschuss
- externe Lager-/Fulfillment-Kosten, soweit eingesetzt
- Zahlungsgebühren im Direktvertrieb
- Werkzeugamortisation bzw. NRE separat transparent
- Zertifizierung und einmalige Entwicklungskosten separat von COGS

**REVIEW:** Vor finaler Preisentscheidung ist zu definieren, welche dieser Positionen in der internen Kennzahl `COGS` und welche unter Operating Expenses/NRE geführt werden. Für Architekturentscheidungen soll konservativ gerechnet werden.

## Gehäuse

Ein kundenspezifisches Spritzgussgehäuse aus deutscher Fertigung ist wirtschaftlich grundsätzlich plausibel. Öffentlich dokumentierte deutsche Fallbeispiele zeigen Serienpreise von wenigen Euro bei vierstelligen und höheren Stückzahlen, allerdings mit fünfstelligen Werkzeugkosten.

**DECIDED:** Die Werkzeugkosten dürfen nicht dadurch vermieden werden, dass das Serienprodukt dauerhaft mit einer qualitativ oder montagewirtschaftlich schlechteren Gehäuselösung gebaut wird. Prototype/Pilot und Serie dürfen unterschiedliche Fertigungsverfahren nutzen.

Für Prototype/Pilot bleiben additive Verfahren sinnvoll. Spritzguss wird erst nach ausreichender mechanischer Validierung freigegeben.

## Verpackung

Die Verpackung wird als echter COGS-Posten geplant. Für ca. 1.000 Stück zeigen aktuelle deutsche Preisbeispiele individuell bedruckter Kartonverpackungen je nach Konstruktion grob etwa 1–3 EUR pro Stück; Inlay und weitere Bestandteile kommen hinzu.

**TARGET:** ca. **2–3 EUR** für eine hochwertige, kompakte und weitgehend papier-/kartonbasierte Produktverpackung inklusive Inlay und notwendigen Drucksachen.

Da der Direktvertrieb der Basisfall ist, muss zusätzlich entschieden werden, ob die Produktverpackung selbst versandfähig ist oder in einen separaten Versandkarton kommt. Das ist von der Produktverpackungskostenposition getrennt zu betrachten.

## DFM-Regel für Made in Germany

Made in Germany wird wirtschaftlich vor allem durch **Design for Manufacturing and Assembly** ermöglicht, nicht durch späteren Preisdruck auf den Fertiger.

Daher gelten als Architekturziele:

- möglichst wenige PCBs und Kabelverbindungen;
- SMT statt manueller THT-/Kabelarbeit, soweit technisch sinnvoll;
- keine unnötigen Handlötprozesse;
- eindeutige, fehlstecksichere Montage;
- geringe Schrauben-/Befestigerzahl;
- Gehäusefunktionen integrieren, wenn dadurch Montage entfällt;
- automatisierter Factory-/EOL-Test;
- automatisiertes Flashing/Provisioning;
- Testpunkte und Factory Mode von Anfang an;
- Variantenarmut;
- Standardakku und möglicher Extended Pack dürfen keine zweite Beltpack-Fertigungslinie erzeugen.

## Vertriebsregel

**DECIDED:** Das Produkt wird wirtschaftlich zunächst als Direktvertriebsprodukt geplant. Stationärer Handel oder klassische Distribution werden nicht vorausgesetzt.

Das schließt spätere Händler nicht aus. Ein Händlerkanal erhält jedoch ein eigenes Margenmodell und darf nicht stillschweigend aus derselben 189-EUR-DTC-Kalkulation finanziert werden.

## Nächste Kostengates

1. Serienkonfiguration des Radxa (RAM/eMMC) festlegen und Hersteller-/Distributor-RFQ einholen.
2. VRI: Preisstaffeln für Standardpack und mögliche Extended-Familie bei 1k/5k/10k anfragen.
3. Carrier-BOM nach Schaltplanstand auf reale MPNs herunterbrechen.
4. Deutsche EMS-RFQ für 500/1k/5k/10k inklusive Material, AOI, Test und Box Build.
5. Deutsches Gehäuse-RFQ inklusive Werkzeug, Stückpreis 1k/5k/10k und Montageoptimierung.
6. Verpackungs-RFQ 1k/5k/10k inklusive Inlay.
7. Target-Cost-Modell nach jedem RFQ aktualisieren.

## Gate

Bei 189 EUR netto gilt:

> **94,50 EUR COGS ist die 50-%-Marge-Grenze. 75–80 EUR ist unser Entwicklungsziel.**

Die Made-in-Germany-Prämisse gilt als wirtschaftlich tragfähig, solange belastbare Serienangebote zeigen, dass das Produkt mit ausreichender Qualitäts-, Garantie- und Beschaffungsreserve innerhalb dieses Korridors hergestellt werden kann.
