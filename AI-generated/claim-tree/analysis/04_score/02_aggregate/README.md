[overview](../../../README.md) / [analysis](../../README.md) / [04_score](../README.md) / **02_aggregate**

# 02_aggregate

**Claim:** Over what weighting is the headline mean taken? The provinces differ in burden by four orders of magnitude, so an unweighted mean over cells and a mean weighted by population or by cases are three different summaries of the same per-cell file.

**Result:**

The headline figures under the unweighted mean, and the four resolutions beside it. The
per-province file is where the aggregate's weakness shows: mean CRPS per province spans four
orders of magnitude, from 0.01 in Phongsaly to 84 in Vientiane Capital, so the unweighted
mean over cells is very nearly a statement about the largest few provinces.

**Both siblings are built and run, and this is the fork the conclusion is most sensitive to.** Population weighting gives **+0.2288** and case weighting **+0.2320**, against the main path's +0.1485 — moves of about **+0.08 of skill**, where the five `02_setup` forks move it by at most 0.038. Re-weighting the same per-cell file, re-running no model, moves the headline four times as much as changing the dataset. They cost thirteen seconds each.

**Under case weighting persistence beats our pool** (86.598 against 88.484), and our pool's 10-90 coverage falls from 0.863 to 0.701 — over-dispersed on the quiet months that dominate the unweighted mean, under-dispersed on the outbreak months that dominate this one. Neither summary alone shows that.

**One known gap.** `03_compare` computes the paired difference, the clustered standard errors and the split-level comparison from the unweighted per-cell file. So under a weighted row, `conclusion.json` carries a re-weighted `skill_score` beside paired statistics that are still unweighted: the headline is weighted and the spread is not. Teaching `compare_models.py` to read `weights.csv`, including a weighted clustered standard error, is a change to shared code every combination runs, and it is recorded here and assigned to batch 14 rather than done quietly.

## Alternatives

Competing ways of answering this node's claim. The reported analysis takes the **main path**; the others are run by `05_stability`.

- [a_unweighted](a_unweighted/README.md) — **main path**  
  Take the plain unweighted mean over evaluable cells, which is what Chap's own evaluation reports and what the project's success criterion is defined against.
- [b_populationWeighted](b_populationWeighted/README.md) — *not taken*  
  Weight the headline mean by province population, so a cell counts in proportion to the people it describes. Provincial burdens differ by four orders of magnitude and the …
- [c_caseWeighted](c_caseWeighted/README.md) — *not taken*  
  Weight the headline mean by the cases actually observed in each cell, so the summary is dominated by the province-months where dengue was happening. A province reporting …

## Material

The node's own files: [`claim.md`](../../../../../analysis/04_score/02_aggregate/claim.md) · [`run.sh`](../../../../../analysis/04_score/02_aggregate/run.sh).

---

> **A snapshot, generated 2026-09-27 from the tree at commit `3d89200`.** Everything here is derived from files the repository versions and regenerates in seconds with `.venv/bin/python AI-internal/useful-scripts/build_claim_tree_md.py` (or `/hierarchical-report`). If the tree has changed since that commit, rebuild rather than trust this copy; never hand-edit.
