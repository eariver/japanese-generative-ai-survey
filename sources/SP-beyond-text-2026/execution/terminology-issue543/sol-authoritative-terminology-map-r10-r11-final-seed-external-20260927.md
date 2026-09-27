# TS-002 Issue #543 — Sol authoritative terminology map r10 (r11 final seed-external audit)

Date: 2026-09-27 JST  
Status: `AUTHORITATIVE / SOL_INDEPENDENT_FINAL_AUDIT / HUMAN_R11_REVIEW_RESULT / APPLY_WITHOUT_REINTERPRETATION`

## 1. Scope and disposition

This map records seed-external residuals found by Sol after Muse correctly executed Human Publication Preview r11 and regenerated the Release Candidate at:

- reviewed branch commit: `f81694363a6d6fc3456c96d77e02ee8360728ef1`
- reviewed tree: `0041c7d06a6b19543c92c3340f6aae5db225f4a4`
- source SHA-256: `d3543075351e14aaf95c2ada8099ec8dd122fb01e879be236a5b6fa162672782`
- candidate SHA-256: `79c3a4fd9a2e9b948920dcd85004f8c22108dfbd2ca7ee268e91a2186140ec9b`
- PDF SHA-256: `4e2250677716fba5cbfe3ea0e57d9f2174e83a93a15a361d8fbae164bf45089d`
- PDF pages: `78`

The r11 worker execution itself is mechanically accepted: Human r11 was recorded, Sol r9 was applied, the frozen Core v2 returned the edition to `RELEASE_CANDIDATE / PUBLICATION_PREVIEW pending`, and the r9 exact residual list is zero.

Issue #543 is nevertheless **not eligible for closure**. Sol's required seed-independent source readback found additional reader-facing canonical-terminology/copy-edit residuals, plus one source-binding defect in the LCM/LCM-LoRA boundary.

Disposition:

`REQUEST_CHANGES / FINAL_SEED_EXTERNAL_RESIDUALS_FOUND / HUMAN_R12_REQUIRED`

This file does not synthesize Human r12. A new explicit Human Publication Preview `REQUEST_CHANGES` decision is required because the edition is already at `RELEASE_CANDIDATE`.

Frozen Core v2 remains immutable.

## 2. Source / Evidence readback used by Sol

### btd032 — Classifier-Free Diffusion Guidance

Consumed Evidence records classifier-free guidance as conditional/unconditional joint training followed by inference-only guidance with a swept guidance weight `w`; reported FID/IS trade-offs are explicitly tied to the sweep. This confirms that reader-facing variants such as `尺度の掃引`, `尺度感度`, and technical `誘導尺度` in this family denote **guidance scale / guidance-scale sweep**, not a generic scale.

### btd025 — Diffusion Transformer

Consumed Evidence records two distinct limitations: throughput figures are hardware-bound, and FID is sensitive to the evaluation suite. Reader-facing `装置依存 ... 評価手順への鋭敏さ` obscures both identities.

### btd079 — Latent Consistency Models

Consumed Evidence explicitly records the boundary `1-step gap remains; solver/skipping/guidance sensitive; custom sets need finetuning without universal module.` Therefore the current one-step/solver/skipping/guidance sensitivity statement belongs to `btd079`.

### btd080 — LCM-LoRA

Consumed Evidence instead records: report-only/no new benchmark, heuristic combination weights, and per-model generality requiring validation. It does **not** support the solver/skipping/guidance-sensitivity boundary by itself.

### btd124 — Wan2.2

Consumed Evidence explicitly records A14B hardware requirements as `80 GB single-GPU / 8-GPU multi-GPU`. Thus the current `単一80GBや複数装置` wording can retain the actual GPU identity.

## 3. Authoritative decisions

### SOL-R10-C001 — CFG grammatical residual `尺度の掃引`

Decision: `REPLACE`

Exact current sentence fragment:

`ドロップアウト率と尺度の掃引と二回計算の費用`

Final:

`ドロップアウト率とガイダンススケールのスイープと二回計算の費用`

This is the same btd032 concept already normalized by Sol r7/r8. Do not alter unrelated ordinary `尺度`.

### SOL-R10-C002 — CFG `尺度感度`

Decision: `REPLACE`, both btd032/btd033-bound occurrences.

`条件別のドロップアウト率と尺度感度の対応`
->
`条件別のドロップアウト率とガイダンススケールへの感度の対応`

`ドロップアウト率と尺度感度の対応`
->
`ドロップアウト率とガイダンススケールへの感度の対応`

Do not replace generic non-guidance sensitivity terminology.

### SOL-R10-C003 — technical `誘導尺度` family

Decision: `REPLACE`, only where the term denotes classifier-free/image guidance scale.

Canonical reader-facing term:

`ガイダンススケール`

Apply to the currently remaining source-bound forms, including:

- `潜在拡散の誘導尺度` -> `潜在拡散のガイダンススケール`
- `誘導尺度一・五から十` -> `ガイダンススケール一・五から十`
- subsection heading `符号器規模と誘導尺度` -> `符号器規模とガイダンススケール`
- IP-Adapter `五十段階級の暗黙的軌道と誘導尺度` -> `...ガイダンススケール`
- MusicGen `誘導尺度$3.0$` -> `ガイダンススケール$3.0$`
- Pick-a-Pic `誘導尺度を振り` -> `ガイダンススケールを振り`

Do not rewrite ordinary `尺度`, metric scale, model scale, inference-time adapter scale, or other unrelated scale concepts.

### SOL-R10-C004 — `焼き直し` technical-copy residual

Decision: `NONSEMANTIC_COPY_EDIT`, three technical-prose occurrences.

- `画像域での焼き直し` -> `画像領域での再検証`
- `誤差帰属は焼き直し検証を要する` -> `誤差帰属は再検証を要する`
- `超解像のテキスト条件の有用性の焼き直し` -> `超解像におけるテキスト条件の有用性の再検証`

No claim or citation change is implied by this copy edit.

### SOL-R10-C005 — broken `報告掃引` phrase

Decision: `NONSEMANTIC_COPY_EDIT`

Current:

`超解像のテキスト条件の有用性の焼き直しは報告掃引の範囲を超えて確立していない。`

Final:

`超解像におけるテキスト条件の有用性の再検証は、報告された範囲を超えて確立していない。`

Do not reinterpret this as an additional quantitative guidance-sweep claim; this edit only restores natural reader-facing wording and preserves the existing claim boundary.

### SOL-R10-C006 — DiT hardware/evaluation sensitivity wording

Decision: `REPLACE`, two btd025-bound reader-facing formulations.

Current:

`装置依存の処理量数値や評価手順への鋭敏さ、画素空間での未検証は境界として残る`

Final:

`ハードウェア依存の処理量数値、評価手順によるFIDの変動、画素空間での未検証は境界として残る`

Current:

`Transformer denoiserの処理量数値は装置に結びつき、評価手順に鋭敏であり、画素空間は未検証である`

Final:

`Transformer denoiserの処理量数値はハードウェアに依存し、FIDは評価手順の影響を受け、画素空間は未検証である`

This preserves the two source-bound limitations separately instead of compressing them into the literalized `鋭敏` wording.

### SOL-R10-C007 — LCM sensitivity wording + source binding

Decision: `REPLACE / CITATION_REBIND`

The current LCM/LCM-LoRA paragraph binds the sentence

`一段階の隔たりと誘導や刻みへの鋭敏さは、四段階実用と一段階研究の線引きを示す。`

to `btd080`, but consumed Evidence assigns solver/skipping/guidance sensitivity to LCM (`btd079`). LCM-LoRA (`btd080`) instead supports heuristic combination weights and per-model generality limitations.

Replace/split as:

`一段階の隔たりとソルバー・ステップ間引き・ガイダンス設定への感度は、四段階実用と一段階研究の線引きを示す\autocite{btd079}。結合重みの発見的手順やモデルごとの再調整の要否は未検証であり、加速と様式の無学習結合を一般則と呼ばない\autocite{btd080}。`

In the later uncited claim-boundary summary:

`一段階の隔たりと解法・間引き・誘導への鋭敏さは残り`
->
`一段階の隔たりとソルバー・ステップ間引き・ガイダンス設定への感度は残り`

New bounded citation authority:

`SOL-CIT-005`: LCM one-step-gap / solver-skipping-guidance-sensitivity boundary -> `btd079`; LCM-LoRA heuristic combination-weight / per-model-generality boundary remains `btd080`.

No other new citation modification is authorized by this map.

### SOL-R10-C008 — generic compute-hardware literalizations

Decision: `CONTEXT-BOUND COPY NORMALIZATION`

Where reader-facing `装置` unambiguously means compute hardware/GPU in the following already-bound contexts, use the established terminology rather than generic `装置`:

- `束ねる量や文脈長や装置の別` -> `束ねる量や文脈長やハードウェアの違い`
- `同一装置・短片条件` -> `同一ハードウェア・短片条件`
- `装置や段階数の拘束` -> `ハードウェアや段階数の拘束` (speech/runtime contexts)
- `民生装置での学習不能条件` -> `民生GPUでの学習不能条件` (btd067; the immediately bound technical statement already identifies a single consumer GPU)
- `大容量配置は単一$80$GBや複数装置を要する` -> `大容量配置は単一$80$GB GPUまたは8 GPU構成を要する` (btd124 Evidence explicitly records `80 GB single-GPU / 8-GPU multi-GPU`)
- conclusion/summary uses such as `遅延・VRAM・装置・量子化` and `版・装置・予算・母集団` -> `遅延・VRAM・ハードウェア・量子化` / `版・ハードウェア・予算・母集団`

Do not blind-replace `装置` outside compute-hardware senses.

## 4. Citation authority

The complete authorized citation-correction set after this map is:

- `SOL-CIT-001`: DAC Balanced data sampling -> `btd008`
- `SOL-CIT-002`: Wan2.2 verified open-weight lineage boundary -> `btd124`
- `SOL-CIT-003`: SPADE/GauGAN Section 4 claims -> `btd041`
- `SOL-CIT-004`: T2I-Adapter Section 4 claims -> `btd037`
- `SOL-CIT-005`: LCM one-step-gap / solver-skipping-guidance-sensitivity boundary -> `btd079`; LCM-LoRA heuristic combination-weight / per-model-generality boundary remains `btd080`

No other citation addition, deletion, substitution, regrouping, or rebinding is authorized.

`references.bib` remains frozen.

## 5. Regression requirements

After application, the worker must confirm at minimum that the following reader-facing residual families are zero except for explicitly unrelated/retained senses:

- `尺度の掃引`
- technical CFG `尺度感度`
- technical guidance-scale `誘導尺度`
- `報告掃引`
- technical-prose `焼き直し`
- hardware/evaluation `鋭敏さ` / `鋭敏`
- LCM `誘導や刻みへの鋭敏さ`
- generic compute-hardware `装置` contexts listed above

Then rerun the complete r2-r10 regression scan **and another seed-independent broad suspicious-translation scan**. Do not stop on this list alone.

If any new unmapped reader-facing candidate appears, do not self-resolve it; return it to Sol.

## 6. Frozen Core v2 — immutable

Frozen Core v2 remains absolutely immutable.

- Core implementation SHA: `95c03bf5285cb4b2c1103a14c460574183a8cb93`
- pipeline contract SHA-256: `ee89796245c22072cec98f34931180214a4928c24f399280793cd6420a4c8e71`
- quality contract SHA-256: `b5b955d524fb438c0f1b2c9490bea1da2083e79028d67a55ca424bbfc20f2958`
- research profile SHA-256: `0f575e6d97caec72b2bf8b7f6b78a562d97ca67b2071193417b968ba3d73e6e8`
- publication profile SHA-256: `a6859559dd1b9d42ab8fb4402b74b7bdd8611dbe65c8e02a7b022b545c20f4eb`

No shared Core script/schema/contract/config/template/stage-plan/transition/compatibility/workflow/validator change is authorized.

If the frozen Core cannot execute a future authorized Publication Preview revision, stop and return to Sol/Human rather than modifying Core.

## 7. Lifecycle rule

Current reviewed state is `RELEASE_CANDIDATE / PUBLICATION_PREVIEW pending` under Human r11.

Therefore this map is **not executable yet**. Sol does not synthesize Human decisions.

A new explicit Human Publication Preview r12 `REQUEST_CHANGES` with regeneration boundary `DRAFT_COMPLETE` is required before a worker may apply this map.

Until then:

- Issue #543 remains OPEN
- no r12 is synthesized
- no Publication approval
- no Freeze
- no Release
- no merge
