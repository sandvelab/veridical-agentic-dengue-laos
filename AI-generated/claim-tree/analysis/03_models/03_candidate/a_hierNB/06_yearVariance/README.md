[overview](../../../../../README.md) / [analysis](../../../../README.md) / [03_models](../../../README.md) / [03_candidate](../../README.md) / [a_hierNB](../README.md) / **06_yearVariance**

# 06_yearVariance

*On a path not taken — an alternative the reported analysis did not use. It is complete and runnable, and the stability analysis ran it.*

**Claim:** Is the year-to-year variability of dengue the same relative size in every province? The province-year effect's variance sets how wide every forecast is, and one number shared across provinces is a constant multiplicative width for burdens that differ by four orders of magnitude.

**Result:**

**Half of batch 8's width diagnosis was right, and the half that was right is nearly
redundant with the observation model.**

Around the batch-8 configuration, estimating one annual variance per province instead of
one shared by all was worth **1.870** CRPS, the second-largest effect in the sweep, and it
lifted Vientiane Capital's 10–90 coverage off **1.000** -- the interval that had covered
every outcome, and the province batch 8 named. It is the main path from batch 9.

It did **not** repair the other side. Salavan's 10–90 coverage was 0.125 under batch 8 and
is **0.12** on the promoted main path: a per-province variance widens a province whose
annual variance is genuinely large, and does nothing for one whose epidemic years are
sharper than any log-scale variance can represent.

And measured from the promoted main path, reverting to a shared variance costs **0.051**
CRPS (`round2_promoted/fork_interaction.csv`) -- the hurdle had already fixed most of what
the per-province variance was promoted to fix.

**The fitted variances differ by far more than sampling**: 2.33 in Xaisomboun against 0.12
in Oudomxay. **They also stop the fit converging**: every combination carrying this child
runs to the 200-round cap where the shared-variance sibling converges in 48, because the
convergence test is a maximum over seventeen relative movements and the smallest variances
keep it above tolerance long after the parameters have settled.

## Alternatives

Competing ways of answering this node's claim. The reported analysis takes the **main path**; the others are run by `05_stability`.

- [a_shared](a_shared/README.md) — *not taken*  
  One province-year variance for the whole country, estimated by pooling every province's annual effects. Every province's forecast is then equally wide in relative terms.
- [b_provinceScaled](b_provinceScaled/README.md) — **main path**  
  One province-year variance per province, estimated from that province's own annual effects, so a province whose epidemic years swing hard gets a wider forecast than one …

## Material

The node's own files: [`claim.md`](../../../../../../../analysis/03_models/03_candidate/a_hierNB/06_yearVariance/claim.md) · [`run.sh`](../../../../../../../analysis/03_models/03_candidate/a_hierNB/06_yearVariance/run.sh).

---

> **A snapshot, generated 2026-09-27 from the tree at commit `3d89200`.** Everything here is derived from files the repository versions and regenerates in seconds with `.venv/bin/python AI-internal/useful-scripts/build_claim_tree_md.py` (or `/hierarchical-report`). If the tree has changed since that commit, rebuild rather than trust this copy; never hand-edit.
