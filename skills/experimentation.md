---
name: experimentation
description: Implementation expertise for A/B testing, experimental design, hypothesis testing, statistical inference, power analysis, and Bayesian methods.
use_when: A workflow stage involves designing or analyzing experiments, significance testing, or causal comparison.
---

# Experimentation — Expertise Module

Load this for experiment design and inference. `claude.md` owns the workflow; this module supplies the how.

## A/B testing
- Define the hypothesis, primary metric, and minimum detectable effect (MDE) *before* running.
- Randomize at the correct unit (user vs session); check for sample-ratio mismatch. One primary metric; pre-register guardrail metrics.
- Don't peek/stop early on naive p-values — it inflates false positives. Run to the pre-computed sample size or use sequential methods.

## Experimental design
- Control confounders via randomization; use blocking/stratification to reduce variance.
- Factorial designs to test multiple factors and interactions efficiently. Watch network/spillover effects (consider cluster randomization).

## Hypothesis testing
- State H0/H1 and α up front. Choose the test by data type: t-test/Welch (means), chi² (proportions/association), Mann-Whitney (non-normal).
- Report effect size + CI alongside p-value. Correct for multiple comparisons (Bonferroni/Benjamini-Hochberg).

## Statistical inference
- Confidence intervals communicate magnitude and uncertainty better than a bare p-value.
- Distinguish statistical significance from practical significance; tie back to the MDE and business impact.

## Power analysis
- Power = P(detect a true effect). Target ≥0.80. Sample size is driven by effect size, variance, α, and power.
- Compute required n *before* the experiment; underpowered tests waste time and mislead.

## Bayesian analysis
- Report P(B > A) and expected loss / credible intervals — often more decision-friendly than frequentist p-values.
- Choose priors deliberately (informative vs weak) and state them. Supports continuous monitoring without the peeking penalty.

## Causal inference (observational)
When a randomized experiment isn't possible (ethics, cost, historical data), estimate causal effect from observational data — but correlation ≠ causation without explicit assumptions.
- **Methods:** difference-in-differences (parallel-trends assumption); regression discontinuity (treatment assigned by a cutoff); instrumental variables (an instrument affecting treatment but not outcome directly); propensity score matching/weighting (balance confounders); synthetic control (construct a counterfactual from a weighted donor pool).
- **Confounding is the central threat:** an unmeasured common cause biases the effect. State assumptions explicitly; run sensitivity/placebo tests.
- **Use cases:** measuring campaign/feature/policy impact when holdouts weren't run; retrospective lift; pricing changes.
- **Tradeoff:** A/B testing is the gold standard for causality — reach for observational methods only when you cannot randomize, and report the identifying assumptions honestly.
- **Key point:** "Randomize if you can; if you can't, name the confounders and the assumption (parallel trends, valid instrument, ignorability) that licenses a causal claim."

## Attribution
- Assigns credit for an outcome across touchpoints. Rule-based (first/last/linear/time-decay) is simple but biased; data-driven (Markov/Shapley) is fairer but needs more data.
- Prefer **incrementality testing** (holdout/geo experiments) over correlational attribution — it answers "what did this cause?" not "what did this co-occur with?"
