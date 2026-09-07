# Compute Module and Production Configuration

[Deutsch — canonical](../../de/20-hardware/compute-module.md) | **English**

> The German version is canonical. This document is a maintained English translation.

## Purpose

This document refines requirements for the beltpack's replaceable compute module and the target Radxa ZERO 3W configuration.

## Architecture

**DECIDED:** The compute module is not the Device Identity anchor. The Carrier carries Device Identity; the compute module is replaceable compute, storage, and networking hardware.

**CANDIDATE:** The RK3566-based Radxa ZERO 3W remains the preferred production candidate. Raspberry Pi Zero 2 W/WH remains a development platform, not the preferred production base.

## Official configurations

Radxa currently documents ZERO 3W options with 1/2/4/8 GB LPDDR4 and 0/8/16/32/64 GB onboard eMMC. The manufacturer states minimum ZERO 3W availability through September 2033.

## Target configuration

**CANDIDATE:** **2 GB LPDDR4 + 16 GB onboard eMMC** is the preferred baseline for Prototype 1 and production economics evaluation.

Rationale:

- 1 GB may be sufficient for today's core workload but leaves limited reserve for PipeWire, Talkkonnect/Mumble, Device Agent, network management, UI, diagnostics, OTA/recovery, and future software;
- 4 GB currently appears unnecessary for the known beltpack workload and would add cost and potentially power without clear product value;
- 8 GB eMMC is unnecessarily tight for a long-lived Linux product with A/B system, recovery, logs, diagnostics, and update reserve;
- 16 GB provides materially more layout/update/recovery headroom without jumping to the likely unnecessary 32 GB class;
- extra storage does not remove the requirement to minimize writes and validate hard-power-loss tolerance.

This is not yet a production release. Prototype 1 must measure real RAM usage, storage occupancy, update slots, boot/recovery behavior, power, and thermals.

## GPIO header

**TARGET:** Production should prefer the ZERO 3W variant **without a pre-soldered 40-pin header** where the final Carrier interface permits it. An unnecessary maker header consumes material, height, and space.

The final ZERO 3W-to-Carrier connection must be serviceable, repeatable, and suitable for series assembly rather than being dictated solely by the development-board header.

## Storage rules

- onboard eMMC is normal runtime storage;
- microSD is not a production runtime medium;
- microSD may be used for development/service where mechanically useful;
- Device Identity and non-reconstructable factory data must not live only on eMMC;
- A/B OTA, rollback, and recovery must tolerate abrupt power loss;
- logs and high-frequency writes are constrained;
- eMMC endurance/storage grade of the concrete production SKU must be clarified with Radxa before release.

## Cost gate

Current Compute budget is **EUR 18–22 per unit** in target series volumes.

**REVIEW:** If 2 GB + 16 GB eMMC materially exceeds this budget in real 1k/5k/10k quotations, RAM or storage shall not be reduced automatically. OEM pricing, configuration alternatives, and actual product value are reviewed first.

A cheaper 1 GB/8 GB configuration is acceptable only if prototype measurements demonstrate adequate reserve and A/B/recovery requirements remain unconstrained.

## Prototype 1 measurements

At minimum measure RAM after boot; RAM with full service stack; peak RAM during network switching/audio/UI/diagnostics/OTA; base-system eMMC occupancy; A/B slot and recovery reserve; log/persistence growth; boot/recovery time; idle/listening/TX/RX/heavy-load power; target-enclosure thermals; and repeated hard power loss including cuts during OTA/config writes.

## Decision rule

> **Compute is optimized for sufficient product headroom, not maximum specification and not minimum purchase price.**

The smallest configuration that carries the complete beltpack stack, A/B OTA, recovery, and realistic future software development with credible reserve wins.

## Sources

- Radxa ZERO 3W product and documentation: https://radxa.com/products/zeros/zero3w/ and https://docs.radxa.com/en/zero/zero3
- Radxa ZERO 3W Product Brief: manufacturer SKU configuration and minimum-availability information through September 2033.
