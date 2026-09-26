# Sol terminology readback — Issue #533 r1

Status: `REQUEST_CHANGES / ONE_RESIDUAL_SOURCE_BOUND_TERM`

Date: 2026-09-26 JST

## Scope

Read-back of the Muse terminology-only repair for TS-002 `SP-beyond-text-2026` after Issue #533.

The repair is accepted in substance except for one explicitly escalated reader-facing term: `ゼロショット素体` (2 occurrences, BT-D096 / AnyGPT).

## What passed

- Human Publication Preview r3 `REQUEST_CHANGES` was canonically recorded and Architecture approval preserved.
- Terminology repair remained publication-local; no Discovery / Screening / Evidence / Materiality / Completeness / Selection / Architecture rerun.
- `references.bib` remained byte-identical and no new authority was added.
- Semantic invariants reported by the worker are consistent: `\autocite` blocks 1259 -> 1259, citation-key multiset identical, number/unit tokens 1041 -> 1041, section order/labels/kickers unchanged, 139/139 citation coverage preserved, Evidence statuses and PARTIAL/NEEDS_MORE/vendor/closed-system boundaries unchanged.
- High-confidence mistranslations were removed from reader-facing manuscript: `零射影`, vocoder-context `声器`, `符号言語`, Consistency-family `無撞着`, `抽出推論`, `類別条件`, `類別脱落`, named-architecture `変換器`, `流れ整合`, `整流流れ`, `模擬なし`, `任意間`, `多能模型`, `話声`, and generative-model `標本化` all reached zero in the worker scan.
- Spot read-back confirms canonical/searchable terminology such as `Consistency Model（整合性モデル）`, `Flow Matching（フローマッチング）`, `Rectified Flow（整流フロー）`, `Diffusion Transformer (DiT)`, `Scalable Interpolant Transformer (SiT)`, `ボコーダ`, and `コーデック言語モデル`.
- Rebuilt candidate is reported as 75 pages, PDF SHA-256 `e05a88bc1574e97868a859989d033f0ca41c23f7e7a986193f0ce2e57e6bed03`, with CI PASS and no blocking/layout findings.

## Residual finding

The worker correctly escalated rather than guessed on:

`ゼロショット素体` ×2

in the AnyGPT / BT-D096 paragraph.

This wording remains reader-facing and is not acceptable as final terminology. `素体` is unnatural here and obscures the experimental subject.

### Source-bound resolution

AnyGPT's official repository explicitly distinguishes a **base model** and a **chat model**. It states that the base model aligns the four modalities and supports intermodal conversions; the base-model inference section also explicitly lists `Zero-shot Text-to-Speech (TTS)` among its tasks.

Therefore the ambiguous evidence-card shorthand `zero-shot base` should be rendered reader-facing as the **base model under zero-shot evaluation/setting**, not as `素体`.

Approved wording direction:

- first occurrence: `報告条件のベースモデルのゼロショット評価では...`
- second occurrence: `ベースモデルのゼロショット設定も値と一体であり...`
- later same-paragraph reference currently phrased `素体のゼロショット値` should be normalized consistently to `ベースモデルのゼロショット結果` if present in the exact candidate.

Equivalent natural Japanese is acceptable only if it preserves the same subject: **AnyGPT base model evaluated in a zero-shot setting**.

Do not change numerical values, comparison targets, citations, or the boundary that these results are condition-bound and must not be extrapolated to the instruction-tuned/chat model.

## Disposition

`REQUEST_CHANGES / ONE_RESIDUAL_SOURCE_BOUND_TERM`

No re-research or broad terminology pass is required. Perform a bounded BT-D096 reader-facing correction, update the terminology ledger from `ESCALATE` to `REPLACE`, rerun semantic/citation invariants and exact PDF build/visual regression, and return to Publication Preview pending.

Freeze / Release remain unauthorized.
