# Autonomously developed dengue forecasting for Laos, veridically

A spatio-temporal model forecasting monthly dengue case counts across the provinces of
Laos, developed by an agentic AI system as autonomously as the setup allows, and evaluated
by Chap's own cross-validated backtest — **together with the complete record of how it
came about**: every execution, environment, judgment call and rejected alternative, and how
far the conclusion survives the alternatives.

**The project is finished and this is its public release** (2026-09-07). The analysis has
run, the held-out year has been opened and scored, the external check on two further
countries has run, and the write-up is done. Everything below is browsable here on GitHub.

## The results — where to look

| To see | Open |
|---|---|
| **The write-up** — what was done, what it found, and where the setup was more trouble than it was worth | [`Human-AI-collaboration/manuscript/26-09-05_illustratingCase.md`](Human-AI-collaboration/manuscript/26-09-05_illustratingCase.md) |
| Which claim every passage of the write-up rests on | [its provenance sidecar](Human-AI-collaboration/manuscript/26-09-05_illustratingCase_sidecar.md) |
| **The claim graph** — every statement the analysis supports, each linked to the node and the result file that grounds it, with a map of claims by node | [`AI-generated/claim-tree/claims.md`](AI-generated/claim-tree/claims.md) |
| **The claim tree** — a diagram of the whole analysis, main path and paths not taken, one page per node giving its claim and its result | [`AI-generated/claim-tree/`](AI-generated/claim-tree/README.md) |
| How stable the conclusion is under the 32 reasonable analyses around it | [`05_stability`](AI-generated/claim-tree/analysis/05_stability/README.md) |
| The same model, unchanged, on Thailand and Vietnam | [`06_external`](AI-generated/claim-tree/analysis/06_external/README.md) |
| **What does not hold** — the reproducibility report, read its last section first | [`AI-generated/repro-report/26-09-05_reproducibilityReport.md`](AI-generated/repro-report/26-09-05_reproducibilityReport.md) |
| What was released, and the safety scan it passed | [`AI-generated/release/`](AI-generated/release/README.md) |

The claim collection the manuscript is written from is
[`Human-AI-collaboration/claims/claims.md`](Human-AI-collaboration/claims/claims.md); the
one under `AI-generated/claim-tree/` is the same collection with its links made clickable.
To descend a reported number to the per-cell scores it averages, clone the repository and
open `AI-generated/hierarchical-report/index.html` in a browser — it is committed, but
GitHub shows HTML as source rather than as a page. Both views are generated snapshots,
stamped with the date and commit they were built from.

### The headline, in brief

- **The reported model is a linear opinion pool** over two model families of our own and
  the two required baselines. Its skill against the reference model (WHO EWARS-csd, at its
  own defaults) is **+0.1485** on the development backtest — mean CRPS 18.817 against
  22.098 — and **+0.0868** on the held-out year 2010, beating both baselines on each
  ([`conclusion.json`](analysis/results/main/conclusion.json),
  [held out](analysis/results/main__holdout/conclusion.json)).
- **That number is one of a distribution.** Across 32 analyses fixed before any ran, skill
  spans −0.0724 to +0.2320 on development, where the reported one sits 13th, and −0.5038 to
  +0.2026 on 2010, where it sits 18th
  ([`distribution.json`](analysis/05_stability/results/distribution.json),
  [held out](analysis/05_stability/results/holdout_distribution.json)). The model family is
  what the conclusion is sensitive to; the choices inside a family mostly are not.
- **The development-to-final-year drop replicates** on Thailand and Vietnam
  ([`external_vs_laos.json`](analysis/06_external/results/external_vs_laos.json)).
- **None of it reaches statistical significance and none is claimed.** The reference model
  is unseeded, and its own re-run spread is reported beside every comparison that divides
  by it.

## What this repository is for

It carries out **one research project** and produces **one article** from it, with full
provenance. The article is the worked case for a manuscript updating *Ten Simple Rules for
Reproducible Computational Research* (Sandve et al., *PLoS Comput Biol* 2013) for the age of
agentic AI; the project also asks how far an agentic system gets on a real, representative
research problem, and where it fails. So the repository is itself the object of study: the
dengue model is the task, and **the record of how an agent produced it is the result**. A
model that scores well but whose development cannot be reconstructed would be a failed run.

An agent makes meticulous recording nearly free, but brings three new risks: it can carry a
number in its own context and leave a chain that reads as complete and is broken on disk; it
can search a large space of analyses quickly, which is where a proxy target and the real
objective come apart; and a standing instruction can be dropped silently late in a long
session. The repository's shape answers each of these structurally — the right thing is the
easy thing, and the wrong thing is detectable. [`MOTIVATION.md`](MOTIVATION.md) gives the
full argument.

## How veridicality is ensured

Reproducibility says what was done; veridicality asks whether the conclusion would survive a
differently-but-equally-reasonably conducted analysis.

- **The analysis is a tree of questions, not a pipeline of steps.** Each node in
  [`analysis/`](analysis/README.md) is an analytical aim. Where a judgment call was made, the
  alternatives are siblings — one on the main path, the rest kept in the tree, complete and
  runnable: 71 nodes, 17 forks, 23 paths not taken. `analysis/run.sh` still reproduces
  exactly the reported analysis.
- **The stability analysis is part of the tree.** `05_stability` runs every fork taken alone
  and eight pairs chosen by a rule fixed in advance — 32 analyses — and reports the
  conclusion as the distribution over them, with each fork's effect measured against the
  reference model's own re-run noise.
- **The final year was cut off before any work began and opened once.** 2010 was never read
  during development; the set of analyses run on it was frozen and committed first, and the
  driver refuses to re-run a held-out row.
- **An external check** re-runs the reported model, unchanged, on two countries it never saw.
- **Every judgment call is recorded with its agency** — `human-set`,
  `agent-on-human-assessment` or `agent-autonomous` — in the plan's decision log and the
  nodes' `claim.md`. How far the plan drifted during execution, and who drove each change,
  is a reported result in [`AI-generated/plan-drift/`](AI-generated/plan-drift/README.md).
- **Failures are kept**: models that lost, approaches abandoned and defects found stay in the
  record with what went wrong.

## How provenance and reproducibility are ensured

- **No number reaches a claim except through a file.** Every reported figure is read by a
  script from the files Chap wrote, never from terminal output, and every result carries a
  `provenance/` record naming the script, its digest, the inputs and the commit.
- **Text is downstream of claims, which are downstream of results.** Every sentence of the
  write-up maps to a claim in the collection, every claim to a result file, every result to
  the command that produced it.
- **The environment is pinned at three layers**: a declarative specification, an exact lock
  of 174 packages (CPython 3.13.0, `chap-core` 2.1.0), and a Docker image. The reference
  model is pinned by image digest, the data by source-repository commit and checksum.
- **Every stochastic step is seeded** from one project seed.
- **Verification instead of trust.** `/validate` runs eleven invariant checks on the record;
  a **clean-room** run rebuilt the environment from nothing and ran `analysis/run.sh` from a
  fresh checkout — every score from a model this project wrote came back identical, 207 of
  207 ([`26-09-05_cleanroom.md`](AI-generated/validation/26-09-05_cleanroom.md)); and an
  **outsider** check had a fresh agent follow the instructions cold
  ([`26-09-05_outsider.md`](AI-generated/validation/26-09-05_outsider.md)).
- **The instructions are part of the method** and are published with it: `AGENTS.md` and the
  skills in `.claude/commands/` determine how the analysis was produced.

The qualification travels with the claim: our models reproduce bit for bit, **the reference
model does not** — it is an unseeded container, so every figure dividing by it is a draw,
and the reports say which ones moved.

## What is in the repository

| Path | Holds |
|---|---|
| [`analysis/`](analysis/README.md) | The claim tree. `analysis/run.sh` reproduces the whole reported analysis, the distribution around it and the external check. |
| `environment/` | The one main environment; nodes override only where they must. |
| [`Human-AI-collaboration/claims/`](Human-AI-collaboration/claims/) | The claim collection — every statement bound to its result. |
| [`Human-AI-collaboration/manuscript/`](Human-AI-collaboration/manuscript/) | The write-up, written from the claims, with its provenance sidecar. |
| `Archive/` | Imported source material — the data, the source manuscript, the plan as delivered — never edited, marked `(IS_SHADOW)`. |
| [`AI-generated/`](AI-generated/README.md) | Derived documents: the claim-tree and hierarchical views, the reproducibility and release reports, validation runs, plan drift, one report per executed batch. |
| `AI-internal/` | The machinery: scripts, skill references, the task log. |
| [`Human-input/`](Human-input/) | The plan the agent executed, one batch per invocation, with its ledger and decision log. |
| `AGENTS.md`, `.claude/commands/` | The standing instructions and the skills — the method. |

[`readme-at-start.md`](readme-at-start.md) states the project in full — its fixed settings,
what must not happen, and the detailed state of every result — and is the first file an
agent reads. [`AGENTS.md`](AGENTS.md) says how work is done here.

## Reproducing this analysis

Two environments, and they are not interchangeable. `environment/chapenv/` runs the
analysis; `.venv/` runs the repository's own machinery. Neither is tracked, and both are
built from a specification that is.

```bash
# 1. the analysis environment — CPython 3.13.0 and chap-core 2.1.0, installed from
#    environment/lock.txt (174 packages, exact versions). Needs `uv` on PATH.
bash environment/install-chap.sh

# 2. run everything
bash analysis/run.sh

# 3. check the record is complete
python3 -m venv .venv          # the machinery interpreter, stdlib only
.venv/bin/python AI-internal/useful-scripts/check_invariants.py
```

`environment/environment.yml` is the **declarative** half — what was asked for — and is not
a conda file; `environment/lock.txt` is what actually reproduces, and `install-chap.sh`
installs from it and reports any difference between what it built and what that file says.
`environment/Dockerfile` freezes the same package set into an image.

**`analysis/run.sh` takes many hours from cold** — the clean-room run of 2026-09-05 took
14.9 — because it reproduces the reported result, the 32 analyses around it on the
development period and again on the held-out year, and the external check. Most of that time
is the reference model: an external container, unseeded, re-run four times per dataset
through an emulated amd64 image. **Docker must be running**; without it everything except
the reference model and the comparisons that divide by it will still run.

`/hierarchical-report` rebuilds the claim-tree and HTML views from the tree in a few seconds.

## Not yet done

A **citable, versioned snapshot with a persistent identifier** (e.g. a Zenodo DOI) — the one
step of the release that needs an account the agent does not have. Until it exists, cite
this repository and the commit you used.

## Licence

Two licences, because this repository is both a record and a program.

- **`LICENSE` — CC BY 4.0** covers the documents, data, records and prose: the root-level
  documents, `AI-generated/`, `Human-AI-collaboration/`, `Human-input/`, `Archive/`, and
  under `analysis/` every `claim.md`, every `provenance/` record and every `results/` file.
- **`LICENSE-CODE` — MIT** covers the scripts: `analysis/**/scripts/`, every `run.sh`,
  `AI-internal/useful-scripts/`, `.claude/` and `environment/`.

Material under `Archive/` also carries the terms it came with, stated per directory in each
`provenance.md`; where an upstream licence applies, it governs and nothing here narrows it.
Third-party code built into the Chap model contract directories carries its own licence.

Use either half and cite the work; both permit commercial use.
