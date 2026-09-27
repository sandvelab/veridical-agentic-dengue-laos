[overview](../../../../../README.md) / [analysis](../../../../README.md) / [03_models](../../../README.md) / [03_candidate](../../README.md) / [c_ensemble](../README.md) / **01_weighting**

# 01_weighting

**Claim:** How much weight does each member of the pool carry? Every member is a model that was fitted and evaluated on this dataset already, and the two answers differ in whether the pool is told anything about how well they did.

**Result:**

**The fork does not move, and the reason is the most useful thing in the batch.** Equal
weights score **18.817**; the minimum-CRPS weights score **22.838**
(`AI-generated/candidate-forks/ensemble_round1/fork_leaderboard.csv`). Estimating the
weights costs **4.021 CRPS** — seven times the 0.565 floor, in the wrong direction — so
batch 9's promotion rule leaves `a_equal` on the main path, as it would have even if the
gap had been a tenth the size.

**What estimating them did.** On the validation year held back inside the training frame,
the pooled CRPS at the fitted weights is 14.227 against 17.026 at equal weights: fitting
looked worth 2.799 CRPS where it was fitted. It put 0.953 of the pool on candidate 1,
which was the best member on that year at CRPS 14.253. On the evaluated period candidate 1
is the *worst* of the three non-baseline members at 23.698, and the pool it dominates
scores 22.838 — 2.067 worse than the best member it was supposed to be selecting.

So the fork measures one thing cleanly: **on this dataset, one year of held-back data
cannot tell which member will be best on the next two.** That is the failure the plan's
phase C names — fitting the available data rather than the data-generating process — with
the two sides of it in one table, and the model that estimates nothing is the one that
survives it.

## Claims resting on this node

- **[C26](../../../../../claims.md#c26)** — Fitting the pool's weights costs far more than it buys. Weights chosen by minimising the pool's CRPS on a validation period held back inside the training frame score 22.838 mean CRPS against equal weights' 18.817 -- 4.021 CRPS worse, and enough to lose to the reference model that equal weighting beats.

## Alternatives

Competing ways of answering this node's claim. The reported analysis takes the **main path**; the others are run by `05_stability`.

- [a_equal](a_equal/README.md) — **main path**  
  Every member carries the same weight. The pool is told nothing about how well its members did, so no member's weight can be a selection made on data the backtest will …
- [b_crpsWeighted](b_crpsWeighted/README.md) — *not taken*  
  The weights are the ones that minimise the pooled CRPS on a validation period held back from inside the training frame, so a member that forecast that period badly …

## Material

The node's own files: [`claim.md`](../../../../../../../analysis/03_models/03_candidate/c_ensemble/01_weighting/claim.md) · [`run.sh`](../../../../../../../analysis/03_models/03_candidate/c_ensemble/01_weighting/run.sh).

---

> **A snapshot, generated 2026-09-27 from the tree at commit `3d89200`.** Everything here is derived from files the repository versions and regenerates in seconds with `.venv/bin/python AI-internal/useful-scripts/build_claim_tree_md.py` (or `/hierarchical-report`). If the tree has changed since that commit, rebuild rather than trust this copy; never hand-edit.
