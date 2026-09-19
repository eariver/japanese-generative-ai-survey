# W37 execution instruction — Human Publication Preview r1 REQUEST_CHANGES via canonical revision path, no Core change

Status: `EXECUTION_AUTHORITY / HUMAN_PUBLICATION_PREVIEW_R1_REQUEST_CHANGES / CANONICAL_REVISION_PATH / REGENERATE_FROM_ARCHITECTURE_ESTABLISHED / NO_CORE_CHANGE / BOUNDED_AT_FRESH_PUBLICATION_PREVIEW_R2`

Date: `2026-09-19 JST`

Repository: `eariver/japanese-generative-ai-survey`

Branch: `weekly/2026-W37-v2-work`

## 1. Why this replacement instruction exists

The prior execution request:

`sources/2026-W37/execution/requests/sol-w37-publication-preview-r1-request-changes-language-provenance-20260919.md`

correctly attempted operator invalidation of an unpresented pending Publication Preview.

Current reviewed Core rejected that path because:

1. `invalidate-pending-gate` forbids Publication Preview invalidation while an active Human Architecture approval exists;
2. operator pending-Gate invalidation also requires no existing Human review records.

The stopped Muse run made zero repository/GitHub writes.

Do **not** change shared Core to bypass those guards.

Current Core already provides the correct supported mechanism:

`survey_human_gate_v2.py request-publication-preview-revision`

with `regeneration_boundary=ARCHITECTURE_ESTABLISHED`.

Current implementation explicitly preserves an active approved Architecture Review at this boundary because:

`_reopens_architecture("ARCHITECTURE_ESTABLISHED") == False`.

This replacement request supersedes only the operational invalidation method in the prior request. The substantive Sol findings and repair requirements remain controlling.

## 2. Human decision authority

The Human Owner has now explicitly instructed that W37 continue **without Core v2 changes** and that the Publication Preview r1 defects identified by Sol be corrected.

For current Core semantics, record the exact reviewed W37 Publication Preview r1 as:

`REQUEST_CHANGES`

This is now a Human Publication Preview decision.

Requested changes are exactly the blocking findings in:

`sources/2026-W37/execution/reviews/sol-w37-publication-preview-r1-independent-review-20260919.md`

namely:

1. Issue #501 recurrence — reader-facing technical Japanese is semantically degraded by forced/novel Japanese substitutions;
2. Issue #506 recurrence — worker semantic/visual reviews falsely use `ChatGPT (Muse Spark)` reviewer identity instead of actual Worker/Muse provenance.

No additional Human defect is implied.

## 3. Exact reviewed r1 authority

Publication Preview r1 reviewed production authority:

- reviewed repository commit: `8057a468897f67d3a11bd9287f6f56f0485877ce`
- candidate SHA-256: `1dfb87957cbab69e30c08a45c66e72b28c72d74d1272a3c3815ab6844445bef6`
- PDF path: `surveys/weekly/2026-W37/main.pdf`
- PDF SHA-256: `08ceb5e9c90b2bf25541bb61e6b14e5b2cdc7fe48635d85c5ab798606b88fd4d`
- PDF bytes: `301238`
- PDF pages: `10`

Publication Preview r1 shell:

`sources/2026-W37/execution/reviews/publication-preview-r1.md`

Independent Sol r1 review:

`sources/2026-W37/execution/reviews/sol-w37-publication-preview-r1-independent-review-20260919.md`

## 4. Invocation guard

The Muse invocation MUST provide the Exact Starting SHA/tree corresponding to the commit containing this replacement execution request.

Before any write, read-only verify:

- remote W37 HEAD == Exact Starting SHA supplied by invocation;
- remote W37 tree == Exact Starting Tree supplied by invocation;
- Exact Starting SHA parent == `bc280c43ea417dae4f8c25abe9bb7b00feb640d8`;
- parent tree == `3d1b15a1f4e48e4afbc548e6a5f46e8c200e6a6c`;
- remote `main` HEAD == `6aa385cbe287b9b20fac4ea3a61d8ffd6179ed3b`;
- remote main tree == `62cf5dfb30cc692cd19c11289fa80c837fd17b66`;
- remote `production/survey-core-v2` HEAD == `774dd39a951c9ac3818e83dfffd4c7666efb0a20`;
- Production Line tree == `cd46a6f7a6dcc4031e76220cea4c52c7dd1fc481`;
- Production State remains:
  - lifecycle `RELEASE_CANDIDATE`
  - next action `PUBLICATION_PREVIEW`
  - terminal `HUMAN_GATE_REACHED`
  - Architecture Review `approved`
  - Publication Preview `pending`;
- canonical Architecture Human review remains revision `1` APPROVED;
- no Publication Preview Human review record exists yet;
- exact r1 candidate/PDF authority matches §3;
- Sol Publication Preview r1 review remains `REQUEST_CHANGES`.

Any mismatch -> zero writes, report expected vs actual, STOP.

No new/fallback/repair/review/temp branch.
No force/reset/rebase/squash/history rewrite.

## 5. Mandatory preflight

Before executing the Human decision, inspect current:

- `scripts/survey_human_gate_v2.py`
- `config/survey-production-v2.json`

and confirm:

1. `PUBLICATION_PREVIEW` is pending;
2. `human_gate_revision_boundaries.PUBLICATION_PREVIEW` includes `ARCHITECTURE_ESTABLISHED`;
3. `_reopens_architecture("ARCHITECTURE_ESTABLISHED")` is false;
4. `_revised_state` therefore preserves:
   - `human_gates.architecture_review == approved`
   - Architecture approval provenance;
5. current Publication Preview next Human revision is exactly `1`.

If any of these do not hold, STOP without writes.

Do not call `invalidate-pending-gate` again.

## 6. Record Human Publication Preview r1 REQUEST_CHANGES canonically

Use current canonical command:

`request-publication-preview-revision`

Required semantics:

- state: `sources/2026-W37/production-state.json`
- expected revision: `1`
- regeneration boundary: `ARCHITECTURE_ESTABLISHED`
- decision: implicit command semantics `REQUEST_CHANGES`
- reviewed_by: `Human Owner`
- reviewed repository commit: `8057a468897f67d3a11bd9287f6f56f0485877ce`
- review reference:
  - this replacement execution request;
  - `publication-preview-r1.md`;
  - `sol-w37-publication-preview-r1-independent-review-20260919.md`.
- requested changes summary:
  - Issue #501 W37 reader-facing technical Japanese repair;
  - Issue #506 worker reviewer-provenance repair;
  - preserve all r1 factual/citation/temporal successes.

Use actual execution timestamp produced at decision-recording time. Do not invent a historical exact timestamp.

After command execution, read back:

- `gates/reviews/publication-r1.json` or exact current canonical generated path;
- review index;
- Production State;
- remaining Architecture approval record/snapshot.

Required post-decision state:

- lifecycle `ARCHITECTURE_ESTABLISHED`;
- Architecture Review remains `approved`;
- Architecture approval provenance remains present and byte-valid;
- Publication Preview returns to `pending`;
- Draft / validation / publication downstream checkpoints become pending as current Core specifies;
- Human Publication Preview r1 `REQUEST_CHANGES` is preserved historically;
- no Human Architecture reopen.

If Architecture approval is removed at this exact boundary, STOP and report. Do not reconstruct it manually.

## 7. Frozen upstream authority

Do not rerun or modify:

- Grok/X;
- Discovery;
- Screening;
- Evidence;
- Materiality;
- Completeness;
- Selection;
- Architecture r2;
- Architecture Human approval.

Frozen values remain:

- Discovery: 14
- Screening: 13 KEEP / 1 DROP
- Evidence: 11 VERIFIED / 2 PARTIAL
- Materiality: 12 MATERIAL / 1 CONTEXT / 1 EXCLUDED
- Selection: 12 SELECTED / 1 HOLD
- Architecture: 7 packages
- Architecture SHA-256: `81e87a64c2418c71340ee8cc1dec28267a55055d2c02d7dbb06e33623efdfcfb`.

No fresh research.

## 8. Draft regeneration is required

The #501 defect exists inside canonical r1 Draft Results, so regenerate Draft from the same approved Architecture and frozen Evidence.

Do not simply hand-edit TeX while leaving defective Draft authority.

Regenerate all seven packages and profile synthesis.

The semantic/content boundaries must remain unchanged; only publication-quality expression may improve.

## 9. Issue #501 — reader-facing technical Japanese repair

Perform semantic drafting in natural technical Japanese.

The rule is:

`technical meaning -> established Japanese technical expression`

not:

`English token -> forced Japanese dictionary substitute`.

A technically literate Japanese reader must not need to reverse-engineer the English term.

### Terms that must be reviewed contextually

Use conventional terminology where appropriate:

- AI model -> `モデル`, `言語モデル`, `テキストモデル`
- code/coding -> `コード`, `コーディング`
- token -> `トークン`
- agent -> `エージェント`
- agent harness -> `エージェントハーネス` or a precise contextual explanation
- sandbox -> `サンドボックス`
- serving -> `サービング`, `推論サービング`, `推論基盤`
- engine -> `エンジン`
- license -> `ライセンス`, `利用条件`
- model card -> `モデルカード`
- translation -> `翻訳`
- MoE -> `MoE`, `Mixture-of-Experts`, `混合エキスパート`
- judge model -> `評価用モデル` or another precise conventional term
- IOC -> `IOC`, `侵害指標`.

Do not use the r1 forced expressions where they represent these technical meanings:

- 模型
- 符号
- 代理人
- 砂場
- 給仕
- 引擎
- 許し
- 札
- 訳し
- 混合専門家
- 検出子.

This is not a blind forbidden-word replacement rule. A word may appear in ordinary Japanese with a genuinely different meaning; evaluate semantics.

### Rewrite r1 editorial calques

Rewrite contextually, not mechanically:

- 「金融向けの整え」
- 「三つの出し分け」
- 「効率旗艦」
- 「声の層」
- 「読みの偏り付け」
- 「雲の上の代理人」
- 「公開試し」
- 「互換の経路」
- 「求めを振り替える」
- 「開かれた重みは縦に伸びる」
- 「安全の物差し」.

Prefer plain, professional Japanese used by AI/software engineers.

Katakana and English technical terminology are allowed when they are the clearest conventional choice.

## 10. Preserve factual/evidence boundaries

Language repair must not change factual authority.

Preserve all r1 successes:

### OpenAI
- Financial Services uses Astra;
- GPT-Live-1 is distinct;
- Agents API is distinct;
- no collapse into one Astra product.

### DeepSeek
- performance comparison is vendor-reported;
- independent reproduction absent;
- Sep 14 routing is future/post-window;
- in-window pricing separate.

### Cognition
- Fusion exact publication time `2026-09-11T17:00:00Z`;
- 39% is table maximum;
- methodology/partner bounds retained.

### Open weights
- MiniCPM/North/Ling vendor/card claims remain bounded;
- North judge/license bounds exact;
- Ling timing uncertainty retained.

### Anthropic
- report is Sep 10 ordinary;
- cases are vendor investigations;
- notable examples not population-wide;
- full PDF/IOCs not consumed;
- late detail not backdated.

### Negative/context items
- resignation discourse not Architecture-bearing;
- GLM rumor excluded.

## 11. Issue #506 — reviewer provenance repair

All Worker-generated QA/review artifacts must identify the actual runner.

Required reviewer style:

`Worker/Agent (Muse Spark)`

or an equivalent truthful actual-runner identity.

Forbidden in Muse-generated review authority:

- `ChatGPT (Muse Spark)`
- `Genuine ChatGPT ... review`
- `Sol review`
- `Human review`
- `independent Sol`

unless exact externally supplied authority is being quoted/bound, not newly authored.

This applies to:

- language QA;
- reader-surface semantic review;
- semantic/editorial review;
- visual review;
- session report.

Independent Sol review will be performed only after r2 is pushed.

## 12. Dedicated language QA before reader rendering

Create an edition-local Worker language-QA artifact before TeX/PDF generation.

It must document:

- reviewer actual identity;
- all 7 Draft Results + synthesis read as continuous prose;
- representative r1 -> r2 repair examples;
- review for technical calques beyond literal token scan;
- result PASS/FAIL.

PASS criterion:

A technically literate Japanese reader can understand the mechanism, product, benchmark limitation, license, temporal condition, or security finding without reconstructing the English source wording.

Do not mark PASS merely because a forbidden-word list is clean.

## 13. Rebuild downstream publication authority

After Draft r2 is established:

1. canonical Draft validation;
2. regenerate reader-facing TeX/Bib;
3. lexical Publication Boundary check;
4. semantic Japanese-language/reader-surface check;
5. CI PDF build;
6. pin exact PDF;
7. reader manuscript;
8. deterministic checks/bundle;
9. reader-surface semantic review with Worker provenance;
10. semantic/editorial review with Worker provenance;
11. visual review with Worker provenance;
12. stage validation;
13. new Publication Candidate;
14. advance to `RELEASE_CANDIDATE`;
15. create fresh Publication Preview r2 shell/dossier;
16. STOP.

Do not reuse r1 PDF/candidate/review identities.

## 14. X/public citation — preserve successful r1 design

Preserve public auditability.

r1 had:

- 19 cited bibliography entries;
- 0 missing;
- 0 unused;
- 8 direct X status URLs;
- no internal GitHub blob URLs;
- no repository-internal reader paths.

r2 counts may change only if editorial citation placement legitimately changes, but:

- every cited key must resolve;
- direct community observations must remain publicly auditable;
- X must remain context/community evidence only;
- technical facts must remain primary-source grounded.

## 15. Reader Publication Boundary

Do not expose internal pipeline semantics in reader prose:

- HOLD
- PARTIAL
- VERIFIED
- MATERIAL
- Screening
- Selection
- candidate status
- blocker
- internal revision IDs
- internal repository paths.

Do not confuse source limitations with production-state language.

## 16. Shared-Core freeze — absolute

No changes under:

- `.github/**`
- `config/**`
- `schemas/**`
- `scripts/**`
- `templates/**`
- `tests/**`.

Do not change:

- `main`;
- `production/survey-core-v2`.

Do not use `revalidate-publication-surface` as a workaround: current Core restricts that mechanism to `REVIEWED_CORE_CHANGE`, which is not the reason for this edition-local repair.

Do not change Core reason classes or validators.

The canonical Human `REQUEST_CHANGES` revision path is the supported mechanism for this run.

## 17. Commit/push discipline

Existing W37 branch only.

Normal commits and non-force pushes.

Remote read-back after each meaningful write group.

No reset/rebase/squash/history rewrite.

## 18. Normal endpoint

Successful endpoint:

- Architecture Human Review remains APPROVED;
- Human Publication Preview r1 = REQUEST_CHANGES, historically preserved;
- Draft r2 regenerated from approved Architecture;
- natural technical Japanese QA PASS;
- new exact PDF/candidate established;
- lifecycle `RELEASE_CANDIDATE`;
- next action `PUBLICATION_PREVIEW`;
- terminal `HUMAN_GATE_REACHED`;
- fresh Publication Preview r2 = PENDING;
- no Human r2 decision;
- Freeze not started;
- Release not started;
- main unchanged;
- Production Line unchanged;
- shared-Core changed paths = 0.

STOP there.

## 19. Final report

Report:

- Starting SHA/tree;
- preflight proof that `ARCHITECTURE_ESTABLISHED` does not reopen Architecture;
- Human Publication Preview r1 REQUEST_CHANGES record path/revision/hash;
- reviewed production commit;
- regeneration boundary;
- preserved Architecture approval path/hash;
- state immediately after revision;
- frozen upstream counts;
- Draft r2 identity;
- language-QA identity/result;
- representative r1 -> r2 wording repairs;
- TeX/Bib identity;
- citation/X audit;
- new PDF path/SHA/bytes/pages;
- semantic/editorial reviewer actual identity/result;
- visual reviewer actual identity/result;
- new candidate SHA;
- fresh Publication Preview r2 reviewed production commit/tree;
- ending HEAD/tree;
- main unchanged;
- Production Line unchanged;
- shared-Core changed paths = 0;
- Human r2 decision = PENDING;
- exact stop reason.
