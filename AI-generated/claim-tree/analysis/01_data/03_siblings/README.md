[overview](../../../README.md) / [analysis](../../README.md) / [01_data](../README.md) / **03_siblings**

# 03_siblings

**Claim:** What do the two sibling harmonised datasets — Thailand and Vietnam — contain, and on what
arrangement of them can the reported model be checked so that the comparison with Laos is
about the country rather than about the years?
The plan's §4 names `tha` and `vnm` as an external check and nothing more: no model is
developed on them, so nothing here is sealed and neither file is a holdout. What this node
has to settle is the arrangement, because an external check run on a different span would
confound the country with the calendar, and then it would answer neither question.

**Result:**

**The mirror is exact on all three countries.** Applied to the sibling files, the two Lao
schemes evaluate **2008-01 to 2009-12** and **exactly 2010**, from training sets ending
2007-12 and 2009-12 — the same months Laos is scored on, checked against chap-core's own
splitter rather than against the formula in its docstring. Thailand contributes 76 of its
77 provinces (its filter drops TH-38, which never reports) over 1 824 and 912 cells;
Vietnam contributes all 63 over 1 512 and 756. Laos contributes 16 over 371 and 192.
→ `results/backtest_scheme_external.json`, `split_schedule_external.csv`

**Two of the three things the Lao schema got wrong are the harmonisation's and not the Lao
file's.** `rainfall`, declared in all three schemas as a monthly total in millimetres, is a
mean daily rate in all three: summing the monthly values over a year gives 23–107 mm, and
multiplying by the days in a month puts the same years at roughly 1 500–2 000 mm. And
`row_count` does not mean the same thing in the three files — Vietnam declares 9 612
against 9 828 rows and Laos 2 575 against 2 808, both counting rows with an observed
target, while Thailand declares 27 720, which is its row count exactly and 696 more than
its complete records.
→ `results/schema_reconciliation.json`

**The fork this project spent a node arguing over, the harmonisation answers differently
per country.** `02_setup/01_population` chose between the archived static population column
and a series back-cast from published growth. Thailand ships the second: all 77 provinces
carry annual WorldPop values interpolated between the 2000, 2010 and 2020 anchors. Vietnam
and Laos ship the first.
→ `results/schema_reconciliation.json`

## Claims resting on this node

- **[C46](../../../claims.md#c46)** — Two of the three statements this project found not to describe the Lao dataset describe none of the three files of that harmonisation, so they are the harmonisation's rather than Laos's. rainfall is declared in all three schemas as a monthly total in millimetres and is a mean daily rate in all three; and row_count means different things in different files -- Vietnam declares 9612 against 9828 rows and Laos 2575 against 2808, both counting rows with an observed target, while Thailand declares 27720, which is its row count exactly and 696 more than its complete records. Thailand's population column is also not a static snapshot: all 77 provinces carry an annual series, so the fork this project spent a node arguing over is one the harmonisation answers differently per country.

## Material

The node's own files: [`claim.md`](../../../../../analysis/01_data/03_siblings/claim.md) · [`results/`](../../../../../analysis/01_data/03_siblings/results) · [`scripts/`](../../../../../analysis/01_data/03_siblings/scripts) · [`provenance/`](../../../../../analysis/01_data/03_siblings/provenance) · [`run.sh`](../../../../../analysis/01_data/03_siblings/run.sh).

---

> **A snapshot, generated 2026-09-27 from the tree at commit `3d89200`.** Everything here is derived from files the repository versions and regenerates in seconds with `.venv/bin/python AI-internal/useful-scripts/build_claim_tree_md.py` (or `/hierarchical-report`). If the tree has changed since that commit, rebuild rather than trust this copy; never hand-edit.
