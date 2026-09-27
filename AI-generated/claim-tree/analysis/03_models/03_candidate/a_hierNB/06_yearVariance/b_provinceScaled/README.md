[overview](../../../../../../README.md) / [analysis](../../../../../README.md) / [03_models](../../../../README.md) / [03_candidate](../../../README.md) / [a_hierNB](../../README.md) / [06_yearVariance](../README.md) / **b_provinceScaled**

# b_provinceScaled

*On a path not taken — an alternative the reported analysis did not use. It is complete and runnable, and the stability analysis ran it.*

**Claim:** One province-year variance per province, estimated from that province's own annual effects, so a province whose epidemic years swing hard gets a wider forecast than one whose record is flat.

**Result:**

**The main path from batch 9.** Around the batch-8 configuration it was worth **1.870**
     CRPS and lifted Vientiane Capital's 10–90 coverage off 1.000; from the promoted
     configuration it is worth **0.051**. The fitted variances differ by far more than
     sampling -- 2.33 in Xaisomboun against 0.12 in Oudomxay -- and Salavan's coverage stays at
     **0.12**, so the too-narrow half of batch 8's width defect is untouched.

## Material

The node's own files: [`claim.md`](../../../../../../../../analysis/03_models/03_candidate/a_hierNB/06_yearVariance/b_provinceScaled/claim.md) · [`results/`](../../../../../../../../analysis/03_models/03_candidate/a_hierNB/06_yearVariance/b_provinceScaled/results) · [`scripts/`](../../../../../../../../analysis/03_models/03_candidate/a_hierNB/06_yearVariance/b_provinceScaled/scripts) · [`provenance/`](../../../../../../../../analysis/03_models/03_candidate/a_hierNB/06_yearVariance/b_provinceScaled/provenance) · [`results/main/`](../../../../../../../../analysis/03_models/03_candidate/a_hierNB/06_yearVariance/b_provinceScaled/results/main) · [`run.sh`](../../../../../../../../analysis/03_models/03_candidate/a_hierNB/06_yearVariance/b_provinceScaled/run.sh).

---

> **A snapshot, generated 2026-09-27 from the tree at commit `3d89200`.** Everything here is derived from files the repository versions and regenerates in seconds with `.venv/bin/python AI-internal/useful-scripts/build_claim_tree_md.py` (or `/hierarchical-report`). If the tree has changed since that commit, rebuild rather than trust this copy; never hand-edit.
