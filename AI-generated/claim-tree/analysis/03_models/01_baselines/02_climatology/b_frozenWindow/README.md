[overview](../../../../../README.md) / [analysis](../../../../README.md) / [03_models](../../../README.md) / [01_baselines](../../README.md) / [02_climatology](../README.md) / **b_frozenWindow**

# b_frozenWindow

*On a path not taken — an alternative the reported analysis did not use. It is complete and runnable, and the stability analysis ran it.*

**Claim:** Estimate each province's calendar-month distribution once, from the training period alone, and hold it fixed across every split rather than re-estimating from the expanding historic frame. The baseline then knows only what it knew at fitting time, which is what a model fitted once and deployed actually has.

**Result:**

**Freezing the table costs 0.532 CRPS — 24.869 against the expanding window's 24.337**
(`analysis/04_score/03_compare/results/climatology_frozenWindow/leaderboard.csv`) — which is
*inside* the 0.565 floor below which nothing on this dataset can be attributed to a model.
Calibration moves as little: 10–90 coverage 0.639 against 0.650, 25–75 coverage 0.520 against
0.542.

**Two dengue seasons of data are worth nothing measurable to this baseline.** The training
frame ends 2007-12 and the evaluation runs through 2009-12, so this model forecasts two
seasons it has never seen, on a series whose reporting improved throughout — and the
difference does not clear the noise. The node's own claim argued before the run that the
choice mattered *because* of that gap. It does not, and that is the answer.

**Its effect on the reported model is smaller still**: the pool moves from 18.817 to 18.872,
skill +0.1485 to +0.1460. This is the smallest move of any tier-1 row run so far, and its
sibling fork's row is the largest.

## Material

The node's own files: [`claim.md`](../../../../../../../analysis/03_models/01_baselines/02_climatology/b_frozenWindow/claim.md) · [`results/`](../../../../../../../analysis/03_models/01_baselines/02_climatology/b_frozenWindow/results) · [`scripts/`](../../../../../../../analysis/03_models/01_baselines/02_climatology/b_frozenWindow/scripts) · [`provenance/`](../../../../../../../analysis/03_models/01_baselines/02_climatology/b_frozenWindow/provenance) · [`run.sh`](../../../../../../../analysis/03_models/01_baselines/02_climatology/b_frozenWindow/run.sh).

---

> **A snapshot, generated 2026-09-27 from the tree at commit `3d89200`.** Everything here is derived from files the repository versions and regenerates in seconds with `.venv/bin/python AI-internal/useful-scripts/build_claim_tree_md.py` (or `/hierarchical-report`). If the tree has changed since that commit, rebuild rather than trust this copy; never hand-edit.
