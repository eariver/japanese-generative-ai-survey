# r12 supplement manifest — traceability + publication restrictions (staged, NOT canonical)

Status: STAGED_R12 / NON_CANONICAL
Scope: ties both r12 notes to canonical IDs, Sol decisions, matrix IDs, and restrictions.

## Bindings

| Note | Discovery ID | Evidence task ID | Matrix candidate ID | Sol decision | Matrix row materiality (canonical) |
|---|---|---|---|---|---|
| astabrief-note.md | `w40-hold-astabrief-20261002` | `evidence:2026-W40:7609eae99dabda8b` | `candidate:2026-W40:00ac1151955c20ff` | Sol r11 IN_WINDOW + MATERIAL direction | HOLD (retained) |
| autosynthdata-note.md | `w40-hold-autosynthdata-20261002` | `evidence:2026-W40:ba72657afb68a868` | `candidate:2026-W40:ba7d989d5b799f66` | Sol r11 IN_WINDOW + MATERIAL direction | HOLD (retained) |

Core r10 matrix IDs, evidence SHAs (`cecb2537…`, `455731c8…`), view SHAs (`f7314f3b…`,
`f3f4fb80…`) per `candidate-matrix-r10-staging.json` / `candidate-id-crosswalk-r10.json`
(unchanged; this manifest introduces NO new canonical IDs).

## Publication restrictions (binding on any downstream use)

1. Neither note is Core-accepted: MUST carry `NOT CORE-SELECTED / NOT PART OF FORMAL
   ARCHITECTURE` labeling wherever rendered; MUST NOT appear in the formal r12 preview
   (they don't — preview keeps both HOLD/NONE), canonical Architecture, or Release PDF
   appendix without a separately authorized human-reviewed supplement process.
2. No timestamp conflation: cite HF article clocks ONLY for the article events; never as
   weight-upload, dataset-creation, code-release, or corporate-page clocks.
3. No license inflation: AstaBrief weights Apache-2.0 vs training mixes CC-BY-NC-4.0
   MUST stay split; AutoSynthData MUST stay method-only (no open-source pipeline claim);
   Gym Apache-2.0 belongs to Gym, not to AutoSynthData.
4. No metric generalization: AstaBrief 51.1/178.5s end-to-end with 2025-era baselines +
   eval-not-rerun caveat; AutoSynthData Hybrid/ITSM publisher-measured SFT-only Gym scope.
5. No post-window contamination: notes MUST NOT pull Oct 6/8/9 items or Cloudflare pair
   into scope; no future-week recategorization.
6. Forward paths (Sol-gated): (a) incorporation as P6a PRIMARY subsections AFTER reviewed
   Core supersession (Issue #562) + Sol re-review; or (b) separate human-reviewed
   publication supplement IF independently authorized. This manifest authorizes neither —
   it only makes the staging reviewable.
