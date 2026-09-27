[overview](../../../README.md) / [analysis](../../README.md) / [03_models](../README.md) / **01_baselines**

# 01_baselines

**Claim:** How well does the problem's own inertia forecast it? Two baselines the plan requires: what the series did last, and what the series usually does in this calendar month.

**Result:**

Both baselines the plan's §4 requires are implemented against the Chap contract and
evaluated through the identical path. **Seasonal climatology scores 24.337 mean CRPS and
persistence 24.879**, over the same 371 cells
(`04_score/02_aggregate/a_unweighted/results/main/metrics_summary.csv`).

The two are 0.54 CRPS apart, which is at the edge of what this evaluation can resolve — the
reference's own re-runs move by up to 0.57 — so the honest reading is that **knowing the
season and knowing the last observation are worth about the same here**, not that one
baseline is better. Their calibration differs more than their score does: climatology's
central interval is too wide (0.542 against a nominal 0.50) where persistence's is almost
exact (0.491), and both have tails far too thin (0.650 and 0.666 against 0.80).

Both contain no randomness, and that is verified rather than asserted: two independent runs
of each produced identical per-cell scores and identical fitted models
(`AI-generated/determinism-checks/model_determinism.json`).

**Batch 22 ran both baselines' alternative constructions, and they are the two extremes of
the stability set so far.** Wrapping the persistence point in a fitted negative binomial
rather than in the empirical distribution of past changes is worth **4.181 CRPS** (24.879 →
20.698) and takes the baseline past the reference model; freezing the climatology's estimation
window is worth **0.532 CRPS** (24.337 → 24.869), inside the noise floor. The better
persistence construction reaches the reported model too, because the pool takes both baselines
as members — and makes it **worse**, 18.817 → 19.434.

So the honest reading of "knowing the season and knowing the last observation are worth about
the same here" is narrower than it looked: it is true of the two constructions the main path
happens to run, and knowing the last observation is worth considerably more when its
uncertainty is wrapped the other published way.

## Sub-analyses

- [01_persistence](01_persistence/README.md)  
  How well does the last observed count forecast the next three months? A persistence forecast is a point, and CRPS scores a distribution, so the baseline is only defined …
- [02_climatology](02_climatology/README.md)  
  How well does the seasonal average forecast the next three months? For each province and calendar month, the empirical distribution of the counts observed in that month …

## Material

The node's own files: [`claim.md`](../../../../../analysis/03_models/01_baselines/claim.md) · [`run.sh`](../../../../../analysis/03_models/01_baselines/run.sh).

---

> **A snapshot, generated 2026-09-27 from the tree at commit `3d89200`.** Everything here is derived from files the repository versions and regenerates in seconds with `.venv/bin/python AI-internal/useful-scripts/build_claim_tree_md.py` (or `/hierarchical-report`). If the tree has changed since that commit, rebuild rather than trust this copy; never hand-edit.
