# 2026-W34 Luna instruction — event-level Screening granularity expansion

Status: `READY_FOR_BOUNDED_LUNA_EXECUTION`

Issue: `2026-W34`  
Canonical branch: `weekly/2026-W34-v2-work`

## 1. Purpose

W34 has formally and validly reached:

- lifecycle: `DISCOVERY_COLLECTED`;
- next action: `stage:screening`;
- Discovery checkpoint: `passed`.

Do **not** reopen or rewrite Discovery acceptance.

Independent Sol review found a downstream granularity problem: the immutable accepted Discovery checkpoint is source/provenance-centric (40 records), while current Core Screening and Evidence operate one decision/task per Discovery ID. Running Screening directly on those 40 aggregate records would collapse 105 semantically distinct W34 events into source-container decisions.

The purpose of this bounded Luna task is to create and validate an **event-level Screening Discovery expansion set** with one independently screenable record for every Sol event identity `W34-C001` through `W34-C105`.

This task stops before any Screening decision is produced.

## 2. Mandatory authorities — read in order

1. `AGENTS.md`
2. `docs/survey-production-core-v2-session-bootstrap.md`
3. `sources/2026-W34/production-profile.json`
4. `sources/2026-W34/production-state.json`
5. `sources/2026-W34/orchestration/v2/checkpoints/ISSUE_INITIALIZED.json`
6. `sources/2026-W34/discovery/discovery-accepted-v2.json`
7. `sources/2026-W34/discovery/discovery-v2.jsonl`
8. `sources/2026-W34/discovery/event-discovery-crosswalk-v0.1.json`
9. `sources/2026-W34/intake/working-set/sol-discovery-event-inventory-v0.2.md`
10. `sources/2026-W34/intake/working-set/dailyx-candidate-crosswalk-v0.1.md`
11. `sources/2026-W34/intake/working-set/grok-r2-candidate-crosswalk-v0.1.md`
12. `sources/2026-W34/external/x/x-source-intake-v2.json`
13. `sources/2026-W34/execution/decisions/sol-discovery-completeness-20260903-r1.md`
14. `sources/2026-W34/execution/findings/sol-discovery-materialization-review-20260903-r1.md`
15. `sources/2026-W34/execution/findings/sol-screening-granularity-review-20260903-r1.md`
16. `config/prompts/source-screening-v2.md`
17. `scripts/survey_screening_v2.py`
18. `scripts/survey_evidence_v2.py`

The last Sol finding is the controlling authority for this task when an earlier W34 materialization assumption conflicts with downstream granularity needs.

## 3. Core facts that must remain unchanged

Preserve all of the following:

- accepted Discovery graph: 40 records / 40 unique IDs;
- accepted Discovery checkpoint and its exact bytes;
- Sol semantic scope: 105/105 events;
- DailyX: 7/7 files and 76/76 topic traceability;
- corrected Grok r2: 47/47 X URLs;
- Grok classification: 10 `ORDINARY_WINDOW` / 20 `BACKGROUND_ONLY` / 17 `LATE_BREAKING`;
- X manifest binding to `w34-grok-r2-corrected-47-url-ledger`;
- carry-over remains represented and unresolved unless an existing event-level record explicitly covers a later verified resolution; do not invent a resolution;
- existing canonical Raw and hashes;
- Production State `DISCOVERY_COLLECTED / stage:screening`.

## 4. No rollback and no accepted-artifact mutation

Current Core lifecycle is monotonic. There is no supported backward transition from `DISCOVERY_COLLECTED` to `ISSUE_INITIALIZED`.

Therefore this task must not modify:

- `sources/2026-W34/production-state.json`;
- `sources/2026-W34/discovery/discovery-accepted-v2.json`;
- `sources/2026-W34/orchestration/v2/checkpoints/ISSUE_INITIALIZED.json`;
- the accepted 40-record `sources/2026-W34/discovery/discovery-v2.jsonl`;
- existing Raw bytes referenced by accepted Discovery;
- shared Core scripts/config/schemas/prompts.

Do not reset, force-push, rewrite, rebase, or create another branch.

## 5. Required new event-level Screening Discovery set

Create a new edition-local Discovery JSONL dedicated to Screening input. Preferred path:

`sources/2026-W34/screening/input/event-discovery-v2.jsonl`

The target is:

- 105 records;
- 105 unique event-level Discovery IDs;
- exact accounting of `W34-C001` through `W34-C105`;
- no silently dropped event;
- no Core Screening decisions embedded in these records.

Use stable IDs that preserve the Sol event identity. Preferred convention:

- `w34-event-c001`
- ...
- `w34-event-c105`

If a different path-safe deterministic convention is required, use one convention for all 105 and record the mapping.

## 6. Event content source of truth

For each event, the semantic event identity comes from:

`sources/2026-W34/intake/working-set/sol-discovery-event-inventory-v0.2.md`

Preserve at least:

- event ID;
- event title;
- lane/scope context;
- pre-Screening status/qualifier;
- known chronology qualifier;
- known authority qualifier;
- next-verification intent.

Do not reinterpret a pre-Screening `KEEP_CANDIDATE` as Core `KEEP`. Do not reinterpret `BOUNDARY_PRE_WINDOW` or `BOUNDARY_POST_CUTOFF` as automatic Core `DROP`. Those decisions remain for Sol Screening.

## 7. Provenance expansion from accepted Discovery

Every event-level record must remain traceable to the immutable accepted Discovery graph.

Use a valid current-Core provenance origin. The default for event decomposition from an accepted aggregate record should be an expansion origin such as `REFERENCE_EXPANSION`, with non-empty `parent_refs` naming actual IDs from the accepted 40-record graph.

Examples of accepted-parent classes include, depending on the event:

- `w34-discovery-sol-event-baseline-v0_2`;
- the appropriate `w34-dailyx-YYYYMMDD-0700` record;
- `w34-grok-r2-corrected-47-url-ledger`;
- an existing canonical GitHub Releases record;
- an existing primary-gapfill Discovery record;
- the carry-over Discovery record.

A record may cite more than one parent when the event is independently observed by multiple accepted sources.

Do not invent parent IDs. Validate every parent against the accepted 40-record ID set before commit.

## 8. Source object and Raw binding

Each event-level record must satisfy the actual `scripts.survey_screening_v2` Discovery contract and include at least one existing Raw path.

Use the strongest already-available source-local basis for the event. Prefer:

1. candidate-specific first-party/primary Raw already materialized in W34;
2. canonical GitHub Releases Raw when it directly supports the event;
3. exact DailyX imported Raw for that event/topic;
4. corrected Grok imported Raw when that post/cluster supports the event;
5. the Sol event inventory working record as a traceability layer, but not as the sole publication-grade technical authority when a better Raw already exists.

`source.locator` should identify the event's best available source locator. `source.raw_paths` may contain multiple existing Raw paths when the event needs more than one source layer.

Do not create fake exact HTTP captures. Tool-extracted/reformatted text must not be described as original exact page bytes.

## 9. Event-level crosswalk

Create:

`sources/2026-W34/screening/input/event-discovery-crosswalk-v0.1.json`

It must account for all 105 events and contain, at minimum, for each event:

- `event_id`;
- `event_title`;
- `event_discovery_id`;
- `accepted_parent_discovery_ids`;
- `raw_paths`;
- `source_locator`;
- `pre_screening_status`;
- `chronology_qualifier`;
- `authority_qualifier`;
- `expansion_rationale`.

Validation summary must explicitly prove:

- 105 expected event IDs;
- 105 mapped event IDs;
- 0 missing;
- 0 duplicates;
- 105 unique event-level Discovery IDs;
- every parent ID exists in accepted 40-record Discovery;
- every Raw path exists.

## 10. Mechanical validation

Use the **actual current Core implementation** at the task starting SHA.

At minimum run equivalent of:

1. `scripts.survey_screening_v2.validate_discovery_set()` / `validate-discovery` against the new 105-record JSONL;
2. `scripts.survey_screening_v2.prepare_package()` using:
   - current `sources/2026-W34/production-state.json`;
   - the new event-level Discovery JSONL;
   - a new temporary or edition-local validation-only output directory;
   - current implementation SHA as required by Core;
3. inspect the generated package and prove:
   - input record count = 105;
   - package basis points at the event-level Discovery set, not the accepted 40-record graph;
   - all batch input IDs equal the 105 event-level Discovery IDs exactly;
   - state remains `DISCOVERY_COLLECTED`;
   - no Screening result files or acceptance were created.

Preferred validation record path:

`sources/2026-W34/execution/luna/w34-screening-granularity-expansion-r1/validation-v0.1.json`

Also write a concise session/worklog and handoff in the same bounded execution area or established W34 execution/checkpoint location.

## 11. Allowed writes

Writes are limited to new edition-local files required for this task under:

- `sources/2026-W34/screening/input/**`
- `sources/2026-W34/execution/luna/w34-screening-granularity-expansion-r1/**`
- one new task-specific checkpoint/handoff under `docs/checkpoints/**` if needed by current project convention.

Do not modify existing accepted Discovery, Raw, Production State, Core, W33, survey prose, Architecture, or publication artifacts.

## 12. Stop / exception rules

Stop with `NEEDS_SOL_REVIEW` and do not start Screening if any of these occurs:

- event-level record count cannot be 105 for a genuine schema/provenance reason;
- any `W34-C001` ... `W34-C105` cannot be mapped without inventing evidence/provenance;
- an accepted parent cannot be identified for an event;
- actual Core `validate_discovery_set` fails and a fix would require shared-Core modification;
- actual Core `prepare_package` fails because the state/contract forbids this post-Discovery expansion strategy;
- any existing accepted artifact would need to be edited to make the expansion work;
- remote branch HEAD changes unexpectedly during the task.

If a failure is a simple event-local mapping defect within the allowed new files, repair it and rerun validation. Do not broaden research unless the mapping cannot be made from existing W34 authorities.

## 13. Explicitly forbidden downstream work

Do not perform:

- actual Screening `KEEP/MAYBE/DROP/INSPECT` decisions;
- Screening acceptance;
- lifecycle advancement to `CANDIDATES_NORMALIZED`;
- Evidence package/task acceptance;
- primary technical Evidence conclusions;
- Materiality;
- Completeness judgment;
- Selection;
- Architecture;
- Human Gate decision;
- reader-facing drafting;
- Freeze or Release.

## 14. Required completion report

Report exactly enough for Sol to independently review:

- Exact Starting SHA;
- Ending SHA;
- start→end ahead / behind / commit count;
- all changed paths;
- Production State before / after;
- accepted 40-record Discovery SHA/record count unchanged confirmation;
- event-level Discovery path;
- event-level Discovery record count / unique ID count;
- `W34-C001`–`W34-C105` mapping: expected / mapped / missing / duplicate;
- accepted parent-ID validation result;
- Raw path existence result;
- DailyX traceability result;
- Grok 47/47 and 10/20/17 preservation result;
- carry-over preservation result;
- actual Core `validate_discovery_set` result;
- actual Core `prepare_package` result;
- prepared package record/batch counts and basis path;
- confirmation that no Screening results/acceptance were created;
- confirmation that Production State and accepted Discovery artifacts were not modified;
- unresolved authority/chronology/capture gaps;
- whether the 105-event set is ready for independent Sol Screening.

Stop after this report. Sol will review the event-level set and decide the actual Screening semantics in the next step.
