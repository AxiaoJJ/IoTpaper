#!/usr/bin/env python3
"""Count publication venues and regenerate the Security Top Four trend chart."""

import re
from collections import Counter, defaultdict
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt


ROOT = Path(__file__).resolve().parents[1]
README = ROOT / "README.md"
OUTPUT = ROOT / "assets" / "security-top4-trend.png"
TOP_FOUR = ("IEEE S&P", "USENIX Security", "ACM CCS", "NDSS")


def canonical_venue(line: str) -> str:
    """Return a canonical Top Four venue name, or ``Other``."""
    if "IEEE S&P " in line:
        return "IEEE S&P"
    if "USENIX Security " in line:
        return "USENIX Security"
    if re.search(r"\b(?:ACM )?CCS(?: \(poster\))? \d{4}", line):
        return "ACM CCS"
    if re.search(r"\bNDSS(?: \(poster\))? \d{4}", line):
        return "NDSS"
    return "Other"


papers = [
    line for line in README.read_text(encoding="utf-8").splitlines()
    if line.startswith("- [")
]
counts = Counter(canonical_venue(line) for line in papers)
by_year = defaultdict(Counter)

for line in papers:
    venue = canonical_venue(line)
    if venue == "Other":
        continue
    years = re.findall(r"\b(?:19|20)\d{2}\b", line)
    if years:
        by_year[int(years[-1])][venue] += 1

years = list(range(min(by_year), max(by_year) + 1))
colors = ("#2563eb", "#16a34a", "#dc2626", "#7c3aed")
fig, ax = plt.subplots(figsize=(10.5, 4.8), dpi=160)
bottom = [0] * len(years)

for venue, color in zip(TOP_FOUR, colors):
    values = [by_year[year][venue] for year in years]
    ax.bar(years, values, bottom=bottom, label=venue, color=color, width=0.72)
    bottom = [current + value for current, value in zip(bottom, values)]

for year, total in zip(years, bottom):
    if total:
        ax.text(year, total + 0.18, str(total), ha="center", va="bottom",
                fontsize=8.5, color="#334155")

ax.set_title("Security Top Four Papers by Year", fontsize=14,
             fontweight="bold", pad=14)
ax.set_xlabel("Publication year")
ax.set_ylabel("Papers in this collection")
ax.set_xticks(years)
ax.tick_params(axis="x", rotation=45)
ax.set_ylim(0, max(bottom) + 2)
ax.grid(axis="y", linestyle="--", alpha=0.25)
ax.spines[["top", "right"]].set_visible(False)
ax.legend(ncol=2, frameon=False, loc="upper left")
ax.text(0.99, 0.96, "2026 is in progress", transform=ax.transAxes,
        ha="right", va="top", fontsize=8.5, color="#64748b", style="italic")

plt.tight_layout()
plt.savefig(OUTPUT, bbox_inches="tight", facecolor="white")

print(f"papers: {len(papers)}")
for venue in TOP_FOUR:
    print(f"{venue}: {counts[venue]}")
print(f"Other: {counts['Other']}")
print(f"saved {OUTPUT}")
