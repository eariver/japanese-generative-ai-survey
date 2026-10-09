# TS-003 Screening-through-Evidence guard addendum v2

Status: `EXECUTION_AUTHORITY_ADDENDUM / GUARD_PRECEDENCE_FIX`

Date: `2026-09-30 JST`

Issue: `SP-vision-multimodal-2026`

Branch: `special/vision-multimodal-2026-work`

## 1. Purpose

This addendum corrects a self-referential guard defect in:

`sources/SP-vision-multimodal-2026/execution/requests/sol-ts003-screening-through-evidence-20260930.md`

The original execution request was committed on top of the Sol Discovery Completeness Review commit. Its Section 0 hard-coded the parent work-branch HEAD/tree (`95cd2c...` / `c13b7ffd...`). Committing the execution request itself advanced the branch to a new HEAD/tree, so those embedded work-branch values became stale by construction.

Muse correctly stopped fail-closed when it observed this mismatch. No production work from the stopped attempt is authorized or assumed.

## 2. Precedence

For the next execution, this addendum **supersedes only Section 0 (`Exact start guard`) of the original execution request**.

All Sections 1–10 of:

`sources/SP-vision-multimodal-2026/execution/requests/sol-ts003-screening-through-evidence-20260930.md`

remain authoritative and unchanged.

If there is any conflict about startup guards, use this addendum plus the exact SHA/tree values supplied in the launch message.

## 3. Correct guard model

The work-branch HEAD/tree MUST NOT be hard-coded inside an execution file that is itself committed to that same branch.

Instead:

- the launch message supplies the exact expected remote work-branch HEAD and tree after this addendum is committed;
- Muse verifies those two launch-supplied values read-only before any write;
- the execution file does not attempt to derive or replace them.

The following stable guards remain fixed and must also match:

- remote main HEAD == `d6381568cc897a47d6de992189e20339350342b7`
- remote main tree == `83ce3a216d852a1c32d0138f9c56fadefa800666`
- remote `production/survey-core-v2` HEAD == `774dd39a951c9ac3818e83dfffd4c7666efb0a20`
- remote Core tree == `cd46a6f7a6dcc4031e76220cea4c52c7dd1fc481`

Canonical edition-state hard guards:

- issue == `SP-vision-multimodal-2026`
- lifecycle == `DISCOVERY_COLLECTED`
- discovery checkpoint == `passed`
- screening == `pending`
- evidence == `pending`
- materiality == `pending`
- completeness == `pending`
- selection == `pending`
- architecture == `pending`
- Human Architecture Review == `pending`
- Human Publication Preview == `pending`

These state values are authoritative from `production-state.json`.

## 4. Discovery-count verification is not a production-state field guard

The following values remain expected and must be checked, but they are **cross-artifact consistency checks**, not fields expected inside `production-state.json`:

- Discovery acceptance record count = `111`
- Discovery unique locators = `111`

Verify them from the canonical Discovery acceptance / coverage artifacts.

If either differs from the accepted Discovery corpus, stop fail-closed and report the mismatch. Do not describe absence of those fields from `production-state.json` as a lifecycle guard failure.

## 5. Fail-closed behavior

If any launch-supplied work-branch SHA/tree, stable main/Core guard, canonical lifecycle/checkpoint guard, or cross-artifact Discovery count actually differs, perform zero writes and report expected vs actual.

Do not create fallback, repair, review, or iteration branches.

## 6. Authorized mission after guards pass

After all corrected guards pass, execute Sections 1–10 of the original request exactly as written:

`Discovery PASS -> Screening -> Evidence -> validation/checkpoints -> STOP for Sol Evidence Semantic Review`

Do not proceed to Materiality, Completeness, Selection, Architecture, Draft, Publication Preview, Freeze, or Release.

Terminal operational state remains:

`TS-003 SCREENING_EVIDENCE_COMPLETE`

`AWAITING_SOL_EVIDENCE_SEMANTIC_REVIEW`

`NO_MATERIALITY`

`NO_SELECTION`

`NO_ARCHITECTURE`
