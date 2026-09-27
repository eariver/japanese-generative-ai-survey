# TS-002 Issue-#533 terminology decision ledger

Authority: Issue #533 + Sol execution-boundary comment. Source/entity-bound; no blind global replace.

## Decision counts

- DUPLICATE_ALREADY_APPLIED: 1
- REPLACE: 228
- REPLACE (manual compose of A+B entries): 1
- REPLACE (manual compose of C+B entries): 1
- REPLACE (manual compose of C+C+B entries): 1
- REPLACE (manual compose): 2
- SUPERSEDED_BY_MANUAL_COMPOSE: 7

## High-confidence items (before -> after, residual)

| term | before | after | note |
|---|---|---|---|
| 零射影 | 31 | 0 | all zero-shot verified; canonical ゼロショット系 |
| 声器 | 35 | 0 | vocoder canonical (ボコーダ系 + named models) |
| 符号言語 | 10 | 0 | codec/token LM canonicals |
| 無撞着 | 13 | 0 | Consistency Model（整合性モデル）系, English kept |
| 抽出推論 | 28 | 0 | 推論時サンプリング/サンプリング/生成手順 per context |
| 類別条件 | 5 | 0 | クラス条件 |
| 類別脱落 | 2 | 0 | クラスドロップアウト |
| 変換器 | 57 | 0 | named architectures only, each source-bound |
| ゼロショット素体 | 2 | 0 | REPLACE with AnyGPT base-model zero-shot wording (Sol readback bound) |
| 流れ整合 | 14 | 0 | Flow Matching（フローマッチング） |
| 整流流れ | 3 | 0 | Rectified Flow（整流フロー） |
| 模擬なし | 4 | 0 | simulation-free + Japanese gloss |
| 任意間 | 11 | 0 | any-to-any / 任意モダリティ間 per AnyGPT framing |
| 多能模型 | 2 | 0 | Seed-TTS（多用途・高忠実音声生成）, title-bound (Sol-reviewable) |
| 話声 | 14 | 0 | 音声/発話音声/話者音声 per source |
| 標本化 | 51 | 0 | generative sampling -> サンプリング, each verified |

## Additional candidates: all REPLACE (素体 residual resolved via Sol-bound base-model wording).
## Overlapping sites: 5 manual compositions (C+B, A+B, C+C+B mixes) recorded with both intents.
## Section titles §6/§7 updated by terminology (符号言語 in headings); fidelity locations rebuilt accordingly.