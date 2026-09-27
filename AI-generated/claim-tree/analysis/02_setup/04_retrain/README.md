[overview](../../../README.md) / [analysis](../../README.md) / [02_setup](../README.md) / **04_retrain**

# 04_retrain

**Claim:** How often is a model refitted across the backtest? Chap's n-retrain governs whether one fit serves all splits or each split gets its own.

**Result:**

**The sibling is built and run.** Refitting at every split gives **+0.1651** against the main path's +0.1485: it helps our pool a little and does not help the reference. That asymmetry is the paragraph below made quantitative — the reference already refits inside `predict`, so the flag buys it nothing and costs it eight times the compute. See `b_everySplit/claim.md`.

`n_retrain = 1` reaches `chap eval` from a file rather than from a constant in each model's
runner, so two models cannot disagree about it silently. The flag governs how often
chap-core calls `train`; it does not stop a model that fits inside `predict` from refitting
at every split, which is what the reference model does. That distinction is recorded because
one flag can otherwise look as though it had made all the models comparable in this respect.

## Alternatives

Competing ways of answering this node's claim. The reported analysis takes the **main path**; the others are run by `05_stability`.

- [a_once](a_once/README.md) — **main path**  
  Refit once, at chap-core's default n-retrain 1: a single fit on the training period, with an expanding historic window handed to predict at every split.
- [b_everySplit](b_everySplit/README.md) — *not taken*  
  Refit every model at every split rather than once, by setting chap-core's n-retrain to the number of splits. A forecast made in 2009 is then made by a model that has …

## Material

The node's own files: [`claim.md`](../../../../../analysis/02_setup/04_retrain/claim.md) · [`run.sh`](../../../../../analysis/02_setup/04_retrain/run.sh).

---

> **A snapshot, generated 2026-09-27 from the tree at commit `3d89200`.** Everything here is derived from files the repository versions and regenerates in seconds with `.venv/bin/python AI-internal/useful-scripts/build_claim_tree_md.py` (or `/hierarchical-report`). If the tree has changed since that commit, rebuild rather than trust this copy; never hand-edit.
