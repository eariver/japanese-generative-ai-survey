# TS-002 Issue #543 — Sol authoritative terminology map r5 (r9-next candidate resolution)

Date: 2026-09-27 JST  
Status: `AUTHORITATIVE / SOL_EDITORIAL_DECISION / R9_CONTINUATION / APPLY_WITHOUT_REINTERPRETATION`

## 1. Scope and authority

This file resolves the six `CANDIDATE_FOR_SOL_REVIEW` entries returned by Muse after applying the Sol r4 map during the same Human Publication Preview r9 `REQUEST_CHANGES` execution.

Human r9 authority remains active because the edition is still at `DRAFT_COMPLETE`; no new Human revision is required or authorized.

This file supplements the r2, r3, and r4 Sol terminology maps. All earlier decisions remain frozen unless this file explicitly addresses a residual grammatical variant.

Frozen Core v2 remains immutable. Muse MUST NOT alter Core implementation, scripts, schemas, contracts, stage plan, transition rules, compatibility logic, templates, or shared configuration.

## 2. Source readback used by Sol

Sol resolved the six candidates against the already-consumed authorities and, where needed, the corresponding primary/public source identity:

- LibriSpeech / OpenSLR: the corpus is approximately 1000 hours of 16 kHz read English speech derived from LibriVox and carefully segmented/aligned; related text resources and evaluation language-model resources are separate resource artifacts.
- AudioPaLM: the model unifies speech and text processing/generation; the relevant scope boundary is speech-and-text, not arbitrary image/video/music support.
- CoDi: text is one modality-specific branch in a composable multimodal generation system; OPTIMUS and GPT-2 belong to the text-side modeling path.
- SynthID: the product terminology is text watermarking / SynthID for text, not a literal `文章透かし` compound.
- Ray3: the product surface uses text/image input plus keyframe/video control terminology; reader-facing wording should use `テキスト` and `画像` rather than `文章`.

No new technical authority is created here; this is editorial adjudication over accepted authority.

## 3. Candidate decisions

### SOL-R5-N001 — `文章と音楽の対応` (btd063/btd065)

Decision:

- `文章と音楽の対応` -> `テキスト・音楽整合`

Preferred sentence:

> 距離指標は音響分布の隔たりの代理であり、対照整合指標はテキスト・音楽整合の代理である。

This intentionally aligns with the r4 decision for `文章と音楽の整合`.

### SOL-R5-N002 — LibriSpeech `文章と言語モデル` and adjacent literalization (btd089)

The current phrase must not remain as `文章と言語モデル`.

Required reader-facing wording for the bound sentence:

> LibriSpeechは、LibriVox由来の約1000時間・16 kHzの読み上げ英語音声を慎重にセグメント化・アライメントしたコーパスであり、関連するテキスト資源や評価用言語モデルも提供されている。

Rules:

- `読書英語` -> `読み上げ英語音声` in this LibriSpeech context;
- `文章` -> `テキスト資源` where it denotes corpus text/transcript/book text;
- do not claim that all related language-model resources are physically inside OpenSLR-12;
- do not add a new citation solely for this wording; remain within the existing LibriSpeech authority boundary.

### SOL-R5-N003 — AudioPaLM `発話音声と文章のみ` residuals (btd095)

Decision:

- prose `発話音声と文章のみ` -> `音声とテキストのみ`;
- residual category/row `発話音声と文章の往復` -> `音声・テキスト双方向変換`;
- any remaining same-context `発話音声と文章` -> `音声とテキスト`.

Preserve the existing scope limitation that image, video, and music are not included in the cited AudioPaLM capability boundary.

### SOL-R5-N004 — CoDi `文章はOPTIMUS` (btd097)

Decision:

- `文章はOPTIMUSとGPT-2` -> `テキスト系はOPTIMUSとGPT-2`.

Preferred grammatical form:

> 画像系、動画系、音声系に加え、テキスト系はOPTIMUSとGPT-2を用いる様式別の表現経路を置き、bridging alignment（ブリッジング・アライメント）で共有マルチモーダル空間へ接続する。

Do not invent a new text-diffusion mechanism claim beyond what the consumed CoDi authority supports. If preserving the surrounding existing sentence requires a smaller edit, `文章は` -> `テキスト系は` is sufficient.

### SOL-R5-N005 — SynthID `文章透かし` (btd099)

Decision:

- `文章透かし` -> `テキスト向けSynthID` when discussing the product capability/boundary;
- if a generic mechanism noun is grammatically necessary, use `テキストウォーターマーキング`.

Preferred sentence fragment:

> テキスト向けSynthIDの品質影響については、本稿が消費した製品頁の範囲を超えて独立頑健性まで一般化しない。

Preserve the edition's existing source-boundary statement. Do not introduce a new quantitative robustness claim.

### SOL-R5-N006 — Ray3 `文章・画像起点` (btd122)

Decision:

- `文章・画像起点` -> `テキスト・画像入力`.

Preferred sentence opening:

> Ray3（日付非開示の頁）はテキスト・画像入力と動画間変換（人物参照・開始・終了キーフレームを含む）…

Retain the already-established version/date binding boundary and do not add capabilities beyond the cited product page.

## 4. Closure rule

After applying this r5 map, Muse MUST again run the pre-validation broad suspicious-translation scan over the full reader-facing manuscript.

If any new unmapped candidate is found:

- do not modify it;
- record it in `sources/SP-beyond-text-2026/execution/terminology-issue543/muse-candidates-for-sol-review-r9-next2.md`;
- remain at `DRAFT_COMPLETE` under the same Human r9 authority;
- do not create r10.

If unresolved candidate count is zero, Muse may proceed through the existing Frozen Core path:

`DRAFT_COMPLETE -> VALIDATED_DRAFT -> RELEASE_CANDIDATE`

and stop at `PUBLICATION_PREVIEW / AWAITING_HUMAN_PUBLICATION_PREVIEW_DECISION`.

No Freeze, Release, merge, or new Human approval is authorized.
