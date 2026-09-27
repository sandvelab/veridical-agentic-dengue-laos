[overview](../../../../../README.md) / [analysis](../../../../README.md) / [03_models](../../../README.md) / [03_candidate](../../README.md) / [a_hierNB](../README.md) / **05_autoregressive**

# 05_autoregressive

*On a path not taken — an alternative the reported analysis did not use. It is complete and runnable, and the stability analysis ran it.*

**Claim:** Does the model see the recent case history, or only the calendar and the weather? A seasonal regression forecasts the average year; the last observed count is what would tell it whether this year is one of the bad ones.

**Result:**

**The recent case history carries nothing this model can use.** `b_lag3` scores **23.345**
against the main path's 23.698, a gain of 0.353 that is inside the 0.57 CRPS floor; around
the batch-8 configuration the same child was worth **−0.075**. Neither number is
attributable.

**The premise says why, and it was computed before the child was run.** Within a province,
log1p counts correlate **0.701** at three months' lag and **0.758** at twelve. Three months
is the shortest lag one model can use at all three of Chap's forecast horizons, and at that
distance the lagged count is mostly telling the model what month of the year it is --
which the seasonal harmonics already say. Batch 7's finding that a persistence baseline is
level with the reference at *one* month's lead does not survive the trip to three.

The node's other purpose is served whatever it scored: the term batch 8 declined to add is
now a child with a claim, a premise and a number, rather than a paragraph in a report.

## Alternatives

Competing ways of answering this node's claim. The reported analysis takes the **main path**; the others are run by `05_stability`.

- [a_none](a_none/README.md) — **main path**  
  No autoregressive term. The forecast for a province-month is built from the calendar, the climate and the province's own level and annual effect, and nothing about how …
- [b_lag3](b_lag3/README.md) — *not taken*  
  The count three months back enters the linear predictor as standardised log1p. Three is the shortest lag one model can use at all three of Chap's forecast horizons, so …

## Material

The node's own files: [`claim.md`](../../../../../../../analysis/03_models/03_candidate/a_hierNB/05_autoregressive/claim.md) · [`run.sh`](../../../../../../../analysis/03_models/03_candidate/a_hierNB/05_autoregressive/run.sh).

---

> **A snapshot, generated 2026-09-27 from the tree at commit `3d89200`.** Everything here is derived from files the repository versions and regenerates in seconds with `.venv/bin/python AI-internal/useful-scripts/build_claim_tree_md.py` (or `/hierarchical-report`). If the tree has changed since that commit, rebuild rather than trust this copy; never hand-edit.
