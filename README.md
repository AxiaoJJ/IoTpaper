# Linux-based IoT Firmware Security Papers

![Awesome](https://awesome.re/badge.svg) ![Papers](https://img.shields.io/badge/papers-12-blue) ![Last Updated](https://img.shields.io/badge/updated-2026--09-green) ![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen)

A curated list of security research on **Linux-based IoT and embedded firmware**.
It covers static and taint analysis, fuzzing, emulation, and rehosting where the
paper explicitly targets Linux-based device firmware, IoT devices, routers, or
embedded Linux applications.

## Scope

Included papers must clearly concern Linux-based IoT or embedded firmware.
Bare-metal/RTOS/UEFI research, generic protocol security, generic IoT studies,
and non-Linux embedded systems are intentionally out of scope. See
[CONTRIBUTING.md](CONTRIBUTING.md) for submission criteria.

## Overview

**12 papers** indexed.

| Venue | 2023 | 2024 | 2025 | 2026 | Total |
|---|---:|---:|---:|---:|---:|
| IEEE S&P | – | – | 1 | 1 | **2** |
| USENIX Security | 1 | 1 | 1 | 1 | **4** |
| NDSS | – | 1 | – | 2 | **3** |
| AI/SE Top (ISSTA) | 1 | – | – | – | **1** |
| Other (journal / IPCCC) | – | – | 1 | – | **2** |

## Categories

[01. Static Analysis](#01-static-analysis) ·
[02. Dynamic Analysis — Fuzzing](#02-dynamic-analysis--fuzzing) ·
[03. Rehosting & Emulation](#03-rehosting--emulation)

## 01. Static Analysis

Static taint, binary, and vulnerability analysis for Linux-based IoT firmware.

- [Bridge: High-Order Taint Vulnerabilities Detection in Linux-based IoT Firmware](01-static-analysis-traditional/Bridge_IEEE_S%26P.pdf) (Bridge, IEEE S&P 2026)
- [FirmCross: Detecting Taint-style Vulnerabilities in Modern C-Lua Hybrid Web Services of Linux-based Firmware](https://www.ndss-symposium.org/ndss-paper/firmcross-detecting-taint-style-vulnerabilities-in-modern-c-lua-hybrid-web-services-of-linux-based-firmware/) (FirmCross, NDSS 2026)
- [FirmPass: Identifying Broken Password Management in Linux-Based IoT Firmware Through Query-Driven Approaches](01-static-analysis-traditional/FirmPass_Identifying_Broken_Password_Management_in_Linux-Based_IoT_Firmware_Through_Query-Driven_Approaches.pdf) (FirmPass, IEEE Internet of Things Journal 2025)
- [Faster and Better: Detecting Vulnerabilities in Linux-based IoT Firmware with Optimized Reaching Definition Analysis](01-static-analysis-traditional/2024-Faster%20and%20Better%20Detecting%20Vulnerabilities%20in.pdf) (HermeScan, NDSS 2024)
- [Detecting Vulnerabilities in Linux-Based Embedded Firmware with SSE-Based On-Demand Alias Analysis](01-static-analysis-traditional/23-Detecting%20Vulnerabilities%20in%20Linux-Based%20Embedded%20Firmware%20with%20SSE-Based%20On-Demand%20Alias%20Analysis.pdf) (EmTaint, ISSTA 2023)

## 02. Dynamic Analysis — Fuzzing

Fuzzing and dynamic testing of Linux-based IoT firmware and embedded applications.

- [Bond: Constraint-Directed Fuzzing for Automated Validation of Taint Analysis Results in Linux-based IoT Firmware](03-dynamic-analysis-fuzzing/Bond_USENIX_Security.pdf) (Bond, USENIX Security 2026)
- [HouseFuzz: Service-Aware Grey-Box Fuzzing for Vulnerability Detection in Linux-Based Firmware](03-dynamic-analysis-fuzzing/HouseFuzz%20Service-Aware%20Grey-Box%20Fuzzing%20for%20Vulnerability%20Detection%20in%20Linux-Based%20Firmware.pdf) (HouseFuzz, IEEE S&P 2025)
- [LEMIX: Enabling Testing of Embedded Applications as Linux Applications](https://www.usenix.org/conference/usenixsecurity25/presentation/tanksalkar) (LEMIX, USENIX Security 2025)
- [Greenhouse: Single-Service Rehosting of Linux-Based Firmware Binaries in User-Space Emulation](03-dynamic-analysis-fuzzing/23-greenhouse%20appendix-tay.pdf) (Greenhouse, USENIX Security 2023)
- [An Efficient Greybox Fuzzing Scheme for Linux-based IoT Programs Through Binary Static Analysis](03-dynamic-analysis-fuzzing/19-An%20efficient%20greybox%20fuzzing%20scheme%20for%20linux-based%20IoT%20programs%20through%20binary%20static%20analysis..pdf) (IEEE IPCCC 2019)

## 03. Rehosting & Emulation

Rehosting and emulation techniques for Linux-based firmware binaries.

- [User-Space Dependency-Aware Rehosting for Linux-Based Firmware Binaries](https://www.ndss-symposium.org/ndss-paper/user-space-dependency-aware-rehosting-for-linux-based-firmware-binaries/) (NDSS 2026)
- [Pandawan: Quantifying Progress in Linux-based Firmware Rehosting](https://www.usenix.org/conference/usenixsecurity24/presentation/angelakopoulos) (Pandawan, USENIX Security 2024)
