[overview](../../../../../../README.md) / [analysis](../../../../../README.md) / [03_models](../../../../README.md) / [03_candidate](../../../README.md) / [a_hierNB](../../README.md) / [01_observation](../README.md) / **b_zeroInflated**

# b_zeroInflated

*On a path not taken — an alternative the reported analysis did not use. It is complete and runnable, and the stability analysis ran it.*

**Claim:** A mixture: a share of the zero months come from a process that reports nothing at all, and the rest of the record — zeros included — comes from the same negative binomial as before. The share is estimated rather than assumed, and if it comes out near zero the fork has answered itself.

**Result:**

The mixing weight fitted at **0.035**, and the combination scored **24.129** mean CRPS
     against the promoted main path's 23.698. Three and a half per cent of months attributed
     to a process that reports nothing is the fork answering itself: the negative binomial's
     variance function was already carrying the zeros.

## Material

The node's own files: [`claim.md`](../../../../../../../../analysis/03_models/03_candidate/a_hierNB/01_observation/b_zeroInflated/claim.md) · [`results/`](../../../../../../../../analysis/03_models/03_candidate/a_hierNB/01_observation/b_zeroInflated/results) · [`scripts/`](../../../../../../../../analysis/03_models/03_candidate/a_hierNB/01_observation/b_zeroInflated/scripts) · [`provenance/`](../../../../../../../../analysis/03_models/03_candidate/a_hierNB/01_observation/b_zeroInflated/provenance) · [`run.sh`](../../../../../../../../analysis/03_models/03_candidate/a_hierNB/01_observation/b_zeroInflated/run.sh).

---

> **A snapshot, generated 2026-09-27 from the tree at commit `3d89200`.** Everything here is derived from files the repository versions and regenerates in seconds with `.venv/bin/python AI-internal/useful-scripts/build_claim_tree_md.py` (or `/hierarchical-report`). If the tree has changed since that commit, rebuild rather than trust this copy; never hand-edit.
