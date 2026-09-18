# W37 Publication Preview r1 — independent Sol review

Status: `SOL_INDEPENDENT_REVIEW / REQUEST_CHANGES`

Date: `2026-09-19 JST`

Issue: `2026-W37`

Reviewed Publication authority:

- production commit: `8057a468897f67d3a11bd9287f6f56f0485877ce`
- presentation branch HEAD before this review: `71a4919aa476993d8e68909cbaff29cb6ac4b107`
- presentation tree: `79a291a927920658074575f814b459431f399d8a`

Exact PDF:

- path: `surveys/weekly/2026-W37/main.pdf`
- SHA-256: `08ceb5e9c90b2bf25541bb61e6b14e5b2cdc7fe48635d85c5ab798606b88fd4d`
- bytes: `301238`
- pages: `10`
- CI artifact: `10556277977`

Human Publication Preview decision remains:

`PENDING`

This is an independent Sol review, not a Human decision.

## 1. Gate / machine state — PASS

Confirmed:

- lifecycle: `RELEASE_CANDIDATE`
- next action: `PUBLICATION_PREVIEW`
- terminal: `HUMAN_GATE_REACHED`
- Architecture Human approval recorded canonically:
  - review revision `1`
  - reviewed production commit `55e700a34765654cd2ced0c2a454d4fb3433dd4f`
  - Architecture SHA `81e87a64c2418c71340ee8cc1dec28267a55055d2c02d7dbb06e33623efdfcfb`
- Publication Preview remains pending;
- Freeze / Release pending;
- main unchanged;
- Production Line unchanged;
- shared-Core changed paths from the approved-through-preview run: `0`.

## 2. Exact PDF integrity / layout — PASS

Sol independently downloaded the exact CI artifact and verified:

- SHA-256 matches the repository authority;
- 301238 bytes;
- 10 pages;
- A4;
- unencrypted;
- all 10 pages render successfully;
- no clipping, overlap, broken glyphs, or black-square rendering defect observed.

The layout is dense but readable.

Page 7 has substantial lower whitespace after the Week in Review continuation, but this is not a blocking layout defect.

## 3. Citation and public auditability — PASS

Independent source scan confirms:

- 19 unique citation keys used;
- 19 bibliography records;
- missing citations: `0`;
- unused bibliography records: `0`;
- internal GitHub blob URLs in reader bibliography: `0`;
- repository-internal source paths in reader prose: `0`.

The reader surface contains 8 direct X status URLs.

Independent Snowflake timestamp reconstruction for those 8 X URLs confirms all are inside the W37 ordinary window:

- Astra official: `2026-09-10T18:35:32Z`
- Astra independent: `2026-09-10T23:59:27Z`
- DeepSeek official: `2026-09-10T06:10:09Z`
- DeepSeek independent: `2026-09-10T07:15:51Z`
- Cognition official: `2026-09-11T16:16:23Z`
- coding independent: `2026-09-10T23:59:00Z`
- MiniCPM official: `2026-09-07T14:36:54Z`
- MiniCPM independent: `2026-09-10T21:05:55Z`.

The X citation design successfully avoids the W36 Issue #502 failure mode.

## 4. Architecture / evidence boundary carry-through — PASS

The reader surface preserves the approved Architecture boundaries in substance:

- Financial Services / GPT-Live-1 / Agents API remain distinct products/layers;
- DeepSeek ahead-of-Pro comparison remains vendor-attributed;
- Sep 14 routing remains future-tense;
- Fusion publication time is correctly retained as `2026-09-11T17:00:00Z`;
- Fusion 39% remains a maximum, not a uniform improvement;
- resignation discourse does not carry Architecture weight;
- GLM rumor is not promoted;
- X remains community observation rather than technical authority;
- vendor/card/partner benchmark limitations remain visible.

No upstream Evidence or Architecture correction is required by this review.

## 5. BLOCKING — reader-facing Japanese technical prose fails Issue #501 standard

The W37 PDF reproduces the exact class of defect previously tracked by Issue #501:

`reader-facing日本語のtechnical meaningが不自然な和語化で崩れている`

This is not a preference for katakana over Japanese. The current Draft systematically substitutes established AI/software terminology with literal or novel Japanese that forces the reader to reconstruct the English technical term.

Independent count across current reader-facing section sources finds:

- `模型`: 15
- `符号`: 14
- `道具立て`: 17
- `代理人`: 5
- `砂場`: 1
- `給仕`: 1
- `引擎`: 1
- `許し`: 10
- `札の...`: 4
- `訳し`: 3
- `混合専門家`: 2
- `検出子`: 4

Representative reader-facing failures include:

- `model -> 模型`
  - 「背後の文章模型」
  - 「符号模型」
  - 「判定模型」
  - 「手元の模型」
- `code -> 符号`
  - 「符号を書く力」
  - 「開かれたCodexの符号」
- `token -> 符号`
  - 「表の1符号あたりの値」
- `harness/tooling -> 道具立て`
  - 「道具立てを束ねる」
- `agent -> 代理人`
  - 「雲の上の代理人」
  - 「複数代理人の枠組み」
- `sandbox -> 砂場`
- `serving -> 給仕`
- `engine -> 引擎`
- `license -> 許し`
  - 「Apache-2.0の許し」
  - 「MITの許し」
- `model card -> 札`
  - 「札の表」
  - 「札の報告」
- `translation -> 訳し`
  - 「訳しに絞った」
- `MoE -> 混合専門家`
- `indicator / IOC -> 検出子`.

Additional awkward editorial phrases include:

- 「金融向けの整え」
- 「三つの出し分け」
- 「効率旗艦」
- 「声の層」
- 「読みの偏り付け」
- 「雲の上の代理人」
- 「公開試し」
- 「引退し、互換の経路」
- 「求めを振り替える」
- 「開かれた重みは縦に伸びる」
- 「安全の物差し」.

Several are semantically opaque; `給仕` and `引擎` are especially unsuitable reader-facing AI infrastructure terminology.

This directly violates the W37 execution requirement to use natural technical Japanese and the acceptance intent of Issue #501.

Issue #501 has therefore been reopened.

## 6. The defect originates in canonical Draft Results

This is not merely a TeX transformation problem.

The same wording is present in canonical Draft Results, including for example:

- `w37-voice-frontier/draft-result.json`
  - 「背後の文章模型」
  - 「道具立て」
- `w37-harness-plane/draft-result.json`
  - 「道具立て」
  - 「雲の上の代理人」
  - 「砂場」
  - 「開かれたCodexの符号」
- `w37-safety-bound/draft-result.json`
  - 「対象の模型」
  - 「複数代理人」
  - 「検出子」
- profile synthesis:
  - 「模型ごとの数値」
  - 「許しの範囲」
  - 「符号の力」.

Therefore a publication-only TeX edit would leave canonical Draft authority semantically defective.

Required bounded regeneration starts at:

`ARCHITECTURE_ESTABLISHED -> Draft`

The approved Architecture itself is not invalidated.

## 7. BLOCKING — Worker review provenance is still misattributed

The W37 execution contract explicitly required worker-generated review to identify itself as Worker/Agent.

One artifact follows this correctly:

`reader-surface-semantic-review-v2.json`

uses:

`Worker/Agent (Muse Spark) — not Sol/Human`.

However:

- `semantic-editorial-review-v2.json`
- `visual-review-v2.json`

both record:

`reviewed_by: "ChatGPT (Muse Spark)"`

and the worker session claims:

`Genuine ChatGPT semantic/editorial QA`.

This run was performed by Muse Spark. No distinct ChatGPT reviewer produced those review artifacts.

That is inconsistent reviewer provenance.

Issue #506 has been updated to cover this downstream recurrence.

Required repair:

- worker-generated semantic/editorial and visual review must identify the actual runner, e.g. `Worker/Agent (Muse Spark)`;
- do not use `ChatGPT`, `Sol`, or `Human` as reviewer identity unless an actual separately bound authority produced the review;
- actual independent Sol review is this artifact.

## 8. Worker semantic-review false positive

The worker semantic/editorial review declares that natural technical Japanese is preserved, yet it passed the phrases listed above.

Therefore its Japanese-language PASS is not accepted as independent quality evidence.

The r2 run must perform an explicit reader-language review against Issue #501 criteria before PDF generation.

The key test is:

> Can a technically literate Japanese reader understand the mechanism, product behavior, metric, license, or limitation without reconstructing the original English phrase?

If not, preserve the conventional English/katakana technical term rather than forcing a novel Japanese substitute.

## 9. Required reader-language repair principles

Regenerated Draft should use established technical Japanese terminology where possible.

Examples of acceptable direction:

- model -> `モデル`
- language/text model -> `言語モデル` / `テキストモデル`
- code / coding -> `コード` / `コーディング`
- token -> `トークン`
- agent -> `エージェント`
- sandbox -> `サンドボックス`
- harness -> `ハーネス` / `エージェントハーネス` where technically appropriate
- serving -> `サービング` / `推論基盤` according to source meaning
- engine -> `エンジン`
- license -> `ライセンス`
- model card -> `モデルカード`
- translation -> `翻訳`
- MoE -> `MoE` / `Mixture-of-Experts` / `混合エキスパート`
- judge model -> `評価用モデル` / `judge model` as context warrants
- IOC / indicators -> `IOC` / `侵害指標` / source-appropriate term.

This is not a mandatory katakana replacement table. Natural Japanese may be used where the technical meaning remains precise.

Do not alter claim strength, attribution, temporal classification, or Evidence boundaries while repairing language.

## 10. Non-blocking visual finding

Exact PDF visual rendering is otherwise acceptable:

- cover and contents are stable;
- two-column body pages render correctly;
- boundary/community boxes are readable;
- bibliography pages are readable;
- no broken URL or glyph rendering observed.

No layout redesign is required solely by this review.

## 11. Regeneration boundary

Required boundary:

`ARCHITECTURE_ESTABLISHED`

Preserve unchanged:

- accepted Grok r3 Raw;
- Discovery;
- Screening;
- Evidence;
- Materiality;
- Completeness;
- Selection;
- approved Architecture r2;
- canonical Human Architecture approval.

Regenerate:

`Draft -> reader-facing source -> PDF -> reader-surface reviews -> Publication Candidate -> fresh Publication Preview r2`

No fresh research is required.

## 12. Sol verdict

`REQUEST_CHANGES`

Blocking findings:

1. reader-facing Japanese technical prose fails Issue #501 semantic-fidelity/naturalness requirement;
2. worker semantic/visual review falsely attributes reviewer identity to `ChatGPT (Muse Spark)`.

Human Publication Preview decision remains:

`PENDING`

Do not record a Human `REQUEST_CHANGES` because Sol requested changes before presenting r1 for Human judgment.

Normal next endpoint after repair:

`RELEASE_CANDIDATE / fresh Publication Preview r2 pending independent Sol review and Human decision`.
