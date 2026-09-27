[overview](../../../../../README.md) / [analysis](../../../../README.md) / [03_models](../../../README.md) / [01_baselines](../../README.md) / [02_climatology](../README.md) / **a_expandingWindow**

# a_expandingWindow

**Claim:** Estimate each province's calendar-month distribution from everything observed by the time the forecast is made — the expanding historic window chap-core hands to predict — so the baseline uses the same information the persistence baseline anchors on.

**Result:**

Mean CRPS **24.337** over the same 371 cells, 28 seconds for the backtest. Byte-identical across two independent runs. The model's environment resolves to the same six packages as the persistence baseline's, so the two differ in what they compute and in nothing else.

## Material

The node's own files: [`claim.md`](../../../../../../../analysis/03_models/01_baselines/02_climatology/a_expandingWindow/claim.md) · [`results/`](../../../../../../../analysis/03_models/01_baselines/02_climatology/a_expandingWindow/results) · [`scripts/`](../../../../../../../analysis/03_models/01_baselines/02_climatology/a_expandingWindow/scripts) · [`provenance/`](../../../../../../../analysis/03_models/01_baselines/02_climatology/a_expandingWindow/provenance) · [`results/main/`](../../../../../../../analysis/03_models/01_baselines/02_climatology/a_expandingWindow/results/main) · [`run.sh`](../../../../../../../analysis/03_models/01_baselines/02_climatology/a_expandingWindow/run.sh).

---

> **A snapshot, generated 2026-09-27 from the tree at commit `3d89200`.** Everything here is derived from files the repository versions and regenerates in seconds with `.venv/bin/python AI-internal/useful-scripts/build_claim_tree_md.py` (or `/hierarchical-report`). If the tree has changed since that commit, rebuild rather than trust this copy; never hand-edit.
