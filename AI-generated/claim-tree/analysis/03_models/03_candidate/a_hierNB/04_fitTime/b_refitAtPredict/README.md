[overview](../../../../../../README.md) / [analysis](../../../../../README.md) / [03_models](../../../../README.md) / [03_candidate](../../../README.md) / [a_hierNB](../../README.md) / [04_fitTime](../README.md) / **b_refitAtPredict**

# b_refitAtPredict

*On a path not taken — an alternative the reported analysis did not use. It is complete and runnable, and the stability analysis ran it.*

**Claim:** The model is refitted inside every predict call, on the whole expanding historic window Chap hands it, so that a forecast late in the backtest is made by a model that has seen the years between. This is what the reference model does.

**Result:**

**22.825** mean CRPS, the best combination in the second sweep and **0.873** better
     than the main path, at **108** seconds against 36. It recovers the 21 months of history a
     train-time fit discards by the last split -- the history the reference model has been
     using all along. It leaves no single fitted object: the fit happens once per split inside
     chap-core's untracked run directories, and `train` writes a stub that says so.

## Material

The node's own files: [`claim.md`](../../../../../../../../analysis/03_models/03_candidate/a_hierNB/04_fitTime/b_refitAtPredict/claim.md) · [`results/`](../../../../../../../../analysis/03_models/03_candidate/a_hierNB/04_fitTime/b_refitAtPredict/results) · [`scripts/`](../../../../../../../../analysis/03_models/03_candidate/a_hierNB/04_fitTime/b_refitAtPredict/scripts) · [`provenance/`](../../../../../../../../analysis/03_models/03_candidate/a_hierNB/04_fitTime/b_refitAtPredict/provenance) · [`run.sh`](../../../../../../../../analysis/03_models/03_candidate/a_hierNB/04_fitTime/b_refitAtPredict/run.sh).

---

> **A snapshot, generated 2026-09-27 from the tree at commit `3d89200`.** Everything here is derived from files the repository versions and regenerates in seconds with `.venv/bin/python AI-internal/useful-scripts/build_claim_tree_md.py` (or `/hierarchical-report`). If the tree has changed since that commit, rebuild rather than trust this copy; never hand-edit.
