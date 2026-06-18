---
name: analytics-engineering
description: Implementation expertise for KPI design, metrics frameworks, dashboard architecture, BI modeling, and reporting strategy.
use_when: A workflow stage produces metrics, dashboards, reports, or BI models and needs methodology.
---

# Analytics Engineering — Expertise Module

Load this when building metrics, dashboards, or reporting layers. `claude.md` owns the workflow; this module supplies the how.

## KPI design
- A good KPI is specific, measurable, tied to a business objective, and actionable. Define numerator, denominator, grain, and time window precisely.
- Distinguish leading (predictive) from lagging (outcome) indicators. Avoid vanity metrics with no decision attached.

## Metrics frameworks
- Define metrics once in a single source of truth (semantic/metrics layer); never let the same metric drift across reports.
- Document each metric's definition, owner, filters, and known caveats. Separate base metrics from derived/ratio metrics.

## Dashboard architecture
- Lead with the headline question; arrange top-down (KPIs → trends → breakdowns → detail).
- One question per chart; pick chart type by intent (trend→line, comparison→bar, composition→stacked, relationship→scatter).
- Pre-aggregate for responsiveness; expose filters that map to real decisions.

## BI modeling
- Model for the consumer: conformed dimensions, consistent grain, pre-joined wide tables where it aids usability.
- Build curated marts on top of warehouse curated layer; keep business logic in the model, not the viz tool.

## Reporting strategies
- Match cadence and format to audience: executives→summary KPIs + narrative; analysts→drill-down + raw access.
- State assumptions, date ranges, and data freshness on every report. Automate refresh; flag staleness.

## Analytics engineering best practices
- Treat transformations as code: version control, tests, modular models (dbt-style), documentation.
- Test data: not-null, uniqueness, accepted-values, referential integrity. CI on model changes.
- DRY metric logic; reproducible, peer-reviewed pipelines over one-off SQL.

## Behavioral analytics patterns
Reusable analyses for understanding user/customer behavior over time.
- **Funnel analysis:** measure conversion through ordered stages; quantify step-to-step drop-off to locate friction. Define the funnel window and whether steps must be sequential; watch for users entering mid-funnel.
- **Cohort analysis:** group users by a shared start (signup month, acquisition channel) and track a metric over relative time. Separates *maturation* from *seasonality/mix shift* — a retention drop may be a worse recent cohort, not overall decline. Acquisition cohorts vs behavioral cohorts.
- **Customer segmentation:** rule-based (RFM, value tiers — transparent, actionable) vs unsupervised (k-means/hierarchical/GMM on behavioral features — discovers structure but needs interpretation). Standardize features; validate segments are stable, distinct, and actionable, not just statistically separable.
- **Use cases:** activation/onboarding optimization (funnel), retention diagnosis (cohort), targeting and personalization (segments).
- **Key points:** cohorts disentangle time-based confounds; funnels localize drop-off; segmentation is only useful if segments are actionable; pair descriptive findings with experimentation (see experimentation.md) before claiming causality.
