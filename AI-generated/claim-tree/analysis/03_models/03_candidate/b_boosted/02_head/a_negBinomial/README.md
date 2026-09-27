[overview](../../../../../../README.md) / [analysis](../../../../../README.md) / [03_models](../../../../README.md) / [03_candidate](../../../README.md) / [b_boosted](../../README.md) / [02_head](../README.md) / **a_negBinomial**

# a_negBinomial

*On a path not taken — an alternative the reported analysis did not use. It is complete and runnable, and the stability analysis ran it.*

**Claim:** One booster for the mean and a negative-binomial distribution around it, its dispersion estimated by maximum likelihood on the training fit. The width is a function of the level and of nothing else.

**Result:**

One booster and one dispersion. The fitted dispersion is **0.313**
(`../../results/family_boosted/head_premise_check.json`), covering a dataset whose
variance-to-mean ratio runs from 2.9 to 842.4 across the eighteen provinces — so a single
shared number is being asked to span more than two orders of magnitude, which is what the
premise recorded before the fit.

It nevertheless produces the best-calibrated model of ours so far: 10–90 coverage 0.825
against a nominal 0.80. The reason the shared dispersion does not hurt as it did in
candidate 1 is that the width here is `mu + mu^2/phi` around a mean the trees place per
cell, so a province the trees separate gets a different width by getting a different mean.
Candidate 1's width was constant on the log scale and could not do that.

## Material

The node's own files: [`claim.md`](../../../../../../../../analysis/03_models/03_candidate/b_boosted/02_head/a_negBinomial/claim.md) · [`results/`](../../../../../../../../analysis/03_models/03_candidate/b_boosted/02_head/a_negBinomial/results) · [`scripts/`](../../../../../../../../analysis/03_models/03_candidate/b_boosted/02_head/a_negBinomial/scripts) · [`provenance/`](../../../../../../../../analysis/03_models/03_candidate/b_boosted/02_head/a_negBinomial/provenance) · [`results/main/`](../../../../../../../../analysis/03_models/03_candidate/b_boosted/02_head/a_negBinomial/results/main) · [`run.sh`](../../../../../../../../analysis/03_models/03_candidate/b_boosted/02_head/a_negBinomial/run.sh).

---

> **A snapshot, generated 2026-09-27 from the tree at commit `3d89200`.** Everything here is derived from files the repository versions and regenerates in seconds with `.venv/bin/python AI-internal/useful-scripts/build_claim_tree_md.py` (or `/hierarchical-report`). If the tree has changed since that commit, rebuild rather than trust this copy; never hand-edit.
