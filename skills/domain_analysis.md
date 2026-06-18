---
name: domain-analysis
description: Domain-specific analytical patterns for customer, marketing, fraud, identity resolution, forecasting, financial, supply chain, and product analytics.
use_when: A project's business domain calls for established domain methodology, target framing, or metrics.
---

# Domain Analysis — Expertise Module

Load this when a project sits in a specific business domain. `claude.md` owns the workflow; this module supplies domain framing, common targets, and metrics.

## Customer analytics
- Segmentation (RFM, clustering), churn prediction, CLV, retention/cohort analysis.
- Targets are often imbalanced (churn, conversion) — evaluate with precision/recall, not accuracy.

## Customer behavior modeling
Predicting individual customer actions to drive proactive, personalized intervention. A family of related supervised problems sharing target framing, leakage, and calibration concerns.
- **Propensity modeling:** P(customer takes action) — buy, click, upgrade, lapse. Classification with **calibrated probabilities** (see data_science.md) so scores are usable for prioritization and expected-value math, not just ranking.
- **Churn / retention:** predict attrition within a horizon; define the churn event and observation/prediction windows carefully. Voluntary vs involuntary churn need different treatment. Survival analysis (Cox, Kaplan-Meier) when *time-to-event* matters, not just yes/no.
- **Conversion / renewal prediction:** time-boxed propensity tied to a funnel stage or contract cycle; beware survivorship and selection bias in the training population.
- **Lifetime value (LTV/CLV):** historical (realized) vs predictive (BG/NBD + Gamma-Gamma for non-contractual; discounted expected margin for contractual). Combine with retention curves; discount future cash flows.
- **Next-best-action / next-best-offer (NBA/NBO):** rank candidate actions by expected value = P(accept | action) × value − cost, subject to eligibility/business constraints. Often a propensity model per action feeding a ranking/optimization layer; can extend to contextual bandits / RL for explore-exploit.
- **Journey signal modeling:** engineer features from event sequences (recency, frequency, velocity, channel mix, stage transitions); sessionize and aggregate behavioral streams into model-ready signals.
- **Use cases:** proactive retention outreach, lead scoring, upsell/cross-sell targeting, marketing prioritization, win-back.
- **Tradeoffs/risks:** **target leakage** is the #1 killer (features that postdate the outcome); concept drift as behavior shifts; acting on predictions changes future data (feedback loops); calibration matters more than raw AUC when scores drive spend.
- **Key points:** propensity needs *calibration* not just discrimination; NBA = propensity × value − cost under constraints; define windows to prevent leakage; survival models when timing matters.

## Marketing analytics
- Attribution (first/last/multi-touch), campaign lift, CAC/LTV ratio, funnel conversion.
- Prefer incrementality/holdout testing over correlational attribution where possible.

## Acquisition channel & marketing-mix value analysis
"Which channels bring customers who generate real value?" — a deceptively simple question that is really about defining value, controlling for time, and separating causation from selection.
- **Define "value" first (the framing move):** clarify the outcome before modeling — revenue, gross margin, retention/tenure, LTV, or engagement? Short-term (first purchase) vs long-term (realized/predicted LTV)? The choice changes every downstream conclusion; surface it and confirm with the stakeholder.
- **Cohort by acquisition channel:** group customers by channel × acquisition period, track value over *relative* time since acquisition. This is the backbone analysis.
- **Maturation / observation-window bias:** "customers who *go on to* generate value" need time to mature — recent cohorts haven't had the chance. Never compare raw lifetime value across channels with different acquisition dates; use equal-tenure windows or predicted LTV.
- **Selection bias is the central trap:** channels are not randomized — customers self-select. A channel may look high-value because it *attracts* already-valuable people, not because it *causes* value. Distinguish **descriptive** (which channels correlate with value) from **causal/incremental** (which channels are worth more spend).
- **Toward causal:** geo/holdout experiments and incrementality tests are gold standard; absent randomization, use causal-inference methods (matching, diff-in-diff — see experimentation.md) and state the assumptions.
- **Economics:** value alone is insufficient — weigh **LTV against CAC** per channel; a high-value channel can still be unprofitable, and a cheap channel with modest value can win on ratio. Consider volume/saturation and diminishing returns.
- **Risks:** attribution-window and multi-touch ambiguity; survivorship/selection in the training population; conflating correlation with incrementality; ignoring channel interaction (assists vs last-click).
- **Key points:** (1) "What does *value* mean here, and over what horizon?" (2) cohort + maturation control before any cross-channel comparison; (3) selection bias — the channel may select for value, not cause it; (4) LTV:CAC, not value alone; (5) be explicit about correlation vs causation and what evidence would upgrade a claim.

## Fraud detection
- Severe class imbalance + adversarial drift. Optimize for recall at acceptable precision; use precision-recall (not ROC) curves.
- Cost-sensitive thresholds (a missed fraud ≠ a false alarm in cost); anomaly detection for novel patterns.

## Identity resolution & Customer 360
Resolving disparate records into a single real-world entity (person/household/account) across sources. Foundational for Customer 360, personalization, fraud, and marketing activation.
- **Matching approaches:** *deterministic* (exact/rule-based on stable keys — email, phone, SSN) is precise but brittle to dirty data; *probabilistic* (Fellegi-Sunter, ML/fuzzy on names, addresses, DOB) recovers more matches but risks false merges. Most production systems are **hybrid**: deterministic first, probabilistic for the residual.
- **Record linkage pipeline:** standardize/normalize → **blocking** (group candidates by a key — zip, soundex — to avoid O(n²) comparisons) → pairwise scoring → classify match/non-match/review → cluster transitive matches into entities.
- **Householding:** roll individuals up to a household/address unit — useful for marketing suppression and shared-economics products.
- **Identity graphs / knowledge graphs:** model entities as nodes and matches/relationships as edges; resolve via connected components or graph clustering. Graphs capture transitive links (A=B, B=C ⇒ A=C) and relationship context a flat table can't. Watch for over-merging via weak edges ("identity bombs").
- **Confidence scoring:** attach a match-confidence/score to each link; expose a threshold so downstream consumers choose precision vs recall per use case.
- **Precision vs recall tradeoff (the core decision):** high precision (fewer false merges) protects against mixing two people's data — critical for privacy/billing/credit; high recall (fewer missed links) maximizes a unified view — better for marketing reach. Tune the threshold to the cost of each error type, not a default.
- **Use cases:** Customer 360, cross-device/cross-channel unification, fraud rings, GDPR/CCPA "right to be forgotten" (need a complete identity), deduplication.
- **Risks:** false merges leak data across people; missed matches fragment the view; addresses/names drift over time; evaluation is hard without labeled ground truth (use clerical review samples, pairwise precision/recall).
- **Key points:** blocking is the scalability lever; hybrid deterministic+probabilistic is the pragmatic default; identity graphs handle transitivity; the threshold is a business cost decision, not a technical one.

## Forecasting
- Respect temporal order: time-based splits, never random. Backtest with rolling/expanding windows.
- Decompose trend/seasonality/residual; baseline with naive/seasonal-naive before ARIMA/Prophet/ML.

## Financial analytics
- Risk scoring, default/credit models, profitability, anomaly detection in transactions.
- Explainability and auditability are often regulatory requirements — favor transparent models.

## Supply chain analytics
- Demand forecasting, inventory optimization, lead-time variability, service-level trade-offs.
- Model uncertainty (safety stock) explicitly; costs are asymmetric (stockout vs holding).

## Product analytics
- Funnels, activation/retention, feature adoption, engagement cohorts, north-star metric design.
- Tie metrics to user actions; pair with experimentation (see experimentation.md) for causal claims.
