[overview](../../../../../../README.md) / [analysis](../../../../../README.md) / [03_models](../../../../README.md) / [03_candidate](../../../README.md) / [c_ensemble](../../README.md) / [01_weighting](../README.md) / **b_crpsWeighted**

# b_crpsWeighted

*On a path not taken — an alternative the reported analysis did not use. It is complete and runnable, and the stability analysis ran it.*

**Claim:** The weights are the ones that minimise the pooled CRPS on a validation period held back from inside the training frame, so a member that forecast that period badly carries less of the pool.

**Result:**

**Not on the main path.** The weights minimising the pool's CRPS on the validation year
are persistence 0.047, climatology 0.000, candidate 1 **0.953**, candidate 2 0.000
(`../../results/weighting_crpsWeighted/fitted_model.json`), and the pool they give scores
**22.838** against the equal pool's 18.817.

**Two of the three registered predictions held and the third understated what happened**
(`../../results/weighting_crpsWeighted/pool_check.json`). Three members were predicted to
be possible below weight 0.05, and three are — a corner the sibling cannot reach at all.
More weight was predicted on the candidate families than on the baselines, and 0.953 of it
is. The third said the fitted weights would be a worse guide to the evaluated period than
to the validation period, so the pool would beat the equal pool by *less* than the 2.799
CRPS it beat it by there. It did not beat it by less; it lost to it by 4.021. The
direction was right and the magnitude was not, and reporting it as two-for-three rather
than three-for-three is the honest count.

**The solve is not what failed.** The weights are the exact minimiser of the pooled CRPS
on the cells they were fitted to: 14.227 against 14.253 for the best single member and
17.026 for equal weights, checked against every vertex of the simplex and against the
equal-weight point. What failed is the assumption that the validation period is
informative about the evaluated one, and it failed by a member's rank reversing between
the two.

## Material

The node's own files: [`claim.md`](../../../../../../../../analysis/03_models/03_candidate/c_ensemble/01_weighting/b_crpsWeighted/claim.md) · [`results/`](../../../../../../../../analysis/03_models/03_candidate/c_ensemble/01_weighting/b_crpsWeighted/results) · [`scripts/`](../../../../../../../../analysis/03_models/03_candidate/c_ensemble/01_weighting/b_crpsWeighted/scripts) · [`provenance/`](../../../../../../../../analysis/03_models/03_candidate/c_ensemble/01_weighting/b_crpsWeighted/provenance) · [`run.sh`](../../../../../../../../analysis/03_models/03_candidate/c_ensemble/01_weighting/b_crpsWeighted/run.sh).

---

> **A snapshot, generated 2026-09-27 from the tree at commit `3d89200`.** Everything here is derived from files the repository versions and regenerates in seconds with `.venv/bin/python AI-internal/useful-scripts/build_claim_tree_md.py` (or `/hierarchical-report`). If the tree has changed since that commit, rebuild rather than trust this copy; never hand-edit.
