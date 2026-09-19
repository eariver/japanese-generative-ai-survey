# Human Publication Preview dossier — 2026-W38 r2 (Worker-prepared, Human decision pending)

Status: `RELEASE_CANDIDATE / HUMAN_GATE_REACHED / PENDING_HUMAN_DECISION`
Generated: `2026-09-19T17:44:27+09:00` (`2026-09-19T08:44:27Z`, actual system wall clock at generation)

Timestamp basis: this dossier asserts no chronology beyond its own generation instant above, Git commit ordering,
and the correction authorities below. Pre-existing invalid Production State history values remain governed by
`execution/provenance/w38-execution-time-correction-20260919.md` and
`execution/provenance/w38-downstream-monotonicity-note-20260919.md`; all new Stage transitions in this
regeneration used actual wall-clock times. Reviewer attribution: Worker/Agent work is labeled as such throughout;
no Sol or Human verdict is claimed here.

## 1. Exact review identity

- Edition `2026-W38` (WEEKLY + WEEKLY_MAGAZINE), target gate `PUBLICATION_PREVIEW`, revision `r2`
  (regeneration after r1 `REQUEST_CHANGES`; no r2 decision exists).
- Reviewed commit `a55ac5b929221bd133d8a4b819bf960d2104d6c7`: exact branch commit containing current
  Production State, Publication Candidate and Candidate-bound PDF.
- Lifecycle `RELEASE_CANDIDATE`, terminal `HUMAN_GATE_REACHED`, next action `PUBLICATION_PREVIEW`.
- Human decision `PENDING`. No decision is inferred from silence.

## 2. r1 REQUEST_CHANGES provenance (what changed and why)

- Canonical r1 decision: `REQUEST_CHANGES`, revision 1, reviewed `f2306ce4`, boundary `ARCHITECTURE_ESTABLISHED`,
  reviewed_at `2026-09-19T08:00:23Z`, record `sources/2026-W38/gates/reviews/publication-r1.json`.
- Requested changes: (a) Issue #511 TypeSafe/Jev temporal-authority correction; (b) Issue #512 full
  community-ledger reader auditability. Both remain OPEN pending independent Sol verification.
- Architecture approval retained (Human r1 `APPROVED` for r2 content, reviewed `56b6d3d65`); no Architecture
  bytes modified; no Architecture gate reopen. Upstream Discovery/Screening/Evidence/Materiality/Completeness/
  Selection never rerun (frozen counts unchanged: 13 / 12-1 / 9-3 / 11-1-1 / 11-1 / 7 packages).

## 3. Issue #511 repair (Jev two-date temporal model)

- Append-only collector correction: `sources/2026-W38/collectors/primary/corrections/typesafe-jev-temporal-correction-20260919.md`
  (binds original record SHA `9f9c904d`; declares original `published_date_on_page: Sep 15` invalid as
  blog displayed-date authority; original bytes preserved).
- Machine-readable Evidence temporal supplement: `sources/2026-W38/evidence/v2/corrections/typesafe-jev-temporal-correction-r1.json`
  (binds Evidence task `evidence:2026-W38:8a560b86678abd25`; normalized model: blog `2026-09-14` DAY precision,
  founder announcement `2026-09-15T18:17:52.151Z` bound separately; window membership ordinary unchanged).
- Worker re-read disclosure: two independent page fetches at repair time rendered body `Sep 15` with
  demonstrably artifactual `Sep 18` front matter (known fetch-date artifact pattern on this page); the renders
  cannot establish displayed-date authority and do not override the execution-request §8 contract model.
  Recorded transparently in the correction file for Sol verification.
- Reader-facing wording (§15 assertions verified): TypeSafe blog `9月14日付` everywhere (section, deck,
  synthesis, source notes, bibliography with Sep 14 note); founder/creator launch announcement `9月15日`
  only when labeled as such with the direct X status cited separately (`w38x-jev-ceo`); no sentence calls the
  blog itself a Sep 15 publication; temporal confidence stays day-level for the blog.

## 4. Issue #512 repair (public 25-row ledger manifest)

- Reader-facing manifest: `surveys/weekly/2026-W38/community-observation-ledger.md` (SHA `fb150df7`,
  committed as `26284fd2e`, pushed, read back byte-identical). All 25 rows generated from the canonical
  row-level ledger with independently recomputed Snowflake UTCs (all 25 match), 23 `ORDINARY_WINDOW` /
  2 `LATE_BREAKING`, no duplicate URLs/IDs, ordinary accounts 15 = 7+3+5. No candidate/Screening/Selection/
  Evidence/lane/internal vocabulary in the manifest.
- Citation form: the execution request preferred a commit-pinned blob URL, but the frozen reader-surface gate
  deterministically rejects any `surveys/`-containing URL as internal-path leakage
  (`RSG-LEX-INTERNAL-PATHS`), and shared-Core modification is prohibited. This is the exact blocker already
  documented for W36 (`w36-r2-reader-surface-suppression-plumbing-blocker-20260917.md`), where the
  Human-accepted resolution was an Issue-comment citation. Following that convention, the full 25-row table
  is mirrored at `https://github.com/eariver/japanese-generative-ai-survey/issues/512#issuecomment-5740537184`
  (posted `2026-09-19T08:38:53Z`) and the bibliography cites that stable public surface (`w38x-ledger-manifest`).
  The committed manifest file remains the byte-stable audit artifact; the existing 9 representative direct X
  citations are unchanged. Gate scan passes suppression-free (0 findings, 0 suppressions).
- Source Notes / community notes point readers to the full manifest for the exact 25/23/2 claim.

## 5. Actual seven-package/section structure

Approved packages render in drafting order with no add/merge/split/reorder (identifier-preservation PASS 7/7;
draft packages byte-identical to r1 except Jev result prose). Sections: 10-law-vertical, 20-voice-frontier,
30-biology-access, 40-pacing-operational, 50-decision-models (two-date model), 60-agent-harness,
70-image-production, plus frontmatter (Jev wording corrected), 80-week-in-review, 99-source-notes.

## 6. Drafting compression

Moderate-length prose condensed from 7 r2 Draft Results (20 content blocks + 7 boundary blocks). No selected
material or required caveat deleted for page targets. Page allocation is a layout outcome (11 pages).

## 7. Exact source/citation behavior

- Validated source `surveys/weekly/2026-W38/main.tex`; bibliography `references.bib` with 20 entries
  (10 primaries + 9 direct X URLs + Issue-comment ledger mirror, each with `urldate` and bound note).
- Citation scan resolves 20 cited keys to 20 bibliography keys, no missing/unused
  (subject-entity-property-binding PASS 20/20). No internal repository paths or blob URLs as reader sources.

## 8. X/community public auditability

Full 25/23/2 ledger auditable from the Issue #512 comment mirror and the committed manifest file; technical
facts cite primaries separately; late-breaking rows excluded from ordinary totals everywhere; privilege-risk
post retained as counter-signal context only.

## 9. Vendor-claim qualification

Unchanged from r1: all benchmarks vendor/publisher-stated without independent reproduction; `$1B` figures
stated expectations; editorial prose guard PASS on all 13 reader files. Worker semantic/editorial QA: 11 PASS.

## 10. PDF pagination/layout

Exact CI-built PDF (`main.pdf`, 11 pages, 347330 bytes, SHA
`3829c1660b55dbe808b3dec2ee14535bbba60ec6e5268f9a91276b71fae54933`, CI run `35432581167`,
artifact `10581840234`, digest `sha256:fba2b536…`, unencrypted, A4). Text extraction clean (525 lines):
cover → contents → 7 sections (corrected Jev dates present) → week-in-review (next-watch travels with its
boundary box) → sources → 20 references including the ledger mirror. CI succeeded on every TeX push in this
regeneration. Worker visual QA: 2 PASS. p.8 closing-page behavior unchanged from Sol-accepted r1 pattern;
generic #508 hardening remains open and untouched.

## 11. Remaining non-blocking limitations

Same source-backed residuals as r1 (vendor benchmarks unreproduced; webfetch excerpts; hour/day precisions;
DeepSeek primary gap; biomolecular repo not found; E-lane thinness/I-lane quiet; partnership operations
unsettled), plus the #511 worker fetch-observation disclosure above, which Sol should verify.

## 12. Deviations from approved Architecture

None. Seven packages, order, thesis, must-cover items and boundaries preserved; Architecture SHA `c123f9af`
unchanged. Deliberate documented deviation from the execution request's *preferred* citation form (§12
commit-pinned blob URL → Issue-comment mirror) for the frozen-gate reason in §4 above; the preferred form's
target file remains committed and pinned for audit. No other deviation.

## 13. Worker review finding

Blocking: 0. Non-blocking: residuals above. The Candidate is sufficient for Human judgment; the approval
decision belongs to the Human on the exact reviewed bytes via the r2 surface.

## 14. Human decision options

Only after reading this dossier: `APPROVED` (records against `a55ac5b929221bd133d8a4b819bf960d2104d6c7`,
continues to Freeze — not in this run) or `REQUEST_CHANGES` (explicit changes + allowed boundary).
Silence is not a decision. Issues #511/#512 stay open for Sol verification either way.
