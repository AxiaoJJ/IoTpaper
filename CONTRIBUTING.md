# Contributing

Thanks for helping improve this Linux-based IoT / embedded firmware security paper collection. Contributions are welcome as long as they keep the repository accurate, readable, and legally redistributable.

## What to Submit

You can submit:

- New Linux-based IoT / embedded-firmware security papers
- Corrections to title, tool name, venue, year, category, or links
- Better classification of existing papers
- Missing author/team/institution information
- Legal open-access PDF replacements for link-only entries

## Paper Scope

This repository focuses only on Linux-based IoT and embedded-firmware security, especially:

- Static/taint/binary analysis and vulnerability detection for Linux-based IoT firmware
- Linux-based firmware fuzzing, dynamic analysis, emulation, and rehosting
- Linux-based IoT device web interfaces and applications, when their device/firmware target is explicit
- LLM/AI/SE techniques when directly applied to Linux-based IoT firmware or embedded Linux applications

Please avoid adding bare-metal/RTOS/UEFI, generic protocol, generic IoT, generic embedded, software-security, or ML-security papers unless they explicitly target Linux-based IoT firmware or embedded Linux applications.

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
- [Bond: Constraint-Directed Fuzzing for Automated Validation of Taint Analysis Results in Linux-based IoT Firmware](...) (USENIX Security 2026)
```

## Required Fields for a New Paper

Please include the following in your PR description:

| Field | Required | Example |
|---|---:|---|
| Full title | yes | `HouseFuzz: Service-Aware Grey-Box Fuzzing for Vulnerability Detection in Linux-Based Firmware` |
| Tool/system name | if any | `HouseFuzz` |
| Venue | yes | `USENIX Security` |
| Year | yes | `2025` |
| Category | yes | `02. Dynamic Analysis — Fuzzing` |
| Official link | yes | USENIX/NDSS/ACM/IEEE/arXiv/DOI page |
| PDF source | if adding PDF | Official open-access PDF or legally redistributable author preprint |
| One-sentence reason | yes | Why this belongs in a Linux-based IoT/firmware security collection |

## Category Guide

Choose the closest category:

1. **Static Analysis**: static taint, binary analysis, code similarity, and vulnerability detection for Linux-based firmware
2. **Dynamic Analysis — Fuzzing**: fuzzing, greybox/blackbox testing, and feedback-driven testing for Linux-based firmware
3. **Rehosting & Emulation**: rehosting, emulation, and hybrid static+dynamic analysis of Linux-based firmware binaries

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

- [ ] The paper explicitly targets Linux-based IoT firmware or embedded Linux applications
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
Add HouseFuzz (IEEE S&P 2025)
Add Linux firmware rehosting analysis (NDSS 2026)
```

## Corrections

Corrections are very welcome. If you find wrong metadata, please open a PR or issue with:

- The current incorrect entry
- The corrected value
- A source URL supporting the correction
