[overview](../../../../../README.md) / [analysis](../../../../README.md) / [03_models](../../../README.md) / [01_baselines](../../README.md) / [01_persistence](../README.md) / **b_negBinomialFloor**

# b_negBinomialFloor

*On a path not taken — an alternative the reported analysis did not use. It is complete and runnable, and the stability analysis ran it.*

**Claim:** Wrap the persistence point in a negative binomial whose mean is the last observation and whose dispersion is fitted from recent observations, with a small floor on the mean so the distribution does not collapse when the last observation is zero. The second of the two published constructions, and the floor is an arbitrary constant doing visible work in the 56 percent of months that report zero.

**Result:**

**It scores 20.698 mean CRPS over the same 371 cells, against the main path's 24.879**
(`analysis/04_score/03_compare/results/persistence_negBinomialFloor/leaderboard.csv`). The
construction batch 6 rejected is **4.181 CRPS better** — more than seven times the 0.565 floor
below which nothing here can be attributed to a model — and better calibrated on both
intervals: 10–90 coverage 0.720 against 0.666, 25–75 coverage 0.550 against 0.491.

**It beats the reference model.** 20.698 against 22.098, a paired per-cell difference of
−1.400 with a split-clustered standard error of 1.424: 0.98 standard errors, which does not
separate them. A model the plan requires as a *baseline* is ahead of the field's own model
on the point estimate, and says something about the reference rather than about this node.

**The claim's own criticism holds and understates the problem.** The floor of 0.2 is an
arbitrary constant doing visible work in the 56 % of observed months that report zero — and
it is the *first* of two. On this dataset the maximum-likelihood dispersion frequently does
not exist: with an all-zero window the likelihood rises monotonically toward a point mass at
zero. The estimator therefore needs bounds, and on the training frame those bounds bind for
**six of the seventeen provinces that report at all** (`results/*/fitted_model.json`). The
second constant does its work in exactly the provinces where the first one does. The
construction is better anyway.

**Every constant is the source's**, not ours: floor 0.2, window of five observations,
dispersion by maximum likelihood, and the same distribution at every horizon, all from the
KIT baseline for the German COVID-19 Forecast Hub. A stability alternative chosen by us
could have been tuned against the path taken.

## Material

The node's own files: [`claim.md`](../../../../../../../analysis/03_models/01_baselines/01_persistence/b_negBinomialFloor/claim.md) · [`results/`](../../../../../../../analysis/03_models/01_baselines/01_persistence/b_negBinomialFloor/results) · [`scripts/`](../../../../../../../analysis/03_models/01_baselines/01_persistence/b_negBinomialFloor/scripts) · [`provenance/`](../../../../../../../analysis/03_models/01_baselines/01_persistence/b_negBinomialFloor/provenance) · [`run.sh`](../../../../../../../analysis/03_models/01_baselines/01_persistence/b_negBinomialFloor/run.sh).

---

> **A snapshot, generated 2026-09-27 from the tree at commit `3d89200`.** Everything here is derived from files the repository versions and regenerates in seconds with `.venv/bin/python AI-internal/useful-scripts/build_claim_tree_md.py` (or `/hierarchical-report`). If the tree has changed since that commit, rebuild rather than trust this copy; never hand-edit.
