[overview](../../../../../README.md) / [analysis](../../../../README.md) / [03_models](../../../README.md) / [03_candidate](../../README.md) / [a_hierNB](../README.md) / **03_population**

# 03_population

*On a path not taken — an alternative the reported analysis did not use. It is complete and runnable, and the stability analysis ran it.*

**Claim:** How does the province population enter the model? The file's population figure is one constant per province, and it can serve as a denominator the model forecasts a rate against, as an ordinary covariate, or not at all.

**Result:**

**How population enters our model does not matter here.** All three children score within
**0.18** CRPS of each other, well inside the 0.57 floor: the offset (the main path,
23.698), dropping population entirely (23.723) and estimating its coefficient (23.876)
(`round2_promoted/fork_leaderboard.csv`).

The reason is visible in the fits. The pooled province effect widens from sigma 1.27 with
the offset to **1.87** with population dropped, and narrows to **0.94** with the
coefficient estimated: the intercept and the population term are explaining the same thing,
and the column is constant within a province so an intercept can stand in for it exactly.

**The premise the offset rests on is nevertheless false.** Across provinces, log mean
reported cases rises **1.74** per unit of log population, where an offset asserts 1.00. It
costs nothing on this backtest because a per-province intercept absorbs the difference --
and it would cost something for a province the model had never seen, which this backtest
never asks about.

## Alternatives

Competing ways of answering this node's claim. The reported analysis takes the **main path**; the others are run by `05_stability`.

- [a_offset](a_offset/README.md) — **main path**  
  As a fixed offset, log population: the model forecasts an incidence rate and multiplies it back up by the province's size, so the fit never has to learn how large a …
- [b_covariate](b_covariate/README.md) — *not taken*  
  Population as an estimated coefficient on standardised log population rather than as a fixed offset, so the data decides how reported cases scale with province size …
- [c_ignored](c_ignored/README.md) — *not taken*  
  Population does not enter the model at all: a province's level is carried entirely by its own pooled intercept, which is estimated from its record rather than from its …

## Material

The node's own files: [`claim.md`](../../../../../../../analysis/03_models/03_candidate/a_hierNB/03_population/claim.md) · [`run.sh`](../../../../../../../analysis/03_models/03_candidate/a_hierNB/03_population/run.sh).

---

> **A snapshot, generated 2026-09-27 from the tree at commit `3d89200`.** Everything here is derived from files the repository versions and regenerates in seconds with `.venv/bin/python AI-internal/useful-scripts/build_claim_tree_md.py` (or `/hierarchical-report`). If the tree has changed since that commit, rebuild rather than trust this copy; never hand-edit.
