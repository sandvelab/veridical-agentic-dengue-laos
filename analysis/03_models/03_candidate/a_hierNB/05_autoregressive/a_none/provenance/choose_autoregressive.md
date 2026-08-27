# Provenance — whether the recent case history enters — it does not (main path)

```
result:              results/main/model_option_spec.json
script:              scripts/choose_autoregressive.py
                     sha256:89a2f5068038495ff4fb8109a4273ed06dd3a7d64c9bf5ed3b69db656165a58a
invocation:          "$PYTHON" scripts/choose_autoregressive.py
                     (from the node directory, via run.sh, with COMBO unset, so the
                     combination is `main` and results go to results/main/. PYTHON is
                     environment/chapenv/bin/python.)
inputs:              analysis/02_setup/results/main/analysis_dataset.csv
                     sha256:c9bf8b0849c768bfe6c65d54975dd08fa390204f8b59e76904170222a7a87d4c
environment:         environment/ (project main) — CPython 3.13.0, chap-core==2.1.0
seeds:               none. The stage states a choice and computes summary statistics of
                     stored columns; project seed 20260822 has no surface here.
commit:              15b8516
instructions-commit: cf97b81
node:                analysis/03_models/03_candidate/a_hierNB/05_autoregressive/a_none
produced:            2026-08-27
```

**What it establishes.** The information the main path declines to use, measured
rather than argued: within a province, log1p case counts correlate **0.701** at three
months' lag and **0.758** at twelve. Twelve months is the seasonal cycle the harmonics
already carry, so the lagged count is not obviously carrying anything the calendar
does not — which is the premise on which this child rests.

**Why this node exists at all.** Batch 8 declined to add an autoregressive term inside
the four forks it had, on the grounds that a structural term added outside the forks
would be exactly the silent judgment call this project exists to make visible. This
node is that call made visible: the term batch 8 declined is `b_lag3`, and declining
it is now a child with a claim, a premise and a score rather than a paragraph in a
report.

alternatives-considered: `b_lag3`, the term itself, built and run in this batch. A lag of one or two months,
    which correlate more strongly (0.882 and 0.791) and are not available at the third of
    Chap's three forecast months; not a fork, because a model that cannot forecast the
    third month is not a model this evaluation can score.

agency: agent-autonomous

---

## Batch 21 addendum — demoted on the branch `greedy`, round 2, 2026-08-27

```
result:              results/autoregressive_none/model_option_spec.json
                     (its results/main/ was removed when the fork moved)
script:              scripts/choose_autoregressive.py   unchanged
invocation:          "$PYTHON" scripts/choose_autoregressive.py, from this node's run.sh
                     with COMBO=autoregressive_none and COMBO_BASE=main, driven by
                     AI-internal/useful-scripts/candidate_fork_sweep.py
commit:              cb61c1d
instructions-commit: cf97b81
produced:            2026-08-27
```

**Dropping the lagged-count term costs 0.582 CRPS on this branch** (21.857 against the
fixpoint's 21.275) and **nothing at all on `main`**, where the same measurement, taken
around a model that fits only in train, put the term inside the resolvable floor. The
difference between those two statements is not about this child; it is about what else the
model was doing when the question was asked.

**On `main` this is the main path.**

agency: agent-autonomous, under a human-set instruction to explore the iterated path on a
branch.
