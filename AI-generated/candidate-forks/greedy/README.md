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
- `../greedy_roundNN/` under `AI-generated/candidate-forks/greedy/round*/` — each round's
  own sweep, in the format `candidate_fork_sweep.py` writes for every other sweep.

Round 1's sweep is batch 9's `../round2_promoted/`, reused rather than re-run: it was taken
around exactly the configuration this branch starts from, and our models are seeded.
