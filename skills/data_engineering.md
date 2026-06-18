---
name: data-engineering
description: Implementation expertise for ingestion, ETL/ELT, pipelines, data architecture, modeling, warehousing, storage formats, and lineage.
use_when: Workflow phases 1–2 (Data Source Discovery, Acquisition) or any pipeline/storage/architecture design needs technique.
---

# Data Engineering — Expertise Module

Load this when acquisition, pipeline, or storage design needs methodology. `claude.md` owns the discovery phase and approval gates; this module supplies the how.

## Data ingestion
- Confirm source type before coding — never assume CSV. Handle Excel, DB, API, cloud storage, warehouse, scraping per the source.
- Validate on ingest: row/file counts, schema, encoding, header correctness. Fail loudly on mismatch.
- Idempotent loads; checkpoint/restart for large or paged sources.

## ETL vs ELT
- ETL (transform before load) for constrained targets / heavy cleansing; ELT (load raw, transform in-warehouse) for cloud warehouses with cheap compute.
- Preserve an immutable raw landing zone regardless of pattern.

## Data pipelines
- Stages: extract → validate → transform → load → verify. Each stage logged and independently testable.
- Make steps deterministic and re-runnable; separate orchestration (Airflow/Prefect/Dagster) from transformation logic.
- Cache expensive intermediates (e.g., parquet) to avoid re-parsing source on every run.

## Data architecture
- Layered design: raw / staging / curated (medallion: bronze→silver→gold).
- Decouple storage from compute; document data contracts between producers and consumers.

## Data modeling
- OLTP → normalized (3NF); OLAP/analytics → dimensional (star/snowflake) with fact + dimension tables.
- Define grain explicitly per table; choose surrogate vs natural keys deliberately.

## Warehousing
- Snowflake/BigQuery/Redshift/Databricks: partition and cluster on common filter/join keys.
- Push heavy aggregation into the warehouse; avoid pulling raw rows to the client.

## Storage formats
- Columnar (Parquet/ORC) for analytics — compression + predicate pushdown. Avoid CSV for large intermediates.
- Match format to access pattern: row formats for record lookups, columnar for scans/aggregations.

## Data lineage
- Track source → transformation → output for every dataset; capture file locations and source systems.
- Version schemas; record transformation logic so outputs are reproducible and auditable.

## Streaming & event-driven architectures
- **Batch** (scheduled, high-throughput, simple) vs **streaming** (continuous, low-latency, complex). Choose by freshness requirement — don't stream what a nightly batch serves fine.
- **Event-driven:** producers emit events to a log/broker (Kafka, Kinesis, Pub/Sub); consumers react independently — decoupled, scalable, replayable.
- **Lambda** (parallel batch + speed layers, reconciled) vs **Kappa** (single streaming path, reprocess from the log) architectures. Kappa is simpler when the stream can replay history.
- Design for idempotency and exactly/at-least-once semantics; handle late/out-of-order events with watermarks and windowing.
- **Key point:** the real question is always latency-vs-complexity; reach for streaming only when freshness drives value (real-time personalization, fraud, monitoring).

## Customer data platforms & identity data architecture
- **CDP:** unifies customer data across sources into persistent, queryable profiles for analytics and activation. Core layers: ingestion → **identity resolution** (see domain_analysis.md) → unified profile store → segmentation → **activation**.
- **Customer 360 store:** a profile keyed by a resolved entity ID, joining behavioral + transactional + demographic data; model the entity grain explicitly and keep source-level detail for traceability.
- **Identity data models:** maintain a mapping of source keys → canonical entity ID (an identity graph / xref table) so any record resolves to the master entity; version it as identities merge/split.
- **Audience activation pipelines:** translate segments/scores into actions in downstream channels (ad platforms, email, CRM) — reverse ETL. Handle suppression, consent/privacy flags, and sync latency.
- **Risks:** identity changes ripple downstream (a merge re-keys history); privacy/consent must propagate to activation; profile staleness vs cost of real-time updates.

## Feature stores
- Central registry of curated features with **offline** (training, point-in-time correct) and **online** (low-latency serving) stores kept consistent.
- **Solves train/serve skew** — the same feature definition feeds both, preventing the #1 production ML bug. Enables reuse and discovery across teams/models.
- Point-in-time/"as-of" joins prevent label leakage in training. Weigh the operational overhead — justified at scale or with real-time models, overkill for a single batch model.
