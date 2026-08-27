#!/usr/bin/env python3
"""What iterating the promotion rule did to development CRPS, round by round.

One figure and the values behind it (Rule 7). The line is the branch's main path after
each round; the points around it are every child every round's sweep measured, which is
what the rule chose from. The reference model and the two required baselines are drawn as
fixed levels, because they do not move: nothing this branch changes is visible to them.

**The figure's subject is the selection, not the model.** A line that walks downward past
the reference is what greedy coordinate descent on a development score looks like when it
is working as designed, and the question the branch exists to raise -- how much of the walk
is the model getting better and how much is it fitting 371 cells -- is not answerable from
anything drawn here. Only the held-out year answers it, and this branch never opens it.

Plotted values:        AI-generated/candidate-forks/greedy/greedy_trajectory.csv
Pre-aggregation values: AI-generated/candidate-forks/greedy/greedy_trajectory_children.csv
Seeds: none; a deterministic summary of stored scores.

Run from the repository root:
  .venv/bin/python AI-internal/useful-scripts/greedy_trajectory.py
"""

from __future__ import annotations

import csv
import json
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

ROOT = Path(__file__).resolve().parents[2]
GREEDY = ROOT / "AI-generated/candidate-forks/greedy"
AGGREGATE = ROOT / "analysis/04_score/02_aggregate/a_unweighted/results/main/metrics_summary.csv"
FLOOR = 0.57


def main() -> None:
    rounds = [json.loads(p.read_text()) for p in sorted(GREEDY.glob("round_*.json"))]
    fixed = {row["model"]: float(row["mean_crps"]) for row in
             csv.DictReader(AGGREGATE.open())
             if row["model"] in ("reference", "climatology", "persistence")}

    # The line: the main path before round 1, and after each round that moved it.
    line = [{"after_round": 0, "mean_crps": rounds[0]["base_mean_crps"],
             "moved": "", "note": "batch 9's promoted candidate, where the branch starts"}]
    for record in rounds:
        if record["fixpoint"]:
            line.append({"after_round": record["round"],
                         "mean_crps": record["base_mean_crps"], "moved": "",
                         "note": "no fork clears the floor: the greedy fixpoint"})
        else:
            line.append({"after_round": record["round"],
                         "mean_crps": record["promoted_mean_crps"],
                         "moved": " + ".join(record["forks_moving"]),
                         "note": f"gain {record['gain']:+.3f}, one at a time predicted "
                                 f"{record['sum_of_the_moving_forks_effects']:+.3f}"})

    with (GREEDY / "greedy_trajectory.csv").open("w", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(line[0]), lineterminator="\n")
        writer.writeheader()
        writer.writerows(line)

    children = []
    for record in rounds:
        for fork in record["forks"]:
            for child, crps in fork["children_scored"].items():
                children.append({"round": record["round"], "fork": fork["fork"],
                                 "child": child, "mean_crps": crps,
                                 "effect_on_the_base": record["base_mean_crps"] - crps,
                                 "chosen": child == fork["best_child"]
                                           and fork["clears_the_floor"]})
    with (GREEDY / "greedy_trajectory_children.csv").open("w", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(children[0]), lineterminator="\n")
        writer.writeheader()
        writer.writerows(children)

    figure, axes = plt.subplots(figsize=(8.4, 5.0))
    for name, style in (("reference", dict(color="#444444", linestyle="-")),
                        ("climatology", dict(color="#999999", linestyle=":")),
                        ("persistence", dict(color="#999999", linestyle="-."))):
        axes.axhline(fixed[name], linewidth=1, **style)
        axes.annotate(f"{name} {fixed[name]:.2f}", (-0.06, fixed[name]),
                      fontsize=8, va="bottom", ha="left", color=style["color"])
    axes.axhspan(fixed["reference"] - FLOOR, fixed["reference"] + FLOOR,
                 color="#444444", alpha=0.07, linewidth=0)

    axes.scatter([row["round"] - 1 for row in children],
                 [row["mean_crps"] for row in children],
                 s=14, color="#c0c0c0", zorder=2,
                 label="every child each round's sweep measured")
    axes.plot([row["after_round"] for row in line], [row["mean_crps"] for row in line],
              marker="o", color="#b2182b", zorder=3, label="the branch's main path")
    for row in line:
        axes.annotate(f"{row['mean_crps']:.2f}", (row["after_round"], row["mean_crps"]),
                      textcoords="offset points", xytext=(0, -14), ha="center",
                      fontsize=8, color="#b2182b")

    axes.set_xlabel("rounds of the promotion rule applied")
    axes.set_ylabel("development mean CRPS, 371 cells")
    axes.set_title("Iterating batch 9's promotion rule to a fixpoint (branch `greedy`)",
                   fontsize=10)
    axes.set_xticks([row["after_round"] for row in line])
    axes.legend(fontsize=8, frameon=False, loc="lower left")
    axes.annotate("shaded: the 0.57 CRPS floor either side of the reference —\n"
                  "differences inside it cannot be attributed to a model",
                  (len(line) - 1.05, fixed["reference"] + FLOOR), fontsize=7,
                  color="#666666", ha="right", va="bottom")
    axes.spines[["top", "right"]].set_visible(False)
    figure.tight_layout()
    figure.savefig(GREEDY / "greedy_trajectory.png", dpi=160)
    print(f"-> {(GREEDY / 'greedy_trajectory.png').relative_to(ROOT)}")


if __name__ == "__main__":
    main()
