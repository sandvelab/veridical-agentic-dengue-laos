[overview](../../../../../README.md) / [analysis](../../../../README.md) / [03_models](../../../README.md) / [03_candidate](../../README.md) / [a_hierNB](../README.md) / **01_observation**

# 01_observation

*On a path not taken — an alternative the reported analysis did not use. It is complete and runnable, and the stability analysis ran it.*

**Claim:** What observation model do the counts get? Monthly province counts on this dataset are heavily over-dispersed and about a third of them are zero, and whether that is one distribution stretched wide or a mixture of two processes is a modelling choice rather than something the data settles.

**Result:**

**The zeros and the large counts are two processes, and modelling them as one was the
candidate's largest single defect.** The hurdle -- a logistic model for whether a month
reports at all and a count model for how much it reports given that it does -- took the
candidate from **26.100** to **23.985** mean CRPS around the batch-8 configuration, past
both required baselines, and it is the main path from batch 9
(`AI-generated/candidate-forks/round1_batch8Defaults/fork_leaderboard.csv`).

**A mixture is not the same answer and is a much weaker one.** `b_zeroInflated` fitted a
mixing weight of **0.035** and scored **24.129** from the promoted main path, worse than
doing nothing. The negative binomial's variance function was already absorbing almost all
of the zeros; what it could not absorb was that the reporting months and the silent months
have different mean functions, which is what the hurdle gives them and the mixture does not.

**How much the hurdle is worth depends where you measure it from**: 2.115 CRPS around the
batch-8 configuration, **0.601** around the promoted one
(`round2_promoted/fork_interaction.csv`).

## Alternatives

Competing ways of answering this node's claim. The reported analysis takes the **main path**; the others are run by `05_stability`.

- [a_negBinomial](a_negBinomial/README.md) — *not taken*  
  One negative-binomial distribution for every cell, with a single dispersion shared across provinces: the over-dispersion and the zeros are both absorbed by the same …
- [b_zeroInflated](b_zeroInflated/README.md) — *not taken*  
  A mixture: a share of the zero months come from a process that reports nothing at all, and the rest of the record — zeros included — comes from the same negative …
- [c_hurdle](c_hurdle/README.md) — **main path**  
  Two processes rather than one distribution: whether a province-month reports any cases at all is a logistic model, and how many it reports given that it reports any is a …

## Material

The node's own files: [`claim.md`](../../../../../../../analysis/03_models/03_candidate/a_hierNB/01_observation/claim.md) · [`run.sh`](../../../../../../../analysis/03_models/03_candidate/a_hierNB/01_observation/run.sh).

---

> **A snapshot, generated 2026-09-27 from the tree at commit `3d89200`.** Everything here is derived from files the repository versions and regenerates in seconds with `.venv/bin/python AI-internal/useful-scripts/build_claim_tree_md.py` (or `/hierarchical-report`). If the tree has changed since that commit, rebuild rather than trust this copy; never hand-edit.
