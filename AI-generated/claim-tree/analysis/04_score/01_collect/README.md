[overview](../../../README.md) / [analysis](../../README.md) / [04_score](../README.md) / **01_collect**

# 01_collect

**Claim:** What did each model score on every evaluable cell? One row per model, province, target month and lead time, with CRPS, absolute error, both interval indicators and the observed value beside them, taken from chap-core's own registered metrics.

**Result:**

2 597 rows: 371 evaluable cells for each of seven model rows — two baselines, the
reference's four repeats, and the reference's per-cell mean. Each row carries CRPS, absolute
error, both interval indicators, the observed value, the split it belongs to and the number
of draws behind it. Every reported figure in the project is an aggregation of this one file.

All three models were scored on the identical 371 cells, which is what makes the paired
comparison at `03_compare` possible at all.

## Material

The node's own files: [`claim.md`](../../../../../analysis/04_score/01_collect/claim.md) · [`results/`](../../../../../analysis/04_score/01_collect/results) · [`scripts/`](../../../../../analysis/04_score/01_collect/scripts) · [`provenance/`](../../../../../analysis/04_score/01_collect/provenance) · [`results/main/`](../../../../../analysis/04_score/01_collect/results/main) · [`run.sh`](../../../../../analysis/04_score/01_collect/run.sh).

---

> **A snapshot, generated 2026-09-27 from the tree at commit `3d89200`.** Everything here is derived from files the repository versions and regenerates in seconds with `.venv/bin/python AI-internal/useful-scripts/build_claim_tree_md.py` (or `/hierarchical-report`). If the tree has changed since that commit, rebuild rather than trust this copy; never hand-edit.
