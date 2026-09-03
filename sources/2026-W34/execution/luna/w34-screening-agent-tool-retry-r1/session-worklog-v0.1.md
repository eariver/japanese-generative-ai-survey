# W34 agent-first Screening wrapper retry — session worklog

- Issue: `2026-W34`
- Branch: `weekly/2026-W34-v2-work`
- Exact starting SHA: `7375afc11dc7a8cf3d9e1ba6f6a135252a42bbf2`
- Current checkout HEAD / helper implementation SHA: `7375afc11dc7a8cf3d9e1ba6f6a135252a42bbf2`
- Final status: **NEEDS_SOL_REVIEW**

## Scope and authority

The remote branch HEAD matched the supplied exact starting SHA before any write. The instruction, Sol wrapper review, current agent-first control module, current screening helper, and retry inputs were read from that checkout. The existing event-level input and crosswalk were treated as immutable. The prior `w34-screening-granularity-expansion-r1` diagnostic was not edited.

The accepted 40-record Discovery graph, acceptance, checkpoint, Production State, and all existing Raw objects remained outside the write scope. No Screening decision, result, acceptance, lifecycle transition, or downstream stage was performed.

## Validation sequence

1. `survey_agent_control_v2.validate_agent_state()` was run against the current Production State and returned **PASS**. State was `DISCOVERY_COLLECTED`, next action `stage:screening`, discovery checkpoint `passed`, and screening checkpoint `pending`.
2. The prior direct helper failure was retained as historical evidence. The direct `python3 scripts/survey_screening_v2.py ...` invocation was not rerun.
3. The canonical `scripts/survey_agent_tool_v2.py` wrapper was run with helper `scripts/survey_screening_v2.py`, the existing event-level Discovery path, a fresh output path, limits `max_records=50` and `max_json_chars=120000`, and the actual current checkout HEAD as `--implementation-sha`.
4. The wrapper's agent-first State preflight passed. The helper then failed while decoding the existing event-level input in `read_jsonl`, before creating the package directory or any batch.

Exact wrapper exception:

```text
'utf-8' codec can't decode byte 0xaa in position 1: invalid start byte
```

Wrapper exit code: `2`.

## Integrity observations

The committed event-level input path is present but its current bytes are not UTF-8 JSONL: byte count `210060`, SHA-256 `a15ddbde1bc3b35ab158d68a50313294091aa33f2d942d2e24d3d578f5344321`. The earlier immutable expansion diagnostic records 105 records / 105 unique IDs and expected SHA-256 `5dbdcbfd70dc1e4605560dc06fc89e940141116b0bf9bf8eefaef6f8bf9f2332`, so this retry does not claim an independently parsed package input.

The crosswalk remains valid as committed JSON: 105 rows, 105 unique `W34-C001`–`W34-C105` event IDs, missing 0, duplicate 0, silently dropped 0; all 259 parent references resolve to the accepted 40-record graph, and all 36 unique Raw paths exist. DailyX remains 7/7 files and 76/76 topics; corrected Grok r2 remains 47/47 with `10 ORDINARY_WINDOW / 20 BACKGROUND_ONLY / 17 LATE_BREAKING`; carry-over remains `RECHECKED_UNRESOLVED` without promotion. These facts do not override the input-byte decode failure.

No prepared package was created, so package schema, batch, prompt, and result-contract checks are **not available** for this attempt. The output directory did not exist after the failure.

## Stop

Because the canonical wrapper itself failed, this session stops at `NEEDS_SOL_REVIEW`. The event-level input was not repaired or rebuilt, shared Core was not changed, and the Production State remains byte-identical. Sol should review the committed input-byte anomaly and authorize the next bounded action.
