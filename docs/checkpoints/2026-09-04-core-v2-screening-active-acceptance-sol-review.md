# Sol review — Core v2 active Screening acceptance authority

Status: **FOLLOW-UP CORE REPAIR REQUIRED**

## Reviewed candidate

- Repository: `eariver/japanese-generative-ai-survey`
- Branch: `fix/core-v2-screening-expansion-authority-20260904`
- Reviewed candidate SHA: `e6739f016031610daf0be19d7e866d4b48ba9f43`
- Reviewed main baseline: `c7a898889463b049dea4ee7337ee16ad5fbf3191`
- W34 read-only fixture: `weekly/2026-W34-v2-work@7350dc3b6eeaa342c3d7d4292e4d386e701c7ba5`

## 1. Strict expansion repair review

The strict accepted-root closure repair is accepted in principle.

`validate_discovery_expansion()` now fails unless every accepted root Discovery ID is represented in the derived parent closure. The previous silent-root-loss defect is therefore closed.

The exact W34 fixture correctly fails because five accepted GitHub Releases roots have no derived child:

- `w34-github-releases-comfy-org-comfyui`
- `w34-github-releases-ggml-org-llama-cpp`
- `w34-github-releases-nvidia-tensorrt-llm`
- `w34-github-releases-sgl-project-sglang`
- `w34-github-releases-vllm-project-vllm`

This is now treated as an edition-data defect, not as a reason to weaken the Core invariant.

## 2. Correct W34 semantic repair shape

The five missing roots are collector-coverage roots, not additional Weekly news events.

The correct W34 repair shape is therefore:

- preserve the existing 105 event-level derived records and all 105 Sol Screening decisions;
- add five one-to-one **coverage passthrough derived records** rooted in the five missing accepted roots;
- use the exact parent source identity and Raw paths, with a parent-requiring expansion origin;
- assign those five coverage-only records `DROP` during corrected Screening because they represent collector coverage without an in-window qualifying event;
- corrected derived Screening basis count: **110**;
- corrected Screening decision count: **110**;
- corrected decision totals: **KEEP 45 / MAYBE 19 / INSPECT 16 / DROP 30**;
- non-DROP Evidence tasks remain **80**.

Do not renumber or reinterpret `W34-C001`–`W34-C105`. The five coverage passthrough records are additional provenance-preserving Screening records, not new event IDs.

## 3. Existing Screening acceptance must remain immutable

W34 already contains one content-addressed Screening acceptance for the incomplete 105-record derived set:

`sources/2026-W34/screening/v2/accepted/2ab82c6b52b26fc01cc6a82d20da08ef4b37dadaf2ff1b0e5a570f50652b3662/screening-accepted.json`

That run was never adopted by a successful Screening Stage Checkpoint / lifecycle advancement. It is failed production evidence under the repaired Core, but its exact bytes should remain immutable for auditability.

Deleting, rewriting, or silently replacing that accepted-run directory is not an acceptable repair.

A corrected W34 Screening run should be allowed to coexist as a second immutable content-addressed accepted run.

## 4. Current Core ambiguity with multiple immutable accepted runs

Current helper code still contains directory-cardinality assumptions, especially interactive downstream helpers that glob `screening/v2/accepted/*/screening-accepted.json` and require exactly one accepted run.

That conflicts with content-addressed immutable retry/recovery semantics: an edition can legitimately retain an earlier failed/unadopted accepted run and later adopt a corrected run.

Core therefore needs an explicit distinction between:

- **historical immutable Screening acceptances**: every content-addressed accepted run retained on disk; and
- **active Screening acceptance authority**: the single run actually adopted by the successful `DISCOVERY_COLLECTED -> CANDIDATES_NORMALIZED` Stage Checkpoint.

## 5. Required active-authority resolver

Implement one reusable, fail-closed Core resolver for the active Screening acceptance after Screening advancement.

The authoritative selection rule should be Stage-Checkpoint based, not directory-order/latest-file based.

At minimum, after the `screening` machine checkpoint is passed:

1. resolve `state.checkpoint_provenance.screening` to the exact Stage Checkpoint;
2. validate the Stage Checkpoint under the current agent/checkpoint contract;
3. locate exactly one artifact named `screening-acceptance` in that checkpoint;
4. verify the artifact path/hash still matches repository bytes;
5. validate that Screening acceptance under current Core;
6. return that path as the active Screening authority;
7. ignore other historical content-addressed Screening acceptances for active selection, while leaving them immutable on disk.

Before Screening advancement, current-stage validation may still use the explicitly supplied Screening acceptance artifact being proposed for adoption.

Never select an active acceptance by lexicographic order, mtime, directory enumeration order, or "latest" heuristic.

## 6. Required downstream use

Audit every shared-Core caller that discovers Screening acceptance by directory search and replace ambiguous discovery with the active Stage-Checkpoint resolver where lifecycle semantics require an already-adopted Screening authority.

At minimum inspect:

- `scripts/run_evidence_v2_interactive.py`
- `scripts/run_selection_architecture_v2_interactive.py`
- any helper or validator that globs `screening/v2/accepted`

Existing handoff/stage validators that receive an explicit acceptance path may continue to validate the explicitly bound path, provided the later Stage Checkpoint records that same accepted run.

## 7. Required regressions

Add generic regressions proving:

1. one historical Screening acceptance + one corrected Screening acceptance may coexist;
2. before stage adoption, explicit current-stage validation can validate the corrected run without rewriting the historical run;
3. after simulated Screening Stage Checkpoint adoption, active resolver returns exactly the checkpoint-bound corrected run;
4. active resolver does not return the earlier historical run;
5. missing screening checkpoint fails closed when active authority is requested after `CANDIDATES_NORMALIZED`;
6. checkpoint with zero or multiple `screening-acceptance` artifacts fails closed;
7. checkpoint artifact hash/path drift fails closed;
8. direct legacy single-run path remains compatible;
9. no directory-order/latest heuristic is used.

## 8. W34 read-only recovery regression

Using W34 exact SHA only as a read-only fixture, construct a temporary corrected 110-record derived set by appending five coverage passthrough derived records to the 105-record event set.

Do not modify W34.

In the temporary regression:

- accepted root count = 40;
- corrected derived count = 110;
- accounted roots = 40/40;
- unaccounted roots = 0;
- retain existing 105 decisions exactly;
- add five `DROP` decisions for coverage passthrough rows;
- corrected totals = KEEP 45 / MAYBE 19 / INSPECT 16 / DROP 30;
- corrected Screening acceptance validates under repaired Core;
- historical 105-run acceptance remains present in the temporary fixture;
- simulated Stage Checkpoint selects the corrected acceptance as active;
- Evidence package preparation uses corrected derived IDs and creates exactly 80 tasks.

If exact W34 State/history defects prevent a full stage simulation, reproduce the active-authority semantics in a synthetic state/checkpoint fixture while still validating the W34 40->110 derivation and corrected Screening acceptance separately. Do not weaken state validation merely to force the archived W34 State through.

## 9. Boundary

This follow-up remains shared-Core maintenance.

Do not:

- write W34;
- write W33;
- merge main;
- delete or mutate historical Screening acceptances;
- weaken strict root closure;
- add edition-specific W34 logic;
- change Screening editorial decisions other than the five explicitly defined coverage-only `DROP` rows in temporary regression fixtures.

The next candidate is reviewable only when strict expansion authority and active Screening acceptance authority are both fail-closed and regression-backed.
