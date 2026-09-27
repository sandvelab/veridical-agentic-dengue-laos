[overview](../../../../../README.md) / [analysis](../../../../README.md) / [03_models](../../../README.md) / [03_candidate](../../README.md) / [a_hierNB](../README.md) / **04_fitTime**

# 04_fitTime

*On a path not taken — an alternative the reported analysis did not use. It is complete and runnable, and the stability analysis ran it.*

**Claim:** Does the model do its fitting in train or in predict? Chap fits once and then predicts at every split, so a model that refits inside predict sees each split's expanded history while one that does not sees only the training period.

**Result:**

**Refitting inside `predict` is worth more than any other unmoved fork, and it is the one
place our model was handicapped against the reference.** `b_refitAtPredict` scores
**22.825** mean CRPS from the promoted main path against 23.698 -- a gain of **0.873**,
outside the 0.57 floor, and the closest any model of ours has come to the reference's
22.098 (`round2_promoted/fork_leaderboard.csv`).

The asymmetry it measures is real: `chapkit_ewars_model` fits inside its own predict
endpoint, so at every split of the backtest it has been using history our train-time fit
discards -- **21 months** of it by the last split.

It costs **108 seconds** against 36, which is eight fits instead of one, and it leaves no
single fitted object for the record, since the fit happens once per split inside chap-core's
untracked run directories.

**It was not promoted**, because around the batch-8 configuration -- the sweep the
promotion rule was applied to -- it was worth 0.408 and inside the floor.

## Alternatives

Competing ways of answering this node's claim. The reported analysis takes the **main path**; the others are run by `05_stability`.

- [a_trainOnly](a_trainOnly/README.md) — **main path**  
  Fit once, in train, on the training period Chap supplies; predict applies the stored fit and reads the expanded history only for the covariate lags it needs.
- [b_refitAtPredict](b_refitAtPredict/README.md) — *not taken*  
  The model is refitted inside every predict call, on the whole expanding historic window Chap hands it, so that a forecast late in the backtest is made by a model that …

## Material

The node's own files: [`claim.md`](../../../../../../../analysis/03_models/03_candidate/a_hierNB/04_fitTime/claim.md) · [`run.sh`](../../../../../../../analysis/03_models/03_candidate/a_hierNB/04_fitTime/run.sh).

---

> **A snapshot, generated 2026-09-27 from the tree at commit `3d89200`.** Everything here is derived from files the repository versions and regenerates in seconds with `.venv/bin/python AI-internal/useful-scripts/build_claim_tree_md.py` (or `/hierarchical-report`). If the tree has changed since that commit, rebuild rather than trust this copy; never hand-edit.
