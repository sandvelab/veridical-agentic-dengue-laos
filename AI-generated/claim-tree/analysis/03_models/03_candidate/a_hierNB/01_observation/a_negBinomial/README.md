[overview](../../../../../../README.md) / [analysis](../../../../../README.md) / [03_models](../../../../README.md) / [03_candidate](../../../README.md) / [a_hierNB](../../README.md) / [01_observation](../README.md) / **a_negBinomial**

# a_negBinomial

*On a path not taken — an alternative the reported analysis did not use. It is complete and runnable, and the stability analysis ran it.*

**Claim:** One negative-binomial distribution for every cell, with a single dispersion shared across provinces: the over-dispersion and the zeros are both absorbed by the same variance function rather than by a separate zero process.

**Result:**

The premise holds and is now on record: over the 2 383 observed cells the pooled
variance-to-mean ratio is **434** — a Poisson would give 1 — and **56 %** of cells are zero
(`results/main/model_option_spec.json`). A single stretched distribution is a defensible
carrier for both; so is a mixture, which is what the unbuilt siblings are for.

## Material

The node's own files: [`claim.md`](../../../../../../../../analysis/03_models/03_candidate/a_hierNB/01_observation/a_negBinomial/claim.md) · [`results/`](../../../../../../../../analysis/03_models/03_candidate/a_hierNB/01_observation/a_negBinomial/results) · [`scripts/`](../../../../../../../../analysis/03_models/03_candidate/a_hierNB/01_observation/a_negBinomial/scripts) · [`provenance/`](../../../../../../../../analysis/03_models/03_candidate/a_hierNB/01_observation/a_negBinomial/provenance) · [`run.sh`](../../../../../../../../analysis/03_models/03_candidate/a_hierNB/01_observation/a_negBinomial/run.sh).

---

> **A snapshot, generated 2026-09-27 from the tree at commit `3d89200`.** Everything here is derived from files the repository versions and regenerates in seconds with `.venv/bin/python AI-internal/useful-scripts/build_claim_tree_md.py` (or `/hierarchical-report`). If the tree has changed since that commit, rebuild rather than trust this copy; never hand-edit.
