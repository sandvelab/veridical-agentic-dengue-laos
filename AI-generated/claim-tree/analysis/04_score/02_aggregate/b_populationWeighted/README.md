[overview](../../../../README.md) / [analysis](../../../README.md) / [04_score](../../README.md) / [02_aggregate](../README.md) / **b_populationWeighted**

# b_populationWeighted

*On a path not taken — an alternative the reported analysis did not use. It is complete and runnable, and the stability analysis ran it.*

**Claim:** Weight the headline mean by province population, so a cell counts in proportion to the people it describes. Provincial burdens differ by four orders of magnitude and the unweighted mean is very nearly a statement about the largest few provinces.

**Result:**

The pool scores **28.577** against the reference's **37.055**, a skill score of **+0.2288** against the main path's +0.1485 — a move of **+0.080**, larger than any setup fork's. Re-weighting the same per-cell file, re-running no model, moves the conclusion four times as much as changing the dataset does.

All 371 cells carry weight; the Kish effective sample size is **215**, the top decile of cells carries 29.8 % of the weight and Vientiane Capital alone 21.2 % (`results/aggregate_populationWeighted/weighting_notes.json`). The concentration the unweighted mean was suspected of is measured here rather than argued about.

## Material

The node's own files: [`claim.md`](../../../../../../analysis/04_score/02_aggregate/b_populationWeighted/claim.md) · [`results/`](../../../../../../analysis/04_score/02_aggregate/b_populationWeighted/results) · [`scripts/`](../../../../../../analysis/04_score/02_aggregate/b_populationWeighted/scripts) · [`provenance/`](../../../../../../analysis/04_score/02_aggregate/b_populationWeighted/provenance) · [`run.sh`](../../../../../../analysis/04_score/02_aggregate/b_populationWeighted/run.sh).

---

> **A snapshot, generated 2026-09-27 from the tree at commit `3d89200`.** Everything here is derived from files the repository versions and regenerates in seconds with `.venv/bin/python AI-internal/useful-scripts/build_claim_tree_md.py` (or `/hierarchical-report`). If the tree has changed since that commit, rebuild rather than trust this copy; never hand-edit.
