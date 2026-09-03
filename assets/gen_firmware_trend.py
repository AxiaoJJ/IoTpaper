#!/usr/bin/env python3
"""Regenerate the yearly paper-count chart from README.md."""

import re
from collections import Counter
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt


ROOT = Path(__file__).resolve().parents[1]
README = ROOT / "README.md"
OUTPUT = ROOT / "assets" / "firmware-paper-trend.png"

counts = Counter()
for line in README.read_text(encoding="utf-8").splitlines():
    if not line.startswith("- ["):
        continue
    years = re.findall(r"\b(?:19|20)\d{2}\b", line)
    if years:
        counts[int(years[-1])] += 1

years = list(range(min(counts), max(counts) + 1))
values = [counts[year] for year in years]

fig, ax = plt.subplots(figsize=(10.5, 4.8), dpi=160)
colors = ["#93c5fd" if year < 2023 else "#2563eb" for year in years]
bars = ax.bar(years, values, color=colors, width=0.72)

for bar, value in zip(bars, values):
    if value:
        ax.text(bar.get_x() + bar.get_width() / 2, value + 0.35, str(value),
                ha="center", va="bottom", fontsize=8.5, color="#1e3a8a")

ax.set_title("IoT / Embedded Firmware Analysis Papers by Year",
             fontsize=14, fontweight="bold", pad=14)
ax.set_xlabel("Publication year")
ax.set_ylabel("Papers in this collection")
ax.set_xticks(years)
ax.tick_params(axis="x", rotation=45)
ax.set_ylim(0, max(values) + 3)
ax.grid(axis="y", linestyle="--", alpha=0.3)
ax.spines[["top", "right"]].set_visible(False)
ax.text(0.99, 0.96, "2026 is in progress", transform=ax.transAxes,
        ha="right", va="top", fontsize=8.5, color="#64748b", style="italic")

plt.tight_layout()
plt.savefig(OUTPUT, bbox_inches="tight", facecolor="white")
print(f"saved {OUTPUT}")
