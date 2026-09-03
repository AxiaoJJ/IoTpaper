# scripts/ — automated paper discovery

`fetch_papers.py` discovers new **IoT / embedded-firmware analysis** papers
and writes a candidate list for human triage. It is the engine behind the weekly
GitHub Actions job in [`.github/workflows/fetch-papers.yml`](../.github/workflows/fetch-papers.yml).

## What it does

1. Reads `README.md` → the set of titles already in the collection (**dedup
   baseline; stays in sync automatically — no separate list to maintain**).
2. Queries **DBLP** for IoT/embedded-firmware vulnerability-analysis terms, keeping only results
   published in the target venues (IEEE S&P, USENIX Security, ACM CCS, NDSS,
   ICSE, FSE, ASE, ISSTA, ICLR) and relevant security/IoT/embedded journals
   (IEEE TDSC/TIFS/IoT Journal, Computers & Security, ACM TECS) in recent years.
3. Queries **arXiv** `cs.CR` for recent preprints about firmware vulnerability
   detection, fuzzing, taint analysis, symbolic execution, or rehosting.
4. Requires both a firmware/embedded-device target and a vulnerability-analysis
   method signal. It filters PLC/ICS, baseband, protocol-only wireless, UEFI,
   vehicle/UAV/satellite, and honeypot topics.
5. Drops anything already in `README.md`.
6. Writes:
   - `scripts/candidates.md` — a Markdown table (Issue body), and
   - `scripts/candidates.count` — the candidate count (used by the workflow).

In GitHub Actions, if `candidates.count > 0`, a new issue labelled `new-papers`
is opened automatically each Monday.

## Run it yourself

```bash
# full run (hits DBLP + arXiv)
python3 scripts/fetch_papers.py

# offline self-test (README parsing + dedup only, no network)
FETCH_OFFLINE=1 python3 scripts/fetch_papers.py

# tune behavior via env
FETCH_MIN_YEAR=2024 DBLP_SLEEP=5 python3 scripts/fetch_papers.py
```

`DBLP_SLEEP` is the pause between DBLP requests — DBLP rate-limits aggressively
and will reset connections if hammered, so keep it ≥ 4–5 s.

## Notes & limitations

- **Firmware-analysis scope.** Linux-based IoT firmware is central, while
  reusable MCU/RTOS firmware-analysis techniques are included. Unrelated IoT
  verticals and protocol-only work are excluded.
- **DBLP coverage.** DBLP metadata has no abstract, so a relevant paper with a
  non-descriptive title may be missed. arXiv has an abstract-level check; a
  venue-wide review remains appropriate when maximum recall is needed.
- **Copyright.** This tool collects **metadata + links only**. It never
  downloads PDFs. See [`CONTRIBUTING.md`](../CONTRIBUTING.md) for the PDF
  policy.
