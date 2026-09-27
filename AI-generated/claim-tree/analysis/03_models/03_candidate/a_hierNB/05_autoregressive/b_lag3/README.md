[overview](../../../../../../README.md) / [analysis](../../../../../README.md) / [03_models](../../../../README.md) / [03_candidate](../../../README.md) / [a_hierNB](../../README.md) / [05_autoregressive](../README.md) / **b_lag3**

# b_lag3

*On a path not taken — an alternative the reported analysis did not use. It is complete and runnable, and the stability analysis ran it.*

**Claim:** The count three months back enters the linear predictor as standardised log1p. Three is the shortest lag one model can use at all three of Chap's forecast horizons, so it is the freshest information available to a forecast that has to serve the third month as well as the first.

**Result:**

**23.345** mean CRPS, 0.353 better than the main path and inside the 0.57 floor; around
     the batch-8 configuration the same child was 0.075 *worse*. The term batch 8 declined to
     add silently turns out not to matter, and now has a number saying so.

## Material

The node's own files: [`claim.md`](../../../../../../../../analysis/03_models/03_candidate/a_hierNB/05_autoregressive/b_lag3/claim.md) · [`results/`](../../../../../../../../analysis/03_models/03_candidate/a_hierNB/05_autoregressive/b_lag3/results) · [`scripts/`](../../../../../../../../analysis/03_models/03_candidate/a_hierNB/05_autoregressive/b_lag3/scripts) · [`provenance/`](../../../../../../../../analysis/03_models/03_candidate/a_hierNB/05_autoregressive/b_lag3/provenance) · [`run.sh`](../../../../../../../../analysis/03_models/03_candidate/a_hierNB/05_autoregressive/b_lag3/run.sh).

---

> **A snapshot, generated 2026-09-27 from the tree at commit `3d89200`.** Everything here is derived from files the repository versions and regenerates in seconds with `.venv/bin/python AI-internal/useful-scripts/build_claim_tree_md.py` (or `/hierarchical-report`). If the tree has changed since that commit, rebuild rather than trust this copy; never hand-edit.
