---
name: mlops
description: Implementation expertise for model deployment, monitoring, drift detection, experiment tracking, model versioning, and production ML systems.
use_when: A workflow stage moves a model toward production, or needs tracking, versioning, monitoring, or deployment.
---

# MLOps — Expertise Module

Load this when operationalizing models. `claude.md` owns the workflow and approval gates; this module supplies the how.

## Model deployment
- Patterns: batch (scheduled scoring), real-time (REST/gRPC), streaming, edge. Choose by latency and throughput needs.
- Package model + preprocessing as one artifact (the fitted pipeline) so train/serve transforms match exactly.
- Roll out safely: shadow → canary → full; keep rollback ready.

## Monitoring
- Track operational (latency, error rate, throughput) and model (prediction distribution, confidence, input stats) health.
- Alert on degradation; log inputs/outputs for audit and debugging. Capture ground truth when it arrives to measure live performance.

## Drift detection
- Data drift: input distribution shifts (PSI, KS test, population stability). Concept drift: input→target relationship changes (live metric decay).
- Set thresholds that trigger investigation/retraining; schedule periodic retrain or trigger on drift.

## Experiment tracking
- Log params, metrics, data version, code version, and artifacts per run (MLflow/W&B). Reproducibility = same data + code + seed.
- Make runs comparable and queryable; tag the candidate promoted to production.

## Model versioning
- Version models, data, and code together; maintain a registry with stage (staging/production/archived) and lineage.
- Record training data snapshot and feature definitions so any version can be reproduced or rolled back.

## Production ML systems
- Prevent train/serve skew with a shared feature pipeline (or feature store — see data_engineering.md).
- Automate the path: data validation → train → evaluate (gate) → register → deploy → monitor (CI/CD for ML).
- Define SLAs, retraining cadence, and human-in-the-loop checkpoints for high-stakes decisions.

## Online vs offline inference & the latency–freshness tradeoff
- **Offline/batch:** precompute predictions on a schedule, store, and look up at request time. Cheap, simple, no serving latency — but predictions are stale between runs. Good for slow-changing scores (LTV, segment, churn risk).
- **Online/real-time:** score on demand with request-time features. Fresh and context-aware — but adds latency, infra, and feature-serving complexity. Needed when the decision depends on in-session signals (real-time personalization, fraud).
- **The core tradeoff:** freshness vs latency vs cost. Many systems are **hybrid** — precompute heavy candidate generation offline, do light ranking/feature lookups online (pairs with the retrieval+ranking pattern in data_science.md).
- **Containerization & orchestration:** package serving in containers (Docker) for reproducible, scalable deploys (Kubernetes); orchestrate training/batch-scoring DAGs with Airflow/Prefect/Dagster. Keep environments pinned so train and serve match.
- **Key point:** "Pick offline unless an in-session signal changes the decision — then the latency/infra cost of online inference is justified; hybrid gets you both."
