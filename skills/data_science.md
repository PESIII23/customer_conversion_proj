---
name: data-science
description: Implementation expertise for data profiling, quality assessment, cleaning, EDA, feature engineering, ML modeling, evaluation, and explainability.
use_when: Workflow phases 3–8 (Data Quality, Cleaning, EDA, Feature Engineering, Modeling, Evaluation) need methodology — the how behind the claude.md workflow stages.
---

# Data Science — Expertise Module

Load this when a workflow stage needs statistical/ML methodology. `claude.md` owns the workflow, gates, and ordering; this module supplies the technique.

## Data profiling
- Start with shape, dtypes, `df.info()`, `df.describe(include='all')`, per-column null/unique counts.
- Profile before deciding anything; never assume schema or distribution.

## Data quality assessment
- Quantify: missingness %, duplicate %, dtype mismatches, range/domain violations, referential integrity across joined sources.
- Distinguish *random* vs *systematic* issues; report findings to the user before imputing or dropping.

## Missing value analysis
- Classify mechanism: MCAR / MAR / MNAR — it dictates the fix.
- Numeric → median (skewed) or mean (symmetric); categorical → mode or explicit "Missing" category; time series → forward/backfill.
- Fit imputers on training folds only (leakage). Add a missingness indicator when absence is informative.

## Duplicate analysis
- Separate exact duplicates from key-level duplicates; confirm the intended grain before deduping.
- Investigate *why* duplicates exist (bad join, repeated ingestion) rather than blindly dropping.

## Outlier detection
- IQR (1.5×) or z-score for univariate; isolation forest / LOF for multivariate.
- Decide per-column: keep (real signal), cap/winsorize, or remove — and document the rationale. Outliers are not automatically errors.

## Data cleaning strategies
- Standardize formats/dtypes/units; resolve inconsistent categoricals (casing, synonyms).
- Treat raw data as immutable; write cleaned output to a separate location. Log every decision.

## EDA methodologies
- Univariate (distributions, skew) → bivariate (target relationships, correlations) → multivariate (interactions, collinearity).
- For non-linear/non-monotonic relationships use mutual information, not just Pearson. Bin continuous vars to expose threshold effects vs the target.
- Triangulate before excluding a feature (e.g., chi² + MI + correlation agreeing).

## Statistical analysis
- Match the test to the data: chi² for categorical association, t-test/ANOVA for group means, correlation for linear relation.
- Report effect size and p-value; beware high-cardinality identifiers inflating chi².

## Feature engineering
- Derive features only when justified by domain or EDA. Encode ordinals with order-preserving maps; one-hot nominal; consider target/frequency encoding for high cardinality.
- Scale for distance/gradient models (KNN, SVM, logistic); unnecessary for tree models.
- Run selection inside CV (fit on train folds) to avoid leakage. Drop redundant collinear features (r > ~0.9).

## Machine learning
- Establish a simple, interpretable baseline first (e.g., logistic regression) before complex models.
- Stratified train/test split for classification; fix `random_state=42`. Address imbalance with `class_weight='balanced'` or resampling — and measure its effect, don't assume it.
- Bagging (Random Forest) reduces variance; boosting (Gradient Boosting/XGBoost) reduces bias. Pick the family that matches the error type.

## Model evaluation
- Never use accuracy alone under imbalance. Report precision, recall, F1, ROC-AUC, and the confusion matrix.
- ROC-AUC measures ranking/discrimination; threshold tuning trades precision vs recall without changing AUC.
- Validate on a held-out test set (Verified), not just CV (Estimated). Compare train vs test for bias-variance.

## Explainability
- Coefficients (logistic/linear) for transparent models; permutation importance, SHAP, or partial dependence for black boxes.
- Favor explainability when the decision must be auditable/regulated; weigh it explicitly against marginal accuracy gains.

## Calibration & probability estimation
When a score drives spend, eligibility, or expected-value decisions (propensity, NBA, risk), the *probability* must be trustworthy — not just the ranking.
- **Discrimination ≠ calibration:** a model can have high AUC yet be poorly calibrated (predicted 0.9 ≠ 90% observed). Check with a reliability/calibration curve and Brier score / log loss.
- **Fixes:** Platt scaling (sigmoid) or isotonic regression on a held-out set; `CalibratedClassifierCV`. Tree ensembles and SVMs often need it; tune *after* selecting the model.
- **Use cases:** expected-value ranking (P × value), thresholding for cost-sensitive decisions, blending model scores with business rules.
- **Key point:** "AUC says it ranks well; calibration says the probabilities are honest — you need both when the number, not just the order, is consumed."

## Ranking models
When the goal is *ordering* (recommendations, search, lead prioritization) rather than absolute prediction.
- **Approaches:** pointwise (regress/classify each item), pairwise (learn relative order — LambdaMART), listwise (optimize the whole list).
- **Metrics:** NDCG, MAP, MRR, Precision@k/Recall@k — position-aware, unlike accuracy.
- **Tradeoff:** pointwise is simplest and reuses classification/calibration; pairwise/listwise optimize ranking directly but cost complexity. Often calibrated propensity feeds a ranker.

## Recommendation & personalization systems
Suggesting relevant items to users; a core personalization capability spanning retrieval, ranking, and serving.
- **Content-based:** recommend items similar to a user's past items via item features/embeddings. Handles new items; limited serendipity; needs good item features.
- **Collaborative filtering (CF):** learn from user-item interaction patterns — neighborhood (user/item-kNN) or latent factor (matrix factorization, ALS). Strong signal; suffers cold-start and popularity bias.
- **Hybrid:** combine content + CF (and context) to cover each other's gaps — the production default.
- **Two-stage retrieval & ranking:** **candidate generation** (cheap, high-recall retrieval of hundreds from millions — ANN over embeddings, co-occurrence) → **ranking** (expensive, high-precision model scoring the shortlist with rich features). Scales personalization to large catalogs.
- **Embeddings:** dense vectors for users/items learned from interactions or content; power similarity search (ANN: FAISS/ScaNN) and serve as features downstream.
- **Cold-start strategies:** new users → popularity/context/onboarding signals; new items → content features; gradually shift to CF as interactions accrue.
- **Real-time personalization:** session/context features at request time; feature store for low-latency lookups (see mlops.md); precompute candidates, rank online.
- **Evaluation:** offline ranking metrics (NDCG, Recall@k, MAP, hit rate) + diversity/coverage/novelty; **validate online with A/B tests** (see experimentation.md) — offline gains often don't transfer. Beware feedback loops (the system shapes the data it learns from) and popularity bias.
- **Use cases:** product/content recommendations, NBO, search ranking, "people you may know," cross-sell.
- **Key points:** retrieval+ranking is the scalability pattern; cold-start is the hardest real problem; offline metrics guide, online A/B decides; feedback loops + popularity bias are the silent failure modes.
