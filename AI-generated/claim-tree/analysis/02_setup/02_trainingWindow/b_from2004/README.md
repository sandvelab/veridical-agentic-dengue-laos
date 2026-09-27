[overview](../../../../README.md) / [analysis](../../../README.md) / [02_setup](../../README.md) / [02_trainingWindow](../README.md) / **b_from2004**

# b_from2004

*On a path not taken — an alternative the reported analysis did not use. It is complete and runnable, and the stability analysis ran it.*

**Claim:** Let models learn only from the second half of the development record, 2004-01 onward. The share of zero-valued months falls monotonically across the period, so the early years may describe a reporting regime the evaluated window no longer belongs to; the cut is taken at the calendar midpoint rather than at a zero-rate threshold, so it is not chosen by the quantity it is meant to probe.

**Result:**

Half the record is discarded: **2 592 rows in, 1 296 out**, 2004-01 to 2009-12, latest dropped period 2003-12 (`results/trainingWindow_from2004/setup_spec.json`). The evaluated span begins 2008-01, so the 371 cells are untouched — asserted by the script rather than assumed, so a cut that reached into the evaluated span would stop the run instead of producing two children scored on different cells.

Halving what the models learn from costs **0.0219 of skill**, from +0.1485 to **+0.1266** — the largest downward move of any fork run so far, and still far inside the reference's own re-run noise. The early years are worth something and not much.

## Material

The node's own files: [`claim.md`](../../../../../../analysis/02_setup/02_trainingWindow/b_from2004/claim.md) · [`results/`](../../../../../../analysis/02_setup/02_trainingWindow/b_from2004/results) · [`scripts/`](../../../../../../analysis/02_setup/02_trainingWindow/b_from2004/scripts) · [`provenance/`](../../../../../../analysis/02_setup/02_trainingWindow/b_from2004/provenance) · [`run.sh`](../../../../../../analysis/02_setup/02_trainingWindow/b_from2004/run.sh).

---

> **A snapshot, generated 2026-09-27 from the tree at commit `3d89200`.** Everything here is derived from files the repository versions and regenerates in seconds with `.venv/bin/python AI-internal/useful-scripts/build_claim_tree_md.py` (or `/hierarchical-report`). If the tree has changed since that commit, rebuild rather than trust this copy; never hand-edit.
