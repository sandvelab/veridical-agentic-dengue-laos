[overview](../../../../../../README.md) / [analysis](../../../../../README.md) / [03_models](../../../../README.md) / [03_candidate](../../../README.md) / [a_hierNB](../../README.md) / [01_observation](../README.md) / **c_hurdle**

# c_hurdle

*On a path not taken — an alternative the reported analysis did not use. It is complete and runnable, and the stability analysis ran it.*

**Claim:** Two processes rather than one distribution: whether a province-month reports any cases at all is a logistic model, and how many it reports given that it reports any is a count model fitted only on the months that did. Reporting and magnitude are then allowed to depend on the season and the climate differently.

**Result:**

**The main path from batch 9.** Around the batch-8 configuration it took the candidate
     from 26.100 to **23.985** mean CRPS, past both required baselines, which is the largest
     single fork effect the project has measured. From the promoted configuration the same
     child is worth **0.601**. The two regimes it separates are far apart: 32.3 cases over all
     observed months against **73.9** over the months that reported anything.

## Material

The node's own files: [`claim.md`](../../../../../../../../analysis/03_models/03_candidate/a_hierNB/01_observation/c_hurdle/claim.md) · [`results/`](../../../../../../../../analysis/03_models/03_candidate/a_hierNB/01_observation/c_hurdle/results) · [`scripts/`](../../../../../../../../analysis/03_models/03_candidate/a_hierNB/01_observation/c_hurdle/scripts) · [`provenance/`](../../../../../../../../analysis/03_models/03_candidate/a_hierNB/01_observation/c_hurdle/provenance) · [`results/main/`](../../../../../../../../analysis/03_models/03_candidate/a_hierNB/01_observation/c_hurdle/results/main) · [`run.sh`](../../../../../../../../analysis/03_models/03_candidate/a_hierNB/01_observation/c_hurdle/run.sh).

---

> **A snapshot, generated 2026-09-27 from the tree at commit `3d89200`.** Everything here is derived from files the repository versions and regenerates in seconds with `.venv/bin/python AI-internal/useful-scripts/build_claim_tree_md.py` (or `/hierarchical-report`). If the tree has changed since that commit, rebuild rather than trust this copy; never hand-edit.
