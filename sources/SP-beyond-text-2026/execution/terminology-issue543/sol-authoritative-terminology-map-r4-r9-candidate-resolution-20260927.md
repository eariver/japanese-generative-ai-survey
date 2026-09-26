# TS-002 Issue #543 — Sol authoritative terminology map r4 (r9 candidate resolution)

Date: 2026-09-27 JST  
Status: `AUTHORITATIVE / SOL_EDITORIAL_DECISION / R9_CONTINUATION / APPLY_WITHOUT_REINTERPRETATION`

## 1. Scope and authority

This file resolves the 23 `CANDIDATE_FOR_SOL_REVIEW` entries returned by Muse during Publication Preview r9 pre-validation closure scan.

Human r9 `REQUEST_CHANGES` remains the active Human authority. The edition is already at `DRAFT_COMPLETE`, therefore **no new Human publication revision is required or authorized** for this continuation.

This file supplements:

- `sol-authoritative-terminology-map-r2-20260926.md`
- `sol-authoritative-terminology-map-r3-final-residual-20260927.md`

r2/r3 decisions remain frozen unless this file explicitly addresses a residual grammatical variant. Muse MUST NOT reinterpret these decisions or invent additional wording.

Frozen Core v2 remains immutable. No Core implementation, script, schema, contract, stage plan, transition rule, compatibility logic, template, or shared configuration may be modified.

## 2. Sol source readback used for the non-trivial candidates

Sol confirmed the following primary/source identities before issuing this map:

- F5-TTS (`btd132`): the text representation is refined with **ConvNeXt** before the DiT; the paper describes refining the text representation rather than a generic `文章精緻化層`.
- Moshi (`btd134`): **time-aligned text tokens are predicted as a prefix to audio tokens** in the **Inner Monologue** method.
- AnimateDiff (`btd074`): the three evaluation aspects are **text alignment / domain similarity / motion smoothness**.
- Wan2.2 (`btd124`): prompt extension is explicitly implemented as **prompt extension**, with DashScope-hosted or local-Qwen execution paths.
- AnyGPT (`btd096`): the paper describes a **multimodal text-centric dataset for multimodal alignment pre-training** and a 108k any-to-any multimodal instruction set; the model remains text-centric rather than using a literal `文章橋渡し` term.
- CoDi (`btd097`): the paper describes **bridging alignment** in a shared multimodal space and any-to-any / joint modality generation.
- MusicLM (`btd065`): MuLan is a **joint music-text embedding** model; training conditions on the music-side MuLan representation and inference substitutes the text-side MuLan representation.

No new technical authority is created here. This is editorial adjudication over already accepted authority.

## 3. Candidate-by-candidate decisions

### SOL-R4-C001 — `文章事前分布` (VITS / btd056)

Decision:

- `文章事前分布` -> `テキスト由来の事前分布`

Preferred sentence form:

> 事後分布とテキスト由来の事前分布、flow、アライメント探索、デュレーション予測、ボコーダによる復号をEnd-to-Endで統合する。

Do not use `文章事前分布`.

### SOL-R4-C002 — `文章精緻化層` (F5-TTS / btd132)

Decision:

- `四層の文章精緻化層` -> `4層のConvNeXtによるテキスト表現精緻化`

Preserve the existing 4-layer count and the DiT architecture claim. Do not invent a separate named `text refinement layer` component.

### SOL-R4-C003 — `文章接頭辞` / Moshi Inner Monologue (btd134)

Decision:

Replace the malformed `時刻アライメントした文章接頭辞の内言` wording with the source-faithful mechanism:

> 時刻アライメントしたテキストトークンを音響トークンのprefixとして先行予測するInner Monologue

Equivalent Japanese grammar is allowed, but the identities `time-aligned text tokens`, `prefix to audio tokens`, and `Inner Monologue` must remain explicit.

### SOL-R4-C004 — `文章と音楽の整合`

Decision:

- `文章と音楽の整合` -> `テキスト・音楽整合`

### SOL-R4-C005 — `結合音楽文章符号` (MusicLM / btd065)

Decision:

- `結合音楽文章符号` -> `MuLanのテキスト・音楽共同埋め込み`

Where the surrounding sentence contrasts training and inference conditioning, use:

- training: `音楽側のMuLan埋め込み`
- inference: `テキスト側のMuLan埋め込み`

Do not use the literalized `結合音楽文章符号`.

### SOL-R4-C006 — `文章側` (MusicLM / btd065)

Decision:

- `文章側` -> `テキスト側`

When specifically referring to MusicLM MuLan conditioning, prefer `テキスト側のMuLan埋め込み`.

### SOL-R4-C007 — `文章クロスアテンション` (MusicGen / btd066)

Decision:

- `文章クロスアテンション` -> `テキストクロスアテンション`

### SOL-R4-C008 — `文章のみ` (MusicGen text-only condition)

Decision:

- `文章のみ` -> `テキストのみ`

### SOL-R4-C009 — `文章と音響の整合間隙` (AudioLDM / btd067)

Decision:

- `文章と音響の整合間隙` -> `テキスト・音響整合のギャップ`

Use the same terminology in the corresponding boundary-summary occurrence.

### SOL-R4-C010 — `文章と拍と和音` (MuSTANGO / btd069)

Decision:

- `文章と拍と和音の順次クロスアテンション` -> `テキスト・拍・和音への順次クロスアテンション`

Do not alter the already-fixed PCM metric identities or numerical values.

### SOL-R4-C011 — `文章や領域やmotion smoothness` (AnimateDiff / btd074)

Canonical evaluation axes:

- **text alignment**
- **domain similarity**
- **motion smoothness**

Decision:

Replace the three-axis wording with:

> text alignment（テキスト整合）、domain similarity（ドメイン類似度）、motion smoothness（モーション滑らかさ）の三軸

Where the numeric `2.825` / `1.615` comparison is specifically the user-ranking motion-smoothness axis, retain that binding.

### SOL-R4-C012 — `文章拡張` (Wan2.2 / btd124)

Canonical: **prompt extension**.

Decision:

- `文章拡張` -> `prompt extension（プロンプト拡張）`

Where the hosted/local execution distinction is stated, use:

> DashScopeを用いるhosted prompt extensionと、local Qwenを用いるローカルprompt extension

Do not generalize this to unrelated text expansion mechanisms.

### SOL-R4-C013 — `動画文章 / 画像文章` (Imagen Video training data / btd071)

Decision:

- `14M動画文章` -> `14Mの動画・テキストペア`
- `60M画像文章` -> `60Mの画像・テキストペア`

Preserve all numeric values exactly.

### SOL-R4-C014 — `文章と画像の条件付け` (adversarial distillation / btd081)

Decision:

- `文章と画像の条件付け` -> `テキスト・画像条件付け`

### SOL-R4-C015 — `文章映像` (VBench / btd092)

Decision:

- `文章映像` -> `テキスト・動画`

Do not use `文章映像` as a modality-pair term.

### SOL-R4-C016 — `文章はSentencePiece指示` (Unified-IO / btd094)

Decision:

Rewrite only the modality/token representation phrase as:

> テキストはSentencePieceトークン、密な予測マップと画像はVQ-GANコード、ボックスと点は離散化した位置トークンとして表す

Important:

- preserve the existing claim boundary and numerical counts;
- `濃密地図` should not remain in this specific dense-prediction context; use `密な予測マップ`;
- do not broaden into a new architectural claim.

### SOL-R4-C017 — `話し言葉と文章の往復` (AudioPaLM / btd095)

Decision:

Use `音声とテキストの双方向変換` as the reader-facing umbrella wording.

Therefore:

- heading `話し言葉と文章の往復を一つの復号器に畳む` -> `音声とテキストの双方向変換を一つの復号器に統合する`
- table/category `発話音声と文章の往復` -> `音声・テキスト双方向変換`

Do not imply arbitrary image/video modality support.

### SOL-R4-C018 — `画像文章` (Unified-IO generation task / btd094)

Decision:

- `画像文章の生成課題` -> `画像・テキスト生成課題`

If the actual sentence distinguishes image generation from text generation separately, grammar may be adjusted to `画像およびテキストの生成課題`; do not use `画像文章` as a compound.

### SOL-R4-C019 — `文章橋渡し` (AnyGPT / CoDi contexts)

This malformed phrase covers two different source concepts and MUST be split by source.

For AnyGPT (`btd096`):

- `文章橋渡しアライメント` -> `テキスト中心のマルチモーダルalignment pre-training（アライメント事前学習）`

For CoDi (`btd097`):

- where `文章橋渡し` refers to the shared multimodal-space mechanism, use `bridging alignment（ブリッジング・アライメント）`.

Do not merge AnyGPT and CoDi into one mechanism.

### SOL-R4-C020 — `二兆文章トークン` (AnyGPT / btd096)

Decision:

- `二兆文章トークン` -> `2兆テキストトークン`

Preserve the numeric value.

### SOL-R4-C021 — `文章音声 / 映像音声` (CoDi / btd097)

Decision:

Use modality-pair terminology:

- `文章音声` -> `テキスト・音声`
- `映像音声` -> `動画・音声`
- residual `文章画像` in the same CoDi modality-pair context -> `テキスト・画像`

Where the source is describing joint generation rather than a dataset pair, use grammatical forms such as `テキスト・音声の共同生成` / `動画・音声の共同生成` without changing the underlying claim.

### SOL-R4-C022 — Suno modality list `文章・音声・画像・映像` (btd114)

Decision:

In product-input/output modality listing:

- `文章・音声・画像・映像` -> `テキスト・音声・画像・動画`

This is a terminology-only normalization. Do not add capabilities not already supported by the cited release notes.

### SOL-R4-C023 — `対照の文章・音響間隙` (AudioLDM / btd067)

Decision:

- `対照の文章・音響間隙` -> `対照学習におけるテキスト・音響整合のギャップ`

Keep the existing boundary that abstract text descriptions can degrade conditioning. Do not change numeric claims.

## 4. Cross-cutting r9 closure rule

For the 23 returned entries above, the canonical generic rule is now explicit:

- ML modality `文章` -> `テキスト` when it denotes text as a model modality, condition, token stream, embedding, prompt, or modality pair;
- ordinary prose/document meaning of `文章` remains Japanese `文章` and is not globally replaced.

Muse may apply this rule only to the exact 23 returned contexts and identical same-source grammatical variants. It MUST NOT perform a new global replace over all Japanese prose.

## 5. Citation and invariant rule

No new citation change is authorized by this r4 map.

The only citation exceptions for the entire Issue #543 repair remain:

1. `SOL-CIT-001` — DAC Balanced data sampling -> `btd008`, with EnCodec boundary at `btd007`.
2. `SOL-CIT-002` — Wan2.2 open-weight lineage boundary -> `btd124`.

Any additional citation addition/removal/rebinding requires stop-and-report.

Preserve:

- section/subsection order;
- labels;
- technical conclusions;
- Issue #529 semantic depth;
- Evidence status and PARTIAL/NEEDS_MORE boundaries;
- vendor attribution and closed-system boundaries;
- numerical meaning and units;
- 139/139 citation coverage;
- `references.bib`.

## 6. Continuation boundary under Human r9

Because Muse correctly stopped at `DRAFT_COMPLETE` before validation, this r4 resolution is a continuation of the **same Human r9 REQUEST_CHANGES**.

No Human r10 decision is needed or authorized.

Next worker sequence:

1. read remote guards;
2. read r2 + r3 + this r4 map;
3. apply only r4 decisions to the returned 23 candidates and exact same-source variants;
4. synchronize Issue #543 ledger JSON/MD;
5. rerun the pre-validation broad closure scan;
6. if any new unmapped candidate remains, leave it unchanged and stop again at `DRAFT_COMPLETE`;
7. only if unresolved count is zero, advance through the existing Frozen Core path to validation and regenerate the Publication Candidate;
8. stop at `PUBLICATION_PREVIEW / AWAITING_HUMAN_PUBLICATION_PREVIEW_DECISION`.

No Freeze, Release, merge, Core v2 modification, new branch, force push, reset, rebase, history rewrite, or autonomous editorial decision is authorized.
