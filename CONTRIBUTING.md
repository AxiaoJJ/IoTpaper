# Contributing

Thanks for helping improve this IoT / embedded firmware security paper collection. Contributions are welcome as long as they keep the repository accurate, readable, and legally redistributable.

## What to Submit

You can submit:

- New IoT / embedded / firmware security papers
- Corrections to title, tool name, venue, year, category, or links
- Better classification of existing papers
- Missing author/team/institution information
- Legal open-access PDF replacements for link-only entries

## Paper Scope

This repository focuses on IoT, embedded systems, firmware, and cyber-physical-device security, especially:

- Firmware static analysis, taint analysis, binary analysis, vulnerability detection
- Firmware fuzzing, dynamic analysis, emulation, rehosting, symbolic/concolic execution
- IoT protocol / application / smart-home / BLE / Zigbee / MQTT / baseband security
- IoT measurement studies, datasets, honeypots, deception systems
- LLM/AI/SE techniques when they are directly applied to IoT, embedded systems, firmware, or device security

Please avoid adding generic software-security or generic ML-security papers unless they have a clear embedded/IoT/firmware angle.

## Required Metadata Format

When adding or proposing a paper, use this format:

```markdown
- [Full Paper Title](official-url-or-local-pdf-path) (ToolName, Venue Year)
```

If the paper does not introduce a named tool/system, omit the tool name:

```markdown
- [Full Paper Title](official-url-or-local-pdf-path) (Venue Year)
```

Examples:

```markdown
- [Detecting Vulnerabilities in Linux-Based Embedded Firmware with SSE-Based On-Demand Alias Analysis](...) (EmTaint, ISSTA 2023)
- [What You Corrupt Is Not What You Crash: Challenges in Fuzzing Embedded Devices](...) (NDSS 2018)
```

## Required Fields for a New Paper

Please include the following in your PR description:

| Field | Required | Example |
|---|---:|---|
| Full title | yes | `Fuzzware: Using Precise MMIO Modeling for Effective Firmware Fuzzing` |
| Tool/system name | if any | `Fuzzware` |
| Venue | yes | `USENIX Security` |
| Year | yes | `2022` |
| Category | yes | `03. Dynamic Analysis — Fuzzing` |
| Official link | yes | USENIX/NDSS/ACM/IEEE/arXiv/DOI page |
| PDF source | if adding PDF | Official open-access PDF or legally redistributable author preprint |
| One-sentence reason | yes | Why this belongs in an IoT/firmware security collection |

## Category Guide

Choose the closest category:

1. **Static Analysis — Traditional**: static taint, binary analysis, code similarity, source/binary vulnerability detection
2. **Static Analysis — LLM-Assisted**: LLM/AI-assisted firmware or embedded-device code analysis
3. **Dynamic Analysis — Fuzzing**: fuzzing, greybox/blackbox testing, feedback-driven testing, protocol/device fuzzing
4. **Dynamic Analysis — Symbolic Execution & Hybrid**: symbolic/concolic execution, rehosting/emulation, hybrid static+dynamic analysis
5. **Surveys & Taxonomies**: SoK, survey, taxonomy, dataset/corpus papers
6. **Measurement & Large-Scale Studies**: empirical studies, internet-wide measurement, firmware ecosystem studies
7. **Protocol & Application Security**: BLE, Zigbee, MQTT, Matter, Wi-Fi, smart-home, baseband, app/device protocol security
8. **Honeypot & Deception**: honeypots, deception, attacker-observation infrastructure

If a paper fits multiple categories, pick the one that best matches its main contribution. Mention the secondary category in the PR description.

## Sorting Rules

Within each category:

1. Sort by year, newest first
2. For the same year, sort alphabetically by title
3. Keep local PDFs and 🆕 link-only entries in the same list
4. Use `🆕` for papers that are only linked and whose PDF has not yet been added

## PDF / Copyright Policy

Do **not** upload paywalled PDFs unless you have the legal right to redistribute them.

Allowed:

- Official open-access PDFs from USENIX, NDSS, arXiv, or authors' institutional pages
- Author-accepted manuscripts explicitly made public by the authors
- PDFs with a clear permissive license

Not allowed:

- PDFs downloaded from ACM DL / IEEE Xplore if they are behind a paywall
- Random PDF mirrors with unclear copyright status
- Publisher PDFs that cannot legally be redistributed

When in doubt, add only the official link and mark the paper as 🆕.

## PR Checklist

Before submitting:

- [ ] The paper is directly relevant to IoT / embedded / firmware security
- [ ] The title is the official full title
- [ ] Tool name, venue, and year are verified
- [ ] The paper is placed in the most appropriate category
- [ ] The category list remains sorted newest-first
- [ ] The link points to an official source, DOI, arXiv, or author page
- [ ] Any uploaded PDF is legally redistributable
- [ ] The paper is not already listed under another name/tool

## Suggested PR Title

```text
Add <ToolName or Short Title> (<Venue Year>)
```

Examples:

```text
Add Fuzzware (USENIX Security 2022)
Add Matter controller security analysis (NDSS 2025)
```

## Corrections

Corrections are very welcome. If you find wrong metadata, please open a PR or issue with:

- The current incorrect entry
- The corrected value
- A source URL supporting the correction

