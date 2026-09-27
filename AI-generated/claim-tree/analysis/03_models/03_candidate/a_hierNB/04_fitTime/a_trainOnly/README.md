[overview](../../../../../../README.md) / [analysis](../../../../../README.md) / [03_models](../../../../README.md) / [03_candidate](../../../README.md) / [a_hierNB](../../README.md) / [04_fitTime](../README.md) / **a_trainOnly**

# a_trainOnly

*On a path not taken — an alternative the reported analysis did not use. It is complete and runnable, and the stability analysis ran it.*

**Claim:** Fit once, in train, on the training period Chap supplies; predict applies the stored fit and reads the expanded history only for the covariate lags it needs.

**Result:**

Under the assembled flags — `n_retrain 1`, eight splits at stride 3 — one fit serves every
split, and by the last split there are **21 months** of observed history the fit never saw
(`results/main/model_option_spec.json`). The figure is read from the flag file rather than
assumed, so a combination that moved `n_retrain` would record that this child no longer means
what it says.

## Material

The node's own files: [`claim.md`](../../../../../../../../analysis/03_models/03_candidate/a_hierNB/04_fitTime/a_trainOnly/claim.md) · [`results/`](../../../../../../../../analysis/03_models/03_candidate/a_hierNB/04_fitTime/a_trainOnly/results) · [`scripts/`](../../../../../../../../analysis/03_models/03_candidate/a_hierNB/04_fitTime/a_trainOnly/scripts) · [`provenance/`](../../../../../../../../analysis/03_models/03_candidate/a_hierNB/04_fitTime/a_trainOnly/provenance) · [`results/main/`](../../../../../../../../analysis/03_models/03_candidate/a_hierNB/04_fitTime/a_trainOnly/results/main) · [`run.sh`](../../../../../../../../analysis/03_models/03_candidate/a_hierNB/04_fitTime/a_trainOnly/run.sh).

---

> **A snapshot, generated 2026-09-27 from the tree at commit `3d89200`.** Everything here is derived from files the repository versions and regenerates in seconds with `.venv/bin/python AI-internal/useful-scripts/build_claim_tree_md.py` (or `/hierarchical-report`). If the tree has changed since that commit, rebuild rather than trust this copy; never hand-edit.
