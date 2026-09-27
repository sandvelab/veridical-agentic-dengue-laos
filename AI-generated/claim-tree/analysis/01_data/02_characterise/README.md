[overview](../../../README.md) / [analysis](../../README.md) / [01_data](../README.md) / **02_characterise**

# 02_characterise

**Claim:** What is in the development period: how complete is it per province and per year, how are dengue counts distributed, what seasonality do they show, and how do the climate covariates behave? Which of its features are analytic problems that phase D must perturb rather than preprocessing details?

**Result:**

**The development period is a small, zero-heavy, strongly seasonal panel.** 2 592 rows over
18 provinces and 144 months, 77 031 reported cases in total. 8.1% of target cells are
missing and 56.3% of the observed ones are zero. Cases peak in July–September at roughly
fourteen times the February trough.
→ `results/dev_overview.json`, `results/seasonality_by_month.csv`, `results/fig_cases_seasonality.png`

**The headline metric is a mean over 16 provinces, not 18.** Vientiane (LA-VI) reports
nothing in the whole development period and is dropped by chap-core's own region filter.
Xaisomboun (LA-XN) reports through 2005-12 and then stops, so it survives the filter — which
looks only at the training period — and still contributes no evaluable cell. Under the fixed
scheme the metric averages 371 cells, not the nominal 408.
→ `results/evaluable_cells_by_province.csv`, `results/backtest_scheme_chosen.json`, `results/fig_completeness.png`

**The burden spans four orders of magnitude across provinces**, and six provinces report
zero in more than 85% of their observed months. An unweighted mean CRPS gives each of them
the same weight as the capital, so the headline number can be moved by provinces where the
answer is almost always zero. This is a property of the plan's chosen metric, established
before any model exists.
→ `results/cases_by_province.csv`, `results/fig_province_burden.png`

**Climate leads dengue, consistently in sign and loosely in size.** Rainfall associates most
strongly at a lag of one month, temperature at two to three, humidity at nought to one; each
is positive in 16 or 17 of the 17 provinces, with a min–max band across provinces roughly
0.0 to 0.7. The negative values at lags five and six are the far side of the annual cycle.
→ `results/lag_correlation.csv`, `results/fig_covariate_lag_correlation.png`

**The backtest scheme is fixed and does not move again.** Development: `n_periods 3`,
`n_splits 8`, `stride 3`, `n_retrain 1`, evaluating 2008-01 to 2009-12 from a training set
ending 2007-12. Phase E: `n_periods 3`, `n_splits 4`, `stride 3` on the full file, evaluating
exactly 2010.
→ `results/backtest_scheme_chosen.json`, `results/backtest_scheme_candidates.csv`, `results/split_schedule.csv`

**Two of the schema's statements do not describe the file.** `population` is a single 2020
snapshot repeated across all thirteen years — confirmed, one distinct value per province.
`rainfall`, declared as a monthly total in millimetres, is a mean daily rate: read as
declared it puts a province's year at 50–78 mm, read as mm/day at 1 518–2 383 mm.
→ `results/population_static_check.csv`, `results/covariate_units_check.json`

## Claims resting on this node

- **[C32](../../../claims.md#c32)** — The headline mean is over 16 provinces and 371 cells, not the 18 provinces the file contains. Chap's own region filter rejects Vientiane province, which reports nothing anywhere in the record, and keeps Xaisomboun, which stops reporting after 2005 and contributes no evaluable cell to the evaluated span; Phongsaly contributes 11 cells of a possible 24. Of the 408 province-months in the span, 371 are scored.
- **[C34](../../../claims.md#c34)** — The target is mostly zeros, and the record gets less complete as it goes on. Of the 2 383 observed province-months in the development period 56.3 % are exactly zero and a further 8.1 % of the grid is missing; reporting completeness holds at 94.4 % through 2005 and falls to 83.3 % by 2008, so the evaluated span is the least complete part of the record.
- **[C36](../../../claims.md#c36)** — The evaluation scheme was fixed before any model ran and never moved: three-month horizons, eight splits, stride three, retrained once, evaluating 2008-01 to 2009-12 from a training set ending 2007-12. The schedule was read out of chap-core's own splitter rather than reimplemented, and the phase-E arrangement -- same horizon and stride, four splits -- evaluates exactly 2010 from training that never reaches into it.

## Material

The node's own files: [`claim.md`](../../../../../analysis/01_data/02_characterise/claim.md) · [`results/`](../../../../../analysis/01_data/02_characterise/results) · [`scripts/`](../../../../../analysis/01_data/02_characterise/scripts) · [`provenance/`](../../../../../analysis/01_data/02_characterise/provenance) · [`run.sh`](../../../../../analysis/01_data/02_characterise/run.sh).

---

> **A snapshot, generated 2026-09-27 from the tree at commit `3d89200`.** Everything here is derived from files the repository versions and regenerates in seconds with `.venv/bin/python AI-internal/useful-scripts/build_claim_tree_md.py` (or `/hierarchical-report`). If the tree has changed since that commit, rebuild rather than trust this copy; never hand-edit.
