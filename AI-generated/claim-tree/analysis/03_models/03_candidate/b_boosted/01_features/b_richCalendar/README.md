[overview](../../../../../../README.md) / [analysis](../../../../../README.md) / [03_models](../../../../README.md) / [03_candidate](../../../README.md) / [b_boosted](../../README.md) / [01_features](../README.md) / **b_richCalendar**

# b_richCalendar

*On a path not taken — an alternative the reported analysis did not use. It is complete and runnable, and the stability analysis ran it.*

**Claim:** The same lag block, plus what the calendar and the map say directly: the month as a pair of harmonics, a year index, the province as an identifier, and rolling summaries of the province's own recent history.

**Result:**

Twenty-seven features: the sibling's eighteen, plus two harmonic pairs of the month, a year
index, the province as an identifier, and rolling means of the count over 3, 6 and 12
months ending at the third lag (`results/features_richCalendar/model_option_spec.json`).

**It scores 20.375 against the sibling's 20.771** — better by 0.396 CRPS, which is inside
the resolvable floor and so does not move the fork. Its point forecast is worse (MAE 28.251
against 26.953) and its intervals wider (10–90 coverage 0.857 against 0.825), which is the
signature of a model that has fitted the training years more closely and is less certain
about a period it cannot extrapolate into. Both costs registered before the run — sixteen
extra cuts from the province identifier, and a year index every forecast month falls beyond
— are consistent with what happened, and neither is separable from the other by this run.

## Material

The node's own files: [`claim.md`](../../../../../../../../analysis/03_models/03_candidate/b_boosted/01_features/b_richCalendar/claim.md) · [`results/`](../../../../../../../../analysis/03_models/03_candidate/b_boosted/01_features/b_richCalendar/results) · [`scripts/`](../../../../../../../../analysis/03_models/03_candidate/b_boosted/01_features/b_richCalendar/scripts) · [`provenance/`](../../../../../../../../analysis/03_models/03_candidate/b_boosted/01_features/b_richCalendar/provenance) · [`run.sh`](../../../../../../../../analysis/03_models/03_candidate/b_boosted/01_features/b_richCalendar/run.sh).

---

> **A snapshot, generated 2026-09-27 from the tree at commit `3d89200`.** Everything here is derived from files the repository versions and regenerates in seconds with `.venv/bin/python AI-internal/useful-scripts/build_claim_tree_md.py` (or `/hierarchical-report`). If the tree has changed since that commit, rebuild rather than trust this copy; never hand-edit.
