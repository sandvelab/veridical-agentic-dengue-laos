[overview](../../../../README.md) / [analysis](../../../README.md) / [02_setup](../../README.md) / [04_retrain](../README.md) / **b_everySplit**

# b_everySplit

*On a path not taken — an alternative the reported analysis did not use. It is complete and runnable, and the stability analysis ran it.*

**Claim:** Refit every model at every split rather than once, by setting chap-core's n-retrain to the number of splits. A forecast made in 2009 is then made by a model that has seen 2008, which is more like how a forecasting system is actually operated and is what the reference model does inside its own predict.

**Result:**

`n_retrain` is set to **8**, the scheme's own `n_splits`, read from the file `assemble_setup.py` reads it from rather than typed. Skill rises to **+0.1651**: refitting at every split helps our pool a little (18.817 to 18.552) and does not help the reference (22.098 to 22.220).

**That asymmetry is the point of the row.** The reference fits inside its own `predict`, so it was already refitting at every split whatever this flag said; `n_retrain` only governs how often chap-core calls `train`. The fork therefore buys the reference no different forecast and charges it **eight times the compute** — 64 jobs against 8 — which is how this row became the most expensive in tier 1 at 2 226 s and the one that exposed the reference's intermittent crash.

## Material

The node's own files: [`claim.md`](../../../../../../analysis/02_setup/04_retrain/b_everySplit/claim.md) · [`results/`](../../../../../../analysis/02_setup/04_retrain/b_everySplit/results) · [`scripts/`](../../../../../../analysis/02_setup/04_retrain/b_everySplit/scripts) · [`provenance/`](../../../../../../analysis/02_setup/04_retrain/b_everySplit/provenance) · [`run.sh`](../../../../../../analysis/02_setup/04_retrain/b_everySplit/run.sh).

---

> **A snapshot, generated 2026-09-27 from the tree at commit `3d89200`.** Everything here is derived from files the repository versions and regenerates in seconds with `.venv/bin/python AI-internal/useful-scripts/build_claim_tree_md.py` (or `/hierarchical-report`). If the tree has changed since that commit, rebuild rather than trust this copy; never hand-edit.
