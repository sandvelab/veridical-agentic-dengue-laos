[overview](../../../../README.md) / [analysis](../../../README.md) / [02_setup](../../README.md) / [03_provinces](../README.md) / **b_reportingOnly**

# b_reportingOnly

*On a path not taken — an alternative the reported analysis did not use. It is complete and runnable, and the stability analysis ran it.*

**Claim:** Remove the two provinces that cannot be evaluated before the dataset reaches the platform, so they are absent from training as well as from scoring. Vientiane province never reports and Xaisomboun stops in 2005; the main path leaves both in the training frame and lets the platform drop them later.

**Result:**

**LA-VI and LA-XN are removed**, leaving 16 provinces and 2 304 rows, and the same **371** evaluable cells (`results/provinces_reportingOnly/setup_spec.json`). The pair is derived from the rule — no non-missing `disease_cases` inside the evaluated span — rather than named, so a province that went silent for another reason would be caught by the rule instead of missed by a constant.

**The skill score rises to +0.1861, and almost none of that is us.** Our pool moves 18.817 to 18.843; the reference moves 22.098 to **23.150**. Taking two unevaluable provinces out of the training frame costs the reference more than a standard error and costs us nothing measurable — presumably because it pools across provinces while fitting. This is the clearest case in tier 1 of a setup choice moving *the comparison* rather than either model, and it is invisible in a headline that reports only our own score.

## Material

The node's own files: [`claim.md`](../../../../../../analysis/02_setup/03_provinces/b_reportingOnly/claim.md) · [`results/`](../../../../../../analysis/02_setup/03_provinces/b_reportingOnly/results) · [`scripts/`](../../../../../../analysis/02_setup/03_provinces/b_reportingOnly/scripts) · [`provenance/`](../../../../../../analysis/02_setup/03_provinces/b_reportingOnly/provenance) · [`run.sh`](../../../../../../analysis/02_setup/03_provinces/b_reportingOnly/run.sh).

---

> **A snapshot, generated 2026-09-27 from the tree at commit `3d89200`.** Everything here is derived from files the repository versions and regenerates in seconds with `.venv/bin/python AI-internal/useful-scripts/build_claim_tree_md.py` (or `/hierarchical-report`). If the tree has changed since that commit, rebuild rather than trust this copy; never hand-edit.
