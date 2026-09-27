[overview](../../../README.md) / [analysis](../../README.md) / [02_setup](../README.md) / **03_provinces**

# 03_provinces

**Claim:** Which provinces belong in the analysis at all? One province reports nothing across the whole record and a second stops reporting partway through, and what the headline mean is a mean over depends on the answer.

**Result:**

**Both siblings are built and run, and both raise the skill score by moving the reference rather than us.** Removing the two unevaluable provinces before the platform sees them gives **+0.1861**; merging Vientiane province into the capital gives **+0.1714**; the main path gives +0.1485. In both, our pool moves by less than 0.2 CRPS and the reference moves by 0.8 to 1.1. Neither changes the number of evaluated cells, which answers batch 12's question about whether `c_mergeVientiane` could be scored at all. See the two children's `claim.md`.

18 provinces go to the platform; **16 contribute 371 evaluable cells**. One province
(LA-VI, Vientiane) never reports and the platform's region filter drops it; one (LA-XN,
Xaisomboun) survives the filter and has no observation inside the evaluated span, so it
contributes nothing. The figure is recomputed here from the dataset and the stored scheme
(`a_chapFilter/results/main/setup_spec.json`) and agrees with batch 3's and with what the
evaluation produced.

Unlike the other three forks, this one's siblings change *what is evaluated*, so raw CRPS is
not comparable across them. That is survivable only because the project's reported
conclusion is a ratio to the reference computed on whatever cell set the child produced.

## Claims resting on this node

- **[C18](../../../claims.md#c18)** — The analysis the development set ranked highest among those that change the data or the models is twenty-ninth of thirty-two on the held-out year, and the fork behind it moved the reference model rather than ours. Removing the two provinces that contribute no evaluable cell before the platform sees them takes the reported skill from +0.1485 to +0.1861 on development and to -0.1828 on 2010; across that change our pool moves from 76.73 to 76.56 mean CRPS, inside the noise, while the reference model moves from 84.03 to 64.72.

## Alternatives

Competing ways of answering this node's claim. The reported analysis takes the **main path**; the others are run by `05_stability`.

- [a_chapFilter](a_chapFilter/README.md) — **main path**  
  Leave inclusion to chap-core's own region filter: pass every province in the file and let the platform drop what it will not model.
- [b_reportingOnly](b_reportingOnly/README.md) — *not taken*  
  Remove the two provinces that cannot be evaluated before the dataset reaches the platform, so they are absent from training as well as from scoring. Vientiane province …
- [c_mergeVientiane](c_mergeVientiane/README.md) — *not taken*  
  Aggregate Vientiane province into Vientiane Capital, which lies geographically inside it, so the province that never reports is not a hole in the map but part of its …

## Material

The node's own files: [`claim.md`](../../../../../analysis/02_setup/03_provinces/claim.md) · [`run.sh`](../../../../../analysis/02_setup/03_provinces/run.sh).

---

> **A snapshot, generated 2026-09-27 from the tree at commit `3d89200`.** Everything here is derived from files the repository versions and regenerates in seconds with `.venv/bin/python AI-internal/useful-scripts/build_claim_tree_md.py` (or `/hierarchical-report`). If the tree has changed since that commit, rebuild rather than trust this copy; never hand-edit.
