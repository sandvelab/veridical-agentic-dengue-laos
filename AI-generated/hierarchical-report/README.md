# hierarchical-report

The linked drill-down over the claim tree (Rule 8). **Generated — never hand-edit.**
**A snapshot: generated 2026-09-27 from the tree at commit 46c2745.**
It is committed so that it can be read without cloning, and it is derived entirely
from files the repository versions, so it regenerates from a clone in a few seconds:

    .venv/bin/python AI-internal/useful-scripts/build_hierarchical_report.py

(or `/hierarchical-report`). If the tree has changed since that commit, rebuild it
rather than trusting this copy. Open `index.html`.

- `index.html` — the reported conclusion, the way into the tree, and every scored
  combination.
- `analysis/**/index.html` — one page per node: its claim, answers, the claims from
  the collection that rest on it, its children with alternatives marked main-path or
  not taken, its results grouped by combination, its scripts, its provenance records
  and its `run.sh`.
- `detail/<combination>/` — the within-result levels: national mean, then province,
  then month, then the per-cell scores every mean above is an average of. 69 combination(s), 1387 pages.

Every number shown is displayed from the file the analysis wrote; nothing here
recomputes an aggregate, so the report cannot disagree with the analysis. Paths the
repository does not version — built virtual environments, `__pycache__`, chap-core's
per-split `work/` — are not listed, because they are not the analysis's material.

`provenance.md` is the exception to the no-hand-editing rule here: it is the record
of each build, appended to and never overwritten.
