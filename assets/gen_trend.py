#!/usr/bin/env python3
"""Regenerate assets/trend-security-top4.png.

Counts below mirror the README 'Overview' table. Update them (and the README)
together when new papers are added.
"""
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

years = [2023, 2024, 2025, 2026]
series = [
    ("IEEE S&P",        [1, 4, 6, 8],   "#1f77b4"),  # blue
    ("USENIX Security", [3, 4, 11, 7],  "#ff7f0e"),  # orange
    ("ACM CCS",         [1, 10, 10, 0], "#2ca02c"),  # green
    ("NDSS",            [3, 2, 10, 15], "#d62728"),  # red
]

fig, ax = plt.subplots(figsize=(8.6, 4.6), dpi=150)
for name, vals, color in series:
    ax.plot(years, vals, marker="o", markersize=7, linewidth=2.2,
            color=color, label=name)
    for x, y in zip(years, vals):
        ax.annotate(str(y), (x, y), textcoords="offset points",
                    xytext=(0, 8), ha="center", fontsize=8.5, color=color)

ax.set_title("Security Top-4: IoT / Firmware Papers per Year",
             fontsize=13, fontweight="bold", pad=12)
ax.set_xlabel("Year", fontsize=11)
ax.set_ylabel("Number of papers", fontsize=11)
ax.set_xticks(years)
ax.set_ylim(-1, max(max(v) for _, v, _ in series) + 2)
ax.grid(True, linestyle="--", alpha=0.4)
ax.legend(title="Venue", loc="upper left", frameon=True, fontsize=10, title_fontsize=10)

ax.axvspan(2025.5, 2026.5, alpha=0.06, color="gray")
ax.text(2026, ax.get_ylim()[0] - (ax.get_ylim()[1] - ax.get_ylim()[0]) * 0.08,
        "2026: partial year (in progress)", ha="center", va="top",
        fontsize=8, color="dimgray", style="italic")

plt.tight_layout()
plt.savefig("assets/trend-security-top4.png", bbox_inches="tight", facecolor="white")
print("saved assets/trend-security-top4.png")
