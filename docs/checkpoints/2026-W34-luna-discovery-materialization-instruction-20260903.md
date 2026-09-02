# 2026-W34 — Luna Discovery Raw Materialization Instruction

Status: **READY_FOR_LUNA / BOUNDED DISCOVERY MATERIALIZATION ONLY**  
Date: `2026-09-03` JST  
Repository: `eariver/japanese-generative-ai-survey`  
Canonical work branch: `weekly/2026-W34-v2-work`  
Reviewed main authority: `c7a898889463b049dea4ee7337ee16ad5fbf3191`  
Current lifecycle before this task: `ISSUE_INITIALIZED`  
Current next action before this task: `stage:discovery`  
Requested worker endpoint: **schema-valid Raw-backed Discovery candidate for Sol review; no lifecycle advancement**

The caller supplies the Exact Starting SHA containing this instruction and the Sol decision below. Luna must start from that exact canonical-branch SHA.

Primary Sol decision authority for this task:

`sources/2026-W34/execution/decisions/sol-discovery-completeness-20260903-r1.md`

---

## 1. Objective

Materialize the Sol-approved W34 semantic Discovery baseline into a **Raw-backed Core-v2 Discovery candidate**.

This task is not a new broad Discovery search. Sol has already accepted semantic Discovery completeness for the 105-event working set.

The worker must:

1. preserve all 105 event identities and their existing boundaries;
2. make the source observations needed by the Discovery graph durable and Raw-backed;
3. import the seven DailyX W34 observation files as exact immutable source observations;
4. reuse the already imported corrected Weekly Grok r2 Raw without mutation;
5. reuse existing canonical GitHub Releases Raw without mutation;
6. create bounded source-local captures for non-X / primary-source observations that still need a Discovery Raw dependency;
7. construct schema-valid `sources/2026-W34/discovery/discovery-v2.jsonl`;
8. create an explicit 105-event → Discovery-record crosswalk;
9. validate that a Core Discovery acceptance package can be built **without committing it**;
10. stop for Sol review.

Do **not** execute `stage:discovery`, do not commit `discovery-accepted-v2.json`, and do not modify `production-state.json`.

---

## 2. Start guard — mandatory before any write

Before writing anything:

1. read remote `refs/heads/weekly/2026-W34-v2-work`;
2. compare it with the Exact Starting SHA supplied by Sol with this instruction;
3. verify reviewed `main` is still `c7a898889463b049dea4ee7337ee16ad5fbf3191` or, if it moved, inspect the movement and do not silently adopt new Core authority into this already-pinned task;
4. verify the Sol decision file above exists at the Exact Starting SHA.

If the canonical work-branch HEAD differs from the Exact Starting SHA:

- perform no repository/content writes;
- do not create another branch;
- report actual HEAD and stop.

No force/reset/rewrite/rebase.

---

## 3. Mandatory read order

Read before materialization:

1. `AGENTS.md` from reviewed main;
2. `docs/survey-production-core-v2-session-bootstrap.md`;
3. `docs/survey-production-core-v2-authority.md`;
4. `docs/survey-production-core-v2-postintegration-amendment.md`;
5. `docs/survey-production-core-v2-x-source-intake.md`;
6. `docs/survey-production-core-v2-execution-record-policy.md`;
7. `docs/survey-production-core-v2-operator-execution-bridge.md`;
8. `schemas/survey-discovery-record.schema.json`;
9. `schemas/discovery-acceptance-v2.schema.json`;
10. `scripts/survey_discovery_v2.py`;
11. `scripts/survey_x_intake_v2.py`;
12. `sources/2026-W34/production-profile.json`;
13. `sources/2026-W34/production-state.json`;
14. `sources/2026-W34/raw-index.json`;
15. `sources/2026-W34/external/x/x-source-intake-v2.json`;
16. `sources/2026-W34/intake/discovery-readiness-v0.2.md`;
17. `sources/2026-W34/intake/discovery-traceability-v0.2.json`;
18. `sources/2026-W34/intake/working-set/sol-discovery-event-inventory-v0.2.md`;
19. `sources/2026-W34/intake/working-set/dailyx-candidate-crosswalk-v0.1.md`;
20. `sources/2026-W34/intake/working-set/grok-r2-candidate-crosswalk-v0.1.md`;
21. `sources/2026-W34/execution/handoffs/w34-luna-sol-completeness-handoff-20260902-r1.md`;
22. `sources/2026-W34/execution/decisions/sol-discovery-completeness-20260903-r1.md`.

Repository/Core authority outranks this instruction on syntax and invariant conflicts. The Sol decision freezes semantic scope, not Core syntax.

---

## 4. Frozen semantic baseline

The following accounting is mandatory and must not shrink because Luna considers an item unimportant:

- Sol event-level inventory: **105/105** (`W34-C001` through `W34-C105`);
- DailyX topics: **76/76**;
- corrected Weekly Grok r2 URLs: **47/47**;
- corrected Grok classifications: **10 `ORDINARY_WINDOW` / 20 `BACKGROUND_ONLY` / 17 `LATE_BREAKING`**;
- carry-over obligations: **1/1**, currently `RECHECKED_UNRESOLVED`;
- existing GitHub Releases Raw: **7 immutable repository response objects**, five in-window matches.

The 105 event identities are a semantic coverage baseline, not a mandate that the Discovery JSONL contain exactly 105 records.

Discovery is source/provenance-centric. Multiple event IDs may map to one Discovery record, and one event may map to multiple Discovery records. Every event ID must nevertheless remain explicitly traceable.

Do not silently remove:

- background events;
- pre-window base events used to explain an in-window delta;
- Late Breaking events;
- context records;
- chronology-verify records;
- authority-gap records;
- low-materiality-looking records.

Those are Screening/Materiality concerns downstream.

---

## 5. Existing Raw that must be reused, not rewritten

### 5.1 Weekly Grok r2

Reuse the current edition-local corrected r2 artifacts under:

`sources/2026-W34/external/x/weekly-x-2026-W34-r2/`

The post-level classification/count authority is:

`sources/2026-W34/external/x/weekly-x-2026-W34-r2/raw/x-url-ledger.corrected.tsv`

Preserve exactly:

- 47 unique URLs;
- 10 ordinary;
- 20 background;
- 17 late-breaking.

Do not use stale corrected narrative prose as count authority.

Do not modify any existing indexed Grok Raw object.

### 5.2 GitHub Releases

Reuse the seven existing canonical GitHub Releases Raw response objects already indexed for W34.

Do not rerun the broad GitHub collector merely to obtain different bytes unless current Core validation proves a required object is missing or corrupt.

Existing Raw is immutable.

---

## 6. DailyX exact observation import

DailyX is an independent high-recall X observation corpus. It must remain separately attributable from the Weekly Grok r2 run.

Google Drive root:

- folder name: `DailyX`
- folder ID: `1VVAqP1ylgywdrOfl2ghS9l00yiu7ThtY`

Collection policy:

- `DailyX_COLLECTION_POLICY.md`
- file ID: `1ojlz497AMiG7JGYWBrAXNjHhuhho3YgJ`

Import the exact available bytes for these seven W34 files:

1. `2026-08-16_0700.md` — `13pdu00Acu-iFpML2KbSxE-catIlreClG`
2. `2026-08-17_0700.md` — `1erwXcN9wO32p56FqY82O-WfG25He_2S6`
3. `2026-08-18_0700.md` — `18Bzcctb1ZDXPBq8diQaE5Dfj-f89fgr3`
4. `2026-08-19_0700.md` — `1frKEYDRhBgmrYwlvgTMU0f_wulTsCDY6`
5. `2026-08-20_0700.md` — `10KzzCppgIfXR9bye6fB4sayhGlR6GWut`
6. `2026-08-21_0700.md` — `1gPkwYYQz2SNnrgrc0ay6JxeTDzpj1xE_`
7. `2026-08-22_0700.md` — `1avn6m20KB6EEDSXCODwSRxGJXsxz60sn`

Recommended repository location unless current Core requires another edition-local external-source layout:

`sources/2026-W34/external/x/dailyx/raw/`

Also create an edition-local DailyX provenance/manifest record containing at minimum:

- Drive folder ID;
- policy file identity;
- each Drive file ID;
- source filename/title;
- observed/imported time;
- repository Raw path;
- SHA-256;
- byte count;
- statement that DailyX is `DISCOVERY_AND_COMMUNITY_SIGNAL_ONLY`.

If the Drive connector exposes exact stored bytes through a downloaded file reference, preserve those bytes without normalization. If the provider exports a native/converted text representation rather than original raw bytes, preserve the exact returned export as the durable observation and record the actual export/capture mode. Do not falsely call it the provider's original HTTP bytes.

DailyX is not required to be inserted into the existing required-Grok run inside `x-source-intake-v2.json` if current schema/policy does not support that cleanly. It may have a separate auxiliary provenance manifest. Do not invent a synthetic Grok task/run identity merely to fit the manifest.

---

## 7. Candidate-level source-local capture

The current 105-event working set contains events supported by first-party pages, model cards, repositories, research papers, official product/changelog pages, X observations, and some secondary discovery leads.

For events not already Raw-backed by existing Grok, DailyX, GitHub Releases, or another existing indexed Raw object, create bounded source-local captures under a dedicated run, preferably:

`sources/2026-W34/collectors/sol-approved-primary-gapfill/runs/w34-discovery-materialization-r1/raw/`

Use stable descriptive filenames.

### 7.1 Preferred capture source

For each event, prefer source classes in this order:

1. official vendor/project announcement or documentation;
2. official repository/release/model card;
3. original paper/technical report/authors' artifact;
4. authoritative first-party X post when no durable first-party page exists;
5. best available secondary discovery source only when a first-party source is genuinely unavailable/inaccessible.

Do not replace a stronger existing source with a weaker one.

### 7.2 Bounded source-local capture format

A bounded capture should contain enough provenance and source-local observation to back Discovery, without pretending to be a full page mirror.

At minimum include:

- capture schema/version or clear record header;
- issue ID;
- event ID(s) supported;
- source URL/locator;
- source publisher/project;
- source/page title;
- retrieval/observation timestamp;
- capture mode, e.g. `EXACT_RETURNED_BYTES`, `CONNECTED_SOURCE_EXPORT`, `BOUNDED_SOURCE_LOCAL_CAPTURE`, or an equivalent explicit mode;
- source publication/event date when explicitly supported;
- concise source-local observations needed for Discovery identity/chronology;
- authority boundary, including `AUTHORITY_GAP` where applicable.

If the execution surface returns parsed/extracted text rather than exact HTTP response bytes, do not claim exact HTTP preservation.

Technical claims in these captures remain unaccepted until Evidence review.

### 7.3 Do not force every event to obtain first-party technical Evidence now

This is Discovery materialization, not Evidence verification.

An event originally discovered only through X or a secondary report may remain Raw-backed by that observation if the primary source cannot be obtained during this task, provided:

- the Discovery record states the actual source class;
- the event→Discovery crosswalk preserves the `AUTHORITY_VERIFY` / `PRIMARY_VERIFY` / equivalent boundary;
- no unsupported technical fact is promoted;
- the missing primary authority is surfaced for Evidence.

Do not drop the event to make validation pass.

---

## 8. Collector retry failures remain historical facts

Do not rewrite or erase the prior arXiv/official-page retry records.

They accurately record:

- arXiv configured collector: `RETRY_REQUIRED`, Raw 0, blocked before HTTP;
- official-page configured collector: `RETRY_REQUIRED`, Raw 0, 22 configured page gaps, blocked before HTTP.

This materialization task may fetch/capture candidate-specific sources through other available execution surfaces. Candidate-specific source capture does not retroactively make those configured collector runs successful.

Do not rerun broad collectors unless current Core validation specifically requires it and the current task environment permits a genuinely canonical run.

---

## 9. Discovery graph construction

Create:

`sources/2026-W34/discovery/discovery-v2.jsonl`

Every line must validate under current `schemas/survey-discovery-record.schema.json`.

For each Discovery record:

- use a stable unique `discovery_id`;
- preserve source identity and actual provenance origin;
- assign `research_pass` consistently;
- use parent refs only when a real Discovery relation exists;
- use Weekly obligations supported by current Core and existing W34/W33 practice;
- set `source.collector_id` and `collector_run_id` to the actual source/capture run;
- set `source.locator` to the actual source locator;
- include at least one real `source.raw_paths` entry;
- keep chronology/boundary facts in metadata rather than redating events;
- never treat X agreement as technical verification.

Do not encode Screening or Selection decisions into Discovery records.

### 9.1 Event-to-Discovery traceability

Create an explicit machine-readable or clearly structured crosswalk, preferably:

`sources/2026-W34/discovery/event-discovery-crosswalk-v0.1.json`

It must account for every event ID `W34-C001` through `W34-C105`.

For each event include at minimum:

- event ID;
- mapped Discovery ID(s);
- mapping relationship;
- primary source class currently backing Discovery;
- relevant Raw path(s);
- retained status/boundary from the Sol working set;
- unresolved authority/chronology gap if any.

Validation target: **105/105 accounted, 0 silently dropped**.

---

## 10. Candidate Discovery acceptance validation — no commit of acceptance artifact

After the Discovery JSONL is complete, exercise current Core's Discovery acceptance builder/validator into a temporary non-repository location, or perform the documented equivalent no-lifecycle-write validation.

Validate at minimum:

1. `discovery-v2.jsonl` parses and validates;
2. every Discovery record has at least one existing Raw path;
3. every Raw path used by acceptance can produce a valid `{path, sha256, byte_count}` ref;
4. `x-source-intake-v2.json` still validates and remains `COMPLETE`;
5. corrected Grok URL set/counts remain 47 and 10/20/17;
6. DailyX seven source files are present and provenance-recorded;
7. event crosswalk is 105/105 with zero missing IDs;
8. one carry-over obligation remains represented;
9. existing indexed Raw is unchanged;
10. all newly created Raw is added intentionally to `raw-index.json` through current Core provenance tooling or equivalent deterministic generation;
11. Raw integrity check passes;
12. a temporary `discovery-accepted-v2.json` candidate can be generated and validates against `schemas/discovery-acceptance-v2.schema.json`;
13. the generated acceptance references the current `x-source-intake-v2.json` authority;
14. `production-state.json` bytes are unchanged from task start;
15. no shared-Core file changed.

Do **not** commit the temporary acceptance file.

Do **not** execute the stage advancement/operator request.

---

## 11. Write allowlist

Allowed writes are limited to edition-local Discovery materialization and execution records, including:

- `sources/2026-W34/discovery/discovery-v2.jsonl`
- `sources/2026-W34/discovery/event-discovery-crosswalk-v0.1.json`
- `sources/2026-W34/external/x/dailyx/**`
- `sources/2026-W34/collectors/sol-approved-primary-gapfill/runs/w34-discovery-materialization-r1/**`
- `sources/2026-W34/raw-index.json`
- `sources/2026-W34/execution/sessions/w34-luna-discovery-materialization-20260903-r1.md`
- `sources/2026-W34/execution/index.md`
- optional deterministic validation artifacts under `sources/2026-W34/execution/luna/w34-discovery-materialization-r1/**`

If current Core requires a narrowly different edition-local path for a manifest/provenance file, use that path and report it explicitly.

Forbidden writes include:

- `sources/2026-W34/production-state.json`
- `sources/2026-W34/discovery/discovery-accepted-v2.json`
- any stage checkpoint/provenance artifact that claims Discovery was accepted
- Screening outputs
- Evidence outputs
- Materiality/completeness outputs
- Selection outputs
- Architecture outputs
- reader-facing draft/publication outputs
- Human Gate decisions
- W33 files
- shared Core roots: `AGENTS.md`, `config/`, `schemas/`, `scripts/`, `.github/workflows/`, `docs/survey-production-core-v2-*.md`

Do not create a new branch.

---

## 12. Execution records and crash recovery

Create/update edition-local execution records according to current policy.

The session record must capture:

- Exact Starting SHA;
- reviewed main pin;
- Sol decision ID/path;
- DailyX import identities;
- existing Grok/GitHub Raw reused;
- source-local capture run identity;
- Discovery record count;
- 105-event crosswalk result;
- Raw-index/integrity result;
- temporary acceptance validation result;
- deviations, blocked sources, and unresolved authority gaps;
- ending commit/branch SHA when known;
- explicit statement that lifecycle advancement was not performed.

Do not turn Markdown work records into an alternative state machine.

---

## 13. Stop conditions

### Normal successful stop

Stop when all of the following are true:

- a schema-valid Raw-backed `discovery-v2.jsonl` is committed;
- 105/105 event identities are accounted in the event crosswalk;
- DailyX seven files are durably imported/provenance-recorded;
- existing Grok and GitHub Raw remain immutable;
- new Raw dependencies are indexed;
- Raw integrity passes;
- temporary Discovery acceptance build/validation passes;
- Production State remains `ISSUE_INITIALIZED` / `stage:discovery`.

Return the candidate commit to Sol for semantic/provenance review.

### Blocking stop

If one or more event identities cannot be Raw-backed or mapped without violating source/provenance truth:

- do not silently delete them;
- do not weaken the 105/105 requirement;
- do not fabricate Raw;
- do not advance lifecycle;
- record the exact blocking event IDs, attempted source locators, failure mode, safe residual graph, and next action for Sol.

A failed candidate-specific source fetch is not by itself an Exception Gate if the original observation Raw can truthfully back the Discovery signal.

---

## 14. Required completion report

Report at minimum:

- branch;
- Exact Starting SHA;
- Ending SHA;
- start→end ahead / behind / commit count;
- exact changed paths;
- reviewed main pin;
- Production State/lifecycle/next action before and after;
- Discovery JSONL record count;
- unique Discovery ID count;
- event crosswalk `105/105` result;
- DailyX imported file count and exact repository paths;
- Grok 47/47 and 10/20/17 preservation result;
- existing GitHub Releases Raw immutability result;
- new source-local Raw/capture count;
- Raw-index update/integrity result;
- temporary Discovery acceptance validation PASS/FAIL;
- unresolved authority/chronology/capture gaps by event ID;
- carry-over status;
- explicit statement that no Screening/Evidence/Materiality/Selection/Architecture/Human Gate decision was made;
- explicit statement that `production-state.json` was unchanged and formal `DISCOVERY_COLLECTED` acceptance was not executed.

When this bounded materialization task is complete, stop for Sol review.
