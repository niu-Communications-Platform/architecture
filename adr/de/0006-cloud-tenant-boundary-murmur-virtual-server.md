---
status: accepted
date: 2026-09-28
---

# ADR-0006: Murmur Virtual Server bilden die Cloud-Mandantengrenze

**Deutsch (kanonisch)** | [English](../en/0006-cloud-tenant-boundary-murmur-virtual-server.md)

## Status

**ACCEPTED**

## Kontext

nıu.cp wird in den Varianten Bare, Base und Cloud gedacht. In der Cloud-Variante betreibt nıu die Mumble-/Murmur-Infrastruktur für mehrere voneinander unabhängige Kunden bzw. Mandanten.

Murmur unterstützt mehrere virtuelle Server innerhalb eines Prozesses. Gleichzeitig stehen innerhalb eines virtuellen Servers Channels, Gruppen und ACLs für die Strukturierung und Zugriffskontrolle zur Verfügung.

Für nıu.cp muss eine klare technische Grenze definiert werden, an der Mandanten voneinander getrennt werden. Eine reine Trennung mehrerer Kunden innerhalb desselben virtuellen Servers über Channel-Passwörter, Tokens oder ACLs würde die Tenant-Isolation von der korrekten Konfiguration einzelner Channel-Berechtigungen abhängig machen. Umgekehrt würde ein eigener Murmur-Prozess oder Container je Standardmandant die von Murmur vorgesehene Virtual-Server-Abstraktion nicht nutzen und den Betriebsaufwand unnötig erhöhen.

## Entscheidung

In **nıu.cp Cloud bildet ein Murmur Virtual Server die technische Standard-Mandantengrenze**.

Die Zuordnung lautet:

- **Tenant / Kunde → Murmur Virtual Server**
- **Projekt / Produktion / Arbeitsbereich → Channel bzw. Channel Tree innerhalb des Virtual Servers**
- **Rolle / Funktion → Murmur Group und ACL**
- **Benutzer / Gerät → authentifizierte Identität innerhalb des zugeordneten Mandanten**

Ein Murmur-Prozess darf mehrere virtuelle Server und damit mehrere nıu.cp-Cloud-Mandanten betreiben.

Die nıu.cp Control Plane verwaltet die Zuordnung mindestens in der Form:

`tenant → Murmur node → virtual server`

Die konkrete Murmur-Topologie ist eine interne Implementierungsdetailschicht. Clients und Beltpacks werden über Provisioning auf ihren Zielservice und ihre Rolle abgebildet und müssen die physische Node-Zuordnung nicht selbst verwalten.

Murmur Ice bzw. eine vergleichbare administrative Management-Schnittstelle ist **kein direktes Tenant-Interface**. Sie bleibt ausschließlich Bestandteil der internen Control Plane. Mandantenadministration erfolgt über nıu.cp-eigene, tenant-autorisierte Verwaltungsfunktionen.

Ein eigener Murmur-Prozess, Container oder Host bleibt als höhere optionale Isolationsstufe zulässig, beispielsweise für besondere Enterprise-, Compliance-, SLA- oder Betriebsanforderungen. Diese stärkere Isolation ist nicht der Standardfall und ändert die logische Tenant-Abstraktion nicht.

## Begründung

Der Murmur Virtual Server ist die passende Zwischenebene zwischen Channel-Berechtigungen und vollständiger Prozess-/Host-Isolation.

Dadurch werden Verantwortlichkeiten klar getrennt:

- Channels und ACLs strukturieren einen Mandanten, statt Mandanten voneinander zu trennen.
- Virtual Server isolieren Standardmandanten auf der dafür vorgesehenen Murmur-Ebene.
- Prozesse, Container und Hosts bilden bei Bedarf zusätzliche Betriebs- und Isolationsgrenzen.
- Die nıu.cp Control Plane bleibt die maßgebliche Instanz für Tenant-Zuordnung, Provisioning und Administration.

Die Architektur kann damit klein beginnen und später auf mehrere Murmur-Nodes skalieren, ohne das Mandantenmodell zu ändern.

## Konsequenzen

- Die Cloud-Control-Plane benötigt eine dauerhafte Zuordnung von Tenant, Murmur Node und Virtual Server ID.
- Beim Anlegen eines Cloud-Tenants wird ein neuer Virtual Server erzeugt oder eindeutig zugewiesen.
- Projekte und Produktionen eines Mandanten erzeugen grundsätzlich keinen eigenen Murmur Virtual Server, sondern werden innerhalb des Tenant-Servers strukturiert.
- Channel-Passwörter, Tokens, Gruppen und ACLs dürfen nicht als primäre Mandantengrenze verwendet werden.
- Administrative Murmur-Schnittstellen dürfen nicht direkt an Mandanten exponiert werden.
- Monitoring, Backup, Migration und Capacity Planning müssen Virtual Server als Tenant-Einheit berücksichtigen.
- Ein Tenant muss zwischen Murmur-Nodes migrierbar bleiben, ohne seine logische nıu.cp-Identität zu verlieren.
- Base- und Bare-Varianten bleiben von dieser Cloud-Betriebsentscheidung entkoppelt: Base kann lokal einen oder mehrere Virtual Server betreiben; Bare darf beliebige kompatible Mumble-/Murmur-Infrastruktur verwenden.

## Abhängigkeiten

- ADR-0003: Open Source und Trust Domain sind getrennt.
- Provisioning Authority / Control Plane müssen Tenant-Zuordnung und Serviceparameter sicher verteilen können.
- Das spätere `cloud`-Repository muss diese Tenant-Abstraktion implementieren, ohne Murmur-spezifische Details unnötig in Geräte- oder Nutzerinterfaces zu leaken.

## Validierungsbedarf

Vor produktivem Cloud-Betrieb ist praktisch zu validieren:

- automatisches Erzeugen, Konfigurieren und Entfernen von Virtual Servern,
- sichere tenantbezogene Administration ausschließlich über die nıu.cp Control Plane,
- Isolation von Benutzer-, Channel- und Konfigurationsdaten zwischen zwei Testmandanten,
- Verhalten bei Ausfall und Neustart eines Murmur-Nodes,
- Backup/Restore und Migration eines einzelnen Tenants auf einen anderen Node,
- Capacity-Grenzen eines Murmur-Prozesses bzw. Nodes für das spätere Scheduling neuer Tenants.
