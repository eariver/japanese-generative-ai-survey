# W40 r5 compat validation report — evidence-source-class-projection-r5

Status: `PROPOSED_NOT_ACCEPTED` (Sol authorization required before any Evidence Acceptance use).
Built: 2026-10-10Z via `build_projection_r5.py` (edition-local, frozen Core imports only).

## 1. Failure reproduction (frozen Core, unmodified)

`evidence.task_authority_sources()` fail-closes on exactly the 3 Sol-flagged tasks:

- `w40-primary-contextlms-20260929`: `unsupported source_type for Evidence authority: 'PRIMARY_RESEARCH_ABSTRACT'`
- `w40-prewindow-lift-20260925`: same `PRIMARY_RESEARCH_ABSTRACT` error
- `w40-primary-aa-agentperf-20260929`: `unsupported source_type for Evidence authority: 'EVALUATOR_PUBLISHER'`

No other task raises (remaining 32 resolve natively). No unsupported class was silently mapped.

## 2. Reviewed narrow projection (Sol r5 §1)

- `PRIMARY_RESEARCH_ABSTRACT` → `PRIMARY_PAPER` (role: arXiv-submission; abstract-only depth until full paper consumed)
- `EVALUATOR_PUBLISHER` → `PRIMARY_OFFICIAL` (role: first-party evaluator/publisher of its own benchmark report ONLY; not model vendor; not independent reproduction)

Projected task SHAs (original → projected):

- lift: `9276f5a3490bf9fa…` → `0e15757456622dcd…`
- agentperf: `52585ecd934d8782…` → `c8299fc8124e74bc…`
- contextlms: `c1d1027c27baba36…` → `07091638d9d66a94…`

Invariant enforced per task: ONLY `source_records[*].source_type` may differ (byte-compared after nulling the field). Compat package (35 tasks): `0be7e105fa7d57cf4345969881dbde3f8762f5b72dfb6714be22af2379557c76`.

## 3. Frozen Core preliminary validation (unmodified validators)

- `validate_evidence_package_basis` over derived compat package: PASS (inside agent-tool historical-tolerance override, same as frozen runner flows).
- `task_authority_sources` over all 35 projected tasks: PASS — every bound task now has a recognized source class.
- Negative failure injection (`BOGUS_UNREVIEWED_TYPE`): FAIL_CLOSED_PASS (still raises).
- Reproducibility: DOUBLE_BUILD_IDENTICAL_PASS (two clean-temp builds, identical package SHA + per-task SHAs).

## 4. What this does NOT authorize

- NOT an Evidence Acceptance (`evidence-accepted.json` absent; no `EVIDENCE_REVIEWED` checkpoint/state).
- NOT a canonical task replacement: original 35 package task bytes + accepted Discovery/Screening preserved verbatim.
- Canonical Discovery `source_type` strings untouched (projection lives ONLY in derived copies + this ledger).
- Use in any acceptance flow requires Sol authorization of the exact ledger above after semantic review.
