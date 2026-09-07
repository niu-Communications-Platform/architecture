# ADR-0001: Der Carrier ist der Anker der physischen Geräteidentität

**Status:** Accepted  
**Datum:** 2026-09-07

## Kontext

SBC, eMMC/Storage und Software müssen im Feld austauschbar bzw. wiederherstellbar sein, ohne dass ein Beltpack dadurch administrativ zu einem neuen physischen Gerät wird. Gleichzeitig darf ein geklonter Datenträger keine Geräteidentität duplizieren können.

## Entscheidung

Die unveränderliche Factory/Device Identity wird an den Carrier gebunden. Der Carrier enthält Secure Element und Carrier-NVM und wird im Factory Registry mit Device UUID und Seriennummer verknüpft.

Ein SBC- oder Storage-Tausch erhält die Factory Identity. Ein Carrier-Tausch erzeugt eine neue Factory Identity.

## Begründung

Der Carrier ist die langlebige physische Einheit des Produkts, während Compute und Storage Service-/Verschleißkomponenten sein können. Die Trennung ermöglicht Reparatur, Reimaging und Zero-Touch-Recovery ohne Identitätsverlust und verhindert Identitätsklone allein durch Kopieren von Storage.

## Konsequenzen

- Secure Element und Carrier-NVM sind V1-Hardwarebestandteile.
- Provisioning und Base/Cloud adressieren Geräte primär über Device UUID/Registry, nicht über IP/MAC.
- RMA benötigt einen expliziten Replace-Device-Prozess für Carrier-Tausch.
- Friendly/Provisioned Identity muss von Factory Identity getrennt bleiben.

## Validierungsbedarf

Konkrete Secure-Element-/EEPROM-Bauteile und deren Factory-Provisioning-/Lock-Prozess müssen praktisch validiert werden.
