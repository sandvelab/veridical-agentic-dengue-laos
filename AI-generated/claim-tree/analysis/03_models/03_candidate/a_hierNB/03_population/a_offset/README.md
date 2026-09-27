[overview](../../../../../../README.md) / [analysis](../../../../../README.md) / [03_models](../../../../README.md) / [03_candidate](../../../README.md) / [a_hierNB](../../README.md) / [03_population](../README.md) / **a_offset**

# a_offset

*On a path not taken — an alternative the reported analysis did not use. It is complete and runnable, and the stability analysis ran it.*

**Claim:** As a fixed offset, log population: the model forecasts an incidence rate and multiplies it back up by the province's size, so the fit never has to learn how large a province is.

**Result:**

The offset can be taken: population is positive in every province, and the largest is
**23.8 times** the smallest (`results/main/model_option_spec.json`). That ratio is also the
reason the choice matters — a model that had to learn each province's size from its counts
would spend a parameter per province on something the file already says.

## Material

The node's own files: [`claim.md`](../../../../../../../../analysis/03_models/03_candidate/a_hierNB/03_population/a_offset/claim.md) · [`results/`](../../../../../../../../analysis/03_models/03_candidate/a_hierNB/03_population/a_offset/results) · [`scripts/`](../../../../../../../../analysis/03_models/03_candidate/a_hierNB/03_population/a_offset/scripts) · [`provenance/`](../../../../../../../../analysis/03_models/03_candidate/a_hierNB/03_population/a_offset/provenance) · [`results/main/`](../../../../../../../../analysis/03_models/03_candidate/a_hierNB/03_population/a_offset/results/main) · [`run.sh`](../../../../../../../../analysis/03_models/03_candidate/a_hierNB/03_population/a_offset/run.sh).

---

> **A snapshot, generated 2026-09-27 from the tree at commit `3d89200`.** Everything here is derived from files the repository versions and regenerates in seconds with `.venv/bin/python AI-internal/useful-scripts/build_claim_tree_md.py` (or `/hierarchical-report`). If the tree has changed since that commit, rebuild rather than trust this copy; never hand-edit.
