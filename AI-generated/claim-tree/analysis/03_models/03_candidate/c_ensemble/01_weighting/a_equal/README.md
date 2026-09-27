[overview](../../../../../../README.md) / [analysis](../../../../../README.md) / [03_models](../../../../README.md) / [03_candidate](../../../README.md) / [c_ensemble](../../README.md) / [01_weighting](../README.md) / **a_equal**

# a_equal

**Claim:** Every member carries the same weight. The pool is told nothing about how well its members did, so no member's weight can be a selection made on data the backtest will later score.

**Result:**

**On the main path, at weight 0.25 each** (`results/main/model_option_spec.json`,
`../../results/main/pool_check.json`). The pool it produces scores 18.817, ahead of the
minimum-CRPS sibling's 22.838 and of all four of its own members.

**The premise registered here before the run was half wrong, and the wrong half is the
finding.** It predicted that an equal pool would score worse than its best member, because
half its mass sits on the two required baselines and they are the two worst-scoring models
of ours. The pool beat its best member by 1.954 CRPS. The prediction reasoned about where
the forecasts sit and not about how wide they are, and CRPS is a function of both: every
member except candidate 2 under-covers its 10–90 interval, and pooling widens.

The other half held exactly as stated: the pool's 10–90 coverage, 0.863, is above the
largest of its members' (0.825), so it is wider than any member and over-covers where one
member already did.

## Material

The node's own files: [`claim.md`](../../../../../../../../analysis/03_models/03_candidate/c_ensemble/01_weighting/a_equal/claim.md) · [`results/`](../../../../../../../../analysis/03_models/03_candidate/c_ensemble/01_weighting/a_equal/results) · [`scripts/`](../../../../../../../../analysis/03_models/03_candidate/c_ensemble/01_weighting/a_equal/scripts) · [`provenance/`](../../../../../../../../analysis/03_models/03_candidate/c_ensemble/01_weighting/a_equal/provenance) · [`results/main/`](../../../../../../../../analysis/03_models/03_candidate/c_ensemble/01_weighting/a_equal/results/main) · [`run.sh`](../../../../../../../../analysis/03_models/03_candidate/c_ensemble/01_weighting/a_equal/run.sh).

---

> **A snapshot, generated 2026-09-27 from the tree at commit `3d89200`.** Everything here is derived from files the repository versions and regenerates in seconds with `.venv/bin/python AI-internal/useful-scripts/build_claim_tree_md.py` (or `/hierarchical-report`). If the tree has changed since that commit, rebuild rather than trust this copy; never hand-edit.
