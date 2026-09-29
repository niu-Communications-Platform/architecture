# P0 Architecture Gate

[Deutsch — canonical](p0-architecture-gate.md) | **English**

**Status:** OPEN  
**Goal:** Sufficient certainty for Prototype 1 without pretending that a complete product freeze has been reached.

## To be sufficiently defined before P0

- SBC/carrier base architecture
- power path and shutdown control
- USB topology and external host port
- audio/TDM base architecture
- GPIO/bus reserves and test points
- secure element and carrier NVM
- factory/device identity
- factory/recovery principles
- central software component boundaries
- mechanical and electrical battery replacement by the end user
- fast field battery replacement without a hot-swap requirement
- hard-power-loss tolerance for storage, configuration, and OTA
- repairability granularity and decision on mechanically stressed I/O daughterboards

## To be validated in practice

- [ ] Radxa ZERO 3W + 2× TLV320AIC3204 on a shared TDM bus
- [ ] SPI control of both AIC3204 devices under Linux ASoC
- [ ] at least 4 independent capture/playback channels and correct slot mapping
- [ ] digital speaker amplifier (TAS2505 or alternative) on TDM
- [ ] jack detection and automatic CTIA/OMTP switching
- [ ] USB-C DFP + hub + VBUS protection under real load
- [ ] parallel USB Audio + USB Ethernet/Wi-Fi
- [ ] network handover with measurement of intercom interruption
- [ ] review international radio standards and regulations for all intended target markets, in particular permitted frequency ranges, transmit power, duty-cycle/channel-access rules, regional variants, and implications for Wi-Fi, Bluetooth, and a possible sub-GHz/LoRa resilience channel
- [ ] validate RF coexistence, antenna spacing, and mutual interference between Wi-Fi, Bluetooth, and possible sub-GHz radio in practice
- [ ] power path / battery care / thermals / runtime
- [ ] end user can safely remove and replace the complete battery within a few seconds
- [ ] battery replacement requires neither soldering nor heat/solvents and does not damage device/battery
- [ ] battery removal without prior shutdown is permitted and results in a consistent system on the next boot
- [ ] repeated automated hard-power-cut cycles during normal operation without permanent corruption
- [ ] targeted power cuts during persistent configuration changes with consistent recovery
- [ ] power cuts during critical OTA phases; A/B system remains bootable and rollback-capable
- [ ] compatible replacement battery works without software pairing or artificial restriction
- [ ] battery health/learning state behaves correctly after battery replacement
- [ ] mechanical decision on replaceable I/O/connector boards completed
- [ ] ATECC608C TrustFLEX profile, KeyProvider, and lock policy
- [ ] A/B OTA, READY marking, and automatic rollback
- [ ] RK3566 Maskrom recovery
- [ ] PTT latency and audio quality
- [ ] internal speaker/microphone behaviour without unacceptable feedback
- [ ] display/button/LED UX in the physical prototype

## Not P0-blocking yet

- complete cloud scaling architecture
- complete manufacturing SOPs
- detailed RMA work instructions
- complete certification test plan
- final developer-mode/custom-trust UX
- final selection of every passive component

## Gate criterion

P0 is reached when the remaining uncertainties are no longer highly likely to force Prototype 1 into an avoidable carrier/PCB redesign and the remaining candidates have a clear validation plan.
