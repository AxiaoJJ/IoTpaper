#!/usr/bin/env python3
"""
fetch_papers.py — auto-discover new IoT / embedded-firmware security papers.

Pipeline:
  1. Read README.md -> set of "known" titles (dedup baseline, stays in sync).
  2. DBLP keyword search across many IoT/firmware terms -> keep only results in
     the target venue set (S&P, USENIX Sec, CCS, NDSS, ICSE, FSE, ASE, ISSTA,
     ICLR) and recent years.
  3. arXiv cs.CR preprints matching IoT/firmware abstract terms.
  4. Drop anything already in README; suggest a category for the rest.
  5. Write scripts/candidates.md (issue body) + scripts/candidates.count.

Stdlib only (urllib, json, re, xml) — no pip install needed in GitHub Actions.
Env:
  FETCH_OFFLINE=1     skip network (parsing/dedup self-test only)
  FETCH_YEARS=2024,2025,2026   minimum years to keep from DBLP
"""

import html
import json
import os
import re
import sys
import time
import urllib.parse
import urllib.request
import xml.etree.ElementTree as ET
from datetime import datetime

README = "README.md"
OUT = "scripts/candidates.md"
# DBLP rejects generic UAs with HTTP 500; a browser UA is required.
UA = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120 Safari/537.36"

MIN_YEAR = int(os.environ.get("FETCH_MIN_YEAR", "2024"))

# ---- DBLP keyword queries (broad recall for IoT/firmware topics) -----------
# Kept to a high-recall core; DBLP aggressively rate-limits, so fewer queries
# with a longer sleep beats many fast ones (which get connection-reset).
DBLP_QUERIES = [
    "firmware", "IoT security", "IoT vulnerability", "embedded system security",
    "embedded firmware", "baseband firmware", "bluetooth low energy", "zigbee",
    "mqtt security", "smart home security", "RTOS firmware", "PLC security",
    "industrial control system security", "drone security", "firmware fuzzing",
    "firmware rehosting", "UEFI security", "cyber-physical system security",
]
DBLP_SLEEP = float(os.environ.get("DBLP_SLEEP", "5"))

# ---- Target venue whitelist (DBLP `venue` field is a short string) ---------
def venue_canonical(raw):
    if isinstance(raw, list):          # DBLP sometimes returns venue as a list
        raw = raw[0] if raw else ""
    v = (raw or "").lower().strip()
    if v in ("sp", "s&p") or "symposium on security and privacy" in v:
        return "IEEE S&P"
    if v == "ndss" or "ndss" in v:
        return "NDSS"
    if "usenix security" in v:
        return "USENIX Security"
    if v == "ccs" or "computer and communications security" in v:
        return "ACM CCS"
    if v == "icse":
        return "ICSE"
    if v == "fse" or "esec/fse" in v or "sigsoft" in v:
        return "FSE"
    if v == "ase":
        return "ASE"
    if v == "issta":
        return "ISSTA"
    if v == "iclr":
        return "ICLR"
    return None

# ---- IoT / firmware relevance (title-level precision filter) ---------------
# Applied to ALL candidates. Cuts arXiv noise (broad abstract terms pull in
# LLM/adversarial-ML papers that aren't IoT/firmware).
KW_SINGLE = {
    "firmware", "iot", "embedded", "baseband", "ble", "bluetooth", "zigbee",
    "matter", "mqtt", "lorawan", "nfc", "rfid", "rtos", "mcu",
    "microcontroller", "plc", "scada", "ics", "cps", "drone", "uav", "robotic",
    "sensor", "rehost", "trustzone", "tee", "uefi", "bootloader", "cellular",
    "lte", "5g", "6g", "wifi", "peripheral", "mmio", "edk",
}
KW_PHRASE = ("smart home", "smart homes", "cyber physical", "cyber-physical",
             "industrial control", "smart speaker", "smart device")

def is_iot_relevant(title):
    s = re.sub(r"\s+", " ", re.sub(r"[^a-z0-9]+", " ", title.lower())).strip(" ")
    words = s.split()
    wset = set(words)
    for kw in KW_SINGLE:
        if len(kw) >= 4:                       # prefix-safe: firmware->firmwares, rehost->rehosting
            if any(w.startswith(kw) for w in words):
                return True
        else:                                  # short tokens (ble, tee, ics): exact only
            if kw in wset:
                return True
    return any(p in s for p in KW_PHRASE)

# ---- arXiv abstract-term queries -------------------------------------------
ARXIV_QUERIES = [
    'cat:cs.CR+AND+(abs:firmware+OR+abs:IoT+OR+abs:embedded+OR+abs:baseband)',
    'cat:cs.CR+AND+(abs:RTOS+OR+abs:microcontroller+OR+abs:PLC+OR+abs:%22smart+home%22)',
    'cat:cs.CR+AND+(abs:BLE+OR+abs:Zigbee+OR+abs:MQTT+OR+abs:UEFI)',
]

# ---- helpers ---------------------------------------------------------------
def norm_title(t):
    return re.sub(r"[^a-z0-9]+", " ", t.lower()).strip()

def http_get(url, tries=2, delay=4):
    """Fetch with light retry. Under DBLP rate-limiting we'd rather skip a
    query fast (and still produce a report) than stall the whole run."""
    last = None
    for k in range(tries):
        try:
            req = urllib.request.Request(url, headers={"User-Agent": UA, "Accept": "application/json, application/xml, */*"})
            with urllib.request.urlopen(req, timeout=20) as r:
                return r.read().decode("utf-8", "replace")
        except Exception as e:  # noqa
            last = e
            time.sleep(delay * (k + 1))   # back off: 4s, 8s
    raise last

def unescape(s):
    """HTML-unescape repeatedly until stable (DBLP sometimes double-escapes)."""
    prev = None
    for _ in range(4):
        if prev == s:
            break
        prev = s
        s = html.unescape(s)
    return s

def read_known(readme_path):
    known = set()
    try:
        text = open(readme_path, encoding="utf-8").read()
    except FileNotFoundError:
        return known
    for m in re.finditer(r"^\s*-\s+(?:🆕\s+)?\[([^\]]+)\]\(", text, re.M):
        known.add(norm_title(m.group(1)))
    return known

def suggest_category(title):
    t = title.lower()
    if "fuzz" in t:
        return "03 Fuzzing"
    if any(k in t for k in ("symbolic", "concolic", "rehost", "emulat")):
        return "04 Symbolic/Hybrid/Rehost"
    if any(k in t for k in ("survey", "taxonomy", "systematiz", "review", "sok")):
        return "05 Survey"
    if any(k in t for k in ("benchmark", "dataset", "corpus", "measurement", "large-scale", "empirical", "in the wild")):
        return "06 Measurement"
    if any(k in t for k in ("honeypot", "decept")):
        return "08 Honeypot"
    if any(k in t for k in ("llm", "large language", "gpt", "transformer", "language model")):
        return "02 LLM-assisted"
    if any(k in t for k in ("ble", "bluetooth", "zigbee", "matter", "mqtt", "wi-fi", "wifi", "fast pair", "lte", "5g", "protocol")):
        return "07 Protocol/App"
    return "01 Static (default)"

# ---- DBLP ------------------------------------------------------------------
def fetch_dblp():
    out, seen = [], set()
    for q in DBLP_QUERIES:
        url = f"https://dblp.org/search/publ/api?q={urllib.parse.quote(q)}&format=json&h=1000&f=0"
        try:
            d = json.loads(http_get(url))
        except Exception as e:  # noqa
            print(f"  [dblp] q={q!r}: {e}", file=sys.stderr)
            time.sleep(DBLP_SLEEP)
            continue
        hits = (d.get("result", {}) or {}).get("hits", {}).get("hit", []) or []
        for h in hits:
            info = h.get("info", {})
            try:
                year = int(info.get("year", 0))
            except (ValueError, TypeError):
                year = 0
            if year < MIN_YEAR:
                continue
            cv = venue_canonical(info.get("venue"))
            if not cv:
                continue
            title = unescape(info.get("title", "")).rstrip(".")
            if not title:
                continue
            ee = info.get("ee") or ""
            if isinstance(ee, list):
                ee = unescape(ee[0]) if ee else ""
            key = info.get("key", "")
            rec_nt = norm_title(title)
            if rec_nt in seen:
                continue
            seen.add(rec_nt)
            out.append({"title": title, "venue": f"{cv} {year}", "year": year,
                        "url": ee or f"https://dblp.org/rec/{key}.html", "src": "dblp"})
        time.sleep(DBLP_SLEEP)  # DBLP fair-use: keep requests sparse
    return out

# ---- arXiv -----------------------------------------------------------------
ARXIV_NS = {"a": "http://www.w3.org/2005/Atom"}
def fetch_arxiv(max_per_query=100):
    out = []
    for q in ARXIV_QUERIES:
        url = f"http://export.arxiv.org/api/query?search_query={q}&start=0&max_results={max_per_query}&sortBy=submittedDate&sortOrder=descending"
        try:
            root = ET.fromstring(http_get(url))
        except Exception as e:  # noqa
            print(f"  [arxiv] query failed: {e}", file=sys.stderr)
            continue
        for entry in root.findall("a:entry", ARXIV_NS):
            t = entry.find("a:title", ARXIV_NS)
            title = unescape(re.sub(r"\s+", " ", t.text or "").strip()) if t is not None else ""
            if not title:
                continue
            pub = entry.find("a:published", ARXIV_NS)
            year = int((pub.text or "")[:4]) if (pub is not None and pub.text) else 0
            if year < MIN_YEAR:
                continue
            id_ = entry.find("a:id", ARXIV_NS)
            link = id_.text.strip() if id_ is not None else ""
            out.append({"title": title, "venue": f"arXiv {year}", "year": year,
                        "url": link, "src": "arxiv"})
        time.sleep(3)  # arXiv requests >=3s between calls
    return out

# ---- main ------------------------------------------------------------------
def main():
    offline = os.environ.get("FETCH_OFFLINE") == "1"
    known = read_known(README)
    print(f"known titles in README: {len(known)}", file=sys.stderr)

    raw = []
    if not offline:
        print("fetching DBLP...", file=sys.stderr)
        raw += fetch_dblp()
        print("fetching arXiv...", file=sys.stderr)
        raw += fetch_arxiv()
    else:
        print("FETCH_OFFLINE=1 -> skipping network", file=sys.stderr)

    seen, cands = set(), []
    for p in raw:
        if not is_iot_relevant(p["title"]):
            continue
        nt = norm_title(p["title"])
        if nt in known or nt in seen:
            continue
        seen.add(nt)
        p["cat"] = suggest_category(p["title"])
        cands.append(p)

    cands.sort(key=lambda x: (x["year"], x["venue"], x["title"]))
    write_report(cands)
    open("scripts/candidates.count", "w").write(str(len(cands)))
    print(f"candidates: {len(cands)}  (written to {OUT})", file=sys.stderr)

def write_report(cands):
    today = datetime.utcnow().strftime("%Y-%m-%d")
    srcs = f"DBLP (>= {MIN_YEAR}) + arXiv cs.CR"
    lines = [
        f"# 📬 New IoT/Firmware Paper Candidates ({today})",
        "",
        f"Auto-discovered from {srcs}, filtered to target venues, and "
        "de-duplicated against the current README.",
        "",
        f"**{len(cands)} new candidate(s).** Review each, then add the relevant ones per "
        "[CONTRIBUTING.md](../CONTRIBUTING.md) — format: `- [Title](url) (Tool, Venue Year)`.",
        "",
        "| Title | Venue | Suggested Category | Link |",
        "|---|---|---|---|",
    ]
    for c in cands[:300]:
        title = c["title"].replace("|", "\\|")
        lines.append(f"| {title} | {c['venue']} | {c['cat']} | [link]({c['url']}) |")
    if len(cands) > 300:
        lines.append(f"| _…{len(cands)-300} more truncated_ | | | |")
    lines += ["", "_Close this issue after triage. The keyword filter prioritizes recall, "
              "so false positives are expected._"]
    open(OUT, "w", encoding="utf-8").write("\n".join(lines))

if __name__ == "__main__":
    main()
