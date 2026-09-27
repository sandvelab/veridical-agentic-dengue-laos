[overview](../../README.md) / [analysis](../README.md) / **03_models**

# 03_models

**Claim:** What forecast does each model make on that common ground? The node holds every model the project scores — our baselines, our candidates and the external reference — so that all of them traverse the identical evaluation path.

**Result:**

Three models have run on the common ground, all through the same `chap eval` path: the two
baselines the plan requires and the external reference. Their scores are computed at
`04_score`, not here.

What this node establishes about *how* they were run: a model of ours reaches the platform
through exactly one piece of code (`scripts/lib/chap_eval.py`), which reads the dataset and
every backtest flag from `02_setup` and hashes the model's own files into its spec before
the run. So the constraint the plan states for phase C — that no candidate is compared on a
metric computed a different way — holds structurally rather than by care.

**A native model of ours costs about 28 seconds for a full eight-split backtest; the
emulated reference costs about 268 seconds per repeat**, four repeats to a combination
(`*/results/main/run_cost.json`). Implementation effort, not evaluation, is what binds this
project, which is what batch 4 concluded from one measurement and what two more confirm.

## Claims resting on this node

- **[C29](../../claims.md#c29)** — The reported model is cheaper to run than the model it beats. One eight-split evaluation of the pool takes 59.5 seconds natively; one repeat of the reference takes between 241 and 285 seconds through an amd64 image under emulation, and the reported reference figure needs four of them, at 1 070 seconds.
- **[C37](../../claims.md#c37)** — Every model this project wrote reproduces byte-identically when it is run again -- per-cell scores, model listing and fitted object, for all seven of them. The reference model cannot be made to do this: it calls its sampler without ever setting a seed and the service exposes no seed, so its variability is quantified by repetition instead of removed.

## Sub-analyses

- [01_baselines](01_baselines/README.md)  
  How well does the problem's own inertia forecast it? Two baselines the plan requires: what the series did last, and what the series usually does in this calendar month.
- [02_reference](02_reference/README.md) · 1 claim  
  What does the field's own model score on this dataset? WHO EWARS-csd as published at chapkit_ewars_model, at its own default configuration, pinned by image digest and …
- [03_candidate](03_candidate/README.md)  
  Which model family should our candidate be? Each child is one family — one possible answer to the same question of what forecast our model makes — so exactly one of them …

## Material

The node's own files: [`claim.md`](../../../../analysis/03_models/claim.md) · [`scripts/`](../../../../analysis/03_models/scripts) · [`run.sh`](../../../../analysis/03_models/run.sh).

---

> **A snapshot, generated 2026-09-27 from the tree at commit `3d89200`.** Everything here is derived from files the repository versions and regenerates in seconds with `.venv/bin/python AI-internal/useful-scripts/build_claim_tree_md.py` (or `/hierarchical-report`). If the tree has changed since that commit, rebuild rather than trust this copy; never hand-edit.
