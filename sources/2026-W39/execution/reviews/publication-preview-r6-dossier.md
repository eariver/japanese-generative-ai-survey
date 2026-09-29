# Human Publication Preview dossier — 2026-W39 r6 (Worker-prepared, Human decision pending)

Status: `RELEASE_CANDIDATE / HUMAN_GATE_REACHED / PENDING_HUMAN_DECISION`
Generated: `2026-09-29T09:56:00+09:00` (`2026-09-29T00:56:00Z`, actual system wall clock at generation)

Timestamp basis: this dossier asserts no chronology beyond its own generation instant above and Git commit ordering.
All Production State history `recorded_at` values in this run are actual execution wall-clock times.
Lifecycle/state identities, checkpoint bindings and substantive review findings remain authoritative as those
ledgers describe. Reviewer attribution: Worker/Agent work is labeled as such throughout;
no Sol or Human verdict is claimed here.

## 1. Exact review identity

- Edition `2026-W39` (WEEKLY + WEEKLY_MAGAZINE), target gate `PUBLICATION_PREVIEW`, revision `r6`
  (sixth presentation after r1–r5 `REQUEST_CHANGES`, all at boundary `DRAFT_COMPLETE`).
- Reviewed commit `98cffa3bbaf36801de1d7bcb8b2449cc0bb0b9d6`: exact branch commit containing current
  Production State, Publication Candidate and Candidate-bound PDF.
- Lifecycle `RELEASE_CANDIDATE`, terminal `HUMAN_GATE_REACHED`, next action `PUBLICATION_PREVIEW`.
- Human decision `PENDING`. No decision is inferred from silence.

## 2. Architecture approval provenance

- Human Architecture Review r1 `APPROVED` (canonical first Human decision)
  against reviewed production commit `9767d68e0d83aa667eaeeee6394806c612708682`,
  reviewed_at `2026-09-28T00:24:35Z`, reviewed_by Human Owner.
- Record `sources/2026-W39/gates/reviews/architecture-r1.json`, immutable snapshot
  `sources/2026-W39/gates/reviews/approvals/architecture-r1.json`, canonical approval
  `sources/2026-W39/gates/architecture-approval.json`, review index `sources/2026-W39/gates/review-index.json`.
- r1–r5 Preview `REQUEST_CHANGES` (revisions 1–5, all `DRAFT_COMPLETE`, reviewed `bb6eacab`/`d95a811a`/`4463e80e`/`eb3bb84f`/`342adad3`);
  all publication-local; Architecture approval preserved throughout.
- Upstream Discovery/Screening/Evidence/Materiality/Completeness/Selection/Architecture bytes
  frozen and unchanged since Architecture approval (counts: Discovery 15; Screening 15 KEEP/0 DROP;
  Evidence 8 VERIFIED/7 PARTIAL; Materiality 12 MATERIAL/3 CONTEXT;
  Selection 13 SELECTED/2 HOLD; Architecture 7 packages).

## 3. Issue #551 supplemental repairs (r5→r6 delta)

Two blocking findings, both repaired wording-only (facts, numbers, dates, attribution, caveats, citations
except no key changes, identical):

1. **Official-X provenance boundary contradiction**: `99-source-notes.tex` Community observation boundary
   now states the general context-only rule PLUS the narrow exception (official first-party post explicitly
   cited in the body for its exact announcement fact may serve as primary announcement evidence;
   ledger membership alone never elevates; independent/community rows stay context-only).
   `community-observation-ledger.md` header carries the same exception. `20-frontier-challenger.tex`
   body already bound the claim correctly; `references.bib` unchanged (no key added/removed).
2. **Claude Code date inconsistency**: `99-source-notes.tex` primary-sources list now reads
   `9月25日のClaude Codeの動作変更`; full-surface sweep confirms Sep 25 consistently everywhere for the
   behavior-change event (body, bib entry, ledger row 2026-09-25T19:04:40Z); plan-tier secondary caveat unchanged.

## 4. Actual seven-package/section structure

Unchanged in order, titles, purposes, must-cover items and boundaries; thesis preserved: cheaper, more
operational frontier with attributed numbers and late-only isolation.

## 5. Drafting compression

- No selected material deleted and no required caveat dropped; 31/31 must-cover FULFILLED reconfirmed
  on regenerated manuscript; identifier-preservation PASS 7/7.

## 6. Exact source/citation behavior

- 27/27 cited keys resolve to 27 bibliography keys with no missing or unused keys (rebuilt binding PASS).
- Citation set unchanged in r6 (no key added/removed/renamed).
- Internal vocabulary still absent from bibliography; no `sources/` or `surveys/` paths in reader prose or URLs.

## 7. Vendor-claim qualification

- Unchanged: all vendor benchmarks/savings/eval claims carry in-prose attribution plus claimboundary boxes
  (incl. Opus typical-workload framing and 最大2.5倍 from the r5 cycle); TBC figures still excluded;
  Pixel Canary late-only.

## 8. PARTIAL/HOLD/EXCLUDED handling (no internal terms in reader prose)

- Unchanged dispositions; PARTIAL authorities still surface as readable caveats; HOLD items still bounded
  context/precursors; internal terms still absent from reader prose (lexical gate PASSED 0/0 suppression-free).

## 9. Japanese prose quality

- Four-corpus regression guard re-run over final TeX (compound-aware bad total 0); r5 PASS repairs intact
  (ART system novelty, Cursor proxy strength, Opus typical-workload + 最大2.5倍, DolphinBench v1/v2,
  Claude Code first-party binding); prior terminology repairs intact.
- Final-byte seed-external reread of all changed lines post-edit: no new coined/metaphorical/Chinese-like/
  identity-destroying wording, no new typo (the one r6 sentence with an awkward relative clause,
  `対象期間後の二次資料が伝える`, was already present in r5 and left untouched as out-of-scope).
- New generic defects requiring successor supplement: 0.
- No linter/auto-rewrite implemented; terminology seeds respected as read-only input; Shared Core untouched.

## 10. PDF pagination/layout

- Exact CI bytes: 12 pages, 335817 bytes, SHA `eb0e49233c8f7c04077d9abc04b2811a625597abda1c7340378b1c9f8cc3e121`
  (CI run `36504726702`, artifact `11006941649`; TeX at HEAD byte-identical to CI-built commit).
- Four-surface byte identity independently demonstrated (shell §Reviewed authority): IDENTITY PASS.
- Cover + contents + This-Week boxes; 7 package sections in drafting order; synthesis; source-notes plus
  References (27 entries). No post-repair build failure (repaired TeX built green; artifact pinned).
- PDF text-extraction re-check on exact final bytes: boundary-exception sentences and Sep-25 date present
  (`一次発表として本文で明示的に引用`, `台帳に載っているという事実だけでは`, `9月25日のClaude Codeの動作変更`);
  defective forms absent (`9月23日のClaude Codeの動作変更`); corrected dates, ledger status IDs, and no
  process-vocabulary leakage confirmed (ASCII-adjacent extraction splits verified component-wise).

## 11. Remaining non-blocking limitations

- Same source-backed limits as r5 (vendor benchmarks unreproduced; DolphinBench PDF unconsumed;
  DeepSeek cutover instant unestablished; Pixel Canary/Codex unverified; TBC quarantined; quiet lanes).
- Draft/synthesis internal bytes retain pre-repair wording under the sealed ARCHITECTURE_ESTABLISHED
  checkpoint + Core overwrite refusal (documented per occurrence in r2/r3/r4 ledgers).

## 12. Deviations from approved Architecture

- None material: 7/7 packages in approved order with approved titles, purposes, must-cover items and
  boundaries; thesis preserved; HOLDs unpromoted; late-only isolation intact.
- Edition-local incidents: one wall-clock timestamp slip on first r5 gate recording attempt
  (future reviewed_at estimated instead of measured; Core fail-closed refusal worked as designed;
  tree restored and re-recorded with measured wall clock). No build failure, no validation-report
  deletion, no history rewrite.

## 13. Worker review finding

- Blocking: 0. Semantic-editorial 11/11 PASS + visual 2/2 PASS + lexical gate PASSED 0/0 + 3 deterministic
  PASS, all Worker/Agent-attributed and rebuilt over repaired bytes; no Sol or Human verdict claimed.
- Machine candidate status READY_FOR_PUBLICATION_PREVIEW is necessary but not sufficient for a Human
  decision; this dossier exists so the Human can judge both the candidate and whether the pipeline did
  enough work.

## 14. Human decision options

- `APPROVED` records against the exact reviewed commit above and authorizes Freeze (Freeze itself is outside this run).
- `REQUEST_CHANGES` requires explicit requested changes + one allowed boundary: publication-local
  (`ARCHITECTURE_ESTABLISHED`, `DRAFT_COMPLETE`, `VALIDATED_DRAFT`) preserves the Architecture approval;
  upstream of `ARCHITECTURE_ESTABLISHED` reopens Architecture per Core contract with prior approval snapshot preserved.
- Silence is not a decision. No decision is recorded in this run.
