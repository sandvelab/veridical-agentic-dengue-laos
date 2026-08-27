# Provenance — candidate-forks/greedy

One section per file, appended and never overwritten (`AGENTS.md` §8). **Branch `greedy`
only.** Nothing recorded here is on `main` and nothing here is a reported result of the
project; it is evidence about the selection rule, produced by batch 21.

## greedy_rule.md — the rule the branch iterates

```
produced:            2026-08-27, batch 21, by hand
commit:              cb61c1d
```

Batch 9's promotion rule with the "applied once" clause removed and a round cap of 8 added.
Written and **committed before the first round it decided was run**, so that what it decides
cannot have been fitted to what it decided. A decision record, not a derived document.

## round_NN.json, round_NN.log — one record per round

```
produced:            2026-08-27, batch 21
script:              AI-internal/useful-scripts/greedy_iterate.py
invocation:          .venv/bin/python AI-internal/useful-scripts/greedy_iterate.py round \
                       --reuse-sweep round2_promoted          (round 1)
                     .venv/bin/python AI-internal/useful-scripts/greedy_iterate.py loop
                                                              (rounds 2 and 3)
inputs:              AI-generated/candidate-forks/round2_promoted/fork_leaderboard.csv
                       (round 1's sweep, reused -- see below)
                     AI-generated/candidate-forks/greedy/roundNN/fork_leaderboard.csv
                       (rounds 2 and 3, each written by candidate_fork_sweep.py)
                     analysis/03_models/03_candidate/a_hierNB/results/main/candidate_spec.json
                     analysis/04_score/02_aggregate/a_unweighted/results/main/metrics_summary.csv
                     analysis/results/main/conclusion.json
environment:         .venv (the repository's own machinery) drives; every step it runs
                     executes under environment/ (project main)
commit:              cb61c1d   (the scripts, throughout)
instructions-commit: cf97b81
```

Each record holds the base the round started from and its configuration hash, what every
fork's best child scored, which forks the rule moved and which it left, what the promoted
combination then scored, and the conclusion the tree computed afterwards. The rule is
applied by the script rather than by a reading of the table: the record is written before
the tree is touched.

**Round 1's sweep was reused, not re-run.** Batch 9's `../round2_promoted/` was taken around
exactly the configuration the branch starts from (`28c7c617d5c26fa0…`), and the driver
checks that recorded hash against the tree before believing it. Rounds 2 and 3 ran their own
sweeps, each of nine combinations, around the path as it then stood.

**Regenerable, at a price.** Re-running the three rounds from batch 9's closing commit
reproduces every number here: our models are seeded and verified deterministic. It costs
about half an hour of compute — **twenty backtests**, 1 350 seconds of them in the two
sweeps and three more main-path runs on top, at 26 to 94 seconds each depending on how many
EM rounds the combination's variance structure needs.

## greedy_path.json — the trajectory across rounds

```
produced:            2026-08-27, batch 21
script:              AI-internal/useful-scripts/greedy_iterate.py (loop)
inputs:              round_01.json, round_02.json, round_03.json
commit:              cb61c1d
```

Copied from the round records; nothing is computed here that is not a difference of two
numbers already in them.

## greedy_trajectory.png, greedy_trajectory.csv, greedy_trajectory_children.csv

```
produced:            2026-08-27, batch 21
script:              AI-internal/useful-scripts/greedy_trajectory.py
invocation:          environment/chapenv/bin/python \
                       AI-internal/useful-scripts/greedy_trajectory.py
inputs:              round_01.json, round_02.json, round_03.json
                     analysis/04_score/02_aggregate/a_unweighted/results/main/metrics_summary.csv
                       (the reference and both baselines, which do not move)
seeds:               none; a deterministic summary of stored scores
commit:              cb61c1d
instructions-commit: cf97b81
```

Rule 7: `greedy_trajectory.csv` is the plotted line, `greedy_trajectory_children.csv` the
pre-aggregation values — every child every round's sweep measured, which is what the rule
chose from — and the plotting script is named above.

## roundNN/ — each round's own sweep

```
produced:            2026-08-27, batch 21
script:              AI-internal/useful-scripts/candidate_fork_sweep.py run --label greedy/roundNN
inputs:              analysis/04_score/02_aggregate/a_unweighted/results/<combo>/metrics_summary.csv
                     analysis/03_models/03_candidate/a_hierNB/results/<combo>/run_cost.json
                     analysis/03_models/03_candidate/a_hierNB/results/<combo>/candidate_spec.json
commit:              cb61c1d
instructions-commit: cf97b81
```

The same driver, the same format and the same inheritance as every other sweep in the
project: one combination per non-main child, everything the combination did not move
inherited from `main` and recorded as inherited, and the reference never re-run.
`round03/` is the sweep that found no fork outside the floor, and is therefore the evidence
that the branch stopped at a fixpoint rather than at a budget line.

**The per-combination results behind `round02/` are gone, and unlike batch 9's round 1 they
are not in git.** Round 3 re-measured the same combination names around the moved main path
and replaced them, and because the loop ran all three rounds unattended between one commit
and the next, no commit ever held them. What survives is `round02/fork_leaderboard.csv`,
`round02/sweep_*.log` and `round_02.json` — the table the round's promotion was decided
from, and the transcript of the commands that produced it. Recovering the files themselves
means re-running the branch from `cb61c1d`, which is deterministic and costs about forty
minutes. This is the price of automating the loop, and batch 9's hand-run rounds did not
pay it.
