# W37 Publication Preview r3 — independent Sol review

Status: `SOL_INDEPENDENT_REVIEW / PASS_WITH_PROVENANCE_CORRECTION / READY_FOR_HUMAN_PUBLICATION_PREVIEW`

Date: `2026-09-19 JST`

Issue: `2026-W37`

Reviewed production authority:

- production commit: `8dfb83499f839907d180d9a06bd155cc12fb27d6`
- presentation branch HEAD before Sol audit additions: `d2a4958d4c8f6fa55f3cfa5b6cf94f03c70a0ca7`
- presentation tree: `f2d1bdb138bc9ec530fa6b16fb25fa8c8e836498`

Exact PDF:

- path: `surveys/weekly/2026-W37/main.pdf`
- SHA-256: `9e957ca2d48dd95091e0013c0f2d23f1570ad9fac89b131365259f1c8e948e56`
- bytes: `309033`
- pages: `11`
- CI artifact: `10559799086`

Human Publication Preview r3 decision remains:

`PENDING`

This is an independent Sol review, not a Human decision.

## 1. Canonical Human review history — PASS

Confirmed Human Gate history:

1. Architecture Review r1:
   - `APPROVED`
   - reviewed production commit `55e700a34765654cd2ced0c2a454d4fb3433dd4f`
2. Publication Preview r1:
   - `REQUEST_CHANGES`
   - reviewed production commit `8057a468897f67d3a11bd9287f6f56f0485877ce`
3. Publication Preview r2:
   - `REQUEST_CHANGES`
   - revision `2`
   - reviewed production commit `74400d716e703c12efee97707ff0ee97d47f98a8`
   - regeneration boundary `ARCHITECTURE_ESTABLISHED`.

Current state:

- lifecycle `RELEASE_CANDIDATE`
- next action `PUBLICATION_PREVIEW`
- terminal `HUMAN_GATE_REACHED`
- Architecture Review remains `approved`
- Publication Preview r3 remains `pending`
- Freeze / Release remain pending.

No Human r3 decision exists.

## 2. Issue #434 semantic Publication Boundary — PASS

The r2 blocking process narration is removed.

Independent scan of all reader-facing W37 r3 sections confirms zero occurrences of process-leak forms including:

- `取得の打ち切り`
- `参照の打ち切り`
- `取り切れなかった`
- `途中で取得`
- tool/time/budget constraint narration
- retrieval-stop narration.

The DeepSeek section now states reader-relevant verification scope, for example:

- `本号ではベンチマーク表・図の詳細な検証までは行っておらず、評価手法はベンダー側の説明の範囲で扱う。`
- `トークン単価表の詳細は本号の検証範囲外である`.

Sources & Limitations now states:

- `本号では全文PDFやIOC、ベンチマーク手法・図表の詳細までは扱わず、その範囲を超える主張は行わない。`

These preserve the true non-consumption/verification boundary without narrating internal production mechanics.

Issue #434 remains open only for generic Core hardening because the r2 semantic gate previously produced a false negative. W37 r3 artifact-level repair passes.

## 3. Issue #501 natural technical Japanese — PASS / NO REGRESSION

Independent reread confirms the r2 natural-Japanese repairs remain intact.

No technical-use regression to:

- 模型
- 符号
- 道具立て
- 代理人
- 砂場
- 給仕
- 引擎
- 許し
- 札
- 訳し
- 混合専門家
- 検出子.

Established AI/software terms remain natural and precise:

- モデル
- コード / コーディング
- トークン
- エージェント
- エージェントハーネス
- サンドボックス
- サービング / 推論基盤
- エンジン
- ライセンス
- モデルカード
- 翻訳
- MoE / Mixture-of-Experts
- 評価用モデル
- IOC / 侵害指標.

Reader-facing Japanese is suitable for a technically literate Japanese audience.

## 4. Issue #506 reviewer provenance — PASS / NO REGRESSION

All new Worker review artifacts use the actual runner identity:

`Worker/Agent (Muse Spark)`

Confirmed for:

- Draft r3 boundary QA;
- reader-surface semantic review;
- semantic/editorial review;
- visual review.

No new worker artifact self-identifies as ChatGPT, Sol, Human, or an independent reviewer.

The r3 dossier correctly states it is not an independent Sol review and not a Human decision.

## 5. Human / Worker timestamp records — PASS

New r3 Human/Worker review timestamps are no longer future-dated.

Human Publication Preview r2:

- reviewed_at: `2026-09-18T17:37:47Z`
- containing commit: `a28800cb0328abfdf5033f2a80144b80359be3e9`
- commit time: `2026-09-18T17:43:03Z`
- result: valid ordering.

Worker Draft r3 boundary QA:

- reviewed_at: `2026-09-19T02:39:00+09:00`
- UTC equivalent: `2026-09-18T17:39:00Z`
- containing commit: `a28800cb0328abfdf5033f2a80144b80359be3e9`
- commit time: `2026-09-18T17:43:03Z`
- result: valid ordering.

Worker reader/semantic/editorial/visual reviews:

- recorded/reviewed_at: `2026-09-18T17:47:29Z`
- containing production commit: `8dfb83499f839907d180d9a06bd155cc12fb27d6`
- commit time: `2026-09-18T17:48:03Z`
- result: valid ordering.

## 6. Issue #507 inherited Production State chronology — NONBLOCKING PROVENANCE EXCEPTION

The regenerated Production State still contains machine-transition `recorded_at` values:

- Draft complete: `2026-09-19T00:30:00Z`
- Validated draft: `2026-09-19T00:31:00Z`
- Release candidate: `2026-09-19T00:32:00Z`.

Those values are not valid wall-clock times: the commits containing the resulting state already existed at `2026-09-18T17:43–17:48Z`.

The r3 worker disclosed this as inherited Core monotonicity from the earlier future-dated state history.

This defect is explicitly covered by the append-only W37 correction ledger:

`sources/2026-W37/execution/provenance/w37-execution-time-correction-20260919.md`

The ledger has been extended for r3 and states:

- original bytes remain preserved;
- the machine-transition times are invalid as wall-clock event times;
- lifecycle state identities remain authoritative;
- Git commit ordering and valid Human/Worker review times govern chronology;
- no fabricated replacement event seconds are introduced.

Generic Core remediation remains Issue #507.

This is a metadata/provenance defect, not a publication-content defect, and does not invalidate the r3 PDF, Candidate, Human decisions, or approved Architecture.

Release provenance must carry the correction ledger.

## 7. Exact PDF / visual review — PASS

Sol independently downloaded CI artifact `10559799086`.

Verified exact PDF:

- SHA-256: `9e957ca2d48dd95091e0013c0f2d23f1570ad9fac89b131365259f1c8e948e56`
- bytes: `309033`
- pages: `11`
- A4
- unencrypted
- creation/modification metadata: `2026-09-18T17:46:37Z`
- all pages render successfully.

Visual inspection found:

- no clipping;
- no overlap;
- no broken Japanese glyphs;
- no black-square rendering;
- stable cover / contents / body / limitations / bibliography layout.

No blocking visual defect remains.

## 8. Citation / X public auditability — PASS

Independent source scan confirms:

- unique cited keys: `19`
- bibliography records: `19`
- missing keys: `0`
- unused records: `0`
- direct X status URLs: `8`
- internal GitHub blob URLs: `0`
- internal repository paths in reader prose: `0`.

The 8 direct X citations remain the same ordinary-window posts independently verified in the r1/r2 audits.

X remains community/context evidence only.

No technical fact is established by X alone.

## 9. Architecture / evidence boundary fidelity — PASS

r3 preserves the approved Architecture and all required evidence boundaries:

- Financial Services on Astra remains distinct from GPT-Live-1 and Agents API;
- GPT-Live-1 remains a separate voice layer;
- Agents API remains a separate agent harness;
- DeepSeek ahead-of-Pro comparison remains vendor-attributed;
- Sep 14 routing remains future/post-window;
- Fusion publication time remains `2026-09-11T17:00:00Z`;
- Fusion 39% remains a maximum, not uniform;
- SWE-2 metrics remain vendor-side;
- MiniCPM/North/Ling remain vendor/model-card bounded;
- North judge-model and license bounds remain visible;
- Anthropic cases remain vendor investigations;
- full Threat PDF / IOC remain outside edition scope;
- resignation discourse remains non-architected;
- GLM rumor remains excluded.

No fresh research or Architecture revision is required.

## 10. Shared-Core / branch integrity — PASS

r3 production run changed no path under:

- `.github/**`
- `config/**`
- `schemas/**`
- `scripts/**`
- `templates/**`
- `tests/**`.

Remote `main` remains:

- HEAD `6aa385cbe287b9b20fac4ea3a61d8ffd6179ed3b`
- tree `62cf5dfb30cc692cd19c11289fa80c837fd17b66`.

Remote `production/survey-core-v2` remains:

- HEAD `774dd39a951c9ac3818e83dfffd4c7666efb0a20`
- tree `cd46a6f7a6dcc4031e76220cea4c52c7dd1fc481`.

No Freeze or Release occurred.

## 11. Residual nonblocking limitations

Carry into final publication/release provenance:

- vendor/card/partner benchmarks remain externally unreproduced where already noted;
- pricing/entitlement/language/telephone/rate/region gaps remain explicit;
- DeepSeek detailed per-table values remain outside edition verification scope;
- Fusion untested pairs remain ungeneralized;
- North language-detail tables remain outside edition verification scope;
- Ling hour precision remains bounded;
- Threat full PDF/IOC remain outside edition scope;
- image/video lanes were quiet in examined Discovery, not proven absent;
- Issue #507 machine-transition timestamp correction ledger must remain included in release provenance.

These do not require further reader-surface regeneration.

## 12. Sol verdict

`PASS_WITH_PROVENANCE_CORRECTION / READY_FOR_HUMAN_PUBLICATION_PREVIEW`

The W37 r3 Publication Candidate is suitable for Human judgment.

Human Publication Preview r3 remains:

`PENDING`

If the Human approves r3, the next step may proceed to the canonical Freeze / Release path, while preserving the Issue #507 correction ledger in release provenance.
