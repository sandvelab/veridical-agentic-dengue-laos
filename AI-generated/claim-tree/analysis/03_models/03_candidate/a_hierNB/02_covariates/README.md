[overview](../../../../../README.md) / [analysis](../../../../README.md) / [03_models](../../../README.md) / [03_candidate](../../README.md) / [a_hierNB](../README.md) / **02_covariates**

# 02_covariates

*On a path not taken — an alternative the reported analysis did not use. It is complete and runnable, and the stability analysis ran it.*

**Claim:** Which climate covariates enter the mean, and at which lags? The file carries rainfall, mean temperature and mean relative humidity, and a transmission signal reaches reported cases only after a delay, so the covariate set and the lag are one joint choice.

**Result:**

**This fork cannot be settled on this dataset, and that is the answer.** Around the batch-8
configuration, dropping the climate covariates entirely *improved* the candidate by
**0.648** CRPS and adding all three at three lags improved it by 0.461 -- both better than
the reference family's own published Lao pair at lag 2. Measured again from the promoted
main path the ordering changes: the rich set is worth **+0.821**, and putting the two
lagged covariates back is worth **+0.112**, so the climate-free choice the promotion took
is now marginally the worse one (`round2_promoted/fork_interaction.csv`).

Two of those four numbers are inside the 0.57 CRPS resolvable floor and the ordering
reverses between sweeps, so no child of this fork is established as better than another.

**What is established** is why. In `b_rich` the fitted seasonal harmonic `sin1` collapses
from −1.235 to **−0.027** as nine climate columns enter, while mean temperature at lag 1
takes **+0.653**: the climate columns and the calendar are substituting for each other
rather than adding. On this dataset the annual cycle can be carried by either, and the
model scores about the same whichever carries it.

## Alternatives

Competing ways of answering this node's claim. The reported analysis takes the **main path**; the others are run by `05_stability`.

- [a_lagged](a_lagged/README.md) — *not taken*  
  Rainfall and mean temperature only, each entering linearly at a two-month lag — the covariate pair and the lag the reference model's own published Lao configuration …
- [b_rich](b_rich/README.md) — *not taken*  
  All three climate columns — rainfall, mean temperature and mean relative humidity — each at one, two and three months' lag, letting the fit decide which of them carries …
- [c_climateFree](c_climateFree/README.md) — **main path**  
  No climate covariates at all, so that the shared annual harmonics and the province-year effect alone carry the seasonal cycle. If this scores like the lagged-climate …

## Material

The node's own files: [`claim.md`](../../../../../../../analysis/03_models/03_candidate/a_hierNB/02_covariates/claim.md) · [`run.sh`](../../../../../../../analysis/03_models/03_candidate/a_hierNB/02_covariates/run.sh).

---

> **A snapshot, generated 2026-09-27 from the tree at commit `3d89200`.** Everything here is derived from files the repository versions and regenerates in seconds with `.venv/bin/python AI-internal/useful-scripts/build_claim_tree_md.py` (or `/hierarchical-report`). If the tree has changed since that commit, rebuild rather than trust this copy; never hand-edit.
