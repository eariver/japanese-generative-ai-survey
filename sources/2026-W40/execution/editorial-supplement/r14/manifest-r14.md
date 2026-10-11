# r14 supplement manifest — traceability + publication restrictions (staged, NOT canonical)

Status: STAGED_R14 / NON_CANONICAL
Supersedes as working manifest (r12/r13 preserved immutable):
`../r12/manifest-r12.md`, `../r13/manifest-r13.md`
Scope: ties r14 revised/corrected material to canonical IDs, Sol decisions, matrix IDs,
and restrictions. Introduces NO new canonical IDs, NO canonical Evidence/Views/Ledger
bytes, NO Selection/Architecture/Gate changes.

## Bindings

| r14 artifact | Revises / corrects (immutable) | Discovery ID | Evidence task ID | Matrix candidate ID | Sol decision | Canonical materiality |
|---|---|---|---|---|---|---|
| `autosynthdata-note-r14.md` (§3/examples only) | `../r13/autosynthdata-note-r13.md` §3 | `w40-hold-autosynthdata-20261002` | `evidence:2026-W40:ba72657afb68a868` | `candidate:2026-W40:ba7d989d5b799f66` | Sol r11 IN_WINDOW + MATERIAL direction; r13-F06 repair accepted | HOLD (retained) |
| `evidence-source-provenance-correction.md` (interpretations only) | `../r13/evidence-source-ledger-r13.md` §0 + dependent wording | both supplement subjects (see ledger) | both task IDs above + `evidence:2026-W40:7609eae99dabda8b` | both candidate IDs above | r13-F04/F08 correction accepted | HOLD (retained) |
| (AstaBrief technical material) | `../r13/astabrief-note-r13.md` — NO r14 repair (auditor: substantially accurate) | `w40-hold-astabrief-20261002` | `evidence:2026-W40:7609eae99dabda8b` | `candidate:2026-W40:00ac1151955c20ff` | preserved as-is | HOLD (retained) |

Core r10 matrix IDs, evidence SHAs (`cecb2537…`, `455731c8…`), view SHAs (`f7314f3b…`,
`f3f4fb80…`) per `candidate-matrix-r10-staging.json` / `candidate-id-crosswalk-r10.json`
(unchanged).

## Claim/limit audit (r14 delta)

- New/changed claims: verifier gate-to-property assignment + finite-test limit + five
  fixture examples (illustrative, Gym-internals-claiming nothing); retrieval clock
  correction (10:57Z ±60s, +0900-mtime evidenced); causation downgrade (bytes-differed
  only); auditor-boundary distinction (Muse re-parse vs no independent ms extraction).
- No new release/license/metric/clock claims. AstaBrief material untouched by design.

## Publication restrictions (binding, carried + r14-amended)

1. Neither note is Core-accepted: MUST carry `NOT CORE-SELECTED / NOT PART OF FORMAL
   ARCHITECTURE` labeling wherever rendered; MUST NOT appear in any formal preview
   (they don't — both HOLD/NONE), canonical Architecture, or Release PDF appendix
   without a separately authorized human-reviewed supplement process.
2. No timestamp conflation: HF article clocks ONLY for article events; never for
   weight/dataset/code/corporate clocks. Retrieval clock is 10:57Z ±60s (corrected);
   raw capture hashes are transport observations, never clocks.
3. No license inflation: weights Apache-2.0 vs mixes CC-BY-NC-4.0 split; third-party-
   terms sentence is a boundary, not a grant; AutoSynthData method-only with F04
   bounded release wording; Gym Apache-2.0 belongs to Gym.
4. No metric generalization: 51.1/178.5s end-to-end vs generation-time framing split;
   2025-era + no-rerun + no-SOTA; hedged 95%; Hybrid/ITSM SFT-only Gym scope, pp vs %
   distinct, ITSM-first ordering; finite tests prove no universal verifier property.
5. No post-window contamination; no future-week recategorization.
6. Forward paths (Sol-gated): (a) P6a PRIMARY subsections AFTER reviewed Core
   supersession (#562) + Sol re-review; or (b) separately Human-authorized supplement
   IF independently authorized (see `supplement-publication-feasibility-r14.md`,
   STUDY ONLY). This manifest authorizes neither.
