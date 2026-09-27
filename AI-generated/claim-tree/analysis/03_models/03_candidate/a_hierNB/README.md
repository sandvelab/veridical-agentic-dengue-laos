[overview](../../../../README.md) / [analysis](../../../README.md) / [03_models](../../README.md) / [03_candidate](../README.md) / **a_hierNB**

# a_hierNB

*On a path not taken — an alternative the reported analysis did not use. It is complete and runnable, and the stability analysis ran it.*

**Claim:** …a hierarchical negative-binomial GLM: monthly province counts as negative-binomial draws around a log-linear mean built from a population offset, a shared annual seasonality and lagged climate covariates, with province and province-year effects pooled toward a common level. The node's six children are the choices that shape it; the node itself assembles those choices into one model configuration and sends the model through the same chap eval path as every other model in the project.

**Result:**

**Mean CRPS 26.100 over 371 cells in 16 provinces, at 43 seconds for the eight-split
backtest** (`results/main/run_cost.json`) — the worst of the four models scored so far, and
worse than both required baselines.

**The same model has the best point forecast in the project.** Mean absolute error **27.106**
against the reference's 28.902, climatology's 30.620 and persistence's 29.073, and the best
interval coverage of any model of ours: **0.720** at 10–90 and **0.590** at 25–75, against
nominal 0.80 and 0.50. The centre of the forecast is right and its width is wrong, which is a
different repair from the one a model with a bad centre needs.

**The width is wrong locally, not on average.** Two provinces carry 2.4 of the 4.0 CRPS gap
to the reference (`04_score/02_aggregate/a_unweighted/results/main/crps_by_location.csv`): in
Vientiane Capital the 10–90 interval covers **every** outcome, and in Salavan it covers
**0.125**. The province-year variance is a single number shared by all provinces, so on the
log scale it is a constant multiplicative width — too much where the burden is largest and
too little where the epidemic years are sharpest.

The fit itself: between-province spread sigma **2.06** on the log-incidence scale,
between-year spread within a province sigma **1.47**, negative-binomial dispersion **0.83**,
converged in 24 EM rounds on 1 978 usable rows over 17 provinces and 168 province-years
(`results/main/fitted_model.json`).

#### Batch 9 — the six forks, swept and promoted

**The candidate now beats both required baselines and is not distinguishable from the
reference.** Mean CRPS **23.698** over the same 371 cells, against climatology's 24.337,
persistence's 24.879 and the reference's 22.098
(`04_score/03_compare/results/main/leaderboard.csv`). The paired difference against the
reference is **1.599** with a split-clustered standard error of **1.551** -- 1.03 standard
errors, against 3.62 for the batch-8 configuration. The project's reported skill score moved
from −0.181 to **−0.072**.

**It is still under-dispersed and still fails in the same two places.** 10–90 coverage
**0.701** against a nominal 0.80. Salavan's coverage is **0.12**, unchanged from batch 8; the
too-wide half of the width defect was repaired and the too-narrow half was not. By lead time
the candidate is 20.4 / 23.2 / **27.5** against the reference's 16.5 / 22.0 / 27.8, so at
three months it is level with the field's own model and at one month it is not close.

**The forks do not add.** Three forks worth 2.115, 1.870 and 0.648 CRPS one at a time
delivered **2.402** together, not 4.632, and two of the nine children measured in both
sweeps reversed sign
(`AI-generated/candidate-forks/round2_promoted/fork_interaction.json`).

## Claims resting on this node

- **[C27](../../../../claims.md#c27)** — The model family the project built first never beat the reference model. The hierarchical negative-binomial GLM scores 23.698 mean CRPS against 22.098, a skill score of -0.0724, and it is the lowest of the thirty-two analyses in the development distribution. It does beat both required baselines, and it stays in the reported model as a pool member.

## Sub-analyses

- [01_observation](01_observation/README.md)  
  What observation model do the counts get? Monthly province counts on this dataset are heavily over-dispersed and about a third of them are zero, and whether that is one …
- [02_covariates](02_covariates/README.md)  
  Which climate covariates enter the mean, and at which lags? The file carries rainfall, mean temperature and mean relative humidity, and a transmission signal reaches …
- [03_population](03_population/README.md)  
  How does the province population enter the model? The file's population figure is one constant per province, and it can serve as a denominator the model forecasts a rate …
- [04_fitTime](04_fitTime/README.md)  
  Does the model do its fitting in train or in predict? Chap fits once and then predicts at every split, so a model that refits inside predict sees each split's expanded …
- [05_autoregressive](05_autoregressive/README.md)  
  Does the model see the recent case history, or only the calendar and the weather? A seasonal regression forecasts the average year; the last observed count is what would …
- [06_yearVariance](06_yearVariance/README.md)  
  Is the year-to-year variability of dengue the same relative size in every province? The province-year effect's variance sets how wide every forecast is, and one number …

## Material

The node's own files: [`claim.md`](../../../../../../analysis/03_models/03_candidate/a_hierNB/claim.md) · [`results/`](../../../../../../analysis/03_models/03_candidate/a_hierNB/results) · [`scripts/`](../../../../../../analysis/03_models/03_candidate/a_hierNB/scripts) · [`provenance/`](../../../../../../analysis/03_models/03_candidate/a_hierNB/provenance) · [`results/main/`](../../../../../../analysis/03_models/03_candidate/a_hierNB/results/main) · [`run.sh`](../../../../../../analysis/03_models/03_candidate/a_hierNB/run.sh).

---

> **A snapshot, generated 2026-09-27 from the tree at commit `3d89200`.** Everything here is derived from files the repository versions and regenerates in seconds with `.venv/bin/python AI-internal/useful-scripts/build_claim_tree_md.py` (or `/hierarchical-report`). If the tree has changed since that commit, rebuild rather than trust this copy; never hand-edit.
