[overview](../../README.md) / [analysis](../README.md) / **05_stability**

# 05_stability

**Claim:** How far does the project's conclusion survive the reasonable alternatives the main path did not take? The node enumerates every judgment call the tree carries as a fork, costs the analyses that take them instead, and runs that set so the reported result is a distribution over analyses that all looked defensible rather than the one that was run.

**Result:**

The tree carries **17 forks**, not the ten batch 5 counted by hand: phase C added five while
building the candidates, and two baseline forks were never on the hand-written list although
the plan's phase D names one of them. `results/forks.csv` is read from the tree, so the next
fork anyone adds is in the manifest without anyone remembering to add it — and
`/validate invariants` fails if it is not.

The manifest is **24 tier-1 combinations**, one per path not taken, plus **8 tier-2 pairs**
selected by a rule fixed and hashed before tier 1 ran, plus one combination that already
exists and perturbs nothing. Tier 1 costs **124 minutes on development and 75 on the
holdout**, against a 12-hour budget, so **nothing is cut** and the cut order is recorded
against the day something is (`results/manifest_notes.json`).

**Compute is not what binds, and it is not close.** Of the 124 development minutes, **89 are
the reference model** — five setup rows at four unseeded repeats each, through an amd64
image under emulation, for a model the plan forbids perturbing. Every model of ours, on
every combination in tier 1, costs 21 minutes together.

What binds is that **nine of the 24 rows have no scripts**: the tree named those children in
prose and did not carry them until this batch created them. And twelve of the fifteen that
do have scripts hold results produced around a main path that has since moved, so their
directories describe a different analysis from the one their manifest row now names.

**Batch 13 ran the seven setup and scoring rows.** `results/conclusions.csv` now has **8 of
33**, and the shape of the answer is already visible.

**The five `02_setup` forks do not move the conclusion.** Skill spans **+0.1266 to +0.1861**
around the main path's +0.1485, and every one of those gaps is smaller than the reference's
own 0.57 CRPS re-run spread. Three of the five move the score by moving *the reference*
rather than our model: dropping two unevaluable provinces costs the reference 1.05 CRPS and
our pool 0.03.

**The one scoring fork moves it four times as much as any of them.** Population weighting
gives +0.2288 and case weighting +0.2320, both about +0.08 of skill from the main path, from
re-weighting a stored file and re-running nothing. The cheapest fork in the manifest —
thirteen seconds against twenty minutes — is the one the conclusion is most sensitive to.

**The main path sits near the bottom of the range.** Six of the seven perturbations improve
the reported skill score. That is what a conservative main path looks like, and it is also
what a systematically flattering set of alternatives would look like; eight rows cannot tell
those apart, and the remaining sixteen tier-1 rows are what would.

**Under case weighting, persistence beats the reported model** (86.598 against 88.484) and
the pool's 10-90 coverage falls from 0.863 to 0.701. The pool is too wide on the quiet months
and too narrow on the outbreak months, which no single weighting shows on its own. This is
the most useful thing tier 1 has produced so far and it is not a skill score.

Sixteen tier-1 rows remain: two baseline children batch 22 builds, and fourteen candidate and
family rows batch 14 runs. Tier 2 stays unselected until every tier-1 row has been attempted —
`plan_manifest.py` now refuses to apply `tier2_rule.md` before then, which is a change to when
the rule is applied and not to the rule, whose sha256 is unchanged.

**Batch 22 ran the two baseline rows, and they are the widest pair in the set.**
`results/conclusions.csv` now has **10 of 33**.

**The persistence fork is the largest single-row move of the reported conclusion so far**, and
it is downward: skill **+0.1206** against the main path's +0.1485, from the pool's mean CRPS
rising to 19.434. **The climatology fork is the smallest move of any row**: +0.1460, 0.0025
of skill. Two forks of the same kind, on the two baselines the plan requires, an order of
magnitude apart in what they are worth.

**The main path is no longer at the bottom of the range.** After batch 13, six of seven
perturbations improved the reported skill and the honest reading was that a conservative main
path and a flattering set of alternatives look the same from there. Both new rows are below
the main path, which is the first evidence for conservatism rather than flattery — two rows,
which is not much, and the fourteen candidate rows are still the ones that would settle it.

**The most useful thing in the pair is not a skill score.** The alternative construction of
the persistence baseline scores 20.698 against the main path's 24.879 and beats the reference
model at 22.098. The reported analysis is built on the worse of two published constructions
of a model the plan's §4 requires, and the pool that contains it is *better off* for that,
because a linear opinion pool profits from its members disagreeing.

Fourteen tier-1 rows remain, all of them batch 14's, and tier 2 stays unselected until they
have been attempted.

**Batch 14 ran the twelve candidate rows, the two family rows and all eight tier-2 pairs.**
`results/conclusions.csv` now has **32 of 33** — the thirty-third is `family_ensemble`, the
main path's own choice under its own name, which perturbs nothing.

**The choice of model family moves the conclusion twenty-seven times further than any choice
inside a family.** Swapping the reported pool for candidate 1 costs **0.2209** of skill, for
candidate 2 **0.0884**. The eight forks inside those two families span **18.638 to 18.933
CRPS** over the eleven combinations they perturb — a range of 0.295, about half the reference's own 0.57 re-run spread — so nothing in
that block can be attributed to a model at all. The mechanism is the pool. Phase C's own sweeps
record candidate 1's observation model as a 0.601 CRPS swing to candidate 1 alone; the same
fork is a 0.102 swing to the pool, because three of its four members did not move. And
candidate 2's quantile head makes candidate 2 worse on its own while making the pool better,
so the damping is not simple scaling — the same fact batch 22 found when a sharper
persistence member made a worse pool.

**The exception is the one candidate-internal fork that is not inside a member.** Fitting the
pool's weights by minimising its CRPS on a year held back inside the training frame is worth
**0.1820** of skill and takes the reported model to 22.838 CRPS, *behind* the reference, with
its paired comparison falling to 0.48 standard errors. It is the second-largest single-fork
move in the set.

**The pairs are not the sum of their parts.** `conclusions.csv` now carries
`delta_skill_additive` and `interaction` for every tier-2 row. Across the eight the
interaction runs from **−0.1033 to +0.0424**, and the extreme is larger than either main
effect behind it: removing the two provinces with no evaluable cell is worth +0.0376 alone,
weighting the headline mean by cases +0.0835 alone, and together they come to **+0.0177**
against an additive +0.1211. Both work by re-weighting what the mean is over, so taking both
does not do it twice. This is the third demonstration that fork effects do not compose —
batches 9 and 21 were the first two — and the first on the reported conclusion. It is why
tier 2 was not cut.

**Case weighting is the one condition under which a required baseline beats the reported
model**, and it does so in every combination it appears in: five rows of the 32, all five
case-weighted. The five rows where our model does not beat the reference are the five that
replace it or refit its weights. No choice about the data, the evaluation, the scoring or the
baselines takes our model below the reference on any row.

**Calibration moves far more than the score does.** 10–90 coverage runs from **0.458 to
0.920** against a nominal 0.80 while the skill score stays positive on 27 of 32 rows. Both
extremes involve a re-weighted mean: the pool under population weighting is badly
over-dispersed and candidate 1 under case weighting badly under-dispersed. §2's rule that a
badly calibrated CRPS winner has not won bites hardest exactly where the CRPS looks best.

The development set is complete. Batch 15 turns it into the reported distribution, puts the
driver into `analysis/run.sh` now that every row can run, and freezes the holdout manifest.

**Batch 15 reported the distribution, and the answer has two halves.**

**The conclusion survives, and the reported number is not the middle of the range it
survives across.** Skill runs **−0.0724 to +0.2320** around the reported +0.1485, which sits
**thirteenth of thirty-two**; our model beats the reference on 27 and both required
baselines on 27; 10–90 coverage runs 0.458 to 0.920 against a nominal 0.80. The failures are
structured rather than scattered: the five rows the reference wins are the five that replace
our model or refit its weights, and the five a required baseline wins are the five that
weight the headline mean by cases. → `results/distribution.json`

**Six of the seventeen forks move the conclusion further than the reference model moves on
its own, and eleven do not.** The yardstick is measured, not chosen: the reference is
unseeded and was scored four times, and our model's skill against those four spans
**0.0218**. Above it: the model family (0.2209), the pool's weighting (0.1820), the
weighting of the headline mean (0.0835), the province filter (0.0376), the persistence
construction (0.0279), the training window (0.0219, which is the band itself to within
0.0001). Below it: everything else, including eight of the nine candidate-internal forks
phase C spent three batches selecting among — eight of the eleven below the line,
the other three being two `02_setup` forks and one baseline fork. → `results/sensitivity_by_fork.csv`

**The manifest was re-planned and did not move.** `manifest.csv` came back byte-identical
now that every row has been attempted and the frozen pair rule reads a complete tier 1 —
which is what made it safe to put the driver into `run.sh`. `analysis/run.sh` now reproduces
the stability result as well as the reported one, at about four hours rather than twenty
minutes, and the node's own script order is the phase's: cost, plan, run tier 1, collect,
re-plan so the frozen rule can pick tier 2 from a tier 1 that exists, run those, collect,
report.

**The whole set cost 3.66 h against a 12 h budget** (`results/run_status.csv`, summed) and
nothing was cut. The frozen cost model predicted the total to within one part in a thousand
— 7 469 s against 7 469 s — and individual rows by ratios from 0.51 to 1.91, so the cut
order it ranks would have carried no information had anything been cut.

**The phase-E set is frozen.** Thirty-three rows under `__holdout` names, an estimated
2.07 h, each carrying the development conclusion it is to be reported beside, so the pairing
is fixed with the set rather than assembled after the seal comes off.
→ `results/manifest_holdout.csv`, `results/holdout_freeze.json`

Phase D is complete.

## Claims resting on this node

- **[C1](../../claims.md#c1)** — The conclusion this project reports is one member of a distribution over thirty-two analyses that all looked reasonable, fixed before any of them ran. The reported skill score against the reference model is +0.1485; across the set it runs from -0.0724 to +0.2320, with a median of +0.1469, and the reported analysis sits thirteenth of thirty-two.
- **[C2](../../claims.md#c2)** — Our model beats the reference model on 27 of the 32 analyses and both required baselines on 27, and the failures are structured rather than scattered. The five analyses where the reference wins are exactly the five that replace our model or refit its weights; the five where a required baseline wins are exactly the five that weight the headline mean by cases.
- **[C3](../../claims.md#c3)** — The choice of model family is what the conclusion is sensitive to, and the choices made inside a family are not. Swapping the reported linear opinion pool for candidate 1 costs 0.2209 of skill and for candidate 2 0.0884, while the eight forks inside those two families move it by at most 0.0081, and the eleven combinations they perturb span 18.638 to 18.933 mean CRPS -- a range of 0.295 against the reference model's own 0.565 re-run spread.
- **[C4](../../claims.md#c4)** — Six of the tree's seventeen judgment calls move the reported conclusion further than the reference model moves on its own, and eleven do not. The yardstick is measured rather than chosen: the reference is unseeded and was scored four times, and our model's skill score against those four repeats spans 0.0218. Above that band sit the model family (0.2209), the pool's weighting (0.1820), the weighting of the headline mean (0.0835), the province filter (0.0376), the persistence construction (0.0279) and the training window (0.0219, which is the band itself).
- **[C5](../../claims.md#c5)** — The cheapest analysis in the perturbation manifest is the one the conclusion is most sensitive to among the choices that leave our model alone. Re-weighting the headline mean re-runs no model at all -- thirteen seconds against twenty minutes -- and moves the reported skill by 0.0835, four times as far as any of the five setup forks that re-run every model on the leaderboard.
- **[C6](../../claims.md#c6)** — Under case weighting a required baseline beats the model this project reports, and it does so in every combination where case weighting appears -- five of the thirty-two analyses, all five case-weighted. The pool is too wide on the quiet months and too narrow on the outbreak months, which no single weighting of the mean shows on its own.
- **[C7](../../claims.md#c7)** — Fork effects do not compose, so a one-at-a-time stability report cannot be added up. Across the eight pairs the interaction runs from -0.1033 to +0.0424, and the extreme is larger than either main effect behind it: dropping the two provinces with no evaluable cell is worth +0.0376 alone and weighting the mean by cases +0.0835 alone, and together they come to +0.0177 against an additive +0.1211, because both work by re-weighting what the mean is over.
- **[C8](../../claims.md#c8)** — Calibration moves much further across the perturbation set than the score does. Interval coverage at 10-90 runs from 0.458 to 0.920 against a nominal 0.80 while the skill score stays positive on 27 of the 32 analyses, and both extremes involve a re-weighted mean. The rule that a badly calibrated CRPS winner has not won therefore bites hardest exactly where the CRPS looks best.
- **[C9](../../claims.md#c9)** — The reported analysis stands on the worse of two published constructions of a baseline the plan requires, and the model it reports is better off for that. Wrapping the persistence point in a fitted negative binomial scores 20.698 mean CRPS against the main path's 24.879 and beats the reference model at 22.098; with that sharper member in the pool, the pool's margin over its own best member falls from 1.954 to 1.264 CRPS. It was not promoted, because phase C was closed and the manifest frozen before the row ran.
- **[C10](../../claims.md#c10)** — Compute was not the constraint on the stability work and was not close to it. The whole development manifest -- twenty-four one-at-a-time analyses and eight pairs -- ran in 3.66 hours against a 12-hour budget, nothing was cut, and most of the time was the reference model's four unseeded repeats running through an amd64 image under emulation for the one model the plan forbids perturbing. What bound the work was implementation effort: nine of the twenty-four alternatives were sentences in a claim file rather than paths in the tree when the manifest was planned.
- **[C11](../../claims.md#c11)** — A cost model that predicts the total to within a per cent can be uninformative about every individual row. Over the whole manifest the planned total is 7469 seconds against an actual 7469, a ratio of 1.00, while per-row ratios run from 0.51 to 1.91 -- because the model summed each row's parts as measured under the main path and could not know that a row changes how much work a part does. The manifest's cut order is ranked on those estimates, so it carries no information; nothing was cut, so nothing rests on it.
- **[C12](../../claims.md#c12)** — The set of analyses to be run on the held-out year is fixed before the year is opened: thirty-three rows, each the development row under a holdout name, with the development conclusion it is to be reported beside carried row by row. Freezing the set but assembling the development half of the comparison afterwards would leave the comparison selectable after the fact even though neither half was.
- **[C13](../../claims.md#c13)** — The held-out year was opened once, and the set of analyses evaluated on it was fixed before it was opened. Thirty-two rows -- every row of the development set that has a conclusion -- ran on 2010 through the same scripts their development twins ran, none failed, and each row's development conclusion was frozen into the manifest beside it so the pairing could not be assembled after the seal came off.
- **[C15](../../claims.md#c15)** — The distribution of conclusions over the frozen set is more than twice as wide on the held-out year as on the development period: -0.5038 to +0.2026 against -0.0724 to +0.2320. Six of the thirty-two analyses fall below zero on 2010, where none did on development, and the reported analysis moves from thirteenth of thirty-two to eighteenth.
- **[C16](../../claims.md#c16)** — Twenty-eight of the thirty-two analyses scored worse on the year they had not seen, with a median drop of 0.056 in skill. The four that scored better were all analyses that had been below the reference model on development.
- **[C17](../../claims.md#c17)** — Ranking these analyses on the development set is a weak guide to how they rank on a year they have not seen. The Spearman rank correlation between the development and holdout skill scores across the thirty-two is +0.396. The ranking of the judgment calls transfers better, at +0.679, with fourteen of seventeen forks agreeing on whether they move the conclusion beyond their own dataset's noise band.
- **[C19](../../claims.md#c19)** — The province filter is the largest single judgment call in the project on the held-out year, at 0.2696 of skill, having been fourth at 0.0376 on development. Over the same change the model family halves, from 0.2209 to 0.0949, and the pool's own weighting fork collapses from 0.1820 to 0.0121 and falls below the noise band.
- **[C20](../../claims.md#c20)** — The reported model's over-dispersion on development does not survive the change of year. Its 10-90 interval coverage is 0.863 against a nominal 0.80 on the development backtest, the widest in the project, and 0.755 on the held-out year; across the frozen set coverage runs 0.458 to 0.920 on development and 0.210 to 0.854 on 2010.
- **[C21](../../claims.md#c21)** — The forks do not compose on the held-out year either. Across the eight frozen pairs the largest interaction is -0.2876, on the same row that carries the largest single move, and it is larger than either main effect behind it.
- **[C39](../../claims.md#c39)** — The cost model was tested as a prediction for the first time on the held-out half and it held at the total: 8 602 seconds actual against 7 468 planned, a ratio of 1.15 over 32 rows, where the development half's 1.00 was measured over runs that had already happened. The worst row is again the one that changes how much work a part does -- refitting at every split, at 1.97 -- so the total being right a second time does not make any individual estimate right, and the cut order those estimates rank still carries no information.
- **[C41](../../claims.md#c41)** — The pool's second path is available on eleven of the fifty-one combinations that run it, and the forty it is missing from are missing it for a structural reason rather than an accidental one. The reconstruction compares the pool with its members' own separate evaluations, and this tree evaluates a member on its own only under the family fork's own combination -- so a row that moves a fork inside a member has no separate run of that member under the configuration the pool gave it, and no order of execution would produce one. Across the eleven, the residual between the rebuilt pool and the pool that ran is 0.016 to 0.136 CRPS, largest on the held-out rows where every score is about four times the size.

## Material

The node's own files: [`claim.md`](../../../../analysis/05_stability/claim.md) · [`results/`](../../../../analysis/05_stability/results) · [`scripts/`](../../../../analysis/05_stability/scripts) · [`provenance/`](../../../../analysis/05_stability/provenance) · [`run.sh`](../../../../analysis/05_stability/run.sh).

---

> **A snapshot, generated 2026-09-27 from the tree at commit `3d89200`.** Everything here is derived from files the repository versions and regenerates in seconds with `.venv/bin/python AI-internal/useful-scripts/build_claim_tree_md.py` (or `/hierarchical-report`). If the tree has changed since that commit, rebuild rather than trust this copy; never hand-edit.
