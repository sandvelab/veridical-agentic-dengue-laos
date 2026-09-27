[overview](../../../../../../README.md) / [analysis](../../../../../README.md) / [03_models](../../../../README.md) / [03_candidate](../../../README.md) / [a_hierNB](../../README.md) / [02_covariates](../README.md) / **b_rich**

# b_rich

*On a path not taken — an alternative the reported analysis did not use. It is complete and runnable, and the stability analysis ran it.*

**Claim:** All three climate columns — rainfall, mean temperature and mean relative humidity — each at one, two and three months' lag, letting the fit decide which of them carries signal instead of the choice being made in advance.

**Result:**

**22.877** mean CRPS, the second-best combination in the second sweep and outside the
     0.57 floor. Its coefficients are the evidence that the covariate question is not settled:
     mean temperature at lag 1 takes **+0.653** and at lag 3 **+0.594**, rainfall takes almost
     nothing at any lag, and the seasonal harmonic `sin1` collapses from −1.235 to −0.027 as
     the climate columns take over the annual cycle.

## Material

The node's own files: [`claim.md`](../../../../../../../../analysis/03_models/03_candidate/a_hierNB/02_covariates/b_rich/claim.md) · [`results/`](../../../../../../../../analysis/03_models/03_candidate/a_hierNB/02_covariates/b_rich/results) · [`scripts/`](../../../../../../../../analysis/03_models/03_candidate/a_hierNB/02_covariates/b_rich/scripts) · [`provenance/`](../../../../../../../../analysis/03_models/03_candidate/a_hierNB/02_covariates/b_rich/provenance) · [`run.sh`](../../../../../../../../analysis/03_models/03_candidate/a_hierNB/02_covariates/b_rich/run.sh).

---

> **A snapshot, generated 2026-09-27 from the tree at commit `3d89200`.** Everything here is derived from files the repository versions and regenerates in seconds with `.venv/bin/python AI-internal/useful-scripts/build_claim_tree_md.py` (or `/hierarchical-report`). If the tree has changed since that commit, rebuild rather than trust this copy; never hand-edit.
