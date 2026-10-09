# TS-003 execution instruction — Draft r3 to Draft r4 under cumulative terminology authority

Status: `EXECUTION_AUTHORITY / SOL_DRAFT_R3_REQUEST_CHANGES / CUMULATIVE_TERMINOLOGY_MAP_R4_REPAIR_ONLY`

Date: `2026-10-02 JST`

Repository: `eariver/japanese-generative-ai-survey`

Branch: `special/vision-multimodal-2026-work`

## 1. Authorities

Sol Draft Review r3:

`sources/SP-vision-multimodal-2026/execution/sol-draft-review-r3.md`

Decision:

`REQUEST_CHANGES`

Reviewed Draft r3 authority commit:

`5e16392d84956b70ee4192657918feb4c4ead265`

Reviewed tree:

`0f4b1d3c4f36d911355ed3991ce9416847a79293`

Binding cumulative terminology authority:

`sources/SP-vision-multimodal-2026/execution/drafting-terminology-map-ja.md`

Authority update commit:

`324d7d7933db2b61c7712b48006480d9b20f6638`

Expected map blob SHA:

`d17d04e3574a33a263f7f10738a601471f6b095d`

Expected map terminal state:

`TS-003_TERMINOLOGY_MAP_CUMULATIVE_R4_BINDING`

Human Architecture r2 remains APPROVED.

This request does not reopen Architecture and is not a new Human gate.

## 2. Start guards

The Sol launch message supplies the sole exact work-branch starting HEAD/tree.

Before any write, read-only verify:

- remote work branch HEAD/tree == launch-message expected HEAD/tree;
- remote main HEAD == `d6381568cc897a47d6de992189e20339350342b7`;
- remote main tree == `83ce3a216d852a1c32d0138f9c56fadefa800666`;
- remote `production/survey-core-v2` HEAD == `774dd39a951c9ac3818e83dfffd4c7666efb0a20`;
- remote Core tree == `cd46a6f7a6dcc4031e76220cea4c52c7dd1fc481`;
- cumulative terminology map blob == `d17d04e3574a33a263f7f10738a601471f6b095d`;
- cumulative terminology map terminal state == `TS-003_TERMINOLOGY_MAP_CUMULATIVE_R4_BINDING`;
- issue == `SP-vision-multimodal-2026`;
- lifecycle == `DRAFT_COMPLETE`;
- Architecture Review == approved;
- Publication Preview == pending;
- draft checkpoint == passed;
- validation/publication_preview/freeze/release == pending;
- current Architecture SHA-256 == `d2f133bcbc84cd4eca729ebcd53bcbdb5bcdae8826ada3acbe0d8623f6c6ec38`;
- current Selection SHA-256 == `378b818e73d328f0b0da3d5207f27098c546c39381ea8ec1035634322555e5ef`.

If any guard differs, perform zero writes and report expected vs actual.

No new branch, fallback branch, repair branch, review branch, reset, rebase, cherry-pick, squash, force push, or history rewrite is authorized.

## 3. Mandatory read order

Read:

1. this request;
2. `execution/sol-draft-review-r3.md`;
3. `execution/drafting-language-policy-ja.md`;
4. `execution/drafting-terminology-map-ja.md`;
5. `execution/language-qa-ja-draft-r3.md`;
6. `execution/draft-r3-20261002/draft-r3-review-report.md`;
7. all 16 canonical Draft r3 Results;
8. current profile synthesis;
9. approved Architecture r2;
10. unchanged Draft Packages;
11. frozen Core Draft schema/prompt/non-mutating validators.

Do not treat Worker r3 `PASS_WITH_NOTES` as Sol approval.

## 4. Mission

Produce Draft r4 by repairing the residual reader-surface failures recorded in Sol Draft Review r3 and the cumulative R4 terminology map.

This is a bounded Draft-only repair.

Do not rerun or modify:

- Discovery;
- Screening;
- Evidence;
- Materiality;
- Completeness;
- Selection;
- Architecture;
- Human Architecture approval.

Do not add new sources or new factual claims from memory/web.

Keep all 16 Draft Package files byte-identical.

Preserve r1/r2/r3 as immutable Git history.

## 5. Highest-priority residuals

### 5.1 Technical segmentation

Audit every `分割` occurrence.

If it means segmentation as a vision task/model family, replace it with the source-appropriate established terminology:

- `セグメンテーション`;
- `セマンティックセグメンテーション`;
- `インスタンスセグメンテーション`;
- `パノプティックセグメンテーション`;
- `オープンボキャブラリーセグメンテーション`;
- or another evidence-supported established form.

Do not alter valid dataset-partition uses such as `学習分割`, `試験分割`, `レア分割`.

P07B is mandatory full review for this distinction.

### 5.2 Bare 測り and evaluation shorthand

Repair noun uses of `測り` when they stand for metric/protocol/condition.

Examples include:

- `測りの切り分け`;
- `測りの同一性`;
- `三つ目の測り`;
- `レアの測り`;
- `接地の測り`;
- `測りは契約ごと`.

Use `評価指標`, `評価方法`, `評価条件`, `測定方法`, `評価プロトコル` as appropriate.

Ordinary verbs `測る` and natural explanatory `測り方` may remain if they are not replacing a technical noun.

### 5.3 決め / 家 / 家系

Repair technical shorthand such as:

- `決めなしの数値`;
- `分割と抽出の決め`;
- `OVD評価の家`;
- model-family senseの `家系`;
- `第二の家`.

Use direct technical wording: evaluation conditions, extraction rule, benchmark role, model family, lineage, repository family, etc.

### 5.4 data augmentation / scaffold / foundation terms

Repair:

- data augmentation senseの `水増し` -> `データ拡張`;
- scaffold senseの `足場` -> `scaffold（補助的手順）` or `補助的手順`;
- foundation/base/backbone senseの `土台` -> `基盤モデル`, `基盤`, `バックボーン`, or `基盤表現`.

Do not replace ordinary nontechnical uses blindly.

### 5.5 Residual metaphor phrases

Rewrite directly:

- `載せ方と組み方と式と移し`;
- `呼びの到達`;
- `結びの仕組み`;
- `教師モデルの写しの産物`;
- streaming senseの `流れの契約`;
- `流れのオムニ`;
- release/availability senseの `配り方 / 配りの範囲`;
- `軸の勘定`;
- `一つの芸`;
- technical additional-sample senseの `追加試料`;
- `フューショット` when the intended term is few-shot;
- neural-unit senseの `素子`;
- openness-mixture senseの `まだら`.

Use the actual technical concept. Do not replace with a new metaphor.

## 6. Cumulative-map maintenance remains mandatory

Run the full map Pass A/B/C.

If a genuinely new terminology failure is discovered:

1. add it to the cumulative map first;
2. repair every occurrence;
3. rerun the complete terminology audit;
4. record the final map blob SHA in r4 QA/report.

Do not silently repair a new failure without updating the map.

## 7. Preserve prior gains

Preserve:

- zero exact duplicates;
- no padding;
- no neural-network `網`;
- no teacher/student school-personification;
- no source-code `符号`;
- no `多様式`;
- no technical `幻覚`;
- no raw English CLAIM_BOUNDARY dump;
- explicit source/evaluator roles;
- P07B mechanism grouping;
- P09 protocol-bound comparisons;
- P15 synthesis density.

Do not restore r1 length.

## 8. Integrity

Preserve all bound Evidence references and must-cover content.

Preserve source-role attribution.

Preserve CLAIM_BOUNDARY dispositions unless wording alone changes.

Preserve G01–G06 and all PARTIAL semantics without reader-facing internal labels.

Do not change Architecture.

If a repair would require new Evidence, flag it for Sol instead of researching.

## 9. Language QA r4

Create:

`sources/SP-vision-multimodal-2026/execution/language-qa-ja-draft-r4.md`

It must include:

- cumulative-map authority path/blob/status;
- exact duplicate scan by package;
- full preferred/avoid conformance;
- full known-failure registry audit;
- technical segmentation-vs-dataset-split classification for every `分割` hit in P07B;
- bare-`測り` audit;
- `決め` audit;
- `家/家系` audit in technical contexts;
- `水増し` classification: data augmentation vs ordinary inflation;
- `足場` audit;
- technical `土台` audit;
- `配り方/配りの範囲` audit;
- residual metaphor audit for all Sol r3 examples;
- code/encoding audit;
- source-role audit;
- CLAIM_BOUNDARY audit;
- P06/P07A/P07B/P09/P13/P14/P15 manual qualitative review;
- new failures discovered during r4, if any, plus map updates.

Do not claim PASS from regex counts alone.

## 10. Deterministic validation

Run available canonical non-mutating Draft Result + synthesis validation while lifecycle remains `DRAFT_COMPLETE`.

Do not fake rollback.

Do not call reader-publication validation.

## 11. Required r4 review report

Create:

`sources/SP-vision-multimodal-2026/execution/draft-r4-20261002/draft-r4-review-report.md`

Report:

- startup guards;
- reviewed r3 commit/tree;
- Sol r3 review authority;
- cumulative-map starting blob/status;
- map changes, if any, and final blob;
- unchanged Draft Package hashes;
- revised Draft Result hashes;
- synthesis hashes;
- duplicate scan;
- segmentation audit;
- terminology-map conformance;
- known-failure regression result;
- residual metaphor repair;
- source-role preservation;
- CLAIM_BOUNDARY status;
- G01–G06/PARTIAL preservation;
- P06/P07A/P07B/P09/P13/P14/P15 review;
- QA r4 path/hash/status;
- deterministic validation result;
- lifecycle/next_action;
- Publication Preview pending;
- main/Core unchanged;
- final HEAD/tree.

## 12. Lifecycle boundary

Keep `DRAFT_COMPLETE`.

Do not:

- call reader-publication validation;
- create Publication Preview;
- record Human Publication Preview decision;
- Freeze;
- Release.

## 13. Terminal condition

`TS-003 DRAFT_R4_CUMULATIVE_TERMINOLOGY_REPAIR_COMPLETE`

`TS-003 LANGUAGE_QA_R4_COMPLETE`

`AWAITING_SOL_DRAFT_REVIEW_R4`

`NO_READER_PUBLICATION_VALIDATION`

`NO_HUMAN_PUBLICATION_PREVIEW_DECISION`

`NO_FREEZE`

`NO_RELEASE`

STOP there.
