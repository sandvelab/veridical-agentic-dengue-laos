[overview](../../../README.md) / [analysis](../../README.md) / [02_setup](../README.md) / **02_trainingWindow**

# 02_trainingWindow

**Claim:** How much of the record should models be allowed to learn from, given that the share of zero-valued months falls monotonically across the period and the early years may describe a different reporting regime?

**Result:**

**The sibling is built and run.** Starting at 2004-01, the calendar midpoint, discards half the record and costs **0.0219 of skill** (+0.1266 against the main path's +0.1485) while leaving the 371 evaluated cells identical — the comparability the paragraph below predicts, checked by the sibling rather than assumed. See `b_from2004/claim.md`.

All 2 592 rows reach the models: no year is discarded on the main path. Because chap-core
lays its splits out backwards from the last period of the file, a sibling that truncates the
early years would change what the models learn from and leave the 371 evaluated cells
identical — which is what makes this fork's children directly comparable.

## Alternatives

Competing ways of answering this node's claim. The reported analysis takes the **main path**; the others are run by `05_stability`.

- [a_from1998](a_from1998/README.md) — **main path**  
  Use the whole development period, 1998-01 to 2009-12, as the record models learn from.
- [b_from2004](b_from2004/README.md) — *not taken*  
  Let models learn only from the second half of the development record, 2004-01 onward. The share of zero-valued months falls monotonically across the period, so the early …

## Material

The node's own files: [`claim.md`](../../../../../analysis/02_setup/02_trainingWindow/claim.md) · [`run.sh`](../../../../../analysis/02_setup/02_trainingWindow/run.sh).

---

> **A snapshot, generated 2026-09-27 from the tree at commit `3d89200`.** Everything here is derived from files the repository versions and regenerates in seconds with `.venv/bin/python AI-internal/useful-scripts/build_claim_tree_md.py` (or `/hierarchical-report`). If the tree has changed since that commit, rebuild rather than trust this copy; never hand-edit.
