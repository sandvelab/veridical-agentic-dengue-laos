[overview](../../README.md) / [analysis](../README.md) / **06_external**

# 06_external

**Claim:** Does the reported model, run unchanged on two other countries' data from the same
harmonisation, hold the margin it holds on Laos — and does the drop from the development
backtest to the final year replicate?
The plan's §4 named `tha` and `vnm` as an optional external check and the human confirmed
it on 2026-08-31, ahead of the release, so that the case write-up could use it. It is here
because phase E's largest open question cannot be answered from inside this project: the
holdout spread is measured on one year through four splits, and nothing in the Lao data can
say whether its width is about 2010, about one-year backtests, or about an agent optimising
freely against a development set. Two more countries, on the same months under the same two
schemes, are two more measurements of the same difference.
**Nothing here is developed, tuned or selected.** No fork moves in any of these rows: each
runs the reported analysis — every setup fork at its main child, both required baselines,
the reference model's four unseeded repeats, the linear opinion pool and the scoring chain
— with the file underneath replaced. The step lists come from the same driver the
perturbation set runs through, because a check that ran different code would measure the
code and not the model.

**Result:**

**The margin holds in five of the six analyses, and the one it does not hold in is a
held-out year.** The reported model, unchanged, beats the reference model on both sibling
countries' development backtests — **+0.0852 on Vietnam and +0.0856 on Thailand** — and on
Thailand's final year at **+0.0197**. On Vietnam's final year it **loses**, at **−0.0862**.
It beats both required baselines on **all six**, including the row it loses on.
→ `results/external_conclusions.csv`, `results/external_vs_laos.json`

**The drop from the development backtest to the final year replicates in both countries.**
Laos −0.0617, Thailand −0.0659, Vietnam −0.1714. **The clause that all three clear the two
reference bands together holds on this draw and not on the next**: the clean-room run of
2026-09-05 returned it false for Laos and for Thailand and true only for Vietnam, so it is
withdrawn as a general statement. What survives both draws is the direction in all three
countries, the ordering, and the sign of the Vietnamese final-year loss. Three countries are not a sample and this does not put a
confidence statement on the effect; what it says is that phase E's central finding is a
thing that happens repeatedly rather than a thing that happened once, and that 2010 alone
does not account for it — the same year is harder for the model relative to the reference
in every country, including the two it never saw.
→ `results/external_vs_laos.json`, `results/fig_external_skill.png`

**The country the model was developed on is the country it scores highest on.** Its Lao
development skill, +0.1485, is **1.74 times** either sibling's, and the two siblings agree
with each other to 0.0004 while differing from Laos by 0.063. That difference is the
project's most direct measurement of what developing against one dataset bought on that
dataset, and it is about as large as the whole development-to-final-year drop.
→ `results/external_conclusions.csv`

**The reference model's own instability is a property of the country, not of the method.**
Its four unseeded repeats span **0.032 CRPS on Thailand's development backtest, 0.565 on
Laos's and 7.082 on Vietnam's** — a factor of **219** across three countries of one
harmonisation, on the same model at the same configuration. In skill that is a band of 0.0024, 0.0256 and 0.1230, so Vietnam's +0.0852
margin sits **inside** the reference's own re-run spread and cannot be attributed to a model
at all, while Thailand's near-identical +0.0856 is thirty-six times its band. A noise floor
measured on one dataset says nothing about another.
→ `results/external_conclusions.csv`

**The reported model's over-dispersion is worse abroad than at home.** Its 10–90 coverage
against a nominal 0.80 is 0.863 on Lao development and 0.941 and 0.967 on the two siblings';
on the final years, 0.755, 0.893 and 0.875. The calibration failure the project reports
beside its Lao score is not a Lao artefact and does not shrink when the model meets more
provinces.
→ `results/external_conclusions.csv`

**The pool's independent reconstruction is not available on these datasets**, because a
member is evaluated on its own only under the family fork's own combination and this check
moves no fork. Recorded, with what it would have cost, rather than left blank.
→ `results/pool_reconstruction_external.json`

**The cost model over-predicted by a factor of about two, and its worst row is again the
one whose shape it does not know.** Planned 3.14 hours, actual **1.81** — a ratio of 0.58
where phase D's two halves came out at 1.00 and 1.15. Per row it runs 0.39 to 1.20, so the
total being wrong this time and right twice before is the same finding a third way: seconds
per evaluated cell measured on 192 Lao cells does not transfer to 1 824 Thai ones, and the
one row that exceeds its estimate is the largest.
→ `results/external_cost_planned_vs_actual.json`

## Claims resting on this node

- **[C42](../../claims.md#c42)** — The development-to-final-year drop measured on Laos replicates on both sibling countries, so it is not about 2010 alone. Run unchanged on the Thai and Vietnamese files of the same harmonisation, on the same months and under the same two schemes, the reported model's skill score against the reference falls from +0.0856 to +0.0197 on Thailand and from +0.0852 to -0.0862 on Vietnam, against Laos's +0.1485 to +0.0868. All three drops -- -0.0659, -0.1714 and -0.0617 -- are larger than the two reference re-run bands they are measured against, taken together.
- **[C43](../../claims.md#c43)** — The country the model was developed on is the country it scores highest on, and the two it never saw agree with each other almost exactly. On the development arrangement the reported model's skill score is +0.1485 on Laos, +0.0856 on Thailand and +0.0852 on Vietnam: the two siblings differ from each other by 0.0004 and from Laos by 0.063, which is about the size of the whole development-to-final-year drop on Laos.
- **[C44](../../claims.md#c44)** — What the backtest can resolve is a property of the country rather than of the evaluation. The reference model is unseeded and is scored four times on every dataset; the largest paired difference between two of its repeats is 0.032 CRPS on Thailand's development backtest, 0.565 on Laos's and 7.082 on Vietnam's -- a factor of 219 on one model at one configuration. So Vietnam's +0.0852 margin sits inside the reference's own re-run spread and cannot be attributed to a model at all, while Thailand's near-identical +0.0856 is about thirty-six times its band.
- **[C45](../../claims.md#c45)** — The reported model's over-dispersion is not a Lao artefact and gets worse on the sibling countries. Its 10-90 interval coverage against a nominal 0.80 is 0.863 on Lao development, 0.941 on Vietnam's and 0.967 on Thailand's, and 0.755, 0.893 and 0.875 on the three final years. It beats both required baselines on all six analyses and the reference model on five of the six, losing only on Vietnam's final year.
- **[C47](../../claims.md#c47)** — The cost model's total was wrong on the external check in the direction its two earlier tests were right. Planned 3.14 hours against 1.81 actual, a ratio of 0.58, where phase D's development half came out at 1.00 and its frozen holdout half at 1.15; per row it runs 0.39 to 1.20. The unit is seconds per evaluated cell measured on the Lao holdout, and it does not transfer to datasets four to ten times the size -- so the total being right twice was a property of estimating a set against itself, and the cut order such estimates rank still carries no information.

## Material

The node's own files: [`claim.md`](../../../../analysis/06_external/claim.md) · [`results/`](../../../../analysis/06_external/results) · [`scripts/`](../../../../analysis/06_external/scripts) · [`provenance/`](../../../../analysis/06_external/provenance) · [`run.sh`](../../../../analysis/06_external/run.sh).

---

> **A snapshot, generated 2026-09-27 from the tree at commit `3d89200`.** Everything here is derived from files the repository versions and regenerates in seconds with `.venv/bin/python AI-internal/useful-scripts/build_claim_tree_md.py` (or `/hierarchical-report`). If the tree has changed since that commit, rebuild rather than trust this copy; never hand-edit.
