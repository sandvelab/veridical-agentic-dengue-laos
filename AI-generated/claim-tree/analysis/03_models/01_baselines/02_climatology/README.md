[overview](../../../../README.md) / [analysis](../../../README.md) / [03_models](../../README.md) / [01_baselines](../README.md) / **02_climatology**

# 02_climatology

**Claim:** How well does the seasonal average forecast the next three months? For each province and calendar month, the empirical distribution of the counts observed in that month across the training years — a baseline that knows the season and nothing else.

**Result:**

The seasonal climatology baseline scores **24.337 mean CRPS** over 371 cells, with 10-90
coverage 0.650 and 25-75 coverage 0.542. It is marginally the better of the two baselines
and the margin is inside what this evaluation can resolve.

Unlike the persistence baseline it needs no decision about how to wrap uncertainty around a
point — a set of past Julys is a distribution already. What it does need is a decision about
which window estimates that distribution, and the main path re-estimates from the expanding
historic frame at each split. The frozen-training-window sibling is not built yet;
`train.py` stores the table it would have used.

**The window does not matter.** Estimating the seasonal table once from the training frame
and holding it fixed scores **24.869** against the expanding window's **24.337**: 0.532 CRPS,
inside the 0.565 floor. The main path re-estimates from everything observed by forecast time
and gains nothing measurable by it, although the frozen table misses the last two years of a
twelve-year series.

Set beside its sibling fork — where the *construction* of the persistence baseline's
uncertainty is worth 4.181 CRPS — the pair says something the two rows do not say separately:
**on this dataset the shape of a baseline's predictive distribution matters and the window it
is estimated over does not.**

## Alternatives

Competing ways of answering this node's claim. The reported analysis takes the **main path**; the others are run by `05_stability`.

- [a_expandingWindow](a_expandingWindow/README.md) — **main path**  
  Estimate each province's calendar-month distribution from everything observed by the time the forecast is made — the expanding historic window chap-core hands to predict …
- [b_frozenWindow](b_frozenWindow/README.md) — *not taken*  
  Estimate each province's calendar-month distribution once, from the training period alone, and hold it fixed across every split rather than re-estimating from the …

## Material

The node's own files: [`claim.md`](../../../../../../analysis/03_models/01_baselines/02_climatology/claim.md) · [`run.sh`](../../../../../../analysis/03_models/01_baselines/02_climatology/run.sh).

---

> **A snapshot, generated 2026-09-27 from the tree at commit `3d89200`.** Everything here is derived from files the repository versions and regenerates in seconds with `.venv/bin/python AI-internal/useful-scripts/build_claim_tree_md.py` (or `/hierarchical-report`). If the tree has changed since that commit, rebuild rather than trust this copy; never hand-edit.
