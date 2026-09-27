[overview](../../../../../../README.md) / [analysis](../../../../../README.md) / [03_models](../../../../README.md) / [03_candidate](../../../README.md) / [a_hierNB](../../README.md) / [03_population](../README.md) / **b_covariate**

# b_covariate

*On a path not taken — an alternative the reported analysis did not use. It is complete and runnable, and the stability analysis ran it.*

**Claim:** Population as an estimated coefficient on standardised log population rather than as a fixed offset, so the data decides how reported cases scale with province size instead of the model asserting proportionality.

**Result:**

**23.876** mean CRPS, 0.178 worse than the offset. The fitted coefficient on
     standardised log population is **1.725** and the pooled province spread falls to sigma
     **0.94** from 1.27, which is the coefficient and the intercept explaining the same thing.
     The premise it computed is the check the offset never makes: log mean cases rise **1.74**
     per unit of log population across provinces, where an offset asserts 1.00.

## Material

The node's own files: [`claim.md`](../../../../../../../../analysis/03_models/03_candidate/a_hierNB/03_population/b_covariate/claim.md) · [`results/`](../../../../../../../../analysis/03_models/03_candidate/a_hierNB/03_population/b_covariate/results) · [`scripts/`](../../../../../../../../analysis/03_models/03_candidate/a_hierNB/03_population/b_covariate/scripts) · [`provenance/`](../../../../../../../../analysis/03_models/03_candidate/a_hierNB/03_population/b_covariate/provenance) · [`run.sh`](../../../../../../../../analysis/03_models/03_candidate/a_hierNB/03_population/b_covariate/run.sh).

---

> **A snapshot, generated 2026-09-27 from the tree at commit `3d89200`.** Everything here is derived from files the repository versions and regenerates in seconds with `.venv/bin/python AI-internal/useful-scripts/build_claim_tree_md.py` (or `/hierarchical-report`). If the tree has changed since that commit, rebuild rather than trust this copy; never hand-edit.
