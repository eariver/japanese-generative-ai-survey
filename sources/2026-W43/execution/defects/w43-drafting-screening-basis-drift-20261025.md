# Shared-Core defect — frozen drafting rejects trusted bridge-advanced State (W43 Draft r1 BLOCKED)

Status: `SHARED_CORE_DEFECT / EDITION_OBSERVED / BLOCKED_DRAFT_NATIVE_VALIDATION`
Observed: `2026-10-25` (Muse Draft r1, work branch `weekly/2026-W43-v2-work`)
Edition: `2026-W43`, State `ARCHITECTURE_ESTABLISHED` (Human Architecture r1 APPROVED)
Instruction: `sources/2026-W43/execution/instructions/sol-w43-approved-r6-substantive-japanese-draft-with-closing-recap-20261025.md`
Stop token reached: `BLOCKED_DRAFT_NATIVE_VALIDATION` (contract §4 genuine-validation-failure stop; NOT `SOL_W43_JAPANESE_DRAFT_R1_WITH_RECAP_EDITORIAL_AUDIT_READY`)

## Preflight (all PASS, zero writes before failure)

- Remote 6-way exact HEAD+Root Tree reconfirmed read-only via `git ls-remote` + `git rev-parse <sha>^{tree}`:
  - Work `weekly/2026-W43-v2-work`: HEAD `5f925ac9e2271faf8e3cbbecec0fda54438c51e4` / Tree `d901ef1fde67e380e179d700f24000db4451a44a`
  - Main: HEAD `041a08dfef3112643cbf85b4a86a7b6f9128aed6` / Tree `a134dc36a407d08ab1de416324229b3955e0325a`
  - Frozen Core v2: HEAD `774dd39a951c9ac3818e83dfffd4c7666efb0a20` / Tree `cd46a6f7a6dcc4031e76220cea4c52c7dd1fc481` (object present, ancestor of main)
- Gate authority valid: `production-state.json` `ARCHITECTURE_ESTABLISHED`, `human_gates.architecture_review=approved`, `publication_preview=pending`, `machine_checkpoints.architecture=passed`, `next_action=stage:drafting-synthesis`.
- Architecture/Summary/Attention SHA256 all match approved bytes (`7d8f0ea5…` / `38c17ecc…` / `7c3e4deb…`); Selection 19/1/12; receipt `sol-w43-r6-architecture-human-approval-weekly-recap-20261025` PASS, reviewed commit `809cd45fe939b078aa8523cf2a98f276df3b99d1`.
- Local sync (explicitly permitted fast-forward only): branch `weekly/2026-W43-v2-work`, clean tree, local HEAD was reported `3c8f91161a254646e860df1aab9b66d9d691cb4c`; `git fetch origin`; `git merge-base --is-ancestor` YES (10 commits behind); `git merge --ff-only origin/weekly/2026-W43-v2-work` → `5f925ac9e…` / Tree `d901ef1f…`. No reset/rebase/force-push/new-branch/merge-commit.

## Source-level error

Command (frozen native workflow only, `PYTHONPATH=.`):

```text
python3 scripts/run_drafting_synthesis_v2_interactive.py --repo-root . \
  --state sources/2026-W43/production-state.json --input /tmp/opencode/w43-draft-input.json
```

Exit: `ValueError: Screening package basis drift: state_sha256`, raised from
`survey_screening_v2.validate_package_basis` via `survey_drafting_v2_base._resolve_effective_screening_discovery`
via `survey_drafting_v2.derive_draft_package` (first package P1; zero Draft artifacts written — `sources/2026-W43/draft/` absent).

Byte evidence:

| Item | SHA256 |
|---|---|
| Current `sources/2026-W43/production-state.json` | `b0450d25b9dd4db8424d1c92d713d28c1b268b4e6a3b960a053f9684bb3eebb6` |
| Screening `v2/packages/r1` basis `state_sha256` | `885927bd98e1ade491bc88e666aa0f39233ba7f0fb93f8ed87c9d2760ac22596` |
| Screening `v2/packages/r2` basis `state_sha256` | `885927bd98e1ade491bc88e666aa0f39233ba7f0fb93f8ed87c9d2760ac22596` |
| Screening r2 basis `profile_sha256` vs current profile | MATCH (`4447d25e…`) |
| Screening r2 basis `discovery_sha256` vs current discovery | MATCH (`f62d8459…`) |

Sole drift is `state_sha256`: both screening packages bind the pre-advancement State bytes, while the current State legitimately advanced through trusted operator bridges (`EVIDENCE_REVIEWED→SELECTION_COMPLETE→ARCHITECTURE_ESTABLISHED`) plus the Human Architecture r1 approval. Frozen `validate_package_basis` demands byte-identical State, so `derive_draft_package` can never succeed after any legitimate bridge advancement.

## Root cause (shared Core, not edition)

Same family as `execution/defects/w43-screening-prepare-state-basis-20261025.md` (frozen screening entry points reject trusted bridge-advanced State): the agent-first bridge writes States that the frozen direct-local validators refuse. The bridge runs reviewed-main Core; the validator enforces single-local conventions (`state_sha256` byte-equality against screening-time State). No edition data corruption: Matrix/Selection/Architecture/Evidence/Views/ledger/completeness, Discovery/Screening, State/Checkpoints, Gates, main and Frozen Core are all intact and byte-verified.

## Lawful options exhausted (all refused as integrity violations)

- Re-creating screening packages at current State: upstream regeneration invalidating approved Selection/Architecture; forbidden.
- Hand-editing State bytes to old hash: rewriting canonical authority; forbidden.
- Patching `scripts/` (shared Core root): production must treat shared roots as read-only; forbidden. Core repair belongs in a separate reviewed change.
- `--implementation-sha` override / skipping validation / hand-assembling Draft Results: manual PASS fabrication; refused.
- Detached scratch at old State: old State is pre-`ARCHITECTURE_ESTABLISHED` with pending Gates; runner `_upstream` requires approved `ARCHITECTURE_ESTABLISHED`; fails by design.
- Operator `ADVANCE_STAGE`: Drafting never advances State, and the instruction forbids bridge requests until Sol reviews the actual Japanese Draft; not applicable.

## Production disposition

- `BLOCKED_DRAFT_NATIVE_VALIDATION`: zero Draft Packages/Results, zero synthesis, zero reader preview, zero conclusion asset, zero State/Gate/metrics mutation. No TeX/PDF, no Publication Preview.
- Prepared-but-unvalidated interactive input preserved as diagnostic evidence ONLY (8 packages / 113 blocks / 62 PARAGRAPH + 28 HEADING + 15 TABLE + 8 NOTE / 22185 body chars; SHA256 `d1cb5277e9243d0feb04f585be8d316e0f6137b2ebd5c9d4763d68760690c409`): `execution/defects/w43-draft-r1-interactive-input-UNVALIDATED-20261025.json`. It is NOT production authority, NOT a Draft Result, and must not be cited as validated prose. After reviewed Core repair, rerun the contracted flow cleanly from the then-current State (this failed run is not carried forward as PASS).
- Human recap requirement (closing「今週の総括」after P8) remains OPEN and pending successful Draft rerun; no fallback publication prose is created hereby.
- Shared-Core repair pointer: reconcile `validate_package_basis` / `verify_state_basis` / `validate_state_semantics` with agent-first bridge conventions (FROM-state checkpoint files; per-executing-commit history SHAs), or route drafting basis resolution through the agent-first resolver. Repair Core separately under review; then rerun this exact instruction cleanly.

## Provenance

- Local pre-sync HEAD `3c8f91161a254646e860df1aab9b66d9d691cb4c` / Tree `e24421091d402b602cb62ac01abe60a829d5a5d3`; post-sync HEAD `5f925ac9e2271faf8e3cbbecec0fda54438c51e4` / Tree `d901ef1fde67e380e179d700f24000db4451a44a` (fast-forward, 10 commits).
- Runner input: `/tmp/opencode/w43-draft-input.json` (scratch, outside repo); builder `/tmp/opencode/w43_input_builder.py` + deepener `/tmp/opencode/w43_deepen.py`.
- `scripts/__pycache__/` bytecode from the run removed; working tree otherwise untouched; frozen Core/main unmodified.
