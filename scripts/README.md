# scripts/ — automated paper discovery

`fetch_papers.py` discovers new IoT / embedded-firmware security papers and
writes a candidate list for human triage. It is the engine behind the weekly
GitHub Actions job in [`.github/workflows/fetch-papers.yml`](../.github/workflows/fetch-papers.yml).

## What it does

1. Reads `README.md` → the set of titles already in the collection (**dedup
   baseline; stays in sync automatically — no separate list to maintain**).
2. Queries **DBLP** for ~18 IoT/firmware keyword terms, keeping only results
   published in the target venues (IEEE S&P, USENIX Security, ACM CCS, NDSS,
   ICSE, FSE, ASE, ISSTA, ICLR) in recent years.
3. Queries **arXiv** `cs.CR` for recent preprints matching firmware / IoT /
   embedded / BLE / RTOS / UEFI / etc.
4. Applies a title-level **relevance filter** (token set + phrase matches) to
   cut arXiv noise (LLM/adversarial-ML preprints).
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

- **Recall vs precision.** The keyword approach prioritizes recall; expect some
  false positives in `candidates.md`. A human still decides what to add.
- **arXiv is noisy.** It contributes the most candidates and the most noise;
  the title relevance filter trims the worst of it.
- **DBLP coverage.** Keyword search can miss papers whose titles don't contain
  an obvious IoT term. If a venue's full listing is ever needed, the DBLP
  *stream* API or per-venue JSON can be added later.
- **Copyright.** This tool collects **metadata + links only**. It never
  downloads PDFs. See [`CONTRIBUTING.md`](../CONTRIBUTING.md) for the PDF
  policy.
