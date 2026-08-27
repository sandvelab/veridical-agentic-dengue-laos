# Provenance — whether the recent case history enters — the count three months back

```
result:              results/autoregressive_lag3/model_option_spec.json
script:              scripts/choose_autoregressive.py
                     sha256:7ef7586d955b56f0c2b12be3e35f6f31e6d8f429d06fdeb4556f30863dbb4191
invocation:          "$PYTHON" scripts/choose_autoregressive.py
                     (from the node directory, via run.sh, driven by
                     AI-internal/useful-scripts/candidate_fork_sweep.py with
                     COMBO=autoregressive_lag3 and COMBO_BASE=main. PYTHON is
                     environment/chapenv/bin/python.)
inputs:              analysis/02_setup/results/main/analysis_dataset.csv
                     sha256:c9bf8b0849c768bfe6c65d54975dd08fa390204f8b59e76904170222a7a87d4c
                     resolved from combination `main`, because this combination moved
                     only this fork and inherits the common ground it did not move.
                     Recorded in the specification as `input_from_combo`.
environment:         environment/ (project main) — CPython 3.13.0, chap-core==2.1.0
seeds:               none. The stage states a choice and computes summary statistics of
                     stored columns; project seed 20260822 has no surface here.
commit:              15b8516
instructions-commit: cf97b81
node:                analysis/03_models/03_candidate/a_hierNB/05_autoregressive/b_lag3
produced:            2026-08-27
```

**What it establishes.** The lagged count is available for **2 324** of the 2 383
observed cells at lag 3, and it costs the first three months of each province's record
at fit time: 1 959 usable rows against the main path's 2 012.

**What the run of it established.** **23.345** mean CRPS against the main path's
23.698 — a gain of 0.353, inside the 0.57 floor and therefore not attributable. Around
the batch-8 configuration the same child was worth **−0.075**, so it moved from
marginally harmful to marginally helpful without either number meaning anything.

The premise predicted this. A lag-3 correlation of 0.701 against a lag-12 correlation
of 0.758 says the recent count is telling the model roughly what month of the year it
is, and the seasonal harmonics say that already. Batch 7's observation that a
persistence baseline is level with the reference at one month's lead does not carry to
three months, which is the only lead a single model can serve here.

alternatives-considered: A separate model per horizon, each using the freshest lag available to it, which
    would let the one-month forecast use a one-month lag; rejected because Chap fits one
    model and asks it for three months, so three models would be three entries on the
    leaderboard evaluated on overlapping cells — a different comparison from the one this
    project defines. Recorded because it is the version of this idea that might work.

agency: agent-autonomous

---

## Batch 21 addendum — promoted on the branch `greedy`, round 2, 2026-08-27

```
result:              results/main/model_option_spec.json
script:              scripts/choose_autoregressive.py   unchanged
invocation:          "$PYTHON" scripts/choose_autoregressive.py, from a_hierNB/run.sh with
                     COMBO=main and no COMBO_BASE, driven by
                     AI-internal/useful-scripts/greedy_iterate.py
commit:              cb61c1d
instructions-commit: cf97b81
produced:            2026-08-27
```

**This is the fork whose worth moved most, and it moved with the company it kept.** Three
measurements of the same child, each from a different configuration:

| measured around | worth |
|---|---|
| batch 8's defaults | **−0.075** |
| batch 9's promoted path (the main line) | +0.353 |
| the greedy branch after round 1 | **+0.582** |

Batch 9's conclusion — that a lagged-count term is worth nothing on this dataset at a
three-month lead — was true where it was measured. What round 1 changed is that the model
now refits inside every `predict` call, so at each split the lagged-count column is filled
from history the train-time fit never saw; the autoregressive term and the refit are
complements, and neither one alone shows it. This is the same non-additivity batch 9 found,
with the sign running the other way: there, three forks worth 4.632 together delivered
2.402; here, a fork worth nothing became worth something once another one moved.

**Promoted in round 2**, taking the branch from 21.857 to 21.275 — exactly the +0.582 the
sweep predicted, the only round in which the prediction and the outcome agreed to three
decimals, because only one fork moved.

**Nothing here is on `main`**, where this fork stays at `a_none`.

agency: agent-autonomous, under a human-set instruction to explore the iterated path on a
branch.
