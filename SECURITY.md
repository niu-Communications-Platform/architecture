# Security Policy

**English (public entry language)** | [Deutsch — canonical](SECURITY.de.md)

Security is part of the nıu.cp architecture, particularly around device identity, provisioning, trust domains, firmware authenticity, update/recovery mechanisms, and service credentials.

## Reporting a vulnerability

Please **do not report exploitable security vulnerabilities through public GitHub issues, pull requests, discussions, or other public project channels**.

Report security vulnerabilities confidentially by email to:

**security@niuversum.de**

This reporting channel is intentionally independent of the repository hosting platform so that it remains stable if nıu.cp moves away from GitHub.

## What to include

Please include, where reasonably possible:

- the affected component, document, implementation, or version;
- a clear description of the vulnerability;
- reproduction steps or a minimal proof of concept;
- the expected and observed behaviour;
- the potential security impact;
- relevant environment or configuration details;
- any suggested mitigation, if known.

Please avoid sending private keys, credentials, production certificates, unnecessary personal data, or unrelated confidential information. If sensitive supporting material is necessary, first describe what you have and coordinate an appropriate transfer method with us.

## Coordinated disclosure

We favour coordinated disclosure. After receiving a report, we will assess the issue and coordinate further communication with the reporter. Where a vulnerability is confirmed, we aim to make remediation information available before or together with public disclosure where practical.

At the current project stage, nıu.cp does not promise fixed response or remediation deadlines. The reporting process may become more formal as implementations mature and the project develops a broader maintainer and security structure.

Please allow reasonable time for assessment and remediation before public disclosure, especially where device identity, provisioning, firmware signing, trust infrastructure, or deployed systems may be affected.

## Scope

Security reports may concern, among other things:

- architecture or specification flaws that could create exploitable implementations;
- device identity and ownership;
- provisioning and enrollment;
- authentication and authorization;
- trust domains, PKI, certificates, and key handling;
- firmware signing, verified boot, OTA, rollback, and recovery;
- network and intercom security;
- factory provisioning and lifecycle transitions;
- vulnerabilities in nıu.cp implementations maintained by the project.

General security design discussion that does **not** disclose an exploitable vulnerability or sensitive operational information may take place publicly as part of normal architecture work.

## Secrets and operational material

Do not submit credentials, private keys, production certificates, Wi-Fi passwords, access tokens, or comparable operational secrets to the repository, issues, or pull requests.

The open nıu.cp architecture is deliberately separated from nıu-controlled trust roots and private operational keys. Open source and open specifications grant implementation freedom; they do not require disclosure of private trust material.

## Third-party components

If a vulnerability exists solely in an upstream third-party component, reporting it to that project's established security channel may be appropriate. If the issue affects how nıu.cp uses, integrates, configures, or specifies that component, please also report the nıu.cp impact to **security@niuversum.de**.

## Good-faith research

Good-faith security research and responsible reporting are welcome. Do not intentionally access data or systems for which you do not have authorization, disrupt production services, or expose third-party data in order to demonstrate a vulnerability.

This policy may evolve as nıu.cp moves from architecture and prototyping toward production implementations and external standardisation participation.
