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

Ein frei implementierbarer Standard darf außerdem nicht dadurch faktisch geschlossen werden, dass eine normative Anforderung nur unter Nutzung eines Patents umgesetzt werden kann, für das Implementierern keine ausreichenden Nutzungsrechte eingeräumt werden.

## Entscheidung

Der offizielle nıu.cp-Architektur- und Spezifikationsbestand wird offen veröffentlicht und soll unter einer ShareAlike-Lizenz stehen. Bearbeitungen dieses lizenzierten Bestands, die verbreitet werden, müssen unter den entsprechenden offenen Bedingungen weitergegeben werden.

Die Implementierung eines nıu.cp-Standards erzwingt dagegen nicht automatisch die Offenlegung sämtlicher Implementierungsdetails oder produktinterner Mehrwertfunktionen. Hersteller dürfen insbesondere proprietäre Funktionen entwickeln und kommerziell nutzen, solange deren bloße Existenz keine Bearbeitung des lizenzierten Architektur- oder Spezifikationsmaterials darstellt.

Interoperable Erweiterungen des gemeinsamen Standards sollen offen spezifizierbar und upstream-fähig sein. Die Lizenz allein wird jedoch nicht als Mechanismus verwendet, um jede unabhängig entwickelte technische Erweiterung eines kompatiblen Produkts offenzulegen.

nıu.cp nimmt keine normative Anforderung in den offiziellen Standard auf, deren Implementierung von einem Patent abhängt, sofern Implementierern nicht ausreichende Patentnutzungsrechte für die standardessentiellen Patentansprüche eingeräumt werden. Proprietäre oder patentierte Produktinnovationen bleiben ausdrücklich möglich, solange sie nicht erforderlich sind, um eine konforme nıu.cp-Implementierung zu erstellen. Eine detaillierte Contributor-/Patent-Policy kann mit Beginn externer Standardisierungsbeiträge festgelegt werden.

Die Entscheidung, welche Beiträge, Erweiterungen oder Forks Bestandteil des offiziellen nıu.cp-Standards werden, verbleibt bei der nıu.cp-Governance. Die Open-Source-/Open-Content-Lizenz verleiht keine Befugnis, eine abgeleitete Spezifikation als offiziellen nıu.cp-Standard auszugeben. Namens-, Marken-, Konformitäts- und Zertifizierungsrechte werden getrennt von der Copyright-Lizenz geregelt.

## Begründung

Ein offener Standard soll Wettbewerb und Interoperabilität fördern, ohne Hersteller daran zu hindern, sich durch eigene Produktinnovationen zu differenzieren. Ein proprietärer Noise-Cancellation-Algorithmus ist beispielsweise ein legitimer Produktmehrwert und muss nicht allein deshalb offengelegt werden, weil das Produkt nıu.cp implementiert.

Umgekehrt soll der gemeinsame Architektur- und Spezifikationsbestand nicht durch proprietäre Bearbeitungen vereinnahmt werden. ShareAlike hält verbreitete Bearbeitungen dieses Bestands offen und ermöglicht ihre erneute Nutzung im Ökosystem.

Dasselbe Offenheitsziel gilt auf Patentebene für normative Anforderungen: Eine öffentlich lesbare Spezifikation wäre nicht frei implementierbar, wenn ihre zwingende Umsetzung von nicht ausreichend lizenzierten standardessentiellen Patentansprüchen abhinge. Das hindert nıu oder andere Hersteller nicht daran, optionale proprietäre und patentierte Mehrwertfunktionen zu entwickeln.

Governance und Markenrecht lösen dabei eine andere Aufgabe als die Lizenz: Sie bestimmen, was als offizieller nıu.cp-Standard und gegebenenfalls als nıu.cp-konforme Implementierung bezeichnet werden darf.

## Konsequenzen

- Kommerzielle und konkurrierende Implementierungen des nıu.cp-Standards sind ausdrücklich zulässig.
- Produktinterne Mehrwertfunktionen dürfen proprietär bleiben, soweit keine weitergehende Lizenz für die jeweilige Implementierung etwas anderes bestimmt.
- Verbreitete Bearbeitungen des lizenzierten Architektur-/Spezifikationsbestands bleiben unter ShareAlike offen.
- Es besteht keine automatische Pflicht, jede unabhängig entwickelte Protokoll- oder Produkterweiterung upstream einzureichen.
- Normative nıu.cp-Anforderungen dürfen keine Patentfalle für Implementierer schaffen; erforderliche Rechte an standardessentiellen Patentansprüchen müssen ausreichend eingeräumt sein.
- Optionale proprietäre und patentierte Produktinnovationen bleiben zulässig, wenn sie für nıu.cp-Konformität nicht erforderlich sind.
- Eine detaillierte Contributor-/Patent-Policy wird spätestens relevant, wenn externe Parteien an der Standardisierung mitwirken.
- Offene Interoperabilität wird zusätzlich durch Spezifikation, Governance, Konformitätsregeln und gegebenenfalls Zertifizierung abgesichert.
- Die offizielle Aufnahme einer Erweiterung in nıu.cp erfolgt ausschließlich durch den definierten Governance-Prozess.
- Marken- und Namensrechte an nıu.cp werden nicht durch die Open-Content-Lizenz eingeräumt.
- Software- und Hardwareimplementierungen können in ihren jeweiligen Repositories unter dafür geeigneten, separat festgelegten Lizenzen stehen.
