# Human Publication Preview dossier — 2026-W39 r1 (Worker-prepared, Human decision pending)

Status: `RELEASE_CANDIDATE / HUMAN_GATE_REACHED / PENDING_HUMAN_DECISION`
Generated: `2026-09-28T09:58:00+09:00` (`2026-09-28T00:58:00Z`, actual system wall clock at generation)

Timestamp basis: this dossier asserts no chronology beyond its own generation instant above and Git commit ordering.
All Production State history `recorded_at` values in this run are actual execution wall-clock times.
Lifecycle/state identities, checkpoint bindings and substantive review findings remain authoritative as those
ledgers describe. Reviewer attribution: Worker/Agent work is labeled as such throughout;
no Sol or Human verdict is claimed here.

## 1. Exact review identity

- Edition `2026-W39` (WEEKLY + WEEKLY_MAGAZINE), target gate `PUBLICATION_PREVIEW`, revision `r1`
  (first Publication Preview presentation; no prior Preview decision exists).
- Reviewed commit `bb6eacabc86e21da77a91d46d4daa2419be5c988`: exact branch commit containing current
  Production State, Publication Candidate and Candidate-bound PDF.
- Lifecycle `RELEASE_CANDIDATE`, terminal `HUMAN_GATE_REACHED`, next action `PUBLICATION_PREVIEW`.
- Human decision `PENDING`. No decision is inferred from silence.

## 2. Architecture approval provenance

- Human Architecture Review r1 `APPROVED` (canonical first Human decision)
  against reviewed production commit `9767d68e0d83aa667eaeeee6394806c612708682`
  (tree `c092b329c8cc1d98a737c6a9d985d4d9e5cb7602`), reviewed_at `2026-09-28T00:24:35Z`
  (actual execution wall clock), reviewed_by Human Owner.
- Record `sources/2026-W39/gates/reviews/architecture-r1.json`, immutable snapshot
  `sources/2026-W39/gates/reviews/approvals/architecture-r1.json`, canonical approval
  `sources/2026-W39/gates/architecture-approval.json`, review index `sources/2026-W39/gates/review-index.json`.
- Upstream Discovery/Screening/Evidence/Materiality/Completeness/Selection/Architecture bytes
  are frozen and unchanged since approval (counts: Discovery 15; Screening 15 KEEP/0 DROP;
  Evidence 8 VERIFIED/7 PARTIAL; Materiality 12 MATERIAL/3 CONTEXT;
  Selection 13 SELECTED/2 HOLD; Architecture 7 packages).

## 3. Actual seven-package/section structure

In drafting order, each with headline, deck, claimboundary and (where applicable) communitynote boxes:
1. `w39-cost-frontier` → `sections/10-cost-frontier.tex` (Sol/Luna + caching + DeepSeek docs context + C1 community note)
2. `w39-frontier-challenger` → `sections/20-frontier-challenger.tex` (Opus 5.5 + C2 community note)
3. `w39-agent-operations` → `sections/30-agent-operations.tex` (harness efficiency + Rollouts/Security, no community note)
4. `w39-coding-models` → `sections/40-coding-models.tex` (Grok 4.7, no community note)
5. `w39-local-inference` → `sections/50-local-inference.tex` (GGUF + C3 community note)
6. `w39-science-eval` → `sections/60-science-eval.tex` (ART + MentalHealthBench + DolphinBench, no community note)
7. `w39-memory-privacy` → `sections/70-memory-privacy.tex` (server-side memory architecture, no community note)
Plus `sections/00-frontmatter.tex` (contents + three This-Week boxes + reading axis),
`sections/80-week-in-review.tex` (FINAL_SYNTHESIS: change/meaning/next-watch + C10 community note),
`sections/99-source-notes.tex` (primary/temporal/vendor/community boundaries + late-only dispositions).

## 4. Drafting compression

- Draft input 4,810 chars across 7 packages expanded into full reader sections; no selected material deleted and no required caveat dropped to hit a page count (no page target exists).
- Coverage is exact: 31/31 must_cover_requirements FULFILLED with reader locations; identifier-preservation PASS 7/7.

## 5. Exact source/citation behavior

- 26/26 cited keys resolve to 26 bibliography keys with no missing or unused keys (SUBJECT_ENTITY_PROPERTY_BINDING PASS).
- Every section sentence carrying a technical fact cites a primary/authoritative entry; vendor figures cite vendor pages with bound notes stating attribution limits.
- Internal `status/materiality` vocabulary never enters bibliography notes; no `sources/` or `surveys/` paths in reader prose or URLs (lexical gate PASSED 0/0 suppression-free).

## 6. X/community public auditability

- 11 direct public X status URLs cited (C1 regression, C2 demos x2, C3 walkthrough + 2 summaries, C10 carry-in x2, late-only C5/C8/C9) plus the committed 26-row public ledger `surveys/weekly/2026-W39/community-observation-ledger.md` referenced by filename.
- No repository Raw paths cited as reader sources; ordinary vs late-breaking boundaries preserved in every community note; momentum never broadened beyond retained supporting accounts.

## 7. Vendor-claim qualification

- All vendor benchmarks (Sol 33.2%, Opus 66.4%, Grok 46.3% and cost-per-task ratios), savings figures (7%, cache discounts), and eval claims carry in-prose attribution plus claimboundary boxes; source-notes vendor boundary restates the rule once more.
- TBC 5x/80%/<0.1% figures excluded from packages entirely (HOLD); Pixel Canary 90.3%/96.8% confined to late-only notes.

## 8. PARTIAL/HOLD/EXCLUDED handling (no internal terms in reader prose)

- PARTIAL authorities surface as readable caveats (pre-print unreviewed, abs-only, audit unverified, grader circularity, effort asymmetry, excerpt-level); the words PARTIAL/HOLD/VERIFIED/Screening/candidate never appear in reader prose (lexical gate confirms).
- HOLD items (TBC commercial context, Pixel Canary/Codex late-only) appear only as bounded context or next-window precursors, never as ordinary facts.

## 9. Japanese prose quality

- Natural technical Japanese throughout; no translated-workflow prose; no `〜として位置づけられる` calques or qualifier dumps; constraints expressed as readable source/evaluation caveats.
- Terminology seed (`docs/editorial/ja-technical-terminology-overtranslation-seed.md`) respected as read-only input: canonical terms preserved (プロンプトキャッシュ, GGUF, Transformers, ベンチマーク, enclave→隔離の座 with gloss); no linter/auto-rewrite implemented; Shared Core untouched.

## 10. PDF pagination/layout

- Exact CI bytes: 12 pages, 323893 bytes, SHA `4e6bf5131dfb744da648907ddaa8f22102b9fccf3ccf5e1c01e2b335eb4c6a6e` (CI run `36363430195`, artifact `10946557163`).
- Cover + contents + This-Week boxes; 7 package sections in drafting order; synthesis with enumerated change/meaning/watch; source-notes plus References (26 entries).
- PDF text-extraction re-check: corrected dates, ledger status IDs, and absence of process-vocabulary/Cyrillic leakage confirmed.

## 11. Remaining non-blocking limitations

- All vendor benchmarks unreproduced; DolphinBench PDF unconsumed; DeepSeek cutover instant unestablished; Pixel Canary methodology/identity and Codex scope unverified; TBC figures quarantined; E/F/D quiet; C sparse; K no new primary release.
- One CI build failure repaired pre-candidate (bib author underscores → W38 X-entry convention); repaired bytes are the reviewed bytes (PDF built from them).

## 12. Deviations from approved Architecture

- None material: 7/7 packages in approved order with approved titles, purposes, must-cover items and boundaries; thesis preserved; HOLDs unpromoted; late-only isolation intact.
- Edition-local incidents (all pre-candidate, documented in session): bib underscore repair; future-`imported_at` on first X record-result (prior run, corrected); validation/advance HEAD-treadmill discipline.

## 13. Worker review finding

- Blocking: 0. Semantic-editorial 11/11 PASS + visual 2/2 PASS + lexical gate PASSED 0/0 + 3 deterministic PASS, all Worker/Agent-attributed; no Sol or Human verdict claimed.
- Machine candidate status READY_FOR_PUBLICATION_PREVIEW is necessary but not sufficient for a Human decision; this dossier exists so the Human can judge both the candidate and whether the pipeline did enough work.

## 14. Human decision options

- `APPROVED` records against the exact reviewed commit above and authorizes Freeze (Freeze itself is outside this run).
- `REQUEST_CHANGES` requires explicit requested changes + one allowed boundary: publication-local (`ARCHITECTURE_ESTABLISHED`, `DRAFT_COMPLETE`, `VALIDATED_DRAFT`) preserves the Architecture approval; upstream of `ARCHITECTURE_ESTABLISHED` reopens Architecture per Core contract with prior approval snapshot preserved.
- Silence is not a decision. No decision is recorded in this run.
