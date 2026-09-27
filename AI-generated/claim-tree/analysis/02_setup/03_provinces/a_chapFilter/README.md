[overview](../../../../README.md) / [analysis](../../../README.md) / [02_setup](../../README.md) / [03_provinces](../README.md) / **a_chapFilter**

# a_chapFilter

**Claim:** Leave inclusion to chap-core's own region filter: pass every province in the file and let the platform drop what it will not model.

**Result:**

18 provinces passed to the platform. LA-VI never reports; LA-XN has no observation inside the evaluated span 2008-01 to 2009-12. **16 provinces, 371 evaluable cells** (`results/main/setup_spec.json`), computed from this dataset and the stored scheme rather than carried from batch 3, and agreeing with it.

## Material

The node's own files: [`claim.md`](../../../../../../analysis/02_setup/03_provinces/a_chapFilter/claim.md) · [`results/`](../../../../../../analysis/02_setup/03_provinces/a_chapFilter/results) · [`scripts/`](../../../../../../analysis/02_setup/03_provinces/a_chapFilter/scripts) · [`provenance/`](../../../../../../analysis/02_setup/03_provinces/a_chapFilter/provenance) · [`results/main/`](../../../../../../analysis/02_setup/03_provinces/a_chapFilter/results/main) · [`run.sh`](../../../../../../analysis/02_setup/03_provinces/a_chapFilter/run.sh).

---

> **A snapshot, generated 2026-09-27 from the tree at commit `3d89200`.** Everything here is derived from files the repository versions and regenerates in seconds with `.venv/bin/python AI-internal/useful-scripts/build_claim_tree_md.py` (or `/hierarchical-report`). If the tree has changed since that commit, rebuild rather than trust this copy; never hand-edit.
