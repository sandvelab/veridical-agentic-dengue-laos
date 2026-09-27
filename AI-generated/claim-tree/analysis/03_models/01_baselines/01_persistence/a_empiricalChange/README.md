[overview](../../../../../README.md) / [analysis](../../../../README.md) / [03_models](../../../README.md) / [01_baselines](../../README.md) / [01_persistence](../README.md) / **a_empiricalChange**

# a_empiricalChange

**Claim:** Wrap the point in the empirical distribution of past h-step changes within the same province, each change entered with its negation so the predictive median stays on the last observation, truncated at zero.

**Result:**

Mean CRPS **24.879** over 371 cells in 16 provinces, 28 seconds for the eight-split backtest (`results/main/run_cost.json`). Identical to batch 6's vertical-slice figure to the last digit, and byte-identical across two independent runs.

## Material

The node's own files: [`claim.md`](../../../../../../../analysis/03_models/01_baselines/01_persistence/a_empiricalChange/claim.md) · [`results/`](../../../../../../../analysis/03_models/01_baselines/01_persistence/a_empiricalChange/results) · [`scripts/`](../../../../../../../analysis/03_models/01_baselines/01_persistence/a_empiricalChange/scripts) · [`provenance/`](../../../../../../../analysis/03_models/01_baselines/01_persistence/a_empiricalChange/provenance) · [`results/main/`](../../../../../../../analysis/03_models/01_baselines/01_persistence/a_empiricalChange/results/main) · [`run.sh`](../../../../../../../analysis/03_models/01_baselines/01_persistence/a_empiricalChange/run.sh).

---

> **A snapshot, generated 2026-09-27 from the tree at commit `3d89200`.** Everything here is derived from files the repository versions and regenerates in seconds with `.venv/bin/python AI-internal/useful-scripts/build_claim_tree_md.py` (or `/hierarchical-report`). If the tree has changed since that commit, rebuild rather than trust this copy; never hand-edit.
