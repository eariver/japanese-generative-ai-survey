# W34 shared-Core defect — canonical Drafting re-derivation rejects valid DERIVED_EXPANSION Screening basis

Status: `BLOCKING_SHARED_CORE_DEFECT / STOPPED_BEFORE_DRAFTING / EDITION_FROZEN_PENDING_CORE_REPAIR`

Issue: `2026-W34`
Edition branch: `weekly/2026-W34-v2-work`
Execution agent: `Muse Spark 1.3`
Execution mode: `EXPERIMENTAL_LUNA_ROLE_SUBSTITUTION`
Date: `2026-09-11 JST`

Execution authority (canonical, read in full):

- `sources/2026-W34/execution/requests/sol-post-architecture-drafting-sidecar-publication-preview-request-20260911-r1.md`
- Human decision reference: `sources/2026-W34/execution/reviews/w34-human-architecture-review-decision-20260911-r3.md`

Reviewed main: `6d748a962d57beff89da7c1b20cb5a9a86c8e261`
Shared roots on this branch are byte-identical to reviewed main
(`git diff origin/main...HEAD -- scripts/ config/ schemas/ docs/survey-production-core-v2-*.md` empty),
so the defect below exists in current reviewed Core, not in stale edition bytes.

## Completed before the blocker (pushed, read back)

1. Read-only guards matched exactly before any write:
   - remote W34 HEAD `b0781fd1adac864e5f2288b3c15c4f13b1c675f0`
   - remote W34 tree `d7fb79a9306ca7e57151c2cef268402e303a0246`
   - remote main HEAD `6d748a962d57beff89da7c1b20cb5a9a86c8e261`
2. Human Architecture approval r3 recorded **only** via the canonical round-trip:
   `survey_human_gate_v2.py record-architecture-approval --expected-revision 3
   --reviewed-by EaRiver --reviewed-at 2026-09-11T11:06:00Z
   --review-reference sources/2026-W34/execution/reviews/w34-human-architecture-review-decision-20260911-r3.md
   --reviewed-commit-sha 498e45b5648f418e346e1a171dc588494dacf716`
   - `gates/reviews/architecture-r3.json` = `APPROVED`, binds `498e45b5...`
   - `gates/reviews/approvals/architecture-r3.json` present
   - `gates/architecture-approval.json` binds approved bytes
     (`7f30d273...` / `a5daa116...` / `2460890a...`, matching the Human decision)
   - review index contiguous r1/r2/r3; State `architecture_review=approved`,
     `publication_preview=pending/null`; no Publication Preview approval created.
3. Checkpoint committed and pushed with remote read-back:
   `f9ff332caf5496b5bbe14bfbd2b19cdac79ac7d3`
   (`W34: record Human Architecture approval r3 (Muse Spark 1.3 EXPERIMENTAL_LUNA_ROLE_SUBSTITUTION)`).
   Approved Architecture/Selection/Evidence bytes were not touched
   (`git diff 498e45b5..HEAD` shows only the two request/decision reference files
   plus the approval checkpoint).

## Exact blocker

Canonical Drafting cannot start. The agent-first wrapper (the reviewed canonical path
for this exact situation):

- `scripts/run_drafting_synthesis_v2_agent.py`
  (wraps `run_drafting_synthesis_v2_interactive.py` under
  `survey_agent_tool_v2.current_stage_basis_override()`)

fails during WU-009 upstream basis load for **every** package before writing any
Draft artifact (`sources/2026-W34/draft/` was never created; working tree otherwise clean):

`WU-009 upstream Architecture basis invalid: Screening acceptance points at a different Discovery set`

Minimal read-only reproduction (no writes, under the canonical override):

```python
architecture.validate_candidate_matrix(
    matrix, root,
    root/'sources/2026-W34/production-profile.json',
    root/'sources/2026-W34/discovery/discovery-v2.jsonl',          # 369 records, root
    root/'sources/2026-W34/screening/v2/accepted/41503363e1aef269ead56ac056b7f58e53eb1934d5de926f2cc49ee3bd84ccc3/screening-accepted.json',
    root/'sources/2026-W34/evidence/v2/accepted/647cde464d92935c1ca633ade62bcbf7ebe88c458cc8b3848bae8d2fc4794831/evidence-accepted.json',
    root/'sources/2026-W34/evidence/v2/views/accepted/e2e644bcc97ac664949b272fca919923385af6192c65b5a3566e30382b0ca7ba/edition-views-accepted.json',
    root/'sources/2026-W34/materiality-ledger-v2.json',
    root/'sources/2026-W34/profile-completeness-v2.json',
    <current-HEAD-implementation-sha>,
)
# -> ['Screening acceptance points at a different Discovery set']
```

Chain: `derive_draft_package` -> `_load_drafting_basis` ->
`architecture.validate_candidate_matrix` -> `derive_candidate_matrix` ->
`_load_upstream` -> `evidence.validate_screening_acceptance`
(`scripts/survey_evidence_v2.py`), which requires the caller-supplied Discovery path
to equal the Screening package's **effective** Discovery path.

## Why this is a shared-Core defect, not an edition data error

- Active Screening acceptance resolved via the canonical checkpoint selector
  (`agent.resolve_checkpoint_artifact(..., 'screening', 'screening-acceptance')`):
  `sources/2026-W34/screening/v2/accepted/41503363e1aef269ead56ac056b7f58e53eb1934d5de926f2cc49ee3bd84ccc3/screening-accepted.json`
  (`d18c8ce3...`), identical to the Architecture Review Attention binding.
- Its package basis is a validated expansion:
  - root: `sources/2026-W34/discovery/discovery-v2.jsonl`
    (`e176326f...`, 369 records) — matches `discovery-accepted-v2.json`
  - derived/effective: `sources/2026-W34/screening/input/event-discovery-v2.jsonl`
    (`0a23be47...`, 439 records)
  - `resolve_effective_discovery_basis()` mode = `DERIVED_EXPANSION` (clean).
- Active Evidence acceptance `647cde46...`
  (`VERIFIED 49 / PARTIAL 352 / NEEDS_MORE 8` over 409 tasks) and the stored
  Candidate Matrix were built on exactly this Screening acceptance and passed the
  `CANDIDATES_NORMALIZED` checkpoint; prior stage validation re-checks stored bytes
  by SHA drift rather than re-deriving the Matrix from Discovery, so the
  inconsistency only surfaces at Drafting re-derivation.
- The Drafting runner always supplies the **root** Discovery path
  (`discovery-accepted-v2.json → discovery-v2.jsonl`), while the downstream
  validator requires the **effective derived** path. For `DIRECT` Screening bases
  (e.g. SP001, root == derived) this passes; for any `DERIVED_EXPANSION` Weekly
  (W34) it fails deterministically. This is the same defect family as the
  2026-09-04 Screening-expansion authority gap (resolved for Evidence via PR #484);
  the Drafting re-derivation path was not covered by that repair.

## Handling (per production/Core-maintenance boundary)

- **No shared-Core edit was made on this branch** (`AGENTS.md`, request section 12).
  `scripts/`, `config/`, `schemas/`, `docs/survey-production-core-v2-*.md` untouched.
- **No Drafting writes exist**: no `sources/2026-W34/draft/` tree, no synthesis
  artifacts, no checkpoint, no State advance beyond the pushed approval.
- **No downstream work was attempted**: no reader/publication validation, no PDF,
  no Publication Boundary Validator sidecar, no feedback files, no Publication
  Candidate, no Authority Auditor sidecar, and **no Publication Preview Human
  decision** was generated.
- State is parked safely at `ARCHITECTURE_ESTABLISHED` with approved r3 provenance
  (commit `f9ff332c`, pushed, read back). Another session can resume from that
  commit without chat history.

## Required before resuming this request

1. Repair shared Core separately under Core change management (reviewed repair +
   clean rerun of any formal validation that touched the defect):
   make the canonical Drafting basis resolve the validated **effective** Screening
   Discovery basis for `DERIVED_EXPANSION` (or otherwise accept the
   checkpoint-bound root→derived expansion consistently through Matrix
   re-derivation), without weakening any package-content hash checks.
2. Rerun W34 Drafting cleanly from commit `f9ff332c` (no partial Draft artifacts
   exist to carry forward) through the same canonical wrapper, then continue the
   authorized path: `DRAFT_COMPLETE` → validation/PDF → `VALIDATED_DRAFT` →
   Boundary Validator sidecar → Candidate → `RELEASE_CANDIDATE` → Auditor sidecar
   → `SOL_PUBLICATION_PREVIEW_REVIEW_READY` → STOP.
3. Do not hand-author Draft/approval/state/index records to bypass the failure.

Markers: `SOL_PUBLICATION_PREVIEW_REVIEW_READY` **not reached**.
`HUMAN_ARCHITECTURE_R3_RECORDED / DRAFTING_BLOCKED_ON_SHARED_CORE / STOPPED`.
