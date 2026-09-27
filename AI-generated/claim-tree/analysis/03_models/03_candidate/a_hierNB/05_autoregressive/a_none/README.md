[overview](../../../../../../README.md) / [analysis](../../../../../README.md) / [03_models](../../../../README.md) / [03_candidate](../../../README.md) / [a_hierNB](../../README.md) / [05_autoregressive](../README.md) / **a_none**

# a_none

*On a path not taken — an alternative the reported analysis did not use. It is complete and runnable, and the stability analysis ran it.*

**Claim:** No autoregressive term. The forecast for a province-month is built from the calendar, the climate and the province's own level and annual effect, and nothing about how the current epidemic is going.

**Result:**

**The main path.** The information it declines to use, measured rather than argued:
     within a province, log1p counts correlate **0.701** at three months and **0.758** at
     twelve. The seasonal harmonics already carry the twelve-month structure, so at the only
     lag a three-month forecast can use, the lagged count is largely redundant.

## Material

The node's own files: [`claim.md`](../../../../../../../../analysis/03_models/03_candidate/a_hierNB/05_autoregressive/a_none/claim.md) · [`results/`](../../../../../../../../analysis/03_models/03_candidate/a_hierNB/05_autoregressive/a_none/results) · [`scripts/`](../../../../../../../../analysis/03_models/03_candidate/a_hierNB/05_autoregressive/a_none/scripts) · [`provenance/`](../../../../../../../../analysis/03_models/03_candidate/a_hierNB/05_autoregressive/a_none/provenance) · [`results/main/`](../../../../../../../../analysis/03_models/03_candidate/a_hierNB/05_autoregressive/a_none/results/main) · [`run.sh`](../../../../../../../../analysis/03_models/03_candidate/a_hierNB/05_autoregressive/a_none/run.sh).

---

> **A snapshot, generated 2026-09-27 from the tree at commit `3d89200`.** Everything here is derived from files the repository versions and regenerates in seconds with `.venv/bin/python AI-internal/useful-scripts/build_claim_tree_md.py` (or `/hierarchical-report`). If the tree has changed since that commit, rebuild rather than trust this copy; never hand-edit.
