[overview](../../../../README.md) / [analysis](../../../README.md) / [02_setup](../../README.md) / [01_population](../README.md) / **b_backCast**

# b_backCast

*On a path not taken — an alternative the reported analysis did not use. It is complete and runnable, and the stability analysis ran it.*

**Claim:** Replace the single population snapshot with a per-province, per-year series back-cast from it, so the figure a model divides by is roughly right at both ends of the record instead of only at the end. The snapshot is a 2020 measurement applied to 1998-2010, and a decade of growth is not uniform across provinces.

**Result:**

The snapshot becomes a per-year series: `population(province, year) = snapshot x N(year)/N(2020)`, scaled from **0.7144** in 1998 to **0.8496** in 2009 (`results/popColumn_backCast/setup_spec.json`). The conclusion moves from +0.1485 to **+0.1347** — the pool still beats the reference, by slightly less.

**The archived column does not have the level its schema claims.** It sums to **4 961 076** across the eighteen provinces; the national total at the schema's stated reference year of 2020 is **7 346 533**, and the year whose total is nearest the snapshot's is **1995**. This is the third statement in that schema found not to describe the file. The anchor is used as declared anyway, and the discrepancy recorded: changing the reference year multiplies every population by one constant, which a log offset absorbs, so what the fork actually probes is the shape of the trend.

The series is national, so every province is scaled by the same factor. The fork probes a trend, not a provincial differential, and `Archive/lao-population/provenance.md` records why the censuses that would give one are not here.

## Material

The node's own files: [`claim.md`](../../../../../../analysis/02_setup/01_population/b_backCast/claim.md) · [`results/`](../../../../../../analysis/02_setup/01_population/b_backCast/results) · [`scripts/`](../../../../../../analysis/02_setup/01_population/b_backCast/scripts) · [`provenance/`](../../../../../../analysis/02_setup/01_population/b_backCast/provenance) · [`run.sh`](../../../../../../analysis/02_setup/01_population/b_backCast/run.sh).

---

> **A snapshot, generated 2026-09-27 from the tree at commit `3d89200`.** Everything here is derived from files the repository versions and regenerates in seconds with `.venv/bin/python AI-internal/useful-scripts/build_claim_tree_md.py` (or `/hierarchical-report`). If the tree has changed since that commit, rebuild rather than trust this copy; never hand-edit.
