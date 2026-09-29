# Security-Richtlinie

[English](SECURITY.md) | **Deutsch (kanonisch)**

Security ist Bestandteil der nıu.cp-Architektur, insbesondere bei Geräteidentität, Provisioning, Trust Domains, Firmware-Authentizität, Update-/Recovery-Mechanismen und Service-Credentials.

## Sicherheitslücke melden

Bitte **melde ausnutzbare Sicherheitslücken nicht über öffentliche GitHub-Issues, Pull Requests, Discussions oder andere öffentliche Projektkanäle**.

Sicherheitslücken können vertraulich per E-Mail gemeldet werden an:

**security@niuversum.de**

Dieser Meldekanal ist bewusst unabhängig von der Repository-Hostingplattform, damit er auch bei einem späteren Wechsel von GitHub stabil bleibt.

## Inhalt einer Meldung

Soweit sinnvoll und möglich, sollte eine Meldung enthalten:

- betroffene Komponente, Dokumentation, Implementierung oder Version;
- klare Beschreibung der Schwachstelle;
- Reproduktionsschritte oder einen minimalen Proof of Concept;
- erwartetes und beobachtetes Verhalten;
- mögliche Security-Auswirkungen;
- relevante Umgebungs- oder Konfigurationsinformationen;
- bekannte Vorschläge zur Behebung, falls vorhanden.

Bitte sende keine privaten Schlüssel, Zugangsdaten, Produktionszertifikate, unnötigen personenbezogenen Daten oder sonstige nicht erforderliche vertrauliche Informationen. Falls sensibles Begleitmaterial notwendig ist, beschreibe zunächst, was vorliegt, und stimme mit uns einen geeigneten Übertragungsweg ab.

## Koordinierte Offenlegung

Wir bevorzugen Coordinated Disclosure. Nach Eingang einer Meldung prüfen wir den Sachverhalt und stimmen die weitere Kommunikation mit der meldenden Person ab. Wird eine Schwachstelle bestätigt, sollen Informationen zur Behebung nach Möglichkeit vor oder gemeinsam mit der öffentlichen Offenlegung verfügbar sein.

In der aktuellen Projektphase verspricht nıu.cp keine festen Reaktions- oder Behebungsfristen. Mit zunehmender Reife der Implementierungen und einer breiteren Maintainer- und Security-Struktur kann der Prozess weiter formalisiert werden.

Bitte räume angemessene Zeit für Prüfung und Behebung ein, bevor eine Schwachstelle öffentlich gemacht wird, insbesondere wenn Geräteidentität, Provisioning, Firmware-Signing, Trust-Infrastruktur oder bereits eingesetzte Systeme betroffen sein können.

## Geltungsbereich

Security-Meldungen können unter anderem betreffen:

- Architektur- oder Spezifikationsfehler, die zu ausnutzbaren Implementierungen führen können;
- Geräteidentität und Ownership;
- Provisioning und Enrollment;
- Authentisierung und Autorisierung;
- Trust Domains, PKI, Zertifikate und Schlüsselverwaltung;
- Firmware-Signing, Verified Boot, OTA, Rollback und Recovery;
- Netzwerk- und Intercom-Security;
- Factory Provisioning und Lifecycle-Übergänge;
- Schwachstellen in vom Projekt gepflegten nıu.cp-Implementierungen.

Allgemeine Diskussionen über Security-Design, die **keine** ausnutzbare Schwachstelle oder sensible Betriebsinformationen offenlegen, können als Teil der normalen Architekturarbeit öffentlich stattfinden.

## Secrets und Betriebsinformationen

Zugangsdaten, private Schlüssel, Produktionszertifikate, WLAN-Passwörter, Access Tokens oder vergleichbare Betriebsgeheimnisse dürfen nicht in Repository, Issues oder Pull Requests eingestellt werden.

Die offene nıu.cp-Architektur ist bewusst von nıu-kontrollierten Trust Roots und privaten Betriebsschlüsseln getrennt. Open Source und offene Spezifikationen gewähren Implementierungsfreiheit; sie verlangen nicht die Offenlegung privaten Trust-Materials.

## Komponenten Dritter

Liegt eine Schwachstelle ausschließlich in einer Upstream-Komponente eines Drittprojekts, kann eine Meldung über dessen etablierten Security-Kanal sinnvoll sein. Betrifft das Problem jedoch die Art, wie nıu.cp diese Komponente verwendet, integriert, konfiguriert oder spezifiziert, melde bitte zusätzlich die Auswirkungen auf nıu.cp an **security@niuversum.de**.

## Security Research in gutem Glauben

Security Research in gutem Glauben und verantwortungsvolle Meldungen sind willkommen. Greife nicht absichtlich auf Daten oder Systeme zu, für die keine Berechtigung besteht, störe keine Produktivdienste und lege keine Daten Dritter offen, um eine Schwachstelle nachzuweisen.

Diese Richtlinie kann weiterentwickelt werden, wenn nıu.cp von Architektur und Prototyping zu produktiven Implementierungen und externer Standardisierungsbeteiligung übergeht.
