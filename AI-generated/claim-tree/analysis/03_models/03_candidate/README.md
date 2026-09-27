[overview](../../../README.md) / [analysis](../../README.md) / [03_models](../README.md) / **03_candidate**

# 03_candidate

**Claim:** Which model family should our candidate be? Each child is one family — one possible answer to the same question of what forecast our model makes — so exactly one of them is ever the reported model, and the others are re-run in the stability work rather than discarded.

**Result:**

**Three families exist, and the fork moves for the first time: the main path is
`c_ensemble`.** At each family's own main path, over the same 371 cells
(`AI-generated/candidate-forks/families/family_leaderboard.csv`):

| family | combination | mean CRPS | MAE | 10–90 | 25–75 | skill |
|---|---|---|---|---|---|---|
| **`c_ensemble`** | `main` | **18.817** | 23.214 | 0.863 | 0.749 | +0.1485 |
| `b_boosted` | `family_boosted` | 20.771 | 26.953 | 0.825 | 0.693 | +0.0601 |
| `a_hierNB` | `family_hierNB` | 23.698 | 27.569 | 0.701 | 0.582 | −0.0724 |

The pool beats the family it replaces by **4.881** CRPS, 8.6 times the 0.565 resolvable
difference floor, and its 10–90 coverage is closer to nominal than that family's, so the
calibration veto in `AI-generated/candidate-forks/family_rule.md` does not fire. The rule
was committed before the promoted family was run under `main`.

**What the switch this node performs now costs is measurable rather than arguable.** The
two demoted families stay in the tree, each runnable under a combination of its own, and
both are re-run in phase D and on the held-out year — which is what turns a selection made
on development CRPS into a measured cost. Candidate 1's per-cell scores under
`family_hierNB` are identical to the ones it produced when it was the main path.

**The families are not independent of each other**, and that is a property of this fork
rather than an accident: `c_ensemble` contains `a_hierNB` and `b_boosted` as members, so
choosing it does not discard the other two so much as weight them. A perturbation that
moves a fork inside candidate 1 moves the pool's candidate-1 member with it, because both
are configured by the same fork nodes.

## Alternatives

Competing ways of answering this node's claim. The reported analysis takes the **main path**; the others are run by `05_stability`.

- [a_hierNB](a_hierNB/README.md) — *not taken* · 1 claim  
  …a hierarchical negative-binomial GLM: monthly province counts as negative-binomial draws around a log-linear mean built from a population offset, a shared annual …
- [b_boosted](b_boosted/README.md) — *not taken* · 1 claim  
  …gradient-boosted trees with a probabilistic head: the conditional distribution of a province-month's count built in two pieces, a boosted-tree fit for where the count …
- [c_ensemble](c_ensemble/README.md) — **main path** · 4 claims  
  …a weighted combination of the models this project already has: the two candidate families and the two required baselines, pooled into one predictive distribution rather …

## Material

The node's own files: [`claim.md`](../../../../../analysis/03_models/03_candidate/claim.md) · [`run.sh`](../../../../../analysis/03_models/03_candidate/run.sh).

---

> **A snapshot, generated 2026-09-27 from the tree at commit `3d89200`.** Everything here is derived from files the repository versions and regenerates in seconds with `.venv/bin/python AI-internal/useful-scripts/build_claim_tree_md.py` (or `/hierarchical-report`). If the tree has changed since that commit, rebuild rather than trust this copy; never hand-edit.
