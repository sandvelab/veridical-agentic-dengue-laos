[overview](../../../../../../README.md) / [analysis](../../../../../README.md) / [03_models](../../../../README.md) / [03_candidate](../../../README.md) / [a_hierNB](../../README.md) / [02_covariates](../README.md) / **c_climateFree**

# c_climateFree

*On a path not taken — an alternative the reported analysis did not use. It is complete and runnable, and the stability analysis ran it.*

**Claim:** No climate covariates at all, so that the shared annual harmonics and the province-year effect alone carry the seasonal cycle. If this scores like the lagged-climate child, the covariates are decoration on this dataset.

**Result:**

**The main path from batch 9**, and the child that says most about the dataset. Around
     the batch-8 configuration, having no climate term at all was worth **+0.648** CRPS; from
     the promoted configuration, putting the two lagged covariates back is worth **+0.112**, so
     the sign reverses. Both are inside or near the floor. It also fits on **2 012** rows
     rather than 1 978, because no row is dropped for a lag falling before the record starts.

## Material

The node's own files: [`claim.md`](../../../../../../../../analysis/03_models/03_candidate/a_hierNB/02_covariates/c_climateFree/claim.md) · [`results/`](../../../../../../../../analysis/03_models/03_candidate/a_hierNB/02_covariates/c_climateFree/results) · [`scripts/`](../../../../../../../../analysis/03_models/03_candidate/a_hierNB/02_covariates/c_climateFree/scripts) · [`provenance/`](../../../../../../../../analysis/03_models/03_candidate/a_hierNB/02_covariates/c_climateFree/provenance) · [`results/main/`](../../../../../../../../analysis/03_models/03_candidate/a_hierNB/02_covariates/c_climateFree/results/main) · [`run.sh`](../../../../../../../../analysis/03_models/03_candidate/a_hierNB/02_covariates/c_climateFree/run.sh).

---

> **A snapshot, generated 2026-09-27 from the tree at commit `3d89200`.** Everything here is derived from files the repository versions and regenerates in seconds with `.venv/bin/python AI-internal/useful-scripts/build_claim_tree_md.py` (or `/hierarchical-report`). If the tree has changed since that commit, rebuild rather than trust this copy; never hand-edit.
