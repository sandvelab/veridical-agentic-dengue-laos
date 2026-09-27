[overview](../../../../../README.md) / [analysis](../../../../README.md) / [03_models](../../../README.md) / [03_candidate](../../README.md) / [b_boosted](../README.md) / **01_features**

# 01_features

*On a path not taken — an alternative the reported analysis did not use. It is complete and runnable, and the stability analysis ran it.*

**Claim:** Which features does the booster see? Trees cannot extrapolate a trend or interpolate a cycle, so what a boosted model knows about time and place is exactly what the feature matrix says, and this is the choice of how much to say.

**Result:**

**The fork does not move the model.** The lag block alone scores **20.771** and the rich
calendar **20.375**, a difference of 0.396 CRPS — inside the 0.565 floor the reference's own
re-runs occupy, so by the rule batch 9 fixed the main path stays at `a_lagBlock`
(`AI-generated/candidate-forks/boosted_round1/fork_leaderboard.csv`).

**What the richer set buys is not accuracy but width.** Its point forecast is worse — MAE
28.251 against 26.953 — and its intervals are wider: 10–90 coverage 0.857 against 0.825,
further from nominal on the over-covering side. A boosted model given the province as an
identifier and a year index fits the training years more closely and forecasts a period it
cannot extrapolate into with correspondingly less confidence, which is what the two
numbers together say.

**So the twelve-month lag was enough.** `a_lagBlock` has no month, no year and no province
identifier, and describing all three explicitly moved the score by less than the evaluation
can resolve. On this dataset a tree given last year's count in the same province has
already been told what the calendar would tell it.

## Alternatives

Competing ways of answering this node's claim. The reported analysis takes the **main path**; the others are run by `05_stability`.

- [a_lagBlock](a_lagBlock/README.md) — **main path**  
  A block of lags and nothing else: the climate columns at the lags a three-month forecast can see, the province's own recent counts at the lags it can see, and the …
- [b_richCalendar](b_richCalendar/README.md) — *not taken*  
  The same lag block, plus what the calendar and the map say directly: the month as a pair of harmonics, a year index, the province as an identifier, and rolling summaries …

## Material

The node's own files: [`claim.md`](../../../../../../../analysis/03_models/03_candidate/b_boosted/01_features/claim.md) · [`run.sh`](../../../../../../../analysis/03_models/03_candidate/b_boosted/01_features/run.sh).

---

> **A snapshot, generated 2026-09-27 from the tree at commit `3d89200`.** Everything here is derived from files the repository versions and regenerates in seconds with `.venv/bin/python AI-internal/useful-scripts/build_claim_tree_md.py` (or `/hierarchical-report`). If the tree has changed since that commit, rebuild rather than trust this copy; never hand-edit.
