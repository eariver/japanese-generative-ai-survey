# TS-003 execution instruction — Draft r2 terminology/readability repair to Draft r3

Status: `EXECUTION_AUTHORITY / SOL_DRAFT_R2_REQUEST_CHANGES / DRAFT_R3_TERMINOLOGY_READER_SURFACE_REPAIR_ONLY`

Date: `2026-10-02 JST`

Repository: `eariver/japanese-generative-ai-survey`

Branch: `special/vision-multimodal-2026-work`

## 1. Authority

Sol Draft Review r2:

`sources/SP-vision-multimodal-2026/execution/sol-draft-review-r2.md`

Decision:

`REQUEST_CHANGES`

Reviewed Draft r2 authority commit:

`4a553c33385cb245d7239c116812999560165188`

Reviewed tree:

`f1f6fdf5582d30d03a280aea00e872dcf026a30f`

Human Architecture r2 remains APPROVED.

This is not a new Human gate and does not reopen Architecture.

## 2. Start guards

Do not hard-code the launch work-branch SHA/tree in this file. The Sol launch message supplies the sole exact work-branch start SHA/tree.

Before any write, read-only verify:

- remote work branch HEAD/tree == launch-message expected HEAD/tree;
- remote main HEAD == `d6381568cc897a47d6de992189e20339350342b7`;
- remote main tree == `83ce3a216d852a1c32d0138f9c56fadefa800666`;
- remote `production/survey-core-v2` HEAD == `774dd39a951c9ac3818e83dfffd4c7666efb0a20`;
- remote Core tree == `cd46a6f7a6dcc4031e76220cea4c52c7dd1fc481`;
- issue == `SP-vision-multimodal-2026`;
- lifecycle == `DRAFT_COMPLETE`;
- Architecture Review == approved;
- Publication Preview == pending;
- draft checkpoint == passed;
- validation/publication_preview/freeze/release == pending;
- current Architecture SHA-256 == `d2f133bcbc84cd4eca729ebcd53bcbdb5bcdae8826ada3acbe0d8623f6c6ec38`;
- current Selection SHA-256 == `378b818e73d328f0b0da3d5207f27098c546c39381ea8ec1035634322555e5ef`.

If any guard differs, perform zero writes and report expected vs actual.

No new branch, fallback branch, repair branch, review branch, reset, rebase, cherry-pick, squash, force push or history rewrite is authorized.

## 3. Mandatory read order

Read at minimum:

1. `sources/SP-vision-multimodal-2026/execution/sol-draft-review-r2.md`
2. `sources/SP-vision-multimodal-2026/execution/drafting-language-policy-ja.md`
3. `sources/SP-vision-multimodal-2026/execution/drafting-terminology-map-ja.md`
4. `sources/SP-vision-multimodal-2026/execution/language-qa-ja-draft-r2.md`
5. `sources/SP-vision-multimodal-2026/execution/draft-r2-20261001/draft-r2-review-report.md`
6. all 16 canonical Draft r2 Results
7. current profile synthesis
8. approved Architecture r2
9. unchanged Draft Packages
10. frozen Core Draft schema/prompt/validators

Do not treat the Worker r2 `PASS_WITH_NOTES` or `F1-F5_CLOSED` claim as Sol approval. The Sol r2 review supersedes that self-assessment.

## 4. Mission

Produce Draft r3 by repairing reader-facing terminology and remaining metaphorical prose only.

Do not rerun or modify:

- Discovery;
- Screening;
- Evidence;
- Materiality;
- Completeness;
- Selection;
- Architecture;
- Human Architecture approval.

Do not add sources or facts from memory/web.

Keep all 16 Draft Package files byte-identical.

Preserve Draft r1 and r2 as immutable Git history.

Use the current schema-valid revision mechanism for Draft r3. Do not invent fields.

## 5. Binding terminology map is authoritative

The edition-local terminology map is mandatory, not advisory.

For every reader-facing headline, deck, PARAGRAPH, TABLE, BULLET and CLAIM_BOUNDARY block, enforce the map semantically.

Required examples:

- neural network -> `ニューラルネットワーク` / `CNN`, never technical `網`;
- multimodal -> `マルチモーダル`, never `多様式 / 多模式`;
- teacher model -> `教師モデル`;
- student model -> `生徒モデル`;
- post-training -> `ポストトレーニング`;
- hallucination -> `ハルシネーション`;
- segmentation -> `セグメンテーション` when the technical operation is meant;
- deployment -> `デプロイ` or `実運用` according to context, with volume-level consistency;
- source/software code -> `コード`, `ソースコード`, `推論コード`, `学習コード`;
- World Model -> `ワールドモデル`;
- multimodal model -> `マルチモーダルモデル`;
- modality -> `モダリティ`.

Do not perform blind global replacement. Words such as `符号化` are legitimate when the concept is actual encoding. Generic `切り分ける` may be legitimate when the sentence literally means separating two concepts. The prohibited case is substituting an ordinary Japanese word for a load-bearing technical term.

## 6. Required targeted repairs

### 6.1 P06 / P07B teacher-student language

Remove recurrent school-personification wording:

- `教員`;
- `教員モデル`;
- `教員役`;
- bare `生徒`.

Rewrite ViLD / RegionCLIP / DeiT / DINO passages using standard distillation terminology.

The r2 sentence:

`CLIP・ALIGNの教員を二段の生徒に蒸留する。`

must not survive.

Use technically direct wording such as `CLIP/ALIGNを教師モデルとして二段検出器へ知識蒸留する` only when that wording is supported by the bound Evidence.

### 6.2 P09 / P11 multimodal terminology

Replace technical `多様式` with `マルチモーダル`.

P09 `事後学習` -> `ポストトレーニング` where the technical concept is post-training.

Do not create a different Japanese synonym to evade the map.

### 6.3 P15 hallucination terminology

Where the concept is model hallucination, use `ハルシネーション`.

Do not use clinical/general `幻覚` as the technical term.

### 6.4 P01 / P03 segmentation wording

Audit every `切り分け / 塗り分け` occurrence.

Where it refers to segmentation as the technical task/operation, restore `セグメンテーション`, `セマンティックセグメンテーション`, `インスタンスセグメンテーション`, or the source-appropriate established form.

Where it merely means “distinguish/separate” in ordinary Japanese, it may remain.

### 6.5 Source/software code wording

Audit `符号`.

When it means code in a repository/software artifact, use `コード` or a specific standard term.

Do not alter actual encoding terminology such as character encoding, positional encoding, time encoding, or representation encoding where `符号化` is technically correct.

### 6.6 Residual metaphor substitutions

Rewrite direct reader-facing examples such as:

- `受け口`;
- `袋詰め`;
- `袋にまとめて照らす`;
- `契約の家`;
- `語彙の足し`;
- `遅い渡し`;
- `固い混ぜ`;
- `規模の回し`;
- `レア側の埋め`;
- `投票は幻のふるい`;
- repeated editorial `錨`;
- `投票の素描`;
- `二言語の輪切り`;
- `配りの極`;
- other equivalent invented metaphors discovered during the full-volume read.

Do not replace these with new metaphors. State the mechanism, evaluation role, comparison axis, source role, or transition directly.

## 7. Full-volume semantic terminology audit

Do not limit the repair to the examples above.

Perform two passes:

### Pass A — terminology-map conformance

For every row in the binding terminology map:

- search preferred form;
- search avoid forms;
- inspect semantically equivalent improvised alternatives;
- classify each hit as technical term vs ordinary-language use;
- repair all technical-term violations.

### Pass B — manual prose review

Read all 16 reader surfaces plus synthesis and CLAIM_BOUNDARY blocks.

Look specifically for:

- over-translation;
- over-domestication;
- metaphor used instead of terminology;
- invented technical Japanese;
- source-code -> `符号`;
- teacher/student personification;
- segmentation euphemisms;
- multimodal euphemisms;
- repeated rhetorical connective tissue.

A replacement is not accepted merely because the original bad string disappears.

## 8. Preserve the r2 improvements

Do not undo:

- zero exact duplicate sentences;
- raw English CLAIM_BOUNDARY repair;
- source-role attribution repair;
- P07B mechanism grouping;
- P09 protocol-bound comparisons;
- P15 deduplication and shorter information-dense structure.

Do not re-pad to restore r1 length.

## 9. Language QA r3

Create:

`sources/SP-vision-multimodal-2026/execution/language-qa-ja-draft-r3.md`

It must include:

- exact duplicate sentence scan by package;
- full terminology-map conformance table;
- every avoid-form hit and disposition;
- teacher/student counts and contexts;
- multimodal terminology counts and contexts;
- post-training terminology counts;
- hallucination terminology counts;
- segmentation-specific `切り分け/塗り分け` audit;
- `符号` audit split into legitimate encoding vs incorrect source-code usage;
- residual metaphor audit;
- CLAIM_BOUNDARY audit;
- internal jargon scan;
- P07B/P09/P15 manual qualitative review.

Do not claim `0` without scanning every reader-facing block class, including CLAIM_BOUNDARY.

If any avoid-form remains intentionally, quote the exact sentence and explain why it is ordinary Japanese rather than a technical-term substitution.

## 10. Deterministic integrity

Preserve all required Evidence refs and must-cover content.

Do not weaken attribution.

Preserve boundary dispositions unless wording alone changes.

Do not change Architecture to make prose easier.

If a correction would require new Evidence, do not research; flag it for Sol.

Run the canonical non-mutating validators available for the revised Draft Results and synthesis at `DRAFT_COMPLETE`.

Do not fake lifecycle rollback.

## 11. Required Draft r3 review report

Create:

`sources/SP-vision-multimodal-2026/execution/draft-r3-20261002/draft-r3-review-report.md`

Report at least:

- startup guard results;
- reviewed r2 commit/tree;
- Sol r2 review authority;
- unchanged Draft Package hashes;
- revised Draft Result hashes;
- synthesis hashes;
- exact duplicate scan;
- terminology-map conformance;
- targeted bad-term before/after counts;
- semantic `符号` audit;
- segmentation audit;
- residual metaphor findings;
- source-role preservation;
- CLAIM_BOUNDARY status;
- G01-G06 / PARTIAL semantic preservation;
- P07B/P09/P15 review;
- language-QA r3 path/hash/status;
- deterministic validation results;
- lifecycle/next_action;
- Publication Preview pending;
- main/Core unchanged;
- final HEAD/tree.

## 12. Lifecycle boundary

Do not call reader-publication validation.

Do not create Publication Preview.

Do not record a Human Publication Preview decision.

Do not freeze or release.

Current `DRAFT_COMPLETE` remains valid.

## 13. Terminal condition

Normal terminal labels:

`TS-003 DRAFT_R3_TERMINOLOGY_READER_SURFACE_REPAIR_COMPLETE`

`TS-003 LANGUAGE_QA_R3_COMPLETE`

`AWAITING_SOL_DRAFT_REVIEW_R3`

`NO_READER_PUBLICATION_VALIDATION`

`NO_HUMAN_PUBLICATION_PREVIEW_DECISION`

`NO_FREEZE`

`NO_RELEASE`

STOP there.
