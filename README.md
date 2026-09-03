# IoT Firmware Security Papers

![Awesome](https://awesome.re/badge.svg) ![Papers](https://img.shields.io/badge/papers-90-blue) ![Last Updated](https://img.shields.io/badge/updated-2026--09-green) ![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen)

A curated collection of security research focused on **IoT and embedded firmware vulnerability analysis**. It covers static and taint analysis, binary analysis, fuzzing, symbolic execution, firmware rehosting/emulation, LLM-assisted analysis, and firmware-focused measurement.

## Scope

Included work must analyze device firmware, firmware binaries/services, embedded software, or techniques directly used for firmware vulnerability discovery. Linux-based firmware is central, while broadly reusable MCU/RTOS firmware-analysis techniques are also included.

Excluded topics include PLC/ICS-only research, cellular baseband, UEFI, automotive/UAV/satellite systems, protocol-only BLE/Zigbee/MQTT/Wi-Fi work, honeypots, and generic IoT privacy/compliance/market studies.

## Overview

**90 papers** indexed across six focused categories.

## Categories

[01. Static & Taint Analysis](#01-static--taint-analysis) ·
[02. LLM-Assisted Firmware Analysis](#02-llm-assisted-firmware-analysis) ·
[03. Firmware Fuzzing & Dynamic Testing](#03-firmware-fuzzing--dynamic-testing) ·
[04. Symbolic Execution, Rehosting & Emulation](#04-symbolic-execution-rehosting--emulation) ·
[05. Surveys, Taxonomies & Corpora](#05-surveys-taxonomies--corpora) ·
[06. Firmware Measurement Studies](#06-firmware-measurement-studies)

## 01. Static & Taint Analysis

Static taint, binary, data-flow, recurring-vulnerability, update, and authentication-bypass analysis for IoT/embedded firmware.

- [Bridge: High-Order Taint Vulnerabilities Detection in Linux-based IoT Firmware](01-static-analysis-traditional/Bridge_IEEE_S%26P.pdf) (Bridge, IEEE S&P 2026)
- [FirmCross: Detecting Taint-style Vulnerabilities in Modern C-Lua Hybrid Web Services of Linux-based Firmware](https://www.ndss-symposium.org/ndss-paper/firmcross-detecting-taint-style-vulnerabilities-in-modern-c-lua-hybrid-web-services-of-linux-based-firmware/) (FirmCross, NDSS 2026)
- [IoTBec: An Accurate and Efficient Recurring Vulnerability Detection Framework for Black Box IoT devices](01-static-analysis-traditional/IoTBec%20An%20Accurate%20and%20Efficient%20Recurring%20Vulnerability%20Detection%20Framework%20for%20Black%20Box%20IoT%20devices.pdf) (IoTBec, NDSS 2026)
- [A Comprehensive Memory Safety Analysis of Bootloaders](https://www.ndss-symposium.org/ndss-paper/a-comprehensive-memory-safety-analysis-of-bootloaders/) (NDSS 2025)
- [FirmPass: Identifying Broken Password Management in Linux-Based IoT Firmware Through Query-Driven Approaches](01-static-analysis-traditional/FirmPass_Identifying_Broken_Password_Management_in_Linux-Based_IoT_Firmware_Through_Query-Driven_Approaches.pdf) (FirmPass, IEEE Internet of Things Journal 2025)
- [From Constraints to Cracks: Constraint Semantic Inconsistencies as Vulnerability Beacons for Embedded Systems](01-static-analysis-traditional/From%20Constraints%20to%20Crack%20Constraint%20Semantic%20Inconsistencies%20as%20Vulnerability%20Beacons%20for%20Embedded%20Systems.pdf) (NUWA, USENIX Security 2025)
- [Kintsugi: Secure Hotpatching for Code-Shadowing Real-Time Embedded Systems](https://www.usenix.org/conference/usenixsecurity25/presentation/mackensen) (Kintsugi, USENIX Security 2025)
- [AutoFirm: Automatically Identifying Reused Libraries inside IoT Firmware at Large-Scale](01-static-analysis-traditional/AutoFirm%20Automatically%20Identifying%20Reused%20Libraries%20inside%20IoT%20Firmware%20at%20Large-Scale.pdf) (AutoFirm, arXiv preprint (no confirmed venue) 2024)
- [Faster and Better: Detecting Vulnerabilities in Linux-based IoT Firmware with Optimized Reaching Definition Analysis](01-static-analysis-traditional/2024-Faster%20and%20Better%20Detecting%20Vulnerabilities%20in.pdf) (HermeScan, NDSS 2024)
- [FITS: Inferring Intermediate Taint Sources for Effective Vulnerability Analysis of IoT Device Firmware](01-static-analysis-traditional/FITS%20Inferring%20Intermediate%20Taint%20Sources%20for%20Effective%20Vulnerability%20Analysis%20of%20IoT%20Device%20Firmware.pdf) (FITS, ASPLOS 2024)
- [Leveraging Semantic Relations in Code and Data to Enhance Taint Analysis of Embedded Systems](https://www.usenix.org/conference/usenixsecurity24/presentation/zhao) (USENIX Security 2024)
- [LuaTaint: A Static Analysis System for Web Configuration Interface Vulnerability of Internet of Things Devices](01-static-analysis-traditional/23-LuaTaint%20A%20Static%20Taint%20Analysis%20System%20for%20Web.pdf) (LuaTaint, IEEE Internet of Things Journal 2024)
- [OctopusTaint: Advanced Data Flow Analysis for Detecting Taint-Based Vulnerabilities in IoT/IIoT Firmware](01-static-analysis-traditional/OctopusTaint_Advanced%20Data%20Flow%20Analysis%20for%20Detecting%20taint-based%20vulnerabilities%20in%20iot%20firmware.pdf) (OctopusTaint, ACM CCS 2024)
- [Operation Mango: Scalable Discovery of Taint-Style Vulnerabilities in Binary Firmware Services](01-static-analysis-traditional/2024%20-%20USENIX%20Security%20-%20Mango.pdf) (Mango, USENIX Security 2024)
- [SaTC: Shared-Keyword Aware Taint Checking for Detecting Bugs in Embedded Systems](https://doi.org/10.1109/TDSC.2023.3307430) (SaTC, IEEE TDSC 2024)
- [Your Firmware Has Arrived: A Study of Firmware Update Vulnerabilities](01-static-analysis-traditional/sec24-Your%20Firmware%20Has%20Arrived-A%20Study%20of%20Firmware%20Update%20Vulnerabilities.pdf) (ChkUp, USENIX Security 2024)
- [Detecting Vulnerabilities in Linux-Based Embedded Firmware with SSE-Based On-Demand Alias Analysis](01-static-analysis-traditional/23-Detecting%20Vulnerabilities%20in%20Linux-Based%20Embedded%20Firmware%20with%20SSE-Based%20On-Demand%20Alias%20Analysis.pdf) (EmTaint, ISSTA 2023)
- [Systematically Detecting Packet Validation Vulnerabilities in Embedded Network Stacks](https://arxiv.org/abs/2308.10965) (ASE 2023)
- [VulHawk: Cross-architecture Vulnerability Detection with Entropy-based Binary Code Search](01-static-analysis-traditional/23-VulHawk-Cross-architecture%20Vulnerability%20Detection.pdf) (VulHawk, NDSS 2023)
- [RapidPatch: Firmware Hotpatching for Real-Time Embedded Devices](01-static-analysis-traditional/sec22-RapidPatch%20Firmware%20Hotpatching%20for%20Real-Time%20Embedded%20Devices.pdf) (RapidPatch, USENIX Security 2022)
- [Sharing More and Checking Less: Leveraging Common Input Keywords to Detect Bugs in Embedded Systems](01-static-analysis-traditional/Chen%20et%20al.%20-%20Sharing%20More%20and%20Checking%20Less%20Leveraging%20Common%20Sanitizer%20Checks.pdf) (USENIX Security 2021)
- [HALucinator: Firmware Re-hosting Through Abstraction Layer Emulation](01-static-analysis-traditional/sec20-HALucinator_%20Firmware%20re-hosting%20through%20abstraction%20layer%20emulation.pdf) (HALucinator, USENIX Security 2020)
- [KARONTE: Detecting Insecure Multi-binary Interactions in Embedded Firmware](01-static-analysis-traditional/20-Karonte_Detecting_Insecure_Multi-binary_Interactions_in_Embedded_Firmware.pdf) (Karonte, IEEE S&P 2020)

## 02. LLM-Assisted Firmware Analysis

LLM-assisted code understanding, interface discovery, request generation, and fuzzing for firmware and IoT devices.

- [FalconScope: Effective and Efficient Detection of Hidden Web Interfaces in IoT Devices](https://doi.org/10.1145/3774904.3792431) (FalconScope, The Web Conference 2026)
- [FirmAgent: Leveraging Fuzzing to Assist LLM Agents with IoT Firmware Vulnerability Discovery](https://www.ndss-symposium.org/ndss-paper/firmagent-leveraging-fuzzing-to-assist-llm-agents-with-iot-firmware-vulnerability-discovery/) (FirmAgent, NDSS 2026)
- [PANGOLIN: Fuzzing Multilingual IoT Firmware with LLM-Driven Code Analysis](https://www.usenix.org/conference/usenixsecurity26/presentation/jia-zhipeng) (PANGOLIN, USENIX Security 2026)
- [EAGLEYE: Exposing Hidden Web Interfaces in IoT Devices via Routing Analysis](02-static-analysis-llm-assisted/EAGLEYE%20Exposing%20Hidden%20Web%20Interfaces%20in%20IoT%20Devices%20via%20Routing%20Analysis.pdf) (EAGLEYE, NDSS 2025)
- [Large Language Model-Powered Protected Interface Evasion: Automated Discovery of Broken Access Control Vulnerabilities in Internet of Things Devices](02-static-analysis-llm-assisted/ACBreaker.pdf) (ACBreaker, Sensors (MDPI journal) 2025)
- [Moye: A Wallbreaker for Monolithic Firmware](https://dl.acm.org/doi/10.1109/ICSE55347.2025.00053) (Moye, ICSE 2025)
- [Fuzzing BusyBox: Leveraging LLM and Crash Reuse for Embedded Bug Unearthing](02-static-analysis-llm-assisted/Fuzzing%20BusyBox%20Leveraging%20LLM%20and%20Crash%20Reuse%20for%20Embedded%20Bug%20unearth.pdf) (USENIX Security 2024)
- [LLMIF: Augmented Large Language Model for Fuzzing IoT Devices](02-static-analysis-llm-assisted/LLMIF%20Augmented%20Large%20Language%20Model%20for%20Fuzzing%20IoT%20Devices.pdf) (LLMIF, IEEE S&P 2024)

## 03. Firmware Fuzzing & Dynamic Testing

Greybox/blackbox fuzzing, dynamic testing, and feedback-guided vulnerability discovery for firmware targets.

- [Bond: Constraint-Directed Fuzzing for Automated Validation of Taint Analysis Results in Linux-based IoT Firmware](03-dynamic-analysis-fuzzing/Bond_USENIX_Security.pdf) (Bond, USENIX Security 2026)
- [Camveil: Unveiling Security Camera Vulnerabilities through Multi-Protocol Coordinated Fuzzing](https://sp2026.ieee-security.org/accepted-papers.html) (Camveil, IEEE S&P 2026)
- [FirmReBugger: A Benchmark Framework for Monolithic Firmware Fuzzers](https://www.usenix.org/conference/usenixsecurity26/presentation/duong) (FirmReBugger, USENIX Security 2026)
- [RTCON: Context-Adaptive Function-Level Fuzzing for RTOS Kernels](https://www.ndss-symposium.org/ndss-paper/rtcon-context-adaptive-function-level-fuzzing-for-rtos-kernels/) (RTCON, NDSS 2026)
- [Stop Starving or Stuffing Me: Boosting Firmware Fuzzing Efficiency with On-demand Input Delivery](https://arxiv.org/pdf/2605.16798) (IEEE S&P 2026)
- [Through the Authentication Maze: Detecting Authentication Bypass Vulnerabilities in Firmware Binaries](03-dynamic-analysis-fuzzing/Through%20the%20Authentication%20Maze%20Detecting%20Authentication%20Bypass%20Vulnerabilities%20in%20Firmware%20Binaries.pdf) (AuthSpark, NDSS 2026)
- [AidFuzzer: Adaptive Interrupt-Driven Firmware Fuzzing via Run-Time State Recognition](03-dynamic-analysis-fuzzing/AidFuzzer%20Adaptive%20Interrupt-Driven%20Firmware%20Fuzzing%20via%20Run-Time%20State%20Recognition.pdf) (AidFuzzer, USENIX Security 2025)
- [DRIFT: Debug-based Trace Inference for Firmware Testing](https://ieeexplore.ieee.org/document/11334624) (DRIFT, ASE 2025)
- [FirmRCA: Towards Post-Fuzzing Analysis on ARM Embedded Firmware with Efficient Event-based Fault Localization](https://arxiv.org/abs/2410.18483) (FirmRCA, IEEE S&P 2025)
- [HouseFuzz: Service-Aware Grey-Box Fuzzing for Vulnerability Detection in Linux-Based Firmware](03-dynamic-analysis-fuzzing/HouseFuzz%20Service-Aware%20Grey-Box%20Fuzzing%20for%20Vulnerability%20Detection%20in%20Linux-Based%20Firmware.pdf) (HouseFuzz, IEEE S&P 2025)
- [LEMIX: Enabling Testing of Embedded Applications as Linux Applications](https://www.usenix.org/conference/usenixsecurity25/presentation/tanksalkar) (LEMIX, USENIX Security 2025)
- [Labrador: Response Guided Directed Fuzzing for Black-box IoT Devices](03-dynamic-analysis-fuzzing/24-LABRADOR%20Response%20Guided%20Directed%20Fuzzing%20for%20Black-box%20IoT%20Devices.pdf) (Labrador, IEEE S&P 2024)
- [RIoTFuzzer: Companion App Assisted Remote Fuzzing for Detecting Vulnerabilities in IoT Devices](https://doi.org/10.1145/3658644.3670342) (RIoTFuzzer, CCS 2024)
- [SyzTrust: State-aware Fuzzing on Trusted OS Designed for IoT Devices](03-dynamic-analysis-fuzzing/24-SyzTrust-State-aware%20Fuzzing%20on%20Trusted%20OS%20Designed%20for%20IoT%20Devices.pdf) (SyzTrust, IEEE S&P 2024)
- [Forming Faster Firmware Fuzzers](03-dynamic-analysis-fuzzing/sec23_Forming%20Faster%20Firmware%20Fuzzers.pdf) (SAFIREFUZZ, USENIX Security 2023)
- [Fuzzing Embedded Systems using Debug Interfaces](03-dynamic-analysis-fuzzing/23-Fuzzing%20Embedded%20Systems%20using%20Debug%20Interfaces.pdf) (GDBFuzz, ISSTA 2023)
- [Greenhouse: Single-Service Rehosting of Linux-Based Firmware Binaries in User-Space Emulation](03-dynamic-analysis-fuzzing/23-greenhouse%20appendix-tay.pdf) (Greenhouse, USENIX Security 2023)
- [Hoedur: Embedded Firmware Fuzzing using Multi-Stream Inputs](03-dynamic-analysis-fuzzing/23-Hoedur%20Embedded%20Firmware%20Fuzzing.pdf) (Hoedur, USENIX Security 2023)
- [SplITS: Split Input-to-State Mapping for Effective Firmware Fuzzing](03-dynamic-analysis-fuzzing/23-Split%20Input-to-State%20Mapping%20for%20Effective%20Firmware%20Fuzzing.pdf) (SplITS, ESORICS 2023)
- [Fuzzware: Using Precise MMIO Modeling for Effective Firmware Fuzzing](03-dynamic-analysis-fuzzing/sec22-fuzzware.pdf) (Fuzzware, USENIX Security 2022)
- [Fw-fuzz: A Code Coverage-Guided Fuzzing Framework for Network Protocols on Firmware](03-dynamic-analysis-fuzzing/22-Fw_fuzz__A_code_coverage_guided_fuzzing_framework_for_network_protocols_on_firmware.pdf) (Fw-fuzz, Concurrency and Computation: Practice and Experience 2022)
- [uAFL: Non-intrusive Feedback-driven Fuzzing for Microcontroller Firmware](03-dynamic-analysis-fuzzing/22-Non-intrusive%20Feedback-driven%20Fuzzing%20for%20Microcontroller%20Firmware.pdf) (uAFL, ICSE 2022)
- [Automatic Firmware Emulation through Invalidity-guided Knowledge Inference](03-dynamic-analysis-fuzzing/sec21-uEmu.pdf) (uEmu, USENIX Security 2021)
- [DIANE: Identifying Fuzzing Triggers in Apps to Generate Under-constrained Inputs for IoT Devices](03-dynamic-analysis-fuzzing/21-Diane.pdf) (DIANE, IEEE S&P 2021)
- [ESRFuzzer: An Enhanced Fuzzing Framework for Physical SOHO Router Devices to Discover Multi-type Vulnerabilities](03-dynamic-analysis-fuzzing/21ESRFuzzer-%20An%20enhanced%20fuzzing%20framework%20for%20physical%20SOHO%20router%20devices%20to%20discover%20multi-type%20vulnerabilities.pdf) (ESRFuzzer, Cybersecurity (Springer) 2021)
- [FIRM-COV: High-Coverage Greybox Fuzzing for IoT Firmware via Optimized Process Emulation](03-dynamic-analysis-fuzzing/21-FIRM-COV_High-Coverage_Greybox_Fuzzing_for_IoT_Firmware_via_Optimized_Process_Emulation.pdf) (FIRM-COV, IEEE Access 2021)
- [From Library Portability to Para-rehosting: Natively Executing Microcontroller Software on Commodity Hardware](03-dynamic-analysis-fuzzing/21-From%20library%20portability%20to%20para-rehosting-%20Natively%20executing%20open-source%20microcontroller%20oss%20on%20commodity%20hardware.pdf) (NDSS 2021)
- [IFIZZ: Deep-State and Efficient Fault-Scenario Generation to Test IoT Firmware](03-dynamic-analysis-fuzzing/21-IFIZZ_Deep-State_and_Efficient_Fault-Scenario_Generation_to_Test_IoT_Firmware.pdf) (IFIZZ, ASE 2021)
- [PASAN: Detecting Peripheral Access Concurrency Bugs within Bare-Metal Embedded Applications](03-dynamic-analysis-fuzzing/21-PASAN-%20Detecting%20peripheral%20access%20concurrency%20bugs%20within%20Bare-Metal%20embedded%20applications.pdf) (PASAN, USENIX Security 2021)
- [SIoTFuzzer: Fuzzing Web Interface in IoT Firmware via Stateful Message Generation](03-dynamic-analysis-fuzzing/SIoTFuzzer%20Fuzzing%20Web%20Interface%20in%20IoT%20Firmware%20via%20Stateful%20Message%20Generation.pdf) (SIoTFuzzer, Applied Sciences (MDPI journal) 2021)
- [EM-Fuzz: Augmented Firmware Fuzzing via Memory Checking](03-dynamic-analysis-fuzzing/EM-fuzz.pdf) (EM-Fuzz, IEEE TCAD (journal) 2020)
- [FIRMCORN: Vulnerability-Oriented Fuzzing of IoT Firmware via Optimized Virtual Execution](03-dynamic-analysis-fuzzing/20-FIRMCORN_Vulnerability-Oriented_Fuzzing_of_IoT_Firmware_via_Optimized_Virtual_Execution.pdf) (FIRMCORN, IEEE Access 2020)
- [An Efficient Greybox Fuzzing Scheme for Linux-based IoT Programs Through Binary Static Analysis](03-dynamic-analysis-fuzzing/19-An%20efficient%20greybox%20fuzzing%20scheme%20for%20linux-based%20IoT%20programs%20through%20binary%20static%20analysis..pdf) (IEEE IPCCC 2019)
- [PeriScope: An Effective Probing and Fuzzing Framework for the Hardware-OS Boundary](03-dynamic-analysis-fuzzing/19_NDSS_PeriScope.pdf) (PeriScope, NDSS 2019)
- [Poster: Fuzzing IoT Firmware via Multi-stage Message Generation](03-dynamic-analysis-fuzzing/19-Fuzzing%20IoT%20Firmware%20via%20Multi-stage%20Message%20Generation.pdf) (IoTHunter, ACM CCS (poster) 2019)
- [SRFuzzer: An Automatic Fuzzing Framework for Physical SOHO Router Devices to Discover Multi-type Vulnerabilities](03-dynamic-analysis-fuzzing/19-SRFuzzer-%20An%20automatic%20fuzzing%20framework%20for%20physical%20SOHO%20router%20devices%20to%20discover%20multi-type%20vulnerabilities%2C.pdf) (SRFuzzer, ACSAC 2019)
- [What You Corrupt Is Not What You Crash: Challenges in Fuzzing Embedded Devices](03-dynamic-analysis-fuzzing/18-What%20you%20corrupt%20is%20not%20what%20you%20crash-%20Challenges%20in%20fuzzing%20embedded%20devices.pdf) (NDSS 2018)
- [Automated Dynamic Firmware Analysis at Scale: A Case Study on Embedded Web Interfaces](03-dynamic-analysis-fuzzing/15-Automated%20dynamic%20firmware%20analysis%20at%20scale-%20A%20case%20study%20on%20embedded%20web%20interfaces.pdf) (ACM ASIACCS 2016)
- [A Large-Scale Analysis of the Security of Embedded Firmwares](03-dynamic-analysis-fuzzing/14-large-scale%20analysis%20of%20the%20security%20of%20embedded%20firmwares.pdf) (USENIX Security 2014)
- [RPFuzzer: A Framework for Discovering Router Protocols Vulnerabilities Based on Fuzzing](03-dynamic-analysis-fuzzing/13-RPFuzzer-%20A%20Framework%20for%20Discovering%20Router%20Protocols%20Vulnerabilities%20Based%20on%20Fuzzing.pdf) (RPFuzzer, KSII Trans. on Internet and Information Systems 2013)

## 04. Symbolic Execution, Rehosting & Emulation

Symbolic/concolic execution, firmware rehosting, peripheral emulation, and hybrid analysis.

- [Khost: KVM-based Near Native MCU Firmware Rehosting](https://www.usenix.org/conference/usenixsecurity26/presentation/wang-chunlin) (Khost, USENIX Security 2026)
- [User-Space Dependency-Aware Rehosting for Linux-Based Firmware Binaries](https://www.ndss-symposium.org/ndss-paper/user-space-dependency-aware-rehosting-for-linux-based-firmware-binaries/) (NDSS 2026)
- [FlexEmu: Towards Flexible MCU Peripheral Emulation](https://doi.org/10.1145/3719027.3765086) (FlexEmu, CCS 2025)
- [GDMA: Fully Automated DMA Rehosting via Iterative Type Overlays](https://www.usenix.org/conference/usenixsecurity25/presentation/scharnowski) (GDMA, USENIX Security 2025)
- [Protocol-Aware Firmware Rehosting for Effective Fuzzing of Embedded Network Stacks](https://arxiv.org/pdf/2509.13740) (CCS 2025)
- [Truman: Constructing Device Behavior Models from OS Drivers to Fuzz Virtual Devices](https://www.ndss-symposium.org/ndss-paper/truman-constructing-device-behavior-models-from-os-drivers-to-fuzz-virtual-devices/) (Truman, NDSS 2025)
- [Accurate and Efficient Recurring Vulnerability Detection for IoT Firmware](04-dynamic-analysis-symbolic-execution/24-FirmRec-Accurate%20and%20Efficient%20Recurring%20Vulnerability%20Detection%20for%20IoT%20Firmware.pdf) (FirmRec, ACM CCS 2024)
- [FFXE: Dynamic Control Flow Graph Recovery for Embedded Firmware Binaries](04-dynamic-analysis-symbolic-execution/Tsang%20-%20FFXE%20Dynamic%20Control%20Flow%20Graph%20Recovery%20for%20Embe.pdf) (FFXE, USENIX Security 2024)
- [Pandawan: Quantifying Progress in Linux-based Firmware Rehosting](https://www.usenix.org/conference/usenixsecurity24/presentation/angelakopoulos) (Pandawan, USENIX Security 2024)
- [Poster: Discovering Authentication Bypass Vulnerabilities in IoT Devices through Guided Concolic Execution](04-dynamic-analysis-symbolic-execution/Poster%20Discovering%20Authentication%20Bypass.pdf) (NDSS (poster) 2024)
- [MMIO Access-Based Coverage for Firmware Analysis](04-dynamic-analysis-symbolic-execution/23-MMIO_Access-Based_Coverage_for_Firmware_Analysis.pdf) (FIRMSTAT, IEEE CNS 2023)
- [Device-agnostic Firmware Execution is Possible: A Concolic Execution Approach for Peripheral Emulation](04-dynamic-analysis-symbolic-execution/20-Laelaps.pdf) (Laelaps, ACSAC 2020)
- [Firmalice: Automatic Detection of Authentication Bypass Vulnerabilities in Binary Firmware](04-dynamic-analysis-symbolic-execution/Firmalice%20-%20Automatic%20Detection%20of%20Authentication%20Bypass%20Vulnerabilities%20in%20Binary%20Firmware.pdf) (Firmalice, NDSS 2015)

## 05. Surveys, Taxonomies & Corpora

Surveys, taxonomies, and firmware corpora supporting vulnerability research.

- [Mens Sana In Corpore Sano: Sound Firmware Corpora for Vulnerability Research](05-surveys-and-taxonomies/Mens%20Sana%20In%20Corpore%20Sano%20Sound%20Firmware%20Corpora%20for%20Vulnerability%20Research.pdf) (LFwC, NDSS 2025)
- [A Taxonomy of IoT Firmware Security and Principal Firmware Analysis Techniques](05-surveys-and-taxonomies/A_taxonomy_of_IoT_firmware_security_and_principal_firmware_analysis_techniques.pdf) (Intl. J. Critical Infrastructure Protection 2022)
- [Embedded Fuzzing: A Review of Challenges, Tools, and Solutions](05-surveys-and-taxonomies/22-Embedded_fuzzing__a_review_of_challenges__tools__and_solutions.pdf) (Cybersecurity (Springer) 2022)
- [Firmware Fuzzing: The State of the Art](05-surveys-and-taxonomies/Firmware%20Fuzzing-The%20State%20of%20the%20Art.pdf) (Internetware 2021)
- [Dynamic Binary Firmware Analysis: Challenges & Solutions](05-surveys-and-taxonomies/19-Dynamic%20binary%20firmware%20analysis-challenges%20%26%20solutions.pdf) (PhD Thesis, EURECOM 2019)

## 06. Firmware Measurement Studies

Empirical studies whose primary object is deployed device firmware or the firmware ecosystem.

- [Unveiling IoT Security in Reality: A Firmware-Centric Journey](https://www.usenix.org/conference/usenixsecurity24/presentation/nino) (USENIX Security 2024)
