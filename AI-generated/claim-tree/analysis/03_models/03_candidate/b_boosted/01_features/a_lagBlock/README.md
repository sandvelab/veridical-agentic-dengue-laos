[overview](../../../../../../README.md) / [analysis](../../../../../README.md) / [03_models](../../../../README.md) / [03_candidate](../../../README.md) / [b_boosted](../../README.md) / [01_features](../README.md) / **a_lagBlock**

# a_lagBlock

*On a path not taken — an alternative the reported analysis did not use. It is complete and runnable, and the stability analysis ran it.*

**Claim:** A block of lags and nothing else: the climate columns at the lags a three-month forecast can see, the province's own recent counts at the lags it can see, and the province's size. Time and place enter only through what they imply about those numbers.

**Result:**

Eighteen features: three climate columns at lags 0, 1, 2 and 3; the province's own counts
at lags 3, 4, 5, 6 and 12; and log population
(`results/family_boosted/model_option_spec.json`). No column is standardised and none is
dropped for being missing. 209 of the 2 012 fitted rows have at least one lag that falls
before the record begins, and the boosters carry those as a missing-value direction learned
at each split rather than discarding the rows — which is where this family differs from
candidate 1, whose fit drops them.

## Material

The node's own files: [`claim.md`](../../../../../../../../analysis/03_models/03_candidate/b_boosted/01_features/a_lagBlock/claim.md) · [`results/`](../../../../../../../../analysis/03_models/03_candidate/b_boosted/01_features/a_lagBlock/results) · [`scripts/`](../../../../../../../../analysis/03_models/03_candidate/b_boosted/01_features/a_lagBlock/scripts) · [`provenance/`](../../../../../../../../analysis/03_models/03_candidate/b_boosted/01_features/a_lagBlock/provenance) · [`results/main/`](../../../../../../../../analysis/03_models/03_candidate/b_boosted/01_features/a_lagBlock/results/main) · [`run.sh`](../../../../../../../../analysis/03_models/03_candidate/b_boosted/01_features/a_lagBlock/run.sh).

---

> **A snapshot, generated 2026-09-27 from the tree at commit `3d89200`.** Everything here is derived from files the repository versions and regenerates in seconds with `.venv/bin/python AI-internal/useful-scripts/build_claim_tree_md.py` (or `/hierarchical-report`). If the tree has changed since that commit, rebuild rather than trust this copy; never hand-edit.
