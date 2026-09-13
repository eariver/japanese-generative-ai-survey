# 2026-W34 Sol review — Discovery materialization r1

Status: `REPAIR_REQUIRED_BEFORE_DISCOVERY_ACCEPTANCE`

Issue: `2026-W34`  
Reviewed Luna start: `1c50f06ff4412cea81efc5d0ca3c28b3dc52f940`  
Reviewed Luna end: `3126be1f99548b413eab19d39a289e95e7c48a09`  
Sol binding-correction commit: `7be3d0af185d5da4009b2728e2b3aec334790340`

## 1. Findings that passed

- Luna start guard was correct.
- Start→end was ahead 2 / behind 0.
- `production-state.json` remained byte-identical at Git blob `87e6ada23ffacf85d9bb0ad96a4e777217260356`.
- Lifecycle remains `ISSUE_INITIALIZED`; next action remains `stage:discovery`.
- Discovery JSONL exists with 40 records / 40 unique Discovery IDs.
- Sol event traceability is 105/105 with 0 silently dropped events.
- DailyX is 76/76 topics across 7 imported Drive-returned Raw files.
- Corrected Grok r2 remains 47/47 URLs with 10 ORDINARY_WINDOW / 20 BACKGROUND_ONLY / 17 LATE_BREAKING.
- Existing GitHub Releases Raw was reused without modification.
- Raw index expansion and the bounded source-local captures are within the assigned materialization scope.

## 2. Blocking defect found by independent Sol review

Luna's `materialization-validation-v0.1.json` reports temporary Discovery acceptance `PASS`, but the committed bytes at Luna end could not pass the current Core implementation.

Current Core `scripts/survey_discovery_v2.py::_validate_x_integration()` requires every `result.discovery_ids[]` in the COMPLETE X Source Intake manifest to:

1. name an actual accepted Discovery record, and
2. bind the imported Grok Raw path in that Discovery record's normalized `raw_refs`.

At Luna end, `sources/2026-W34/external/x/x-source-intake-v2.json` named these event-level working IDs as Discovery IDs:

- `W34-C001`
- `W34-C025`
- `W34-C039`
- `W34-C040`
- `W34-C041`
- `W34-C042`
- `W34-C043`
- `W34-C044`
- `W34-C065`
- `W34-C070`
- `W34-C089`
- `W34-C090`

The actual Discovery graph does not use those IDs. Its dedicated Grok record is:

`w34-grok-r2-corrected-47-url-ledger`

and that record directly binds:

`sources/2026-W34/external/x/weekly-x-2026-W34-r2/raw/grok-x-result.corrected.md`

Therefore the reported temporary acceptance PASS was a false positive caused by using a schema-equivalent/custom validation rather than proving the committed graph with the current Core `build_acceptance()` path.

## 3. Sol correction

Sol corrected only the X manifest Discovery binding at commit:

`7be3d0af185d5da4009b2728e2b3aec334790340`

The manifest now names exactly:

`w34-grok-r2-corrected-47-url-ledger`

as its `DISCOVERY_RECORDED` Discovery ID.

This is a binding correction, not a change to X Raw, Grok classifications, Sol event scope, materiality, chronology, or technical Evidence.

The 47 X URLs → W34 event-level relationships remain preserved in:

`sources/2026-W34/intake/working-set/grok-r2-candidate-crosswalk-v0.1.md`

and the 105-event mapping remains preserved in:

`sources/2026-W34/discovery/event-discovery-crosswalk-v0.1.json`

## 4. Required repair validation

Before formal Discovery advancement, the current branch must be validated using the actual reviewed-main implementation, not a schema-equivalent substitute:

- `scripts.survey_x_intake_v2.validate_manifest(..., require_complete=True)`
- `scripts.survey_discovery_v2.build_acceptance(...)` to a temporary non-repository output path
- `scripts.survey_discovery_v2.validate_acceptance(...)` on that temporary output

The real temporary acceptance must prove:

- 40 Discovery records / 40 unique IDs;
- graph validation PASS;
- X integration PASS with the corrected dedicated Grok Discovery ID;
- every normalized `raw_ref` exists and hashes current bytes;
- 105/105 event crosswalk remains intact;
- DailyX 76/76 and Grok 47/47 + 10/20/17 remain intact;
- `production-state.json` is still unchanged before advancement.

If and only if the real current-Core acceptance build and validation pass, the bounded repair worker may proceed with the deterministic Core `stage:discovery` advancement because Sol has already accepted the semantic Discovery completeness baseline in `sources/2026-W34/execution/decisions/sol-discovery-completeness-20260903-r1.md`.

Do not begin Screening in the same repair task.
