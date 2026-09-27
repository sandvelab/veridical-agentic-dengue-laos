[overview](../../../README.md) / [analysis](../../README.md) / [04_score](../README.md) / **03_compare**

# 03_compare

**Claim:** How do the models compare, and can the comparison separate them? The leaderboard from the stored scores, and the paired per-cell difference against the reference with its spread — the paired form because forecasting difficulty varies far more between periods than between models, and that variation is common to both sides.

**Result:**

**The paired comparison is roughly three times tighter than the unpaired one, and it is
still not tight enough to separate a 2 CRPS difference.** That is the answer to the question
batch 4 left open, and it changes what phase C has to aim at.

The numbers, all in `results/main/paired_summary.csv` and `comparison_notes.json`:

- the unpaired standard error of the reference's own CRPS across splits is **5.68** — the
  figure batch 4 reported, recomputed here;
- pairing cell by cell brings the standard error of a model difference to **1.34** for
  climatology and **2.05** for persistence, if the 371 cells are treated as independent;
- clustering by split — which allows the cells inside a split to be correlated in any way,
  and they are — gives **1.92** and **2.99**;
- climatology is **2.24 CRPS worse** than the reference and persistence **2.78** worse. Both
  differences are inside two clustered standard errors of zero.

So the comparison's resolution on this dataset is about **4 CRPS at anything like
conventional confidence** — wider than the entire gap between the persistence baseline and
the reference. A candidate that beats the reference by one or two CRPS on the development
backtest will not have been shown to beat it.

Two further findings sharpen that. The per-cell win rate is **44 %** for climatology and
**47 %** for persistence: at the level of an individual province-month the baselines and the
reference are close to a coin flip, and the reference's advantage comes from a minority of
cells rather than from being broadly better. And the reference's own unseeded repeats differ
by up to **0.57 CRPS** in the same paired statistic, which is the floor below which nothing
can be attributed to a model at all.

**A fourth finding, once a candidate existed: CRPS and MAE can rank the models in opposite
orders, and calibration does not explain the difference.** The candidate is first on mean
absolute error and last on CRPS, while sitting closer to both nominal interval levels than any
other model of ours (`results/main/fig_accuracy_and_spread.csv`). A mean coverage cannot see
an interval that is far too wide in one province and far too narrow in another, so the
headline calibration figure the plan asks for beside CRPS is not on its own enough to diagnose
a model — the per-province panel of `fig_crps_by_location` is where the disagreement resolves.

## Claims resting on this node

- **[C23](../../../claims.md#c23)** — The margin is not large enough to separate the two models. The paired difference is 3.282 CRPS per cell against a split-clustered standard error of 1.726 -- 1.90 standard errors -- and our model has the lower mean while winning only 43.1 % of the individual cells. This is the largest margin the project produced against the reference, and a comparison at this resolution still cannot say the two models differ.
- **[C31](../../../claims.md#c31)** — Both required baselines lose to the reference model, so beating the baselines is not the bar that binds. Persistence scores 24.879 and seasonal climatology 24.337 against the reference's 22.098, skill scores of -0.126 and -0.101. The reference is the harder bar by about 2.5 CRPS, and it is the one every reported ratio is taken against.
- **[C48](../../../claims.md#c48)** — The margin that the evaluation cannot separate is the usual case rather than the exception, and it applies to the held-out headline this project reports. Measured as the paired per-cell difference over its split-clustered standard error, the reported model stands 1.90 standard errors from the reference on the Lao development backtest, 0.94 on the Lao held-out year, 3.62 and 1.45 on the two sibling development backtests, and 0.97 and 0.49 on the two sibling final years. This project's own line for the case arriving in practice is 1.03, so five of the six analyses are on the wrong side of it -- including the held-out result the project reports as beating the reference, and including the Vietnamese final year it reports as a loss.

## Material

The node's own files: [`claim.md`](../../../../../analysis/04_score/03_compare/claim.md) · [`results/`](../../../../../analysis/04_score/03_compare/results) · [`scripts/`](../../../../../analysis/04_score/03_compare/scripts) · [`provenance/`](../../../../../analysis/04_score/03_compare/provenance) · [`results/main/`](../../../../../analysis/04_score/03_compare/results/main) · [`run.sh`](../../../../../analysis/04_score/03_compare/run.sh).

---

> **A snapshot, generated 2026-09-27 from the tree at commit `3d89200`.** Everything here is derived from files the repository versions and regenerates in seconds with `.venv/bin/python AI-internal/useful-scripts/build_claim_tree_md.py` (or `/hierarchical-report`). If the tree has changed since that commit, rebuild rather than trust this copy; never hand-edit.
