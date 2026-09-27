[overview](../../../../README.md) / [analysis](../../../README.md) / [04_score](../../README.md) / [02_aggregate](../README.md) / **c_caseWeighted**

# c_caseWeighted

*On a path not taken — an alternative the reported analysis did not use. It is complete and runnable, and the stability analysis ran it.*

**Claim:** Weight the headline mean by the cases actually observed in each cell, so the summary is dominated by the province-months where dengue was happening. A province reporting four cases in twelve years then stops carrying the same weight as the capital.

**Result:**

Weighted by the cases actually observed, the pool scores **88.484** against the reference's **115.216** — skill **+0.2320**, the highest in tier 1. **The number beside it is the result.** Persistence scores **86.598**: on the months when dengue was happening, the simplest baseline in the project forecasts better than the model this project reports.

The calibration inverts too. Our pool is over-dispersed everywhere else — 10-90 coverage 0.863 against nominal 0.80 — and here it is **0.701**, under-dispersed. It is too wide on the quiet months that dominate the unweighted mean and too narrow on the outbreak months that dominate this one.

**137 of 371 cells carry zero weight.** The effective sample falls to **65**, the top decile of cells carries 62.3 % of the weight, and 240 province-by-split groups have no weighted mean at all and are reported missing rather than zero (`results/aggregate_caseWeighted/weighting_notes.json`). This is the opposite blind spot to the unweighted mean's, not a correction of it.

## Material

The node's own files: [`claim.md`](../../../../../../analysis/04_score/02_aggregate/c_caseWeighted/claim.md) · [`results/`](../../../../../../analysis/04_score/02_aggregate/c_caseWeighted/results) · [`scripts/`](../../../../../../analysis/04_score/02_aggregate/c_caseWeighted/scripts) · [`provenance/`](../../../../../../analysis/04_score/02_aggregate/c_caseWeighted/provenance) · [`run.sh`](../../../../../../analysis/04_score/02_aggregate/c_caseWeighted/run.sh).

---

> **A snapshot, generated 2026-09-27 from the tree at commit `3d89200`.** Everything here is derived from files the repository versions and regenerates in seconds with `.venv/bin/python AI-internal/useful-scripts/build_claim_tree_md.py` (or `/hierarchical-report`). If the tree has changed since that commit, rebuild rather than trust this copy; never hand-edit.
