[overview](../../../README.md) / [analysis](../../README.md) / [01_data](../README.md) / **01_partition**

# 01_partition

**Claim:** Does the archived source file partition exactly into a development period (1998-01 to 2009-12) and a held-out year (2010), and is each part well-formed? This is the only node in the project that reads the full file.

**Result:**

**The partition is exact.** The archived file's 2 808 data rows go to 2 592 development
(1998-01 to 2009-12) and 216 holdout (2010), with no line in both, the sorted union
byte-identical to the sorted source, and each part an order-preserving subsequence of it.
The file is ordered by province and then by month, so the two parts do not concatenate back
into it; content and ordering are checked separately for that reason.
→ `results/partition_check.json`

**The source is a complete rectangular panel**: 18 provinces × 156 months, no missing
months, no duplicate primary keys. Every column is fully populated except `disease_cases`,
which is absent in 233 cells — 209 in development, 24 in the holdout.
→ `results/part_structure.csv`

**The schema's row count is a label error, not a stale figure.** `row_count: 2575` is the
number of rows carrying a non-missing `disease_cases`; the file has 2 808 rows. Both numbers
are right about different things, and the field counts complete records rather than rows.
→ `results/rowcount_reconciliation.json`

**No conversion is needed for `chap eval`.** The archived CSV is already in the form the
platform reads. chap-core's own loader takes both parts with every row, every province and
every missing target preserved, adding only a `parent` column.
→ `results/chap_ingest_check.json`

**The holdout is well-formed and sealed**: 216 rows, all 18 provinces, all 12 months of
2010, no duplicates, 24 cells without a dengue count. Where those 24 fall was not examined.

## Claims resting on this node

- **[C35](../../../claims.md#c35)** — The development file and the sealed holdout partition the archived source exactly, and this was verified rather than assumed: 2 592 and 216 lines against the source's 2 808, no line in both, and the sorted union byte-identical to the source under sha256. The check runs again on every run of the analysis, against the archive's own checksum manifest.

## Material

The node's own files: [`claim.md`](../../../../../analysis/01_data/01_partition/claim.md) · [`results/`](../../../../../analysis/01_data/01_partition/results) · [`scripts/`](../../../../../analysis/01_data/01_partition/scripts) · [`provenance/`](../../../../../analysis/01_data/01_partition/provenance) · [`run.sh`](../../../../../analysis/01_data/01_partition/run.sh).

---

> **A snapshot, generated 2026-09-27 from the tree at commit `3d89200`.** Everything here is derived from files the repository versions and regenerates in seconds with `.venv/bin/python AI-internal/useful-scripts/build_claim_tree_md.py` (or `/hierarchical-report`). If the tree has changed since that commit, rebuild rather than trust this copy; never hand-edit.
