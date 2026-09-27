[overview](../../../README.md) / [analysis](../../README.md) / [02_setup](../README.md) / **01_population**

# 01_population

**Claim:** How should the static population figure enter the analysis dataset? The file carries one population number per province for the whole 1998-2010 record, which is wrong by a decade of growth at both ends.

**Result:**

**The sibling is built and run.** Back-casting the snapshot to a per-year series with the archived national population series moves the conclusion from +0.1485 to **+0.1347**, and establishes that the archived column does not have the level its schema claims: it sums to 4.96 million against a 2020 national total of 7.35 million, matching the country's population around **1995**. See `b_backCast/claim.md`.

The population column is **constant within every province** across the whole development
period — verified in `a_static/results/main/setup_spec.json` rather than assumed, since it
is the premise the fork rests on. The main path takes it unchanged. The sibling that
back-casts a per-year series is not built yet.

## Alternatives

Competing ways of answering this node's claim. The reported analysis takes the **main path**; the others are run by `05_stability`.

- [a_static](a_static/README.md) — **main path**  
  Take the archived population column unchanged: one constant per province across the period, as the source file supplies it.
- [b_backCast](b_backCast/README.md) — *not taken*  
  Replace the single population snapshot with a per-province, per-year series back-cast from it, so the figure a model divides by is roughly right at both ends of the …

## Material

The node's own files: [`claim.md`](../../../../../analysis/02_setup/01_population/claim.md) · [`run.sh`](../../../../../analysis/02_setup/01_population/run.sh).

---

> **A snapshot, generated 2026-09-27 from the tree at commit `3d89200`.** Everything here is derived from files the repository versions and regenerates in seconds with `.venv/bin/python AI-internal/useful-scripts/build_claim_tree_md.py` (or `/hierarchical-report`). If the tree has changed since that commit, rebuild rather than trust this copy; never hand-edit.
