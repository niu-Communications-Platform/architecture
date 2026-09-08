# Power Topology: Consolidation and Series Optimization

[Deutsch — canonical](../../de/20-hardware/power-topology-optimization.md) | **English**

> The German version is canonical. This document is a maintained English translation.

## Purpose

This document checks whether the current Prototype-1 architecture

```text
PD Sink → Buck-Boost Charger / Power Path → Battery/System Node → dedicated 5-V regulator → 5V_SYS
```

contains unnecessary conversion stages for series production, or whether the apparently redundant blocks are still the most robust system solution.

The Battery Pack/BMS responsibility boundary remains unchanged: pack safety and cell management belong to the production battery pack; the Carrier owns only system power and specification-compliant charging integration.

## Starting point

The beltpack requires a preferred 1S Prototype-1 direction, robust `5V_SYS` for compute/audio, ACCESSORY USB-C around 5 V / 1 A, operation with or without battery on external power, USB-C PD for full-load-plus-charge headroom, graceful behavior with weak sources, abrupt battery removal tolerance, a EUR 8–11 Power+USB target, and strong audio/EMI performance.

## BQ25798-specific finding

BQ25798 exposes two relevant power nodes:

- `SYS` largely tracks battery voltage above `VSYSMIN`, so with 1S it is **not a fixed 5-V rail**;
- `PMID` roughly follows input voltage in forward mode and can be regulated from the battery in backup/OTG mode.

Therefore BQ25798 can in principle generate a regulated 5-V backup rail from a 1S battery, but it cannot simply be treated as one universal fixed 5-V system output in all operating modes. With a 9-V PD input, `PMID` is approximately 9 V in forward mode.

**Consequence:** the dedicated 5-V regulation stage is not present merely because of a misunderstanding.

## Variant A — current architecture: SYS → dedicated 5V_SYS boost

Advantages: one defined `5V_SYS` behavior in all modes; compute/audio decoupled from source mode; 5/9/12-V external inputs do not change system rail; charger power-path and battery supplement remain usable; clear, measurable functional blocks; fewer rail-mode transitions; strong Prototype-1 debugging/thermal/EMI characteristics.

Disadvantages: external PD power may be converted down toward the battery/system domain and then back up to 5 V, adding stationary conversion loss, regulator BOM, inductor, passives, area and cost.

## Variant B — use PMID directly as 5-V system rail

This looks attractive because BQ25798 can regulate PMID to 5 V from the battery in backup mode and PMID is also near 5 V with a 5-V input.

It is not preferred for the current target because a 9-V PD input makes PMID approximately 9 V in forward mode; limiting PD to 5 V removes much of the simultaneous load/charge headroom; backup mode requires defined host/re-arm behavior; and the system rail becomes more dependent on charger operating mode.

## Variant C — external 5-V path on adapter, boost only on battery

```text
                  ┌─ Buck 9V→5V ──────────┐
USB-C PD ─────────┤                        ├─ ideal power mux / OR → 5V_SYS
                  └─ Charger → Battery ─ Boost 1S→5V ─┘
```

Potential advantages are better stationary efficiency, lower charger/battery-path losses on adapter power, independent charging, and a battery boost that need not carry normal external-power operation.

Costs are an additional buck stage, mux/ideal-diode/ORing logic, more complex seamless switching and transients, more FETs/controllers/protection paths, more failure modes/EOL cases, and higher layout complexity. It may consume the expected savings elsewhere.

**Assessment:** interesting for series optimization, not automatically cheaper or simpler.

## Variant D — one true system buck-boost behind a suitable power path

Theoretically attractive, but one regulator alone does not replace charging and power-path functions. A suitable source mux or charger/system-node architecture is still required.

**Assessment:** revisit after real load/efficiency measurements; no present evidence that total BOM, area and complexity actually decrease.

## Current conclusion

**CANDIDATE / PREFERRED FOR PROTOTYPE 1:** keep the existing three functional blocks:

```text
PD Controller
    ↓
Buck-Boost Charger / NVDC Power Path
    ↔ production Battery Pack
    ↓
dedicated regulated 5V stage
    ↓
5V_SYS
```

The reason is measurement clarity and consistent product behavior, not conservatism.

Prototype 1 shall determine the real external-PD double-conversion loss, actual stationary-duty share, charger/5-V-regulator thermal load, true series cost of the dedicated 5-V stage, whether buck+boost+mux is really cheaper in total, and whether additional mode switching introduces audio/EMI/reliability penalties.

## Post-Prototype optimization gate

A more complex dual-path/bypass architecture is introduced only if measurements show at least two meaningful advantages without hurting P0 requirements: roughly EUR 1 or more real series BOM savings; relevant PCB-area reduction; significantly better stationary efficiency; meaningful thermal relief; lower part count/higher reliability; or better sourcing/second-source position.

A merely theoretically more elegant schematic is insufficient.

## Architecture rule

> **Minimize power stages only when the complete system becomes simpler. Fewer converter blocks are not a goal by themselves.**

And for this beltpack:

> **A single stable 5V_SYS behavior across battery, weak USB-C and PD operation is more valuable than saving one converter on paper.**

## Series direction

No final series choice yet. Prototype 1 builds and measures the current three-block topology. In parallel, current boost alternatives and dual-path/power-mux solutions remain under observation. Only after measured mobile and stationary efficiency curves are available is the series topology frozen.
