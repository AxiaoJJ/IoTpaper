#!/usr/bin/env python3
"""
fetch_papers.py — auto-discover IoT / embedded-firmware security papers.

Pipeline:
  1. Read README.md -> set of "known" titles (dedup baseline, stays in sync).
  2. DBLP keyword search for IoT/embedded-firmware analysis terms -> keep only results in
     the target venue set (S&P, USENIX Sec, CCS, NDSS, ICSE, FSE, ASE, ISSTA,
     ICLR) and recent years.
  3. arXiv cs.CR preprints matching firmware-analysis abstract terms.
  4. Drop anything already in README; suggest a category for the rest.
  5. Write scripts/candidates.md (issue body) + scripts/candidates.count.

Stdlib only (urllib, json, re, xml) — no pip install needed in GitHub Actions.
Env:
  FETCH_OFFLINE=1     skip network (parsing/dedup self-test only)
  FETCH_MIN_YEAR=2024          minimum year to keep
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

# ---- DBLP keyword queries (IoT/embedded-firmware analysis) -----------------
DBLP_QUERIES = [
    "IoT firmware vulnerability", "embedded firmware security",
    "binary firmware analysis", "firmware taint analysis",
    "firmware vulnerability detection", "firmware fuzzing",
    "firmware rehosting", "firmware emulation", "router firmware security",
    "IoT firmware authentication bypass", "embedded system taint analysis",
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
    if "dependable and secure computing" in v or "dependable secur" in v:
        return "IEEE TDSC"
    if "information forensics and security" in v or "inf. forensics secur" in v:
        return "IEEE TIFS"
    if "internet of things journal" in v or "internet things j" in v:
        return "IEEE IoT Journal"
    if "computers & security" in v or "computers and security" in v or "comput. secur" in v:
        return "Computers & Security"
    if "embedded computing systems" in v or "embed. comput. syst" in v:
        return "ACM TECS"
    return None

# ---- IoT / embedded-firmware relevance -------------------------------------
TARGET_TERMS = (
    "firmware", "embedded system", "embedded software", "iot device",
    "internet of things device", "router", "microcontroller", "mcu", "rtos",
    "bootloader", "busybox",
)
ANALYSIS_TERMS = (
    "vulnerab", "fuzz", "taint", "static analysis", "dynamic analysis",
    "binary analysis", "rehost", "emulat", "symbolic execution", "concolic",
    "authentication bypass", "security analysis", "hotpatch", "firmware update",
    "testing", "corpus", "corpora", "taxonomy",
)
EXCLUDED_TERMS = (
    "plc", "industrial control", "scada", "baseband", "cellular firmware",
    "bluetooth", "ble protocol", "zigbee", "mqtt", "matter controller",
    "wi fi", "drone", "uav", "robotic vehicle", "satellite", "automobile",
    "automotive", "ecu firmware", "uefi", "smi handler", "honeypot",
    "building automation",
)

def is_firmware_relevant(text):
    s = re.sub(r"\s+", " ", re.sub(r"[^a-z0-9]+", " ", text.lower())).strip(" ")
    return (any(term in s for term in TARGET_TERMS)
            and any(term in s for term in ANALYSIS_TERMS)
            and not any(term in s for term in EXCLUDED_TERMS))

# ---- arXiv abstract-term queries -------------------------------------------
ARXIV_QUERIES = [
    'cat:cs.CR+AND+abs:firmware+AND+(abs:vulnerability+OR+abs:fuzzing+OR+abs:taint)',
    'cat:cs.CR+AND+(abs:firmware+OR+abs:%22embedded+system%22)+AND+(abs:rehosting+OR+abs:emulation+OR+abs:%22symbolic+execution%22)',
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
    if any(k in t for k in ("llm", "large language", "gpt", "language model")):
        return "02 LLM-Assisted Firmware Analysis"
    if any(k in t for k in ("survey", "taxonomy", "systematiz", "review", "sok", "corpus", "corpora")):
        return "05 Surveys, Taxonomies & Corpora"
    if any(k in t for k in ("measurement", "large-scale", "empirical", "in the wild", "longitudinal")):
        return "06 Firmware Measurement Studies"
    if "fuzz" in t:
        return "03 Firmware Fuzzing & Dynamic Testing"
    if any(k in t for k in ("symbolic", "concolic", "rehost", "emulat")):
        return "04 Symbolic Execution, Rehosting & Emulation"
    return "01 Static & Taint Analysis"

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
            summary = entry.find("a:summary", ARXIV_NS)
            abstract = unescape(re.sub(r"\s+", " ", summary.text or "").strip()) if summary is not None else ""
            id_ = entry.find("a:id", ARXIV_NS)
            link = id_.text.strip() if id_ is not None else ""
            out.append({"title": title, "venue": f"arXiv {year}", "year": year,
                        "url": link, "src": "arxiv", "scope_text": f"{title} {abstract}"})
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
        if not is_firmware_relevant(p.get("scope_text", p["title"])):
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
        f"# 📬 New IoT/Firmware Analysis Paper Candidates ({today})",
        "",
        f"Auto-discovered from {srcs}, filtered to IoT/embedded-firmware analysis scope and target venues, and "
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
