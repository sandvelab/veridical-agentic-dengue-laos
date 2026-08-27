# The rule the greedy branch iterates

Branch `greedy`, batch 21. Written and committed **before the first round it decides was
run**, as batch 9's promotion rule was, and for the same reason: a rule fixed after the
numbers it selects on is not a rule, it is a description of the choice.

It is batch 9's promotion rule with one clause removed — the clause that said "applied
once". Everything else is identical, deliberately, so that what this branch measures is the
effect of *iterating*, and not the effect of iterating a different rule.

## The rule

Let the branch's current main path be the **base**, and let 0.57 CRPS be the floor batch 7
measured from the unseeded reference model's own four repeats — the smallest difference
that can be attributed to a model at all.

Repeat:

1. **Sweep.** Run one combination per non-main child of every fork under
   `03_models/03_candidate/a_hierNB`, around the base, through the tree's own scripts.
2. **Select.** A fork moves if and only if its best child beats the base by more than the
   floor. Where a fork moves it takes its best-scoring child.
3. **Stop** if no fork moves. The base is then the greedy fixpoint.
4. **Promote and run.** Move the main-path markers of the forks that moved, and run and
   score the promoted combination as the new base.
5. **Back off** if the promoted combination is worse than the best single-fork combination
   of that round by more than the floor: revert to that single fork alone, re-run, and
   record the interaction as the finding it is.
6. Go to 1.

**Round cap: 8.** A cap is not part of the rule's logic; it is the budget line `AGENTS.md`
§6 asks to be drawn in advance. If the iteration hits it, the report says the fixpoint was
*not* reached and what the last round still had outside the floor. Each round costs one
sweep of nine backtests plus one main-path run — about twenty minutes at the branch's
per-combination costs, more once a child that refits inside `predict` is on the path.

## What the first round's sweep is

Round 1's sweep is **not re-run**. Batch 9's second sweep
(`../round2_promoted/fork_leaderboard.csv`) was taken around exactly this base — the
configuration `28c7c617…` that closed batch 9 — and re-running it would spend eighteen
minutes to reproduce a table the branch already has. Our models are seeded and their
determinism is verified (`AI-generated/determinism-checks/model_determinism.json`), so the
re-run would produce the same numbers rather than a second draw. Round 1 therefore reads
that table, and the round record names the file it read.

## What this rule is not

**It is not a proposal for the main path.** `main` applies the rule once, by the human's
decision of 2026-08-27, and nothing on this branch is merged. The reported analysis is the
one that stopped.

**It is not a search for the best model.** Coordinate descent on a development score is not
that, and this branch is the demonstration rather than the counterexample: what it produces
is a model chosen by *k* rounds of selection on the same 371 cells it is then scored on.
The number the branch exists to produce is **how far development CRPS can be driven by
iterating a defensible-looking rule**, which is the quantity phase E's held-out year is set
up to catch and which this branch, by design, never checks.

**It does not open the holdout.** Not on this branch and not on any other. The one opening
the project has belongs to phase E and to the frozen manifest.
