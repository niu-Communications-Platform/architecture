---
status: accepted
date: 2026-09-29
---

# ADR-0007: Offener Standard und proprietäre Implementierungen sind getrennt

**Deutsch (kanonisch)** | [English](../en/0007-open-standard-proprietary-implementations.md)

**Status:** Accepted  
**Datum:** 2026-09-29

## Kontext

nıu.cp soll als offener, frei implementierbarer Kommunikationsstandard und als Grundlage eines interoperablen Ökosystems entwickelt werden. Andere Hersteller sollen ausdrücklich kompatible Produkte entwickeln, kommerziell vertreiben und mit eigenen technischen Mehrwerten differenzieren können.

Dabei muss zwischen dem gemeinsamen offenen Standard und einer konkreten Produktimplementierung unterschieden werden. Beispielsweise kann nıu.cp eine Audioschnittstelle und ihr Verhalten spezifizieren, während ein Hersteller innerhalb seines Produkts eine eigene Noise-Cancellation-Funktion implementiert. Eine solche produktinterne Mehrwertfunktion ist nicht allein deshalb Bestandteil des Standards.

Gleichzeitig sollen Bearbeitungen und Weiterentwicklungen des veröffentlichten Architektur- und Spezifikationsbestands offen bleiben und grundsätzlich wieder in den gemeinsamen Standard zurückfließen können.

## Entscheidung

Der offizielle nıu.cp-Architektur- und Spezifikationsbestand wird offen veröffentlicht und soll unter einer ShareAlike-Lizenz stehen. Bearbeitungen dieses lizenzierten Bestands, die verbreitet werden, müssen unter den entsprechenden offenen Bedingungen weitergegeben werden.

Die Implementierung eines nıu.cp-Standards erzwingt dagegen nicht automatisch die Offenlegung sämtlicher Implementierungsdetails oder produktinterner Mehrwertfunktionen. Hersteller dürfen insbesondere proprietäre Funktionen entwickeln und kommerziell nutzen, solange deren bloße Existenz keine Bearbeitung des lizenzierten Architektur- oder Spezifikationsmaterials darstellt.

Interoperable Erweiterungen des gemeinsamen Standards sollen offen spezifizierbar und upstream-fähig sein. Die Lizenz allein wird jedoch nicht als Mechanismus verwendet, um jede unabhängig entwickelte technische Erweiterung eines kompatiblen Produkts offenzulegen.

Die Entscheidung, welche Beiträge, Erweiterungen oder Forks Bestandteil des offiziellen nıu.cp-Standards werden, verbleibt bei der nıu.cp-Governance. Die Open-Source-/Open-Content-Lizenz verleiht keine Befugnis, eine abgeleitete Spezifikation als offiziellen nıu.cp-Standard auszugeben. Namens-, Marken-, Konformitäts- und Zertifizierungsrechte werden getrennt von der Copyright-Lizenz geregelt.

## Begründung

Ein offener Standard soll Wettbewerb und Interoperabilität fördern, ohne Hersteller daran zu hindern, sich durch eigene Produktinnovationen zu differenzieren. Ein proprietärer Noise-Cancellation-Algorithmus ist beispielsweise ein legitimer Produktmehrwert und muss nicht allein deshalb offengelegt werden, weil das Produkt nıu.cp implementiert.

Umgekehrt soll der gemeinsame Architektur- und Spezifikationsbestand nicht durch proprietäre Bearbeitungen vereinnahmt werden. ShareAlike hält verbreitete Bearbeitungen dieses Bestands offen und ermöglicht ihre erneute Nutzung im Ökosystem.

Governance und Markenrecht lösen dabei eine andere Aufgabe als die Lizenz: Sie bestimmen, was als offizieller nıu.cp-Standard und gegebenenfalls als nıu.cp-konforme Implementierung bezeichnet werden darf.

## Konsequenzen

- Kommerzielle und konkurrierende Implementierungen des nıu.cp-Standards sind ausdrücklich zulässig.
- Produktinterne Mehrwertfunktionen dürfen proprietär bleiben, soweit keine weitergehende Lizenz für die jeweilige Implementierung etwas anderes bestimmt.
- Verbreitete Bearbeitungen des lizenzierten Architektur-/Spezifikationsbestands bleiben unter ShareAlike offen.
- Es besteht keine automatische Pflicht, jede unabhängig entwickelte Protokoll- oder Produkterweiterung upstream einzureichen.
- Offene Interoperabilität wird zusätzlich durch Spezifikation, Governance, Konformitätsregeln und gegebenenfalls Zertifizierung abgesichert.
- Die offizielle Aufnahme einer Erweiterung in nıu.cp erfolgt ausschließlich durch den definierten Governance-Prozess.
- Marken- und Namensrechte an nıu.cp werden nicht durch die Open-Content-Lizenz eingeräumt.
- Software- und Hardwareimplementierungen können in ihren jeweiligen Repositories unter dafür geeigneten, separat festgelegten Lizenzen stehen.
