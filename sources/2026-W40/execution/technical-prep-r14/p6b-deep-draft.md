# P6b deep draft r14 — evaluation and execution infra (NON_CANONICAL technical prep)

Status: `TECHNICAL_PREP_R14 / NON_CANONICAL / NOT_ARCHITECTURE / NOT_READER_PROSE`
Covers (ordinary 28 only): `candidate:2026-W40:9de6ffd245268468` (AgentPerf, PRIMARY)
+ `candidate:2026-W40:113e97bcb642e557` (OpenTTS, PRIMARY)
+ `candidate:2026-W40:bed589208da5f196` (RL Environments Hub, SUPPORTING).
Basis: W40 accepted Evidence/Views (publisher claim-level notes + bounded excerpts).
Publisher-only metrics と再現可能事項を分離し、named numerator/denominator/hardware/
baseline/version を付記。消費範囲外は `UNVERIFIED` — 捏造しない。
HUMAN APPROVED としての引用・`architecture-v2.json`・`main.tex` への混入はしない
(いずれも本単位では書かない)。

## 1. AgentPerf — serving-only benchmark (Artificial Analysis, Sep 29 day-only)

Source: https://artificialanalysis.ai/articles/aa-agentperf-local (EVALUATOR_PUBLISHER;
日付は publisher header の day-only)。Code: github.com/ArtificialAnalysis/aa-agentperf-local
(存在として消費; 版ピン UNVERIFIED)。
性質の境界 (Sol 確定・publisher 自認): 推論サービングの測定であり、自律タスク正答率や
モデル知能の評価ではない。混同しない。

### 仕組み (workload replay)

実エージェント軌跡のリプレイ: 8 tasks / 168 turns / ~56K growing context /
identical token work (同一トークン作業の固定)。tool execution は default で skip。
単一エージェント・全システム焦点; マルチエージェント・共有負荷は publisher によれば
pending。ハード・ソフトは速く変化し、leaderboard は living (frozen の W40 権威とせず
commit pin なしでは引用しない)。

### 条件・指標 (publisher-measured; 分母明示)

| 主張 | 分子/分母・条件 | ベースライン・版 |
|---|---|---|
| 対象 HW: DGX Spark 128GB / RTX 5090 32GB / Ryzen AI Max+ Halo 128GB / MacBook Pro M5 Pro 64GB | 初期カバレッジ 4 プラットフォーム (publisher 方法記述) | — (測定母集団の定義) |
| 対象モデル: Qwen3.5-9B, Qwen3.8-27B, Qwen3.6-35B-A3B, Ling 3.0 Flash 124B/5B-active (4-bit) | モデル×量子化の組み合わせ | — (同上) |
| 14 configs (speculative decoding: MTP/DFlash/DSpark) | 構成数 14 (内訳の完全列挙は UNVERIFIED; 技法名のみ消費) | 非投機 baseline との対比 (構成対応表 UNVERIFIED) |
| active-params trend (例外あり) | 傾向記述 (例外の具体名 UNVERIFIED) | — |
| RTX 5090 fastest where fits (>3.5x) | 収まる場合の速度比 (分母=比較対象構成; 厳密対応 UNVERIFIED) | 比較構成 |
| Spark 1.4–1.7x Halo (3/4 models), 帯域差 7% にもかかわらず | 4 モデル中 3 での比率; compute/CUDA 成熟度の寄与 (publisher 解釈) | Ryzen Halo |
| MacBook within 2–9% Halo (2 models) | 2 モデルでの近接率 | Ryzen Halo |
| prefill share 22–41% (Qwen3.8-27B), KV-cache hit 73–93% にもかかわらず | プリフィル占有率の範囲 | — (内部内訳の解釈として帰属) |
| speculative +30–120% decode | デコード改善率の範囲 (構成依存) | 非投機構成 |
| 価格は MSRP vs inflated street を区別 | 表示価格の基準注記 | — |

### 再現性 vs publisher-only

再現可能: リプレイ手順 (同一トークン作業・tool skip default) + 公開コードの存在 +
HW/モデル/構成名。Publisher-only: 全測定値 (第三者再現なし)、living 変動分、
価格の実勢。引用時は版・日付ピン必須 (living のため)。

## 2. OpenTTS — objective TTS evaluation platform (Hugging Face, Sep 30 day-only)

Source: HF Open TTS Leaderboard (PLATFORM release; day-only "September 30, 2026")。
性質の境界 (Sol 確定): 評価プラットフォームのリリースであり、新しい音声モデルではない。
客観指標は human MOS/MUSHRA/arena preference を補完するが置換しない。WER/SIM は
proxy であり自然さそのものではない (「最良 TTS モデル」の verdict として提示しない)。

### 仕組み (metrics)

- 客観・多言語 + voice-cloning 評価。WER/CER は Qwen3-ASR-1.7B による計測、
  RTFx/TTFA は H200 GPU/CPU、SIM は WavLM embeddings。Seed-TTS-Eval + CV3-Eval。
  Spaces app + Listen tab、eval scripts repo 公開 (存在として消費; 版 UNVERIFIED)。
- スナップショット: 英語 WER リーダー Kokoro-82M / supertonic-3 / s2-pro、
  多言語 OmniVoice / s2-pro / Fun-CosyVoice3、streaming pocket-tts、
  voice-clone SIM table (いずれも vendor-reported snapshot; 数値自体は r14 消費範囲外→
  リーダー名のみ主張し WER 値の引用は UNVERIFIED として行わない)。
- 文脈値: AA モデルのうち open-weights は 16/92 (arena skew の文脈として消費;
  arena 側の測定条件 UNVERIFIED)。

### 条件・指標

| 主張 | 分子/分母・条件 | ベースライン・版 |
|---|---|---|
| WER/CER (via Qwen3-ASR-1.7B) | 認識誤り率 (評価集合= Seed-TTS-Eval + CV3-Eval) | プラットフォーム内比較 (スナップショット) |
| RTFx / TTFA (H200 GPU/CPU) | 速度・初音レイテンシ (HW 固定) | 同上 |
| SIM (WavLM embeddings) | 話者類似度 (proxy) | 同上 (human preference ではない) |
| 16/92 open-weights | AA 側母集団における公開重み比率 | arena 文脈値 |

### 限界

human-preference の証明なし。数値は leaderboard snapshot であり普遍ランキングでは
ない。音声素材・評価レーンのリードは discovery 事項であり selection ではない
(claim-note 境界を継承)。

## 3. RL Environments Hub — cross-framework discovery/integration (HF, Sep 28 day-only; SUPPORTING)

Source: huggingface.co/blog/rl-environments (FIRST_PARTY day-only "Published
September 28, 2026"; 時刻・TZ は UNVERIFIED のため T12:00:00Z 等を捏造しない)。
役割: SUPPORTING (相互運用タグ意味・seeded taskset・per-config future)。
性質の境界 (publisher-stated, 継承必須): 今回 W40 ローンチは cross-framework の
discovery/integration 機能であり、2025 年の OpenEnv 創設でも、新規モデル学習結果でも
ない。per-config snippet・構造検出は forward-looking (未出荷)。reward-None / error
inspection の注意。bare Hub repo ID は Harbor registry の repo+dataset ペアを代替
しない。

### 仕組み (architecture, publisher-stated)

- 専用 `rl-environment` dataset filter + 4 framework 互換タグ
  (`harbor`, `verifiers`, `openenv`, `nemo-gym`) と framework 別生成 `Use this dataset`
  snippet。dataset-repo 基盤の発見・版管理・議論。
- taskset dataset は runtime/reward 実行から分離可能。新 repo type・registry・sign-up
  なし。framework がファイルを読み込み、local または対応 cloud (Jobs/Sandboxes) で
  実行。タグは互換宣言であり、形式変換も job/sandbox 起動もしない。
  マルチタグ可 (各 framework がファイル対応必須)。
- 例 (publisher-provided, version-pinned — 版ピン付きで引用):
  harbor oracle `harbor==0.21.0` on terminal-bench-2.1@2.1.0 `*regex-log`;
  verifiers v1 harbor integration (Docker/bash harness, registry.json conventions);
  openenv[harbor]==0.7.0 rollout (Docker, Gradio tunnel, reward None semantics);
  NeMo Gym structured-outputs (schema adherence, not factuality)。
- seeded content (publisher-stated snapshot; 件数は snapshot としてのみ):
  Harbor (BeyondSWE, Terminal-Lego-15k, harbor-mix 100, NatureBench 90);
  Verifiers (Reverse-Text-RL, Multi-SWE-RL-Verified 2,232/4,703, R2E-Gym-Subset,
  Scale-SWE-Verified 17,202/20,181); NeMo Gym (Workplace Assistant 5DB/26tools/
  690tasks, Structured Outputs, CFBench, SysBench)。
- コマンド・版は Sep 28 snapshot; リポジトリ・framework は変化するため引用時は版ピン
  必須 (claim-note 境界を継承)。

### P6b 内の位置づけ

AgentPerf・OpenTTS の PRIMARY 測定に対し、RL-Env Hub は相互運用・配布層の
SUPPORTING。Holo4 (agent models)・Olmo-core 3 (MoE 学習スタック)・AutoSynthData
(synthetic curriculum) とは別物として区別する (claim-note §6 を継承)。

## 4. Source→Claim table (P6b)

| 段落主張 | Source | Class | ID anchor |
|---|---|---|---|
| AgentPerf リリース事実・リプレイ定義・HW/モデル/14 configs | AA article | PRIMARY_FACT (方法記述) / EVALUATOR_CLAIM (測定値) | evidence:2026-W40:6b710e391126f2cd |
| serving-only 境界・living 注意 | AA article + Sol register | EDITORIAL_BOUNDARY | 同 task (INFERENCE 行) |
| OpenTTS リリース事実・指標定義・scripts 存在 | HF leaderboard | PRIMARY_FACT (platform) | evidence:2026-W40:35982cdbdced5526 |
| リーダー名・16/92・proxy 免責 | HF leaderboard | PUBLISHER_CLAIM / BOUNDARY | 同 task (数値引用なし) |
| RL-Env Hub ローンチ・タグ・アーキテクチャ・版ピン例・seeded 件数・境界 | HF blog (full-read claim-note) | PRIMARY_FACT (arch記述) / PUBLISHER_CLAIM (例・件数) | evidence:2026-W40:5d98661975a7fd04 |

## 5. 日本語品質セルフレビュー (paragraph-level)

- 訳語: workload replay「作業負荷リプレイ」(初出英語併記)、speculative decoding
  「投機的デコーディング」、話者類似度 (SIM)、初音レイテンシ (TTFA)。
- 過剰漢字の回避: 「相互運用性」は interoperability の定訳として維持するが、
  「配布層」は distribution layer の意訳である旨を文脈で明示した。
- 帰属の徹底: publisher 測定値には「〜と報告」「publisher によれば」を付け、
  evaluator と独立再現の区別を崩さない。living 変動の注意は断定形にしない。
- 残課題: WER 数値・14 構成内訳・snippet 全文は原文確認待ち ( cited しない)。
