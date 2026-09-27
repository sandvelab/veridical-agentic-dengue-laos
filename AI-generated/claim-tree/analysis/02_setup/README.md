[overview](../../README.md) / [analysis](../README.md) / **02_setup**

# 02_setup

**Claim:** What dataset and evaluation setting do all models — ours, the baselines and the reference — face in common? Everything decided here moves every model together, so a choice taken differently re-scores the whole comparison rather than one side of it.

**Result:**

Every model in the project — the two baselines and the external reference — is evaluated on
**one dataset of 2 592 rows over 18 provinces, 1998-01 to 2009-12**, at
`n_periods 3, n_splits 8, stride 3, n_retrain 1`. The dataset is
`results/main/analysis_dataset.csv` and the flags are in `results/main/setup_spec.json`,
which also records where each flag came from: the first three from batch 3's stored scheme
file, the fourth from the fork that decides it.

On the main path all four choices are the identity on the data, and that is checked rather
than claimed: `identical_to_development_file` is **true**, so the file every model faces is
the archived development file byte for byte. It will not be true off the main path, and then
the field says so.

The four choices are `a_static` (population as the archive supplies it), `a_from1998` (the
whole development period), `a_chapFilter` (province inclusion left to the platform) and
`a_once` (one fit per backtest). Each is a fork whose siblings are built when the stability
manifest needs them; each of those siblings re-scores **every** model, which is a property
of where the node sits rather than a rule anyone has to remember.

## Sub-analyses

- [01_population](01_population/README.md)  
  How should the static population figure enter the analysis dataset? The file carries one population number per province for the whole 1998-2010 record, which is wrong by …
- [02_trainingWindow](02_trainingWindow/README.md)  
  How much of the record should models be allowed to learn from, given that the share of zero-valued months falls monotonically across the period and the early years may …
- [03_provinces](03_provinces/README.md) · 1 claim  
  Which provinces belong in the analysis at all? One province reports nothing across the whole record and a second stops reporting partway through, and what the headline …
- [04_retrain](04_retrain/README.md)  
  How often is a model refitted across the backtest? Chap's n-retrain governs whether one fit serves all splits or each split gets its own.

## Material

The node's own files: [`claim.md`](../../../../analysis/02_setup/claim.md) · [`results/`](../../../../analysis/02_setup/results) · [`scripts/`](../../../../analysis/02_setup/scripts) · [`provenance/`](../../../../analysis/02_setup/provenance) · [`results/main/`](../../../../analysis/02_setup/results/main) · [`run.sh`](../../../../analysis/02_setup/run.sh).

---

> **A snapshot, generated 2026-09-27 from the tree at commit `3d89200`.** Everything here is derived from files the repository versions and regenerates in seconds with `.venv/bin/python AI-internal/useful-scripts/build_claim_tree_md.py` (or `/hierarchical-report`). If the tree has changed since that commit, rebuild rather than trust this copy; never hand-edit.
