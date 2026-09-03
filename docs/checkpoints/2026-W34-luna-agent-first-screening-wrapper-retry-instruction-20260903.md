# 2026-W34 Luna instruction — agent-first Screening wrapper retry

Status: `READY_FOR_BOUNDED_LUNA_EXECUTION`

Issue: `2026-W34`  
Canonical branch: `weekly/2026-W34-v2-work`

## 1. Purpose

The previous event-level Screening granularity task successfully materialized the 105-event Screening input, but package preparation was attempted by invoking `scripts/survey_screening_v2.py` directly. That direct invocation reached legacy `core.verify_state_basis()` semantics and stopped on an agent-first Production State that is valid under the current postintegration controller.

Reviewed main and the W34 branch already contain the canonical compatibility execution surface:

`scripts/survey_agent_tool_v2.py`

This bounded retry must reuse the existing 105-event input unchanged and execute Screening package preparation through that agent-first wrapper.

This task stops after a valid Screening package is prepared and validated for independent Sol semantic Screening. Do not produce Screening decisions.

## 2. Exact preconditions

At task start verify the remote branch HEAD exactly matches the supplied Exact Starting SHA from the user prompt.

Then read, in order:

1. `AGENTS.md`
2. `docs/survey-production-core-v2-session-bootstrap.md`
3. `docs/survey-production-core-v2-agent-first-reaudit-2026-08-22.md`
4. `sources/2026-W34/production-profile.json`
5. `sources/2026-W34/production-state.json`
6. `sources/2026-W34/discovery/discovery-accepted-v2.json`
7. `sources/2026-W34/discovery/discovery-v2.jsonl`
8. `sources/2026-W34/screening/input/event-discovery-v2.jsonl`
9. `sources/2026-W34/screening/input/event-discovery-crosswalk-v0.1.json`
10. `sources/2026-W34/execution/luna/w34-screening-granularity-expansion-r1/validation-v0.1.json`
11. `sources/2026-W34/execution/luna/w34-screening-granularity-expansion-r1/sol-screening-handoff-v0.1.md`
12. `sources/2026-W34/execution/findings/sol-screening-granularity-review-20260903-r1.md`
13. `sources/2026-W34/execution/findings/sol-agent-first-screening-wrapper-review-20260903-r1.md`
14. `scripts/survey_agent_tool_v2.py`
15. `scripts/survey_agent_control_v2.py`
16. `scripts/survey_screening_v2.py`
17. `tests/test_survey_agent_tool_v2.py`

The latest Sol wrapper finding is controlling authority where the previous task assumed direct helper execution.

## 3. Existing artifacts are immutable inputs

Do not rebuild or modify:

- `sources/2026-W34/screening/input/event-discovery-v2.jsonl`;
- `sources/2026-W34/screening/input/event-discovery-crosswalk-v0.1.json`;
- `sources/2026-W34/production-state.json`;
- accepted 40-record Discovery JSONL/acceptance;
- Discovery Stage Checkpoint;
- existing DailyX/Grok/GitHub Releases/primary-gapfill/carry-over Raw.

The existing event-level input is already validated as:

- 105 records;
- 105 unique IDs;
- `W34-C001` through `W34-C105`: 105/105;
- accepted parent validation PASS;
- 36 unique Raw paths, all present;
- DailyX 7/7 and 76/76;
- corrected Grok r2 47/47 with 10/20/17;
- current Core `validate_discovery_set()` PASS.

The retry concerns execution mode only.

## 4. Canonical execution mode

Do not run Screening `prepare` directly through:

`python3 scripts/survey_screening_v2.py ...`

Instead use the current reviewed agent-first wrapper:

`scripts/survey_agent_tool_v2.py`

The wrapper must receive:

- current W34 Production State;
- helper `scripts/survey_screening_v2.py`;
- the helper `prepare` command;
- event-level Discovery path;
- a fresh bounded output directory;
- the **actual current checkout HEAD** as the helper's `--implementation-sha`.

Conceptual command:

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

Equivalent invocation is acceptable only if it uses `survey_agent_tool_v2` and preserves the same agent-first State validation semantics.

Do not pass the initialization SHA `bdbc2126...` as the current helper implementation identity.

## 5. Wrapper validation requirements

Before package preparation, explicitly prove that current State passes:

`survey_agent_control_v2.validate_agent_state()`

The retry must distinguish:

- direct-helper legacy verifier failure from r1; and
- canonical agent-tool wrapper result from this retry.

Do not call the r1 direct-helper failure a current shared-Core defect unless the canonical wrapper also fails.

## 6. Prepared package requirements

Preferred package root:

`sources/2026-W34/screening/v2/prepared/w34-event-screening-r1/`

Expected package:

`package.json`

plus generated `input/batches/batch-###.jsonl` files.

After preparation, validate at least:

- `package.json` parses;
- schema version `2.0-rc1`;
- issue `2026-W34`;
- research profile `WEEKLY`;
- `basis.state_path` is current W34 Production State;
- `basis.discovery_path` is exactly `sources/2026-W34/screening/input/event-discovery-v2.jsonl`;
- Discovery hash equals current event-level file bytes;
- input record count = 105;
- batch metadata/hash integrity PASS;
- concatenated batch Discovery IDs equal exactly all 105 input IDs;
- no duplicate or missing ID;
- prompt/result-contract hashes match current reviewed Core.

Run the package-basis validation through the same agent-first wrapper semantics, not by bypassing State verification.

## 7. Expected batching

With current default limits requested here (`max_records=50`, `max_json_chars=120000`), record the actual batch count and per-batch counts. Do not hard-code an expected count if the character limit causes a different partition.

Only the total 105 and exact ID coverage are mandatory.

## 8. Allowed writes

Only new edition-local files under:

- `sources/2026-W34/screening/v2/prepared/w34-event-screening-r1/**`
- `sources/2026-W34/execution/luna/w34-screening-agent-tool-retry-r1/**`

may be created/updated in this task.

Do not modify r1 validation/worklog/handoff; preserve the failed direct invocation as historical diagnostic evidence.

## 9. Required execution record

Create under:

`sources/2026-W34/execution/luna/w34-screening-agent-tool-retry-r1/`

at least:

- `validation-v0.1.json`;
- `session-worklog-v0.1.md`;
- `sol-screening-handoff-v0.1.md`.

Record:

- exact starting HEAD;
- actual helper implementation SHA passed through the wrapper;
- agent-state validation result;
- direct-r1 failure retained as historical diagnostic;
- wrapper prepare result;
- package path/hash;
- batch count/counts/hashes;
- 105/105 ID coverage;
- unchanged State/accepted Discovery hashes;
- no Screening decision/acceptance.

## 10. Explicitly forbidden

Do not:

- modify shared Core/config/schema/prompt/workflow files;
- modify Production State;
- modify accepted Discovery/checkpoint;
- rebuild the 105-event set;
- create `KEEP/MAYBE/DROP/INSPECT` decisions;
- create Screening result files;
- create Screening acceptance;
- advance to `CANDIDATES_NORMALIZED`;
- start Evidence/Materiality/Completeness/Selection/Architecture;
- modify W33;
- create another branch;
- force/reset/rewrite/rebase.

## 11. Stop conditions

### PASS stop

If the canonical wrapper successfully prepares and validates the package, commit only allowed paths and stop with status:

`READY_FOR_SOL_SCREENING`

### Failure stop

If `survey_agent_tool_v2` itself fails, do not alter State or Core. Record the exact exception, whether failure occurred before/inside/after helper execution, and stop:

`NEEDS_SOL_REVIEW`

A wrapper failure may justify shared-Core maintenance; a direct-helper-only failure does not.

## 12. Required completion report

Report:

- Exact Starting SHA;
- Ending SHA;
- start→end ahead / behind / commit count;
- changed paths;
- Production State before/after and SHA;
- accepted 40-record Discovery unchanged confirmation;
- event-level 105/105 unchanged confirmation;
- `validate_agent_state` result;
- actual current helper implementation SHA;
- canonical `survey_agent_tool_v2` prepare result;
- package path and SHA;
- package discovery basis path/hash;
- package input record count;
- batch count and per-batch record counts;
- exact 105-ID batch coverage result;
- prompt/result-contract hash validation;
- confirmation r1 failed diagnostic remains unchanged;
- confirmation no Screening decisions/results/acceptance exist;
- confirmation no lifecycle advancement occurred;
- final status `READY_FOR_SOL_SCREENING` or `NEEDS_SOL_REVIEW`.

Stop after this report.