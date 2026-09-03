# 2026-W34 Sol review — Screening granularity after Discovery acceptance

Status: `RECOVERY_REQUIRED_BEFORE_SCREENING`

Issue: `2026-W34`  
Reviewed branch: `weekly/2026-W34-v2-work`  
Reviewed HEAD: `2a5950357158bece3278be3ea39e289cf1691108`  
Production State: `DISCOVERY_COLLECTED / stage:screening`

Decision / finding ID: `SOL-W34-SCREENING-GRANULARITY-20260903-R1`

## 1. What passed

The formal Discovery advancement is valid and must remain immutable historical provenance:

- lifecycle advanced from `ISSUE_INITIALIZED` to `DISCOVERY_COLLECTED` through the Core operator bridge;
- Discovery checkpoint is `passed`;
- accepted Discovery graph contains 40 unique Discovery records;
- the accepted graph preserves the Sol semantic baseline through 105/105 event traceability;
- DailyX remains 76/76 topics across seven imported Raw files;
- corrected Weekly Grok r2 remains 47/47 URLs with 10 `ORDINARY_WINDOW` / 20 `BACKGROUND_ONLY` / 17 `LATE_BREAKING`;
- current accepted X binding is valid;
- accepted Discovery Raw/provenance is not to be rewritten, deleted, or retroactively replaced.

This finding does **not** invalidate the formal Discovery checkpoint.

## 2. Blocking downstream granularity defect

Independent Sol review of the actual current-Core downstream code found that the accepted 40-record source/provenance graph is too coarse for the semantic unit required by Screening and Evidence.

The key current-Core behavior is:

- `scripts/survey_screening_v2.py` emits exactly one Screening decision for every supplied Discovery record;
- `scripts/survey_evidence_v2.py` creates one Evidence Task for each non-`DROP` Discovery ID;
- each Evidence Task is required to bind exactly one Discovery ID.

The accepted graph includes source-level aggregate records such as:

- one Sol working-set Discovery record representing all 105 event identities;
- one Discovery record per DailyX daily file rather than per event/topic;
- a dedicated aggregate Grok ledger Discovery record.

If Screening were run directly on those 40 records, semantically independent developments such as GLM-5.3, Claude watermarking, OpenRouter/Stripe, AgentCore Payments, Pika Audio, Mistral Agentic Search, DeepSeek-V4-Flash-Vision-Exp, Ray KEV, Slack Code, LFM2.5-DSpark, and the remaining W34 event identities could not receive independent `KEEP / MAYBE / DROP / INSPECT` decisions and independent Evidence Tasks.

That would collapse event-level Screening, verification targets, materiality, and later Candidate Selection into source-container decisions. This is not acceptable for W34 editorial/research semantics.

## 3. Why rollback or accepted-artifact rewriting is not the recovery path

Current Core `scripts/survey_production_v2.py::transition_state()` is strictly monotonic and requires exactly one forward lifecycle step. There is no supported `DISCOVERY_COLLECTED -> ISSUE_INITIALIZED` rollback/reopen transition.

Therefore do not:

- edit or replace `sources/2026-W34/discovery/discovery-accepted-v2.json`;
- rewrite `sources/2026-W34/orchestration/v2/checkpoints/ISSUE_INITIALIZED.json`;
- reset Production State;
- delete the accepted 40-record graph;
- create history-rewriting repair branches;
- modify shared Core to add a W34-specific rollback.

The accepted 40-record graph remains the immutable Discovery checkpoint basis.

## 4. Supported recovery mechanism

Current Core Screening preparation explicitly permits state `DISCOVERY_COLLECTED` and accepts a caller-supplied valid Discovery set as its Screening basis.

Current Core Evidence then validates and follows the exact Discovery set pinned by the accepted Screening package, rather than assuming that every downstream Screening record must be identical to the earlier source-centric Discovery acceptance graph.

Therefore W34 should recover by creating an **event-level Screening Discovery expansion set** derived from the immutable accepted Discovery graph and the Sol 105-event inventory.

This expansion set is downstream preparation material. It does not replace the accepted Discovery checkpoint.

## 5. Required event-level expansion semantics

The Screening Discovery expansion set must:

- account for every `W34-C001` through `W34-C105` exactly once at event identity level;
- use one event-level Discovery ID per Sol event identity unless an event truly requires multiple source records; the default is one record per event;
- preserve the existing event title, lane, pre-Screening status, boundary/authority qualifier, and next-verification intent from `sources/2026-W34/intake/working-set/sol-discovery-event-inventory-v0.2.md`;
- bind each event record to one or more existing Raw/provenance paths that actually support the existence of the Discovery signal;
- retain source authority boundaries: X/community observations are discovery signals, not publication-grade technical Evidence;
- retain pre-window/post-cutoff/context records rather than silently deleting them; their Screening decision may later be `DROP`, `MAYBE`, `INSPECT`, or contextually `KEEP`;
- preserve carry-over traceability;
- preserve DailyX and Grok independent attribution;
- preserve all known chronology and authority gaps.

The event-level set must not perform Screening itself. Existing working labels such as `KEEP_CANDIDATE`, `KEEP_CONTEXT`, `BOUNDARY_PRE_WINDOW`, `BOUNDARY_POST_CUTOFF`, and `AUTHORITY_VERIFY` are pre-Screening traceability labels, not Core Screening decisions.

## 6. Provenance relationship to accepted Discovery

Every event-level expansion record must be traceable to the immutable accepted 40-record graph.

Use valid Core provenance fields. Where an event is derived from an accepted aggregate Discovery record, prefer a provenance relationship such as `REFERENCE_EXPANSION` or another current-Core-valid expansion origin with explicit `parent_refs` naming the accepted Discovery ID(s) from which the event-level record is expanded.

Do not invent parent IDs. Parent refs must name actual accepted Discovery IDs or explicit external refs allowed by the current contract.

Maintain a deterministic crosswalk with at least:

- `event_id` (`W34-C001` ... `W34-C105`);
- new event-level `discovery_id`;
- accepted parent Discovery ID(s);
- Raw path(s);
- source locator;
- chronology/boundary qualifier;
- authority qualifier;
- short expansion rationale.

## 7. Core validation required before Screening

Before any Screening decisions are produced, the event-level expansion set must pass the actual current-Core validator:

- `scripts.survey_screening_v2.validate_discovery_set()` / CLI `validate-discovery` equivalent;
- actual `scripts.survey_screening_v2.prepare_package()` to a temporary or edition-local non-accepted package location using current `sources/2026-W34/production-state.json`;
- package input record count must equal the event-level expansion record count;
- every input event-level Discovery ID must be unique;
- no current Core/shared contract files may be modified to make validation pass.

The prepared Screening package is only a validation artifact in this bounded recovery task. Do not create Screening result decisions and do not advance lifecycle.

## 8. Expected cardinality

The semantic target is 105 event identities.

The preferred Screening Discovery cardinality is therefore **105 records / 105 unique event-level Discovery IDs**.

If a strict schema/provenance reason makes a different record count necessary, do not silently choose a different count. Record the exact reason and stop with `NEEDS_SOL_REVIEW` before Screening.

## 9. Lifecycle boundary

During this recovery task:

- Production State remains `DISCOVERY_COLLECTED`;
- next action remains `stage:screening`;
- Discovery checkpoint remains passed and immutable;
- Screening checkpoint remains pending;
- no Screening acceptance is created;
- no Evidence Task is created;
- no Materiality/Completeness/Selection/Architecture work is performed;
- no Human Gate is resolved.

After Luna returns the validated event-level expansion set, Sol will independently review the 105 records and then perform/authorize semantic Screening on those event-level records.

## 10. Correction to the earlier Sol completeness materialization assumption

`SOL-W34-DISCOVERY-COMPLETENESS-20260903-R1` correctly fixed the 105-event semantic scope, but its allowance for many-to-one event-to-Discovery materialization was too permissive for the actual downstream Screening/Evidence cardinality contract.

This finding narrows that earlier assumption without changing the semantic completeness decision or invalidating the accepted Discovery checkpoint:

- source-centric many-to-one materialization remains valid as immutable Discovery checkpoint provenance;
- downstream Screening must recover event-level granularity through an explicit expansion set before any Screening decision is accepted.
