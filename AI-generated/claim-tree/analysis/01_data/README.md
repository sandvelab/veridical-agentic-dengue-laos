[overview](../../README.md) / [analysis](../README.md) / **01_data**

# 01_data

**Claim:** What does the Lao admin-1 monthly dengue dataset contain, and on what part of it may development happen? The node separates the held-out final year from the development period before anything characterises the data, then describes the development period only. It also holds the two sibling datasets the external check runs on, because between them its children are the only nodes licensed to read anything under `Archive/`.

**Result:**

The held-out year is separated before anything looks at the data, and the separation is
verified rather than asserted; the development period is then described on its own. The
answers are at the two children — `01_partition` for the partition, the schema
reconciliation and the Chap ingest; `02_characterise` for what the development period
contains and for the backtest scheme, which is fixed here and does not move again.

**The data problems this node found, each a candidate fork for phase D**, are listed in the
batch-3 report `AI-generated/batch-reports/26-08-23_b03_dataCharacterisation.md` §6. The
three that change what the headline number means are: one province absent from the metric
entirely and a second contributing nothing; a static population figure that makes any rate
wrong by a decade of growth; and an unweighted mean over provinces whose burdens differ by
four orders of magnitude.

**`03_siblings` was added in batch 20**, for the external check. It cuts the Thai and
Vietnamese files onto the Lao calendar in the same two arrangements — the development
backtest and the final year — and establishes that the two fixed schemes land on the same
months there. Two of the three statements this node found not to describe the Lao file turn
out to describe none of the three, so they are the harmonisation's rather than Laos's.

## Claims resting on this node

- **[C33](../../claims.md#c33)** — Three statements in the dataset's own schema do not describe the file it ships with. The schema states 2 575 rows where the file carries 2 808 -- the stated figure is the count of rows whose target is not null. It declares rainfall as a monthly total in millimetres, which would put a province's whole year at a few tens of millimetres; read as a mean daily rate the same column puts the year in the thousands, a factor of 30.4 apart, and the second reading is the one the file supports. And the population column, declared against a 2020 reference, sums to 4.96 million where the national total that year was 7.35 million, matching the country around 1995.

## Sub-analyses

- [01_partition](01_partition/README.md) · 1 claim  
  Does the archived source file partition exactly into a development period (1998-01 to 2009-12) and a held-out year (2010), and is each part well-formed? This is the only …
- [02_characterise](02_characterise/README.md) · 3 claims  
  What is in the development period: how complete is it per province and per year, how are dengue counts distributed, what seasonality do they show, and how do the climate …
- [03_siblings](03_siblings/README.md) · 1 claim  
  What do the two sibling harmonised datasets — Thailand and Vietnam — contain, and on what arrangement of them can the reported model be checked so that the comparison …

## Material

The node's own files: [`claim.md`](../../../../analysis/01_data/claim.md) · [`run.sh`](../../../../analysis/01_data/run.sh).

---

> **A snapshot, generated 2026-09-27 from the tree at commit `3d89200`.** Everything here is derived from files the repository versions and regenerates in seconds with `.venv/bin/python AI-internal/useful-scripts/build_claim_tree_md.py` (or `/hierarchical-report`). If the tree has changed since that commit, rebuild rather than trust this copy; never hand-edit.
