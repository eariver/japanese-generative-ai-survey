# 2026-W34 Luna instruction — event-level Screening input byte-integrity repair

Status: `READY_FOR_BOUNDED_LUNA_EXECUTION`

Issue: `2026-W34`  
Canonical branch: `weekly/2026-W34-v2-work`

## 1. Purpose

The W34 event-level Screening expansion has already been semantically materialized and crosswalked at 105/105 events. The canonical agent-first Screening wrapper retry proved that the current Production State is valid, but package generation then failed because the committed `event-discovery-v2.jsonl` bytes are not valid UTF-8 JSONL.

This task repairs **only** that non-accepted edition-local Screening input artifact, proves its remote byte identity, and reruns canonical agent-first package preparation.

This task does not perform Screening decisions.

## 2. Mandatory read order

Read, in order:

1. `AGENTS.md`
2. `docs/survey-production-core-v2-session-bootstrap.md`
3. `sources/2026-W34/production-profile.json`
4. `sources/2026-W34/production-state.json`
5. `sources/2026-W34/discovery/discovery-accepted-v2.json`
6. `sources/2026-W34/discovery/discovery-v2.jsonl`
7. `sources/2026-W34/screening/input/event-discovery-crosswalk-v0.1.json`
8. `sources/2026-W34/intake/working-set/sol-discovery-event-inventory-v0.2.md`
9. `sources/2026-W34/execution/findings/sol-screening-granularity-review-20260903-r1.md`
10. `sources/2026-W34/execution/findings/sol-agent-first-screening-wrapper-review-20260903-r1.md`
11. `sources/2026-W34/execution/findings/sol-event-discovery-byte-integrity-review-20260904-r1.md`
12. `sources/2026-W34/execution/luna/w34-screening-granularity-expansion-r1/validation-v0.1.json`
13. `sources/2026-W34/execution/luna/w34-screening-agent-tool-retry-r1/validation-v0.1.json`
14. `scripts/survey_screening_v2.py`
15. `scripts/survey_agent_tool_v2.py`
16. `scripts/survey_agent_control_v2.py`
17. `config/prompts/source-screening-v2.md`
18. applicable current schemas referenced by those helpers

The Sol byte-integrity review is the controlling authority for this repair.

## 3. Starting facts

At the instruction-preparation point, the corrupted committed object was:

- path: `sources/2026-W34/screening/input/event-discovery-v2.jsonl`
- Git blob SHA: `20b394ea7bb0ca4cb32a90f31678d1045678255b`
- byte count: `210060`
- observed SHA-256: `a15ddbde1bc3b35ab158d68a50313294091aa33f2d942d2e24d3d578f5344321`
- UTF-8 parse: FAIL

The earlier local expansion validation recorded 105 records / 105 unique event Discovery IDs and historical local SHA-256 `5dbdcbfd70dc1e4605560dc06fc89e940141116b0bf9bf8eefaef6f8bf9f2332`.

Do **not** force the reconstructed file to match that historical SHA. It is diagnostic evidence only. Correctness is defined by the current crosswalk/authority and current Core validation.

The valid crosswalk remains:

`sources/2026-W34/screening/input/event-discovery-crosswalk-v0.1.json`

It contains 105 records and preserves, for each event:

- `event_id`
- `event_title`
- `event_discovery_id`
- `accepted_parent_discovery_ids`
- `raw_paths`
- `source_locator`
- `source_type`
- `lane`
- `pre_screening_status`
- `chronology_qualifier`
- `authority_qualifier`
- `expansion_rationale`
- `next_verification`
- source-layer / selected-parent metadata where present

## 4. Exact-start guard

Before any write:

1. fetch remote `weekly/2026-W34-v2-work` HEAD;
2. require exact equality with the Exact Starting SHA supplied in the user prompt;
3. if it differs, do not write anything and stop with actual HEAD;
4. do not create another branch.

Also record the current blob SHA of `event-discovery-v2.jsonl` before replacing it.

## 5. Reconstruction method

Do not salvage text from the corrupted file.

Rebuild a fresh event-level Discovery JSONL from the valid authorities, primarily the crosswalk.

For each of the 105 crosswalk rows, create exactly one valid current-Core Discovery record with:

- `discovery_id` = the row's `event_discovery_id`;
- event semantic identity preserved from `event_id` / `event_title` / lane / qualifiers;
- valid current-Core origin suitable for expansion from accepted Discovery, ordinarily `REFERENCE_EXPANSION` if still permitted by current contract;
- `parent_refs` = actual accepted parent Discovery IDs from `accepted_parent_discovery_ids`;
- source locator/type derived from the crosswalk row;
- `source.raw_paths` = the crosswalk row's existing Raw paths;
- no Screening decision embedded;
- no promotion of X/community observations to technical Evidence.

Preserve exact event-level cardinality:

- expected events = 105;
- mapped events = 105;
- unique `event_discovery_id` = 105;
- IDs exactly `w34-event-c001` through `w34-event-c105`;
- no missing;
- no duplicate;
- no silently dropped event.

If the current `survey_screening_v2` Discovery contract requires fields not literally stored in the crosswalk, derive them only from the existing Sol inventory, accepted parent Discovery, or current Core contract. Do not invent research conclusions.

## 6. Temporary candidate and pre-commit validation

Generate the repaired content first at a temporary local path outside the canonical target.

Before replacing the repository file, require all of the following:

1. file decodes as strict UTF-8;
2. each non-empty line parses as exactly one JSON object;
3. actual current `scripts.survey_screening_v2.validate_discovery_set()` PASS;
4. 105 records / 105 unique Discovery IDs;
5. crosswalk event accounting 105/105, missing 0, duplicate 0;
6. all parent IDs exist in accepted 40-record Discovery;
7. all referenced Raw paths exist;
8. DailyX/Grok/carry-over traceability unchanged;
9. compute temporary candidate SHA-256 and byte count.

Write these values to a new repair validation record as:

- `pre_commit_sha256`
- `pre_commit_byte_count`
- `pre_commit_utf8_jsonl_parse = PASS`
- `pre_commit_validate_discovery_set = PASS`

Preferred execution area:

`sources/2026-W34/execution/luna/w34-event-discovery-byte-repair-r1/`

## 7. Replace only the corrupted input

Replace in place:

`sources/2026-W34/screening/input/event-discovery-v2.jsonl`

Do not modify the crosswalk.

The repair commit may include:

- the repaired `event-discovery-v2.jsonl`;
- new validation/worklog/handoff records under the task execution area.

Do not include unrelated files.

## 8. Mandatory post-commit remote byte verification

This is the critical guard that was missing from the original materialization.

After the repair commit is pushed to the canonical branch:

1. fetch the new remote branch HEAD;
2. require it to equal the repair commit you just created;
3. retrieve the exact committed Git blob/raw bytes for `event-discovery-v2.jsonl` from that remote HEAD;
4. compute remote SHA-256 and byte count;
5. require:

```text
remote_sha256 == pre_commit_sha256
remote_byte_count == pre_commit_byte_count
```

6. decode the remote bytes as strict UTF-8;
7. parse all lines as JSON;
8. prove 105 records / 105 unique IDs;
9. use a fresh checkout/worktree at the exact remote HEAD and rerun actual current `validate_discovery_set()`.

Record:

- `post_commit_remote_sha256`
- `post_commit_remote_byte_count`
- `pre_post_sha256_equal`
- `pre_post_byte_count_equal`
- `remote_utf8_jsonl_parse`
- `remote_validate_discovery_set`

If any of these fail, stop `NEEDS_SOL_REVIEW`. Do not run Screening package preparation.

## 9. Canonical agent-first package preparation

Only after Section 8 is fully PASS, use the canonical wrapper:

`scripts/survey_agent_tool_v2.py`

with helper:

`scripts/survey_screening_v2.py`

and the exact current remote-HEAD implementation SHA.

Conceptually:

```bash
CURRENT_HEAD="$(git rev-parse HEAD)"

PYTHONPATH=. python3 scripts/survey_agent_tool_v2.py \
  --repo-root . \
  --state sources/2026-W34/production-state.json \
  --helper scripts/survey_screening_v2.py \
  -- \
  prepare \
  --state sources/2026-W34/production-state.json \
  --discovery sources/2026-W34/screening/input/event-discovery-v2.jsonl \
  --output-dir sources/2026-W34/screening/v2/prepared/w34-event-screening-r1 \
  --max-records 50 \
  --max-json-chars 120000 \
  --implementation-sha "$CURRENT_HEAD"
```

Equivalent invocation is allowed only if it still uses `survey_agent_tool_v2.py`.

Before helper execution, explicitly confirm `survey_agent_control_v2.validate_agent_state()` PASS.

## 10. Package validation

If package creation succeeds, validate at least:

- schema version `2.0-rc1`;
- issue `2026-W34`;
- research profile `WEEKLY`;
- `basis.discovery_path` points to the repaired event-level file;
- `basis.discovery_sha256` equals the remote committed repaired file SHA-256;
- input record count = 105;
- batch hashes/paths valid;
- union of batch Discovery IDs equals all 105 event-level IDs exactly;
- missing 0;
- duplicate 0;
- prompt hash valid;
- result-contract hash valid;
- Production State unchanged;
- accepted 40-record Discovery unchanged.

Prepared package outputs may be written under:

`sources/2026-W34/screening/v2/prepared/w34-event-screening-r1/**`

## 11. Allowed writes

Allowed writes are limited to:

- replacement of `sources/2026-W34/screening/input/event-discovery-v2.jsonl`;
- `sources/2026-W34/screening/v2/prepared/w34-event-screening-r1/**`;
- `sources/2026-W34/execution/luna/w34-event-discovery-byte-repair-r1/**`;
- one new task-specific checkpoint/handoff under `docs/checkpoints/**` only if current convention genuinely requires it.

## 12. Explicit prohibitions

Do not modify:

- `sources/2026-W34/production-state.json`;
- accepted Discovery JSONL;
- Discovery acceptance;
- Discovery checkpoint;
- `event-discovery-crosswalk-v0.1.json`;
- existing Raw;
- shared Core scripts/config/schemas/prompts;
- W33;
- reader-facing survey/draft/Architecture artifacts.

Do not perform:

- Screening `KEEP/MAYBE/DROP/INSPECT` decisions;
- Screening results;
- Screening acceptance;
- lifecycle advance to `CANDIDATES_NORMALIZED`;
- Evidence;
- Materiality;
- Completeness;
- Selection;
- Architecture;
- Human Gate decision;
- Freeze/Release;
- new broad research.

Do not use force/reset/rewrite/rebase or create another branch.

## 13. Stop rules

Stop `NEEDS_SOL_REVIEW` if:

- reconstruction cannot produce 105 valid event records from existing authorities;
- pre-commit validation fails;
- pre/post commit SHA or byte count differs;
- remote committed bytes do not parse as UTF-8 JSONL;
- remote `validate_discovery_set()` fails;
- canonical agent-first wrapper still fails;
- package basis does not bind the repaired remote file;
- any repair would require modifying accepted Discovery, Production State, shared Core, or event semantics.

Stop `READY_FOR_SOL_SCREENING` only when all byte-integrity, Core validation, and package checks pass.

## 14. Required completion report

Report:

- Exact Starting SHA;
- repair commit SHA;
- Ending SHA;
- start→end ahead / behind / commit count;
- all changed paths;
- corrupted blob SHA before repair;
- Production State before/after and byte-identity result;
- accepted Discovery unchanged result;
- crosswalk unchanged result;
- reconstructed record count / unique ID count;
- W34-C001–W34-C105 expected/mapped/missing/duplicate;
- parent-ID validation;
- Raw path validation;
- pre-commit SHA-256 / byte count;
- post-commit remote SHA-256 / byte count;
- pre/post byte identity result;
- remote UTF-8/JSONL parse result;
- remote actual `validate_discovery_set()` result;
- agent-first State validation result;
- canonical wrapper `prepare` result;
- prepared package path / record count / batch count / basis SHA;
- prompt/result-contract validation;
- DailyX 7/7 + 76/76 preservation;
- Grok 47/47 + 10/20/17 preservation;
- carry-over preservation;
- confirmation no Screening decision/acceptance/state advance occurred;
- final status `READY_FOR_SOL_SCREENING` or `NEEDS_SOL_REVIEW`.

Stop after this report.
