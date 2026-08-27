# The greedy branch's rounds

**Branch `greedy`, batch 21. Nothing here is a reported result of the project**, and
nothing here is on `main`. The reported analysis applies batch 9's promotion rule once and
stops; this directory is what happens when the same rule is iterated to a fixpoint.

- `greedy_rule.md` — the rule, committed before the first round it decided was run. It is
  batch 9's promotion rule with the "applied once" clause removed and a round cap added.
- `round_NN.json` — one record per round: the base it started from, what every fork's best
  child scored, which forks the rule moved and which it left, what the promoted combination
  then scored, and the conclusion the tree computed afterwards. This is the file the rule's
  decisions are recorded in, and it is written by
  `AI-internal/useful-scripts/greedy_iterate.py` rather than by a reading of a table.
- `round_NN.log` — the commands each round ran, in order.
- `greedy_path.json` — the trajectory across rounds, and the final main path.
- `roundNN/` — each round's own sweep, in the format `candidate_fork_sweep.py` writes for
  every other sweep in the project.
- `greedy_trajectory.png`, `.csv`, `_children.csv` — the figure, its plotted values, and the
  pre-aggregation values: every child every round measured.
- `provenance.md` — one section per file (`AGENTS.md` §8).

Round 1's sweep is batch 9's `../round2_promoted/`, reused rather than re-run: it was taken
around exactly the configuration this branch starts from, and our models are seeded.

## What it found

Three rounds and then a fixpoint: 23.698 → 21.857 → **21.275** mean CRPS, past the
reference model's 22.098 and past each of its four repeats. The fourth sweep found the best
remaining move worth 0.150 CRPS, a quarter of the resolvable floor, so the branch stopped
because the rule ran out and not because the round cap bound.

It changes nothing the project can conclude — the paired difference against the reference is
half a standard error — and it costs the model's fitted object, because the first fork the
rule moved is the one that fits inside `predict` and stores nothing.
