[overview](../../../../../../README.md) / [analysis](../../../../../README.md) / [03_models](../../../../README.md) / [03_candidate](../../../README.md) / [a_hierNB](../../README.md) / [06_yearVariance](../README.md) / **a_shared**

# a_shared

*On a path not taken — an alternative the reported analysis did not use. It is complete and runnable, and the stability analysis ran it.*

**Claim:** One province-year variance for the whole country, estimated by pooling every province's annual effects. Every province's forecast is then equally wide in relative terms.

**Result:**

**23.749** mean CRPS, **0.051** from the promoted main path -- so from where the model
     now stands, one shared annual variance and seventeen separate ones are indistinguishable.
     Around the batch-8 configuration the same fork was worth 1.870. It is also the only
     combination in the second sweep whose fit **converged**, in 48 rounds against the
     200-round cap every province-scaled fit reaches.

## Material

The node's own files: [`claim.md`](../../../../../../../../analysis/03_models/03_candidate/a_hierNB/06_yearVariance/a_shared/claim.md) · [`results/`](../../../../../../../../analysis/03_models/03_candidate/a_hierNB/06_yearVariance/a_shared/results) · [`scripts/`](../../../../../../../../analysis/03_models/03_candidate/a_hierNB/06_yearVariance/a_shared/scripts) · [`provenance/`](../../../../../../../../analysis/03_models/03_candidate/a_hierNB/06_yearVariance/a_shared/provenance) · [`run.sh`](../../../../../../../../analysis/03_models/03_candidate/a_hierNB/06_yearVariance/a_shared/run.sh).

---

> **A snapshot, generated 2026-09-27 from the tree at commit `3d89200`.** Everything here is derived from files the repository versions and regenerates in seconds with `.venv/bin/python AI-internal/useful-scripts/build_claim_tree_md.py` (or `/hierarchical-report`). If the tree has changed since that commit, rebuild rather than trust this copy; never hand-edit.
