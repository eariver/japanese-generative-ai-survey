# r13 supplement manifest — traceability + publication restrictions (staged, NOT canonical)

Status: STAGED_R13 / NON_CANONICAL
Supersedes (as working manifest; r12 preserved immutable): `../r12/manifest-r12.md`
Scope: ties r13 revised notes to canonical IDs, Sol decisions, matrix IDs, and restrictions.

## Bindings

| Note (r13) | Revises (r12, immutable) | Discovery ID | Evidence task ID | Matrix candidate ID | Sol decision | Matrix row materiality (canonical) |
|---|---|---|---|---|---|---|
| astabrief-note-r13.md | astabrief-note.md | `w40-hold-astabrief-20261002` | `evidence:2026-W40:7609eae99dabda8b` | `candidate:2026-W40:00ac1151955c20ff` | Sol r11 IN_WINDOW + MATERIAL direction | HOLD (retained) |
| autosynthdata-note-r13.md | autosynthdata-note.md | `w40-hold-autosynthdata-20261002` | `evidence:2026-W40:ba72657afb68a868` | `candidate:2026-W40:ba7d989d5b799f66` | Sol r11 IN_WINDOW + MATERIAL direction | HOLD (retained) |

Core r10 matrix IDs, evidence SHAs (`cecb2537…`, `455731c8…`), view SHAs (`f7314f3b…`,
`f3f4fb80…`) per `candidate-matrix-r10-staging.json` / `candidate-id-crosswalk-r10.json`
(unchanged; this manifest introduces NO new canonical IDs).
Ledger: `evidence-source-ledger-r13.md` (re-verified JSON-LD + dataset-card annex).

## Related r13 disposition (recorded here for completeness, owned by preview-r13)

- DGX Spark `candidate:2026-W40:071ac2e6d62319fd`: Sol r13 editorial REJECT as standalone
  narrative item; `selection-preview-r13.json` changes disposition INSPECT→REJECT with
  Sol-worded rationale only. DGX evidence/Materiality bytes untouched.

## Publication restrictions (binding on any downstream use)

1. Neither note is Core-accepted: MUST carry `NOT CORE-SELECTED / NOT PART OF FORMAL
   ARCHITECTURE` labeling wherever rendered; MUST NOT appear in the formal r13 preview
   (they don't — preview keeps both HOLD/NONE), canonical Architecture, or Release PDF
   appendix without a separately authorized human-reviewed supplement process.
2. No timestamp conflation: cite HF article clocks ONLY for the article events; never as
   weight-upload, dataset-creation, code-release, or corporate-page clocks. New r13
   byte/hash evidence distinguishes dynamic framing (hash drift) from authoritative
   JSON-LD strings — cite the strings, never the raw hashes, as clocks.
3. No license inflation: AstaBrief weights Apache-2.0 vs training mixes CC-BY-NC-4.0
   MUST stay split; third-party-terms sentence is a boundary, not a grant;
   AutoSynthData MUST stay method-only with F04 bounded release wording (no
   open-source pipeline claim); Gym Apache-2.0 belongs to Gym, not to AutoSynthData.
4. No metric generalization: AstaBrief 51.1/178.5s end-to-end (vs generation-time
   "nearly order of magnitude") with 2025-era baselines + eval-not-rerun caveat;
   95% judge–human agreement cited ONLY with undisclosed-sample-size hedge;
   AutoSynthData Hybrid/ITSM publisher-measured SFT-only Gym scope, pp vs % distinct,
   ITSM-first ordering preserved.
5. No post-window contamination: notes MUST NOT pull Oct 6/8/9 items or Cloudflare pair
   into scope; no future-week recategorization.
6. Forward paths (Sol-gated): (a) incorporation as P6a PRIMARY subsections AFTER reviewed
   Core supersession (Issue #562) + Sol re-review; or (b) separate human-reviewed
   publication supplement IF independently authorized (see
   `execution/supplement-publication-feasibility-r13.md` — authorized as STUDY ONLY).
   This manifest authorizes neither — it only makes the staging reviewable.
