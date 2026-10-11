# J-GAS W40 — Approved Publication Preview r4 → Freeze, main integration, Release

Status: `EXECUTION_AUTHORITY / HUMAN_PUBLICATION_R4_APPROVED / EXACT_PDF_FROZEN_RELEASE / CORE_V2_IMMUTABLE`
Date: 2026-10-11 JST
Repository: `eariver/japanese-generative-ai-survey`
Work branch: `weekly/2026-W40-v2-work`

## 1. Human decision — ALREADY formally recorded

The Human Owner explicitly said in the J-GAS W40 Sol conversation:

> 今回のPDFは承認できます、FreezeとReleaseをしてください。

This approves Publication Preview and the normal exact-byte Freeze, normal main integration and public Release. **Do not ask for another routine Human Gate.**

Sol already executed the trusted Core v2 operator bridge successfully on 2026-10-11:
- Human approval trigger: Issue #448 comment `/survey-core-execute 3fe7a7a010693d69218bab08c94b914d74deccf7`.
- Workflow run: `38139577639` — success.
- Request-only commit: `3fe7a7a010693d69218bab08c94b914d74deccf7`, parent is exact reviewed commit `3d2715ddd0635ab3e5d15409b3cf480812479856`.
- Approval-bearing Core-executed commit: `69920428a70a179bf0ffe84d4521297fc075936e`.
- Human Publication Preview review: `sources/2026-W40/gates/reviews/publication-r4.json`, `APPROVED`, revision 4.
- Canonical approval: `sources/2026-W40/gates/publication-preview-approval.json`; immutable snapshot `gates/reviews/approvals/publication-r4.json`.
- Current Core State at this point: `RELEASE_CANDIDATE`, `architecture_review=approved`, `publication_preview=approved`, `next_action=stage:freeze`, `terminal_reason=null`.
- Keep all earlier r1/r2/r3 REQUEST_CHANGES records.

**Never re-record Human approval or regenerate the candidate.** If these already existing Core outputs differ from expected, STOP.

## 2. Exact approved Candidate and PDF authority

Human-reviewed commit: `3d2715ddd0635ab3e5d15409b3cf480812479856`
Human-reviewed tree: `c42d726dfd4bf1f875741193cc66f37687786325`
Candidate path: `sources/2026-W40/publication/v2/publication-candidate-v2.json`
Candidate file SHA-256: `fd5ee590822d38b0ed4b00d5813cb5360ab2dcee3f4d501bae3eaa16bea3f49d`
Candidate's internal `candidate_sha256`: `4defefc61d61d1ba34e601d09370796dde7ad9651ee4f1aa625855428a8068b4`
PDF path: `surveys/weekly/2026-W40/main.pdf`
PDF SHA-256: `52b752bda7e3a37957ced7f815a4a2cc56bd8883c4579505e76057174e918ca6`
PDF byte count: `466202`
PDF pages: `14`
PDF checksum path: `surveys/weekly/2026-W40/main.pdf.sha256`
CI PDF run/artifact: `38137417169` / `11701871676`

This exact PDF was visually checked after the p.3/p.4/p.9 layout repair; the three blocking defects were resolved. Any changed PDF bytes/source semantics after Human approval are FORBIDDEN. Do not rebuild/replace the approved PDF, even if CI can produce a similar result.

## 3. Exact Starting Identity — MUST be supplied by invoking Muse session

Execution contract file commit will be a **docs-only commit** after the approved Gate commit.

At startup, read-only verify:
- remote W40 HEAD == exact invocation Starting SHA (the commit that adds this instruction);
- remote W40 tree == exact invocation Starting Tree;
- that commit parent == `69920428a70a179bf0ffe84d4521297fc075936e`, or another explicitly verified docs-only chain;
- parent approval-bearing tree == `ea8103ac7fd97bfe139c48888394ba4963938009`;
- remote main HEAD == `afdb3df3faa20af3bb5798be429bba8dbd2100b1`;
- remote main Tree == `fe3f07c653f255f67087b4b46d006f8943df7115`;
- W40 State exactly `RELEASE_CANDIDATE`, Preview `approved`, `stage:freeze`, Architecture `approved`, freeze and release pending;
- latest Human Preview review r4 `APPROVED` with original reviewed commit and matching Candidate+PDF SHA;
- no unauthorized Core or approved-PDF changes; no competing work branch or out-of-scope local worktree differences.

If any guard fails, **ZERO WRITES, report expected/actual, STOP**. Never force, reset, rebase, squash, cherry-pick, or silently resynchronize divergent authoritative bytes. Do not modify the reviewed main identity to evade a guard.

## 4. Freeze — normal Core v2 only

Read in order:
1. this request, Core State, review index, canonical Approval r4 and snapshot;
2. `docs/freeze-release-policy.md`;
3. `scripts/survey_profiled_freeze_v2.py`, `scripts/survey_publication_v2.py` and the active Core Freeze stage;
4. `scripts/survey_agent_control_v2.py`, quality/schema validators;
5. `sources/2026-W39/execution/requests/sol-w39-publication-preview-r6-approved-freeze-release-20260929.md` for compatible **precedent**, NOT a license to alter Core;
6. `.github/workflows/survey-production-v2-release.yml`.

Before Freeze independently re-hash current Candidate, PDF, checksum and approval; every approved value must match §2. Use unchanged Core helpers and Profile-bound release identity `weekly/2026-W40` to create:
- `sources/2026-W40/publication/v2/freeze-record-v2.json`
- `sources/2026-W40/publication/v2/release-manifest-v2.json`
- canonical stage validation, agent reviews and Freeze stage checkpoint;
- State transition `RELEASE_CANDIDATE -> FROZEN`.

If the known older visual-review-shape compatibility issue arises, use the existing W34–W39 approved edition-local compatibility approach with `survey_publication_v2.build_freeze` only where correct, preserving validations and without changing shared Core. Record any compatibility workaround accurately.

Normal commit and non-force push to existing W40 branch. Independently read back remote `FROZEN` State, manifest, Freeze record, approved PDF SHA. Verify no publication asset changes.

## 5. Main integration — exact frozen authority

After FROZEN, re-read remote main HEAD/Tree. If main HEAD differs from §3, STOP; no auto-update to an unreviewed main.

Check PR diff for W40 edition-local changes only. No shared Core/schema/config/workflow modifications, no changed unrelated editions or material HOLD promotion.

Open a normal PR from `weekly/2026-W40-v2-work` to `main`, no new staging/work/fallback branch. Use a history-preserving normal merge when checks permit; never squash/rebase/force.

PR metadata should state:
- Human Preview r4 APPROVED against `3d2715d`;
- exact PDF SHA `52b752bd...`, 466202 bytes, 14pp;
- release identity `weekly/2026-W40`;
- Freeze Record/Manifest exact SHA from on-disk output;
- Core v2 unmodified; no edition content changes after approval.

Verify actual merged main SHA/Tree and that main contains the exact FROZEN State and frozen PDF. A changed PDF SHA stops release.

## 6. Public Release — canonical GitHub Actions

After normal main integration, use `.github/workflows/survey-production-v2-release.yml`, which requires the FROZEN authority present on `main`.

Dispatch on canonical `main` with **actual sha256 values independently recomputed from merged main**:
- `issue_id = 2026-W40`
- `production_state_sha256 = <exact FROZEN merged-main production-state SHA256>`
- `release_manifest_sha256 = <exact FROZEN merged-main release-manifest SHA256>`
- `confirmation = release:2026-W40`.

Canonical tag/identity: `weekly/2026-W40`. Weekly asset naming must come from Core Profile/workflow, not manually invented.

Use existing-release reconciliation if the release identity already exists, verifying its bytes before any attempt to write. Absolutely no duplicate tag/release or replacement asset, no silent substitution, no alternative PDF.

Verify Release URL, tag, non-draft/non-prerelease state, exact public PDF asset SHA256 `52b752bda7e3a37957ced7f815a4a2cc56bd8883c4579505e76057174e918ca6` and byte count `466202`; validate Merge Verification and Release Record on main. Follow the release workflow's normal provenance branch/PR if it creates one.

Known W34–W39 issue: The post-publication release workflow may call nonexistent `survey_agent_control_v2.py validate-state` after successful asset creation, yielding false workflow failure and skipped provenance PR. **Only if** public exact-byte Release already exists and all previous steps succeeded, apply the documented bounded W38/W39 recovery: do NOT recreate/rerun/replace asset; use canonical release-checkpoint helper and `validate_agent_state()` API to commit minimum edition-local Release provenance via history-preserving PR. No Shared Core changes. Any different failure -> STOP and report, do not generalize authorization.

## 7. Terminal Success Criteria

Only claim RELEASED when verified on current main:
- State `RELEASED`, `next_action=null`, `terminal_reason=COMPLETE`;
- Architecture Review approved; Publication Preview r4 APPROVED;
- Freeze and Release checkpoints passed;
- canonical Freeze Record, Release Manifest, Merge Verification and Release Record exist and are valid;
- public GitHub Release `weekly/2026-W40` and its PDF asset match §2 exactly;
- main/approved W40 content not mutated after Human approval;
- no Core v2 or unrelated edition changes.

Final report: exact starting/ending branch HEAD+Tree; main SHA/Tree; Human approval, Freeze and Release authority hashes; PR number and merge; Actions run; Release URL/tag/asset; public SHA/bytes/pages; any known workflow recovery; terminal State. STOP after W40 closure and do not begin W41 or other editions.

No additional Human routine approval is needed. If a genuine Exception Gate trigger is encountered (actual byte/content/provenance change or policy deviation), STOP and request new authority rather than fabricating consent.
