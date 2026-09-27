[overview](../../../../README.md) / [analysis](../../../README.md) / [02_setup](../../README.md) / [04_retrain](../README.md) / **a_once**

# a_once

**Claim:** Refit once, at chap-core's default n-retrain 1: a single fit on the training period, with an expanding historic window handed to predict at every split.

**Result:**

`n_retrain = 1` is written into the stage specification and reaches `chap eval` from there (`results/main/setup_spec.json`).

## Material

The node's own files: [`claim.md`](../../../../../../analysis/02_setup/04_retrain/a_once/claim.md) · [`results/`](../../../../../../analysis/02_setup/04_retrain/a_once/results) · [`scripts/`](../../../../../../analysis/02_setup/04_retrain/a_once/scripts) · [`provenance/`](../../../../../../analysis/02_setup/04_retrain/a_once/provenance) · [`results/main/`](../../../../../../analysis/02_setup/04_retrain/a_once/results/main) · [`run.sh`](../../../../../../analysis/02_setup/04_retrain/a_once/run.sh).

---

> **A snapshot, generated 2026-09-27 from the tree at commit `3d89200`.** Everything here is derived from files the repository versions and regenerates in seconds with `.venv/bin/python AI-internal/useful-scripts/build_claim_tree_md.py` (or `/hierarchical-report`). If the tree has changed since that commit, rebuild rather than trust this copy; never hand-edit.
