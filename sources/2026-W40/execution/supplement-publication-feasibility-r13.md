# W40 r13 supplement-publication feasibility — read-only authority/topology study (F01)

Status: `STUDY_ONLY_R13 / NO_RELEASE / NO_APPENDIX / NO_ARCHITECTURE_INSERTION`
Date: 2026-10-10
Reviewed Core: main `afdb3df3faa20af3bb5798be429bba8dbd2100b1` (read, NOT modified)
State: `EVIDENCE_REVIEWED` (no transition attempted or performed)
Scope: authority + delivery-topology investigation + edition-local documentation ONLY.
This study authorizes NO release, NO Human-Gate bypass, NO fake core-accepted appendix,
and NO insertion of notes into `architecture-v2.json`, the ordinary W40 PDF, the Release
bundle, or first-party Source notes. A provisional method/draft delivery plan is
described; no actual release is created.

## 0. Question

Two in-window, Sol-confirmed MATERIAL article events (AstaBrief, AutoSynthData) are
canonically HOLD pending lawful supersession (Issue #562 / CV2-DM-022). The 28-item
preview is formally consistent but not reader-complete. Under CURRENT reviewed-main
contracts, is there a lawful way to give readers those two subjects — (A) as an
independent separately-reviewed supplement, or (B) as a bundled sidecar of the W40
main publication — or (C) is neither available without an unauthorized exception?

## 1. Authority read (exact clauses)

- Production/Publication Profile: `config/survey-production-v2.json` —
  `publication_profiles.WEEKLY_MAGAZINE` (`role_namespace: "WEEKLY_MAGAZINE:"`),
  `human_gates: ["ARCHITECTURE_REVIEW", "PUBLICATION_PREVIEW"]`, lifecycle
  `… EVIDENCE_REVIEWED → SELECTION_COMPLETE → … → RELEASE_CANDIDATE → FROZEN → RELEASED`.
- Selection: `scripts/survey_architecture_v2_base.py::validate_selection` —
  `row["materiality"] in {"NON_MATERIAL","HOLD"}` → `"candidate cannot be SELECTED"`
  (lines ~416-417); non-selected assignments must carry usage NONE + null roles;
  `summary` must recompute from bytes; `basis` must bind exact
  Profile/Matrix/Completeness/Ledger SHAs.
- Architecture: `validate_architecture` (~551-555) builds `selected` ONLY from
  assignments with `disposition == "SELECTED"`; `nonselected` excluded from packages.
- Reader Manuscript: `scripts/survey_reader_publication_v2.py::_validate_manifest_semantics` —
  exactly ONE `primary_source`, which MUST resolve to `survey_root/main.tex`;
  `supporting_files` allowed as SHA-bound role-labeled files; `architecture_coverage`
  must EXACTLY equal the architecture must-cover set (missing OR extra both fail);
  WEEKLY reader requirements = `FINAL_SYNTHESIS + WEEKLY_COMMUNITY_MOVEMENT`.
- Publication Candidate: `scripts/survey_publication_v2.py::build_candidate` /
  `validate_candidate` — binds exactly ONE source + ONE repository-resident PDF +
  manuscript + quality bundle + SEMANTIC_EDITORIAL + VISUAL reviews, all SHA/byte-count
  cross-checked. No appendix/sidecar/supplement slot exists in code or in
  `schemas/publication-candidate-v2.schema.json`.
- Release identity: `scripts/release_identity.py::weekly_release_identity` —
  `ISSUE_ONLY`: tag `weekly/2026-W40`, title `Japanese Generative AI Technical
  Survey — 2026-W40`, single asset `Japanese_Generative_AI_Technical_Survey_2026-W40.pdf`.
  `.github/workflows/survey-production-v2-release.yml` enforces tag/title match and
  exactly ONE asset (duplicate asset names fail closed).
- "Audit sidecar" (`.github/workflows/survey-production-v2-export-publication-preview.yml`,
  "Write exact-byte audit sidecar") is a preview-export transport artifact (copies the ONE
  candidate PDF + audit JSON) — NOT a content-supplement lane.
- "Supplement" elsewhere in Core means pre-acceptance Evidence Authority Supplement
  (`schemas/evidence-authority-supplement-v2.schema.json`,
  `authority_supplement_source_ids`) — evidence gap-fill, NOT a publication supplement.
- State machine locks: `transition_state` permits exactly one forward step
  (`survey_production_v2.py:935-952`); `invalidate_pending_gate` has no configured
  pending Gate at EVIDENCE_REVIEWED (`survey_human_gate_v2.py:1103-1133, 364-409`);
  see edition-local `execution/core-reentry-feasibility-r11.md` (three locks).
- TS-003 precedent (historical ONLY): CV2-DM-021 record in
  `docs/core-v2-deferred-maintenance-summary.md` (~690-730, ~857) — post-`VALIDATED_DRAFT`
  one-off for an already-Human-approved 39pp PDF (`b2de8449…`, 708782 bytes):
  Issue #560, `EXCEPTION_FROZEN` manifest + PR #561, public Release
  `special/vision-multimodal-2026`, `EXCEPTION_RELEASED` record, workflow run
  `37955511006`; normal State REMAINED `VALIDATED_DRAFT`, NO normal FROZEN/RELEASED
  claim. Records: `sources/SP-vision-multimodal-2026/publication/exception-20261010/`.
- Sol constraints: r11 scope decision (Plan B provisional MATERIAL direction, NO final
  allocation/count until amended authority); r12 disposition (Core HOLD is NOT merit
  rejection; no premature acceptance; no ad hoc PDF appendices or post-approval edits);
  r13 instruction §3 (study only); manifest-r13 restrictions (notes stay noncanonical).

## 2. Path A — independent separately-reviewed supplement (non-Core companion)

| Aspect | Assessment |
|---|---|
| What it is | A standalone document (own source bytes, own PDF if any), reviewed by its own Human + semantic/editorial (+ visual if PDF) process, explicitly NOT the Core-approved W40 main-PDF appendix and NOT the core Release identity. |
| Support | No Core clause forbids authoring standalone edition-local documents (r13 notes themselves exist as such). A Human may review any bytes; TS-003 shows distinct exception records can coexist with normal State. |
| Contradictions | (1) It CANNOT use `weekly/2026-W40` Release identity: that tag/title/single-asset triple is ISSUE_ONLY and workflow-enforced exactly-once. Same-tag upload breaks the 1-asset invariant (fail-closed); different-tag upload is not the W40 release. (2) It carries NO Core provenance chain (no Selection binding, no architecture coverage, no manuscript authority) — readers cannot verify it as "W40". (3) The canonical W40 Release would still ship 28-item-incomplete; the companion does not cure reader-facing incompleteness of the issue itself. |
| Provenance/hashes/review | Would need its own SHA-bound review records (authored_by, manuscript-equivalent, QA kinds) designed from scratch + Human approval record; none exists. r13 drafts are explicitly NOT that (no semantic/editorial QA, no visual QA, no PDF). |
| Reader-accessibility | Detached file (repo path or separate tag TBD); high confusion risk (two "W40" documents); must be labeled NON-CORE at every rendering. |
| Compatibility risks | Label drift (companion cited as W40 canon); version skew vs later Core-superseded P6a sections; precedent creep (future editions citing a companion as ordinary). |
| Human decisions required | (i) authorize a non-Core companion as a publication act; (ii) define its review process + labeling + hosting; (iii) accept canonical W40 Release stays 28-item; (iv) accept confusion/skew risks. NONE preapproved. |
| Verdict | LAWFUL ONLY as an explicitly Human-authorized non-Core companion with its own review + labeling. It does NOT complete W40 within Core identity. Feasible-but-insufficient; process design + decisions pending. |

## 3. Path B — true bundled sidecar (HOLD content inside W40 main PDF/Release)

| # | Block (each independently sufficient) |
|---|---|
| B1 | `validate_selection` forbids SELECTED for HOLD rows — the 2 subjects are canonical HOLD. No ordinary Selection can admit them. |
| B2 | `validate_architecture` derives packages from SELECTED only; HOLD content cannot enter `architecture-v2.json` lawfully. |
| B3 | Reader Manifest coverage must EXACTLY equal architecture must-cover: HOLD-derived sections cannot be covered (no lawful package) and uncovered prose breaks the manuscript→architecture authority chain the Human gates attest. |
| B4 | Publication Candidate binds ONE source + ONE PDF with no appendix slot; inserting HOLD prose into `main.tex` outside architecture coverage manufactures exactly the "fake core-accepted appendix" r13 §3 forbids — byte checks might not fire on every such insertion, but the authority chain (Selection→Architecture→Manuscript→Candidate→Preview approval) would be false, and Sol/semantic review must reject it. |
| B5 | Release identity is single-tag/single-asset; a second "sidecar PDF" asset breaks the release workflow fail-closed. |
| B6 | State machine offers no pre-Architecture upstream promotion (CV2-DM-022 three locks); running Selection now would enshrine stale HOLDs or contradict accepted upstream. |

TS-003 does NOT open Path B: it was post-`VALIDATED_DRAFT`, for already-approved bytes,
via a NEW one-off Human Owner exception (Issue #560 + explicit conditional authorization
+ distinct EXCEPTION records + no normal lifecycle claim). W40 is pre-Architecture with
unapproved, unselected content — different lifecycle position, different gap. A W40
content-addition exception would need its own Owner Exception Gate (new issue, exact-byte
freeze-pin, EXCEPTION records, no ordinary-path claim) — NOT preapproved, NOT requested,
and NOT recommended: TS-003 was a *correction* vehicle for approved bytes, not a
*content-expansion* vehicle. Do not infer authority from the fact that GitHub permits
uploads or that an exception occurred once.

Required evidence IF Path B were ever pursued: (i) Issue-#562 Core supersession landed
on main via normal review (designed route: HOLDs become MATERIAL, ordinary chain
Selection→Architecture→Manuscript→Candidate→Preview→Freeze→Release carries them), OR
(ii) a new explicit one-off Owner exception with the TS-003-shaped record set. Neither exists.
Verdict: NOT admissible under current ordinary contracts.

## 4. Path C — result when neither ordinary path serves the bundled goal

For the actual goal — a reader-complete W40 Core publication INCLUDING the two material
subjects under Core identity — current contracts allow NEITHER Path A (wrong identity)
NOR Path B (blocked B1–B6) without an unauthorized exception. Honest result:
**`UNPROVEN / BLOCKED_FOR_FORMAL_PUBLICATION`** for the bundled goal. This is a
documented contract outcome, not a finding of non-materiality (Sol r11 MATERIAL direction
stands) and not a rejection (Core HOLD ≠ merit rejection).

What continues lawfully: noncanonical drafting (r13 notes/ledger/outline), DGX editorial
resolution (preview-r13, validator-clean), staged Architecture preparation (F08), and the
separate Core maintenance path (Issue #562). No ad hoc PDF appendices, no post-approval
edits, no SHA/provenance manufacture.

## 5. Dependencies + next lawful conditions

1. Core maintenance (Issue #562, separate task/branch/review): same-state append-only
   SHA-bound supersession op (per `core-reentry-feasibility-r11.md` §3 sketch or reviewed
   equivalent) → W40 bounded re-entry run regenerates ONLY allowlisted Evidence/Views/
   Materiality/Completeness versions → Sol re-review → Selection continuation
   (EVIDENCE_REVIEWED → SELECTION_COMPLETE) on the new basis → ordinary Architecture →
   manuscript → Candidate → Human Gates → Freeze → Release. The two P6a subsections then
   ride the ordinary chain.
2. If the Human instead wants a Path-A companion: explicit companion authorization +
   review-process definition + labeling/hosting decision (this study does not presume them).
3. If the Human wants a Path-B-shaped exception: Owner Exception Gate with TS-003-shaped
   records (this study does not request it and records its non-transferability).
