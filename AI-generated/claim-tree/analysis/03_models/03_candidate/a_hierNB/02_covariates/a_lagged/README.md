[overview](../../../../../../README.md) / [analysis](../../../../../README.md) / [03_models](../../../../README.md) / [03_candidate](../../../README.md) / [a_hierNB](../../README.md) / [02_covariates](../README.md) / **a_lagged**

# a_lagged

*On a path not taken — an alternative the reported analysis did not use. It is complete and runnable, and the stability analysis ran it.*

**Claim:** Rainfall and mean temperature only, each entering linearly at a two-month lag — the covariate pair and the lag the reference model's own published Lao configuration uses, standardised on the training period.

**Result:**

Rainfall and mean temperature at a two-month lag, both complete across all 2 592 rows
(`results/main/model_option_spec.json`). The pair and the lag are the reference family's own
published Lao configuration, not ours: `laos_eval_config.yaml` in
`chap-models/ewars_plus_template` names exactly these two at `n_lags: 2`.

## Material

The node's own files: [`claim.md`](../../../../../../../../analysis/03_models/03_candidate/a_hierNB/02_covariates/a_lagged/claim.md) · [`results/`](../../../../../../../../analysis/03_models/03_candidate/a_hierNB/02_covariates/a_lagged/results) · [`scripts/`](../../../../../../../../analysis/03_models/03_candidate/a_hierNB/02_covariates/a_lagged/scripts) · [`provenance/`](../../../../../../../../analysis/03_models/03_candidate/a_hierNB/02_covariates/a_lagged/provenance) · [`run.sh`](../../../../../../../../analysis/03_models/03_candidate/a_hierNB/02_covariates/a_lagged/run.sh).

---

> **A snapshot, generated 2026-09-27 from the tree at commit `3d89200`.** Everything here is derived from files the repository versions and regenerates in seconds with `.venv/bin/python AI-internal/useful-scripts/build_claim_tree_md.py` (or `/hierarchical-report`). If the tree has changed since that commit, rebuild rather than trust this copy; never hand-edit.
