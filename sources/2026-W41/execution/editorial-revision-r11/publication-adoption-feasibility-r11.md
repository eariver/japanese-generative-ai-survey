# W41 r11 publication adoption feasibility (READ-ONLY analysis, no Core change)

Status: `EDITION_LOCAL / FEASIBILITY / NO_STAGE_ATTEMPTED`
Date: 2026-10-13 JST
Code read (no execution of publication stages):
`scripts/survey_agent_control_v2.py`, `scripts/survey_stage_validation_v2.py`,
`scripts/survey_reader_publication_v2.py`, `scripts/survey_weekly_semantic_publication_v2.py`,
`config/survey-production-v2.json`.

## Q1 — Lawful next stage from current DRAFT_COMPLETE

The configured `stage_plan` maps `DRAFT_COMPLETE` → `VALIDATED_DRAFT` via handler
`stage:reader-publication-validation` (artifacts: reader-manuscript, validated-source
`surveys/weekly/2026-W41/main.tex`, publication-pdf, quality bundle, semantic + visual
reviews). Current State (`DRAFT_COMPLETE`, next `stage:reader-publication-validation`)
is consistent with that plan. No other forward edge exists.

## Q2 — Does Core reader-publication validation accept hand-authored prose?

Yes, structurally: the manuscript manifest (`build_manuscript_manifest`) binds
Profile + Architecture + Approval + `main.tex` bytes + coverage + requirements — it does
**not** hash-bind any `draft-result.json`. Reader fidelity checks TeX blocks against
Architecture coverage/requirements, not against Draft JSON text. So improved prose can
in principle be authored into `main.tex` without violating a Draft hash binding.

## Q3 — Manuscript↔Architecture binding conditions

`architecture_coverage` must exactly equal all (package_id, must-cover requirement) pairs
from canonical Architecture (27); reader requirements must equal the Profile contract set;
`authored_by` + timestamp required; TeX fidelity must resolve every claimed block;
reader-surface gate + semantic/visual reviews + quality bundle + exact PDF follow.

## Q4 — Can r11 proposals serve as editing input with checkpoint SHA intact?

Yes, as **editing input** (not as authority substitution): authoring `main.tex` from r11
prose changes no checkpointed byte (draft checkpoint keeps r10 SHAs; manuscript binds
only the artifacts in Q2/Q3). The r11→TeX transcription must preserve all 27 must-cover
mappings and keep legacy spans out (fidelity + surface gate enforce this).

## Q5 — Is the Weekly renderer mandatory, or is another canonical path open?

The Weekly-only renderer (`survey_weekly_semantic_publication_v2.py`) is **not usable
here** — four independent refusals, all verified read-only:
1. Requires State `next_action == stage:semantic-publication-validation`; ours is
   `stage:reader-publication-validation`.
2. Requires non-empty synthesis `publication_payload`; Core synthesis contract forces
   `{}` for WEEKLY_MAGAZINE (and our canonical result carries `{}`) — renderer refuses
   fallback explicitly.
3. Requires `draft/v2/interactive-drafting-synthesis-input.json` semantic archive with
   exact headline/deck/block-text equality — absent in this Core-produced flow.
4. Reads canonical `draft/v2/packages/*/draft-result.json` only — r11 proposal paths
   are invisible to it.
The open canonical path is therefore the generic `stage:reader-publication-validation`
flow (Q1–Q4), not the Weekly renderer. No renderer use was attempted.

## Q6 — Can traceability / semantic review / surface gate all pass?

In principle yes: r11 preserves all 27 must-cover mappings, exact boundary dispositions,
evidence refs, and vendor/unresolved separations; legacy spans are absent from reader
fields; fidelity targets (coverage pairs) are unchanged. Proof requires executing the
banned publication stages (TeX authoring, fidelity, semantic + visual reviews, gate,
PDF) — **deferred, not claimed**.

## Q7 — Blocking Core rules (if any)

- **Direct checkpoint substitution is BLOCKED_BY_CORE_CONTRACT**: the DRAFT_COMPLETE
  checkpoint binds r10 Draft bytes; `build_stage_checkpoint` refuses divergent overwrite;
  State has no amend-past operation. Adopting r11 bytes AS the checkpoint would need a
  Human `REQUEST_CHANGES` regeneration boundary or a new operator boundary — neither
  exists now (ARCHITECTURE_REVIEW approved; PUBLICATION_PREVIEW boundaries `[]`).
- No rule blocks using r11 prose as manuscript-editing input (Q4), provided Q3/Q6 gates
  are genuinely executed later.

## Verdict

`ADOPTION_VIA_MANUSCRIPT_EDITING_FEASIBLE_IN_PRINCIPLE / CHECKPOINT_SUBSTITUTION_BLOCKED_BY_CORE_CONTRACT / PROOF_DEFERRED`.
No Core modification proposed or performed. No stage transition attempted.

(End of file)
