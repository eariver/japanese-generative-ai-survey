# SOL W40 r13 handoff — editorial repair + DGX disposition + supplement feasibility (REVIEW REQUIRED)

Status: `SOL_W40_R13_EDITORIAL_AND_PUBLICATION_FEASIBILITY_REVIEW_REQUIRED`
Date: 2026-10-10
Branch (existing only): `weekly/2026-W40-v2-work` — normal commits + non-force push ONLY.
Authorizing inputs: `execution/instructions/2026-10-10_muse-w40-r13-editorial-repair-and-supplement-feasibility.md`
(Sol-bounded) + `execution/reviews/sol-w40-r12-independent-audit-disposition-20261010.md`
(`REVISION_REQUIRED` accepted, r13 repair authorized, Selection Acceptance HOLD).

## 1. Git authority (exact bytes)

- Starting remote HEAD (verified read-only BEFORE any write, via `git ls-remote` + GH API
  commit read — zero local writes): `46f03905edb3bffa9ea054403ace8f64ef239d52` ==
  outer Exact Starting SHA; its tree `df53c37849f356c044569d67dc81f962eb3091f9` ==
  Expected Starting Tree; remote `main` == `afdb3df3faa20af3bb5798be429bba8dbd2100b1`
  == reviewed main; remote HEAD == main. ALL MATCH → proceeded.
- Local workspace was 1 commit behind (`e7e84c281…`); aligned by `git fetch` +
  `git merge --ff-only` (no reset/rebase/force/new branch). Post-align HEAD/Tree ==
  Starting SHA/Tree exactly.
- Pre-write guards (all PASS): State `EVIDENCE_REVIEWED`, next `stage:selection`,
  selection/architecture checkpoints pending, both Human Gates pending with null
  provenance; accepted 37 Discovery / 37 Screening / 35 Cards / 35 Views /
  37 Materiality rows; checkpoint SHAs `bc61fda4…` / `10b3335c…` / `19214802…` all match
  State provenance. No new/review/fallback branches; no State/checkpoint/Gate edits;
  no `scripts/`/`schemas/`/`config/`/`.github/`/main/other-edition/shared-Core-doc writes
  (working tree `git status` clean except pre-existing untracked `scripts/__pycache__/`).
- This run: W40-local commits only (list at §7); final HEAD/Tree reported after push in
  the outer completion report (this file written pre-push; push is non-force FF).

## 2. Changed paths (W40-local only, 10 new files)

1. `execution/editorial-supplement/r13/astabrief-note-r13.md` (F05 repair)
2. `execution/editorial-supplement/r13/autosynthdata-note-r13.md` (F03/F04/F05 repair)
3. `execution/editorial-supplement/r13/evidence-source-ledger-r13.md` (F06 re-retrieval)
4. `execution/editorial-supplement/r13/manifest-r13.md` (bindings + restrictions)
5. `execution/selection/selection-preview-r13.json` (F02; SHA `dc024778…`)
6. `execution/selection/selection-validation-r13.md` (validator record, PASS)
7. `execution/selection/count-audit-r13.json` (machine recount)
8. `execution/supplement-publication-feasibility-r13.md` (F01 study)
9. `execution/architecture-staged-outline-r13.md` (F08 staging + matrices)
10. This handoff `execution/SOL_W40_R13_EDITORIAL_AND_SUPPLEMENT_FEASIBILITY_HANDOFF.md`
    (+ `execution/index.md` r13 entry + `execution/sessions/muse-w40-r13-20261010.md` log)
- r12 notes/ledger/manifest/preview/outline preserved immutable (review evidence).
- Counts: 35 assigned = 28 SELECTED (20 PRIMARY / 8 SUPPORTING, machine-verified) +
  4 HOLD + 3 REJECT + 0 INSPECT. Basis SHAs unchanged
  (`c921bd14…` / `f07b1166…` / `f83b2d94…` / `ce63f3a9…`).
- Core validator: `survey_architecture_v2_base.py::validate_selection` on UNMODIFIED
  reviewed-main Core → **PASS (0 errors)** for preview-r13. (Had it disagreed, the unit
  would have stopped with validator errors — it did not.)

## 3. Finding-by-finding closure (W40-R12-F01–F09)

| Finding | Severity | r13 status |
|---|---|---|
| F01 lawful reader-facing distribution | MAJOR | INVESTIGATED, HONEST RESULT (see §4). Bundled goal: `UNPROVEN / BLOCKED_FOR_FORMAL_PUBLICATION` under current ordinary contracts. Path A lawful ONLY as explicitly Human-authorized non-Core companion (insufficient for W40 identity). Path B blocked (B1–B6). Noncanonical drafting continues; #562 Core path pending. No release/appendix/bypass created. |
| F02 DGX Spark exclusion | MAJOR | RESOLVED editorially. Preview-r13: DGX INSPECT→REJECT with Sol-worded rationale (in-window 13:00:39Z ordinary-eligible preserved; 64GB SKU + Sync Cluster Assistant + Oct 23 $4,999 third-party FUTURE preserved; preorder≠shipment; substance/priority insufficient vs P1–P7). Validator PASS. Evidence/Materiality bytes untouched. Still NOT full editorially-sufficient Selection (HOLDs remain). |
| F03 verifier soundness/completeness | MINOR | CORRECTED. Triad restored (consistency + soundness=reject-failures + completeness=accept-valid-alternatives) with positive/negative accept/reject examples; r12's inverted soundness gloss fixed. |
| F04 no-release wording | MINOR | CORRECTED. Bounded form ("not independently identified in bounded checked sources at retrieval time"); 401/empty ≠ absence proof; article's own models/datasets-mentioned sections corroborate no release claim. |
| F05 AstaBrief/AutoSynthData numbers | MINOR | CORRECTED from primary sources re-read 2026-10-10: 47K→(density≥0.25)→39.5K lineage per SFT card (threshold used ONLY because card states it); ~6K vs 6,622 rows; judges + pairwise-prompt link; 95% HEDGED (sample size/conditions undisclosed in article AND card); Hybrid/ITSM symmetric table (pp vs % distinct, ITSM-first ordering); third-party-terms boundary sentence (card license section); speed-framing split; 2025-vintage/no-rerun/no-SOTA; grounding/density/precision/scope-drift kept distinct. |
| F06 JSON-LD re-capture | OBS | CLOSED stronger than asked. Both HF pages re-fetched (curl, 2026-10-10): byte counts EXACTLY reproduce r11 (169,199 / 210,484) while SHA256 differ (`49e4b99b…` / `1e5af1b3…`) — dynamic framing PROVEN, JSON-LD strings authoritative and VERBATIM re-verified (both clocks/authors/publisher/canonical match r12). Min quoted excerpts + method/URL/byte framing recorded in ledger-r13. Raw bytes uncommitted (policy). HF-API timestamps + corporate RSS carried as such (not re-queried). |
| F07 validator-execution distinction | OBS | PRESERVED. r13 validation record states direct Python `validate_selection` execution by Muse vs independent equivalent-logic check boundary (no false execution claim). |
| F08 deep staged Architecture | OBS | STAGED. Outline-r13: P1–P8 for 28 + COND-A/COND-B P6a modules at r13-corrected density; full depth reserved for ContextLM, Olmo-core 3, AgentPerf, OpenTTS, RL-Env Hub; coverage matrices (28+2) with source/mechanism/metric-denominator/baseline/license/validity columns; decision table (28 / 2 HOLD / DGX REJECT / W39 HOLDs / other REJECTs); reader-today vs staged-only split. NO canonical Architecture artifacts/checkpoints. |
| F09 Core debt tracking | OBS | PRESERVED. #562 / CV2-DM-022 cited as the designed route; never marked CORE_FIXED; no shared-Core writes. |

## 4. Supplement feasibility matrix (study only)

- Path A (independent separately Human-reviewed companion, non-Core identity): LAWFUL ONLY
  with explicit Human authorization + own review process + labeling + hosting; does NOT
  complete W40 (canonical Release stays 28-item; confusion/skew risks). Feasible-but-insufficient.
- Path B (bundled sidecar in main PDF/Release): BLOCKED under current ordinary contracts
  (B1 selection HOLD-bar, B2 architecture SELECTED-only, B3 manuscript coverage equality,
  B4 single-source/single-PDF candidate with no appendix slot, B5 single-asset release
  identity, B6 pre-Architecture promotion gap). TS-003 (#560/PR #561/EXCEPTION records/
  run 37955511006) is NON-TRANSFERRABLE (post-`VALIDATED_DRAFT` correction of approved
  bytes ≠ pre-Architecture content expansion). New Owner exception neither preapproved
  nor requested.
- Path C result: bundled goal `UNPROVEN / BLOCKED_FOR_FORMAL_PUBLICATION`; NOT a
  materiality rejection. Dependencies: (1) #562 Core supersession → bounded re-entry →
  Sol re-review → ordinary chain; (2) Path-A companion authorization (Human);
  (3) Path-B-shaped exception (Owner Gate; not recommended/requested).
- Full clause-level evidence: `execution/supplement-publication-feasibility-r13.md`.

## 5. New technical claims — independent evidence + uncertainty

All article prose re-read live 2026-10-10 (rendered fetch) + dataset cards (SFT Mix,
DPO Mix) + direct byte capture (`curl`) + JSON-LD parse. Uncertainties honestly kept:
95% without N/conditions; HF-API repo timestamps carried (not re-queried); teacher model
identifiers verbatim (no registry proof); no independent repro of quality/speed; ITSM
verifier-gap numbers not reported in article (not imputed); DGX page not re-fetched
(r6/r7 delegated read stands). No claim exceeds its cited source (see notes/ledger).

## 6. Canonical State / Human Gate readback (UNMODIFIED)

`lifecycle_state: EVIDENCE_REVIEWED`, `next_action: stage:selection`,
`human_gates: {architecture_review: pending, publication_preview: pending}`,
`human_gate_provenance: {…: null, …: null}`, selection/architecture/draft/validation/
publication_preview/freeze/release checkpoints pending, `target_gate: ARCHITECTURE_REVIEW`,
`exception_gate: inactive`. NO formal Selection Acceptance, NO stage transition,
NO checkpoint write, NO Human Gate action, NO Freeze/Release in this unit.

## 7. Commits (this run; non-force, FF)

- Content commit(s) + readback/close-out commit on `weekly/2026-W40-v2-work` (exact SHAs
  in outer completion report). Ancestry: children of `46f03905…`, no force.

## 8. Next lawful conditions

- Editorial: Sol r13 review of this handoff (`SOL_W40_R13_EDITORIAL_AND_PUBLICATION_FEASIBILITY_REVIEW_REQUIRED`
  — the terminal boundary; stop here).
- Canonical: (a) #562 Core supersession reviewed onto main → bounded W40 re-entry run
  (allowlisted Evidence/Views/Materiality/Completeness versions only) → Sol re-review →
  Selection continuation; or (b) Human companion/exception decisions per §4 (not presumed).
- Canonical 28-item Selection is still NOT editorially sufficient (HOLDs staged, not admitted).
