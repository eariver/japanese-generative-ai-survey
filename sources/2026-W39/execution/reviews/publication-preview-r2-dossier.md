# Human Publication Preview dossier — 2026-W39 r2 (Worker-prepared, Human decision pending)

Status: `RELEASE_CANDIDATE / HUMAN_GATE_REACHED / PENDING_HUMAN_DECISION`
Generated: `2026-09-28T23:23:00+09:00` (`2026-09-28T14:23:00Z`, actual system wall clock at generation)

Timestamp basis: this dossier asserts no chronology beyond its own generation instant above and Git commit ordering.
All Production State history `recorded_at` values in this run are actual execution wall-clock times.
Lifecycle/state identities, checkpoint bindings and substantive review findings remain authoritative as those
ledgers describe. Reviewer attribution: Worker/Agent work is labeled as such throughout;
no Sol or Human verdict is claimed here.

## 1. Exact review identity

- Edition `2026-W39` (WEEKLY + WEEKLY_MAGAZINE), target gate `PUBLICATION_PREVIEW`, revision `r2`
  (second Publication Preview presentation after r1 `REQUEST_CHANGES` at boundary `DRAFT_COMPLETE`).
- Reviewed commit `d95a811abd014ad4476d8f305b792920aa6e87fe`: exact branch commit containing current
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
- r1 Preview `REQUEST_CHANGES` recorded as revision 1 (boundary `DRAFT_COMPLETE`, reviewed `bb6eacab`,
  record `sources/2026-W39/gates/reviews/publication-r1.json`); publication-local invalidation only
  (checkpoints `DRAFT_COMPLETE`/`VALIDATED_DRAFT` removed and rebuilt; Architecture approval preserved).
- Upstream Discovery/Screening/Evidence/Materiality/Completeness/Selection/Architecture bytes
  frozen and unchanged since Architecture approval (counts: Discovery 15; Screening 15 KEEP/0 DROP;
  Evidence 8 VERIFIED/7 PARTIAL; Materiality 12 MATERIAL/3 CONTEXT;
  Selection 13 SELECTED/2 HOLD; Architecture 7 packages).

## 3. Actual seven-package/section structure

Unchanged from r1 in order, titles, purposes, must-cover items and boundaries; only terminology wording
repaired (facts, numbers, dates, attribution, caveats, citations identical). Sections:
`10-cost-frontier`, `20-frontier-challenger`, `30-agent-operations`, `40-coding-models`,
`50-local-inference`, `60-science-eval`, `70-memory-privacy`, plus frontmatter, week-in-review
synthesis, and source-notes. Thesis preserved: cheaper, more operational frontier with attributed
numbers and late-only isolation.

## 4. Drafting compression

- No selected material deleted and no required caveat dropped; 31/31 must-cover FULFILLED reconfirmed
  on regenerated manuscript; identifier-preservation PASS 7/7.
- r2 delta vs r1 is wording-only (terminology REPLACE per occurrence ledger); no factual, numerical,
  temporal, attributional, evidential, or boundary change.

## 5. Exact source/citation behavior

- 26/26 cited keys resolve to 26 bibliography keys with no missing or unused keys (rebuilt binding PASS).
- Citation set unchanged from r1 (no key added/removed/renamed by terminology repair).
- Internal vocabulary still absent from bibliography; no `sources/` or `surveys/` paths in reader prose or URLs.

## 6. X/community public auditability

- Unchanged: 11 direct public X status URLs plus committed 26-row ledger referenced by filename;
  ordinary vs late-breaking boundaries intact; momentum never broadened.

## 7. Vendor-claim qualification

- Unchanged: all vendor benchmarks/savings/eval claims carry in-prose attribution plus claimboundary boxes;
  TBC figures still excluded from packages; Pixel Canary evals still late-only.

## 8. PARTIAL/HOLD/EXCLUDED handling (no internal terms in reader prose)

- Unchanged dispositions; PARTIAL authorities still surface as readable caveats; HOLD items still bounded
  context/precursors; internal terms still absent from reader prose (lexical gate PASSED 0/0 suppression-free).

## 9. Japanese prose quality

- Full-corpus terminology repair applied: 352 combined forms searched across all reader surfaces;
  649 occurrences adjudicated (REPLACE 335 / RETAIN 314); 171 forms ZERO_HIT_CHECKED.
  All W39-supplement defective forms removed from reader TeX; remaining corpus hits are canonical names,
  standard business/document terms, correct compounds, ordinary verbs, or URL spans (each logged).
- Seed-external residual scan performed over rewritten TeX: additional literary metaphors repaired
  (切れ味, 頂点, 対話欄, 書き残した, 身につけさせた, 補いの学び, 射程, 速さ比べ, 書きぶり, 建て付け,
  作り比べ, 出し先, 解きほぐし, 加入見立て); reviewed-and-retained ordinary words logged
  (挑む者, 試し, 手ほどき, 用立て, 場の声, 力の入れ方, 要約文の数え).
- No linter/auto-rewrite implemented; terminology seed respected as read-only input; Shared Core untouched.

## 10. PDF pagination/layout

- Exact CI bytes: 12 pages, 328743 bytes, SHA `bffda20157e290d95b700c49e7d4fb5c6307e2fcbcd24f7c27cad709176089db`
  (CI run `36434164543`, artifact `10975205959`).
- Four-surface byte identity independently demonstrated (shell §Reviewed authority): IDENTITY PASS.
- Cover + contents + This-Week boxes; 7 package sections in drafting order; synthesis; source-notes plus
  References (26 entries). One r1→r2 CI rebuild cycle: first r2 build failed only before repair existed;
  repaired TeX built green on the first attempt (no post-repair build failure).
- PDF text-extraction re-check on exact r2 bytes: repaired terms present (プロンプトキャッシュ,
  ベンチマーク, エージェント運用, サーバー側メモリ, attestation, 再暗号化, ロールバック);
  defective forms absent (待ち受け, 物差し, 器, 使い手, 符号の新顔, 出荷の番人, 引き継ぎ);
  corrected dates, ledger status IDs, and no process-vocabulary leakage confirmed
  (extraction-dropout artifacts like ログ/セキュア splitting verified against source as present).

## 11. Remaining non-blocking limitations

- Same source-backed limits as r1 (vendor benchmarks unreproduced; DolphinBench PDF unconsumed;
  DeepSeek cutover instant unestablished; Pixel Canary/Codex unverified; TBC quarantined; quiet lanes).
- Draft/synthesis internal bytes retain pre-repair wording under the sealed ARCHITECTURE_ESTABLISHED
  checkpoint + Core overwrite refusal; they are not reader-facing and the DRAFT_COMPLETE boundary
  does not authorize their regeneration (ledger documents per occurrence).
- r1 PDF provenance defect (artifact/sidecar inconsistency observed by Sol on run 36363430195) is superseded by the r2
  four-surface independent demonstration; no Core/CI change was needed. Adjacent runs rebuilding near-identical
  TeX produced different bytes (7700ad9b for the pin commit vs 4e6bf513 pinned), so cross-commit byte comparison
  is not a valid provenance method; same-run artifact↔repo comparison with independent hashing is used instead,
  exactly as performed here.

## 12. Deviations from approved Architecture

- None material: 7/7 packages in approved order with approved titles, purposes, must-cover items and
  boundaries; thesis preserved; HOLDs unpromoted; late-only isolation intact.
- Edition-local incidents: bib-underscore repair carried over from r1 run (already in reviewed bytes);
  no new build failures; no validation-report deletions; no history rewrite.

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
