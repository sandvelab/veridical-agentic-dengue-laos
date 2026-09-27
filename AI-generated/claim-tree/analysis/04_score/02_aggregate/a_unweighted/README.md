[overview](../../../../README.md) / [analysis](../../../README.md) / [04_score](../../README.md) / [02_aggregate](../README.md) / **a_unweighted**

# a_unweighted

**Claim:** Take the plain unweighted mean over evaluable cells, which is what Chap's own evaluation reports and what the project's success criterion is defined against.

**Result:**

The headline row per model and the four resolutions beside it, all `groupby` aggregations of one per-cell file. Mean CRPS per province spans **0.01 to 84** across the 16 provinces (`results/main/crps_by_location.csv`), which is the measurement behind the warning that an unweighted mean over cells is close to a statement about the largest few provinces.

## Material

The node's own files: [`claim.md`](../../../../../../analysis/04_score/02_aggregate/a_unweighted/claim.md) · [`results/`](../../../../../../analysis/04_score/02_aggregate/a_unweighted/results) · [`scripts/`](../../../../../../analysis/04_score/02_aggregate/a_unweighted/scripts) · [`provenance/`](../../../../../../analysis/04_score/02_aggregate/a_unweighted/provenance) · [`results/main/`](../../../../../../analysis/04_score/02_aggregate/a_unweighted/results/main) · [`run.sh`](../../../../../../analysis/04_score/02_aggregate/a_unweighted/run.sh).

---

> **A snapshot, generated 2026-09-27 from the tree at commit `3d89200`.** Everything here is derived from files the repository versions and regenerates in seconds with `.venv/bin/python AI-internal/useful-scripts/build_claim_tree_md.py` (or `/hierarchical-report`). If the tree has changed since that commit, rebuild rather than trust this copy; never hand-edit.
