---
language: en
canonical: false
status: accepted
date: 2026-09-07
source: ../../de/0005-end-user-replaceable-battery.md
translation_status: current
---

# ADR-0005: The battery is replaceable by the end user

## Status

**ACCEPTED**

## Context

The beltpack is a portable, battery-powered product intended for commercial distribution in the European Union. Article 11 of Regulation (EU) 2023/1542 applies from 18 February 2027 and generally requires portable batteries incorporated into appliances to be readily removable and replaceable by the end user throughout the lifetime of the product.

Under Article 11, a battery is considered readily removable in particular where it can be removed with commercially available tools and where neither manufacturer-specific tools, heat energy nor solvents are required for disassembly. Specialised tools are only acceptable where they are supplied free of charge with the product. The beltpack architecture will not rely on a statutory exemption from end-user replaceability.

The Regulation also requires instructions and safety information for removal and replacement, their permanent public availability online, availability of compatible replacement batteries for at least five years after the last unit of the appliance model has been placed on the market, and prohibits software from making the replacement of compatible batteries more difficult.

Legal basis: Regulation (EU) 2023/1542, in particular Articles 11 and 96. The current guidance and delegated acts of the European Commission must also be taken into account.

## Decision

The complete beltpack battery will be designed as an **End-User Replaceable Unit**.

The production product must therefore meet at least the following architectural conditions:

- no soldering is required for battery replacement,
- no adhesive whose removal requires heat or solvents,
- access using commercially available tools; no manufacturer-specific tools,
- a polarity-safe and mechanically suitable connector,
- safe removal and installation without damaging the device or battery when performed as intended,
- a compatible replacement battery must not impair the function, performance or safety of the device,
- no software pairing or other software mechanism that makes compatible battery replacement more difficult,
- Battery Health / Learning State must be capable of being sensibly reinitialised after battery replacement,
- clear replacement and safety instructions are supplied with the product and kept permanently available online,
- the spare-parts strategy accounts for the legally required minimum availability period after the appliance model is no longer placed on the market.

A tool-free battery door is not mandatory. A screwed enclosure is acceptable provided that an end user can readily and safely access and replace the battery using commercially available tools.

## Rationale

The decision not only addresses an expected EU compliance requirement but also directly supports the product goals of longevity, repairability and resource conservation. The battery is an expected wear component and must therefore not determine the lifetime of the complete beltpack.

## Consequences

- Battery geometry, retention, connector and enclosure access are P0-relevant hardware requirements.
- The battery must not be designed as a permanently integrated part of the carrier.
- Power Path, Fuel Gauge and software must tolerate a physical battery replacement.
- The mechanical design must demonstrate replaceability before enclosure/PCB freeze.
- Documentation and spare-parts strategy are part of product compliance.

## To be validated

Before mechanical design freeze, the final prototype must be tested and documented to demonstrate that an end user can safely remove and replace the battery with a compatible battery in accordance with Article 11 of Regulation (EU) 2023/1542 and without prohibited tools or methods.
