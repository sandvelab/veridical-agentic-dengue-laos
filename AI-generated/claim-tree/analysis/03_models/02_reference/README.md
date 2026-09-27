[overview](../../../README.md) / [analysis](../../README.md) / [03_models](../README.md) / **02_reference**

# 02_reference

**Claim:** What does the field's own model score on this dataset? WHO EWARS-csd as published at chapkit_ewars_model, at its own default configuration, pinned by image digest and never tuned by us. It is unseeded, so it is run repeatedly and its spread carried rather than hidden.

**Result:**

The reference model scores **22.098 mean CRPS** over the same 371 cells, taken as the
per-cell mean of four repeats. The four individual repeats score 21.820, 21.917, 22.272 and
22.385 — a range of 0.57, or 2.6 % of the mean, from a model that is unseeded and cannot be
seeded. Batch 4 measured the same spread at sd 0.196 on a different set of four runs, so
this is a stable property of the model rather than an unlucky day.

It is well calibrated in the tails (10-90 coverage 0.804 against a nominal 0.80) and
materially too wide in the middle (25-75 coverage 0.602 against 0.50) — the mirror image of
our baselines, which are almost exact in the middle and far too thin in the tails.

**The asymmetry Rule 6 runs into is now demonstrated at both ends**: the models this project
builds are bit-reproducible, and the model it is measured against moves by half a CRPS
between identical runs. That is not a defect to be worked around but the quantity that sets
what the comparison can resolve.

## Claims resting on this node

- **[C24](../../../claims.md#c24)** — The reference model cannot be seeded, and its own re-run spread is the floor on what this backtest can attribute to a model at all. Four repeats score 21.820, 21.917, 22.272 and 22.385 mean CRPS, and the largest paired difference between two of them is 0.565 CRPS. Anything smaller than that belongs to the reference's sampler rather than to any model.

## Material

The node's own files: [`claim.md`](../../../../../analysis/03_models/02_reference/claim.md) · [`results/`](../../../../../analysis/03_models/02_reference/results) · [`scripts/`](../../../../../analysis/03_models/02_reference/scripts) · [`provenance/`](../../../../../analysis/03_models/02_reference/provenance) · [`results/main/`](../../../../../analysis/03_models/02_reference/results/main) · [`run.sh`](../../../../../analysis/03_models/02_reference/run.sh).

---

> **A snapshot, generated 2026-09-27 from the tree at commit `3d89200`.** Everything here is derived from files the repository versions and regenerates in seconds with `.venv/bin/python AI-internal/useful-scripts/build_claim_tree_md.py` (or `/hierarchical-report`). If the tree has changed since that commit, rebuild rather than trust this copy; never hand-edit.
