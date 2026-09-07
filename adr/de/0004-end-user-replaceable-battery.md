# ADR-0004: Der Akku ist durch den Endnutzer austauschbar

**Status:** Accepted  
**Datum:** 2026-09-07

## Kontext

Das Beltpack ist ein tragbares, akkubetriebenes Produkt und soll in der Europäischen Union kommerziell vertrieben werden. Art. 11 der Verordnung (EU) 2023/1542 gilt ab 18. Februar 2027 und verlangt grundsätzlich, dass Gerätebatterien während der Produktlebensdauer vom Endnutzer leicht entfernt und ausgetauscht werden können.

Nach Art. 11 gilt eine Batterie insbesondere dann als leicht entfernbar, wenn handelsübliche Werkzeuge ausreichen und weder herstellerspezifische Werkzeuge noch Wärmeenergie oder Lösungsmittel für die Demontage erforderlich sind. Spezialwerkzeuge sind nur dann unschädlich, wenn sie kostenlos mit dem Produkt bereitgestellt werden. Für das Beltpack wird nicht auf eine gesetzliche Ausnahme von der Endnutzer-Austauschbarkeit geplant.

Die Verordnung verlangt außerdem Anleitungen und Sicherheitsinformationen zum Entfernen und Austauschen, deren dauerhafte öffentliche Online-Verfügbarkeit, die Ersatzteilverfügbarkeit kompatibler Batterien für mindestens fünf Jahre nach Inverkehrbringen der letzten Einheit des Gerätemodells sowie das Verbot, den Austausch kompatibler Batterien durch Software zu erschweren.

Rechtsquelle: Verordnung (EU) 2023/1542, insbesondere Art. 11 und Art. 96. Ergänzend sind die jeweils aktuellen Leitlinien und delegierten Rechtsakte der Europäischen Kommission zu berücksichtigen.

## Entscheidung

Der vollständige Akku des Beltpacks wird als **End-User Replaceable Unit** ausgelegt.

Das Serienprodukt muss daher mindestens folgende Architekturbedingungen erfüllen:

- kein Löten zum Akkuwechsel
- keine Verklebung, deren Entfernung Wärme oder Lösungsmittel erfordert
- Zugang mit handelsüblichen Werkzeugen; keine herstellerspezifischen Werkzeuge
- verpolungssicherer und mechanisch geeigneter Steckverbinder
- sicherer Ausbau und Einbau ohne Beschädigung des Geräts oder Akkus bei bestimmungsgemäßem Vorgehen
- kompatibler Ersatzakku darf Funktion, Leistung oder Sicherheit des Geräts nicht beeinträchtigen
- kein Software-Pairing oder sonstiger Softwaremechanismus, der kompatiblen Akkutausch erschwert
- Battery-Health-/Learning-State muss nach Akkuwechsel sinnvoll neu initialisiert werden können
- verständliche Austausch- und Sicherheitsanleitung wird mit dem Produkt bereitgestellt und dauerhaft öffentlich online verfügbar gehalten
- Ersatzteilstrategie berücksichtigt die gesetzliche Mindestverfügbarkeit nach Ende des Inverkehrbringens des Gerätemodells

Ein werkzeugloser Akkudeckel ist nicht zwingend erforderlich. Ein verschraubtes Gehäuse ist zulässig, sofern der Endnutzer den Akku mit handelsüblichen Werkzeugen leicht und sicher erreichen und ersetzen kann.

## Begründung

Die Entscheidung erfüllt nicht nur eine voraussichtliche EU-Compliance-Anforderung, sondern entspricht unmittelbar den Produktzielen Langlebigkeit, Reparierbarkeit und Ressourcenschonung. Der Akku ist eine erwartbare Verschleißkomponente und darf daher nicht die Lebensdauer des gesamten Beltpacks begrenzen.

## Konsequenzen

- Akkugeometrie, Befestigung, Steckverbinder und Gehäusezugang sind P0-relevante Hardwareanforderungen.
- Akku darf nicht als dauerhaft integrierter Bestandteil des Carriers ausgelegt werden.
- Power-Path, Fuel Gauge und Software müssen einen physischen Akkuwechsel tolerieren.
- Mechanisches Design muss die Austauschbarkeit vor Gehäuse-/PCB-Freeze nachweisen.
- Dokumentation und Ersatzteilstrategie sind Teil der Produkt-Compliance.

## Validierungsbedarf

Vor dem mechanischen Design Freeze ist anhand des finalen Prototyps zu prüfen und zu dokumentieren, dass ein Endnutzer den Akku entsprechend Art. 11 der Verordnung (EU) 2023/1542 sicher und ohne unzulässige Hilfsmittel entfernen und durch einen kompatiblen Akku ersetzen kann.
