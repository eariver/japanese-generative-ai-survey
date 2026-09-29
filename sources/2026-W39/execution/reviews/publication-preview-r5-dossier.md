# Human Publication Preview dossier — 2026-W39 r5 (Worker-prepared, Human decision pending)

Status: `RELEASE_CANDIDATE / HUMAN_GATE_REACHED / PENDING_HUMAN_DECISION`
Generated: `2026-09-29T03:37:00+09:00` (`2026-09-28T18:37:00Z`, actual system wall clock at generation)

Timestamp basis: this dossier asserts no chronology beyond its own generation instant above and Git commit ordering.
All Production State history `recorded_at` values in this run are actual execution wall-clock times.
Lifecycle/state identities, checkpoint bindings and substantive review findings remain authoritative as those
ledgers describe. Reviewer attribution: Worker/Agent work is labeled as such throughout;
no Sol or Human verdict is claimed here.

## 1. Exact review identity

- Edition `2026-W39` (WEEKLY + WEEKLY_MAGAZINE), target gate `PUBLICATION_PREVIEW`, revision `r5`
  (fifth presentation after r1–r4 `REQUEST_CHANGES`, all at boundary `DRAFT_COMPLETE`).
- Reviewed commit `342adad3400bd6dee07fb920441f8e259f18eb15`: exact branch commit containing current
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
- r1–r4 Preview `REQUEST_CHANGES` (revisions 1–4, all `DRAFT_COMPLETE`, reviewed `bb6eacab`/`d95a811a`/`4463e80e`/`eb3bb84f`);
  all publication-local; Architecture approval preserved throughout.
- Upstream Discovery/Screening/Evidence/Materiality/Completeness/Selection/Architecture bytes
  frozen and unchanged since Architecture approval (counts: Discovery 15; Screening 15 KEEP/0 DROP;
  Evidence 8 VERIFIED/7 PARTIAL; Materiality 12 MATERIAL/3 CONTEXT;
  Selection 13 SELECTED/2 HOLD; Architecture 7 packages).

## 3. Issue #551 source-fidelity repairs (r4→r5 delta)

All five correction groups verified against accepted Evidence/primary source read-back before editing;
no Evidence escalation was required:

1. **ART** (60-science-eval): primary source re-read confirms RT known from prior jumbo-phage studies,
   novelty at system level (RT + partner gene + long repeat array; short-RNA expression validated;
   function unknown). `新規の逆転写酵素の傍ら…` replaced with `既知の逆転写酵素（RT）遺伝子の隣に、反復配列と未知機能の付随遺伝子からなる未特徴づけの系…ART…三部` wording. Consistent with accepted Evidence (system-level `previously uncharacterized`).
2. **Cursor proxy** (30-agent-operations): collector method note confirms evals-as-proxy strength.
   `proxy指標としての評価は当てにならず` replaced with `evalは速く有用なproxyになり得る一方、難問に偏りやすく、実利用の分布を十分反映しない場合がある`.
3. **Claude Code** (20-frontier-challenger): first-party `@ClaudeDevs` X status URL present in accepted
   Raw ledger (ordinary, Sep 25 19:04 UTC) — no new source needed. Behavior-change claim now cites new
   bib entry `w39x-c2-claudedevs`; plan-tier split stays on post-window secondary `claudecodegraceful`
   (explicitly framed). Citation keys 26→27.
4. **Opus 5.5** (20-frontier-challenger, 00-frontmatter, main.tex deck): `4割減` reframed as
   `典型ワークロードで約4割軽い（Anthropic算定）` per primary-source read-back
   (`at default settings…40% less…on typical workloads`); fast mode now `最大2.5倍の速度`
   per source (`up to 2.5x speed`).
5. **DolphinBench** (60-science-eval, 99-source-notes): `9月21日（改め22日）` replaced with explicit
   `9月21日にv1、22日にv2が公開` per accepted Evidence abs record.

## 4. Actual seven-package/section structure

Unchanged in order, titles, purposes, must-cover items and boundaries; wording-only repairs above
(facts, numbers, dates, attribution, caveats, citations except the one Claude Code rebinding, identical).
Thesis preserved: cheaper, more operational frontier with attributed numbers and late-only isolation.

## 5. Drafting compression

- No selected material deleted and no required caveat dropped; 31/31 must-cover FULFILLED reconfirmed
  on regenerated manuscript; identifier-preservation PASS 7/7.

## 6. Exact source/citation behavior

- 27/27 cited keys resolve to 27 bibliography keys with no missing or unused keys (rebuilt binding PASS).
- One citation key added (`w39x-c2-claudedevs`, first-party X status URL already in accepted Raw);
  all other keys unchanged.
- Internal vocabulary still absent from bibliography; no `sources/` or `surveys/` paths in reader prose or URLs.

## 7. Vendor-claim qualification

- Unchanged except Opus cost/fast-mode fidelity tightening above; all other vendor benchmarks/savings/eval
  claims carry in-prose attribution plus claimboundary boxes; TBC figures still excluded; Pixel Canary late-only.

## 8. PARTIAL/HOLD/EXCLUDED handling (no internal terms in reader prose)

- Unchanged dispositions; PARTIAL authorities still surface as readable caveats; HOLD items still bounded
  context/precursors; internal terms still absent from reader prose (lexical gate PASSED 0/0 suppression-free).

## 9. Japanese prose quality

- Four-corpus regression guard re-run over final TeX: 12 residual forms rechecked, all confined to
  correct compounds/standard senses (製品/見守り/専門家・臨床家/読み込み/再利用窓/難題・話題・取り上げ/画像・音声/台帳/利用枠/検証); Issue #551 repairs introduce no new overtranslation
  (verified: no 卓上版/物差し/待ち受け-class regressions; 最大 hit is the intended `最大2.5倍` fix).
- Final-byte seed-external reread of all sections post-edit: no new coined/metaphorical/Chinese-like/
  identity-destroying wording, no new typo.
- New generic defects requiring successor supplement: 0.
- No linter/auto-rewrite implemented; terminology seeds respected as read-only input; Shared Core untouched.

## 10. PDF pagination/layout

- Exact CI bytes: 12 pages, 335104 bytes, SHA `d81e47c4ab95d8fe4bbdc8330bccb0458849d1785b975d953b5cffbd2b0a156f`
  (CI run `36465420944`, artifact `10989018607`; TeX at HEAD byte-identical to CI-built commit).
- Four-surface byte identity independently demonstrated (shell §Reviewed authority): IDENTITY PASS.
- Cover + contents + This-Week boxes; 7 package sections in drafting order; synthesis; source-notes plus
  References (27 entries). No post-repair build failure (repaired TeX built green; artifact pinned).
- PDF text-extraction re-check on exact final bytes: repaired terms present (既知の逆転写酵素,
  未特徴づけの系, 大規模, 公式発表, 最大2.5倍, 典型ワークロード, 繰り越し可能, v1/v2 dates);
  defective forms absent (新規の逆転写酵素, 当てにならず, unconditional 2.5倍, flat 4割減,
  改め22日); corrected dates, ledger status IDs, and no process-vocabulary leakage confirmed
  (ASCII-adjacent extraction splits verified component-wise).

## 11. Remaining non-blocking limitations

- Same source-backed limits as r4 (vendor benchmarks unreproduced; DolphinBench PDF unconsumed;
  DeepSeek cutover instant unestablished; Pixel Canary/Codex unverified; TBC quarantined; quiet lanes).
- Draft/synthesis internal bytes retain pre-repair wording under the sealed ARCHITECTURE_ESTABLISHED
  checkpoint + Core overwrite refusal (documented per occurrence in r2/r3/r4 ledgers).

## 12. Deviations from approved Architecture

- None material: 7/7 packages in approved order with approved titles, purposes, must-cover items and
  boundaries; thesis preserved; HOLDs unpromoted; late-only isolation intact.
- Edition-local incidents: none in r5 cycle (no build failure, no validation-report deletion,
  no history rewrite).

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
