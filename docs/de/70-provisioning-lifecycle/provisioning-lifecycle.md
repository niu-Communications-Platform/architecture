---
language: de
canonical: true
status: current
last_reviewed: 2026-09-07
---

# Provisioning, Ownership und Lifecycle

## Grundsatz

Factory Identity, Ownership, Provisioned Identity und Service Identities sind getrennte Ebenen.

Ein factory-neues Gerät besitzt Device Identity, aber noch keinen Besitzer, Friendly Name, Rolle, Netzwerk- oder Serviceaccount.

## Enrollment

Der Zielablauf umfasst:

1. Discovery
2. kryptographische Geräteauthentisierung
3. physischen Claim-Nachweis
4. Admin-Autorisierung
5. Owner-/Deployment-Bindung
6. Capability-Prüfung
7. Erzeugung von Servicekeys/Zertifikaten
8. signiertes deklaratives Provisioning Document
9. transaktionales Anwenden, Health Check und Commit/Rollback

Provisioning-Dokumente enthalten u. a. Ziel-UUID, Schema-/Config-Revision, Name, Profile, Netzwerk, Intercom, Audio und Systemparameter. Das Gerät prüft Signer/Trust Domain, Ziel-UUID, Schema, Capabilities und Revision.

## Zustände

Zielzustände:

`MANUFACTURED → UNCLAIMED → DISCOVERED → AUTHENTICATED → CLAIMED → PROVISIONED → READY`

Zusätzlich sind Fehler-/Degraded-/Offline-/Blocked-/Released-/Retired-Zustände vorgesehen.

## Reset und Ownership

Factory Reset löscht niemals UUID, Seriennummer oder Device Root Key.

- Soft Reset → Benutzereinstellungen
- Config Reset → Netzwerk/Mumble/Profile/Friendly Name, Root Identity bleibt
- Ownership Release → Owner-/Servicebindung entfernen bzw. widerrufen; Rückkehr zu `UNCLAIMED`

## Replace Device

Bei Carrier-Ersatz entsteht eine neue Factory Identity. Friendly Identity, Rolle, Profile, Netzwerk-/Audio-/Intercom-Zuordnung können kontrolliert auf das Ersatzgerät übertragen werden. Neue Servicekeys und Zertifikate werden erzeugt; das alte Gerät wird im Registry als replaced/blocked markiert.

Grundsatz:

**Factory Identity immutable. Provisioned Identity transferable. Service Identities rotatable. Runtime Identity ephemeral.**
