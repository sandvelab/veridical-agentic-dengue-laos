[overview](../../../../../../README.md) / [analysis](../../../../../README.md) / [03_models](../../../../README.md) / [03_candidate](../../../README.md) / [a_hierNB](../../README.md) / [03_population](../README.md) / **c_ignored**

# c_ignored

*On a path not taken — an alternative the reported analysis did not use. It is complete and runnable, and the stability analysis ran it.*

**Claim:** Population does not enter the model at all: a province's level is carried entirely by its own pooled intercept, which is estimated from its record rather than from its size.

**Result:**

**23.723** mean CRPS, 0.025 from the main path -- two orders of magnitude inside the
     resolvable floor. Dropping the population column changes nothing this backtest can
     measure, because the column is constant within a province and the pooled intercept
     absorbs it exactly: the province spread widens to sigma **1.87** from 1.27.

## Material

The node's own files: [`claim.md`](../../../../../../../../analysis/03_models/03_candidate/a_hierNB/03_population/c_ignored/claim.md) · [`results/`](../../../../../../../../analysis/03_models/03_candidate/a_hierNB/03_population/c_ignored/results) · [`scripts/`](../../../../../../../../analysis/03_models/03_candidate/a_hierNB/03_population/c_ignored/scripts) · [`provenance/`](../../../../../../../../analysis/03_models/03_candidate/a_hierNB/03_population/c_ignored/provenance) · [`run.sh`](../../../../../../../../analysis/03_models/03_candidate/a_hierNB/03_population/c_ignored/run.sh).

---

> **A snapshot, generated 2026-09-27 from the tree at commit `3d89200`.** Everything here is derived from files the repository versions and regenerates in seconds with `.venv/bin/python AI-internal/useful-scripts/build_claim_tree_md.py` (or `/hierarchical-report`). If the tree has changed since that commit, rebuild rather than trust this copy; never hand-edit.
