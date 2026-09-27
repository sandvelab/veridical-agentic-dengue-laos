[overview](../../../../../../README.md) / [analysis](../../../../../README.md) / [03_models](../../../../README.md) / [03_candidate](../../../README.md) / [b_boosted](../../README.md) / [02_head](../README.md) / **b_quantileEnsemble**

# b_quantileEnsemble

*On a path not taken — an alternative the reported analysis did not use. It is complete and runnable, and the stability analysis ran it.*

**Claim:** A ladder of quantile boosters, each fitted to a different quantile of the same target, and the forecast drawn from the distribution they trace out. The width is learned per cell rather than derived from the level.

**Result:**

Fifteen boosters, 1 302 trees, and a lower half that does not exist
(`../../results/head_quantileEnsemble/head_premise_check.json`).

**Seven of the fifteen levels are flat at zero across the whole file** — the largest count
any of them returns anywhere is 0.3 — and the eighth, 0.50, is flat in Vientiane Capital,
where the observed median is 109 cases. Seven of those eight took a single boosting round
before their loss on the held-back months stopped improving, and 0.50 and 0.60 ran to the
400-round cap without settling. The registered prediction named eight levels; seven met the
test as stated and the eighth met it in the province the prediction was about.

The head scores **20.960** mean CRPS — 0.189 worse than the sibling, inside the floor — with
the project's closest interval coverage (0.798 against nominal 0.80) and its worst point
forecast (MAE 33.020). Fitting the ladder was also the most expensive thing in the batch at
75 seconds against 52.

**The ladder crossed on 1 408 of 2 012 training rows**, repaired by cumulative maximum
before anything was drawn, with a largest repair of 2.49 on the log1p scale
(`../../results/head_quantileEnsemble/fitted_model.json`). Fifteen boosters fitted without
reference to each other do not produce fifteen ordered quantiles, and the size of the
disagreement is recorded rather than only the fact of the repair.

## Material

The node's own files: [`claim.md`](../../../../../../../../analysis/03_models/03_candidate/b_boosted/02_head/b_quantileEnsemble/claim.md) · [`results/`](../../../../../../../../analysis/03_models/03_candidate/b_boosted/02_head/b_quantileEnsemble/results) · [`scripts/`](../../../../../../../../analysis/03_models/03_candidate/b_boosted/02_head/b_quantileEnsemble/scripts) · [`provenance/`](../../../../../../../../analysis/03_models/03_candidate/b_boosted/02_head/b_quantileEnsemble/provenance) · [`run.sh`](../../../../../../../../analysis/03_models/03_candidate/b_boosted/02_head/b_quantileEnsemble/run.sh).

---

> **A snapshot, generated 2026-09-27 from the tree at commit `3d89200`.** Everything here is derived from files the repository versions and regenerates in seconds with `.venv/bin/python AI-internal/useful-scripts/build_claim_tree_md.py` (or `/hierarchical-report`). If the tree has changed since that commit, rebuild rather than trust this copy; never hand-edit.
