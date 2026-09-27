[overview](../README.md) / **analysis**

# analysis

**Claim:** Can a spatio-temporal model of monthly dengue case counts across the admin-1 provinces of
Laos, developed as autonomously as this setup allows, forecast well enough under Chap's own
cross-validated backtest to beat a persistence and a seasonal-climatology baseline on mean
CRPS — and how far does that answer survive the reasonable alternatives to the judgment
calls made along the way?
The question has two halves and neither is subordinate. The forecasting half is settled on
a held-out year (2010) that is absent from the data development ever sees; the veridical
half is settled by the alternatives siblings in this tree and by the stability node that
runs them.

**Result:**

**The forecasting half: yes, on both datasets, and by a margin the evaluation cannot
separate.** The reported model is candidate 3, a linear opinion pool over two candidate
families and both required baselines. On the development backtest it scores **18.817** mean
CRPS against the reference model's 22.098 — a skill score of **+0.1485** — and beats both
required baselines. On the held-out year, which was opened once and evaluated on a set of
analyses frozen beforehand, it scores **76.731** against the reference's **84.026**, a skill
score of **+0.0868**, and again beats both required baselines.
→ `results/main/conclusion.json`, `results/main__holdout/conclusion.json`

**Nothing here reaches significance and nothing pretends to.** The pool is 1.90 standard
errors from the reference on development and less than one on the holdout, where the
backtest is four splits rather than eight. The reference is unseeded, and below **0.57 CRPS**
on development and **1.30** on the holdout nothing can be attributed to a model at all,
because that is how far the reference moves against itself. "We cannot separate these two" is
the honest reading of the margin, and it is the reading. → `04_score/03_compare`

**The veridical half is the larger result, and it is a distribution rather than a number.**
Thirty-two analyses that all looked reasonable were fixed before either dataset was scored.
On development the skill score runs **−0.0724 to +0.2320** around the reported +0.1485, which
sits thirteenth of thirty-two. On the held-out year it runs **−0.5038 to +0.2026** around
+0.0868, eighteenth of thirty-two — **a spread more than twice as wide**.
→ `05_stability/results/distribution.json`, `holdout_distribution.json`

**Most of the effort went below the resolution of the evaluation.** Six of the seventeen
judgment calls the tree carries move the conclusion further than the reference model moves on
its own; eleven do not, and nine of those eleven are the candidate-internal forks phase C
spent three of its four batches choosing among.
→ `05_stability/results/sensitivity_by_fork.csv`

**The development set is a weak guide to the held-out year.** Twenty-eight of the thirty-two
analyses scored worse on 2010, and the rank correlation between the two skill scores is
**+0.396**. The fork ranking transfers better, at +0.679, with 14 of 17 forks agreeing on
whether they matter — but the largest single effect on the holdout, the province filter at
0.2696, was fourth and nearly negligible on development — and the analysis behind it ranked
fourth of thirty-two there, highest of every analysis that does not re-weight the headline
mean, against twenty-ninth on the held-out year.
→ `05_stability/results/holdout_vs_development.json`, `fork_sensitivity_both.csv`

**Calibration is reported beside the score and not under it**, because a badly calibrated
CRPS winner has not won. The reported model is the most over-dispersed in the project on
development — 10–90 coverage 0.863 against a nominal 0.80 — and 0.755 on the holdout; across
the frozen set, coverage runs 0.458 to 0.920 on development and 0.210 to 0.854 on 2010.

**The drop from the development backtest to the held-out year is not about 2010, and the
model's Lao margin is partly about Laos.** Run unchanged on two other countries of the same
harmonisation, on the same months and under the same two schemes, the model drops in both:
Thailand +0.0856 to +0.0197, Vietnam +0.0852 to **−0.0862**, against Laos's +0.1485 to
+0.0868. All three drops exceed the two reference bands they are measured against. And the
two countries the model was never developed on agree with each other to 0.0004 on the
development arrangement while sitting 0.063 below Laos, which is about the size of the drop
itself. It beats both required baselines on all six analyses and the reference on five.
→ `06_external/results/external_vs_laos.json`, `external_conclusions.csv`

**What the evaluation can resolve is a property of the country and not of the method.** The
reference model's four unseeded repeats span 0.032 CRPS on Thailand's development backtest,
0.565 on Laos's and 7.082 on Vietnam's — a factor of 219 on one model at one configuration.
Vietnam's +0.0852 margin is inside its own noise floor; Thailand's near-identical +0.0856 is
thirty-five times it. → `06_external/results/external_conclusions.csv`

_(Every figure above is read from a file this tree produced. Nothing in this section states a
number that is not in `results/main/conclusion.json`, `results/main__holdout/conclusion.json`,
`06_external/results/external_conclusions.csv` or the files those name.)_

## Claims resting on this node

- **[C14](../claims.md#c14)** — The reported model beats the reference model and both required baselines on the held-out year as well as on the development period, at a skill score of +0.0868 against +0.1485. The gap between the two is -0.0617, and it is a gap in a ratio rather than in a raw score: 2010 was a much harder year, and the reference model, which nobody here tuned, scores 84.026 mean CRPS on it against 22.098 on development.
- **[C22](../claims.md#c22)** — On the development backtest the model this project reports beats the reference model and both required baselines: mean CRPS 18.817 against the reference's 22.098, a skill score of +0.1485, and the lower CRPS in six of the eight splits. The model is a linear opinion pool over two candidate families and the two required baselines.

## Sub-analyses

- [01_data](01_data/README.md) · 1 claim  
  What does the Lao admin-1 monthly dengue dataset contain, and on what part of it may development happen? The node separates the held-out final year from the development …
- [02_setup](02_setup/README.md)  
  What dataset and evaluation setting do all models — ours, the baselines and the reference — face in common? Everything decided here moves every model together, so a …
- [03_models](03_models/README.md) · 2 claims  
  What forecast does each model make on that common ground? The node holds every model the project scores — our baselines, our candidates and the external reference — so …
- [04_score](04_score/README.md)  
  What does each model score, and how do they compare, at every resolution the platform allows? Scores are collected once at the platform's finest resolution and …
- [05_stability](05_stability/README.md) · 21 claims  
  How far does the project's conclusion survive the reasonable alternatives the main path did not take? The node enumerates every judgment call the tree carries as a fork, …
- [06_external](06_external/README.md) · 5 claims  
  Does the reported model, run unchanged on two other countries' data from the same harmonisation, hold the margin it holds on Laos — and does the drop from the …

## Material

The node's own files: [`claim.md`](../../../analysis/claim.md) · [`results/`](../../../analysis/results) · [`scripts/`](../../../analysis/scripts) · [`provenance/`](../../../analysis/provenance) · [`results/main/`](../../../analysis/results/main) · [`run.sh`](../../../analysis/run.sh).

---

> **A snapshot, generated 2026-09-27 from the tree at commit `3d89200`.** Everything here is derived from files the repository versions and regenerates in seconds with `.venv/bin/python AI-internal/useful-scripts/build_claim_tree_md.py` (or `/hierarchical-report`). If the tree has changed since that commit, rebuild rather than trust this copy; never hand-edit.
