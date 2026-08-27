#!/usr/bin/env python3
"""Iterate batch 9's promotion rule to a fixpoint, on the `greedy` branch.

Batch 9 applied its promotion rule once and stopped, because iterating it is greedy
coordinate descent on development CRPS -- the failure the plan's phase C names, and one
that a single held-out year cannot diagnose. The cost of stopping was stated rather than
hidden. This script pays that cost out, on a branch that is never merged, so that the cost
is a measured quantity.

**The rule is executed by this file, not by a reading of a table.** It is written out in
`AI-generated/candidate-forks/greedy/greedy_rule.md`, which was committed before the first
round it decides was run. What the code adds is that no number crosses from a sweep to a
promotion through anyone's attention: each round reads the leaderboard the tree wrote,
writes down which forks its rule moves and why, and only then touches the tree.

## What one round is

1. **Sweep** -- one combination per non-main child of every fork under the candidate,
   around the current main path, driven by `candidate_fork_sweep.py` so that the branch and
   the main line measure forks the same way. Round 1 reuses batch 9's second sweep, which
   was taken around exactly this base; `--reuse-sweep` names it and the base configuration
   hash is checked before it is believed.
2. **Select** -- a fork moves if its best child beats the base by more than the floor
   (0.57 CRPS, batch 7's measured resolution). Where it moves it takes its best child.
3. **Promote** -- `node.py promote` per moved fork, and the results that described the old
   main path are removed rather than renamed, for batch 9's reason: a specification file
   records the combination it was produced under, so a renamed directory would contradict
   its own contents.
4. **Run** -- the promoted combination as the new main path, through the candidate node and
   the whole scoring chain, ending in the same `conclusion.json` the reported analysis
   ends in. The reference and the baselines are not re-run: nothing this branch moves
   changes what they face, and the reference is unseeded.
5. **Back off** -- if the promoted combination is worse than the round's best single-fork
   combination by more than the floor, the promotion is reverted to that fork alone and
   re-run.

The round writes `round_NN.json` under `AI-generated/candidate-forks/greedy/`, which is the
record the next round's base is read from, and stops the loop when no fork moves.

Run from the repository root:
  .venv/bin/python AI-internal/useful-scripts/greedy_iterate.py loop \
      --reuse-sweep round2_promoted
  .venv/bin/python AI-internal/useful-scripts/greedy_iterate.py loop --max-rounds 2
"""

from __future__ import annotations

import argparse
import csv
import json
import os
import shutil
import subprocess
import sys
import time
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import candidate_fork_sweep as sweep  # noqa: E402

ROOT = sweep.ROOT
CANDIDATE = sweep.CANDIDATE
OUT = ROOT / "AI-generated/candidate-forks/greedy"
AGGREGATE = ROOT / "analysis/04_score/02_aggregate/a_unweighted/results"
VENV = ROOT / ".venv/bin/python"
PYTHON = ROOT / "environment/chapenv/bin/python"

# Batch 7's measured resolution: the largest difference the unseeded reference model shows
# against its own repeats, and therefore the smallest movement attributable to a model.
FLOOR = 0.57
ROUND_CAP = 8


# --------------------------------------------------------------------------- the base

def base_state() -> dict:
    """What the branch's current main path is, read from the files the tree wrote."""
    spec = json.loads((CANDIDATE / "results/main/candidate_spec.json").read_text())
    summary = {row["model"]: row for row in
               csv.DictReader((AGGREGATE / "main/metrics_summary.csv").open())}
    return {
        "configuration_sha256": spec["configuration_sha256"],
        "mean_crps": float(summary["hier_nb"]["mean_crps"]),
        "crps_reference": float(summary["reference"]["mean_crps"]),
        "main_path": {fork.name: sweep.field((fork / "claim.md").read_text(), "main-path")
                      for fork, _, _ in sweep.forks()},
    }


# --------------------------------------------------------------------------- the sweep

def run_sweep(label: str, log) -> Path:
    out = sweep.OUT_ROOT / label
    step([str(VENV), str(HERE / "candidate_fork_sweep.py"), "run", "--label", label], log)
    return out


def check_sweep_base(out: Path, base: dict) -> None:
    """Refuse a table that was not measured around the configuration we are selecting on."""
    recorded = json.loads((out / "fork_sweep.json").read_text())["base_configuration_sha256"]
    if recorded != base["configuration_sha256"]:
        raise SystemExit(
            f"{out.name} was taken around {recorded}, and the branch's main path is "
            f"{base['configuration_sha256']}. A selection made on a table measured "
            "around a different configuration is not this rule.")


# --------------------------------------------------------------------------- the rule

def select(out: Path, base: dict) -> list[dict]:
    """Apply the rule to one sweep. One row per fork, whether or not it moves."""
    rows = {row["combo"]: row for row in
            csv.DictReader((out / "fork_leaderboard.csv").open())}
    decided = []
    for fork, main, siblings in sweep.forks():
        scored = []
        for child in siblings:
            combo = sweep.combination(fork, child)
            if combo in rows:
                scored.append((float(rows[combo]["mean_crps"]), child.name, combo))
        if not scored:
            continue
        scored.sort()
        best_crps, best_child, best_combo = scored[0]
        effect = base["mean_crps"] - best_crps
        decided.append({
            "fork": fork.name,
            "on_the_main_path": main,
            "best_child": best_child,
            "best_combination": best_combo,
            "best_child_mean_crps": best_crps,
            "effect_on_the_base": effect,
            "clears_the_floor": effect > FLOOR,
            "children_scored": {child: crps for crps, child, _ in scored},
        })
    return decided


# ------------------------------------------------------------------- moving the tree

def combination_directories(combo: str) -> list[Path]:
    """Every place in the tree that holds results for one combination."""
    return [CANDIDATE / "results" / combo,
            CANDIDATE / "work" / combo,
            ROOT / "analysis/04_score/01_collect/results" / combo,
            AGGREGATE / combo]


def promote(fork_name: str, child_name: str, log) -> dict:
    """Make `child_name` the main path of `fork_name`, and clear what contradicts it.

    The demoted child's `results/main/` goes, because two children of one fork with
    results under one combination is a configuration `assemble_candidate_config.py`
    refuses on purpose. The promoted child's own combination goes with it: it is the main
    path now, not an alternative to it, and the next sweep will name the demoted child's
    combination instead.
    """
    fork = CANDIDATE / fork_name
    old = sweep.field((fork / "claim.md").read_text(), "main-path")
    step([str(VENV), str(HERE / "node.py"), "promote",
          str(fork.relative_to(ROOT)), child_name], log)

    removed = []
    for path in [fork / old / "results/main",
                 fork / child_name / "results" / sweep.combination(fork, fork / child_name),
                 *combination_directories(sweep.combination(fork, fork / child_name))]:
        if path.exists():
            shutil.rmtree(path)
            removed.append(str(path.relative_to(ROOT)))
    log.write(f"# promoted {fork_name}: {old} -> {child_name}\n")
    for path in removed:
        log.write(f"#   removed {path}\n")
    log.flush()
    return {"fork": fork_name, "from": old, "to": child_name, "removed": removed}


# ------------------------------------------------------------------- running the path

def step(command: list[str], log, environment: dict | None = None) -> None:
    log.write("$ " + " ".join(command) + "\n")
    log.flush()
    result = subprocess.run(command, stdout=log, stderr=subprocess.STDOUT,
                            env={**os.environ, **(environment or {})}, cwd=str(ROOT))
    if result.returncode != 0:
        raise SystemExit(f"failed ({result.returncode}): {' '.join(command)}; "
                         f"see {log.name}")


def run_main(log) -> float:
    """Run the branch's main path from the candidate down to the conclusion.

    Not `analysis/run.sh`: the data, the setup, the baselines and the reference are
    untouched by anything this branch moves, and the reference is unseeded, so re-running
    it would replace its four repeats with a different draw and move the denominator of
    every comparison for reasons unrelated to the promotion. Everything below the
    candidate is re-run, because that is where the promotion's effect has to appear.
    """
    environment = {"COMBO": "main"}
    os.environ.pop("COMBO_BASE", None)
    started = time.time()
    step(["bash", str(CANDIDATE / "run.sh")], log, environment)
    for node in ("04_score/01_collect", "04_score/02_aggregate", "04_score/03_compare"):
        step(["bash", str(ROOT / "analysis" / node / "run.sh")], log, environment)
    step([str(PYTHON), str(ROOT / "analysis/scripts/conclude.py")], log, environment)
    log.write(f"# main path re-run in {time.time() - started:.0f} s\n")
    return base_state()["mean_crps"]


# ------------------------------------------------------------------------- the round

def one_round(number: int, reuse: str | None) -> dict:
    OUT.mkdir(parents=True, exist_ok=True)
    label = f"greedy/round{number:02d}"
    log_path = OUT / f"round_{number:02d}.log"
    base = base_state()

    with log_path.open("w") as log:
        log.write(f"# round {number}: base {base['configuration_sha256'][:12]}, "
                  f"mean CRPS {base['mean_crps']:.3f}\n\n")
        if reuse:
            out = sweep.OUT_ROOT / reuse
            log.write(f"# sweep reused from {out.relative_to(ROOT)}\n")
        else:
            out = run_sweep(label, log)
        check_sweep_base(out, base)

        decided = select(out, base)
        moving = [row for row in decided if row["clears_the_floor"]]
        record = {
            "round": number,
            "floor_crps": FLOOR,
            "base_configuration_sha256": base["configuration_sha256"],
            "base_mean_crps": base["mean_crps"],
            "base_main_path": base["main_path"],
            "sweep": str(out.relative_to(ROOT)),
            "sweep_reused": bool(reuse),
            "forks": decided,
            "forks_moving": [row["fork"] for row in moving],
            "sum_of_the_moving_forks_effects": sum(row["effect_on_the_base"]
                                                   for row in moving),
        }

        if not moving:
            record["fixpoint"] = True
            log.write("# no fork clears the floor: this base is the greedy fixpoint\n")
        else:
            record["fixpoint"] = False
            best_single = min(moving, key=lambda row: row["best_child_mean_crps"])
            record["best_single_fork"] = {
                "combination": best_single["best_combination"],
                "mean_crps": best_single["best_child_mean_crps"],
            }
            record["promotions"] = [promote(row["fork"], row["best_child"], log)
                                    for row in moving]
            record["promoted_mean_crps"] = run_main(log)
            record["gain"] = base["mean_crps"] - record["promoted_mean_crps"]
            record["one_at_a_time_overstates_the_gain_by"] = (
                record["sum_of_the_moving_forks_effects"] - record["gain"])
            # Clause 5. Promoting several forks at once asserts that their effects
            # combine, and a one-at-a-time sweep tests no such thing.
            worse_by = (record["promoted_mean_crps"]
                        - best_single["best_child_mean_crps"])
            record["worse_than_the_best_single_fork_by"] = worse_by
            record["backed_off"] = worse_by > FLOOR
            if record["backed_off"]:
                log.write(f"# clause 5: the promoted combination is {worse_by:.3f} CRPS "
                          f"worse than {best_single['best_combination']}; backing off\n")
                reverted = []
                for promotion in record["promotions"]:
                    if promotion["fork"] != best_single["fork"]:
                        reverted.append(promote(promotion["fork"], promotion["from"], log))
                record["reverted"] = reverted
                record["promoted_mean_crps"] = run_main(log)
                record["gain"] = base["mean_crps"] - record["promoted_mean_crps"]
            record["conclusion_after_the_round"] = json.loads(
                (ROOT / "analysis/results/main/conclusion.json").read_text())

    (OUT / f"round_{number:02d}.json").write_text(
        json.dumps(record, indent=1, sort_keys=True) + "\n")
    return record


def show(record: dict) -> None:
    print(f"\n== round {record['round']}: base {record['base_mean_crps']:.3f} CRPS")
    for row in record["forks"]:
        mark = "MOVES" if row["clears_the_floor"] else "     "
        print(f"  {mark}  {row['fork']:<20} {row['best_child']:<20} "
              f"{row['best_child_mean_crps']:7.3f}  {row['effect_on_the_base']:+7.3f}")
    if record["fixpoint"]:
        print("  no fork clears the floor -- fixpoint")
    else:
        print(f"  promoted {', '.join(record['forks_moving'])} -> "
              f"{record['promoted_mean_crps']:.3f} CRPS "
              f"(one at a time predicted "
              f"{record['base_mean_crps'] - record['sum_of_the_moving_forks_effects']:.3f})")


def loop(start: int, max_rounds: int, reuse: str | None) -> int:
    history = []
    for offset in range(max_rounds):
        number = start + offset
        if number > ROUND_CAP:
            print(f"round cap {ROUND_CAP} reached; the fixpoint was not")
            break
        record = one_round(number, reuse if offset == 0 else None)
        history.append(record)
        show(record)
        if record["fixpoint"]:
            break
    if history:
        trail = OUT / "greedy_path.json"
        rounds = sorted(int(p.stem.split("_")[1]) for p in OUT.glob("round_*.json"))
        every = [json.loads((OUT / f"round_{n:02d}.json").read_text()) for n in rounds]
        trail.write_text(json.dumps({
            "rounds": len(every),
            "reached_the_fixpoint": every[-1]["fixpoint"],
            "round_cap": ROUND_CAP,
            "floor_crps": FLOOR,
            "started_at_mean_crps": every[0]["base_mean_crps"],
            "ended_at_mean_crps": every[-1]["base_mean_crps"],
            "total_gain": every[0]["base_mean_crps"] - every[-1]["base_mean_crps"],
            "trajectory": [{"round": r["round"], "base_mean_crps": r["base_mean_crps"],
                            "moved": r["forks_moving"],
                            "promoted_mean_crps": r.get("promoted_mean_crps")}
                           for r in every],
            "final_main_path": every[-1]["base_main_path"],
            "source": "AI-generated/candidate-forks/greedy/round_NN.json",
        }, indent=1, sort_keys=True) + "\n")
        print(f"\n-> {trail.relative_to(ROOT)}")
    return 0


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    sub = parser.add_subparsers(dest="command", required=True)
    for name in ("loop", "round"):
        p = sub.add_parser(name)
        p.add_argument("--start", type=int, default=None,
                       help="round number; default is one past the last recorded round")
        p.add_argument("--reuse-sweep", default=None,
                       help="a sweep label under AI-generated/candidate-forks/ taken "
                            "around the current main path, to select on instead of "
                            "running a new one")
        if name == "loop":
            p.add_argument("--max-rounds", type=int, default=ROUND_CAP)
    args = parser.parse_args(argv)

    done = sorted(int(p.stem.split("_")[1]) for p in OUT.glob("round_*.json"))
    start = args.start or (done[-1] + 1 if done else 1)
    return loop(start, getattr(args, "max_rounds", 1), args.reuse_sweep)


if __name__ == "__main__":
    sys.exit(main())
