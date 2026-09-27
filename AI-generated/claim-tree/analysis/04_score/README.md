[overview](../../README.md) / [analysis](../README.md) / **04_score**

# 04_score

**Claim:** What does each model score, and how do they compare, at every resolution the platform allows? Scores are collected once at the platform's finest resolution and everything reported is an aggregation of that one file.

**Result:**

The leaderboard for this combination, from best to worst mean CRPS: the reference at
**22.098**, seasonal climatology at **24.337**, persistence at **24.879**
(`03_compare/results/main/leaderboard.csv`). Every figure is an aggregation of one per-cell
file, and that file is written from chap-core's own registered metrics.

The node's substantive answer is not the ordering but **what the ordering can support**, and
that is at `03_compare`.

## Sub-analyses

- [01_collect](01_collect/README.md)  
  What did each model score on every evaluable cell? One row per model, province, target month and lead time, with CRPS, absolute error, both interval indicators and the …
- [02_aggregate](02_aggregate/README.md)  
  Over what weighting is the headline mean taken? The provinces differ in burden by four orders of magnitude, so an unweighted mean over cells and a mean weighted by …
- [03_compare](03_compare/README.md) · 3 claims  
  How do the models compare, and can the comparison separate them? The leaderboard from the stored scores, and the paired per-cell difference against the reference with …

## Material

The node's own files: [`claim.md`](../../../../analysis/04_score/claim.md) · [`scripts/`](../../../../analysis/04_score/scripts) · [`run.sh`](../../../../analysis/04_score/run.sh).

---

> **A snapshot, generated 2026-09-27 from the tree at commit `3d89200`.** Everything here is derived from files the repository versions and regenerates in seconds with `.venv/bin/python AI-internal/useful-scripts/build_claim_tree_md.py` (or `/hierarchical-report`). If the tree has changed since that commit, rebuild rather than trust this copy; never hand-edit.
