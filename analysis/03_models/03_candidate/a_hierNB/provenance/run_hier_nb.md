# Provenance — candidate 1, the hierarchical negative-binomial GLM, evaluated

```
result:              results/main/eval.nc
                     results/main/eval.log
                     results/main/model_spec.json
                     results/main/run_cost.json
                     results/main/fitted_model.json
script:              scripts/run_hier_nb.py
                     sha256:f6f6a96aefe64e6dba05a5b3e7f9c98667f4935eb514bbc1824aed575e7b420b
                     analysis/03_models/scripts/lib/chap_eval.py
                     sha256:028835c823eacb999ea60125be3a871b2c4c58985538574d7afa8b61525df21a
                     the model itself, scripts/hier_nb_model/:
                     MLproject       sha256:aaa3bb10be0325fb…
                     hier_nb.py      sha256:94300ffe80f98789…
                     train.py        sha256:656dc6551056cc60…
                     predict.py      sha256:7b84349d2728a2a3…
                     uv.lock         sha256:a5a6840b752fc538…
                     (the full digests are in results/main/model_spec.json, written by
                     the run before it started)
invocation:          "$PYTHON" scripts/run_hier_nb.py
                     which issues
                     environment/chapenv/bin/chap eval
                       --model-name <node>/scripts/hier_nb_model
                       --dataset-csv analysis/02_setup/results/main/analysis_dataset.csv
                       --output-file results/main/eval.nc
                       --backtest-params.n-periods 3 --backtest-params.n-splits 8
                       --backtest-params.stride 3 --backtest-params.n-retrain 1
                       --model-configuration-yaml results/main/model_configuration.yaml
                     with every flag read from the assembled setup and every option from
                     the assembled configuration, neither chosen by this script. The
                     exact command line is the first line of results/main/eval.log.
inputs:              analysis/02_setup/results/main/analysis_dataset.csv
                     sha256:c9bf8b0849c768bfe6c65d54975dd08fa390204f8b59e76904170222a7a87d4c
                     analysis/02_setup/results/main/setup_spec.json (the flags)
                     results/main/model_configuration.yaml (the options and the seed)
                     sha256:ddfa21a670e4… (full digest in model_spec.json)
environment:         environment/ (project main) — CPython 3.13.0, chap-core==2.1.0,
                     for the platform. The *model* runs in its own environment, which
                     chap-core builds from the model's pyproject.toml and uv.lock —
                     numpy 2.5.2, pandas 3.0.5, pyyaml 6.0.3 on CPython 3.13.0. The
                     runner verifies after the run that the lockfile chap-core built
                     from is byte-identical to the tracked one and records it as
                     `shipped_lockfile_is_the_one_built_from`, which was true.
seeds:               project seed 20260822 → component seed 849487747 for
                     03_models/03_candidate/a_hierNB, derived and recorded by
                     scripts/assemble_candidate_config.py and carried into the model
                     inside model_configuration.yaml. One NumPy generator in predict.py
                     serves all three sources of randomness — the Laplace posterior of
                     the coefficients, the prior draw of the province-year effect, and
                     the negative-binomial observation draw. The fit itself is
                     deterministic. Verified rather than asserted: two independent runs
                     under scratch combinations produce identical per-cell scores and an
                     identical fitted object
                     (AI-generated/determinism-checks/model_determinism.json).
commit:              4563baf
instructions-commit: cf97b81
node:                analysis/03_models/03_candidate/a_hierNB
produced:            2026-08-27
```

**What it establishes.** The project's first candidate scores a development mean CRPS of
**26.100** over the same 371 cells as everything else, against 24.337 for climatology, 24.879
for persistence and 22.098 for the reference. It is **last on the headline metric and first
on mean absolute error** — 27.106, better than the reference's 28.902 — and it has the best
interval coverage of any model of ours, 0.720 at 10–90 against a nominal 0.80. The fit took
about two seconds; the eight-split backtest 43 seconds, 5.3 per split.

**What the fitted object records.** Between-province spread on the log-incidence scale
sigma 2.06, between-year spread within a province sigma 1.47, negative-binomial dispersion
0.83, converged in 24 EM rounds on 1 978 usable rows over 17 provinces and 168
province-years. The 1 978 is 2 040 minus the 62 rows whose two-month covariate lag falls
before the record starts, dropped rather than imputed at fit time.

**Where the CRPS goes.** Two provinces carry 2.4 of the 4.0 CRPS by which the candidate
trails the reference: Vientiane Capital, where its 10–90 interval covers **every** outcome
and so is far too wide, and Salavan, where it covers **0.125** and so is far too narrow. The
province-year variance is one number shared by every province, and on the log scale that is
a constant multiplicative width — which is too much for the province with 3 707 observed
cases and too little for the one whose epidemic years are sharper than its variance implies.
That is a structural finding about this configuration, and it is what batch 9's forks have to
answer.

**Cost.** 43 seconds for the full eight-split backtest (`results/main/run_cost.json`),
against 28 for each baseline and about 18 minutes for the reference's four repeats. Batch 5's
manifest estimate for a real candidate was 120 seconds; the measured figure is a third of
that, which batch 12 should carry rather than the estimate.

alternatives-considered: a Bayesian sampler (PyMC or NumPyro) instead of the Laplace
approximation, which would drop the symmetry assumption and add a large dependency with a
compiler in it; rejected for the defaults, and it is the natural sibling if the width problem
above turns out to be in the approximation rather than in the model. An autoregressive term
on lagged counts, which no fork of this node covers and which would give the model
information about the current epidemic that a seasonal-plus-climate regression cannot have;
**not taken**, because adding a structural term outside the four forks would be a silent
judgment call, and it is proposed to batch 9 as a fifth fork instead. Estimating the variance
components by MCMC or REML rather than by the EM update; rejected as a difference the fits
here are too small to feel.

agency: agent-autonomous. The candidate family is batch 4's shortlist and batch 5's design
(`human-set` at the level of "several candidates from the shortlist"); every choice inside
the model — the two harmonics, the Laplace approximation, the province-year prior draw, the
EM update — is this batch's, and each is stated in scripts/hier_nb_model/README.md.

---

## Batch 9 addendum — the fork sweep, 2026-08-27

```
commit:              15b8516   (round 2, and the promoted main path)
                     49825b5   (round 1, which round 2 replaced in the tree; its table
                                is kept at AI-generated/candidate-forks/round1_batch8Defaults/)
instructions-commit: cf97b81
produced:            2026-08-27
```

```
result:              results/main/eval.nc · eval.log · model_spec.json · run_cost.json
                     results/main/fitted_model.json
                     autoregressive_lag3/eval.nc
                     autoregressive_lag3/eval.log
                     autoregressive_lag3/model_spec.json
                     autoregressive_lag3/run_cost.json
                     autoregressive_lag3/fitted_model.json
                     covariates_lagged/eval.nc
                     covariates_lagged/eval.log
                     covariates_lagged/model_spec.json
                     covariates_lagged/run_cost.json
                     covariates_lagged/fitted_model.json
                     covariates_rich/eval.nc
                     covariates_rich/eval.log
                     covariates_rich/model_spec.json
                     covariates_rich/run_cost.json
                     covariates_rich/fitted_model.json
                     fitTime_refitAtPredict/eval.nc
                     fitTime_refitAtPredict/eval.log
                     fitTime_refitAtPredict/model_spec.json
                     fitTime_refitAtPredict/run_cost.json
                     fitTime_refitAtPredict/fitted_model.json
                     observation_negBinomial/eval.nc
                     observation_negBinomial/eval.log
                     observation_negBinomial/model_spec.json
                     observation_negBinomial/run_cost.json
                     observation_negBinomial/fitted_model.json
                     observation_zeroInflated/eval.nc
                     observation_zeroInflated/eval.log
                     observation_zeroInflated/model_spec.json
                     observation_zeroInflated/run_cost.json
                     observation_zeroInflated/fitted_model.json
                     population_covariate/eval.nc
                     population_covariate/eval.log
                     population_covariate/model_spec.json
                     population_covariate/run_cost.json
                     population_covariate/fitted_model.json
                     population_ignored/eval.nc
                     population_ignored/eval.log
                     population_ignored/model_spec.json
                     population_ignored/run_cost.json
                     population_ignored/fitted_model.json
                     yearVariance_shared/eval.nc
                     yearVariance_shared/eval.log
                     yearVariance_shared/model_spec.json
                     yearVariance_shared/run_cost.json
                     yearVariance_shared/fitted_model.json
script:              scripts/run_hier_nb.py   (unchanged)
                     scripts/hier_nb_model/hier_nb.py   sha256:5bdb59a5b3986d68dec84d66afd1e199a927acf4829f7807be4d759bcdea35be
                     scripts/hier_nb_model/train.py     sha256:1f53ccdb593e62f044c4358e7555fc6b2ba5eb58258eda75853b710529276f0f
                     scripts/hier_nb_model/predict.py   sha256:1cdb6ce0e971bbb3f3a86a4d60e3b52ab93eab300b316736cd1af007c6cd3135
                     scripts/hier_nb_model/MLproject    sha256:38964b3208a2662a13ff832357310794aa5ac778d4cf7d75080447e389ccdde3
                     (full digests per combination in each results/<combo>/model_spec.json)
```

**What the model gained.** Code for all six options: a zero-inflation EM step, a two-part
hurdle whose presence block is a penalised logistic fit on the same design, covariates at
several lags, a lagged-count column, a refit inside `predict`, and a province-year variance
estimated per province. `fit_model` and `draw` are new, and they are what let `train` and
`predict` share one fit rather than two implementations of it -- which is what
`b_refitAtPredict` needs to exist at all.

**The rewrite changed nothing on the main path.** Re-running the batch-8 configuration
after it reproduced `04_score/01_collect/results/main/metrics_cell.csv` byte for byte,
which is a stronger check than the tests that would have been written instead.

**What the promoted main path scores.** Mean CRPS **23.698** over the same 371 cells,
against 24.337 for climatology, 24.879 for persistence and 22.098 for the reference. It is
the first model of ours to beat both required baselines. Mean absolute error **27.569**,
the best in the project; 10–90 coverage **0.701** against a nominal 0.80, so it is still
under-dispersed. 36 seconds for the eight-split backtest.

**Every combination was scored on the same data.** `dataset_sha256` is
`c9bf8b0849c7…` in all ten `model_spec.json` files, which is what makes the comparison
paired and is checked rather than assumed.

**The fit does not converge under `year_variance: province_scaled`.** Every combination
carrying that child runs to the 200-round cap; `yearVariance_shared` converges in 48. The
convergence test is a maximum over the relative movement of all seventeen variances, and
the smallest of them keep it above tolerance long after the parameters have stopped moving:
`sigma_province` is 1.265204 at round 197 and 1.265199 at round 200, and the log-likelihood
moves in its sixth significant figure. The tolerance was **not** relaxed -- a criterion
adjusted after seeing a run is a criterion adjusted to pass.

**Rule 6, verified rather than asserted.** Two independent runs of every model of ours
under scratch combinations produced identical per-cell scores and identical fitted objects,
the promoted hurdle candidate included
(`AI-generated/determinism-checks/model_determinism.json`, status `identical`).

alternatives-considered: a zero-truncated negative binomial for the hurdle's positive part
instead of the shifted one; rejected for the cost of a score function this module does not
have, and recorded because it is the obvious next version. Fitting the presence block with
the population offset rather than an estimated log-population coefficient; rejected because
an offset is a statement on the log-mean scale and has no meaning on the logit scale.
Raising the outer-round cap above 200 so the province-scaled fits converge; not taken,
because the parameters are already stable to six figures and the cap is the honest record
of where the procedure stopped.

agency: agent-autonomous.

---

## Batch 21 addendum — the greedy branch, three rounds to a fixpoint, 2026-08-27

**Branch `greedy` only. Nothing recorded in this section is on `main`, and nothing here is
a reported result of the project.** The main line's candidate is the one this file records
above: 23.698 mean CRPS, one application of batch 9's promotion rule. This section records
what the same rule produced when it was iterated.

```
result:              results/main/eval.nc · eval.log · model_spec.json · run_cost.json
                     results/main/fitted_model.json   (a stub -- see below)
                     and the nine sweep combinations, each named after the child it
                     takes, each re-measured in round 3 around the fixpoint so that the
                     leaderboard rows and the files agree. Three of the nine are new on
                     this branch, because the promotions moved which child of those forks
                     is the alternative:
                     autoregressive_none/eval.nc · autoregressive_none/eval.log
                     autoregressive_none/model_spec.json · autoregressive_none/run_cost.json
                     autoregressive_none/fitted_model.json
                     autoregressive_none/candidate_spec.json
                     autoregressive_none/model_configuration.yaml
                     covariates_climateFree/eval.nc · covariates_climateFree/eval.log
                     covariates_climateFree/model_spec.json
                     covariates_climateFree/run_cost.json
                     covariates_climateFree/fitted_model.json
                     covariates_climateFree/candidate_spec.json
                     covariates_climateFree/model_configuration.yaml
                     fitTime_trainOnly/eval.nc · fitTime_trainOnly/eval.log
                     fitTime_trainOnly/model_spec.json · fitTime_trainOnly/run_cost.json
                     fitTime_trainOnly/fitted_model.json
                     fitTime_trainOnly/candidate_spec.json
                     fitTime_trainOnly/model_configuration.yaml
                     and six that batch 9's record above already names:
                     covariates_lagged, observation_negBinomial,
                     observation_zeroInflated, population_covariate,
                     population_ignored, yearVariance_shared
script:              scripts/run_hier_nb.py            unchanged from batch 9
                     scripts/hier_nb_model/*           unchanged from batch 9
                     driven by AI-internal/useful-scripts/greedy_iterate.py, which
                     executes the rule in AI-generated/candidate-forks/greedy/greedy_rule.md
invocation:          .venv/bin/python AI-internal/useful-scripts/greedy_iterate.py round \
                       --reuse-sweep round2_promoted        (round 1)
                     .venv/bin/python AI-internal/useful-scripts/greedy_iterate.py loop
                                                            (rounds 2 and 3)
                     Each round runs candidate_fork_sweep.py for its sweep and then, for
                     the promoted combination, a_hierNB/run.sh and the whole scoring chain
                     with COMBO=main and no COMBO_BASE. The reference and the baselines are
                     not re-run: nothing this branch moves changes what they face, and the
                     reference is unseeded.
inputs:              analysis/02_setup/results/main/analysis_dataset.csv
                     sha256:c9bf8b0849c768bfe6c65d54975dd08fa390204f8b59e76904170222a7a87d4c
                     -- the same file, byte for byte, as every other run in the project
environment:         unchanged: environment/ (CPython 3.13.0, chap-core==2.1.0); the model
                     in its own uv environment built from the tracked lockfile, verified
                     byte-identical after each of the sixteen runs
seeds:               unchanged: project seed 20260822 -> component seed 849487747
commit:              cb61c1d  (the scripts, throughout all three rounds)
instructions-commit: cf97b81
node:                analysis/03_models/03_candidate/a_hierNB
produced:            2026-08-27
```

**What the iteration produced.** Three rounds, ending in a fixpoint — a round in which no
fork's best child beat the main path by more than the 0.57 CRPS floor.

| after round | main path moved | mean CRPS |
|---|---|---|
| 0 | — (batch 9's promoted candidate) | 23.698 |
| 1 | `02_covariates` → `b_rich`, `04_fitTime` → `b_refitAtPredict` | **21.857** |
| 2 | `05_autoregressive` → `b_lag3` | **21.275** |
| 3 | nothing clears the floor: the fixpoint | 21.275 |

The greedy model is the hurdle observation model with all three climate columns at lags 1,
2 and 3, a log-population offset, a lagged-count term at three months, per-province annual
variances, and refitting inside every `predict` call. Configuration
`8e021eaf2d1e3751…`; 91 seconds for the eight-split backtest against 36 for the main
line's.

**What it scores.** Mean CRPS **21.275** over the same 371 cells, against the reference's
22.098, climatology's 24.337 and persistence's 24.879 — and against every one of the
reference's four repeats individually, the best of which is 21.820. Skill score **+0.037**,
where the main line's is −0.072. Mean absolute error 26.278, the best in the project. 10–90
coverage 0.741 against a nominal 0.80.

**And the comparison still cannot separate the two models.** The paired per-cell difference
is −0.823 CRPS with a split-clustered standard error of **1.602** — 0.51 standard errors.
It wins **50.4 %** of cells and 3 of 8 splits. Beating the reference on the mean and being
indistinguishable from it are both true, and reporting the first without the second would
be the more attractive half of a result the backtest does not support.

**Where the gain is.** By lead time the greedy model is 17.97 / 20.41 / **25.44** against
the reference's 16.54 / 21.97 / 27.79: it now wins at two and three months and still loses
at one, which is where the whole remaining gap is. The main line's candidate was 20.4 /
23.2 / 27.5, so two rounds of selection bought about 2.4 CRPS at the two longer leads and
2.4 at the shortest.

**Rule 5, and the cost the greedy path pays for its score.** `results/main/fitted_model.json`
**is a stub**. The first fork the rule moved was `04_fitTime`, and under `fit_time = predict`
the fit happens once per split inside chap-core's untracked run directories, so the model
this branch ends on has *no stored fitted object at all* — no coefficients, no variance
components, no EM history. Batch 9 recorded that gap as a property of one non-main child;
on this branch it is a property of the reported model. A selection rule that maximises
development CRPS is indifferent to whether the model it selects can be inspected, and this
is what that looks like in the record.

alternatives-considered: promoting one fork per round rather than every fork that clears
the floor, which is the stricter reading of coordinate descent and would have taken four
rounds instead of three; not taken, because it is not the rule batch 9 wrote and the branch
exists to iterate *that* rule. Committing each round's promotion separately, as batch 9 did
by hand; not done, because the loop runs unattended — the cost is that the tree's
main-path markers moved twice inside one commit, and the round records rather than the git
history are what say when.

agency: agent-autonomous, under a human-set instruction to explore the iterated path on a
branch (plan §4b, 2026-08-27).
