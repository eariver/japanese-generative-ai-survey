# 2026-W34 — Luna Discovery Readiness Canonicalization Instruction

Status: **BOUNDED EXECUTION AUTHORITY FROM SOL**  
Date: 2026-09-03 JST  
Repository: `eariver/japanese-generative-ai-survey`  
Canonical work branch: `weekly/2026-W34-v2-work`  
Reviewed main baseline at W34 initialization: `c7a898889463b049dea4ee7337ee16ad5fbf3191`  
Pre-instruction branch authority: `ed05b69f75a0f8421018f9f3196bc1641a04ef3b`  
Requested boundary: **canonicalize the completed Sol/X discovery working set, retry remaining canonical non-X collectors, close the prior bounded intake handoff accurately, and stop before formal Discovery acceptance / Screening.**

The Exact Starting SHA for the Luna run is the commit containing this instruction and will be supplied separately by Sol. Treat it as mandatory input.

---

## 1. Mission

Continue `2026-W34` from the existing initialized edition. Do **not** reinitialize the issue and do not replay the initial assignment from scratch.

This assignment has four purposes:

1. consume and preserve the completed Sol-side discovery working set and X traceability records;
2. retry the previously blocked canonical arXiv and official-page collector/capture gaps using the current execution surface;
3. convert the discovery working set into durable **edition-local pre-Screening intake/readiness records** without silently dropping observations;
4. leave a closed, precise handoff to Sol identifying whether Source Intake appears ready for Sol's independent completeness judgment.

Even if all intake preconditions appear satisfied, **do not perform `ISSUE_INITIALIZED -> DISCOVERY_COLLECTED` acceptance in this assignment.** Sol owns the final completeness/disposition judgment after reviewing the canonicalized results.

Do not proceed to Screening, Evidence, Candidate Selection, Architecture, drafting, Freeze, or Release.

---

## 2. Mandatory start guard

Before any repository write:

1. read remote `refs/heads/weekly/2026-W34-v2-work`;
2. compare it byte-for-byte to the Exact Starting SHA supplied by Sol;
3. if it differs, perform **no GitHub writes**, create no alternate branch, report the actual HEAD, and stop;
4. inspect current `main` movement relative to the reviewed baseline `c7a898889463b049dea4ee7337ee16ad5fbf3191`; do not silently substitute a newer shared-Core authority into the already-initialized W34 edition.

No force, reset, rebase, rewrite, revert-as-repair, fallback branch, repair branch, or review branch.

---

## 3. Mandatory read order

Read repository authority first. At minimum:

1. `AGENTS.md`
2. `docs/survey-production-core-v2-session-bootstrap.md`
3. `docs/survey-production-core-v2-authority.md`
4. `docs/survey-production-core-v2-postintegration-amendment.md`
5. `docs/survey-production-core-v2-issue-prevention-checklist.md`
6. `docs/survey-production-core-v2-x-source-intake.md`
7. `docs/survey-production-core-v2-execution-record-policy.md`
8. `docs/survey-production-core-v2-operator-execution-bridge.md`
9. `docs/weekly-pipeline-operations.md`
10. `docs/weekly-carryover-policy.md`
11. `docs/checkpoints/2026-W34-luna-initial-instruction-20260902.md`
12. current W34 `production-profile.json`, `production-state.json`, `raw-index.json`, `source-intake-report.json`
13. all current `sources/2026-W34/intake/`, `collectors/`, `carryover/`, and `execution/` records needed to understand the existing handoff

Repository authority outranks this instruction if a stricter invariant exists.

Shared-Core denylist remains read-only:

```text
AGENTS.md
config/
schemas/
scripts/
.github/workflows/
docs/survey-production-core-v2-*.md
```

---

## 4. Existing W34 state that must be preserved

The current edition is already initialized and must not be reinitialized.

Expected state before this run:

- lifecycle remains `ISSUE_INITIALIZED`;
- `next_action` remains Discovery-oriented;
- Weekly window is `[2026-08-14T18:00:00-04:00, 2026-08-21T18:00:00-04:00)` = `[2026-08-14T22:00:00Z, 2026-08-21T22:00:00Z)`;
- canonical GitHub Releases Raw already exists for 7 configured repositories and must remain immutable;
- prior broad non-X manual intake exists under `sources/2026-W34/intake/`;
- W33 carry-over recheck is already recorded and must not be promoted merely to close bookkeeping;
- arXiv canonical Raw and configured official-page canonical Raw were previously `RETRY_REQUIRED` because the prior execution surface could not fetch them canonically.

Validate these facts from the repository instead of trusting this summary.

---

## 5. Sol working-set handoff — read-only external inputs

The following Google Drive records are **temporary / non-canonical Sol working records**. They are execution inputs, not lifecycle authority and not final Selection.

### 5.1 Sol event-level Discovery inventory

Google Doc:

- title: `W34_Sol_Discovery_Candidate_Inventory_v0.2`
- file ID: `1PeshezfNyePL9idRF6jgZrqweTzQLIGT0V9iNCIzxnI`
- folder: `Sol_Primary_Source_Temp`
- folder ID: `1BeQ_fyayfwVhwJyxbdPJfqfAXb_LOKHT`

Current validated summary from Sol:

- total event-level records: **105**;
- this is intentionally pre-Screening and includes candidates, context, boundary items, chronology/authority gaps, and research-screen items;
- no item may be silently deleted merely because Luna considers it low-materiality;
- event identity may be merged only if source-observation traceability remains explicit.

### 5.2 DailyX traceability crosswalk

Google Doc:

- title: `W34_DailyX_Candidate_Crosswalk_v0.1`
- file ID: `1bVvtBHLKd6vsi3uUqPXa6zBITIFFLCWl2usYHrBNUP4`

Validated by Sol:

- DailyX W34 files: 7;
- topic records: **76**;
- mapped to event inventory: **76/76**;
- unmapped: **0**;
- DailyX exact X URLs observed across the seven files: **99 unique**;
- Sol post-ID/time recheck: **98 ordinary-window / 1 pre-window**.

DailyX is a supplemental independent X observation corpus. It does **not** replace the required Weekly Grok run and does not become technical Evidence by agreement with Grok.

### 5.3 Weekly Grok r2 corrected post-level record

Run folder:

- `Grok_X_SourseIntake/Weekly/2026-W34/weekly-x-2026-W34-r2`
- folder ID: `1yXFesy7SBAbpCy1YXvil1C5-qdDFDeIe`

Original task:

- `grok-task.md`
- file ID: `1pcf1_Dz_ggjmGJLsWkKdgbaaDZVYbhsU9D8j61Vm7cY`

Original output files must be preserved as historical Raw but **must not be used for window counts** because the original classification was wrong:

- `grok-x-result.md` — `1Q-Y3Em0pLDLgD1Sve3JEizWqgFK4-TWf`
- `x-url-ledger.tsv` — `1qqqVw8Q--uDcs2yQ92TO8eulVRIN_psK`
- `search-accounting.md` — `1LrfzGKk4-NUwUAy1aVMRf5dc0-KpxueV`

Correction artifacts:

- `grok-x-result.corrected.md` — `1r8t21hzif4_FxGRO1AP-j2WvneYgiCrh`
- `x-url-ledger.corrected.tsv` — `1c6kP4vam4-vY2zRr1ffkuWUCeWuYfJHC`
- `search-accounting.corrected.md` — `1K0x-nIhQ7NzpYiM5vYJmkNBqLkHl6oaj`
- `correction-report.md` — `1yLAVEIsl1xXjRCmaLTeiokh_zvMrnqZn`

Sol independently verified the **corrected ledger**:

- exact URL set preserved from original: **47/47**;
- URLs added: 0;
- URLs removed: 0;
- duplicate exact URLs: 0;
- only `window_status` changed in the correction;
- corrected classification: **10 `ORDINARY_WINDOW` / 20 `BACKGROUND_ONLY` / 17 `LATE_BREAKING`**;
- classification changed rows: 35;
- linked non-X primary URLs: 9 unique;
- corrected ledger timestamps satisfy the canonical UTC boundary.

Important: the corrected narrative report still contains some stale cluster prose inherited from r2. Therefore **`x-url-ledger.corrected.tsv` is the post-level classification/count authority for this handoff**, while the narrative report is supporting Raw context only.

### 5.4 Grok r2 candidate crosswalk

Google Doc:

- title: `W34_GrokR2_Candidate_Crosswalk_v0.1`
- file ID: `1DrW3rw01lG7EVlKyR51A7AW0uLFWkkajuZN8SIyDoRU`

Validated by Sol:

- corrected Grok r2 rows: **47**;
- mapped to event inventory: **47/47**;
- unmapped: **0**.

These two crosswalks are traceability inputs, not materiality decisions.

---

## 6. Task A — import/canonicalize the discovery traceability set

Using current Core rules, create/update **edition-local pre-Screening intake/readiness records** that let Sol trace every imported observation to:

- originating source layer (`DailyX`, Weekly Grok r2, Sol/non-X primary discovery, configured collector, carry-over, etc.);
- exact source URL where available;
- event-level inventory identity;
- chronology relation (`ORDINARY_WINDOW`, pre-window/background, post-cutoff/Late Breaking, date-only boundary, unresolved chronology);
- source class / authority class;
- whether canonical Raw bytes are present;
- any remaining primary-authority or chronology verification gap.

Do not convert the 105-event inventory into final Selection. Preserve its pre-Screening status semantics or map them to the current Core's equivalent intake vocabulary without changing meaning.

Do not silently discard DailyX or Grok rows because they duplicate a topic. Event/topic deduplication is allowed only if observation-level provenance remains recoverable.

For X material:

- treat X posts as Raw Observation/community signal;
- preserve exact X URLs and timestamps;
- do not use X-only benchmark/spec/license/release claims as technical Evidence;
- preserve the distinction between base events outside the window and genuine W34 adoption/pricing/integration/safety deltas.

If the Core defines a canonical X import/manifest path, use it. If not, do not invent a fake lifecycle artifact; retain edition-local intake/traceability records and report the gap.

---

## 7. Task B — retry canonical arXiv and official-page capture

Retry the previously blocked collectors using the current execution surface.

### arXiv

- execute the configured canonical arXiv collector/query set;
- preserve the response bytes exactly as current Core requires;
- update Raw index/provenance only through the canonical path;
- do not substitute manual `arxiv.org/abs/...` locators for canonical collector Raw;
- if outbound access still prevents canonical capture, preserve the failure and keep `RETRY_REQUIRED` with exact diagnostics.

### configured official pages

- retry the configured official-page snapshot collector;
- preserve canonical HTML/response bytes and provenance as Core requires;
- do not mutate already indexed immutable Raw;
- if some pages are dynamic/unreachable, record per-source failure rather than claiming collector completeness.

### Sol-discovered first-party sources

The 105-event working inventory contains additional first-party pages/repos/model cards/papers beyond the original configured collector set. Where current Core permits candidate-level primary capture, capture those primary sources canonically or create explicit primary-capture gaps.

Do not force every source into a configured collector if it belongs in candidate-specific Raw/provenance instead.

---

## 8. Task C — completeness/readiness audit without Screening

After import and collector retry, produce an edition-local readiness audit that answers, by technical lane:

- which event/source families are represented;
- which have canonical primary Raw;
- which are X/community-only and still need first-party verification;
- which are pre-window boundary/context;
- which are post-cutoff/Late Breaking;
- which chronology/authority gaps remain;
- which lanes are quiet after actual search rather than merely absent from collector output.

The audit must explicitly account for the Sol inventory total and both X crosswalks. At minimum verify:

- Sol event records accounted for: 105/105, or list every unmapped record;
- DailyX topic records accounted for: 76/76, or list every unmapped topic;
- corrected Grok r2 rows accounted for: 47/47, or list every unmapped exact URL;
- corrected Grok ordinary/background/Late Breaking counts remain 10/20/17 unless an actual source-data defect is proven;
- no event is dropped solely by a Luna materiality judgment.

This is a **readiness/completeness audit**, not Screening acceptance.

---

## 9. Task D — reconcile execution records and close this bounded session

Create a new W34 execution session record under the current execution-record policy and update `sources/2026-W34/execution/index.md` as appropriate.

The previous initial intake session was left historically `IN_PROGRESS`. Do not rewrite history inaccurately. Inspect the current policy:

- if it permits a factual closure/supersession annotation, close or annotate the prior handoff with the actual bounded end at `ed05b69f75a0f8421018f9f3196bc1641a04ef3b`;
- otherwise leave the historical record intact and create an explicit new closure/handoff record that references it.

The new session must finish with a real terminal status for **this bounded assignment** and enumerate remaining gaps. Do not invent a second lifecycle state machine in Markdown.

---

## 10. Write boundary

Writes are limited to:

- edition-local `sources/2026-W34/**` files required by current Core for Raw/provenance/intake/collector/readiness/execution records;
- no production-state lifecycle advance;
- no shared-Core modification;
- no W33 modification;
- no final Selection/Architecture/publication artifacts.

This Sol instruction file itself already exists before Luna starts and must not be edited by Luna.

If a required canonical tool would modify a shared-Core path, stop that operation and record the defect/gap instead.

---

## 11. Explicit non-goals / prohibitions

Do not:

- reinitialize W34;
- perform formal `DISCOVERY_COLLECTED` acceptance;
- perform Screening or Evidence acceptance;
- establish final Candidate Selection;
- decide final materiality on Sol's behalf;
- write Architecture or reader-facing article prose;
- create Publication Preview;
- Freeze or Release;
- create any branch;
- force/reset/rewrite/rebase history;
- modify shared Core;
- treat X agreement as technical verification;
- treat the stale corrected narrative prose as post-level classification authority;
- silently delete a Sol/DailyX/Grok observation because it appears unimportant.

---

## 12. Validation before stop

Before the final completion report:

1. re-read the remote W34 branch HEAD and prove all commits are descendants of the Exact Starting SHA;
2. verify no new branch exists;
3. compare start→end and list every changed path;
4. verify all changed production paths are inside `sources/2026-W34/**`;
5. verify shared-Core denylist paths are unchanged;
6. validate Production Profile/State without advancing lifecycle;
7. validate Raw index/provenance integrity for every newly imported canonical Raw object;
8. prove immutable pre-existing Raw was not mutated;
9. verify Sol inventory mapping count;
10. verify DailyX 76/76 traceability;
11. verify Grok r2 corrected 47/47 traceability and 10/20/17 window counts;
12. report arXiv collector status and official-page collector status separately;
13. verify carry-over ledger remains represented;
14. explicitly prove formal Discovery acceptance was not executed.

---

## 13. Stop condition and completion report

Stop when the bounded canonicalization/retry/readiness audit is complete.

Report exactly:

- Exact Starting SHA;
- Ending SHA;
- start→end ahead/behind/commit count;
- changed paths;
- Production State/lifecycle/next action;
- W34 canonical window;
- arXiv canonical collector result and Raw count;
- configured official-page canonical collector result and Raw count;
- GitHub Releases Raw status (must remain immutable);
- Sol 105-event mapping result;
- DailyX 76-topic mapping result;
- corrected Grok r2 47-URL mapping result and 10/20/17 classification counts;
- new canonical Raw/provenance objects created;
- remaining authority/chronology/capture gaps;
- carry-over status;
- whether Source Intake appears technically ready for **Sol's independent completeness judgment**;
- explicit statement that no Screening, Selection, Architecture, or formal Discovery acceptance was performed.

If Source Intake appears ready, stop and hand control to Sol. Do not advance the lifecycle yourself.
