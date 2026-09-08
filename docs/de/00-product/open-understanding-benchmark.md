# Open Understanding – Benchmark gegen Fairphone und Framework

**Deutsch (kanonisch)** | [English](../../en/00-product/open-understanding-benchmark.md)

## Zweck

Dieses Dokument prüft das Produktversprechen **Open Understanding** gegen zwei besonders relevante bestehende Konzepte: Fairphone und Framework.

Ziel ist ausdrücklich nicht, Fairphone oder Framework kleinzureden. Beide Unternehmen setzen wichtige Maßstäbe für Reparierbarkeit, Langlebigkeit, Modularität und technische Offenheit. Für nıu.cp ist entscheidend, welche Teile dieser Ansätze bereits etabliert sind, wo wir davon lernen können und worin ein eigenständiger zusätzlicher Anspruch liegen kann.

## Ausgangspunkt nıu.cp

Die nıu Communications Platform verfolgt die Kette:

**Open Source → Open Hardware → Open Diagnostics → Open Repair Documentation → Open Understanding.**

Open Understanding ergänzt klassische Offenheit um ein didaktisches Versprechen:

> **Open Hardware bedeutet nicht nur: Du darfst hineinsehen. Open Understanding bedeutet: Wir helfen Dir zu verstehen, was Du dort siehst.**

Das bedeutet nicht, dass jede Baugruppe per Hand bestückbar sein muss. Moderne SMT-Packages, mehrlagige Leiterplatten, USB-C/PD, Hochgeschwindigkeitssignale, HF und rauscharme Audioelektronik können professionelle Fertigung erfordern. Offenheit und Verständlichkeit bleiben trotzdem Ziele.

## Fairphone

### Was Fairphone bereits sehr stark macht

Fairphone entwickelt seine Produkte explizit für Reparierbarkeit und Langlebigkeit. Die offiziellen Reparaturseiten führen Nutzer durch Diagnose und DIY-Reparaturen. Für aktuelle Geräte werden typische Modulreparaturen mit kurzen Zeitangaben beschrieben; Ersatzteiltausch ist ausdrücklich als Nutzeraufgabe vorgesehen.

Fairphone veröffentlicht außerdem umfangreiche Open-Source-Software und beschreibt die Kontrolle des Nutzers über das eigene Gerät als Kernwert. Die eigene Formulierung „If you can’t open it, you don’t own it“ fasst diesen Anspruch prägnant zusammen.

Besonders relevant: Fairphone veröffentlicht bei neueren Geräten auch PCB-Schaltpläne bzw. sehr weitgehende Board-Unterlagen für fortgeschrittene Reparaturen. Im Impact Report 2024 beschreibt Fairphone die Veröffentlichung der Fairphone-5-Schaltpläne ausdrücklich als Beitrag zu anspruchsvolleren Reparaturen. Der Impact Report 2025 führt die Veröffentlichung von Kernel-/Device-Tree-Quellen und Schematics als Teil der Transparenzstrategie fort.

### Was wir von Fairphone übernehmen sollten

- Reparierbarkeit bereits in der Produktarchitektur und Mechanik einplanen.
- Ersatzteile und Reparaturinformationen nicht nur theoretisch, sondern praktisch verfügbar machen.
- Reparaturen so gestalten, dass einfache Arbeiten wirklich vom Nutzer durchgeführt werden können.
- Board-Level-Unterlagen für fortgeschrittene Reparaturen bereitstellen, soweit technisch und lizenzrechtlich möglich.
- Software-Offenheit und langfristige Nutzbarkeit als Bestandteil der Gerätehoheit verstehen.

### Unterschied zu Open Understanding

Fairphone erklärt sehr überzeugend, **wie ein Gerät repariert wird**, und stellt fortgeschrittene technische Unterlagen bereit. In den geprüften offiziellen Materialien ist jedoch kein gleich stark formuliertes, systematisches Produktversprechen erkennbar, den Nutzer anhand des konkreten Produkts didaktisch durch dessen gesamte Funktionsweise zu führen.

Open Understanding ergänzt daher nicht primär „mehr Schaltpläne“, sondern eine Vermittlungsebene zwischen Nutzer und Engineering Reference:

- Was macht eine Baugruppe?
- Warum existiert sie?
- Wie hängt sie mit anderen Baugruppen zusammen?
- Warum wurde genau diese Architektur gewählt?
- Welches Problem verhindert ein bestimmtes Bauteil?

Die Abgrenzung ist graduell, nicht absolut. Fairphone leistet bereits erhebliche Aufklärungs- und Community-Arbeit; nıu.cp soll diesen Gedanken explizit und systematisch als Dokumentationsschicht ausbauen.

## Framework

### Was Framework bereits sehr stark macht

Framework verbindet Reparierbarkeit mit Modularität und Erweiterbarkeit. Die offiziellen Support-Seiten stellen Setup-, Upgrade- und Repair Guides bereit. Komponenten sind gezielt austauschbar; der Nutzer wird ausdrücklich ermutigt, Geräte aufzurüsten und zu verändern.

Für Entwickler stellt Framework offene Schnittstellen, 2D-Zeichnungen, Pinouts und Referenzdesigns bereit. Besonders die Expansion-Card- und Input-Module-Ökosysteme zeigen, wie aus einem Consumerprodukt eine Entwicklerplattform werden kann.

Framework veröffentlicht jedoch nicht allgemein die vollständigen Mainboard-Schaltpläne für jedermann. Die Knowledge Base beschreibt, dass Pinouts und 2D-Zeichnungen öffentlich sind, vollständige Schematics und Assembly Drawings jedoch qualifizierten Repair Shops bereitgestellt werden. Für Expansion Cards gibt es dagegen öffentliche Schematics und Reference Designs.

### Was wir von Framework übernehmen sollten

- Hardware nicht nur reparierbar, sondern bewusst erweiterbar denken.
- Schnittstellen so dokumentieren, dass Dritte tatsächlich Zubehör und eigene Module entwickeln können.
- Reparatur- und Upgrade-Anleitungen als normale Produktdokumentation behandeln, nicht als Ausnahmefall.
- Developer-Dokumentation und Consumer-Dokumentation klar trennen, aber miteinander verlinken.
- Offizielle Erweiterbarkeit durch definierte elektrische, mechanische und softwareseitige Verträge ermöglichen.

### Unterschied zu Open Understanding

Framework ist besonders stark beim Versprechen:

> Du darfst dieses Gerät verändern, erweitern und aufrüsten.

Open Understanding ergänzt dazu:

> Wir erklären Dir zusätzlich, wie und warum die relevanten Teile funktionieren.

Das ist insbesondere für Nutzer interessant, die noch keine Elektronikentwickler sind, aber genug Neugier besitzen, um es zu werden.

## Vergleich

| Dimension | Fairphone | Framework | nıu.cp Ziel |
| --- | --- | --- | --- |
| Nutzerreparatur | sehr stark | sehr stark | sehr stark |
| Ersatzteile | Kernkonzept | Kernkonzept | vorgesehen |
| Modularität/Upgrade | stark | sehr stark | gezielt |
| Open-Source-Software | stark, mit Vendor-Grenzen | stark/selektiv | Kernprinzip |
| öffentliche Hardwareunterlagen | weitgehend, modellabhängig | selektiv | möglichst vollständig |
| Maker-Erweiterbarkeit | vorhanden | sehr stark | explizites Developer-Ziel |
| professionelle Repair Reference | ja | ja | ja |
| systematische Erklärung der Gerätefunktion | teilweise | teilweise | explizites Produktziel |
| Gerät als Lernplattform | nicht primär | indirekt | explizit durch Inside nıu.cp |

## Eigenständiges nıu.cp-Versprechen

nıu.cp soll nicht behaupten, Reparierbarkeit, offene Hardware oder Maker-Unterstützung erfunden zu haben. Das wäre sachlich falsch und unnötig.

Die eigenständige Positionierung entsteht durch die Kombination:

- Consumer-Komfort ohne Zwang zu technischem Wissen,
- echte Reparierbarkeit,
- Entwicklerfreiheit,
- offene technische Referenzen,
- und eine zusätzliche didaktische Ebene, die den Nutzer aktiv vom Produktverständnis bis zum Engineering-Detail führen kann.

Daraus ergibt sich folgende Positionierung:

- **Fairphone:** Dieses Gerät gehört Dir – repariere es.
- **Framework:** Dieses Gerät gehört Dir – erweitere es.
- **nıu.cp:** Dieses Gerät gehört Dir – und wir helfen Dir zu verstehen, wie es funktioniert.

Diese Gegenüberstellung ist eine interne strategische Verdichtung, keine Aussage der jeweiligen Hersteller über sich selbst und keine Werbeaussage über eine behauptete Einzigartigkeit.

## Dokumentationsarchitektur

### Engineering & Repair Reference

Zielgruppe: Elektroingenieure, professionelle Reparaturbetriebe, erfahrene Maker.

Inhalte:

- vollständige bzw. maximal mögliche Schaltpläne
- Stücklisten mit MPNs
- PCB-/Signalinformationen
- Pinouts und Schnittstellen
- Testpunkte und Sollwerte
- Mess- und Diagnoseverfahren
- Kalibrierung
- Factory- und EOL-Tests
- Explosionszeichnungen
- Austausch- und Recovery-Prozeduren
- bekannte Fehlerbilder und Reparaturpfade

### Inside nıu.cp

Zielgruppe: technisch interessierte Nutzer, motivierte Amateure, Maker, Schüler/Studierende und Quereinsteiger.

Didaktische Regel:

**Produktnutzen → Architekturverständnis → Engineering-Detail.**

Fachbegriffe werden erklärt, nicht vermieden. Die Darstellung darf unterhaltsam, visuell und neugierig machend sein, ohne technische Wahrheit zu opfern.

Beispiele:

- Wie wird Sprache zu digitalen Daten?
- Was macht ein Audio-Codec?
- Warum sind auf dem Carrier zwei Codecs vorgesehen?
- Woher kommen die stabilen 5 Volt?
- Was verhandelt USB Power Delivery eigentlich?
- Was unterscheiden I²C, SPI, I²S/TDM und USB?
- Wie läuft ein Audiopaket vom Mikrofon bis zum Beltpack der Gegenstelle?
- Warum ist ESD-Schutz nötig?
- Warum besitzt das Gerät ein Secure Element?
- Was passiert bei einem Stromausfall mitten im Update?

Jedes didaktische Kapitel sollte, wo sinnvoll, direkt auf die Engineering Reference verlinken. Ein Nutzer kann so von einer verständlichen Erklärung bis zum echten Schaltplan derselben Baugruppe durchsteigen.

## Architekturtest durch Erklärbarkeit

Open Understanding kann zusätzlich als Qualitätskontrolle für Architekturentscheidungen dienen.

Für jede wesentliche Baugruppe sollten wir drei Fragen beantworten können:

1. Was macht sie?
2. Warum brauchen wir sie?
3. Warum haben wir sie genau so gebaut?

Wenn die dritte Frage nicht überzeugend beantwortet werden kann, ist das ein Warnsignal für unnötige Komplexität, historische Altlasten oder eine nicht sauber begründete Architekturentscheidung.

Erklärbarkeit ersetzt keine Engineering-Validierung. Sie ist aber ein zusätzlicher Test für konzeptionelle Klarheit.

## Grenzen des Versprechens

Open Understanding bedeutet nicht:

- dass jede Leiterplatte von Hand nachbaubar sein muss,
- dass sicherheitskritische Arbeiten ohne Qualifikation empfohlen werden,
- dass private Trust-Schlüssel oder andere Sicherheitsgeheimnisse veröffentlicht werden,
- dass proprietäre Drittanbieterinformationen entgegen Lizenz oder NDA offengelegt werden,
- dass jede interne Fertigungsinformation automatisch öffentlich sein muss,
- oder dass eine Modifikation weiterhin als offiziell von nıu zertifiziert gelten muss.

Die Trennung bleibt:

> **Diagnostics are open. Trust issuance is not.**

## Quellenbasis des Benchmarks

Offizielle Fairphone-Quellen, geprüft September 2026:

- https://www.fairphone.com/de/repairs
- https://www.fairphone.com/de/open-source
- https://www.fairphone.com/de/software-longevity
- https://www.fairphone.com/de/stories/our-2024-impact-report-is-out-here-are-the-highlights
- https://www.fairphone.com/wp-content/uploads/2026/04/Fairphone-Impact_Report-2025.pdf

Offizielle Framework-Quellen, geprüft September 2026:

- https://frame.work/support
- https://knowledgebase.frame.work/availability-of-schematics-and-boardviews-BJMZ6EAu

## Schlussfolgerung

Fairphone und Framework zeigen, dass Reparierbarkeit, offene technische Dokumentation, Modularität und Entwicklerfreiheit bei hochwertigen Consumerprodukten praktisch umsetzbar sind.

nıu.cp sollte diese bestehenden Konzepte ausdrücklich als Referenz und Inspiration behandeln und nicht versuchen, sie rhetorisch zu übertrumpfen.

Das eigenständige Produktversprechen liegt in der zusätzlichen, bewusst geplanten Vermittlungsebene:

> **Ein nıu.cp-Gerät soll nicht nur benutzbar, reparierbar und veränderbar sein. Ein neugieriger Eigentümer soll die Chance bekommen, es wirklich zu verstehen.**
