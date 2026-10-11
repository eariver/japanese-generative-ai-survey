# P6b deep draft r15 — AgentPerf + OpenTTS + RL-Env Hub (NON_CANONICAL successor)

Status: `TECHNICAL_PREP_R15 / NON_CANONICAL / NOT_ARCHITECTURE / NOT_READER_PROSE`
Successor of (r14 preserved immutable): `../technical-prep-r14/p6b-deep-draft.md`
Covers (ordinary 28 only): `candidate:2026-W40:9de6ffd245268468` (AgentPerf, PRIMARY)
+ `candidate:2026-W40:113e97bcb642e557` (OpenTTS, PRIMARY)
+ `candidate:2026-W40:bed589208da5f196` (RL-Env Hub, SUPPORTING).
New r15 retrievals (2026-10-10 JST): AA article full page (355,778 B — roofline/
14-configs/local-vs-production verified); HF Open TTS blog full page (323,513 B —
aggregation/TTFA/scripts-future verified); GH API repo facts
(huggingface/open-tts-leaderboard: created 2026-09-15T01:43:54Z, Apache-2.0,
commits 36b6a79e2e9a → 1645e63016f0 (eval scripts, 2026-10-07) → 2b2cd31257d2
(2026-10-09 HEAD)).
Every quantitative claim cites primary URL + section/pin. `VERIFIED` = text-confirmed,
not independently replicated. Never HUMAN APPROVED; never into `architecture-v2.json` /
`main.tex` (not written).

## 1. AgentPerf (AA-AgentPerf-Local, Sep 29 day-only; W40-period article re-read r15)

Source: https://artificialanalysis.ai/articles/aa-agentperf-local (EVALUATOR_PUBLISHER)。
Code/repo + configs page の存在として消費 (版ピン UNVERIFIED; Sep29 announcement と
later code の区別は §1.4)。
性質境界: 単一ユーザーの推論サービング測定。自律正答率・モデル知能の評価ではない。

### なぜ roofline 比較なのか (F05 correction)

r14 までの「speculative +30–120%」は対照群 (speculative-off) との差分に読めたが誤り。
原文: "Speculative decoding was implemented on all of the most successful configs so
far, e.g. raising Qwen3.8-27B decode speeds ~30-120% above the bandwidth-constraint
roofline." すなわち (i) 比較対象は memory-bandwidth 制約の roofline (理論上限線) であり
(ii) 非投機対照群との差ではない。(iii) 主語は "most successful configs" の
Qwen3.8-27B デコード速度という範囲付き主張である。Single-user decoding が memory
bandwidth に強く影響されること (5090: 1,792 GB/s vs unified-memory 256–307 GB/s) が
roofline 比較の前提として同記事に書かれている。+30–120% の幅は構成依存の範囲であり、
単一代表値に丸めない。

### 14 configs の実態 (all-speculative verified)

"Where an official off-the-shelf config was available for a system and model pair, we
used the published config. We developed our own configs for all other cases. Every
config uses speculative decoding (MTP, DFlash or DSpark), and all 14 are published in
the repo and on the configs page." 初期 14 構成は例外なく投機的手法
(MTP / DFlash / DSpark のいずれか) を用いる — 独立監査の指摘通り。
official 既製品 config と自作 config の区別あり ("developed our own for all other
cases")。repo + configs page に全公開 (存在として消費; 各構成の完全列挙・版ピンは
UNVERIFIED)。"all/strongest initial configs" を超える一般化 (全将来構成が投機的等)
はしない。

### 条件・指標 (source-specific definitions)

| 主張 | 定義・分母・条件 | ベースライン・版 |
|---|---|---|
| replay: 8 tasks / 168 turns / ~56K growing context / identical token work | 同一トークン作業の固定 (task 集合は default trajectory set) | publisher 方法記述 |
| tool execution skipped by default | 実行スキップ既定 (忠実度への影響は publisher 注記範囲) | 同上 |
| HW 4種: Spark 128GB / RTX 5090 32GB / Ryzen Halo 128GB / M5 Pro 64GB | 初期カバレッジ (publisher 記述) | 測定母集団の定義 |
| モデル: Qwen3.5-9B, Qwen3.8-27B, Qwen3.6-35B-A3B, Ling 3.0 Flash 124B/5B-active (4-bit) | モデル×量子化 | 同上 |
| completion time ↔ active params (例外あり): Qwen3.6-35B-A3B (3B active) が全 system で最速 (dense 27B 比 2.5–3.3x); Ling (124B/5B-active) は Qwen3.5-9B に後塵 | 対応表は記事内範囲 | — (傾向記述) |
| 5090 fastest where fits (>3.5x) | 収まる場合の完了時間比 | 他 systems |
| Spark 1.4–1.7x Halo (3/4 models; Halo は Qwen3.5-9B で tie) | default trajectory set | Ryzen Halo (帯域差 7% に対し compute/CUDA 成熟度の寄与と解釈) |
| MacBook within 2–9% Halo (2 models) | 2 モデル範囲 | 同上 |
| prefill 22–41% (Qwen3.8-27B), KV-hit 73–93% にもかかわらず | 占有率範囲 | — |
| 価格: MSRP 基準表示 + custom entry; Spark/Halo 同一 MSRP $4,000 | 表示基準注記 (実勢高騰の注記あり) | — |

### local vs production (different methods — no conflation)

本件 (Local): 単一ユーザー serving replay (上記)。
別件 AA-AgentPerf (2026-06-12 記事, 同サイト内リンク): "measures how many concurrent
agents an AI system can serve on real coding-agent trajectories while meeting
production service-level targets, with Agents per Megawatt as its lead metric"
(concurrent + production SLO + 効率指標)。方法も指標も別物であり、数値の相互引用・
統合をしない。living 性: HW/soft 急変 + leaderboard living のため版・日付ピン必須。

## 2. OpenTTS (HF blog Sep 30 day-only; full-page re-read r15)

Source: https://huggingface.co/blog/open-tts-leaderboard (PLATFORM)。
性質境界: 評価プラットフォーム。音声モデルではない。客観指標は human preference
(MOS/MUSHRA/arena) を補完し置換しない。"human preference is the ultimate decider"
(blog)。"Numbers only tell part of the story" (同)。

### 集計定義 (F06 — announcement defines)

- Intelligibility: prompt と生成音声 transcript 間の WER/CER (Qwen3 ASR 計測;
  top ranking open-source model on the Open ASR Leaderboard と位置づけ)。
- Speed: RTFx = batched offline inference (H200 GPU); TTFA = streaming batch-size-1
  latency (H200 GPU and CPU)。
- SIM: WavLM speaker embeddings 間の cosine similarity (生成音声 vs 参照音声;
  voice cloning 時の参照あり条件と対応)。
- ランキング: Seed TTS Eval + CV3 Eval (zero shot) の English splits 上の
  macro-average WER。英語リーダー: hexgrad/Kokoro-82M, Supertone/supertonic-3,
  fishaudio/s2-pro (snapshot; 値の引用はしない — リーダー名のみ)。
- 多言語: per-language 表示切替。Seed TTS Eval は英・中のみ音声あり、他言語は CV3
  Eval (zero shot) のみ。中国語・日本語・韓国語は character-based のため CER を報告。
  "Average WER" across languages は macro-average across languages。
  強い多言語: k2-fsa/OmniVoice, fishaudio/s2-pro, Fun-CosyVoice3-0.5B-2512。
- Voice cloning 切替で SIM 列 + Pareto 追加表示。一部モデル (例 bosonai/higgs-tts-3-4b,
  openbmb/VoxCPM2) は参照音声ありで average WER 改善 (条件付き事実として保持)。

### TTFA 測定プロトコル (each clause verified)

"Every model runs one audio at a time (batch size 1), on the same 50 English prompts
from CV3-Eval, on the same hardware and in its default voice. We drop the first 3 runs
as warm-up and report the median TTFA across the rest. The default view compares
performance on an H200 GPU. Results are also available for CPU for a small (but
growing) set of models!" — batch=1 / 50 prompts (CV3-Eval English) / same HW+default
voice / 先頭3 run 除外 / median / H200 既定表示 (+CPU は small growing 集合) の
各節を原文確認済み。kyutai/pocket-tts は GPU+CPU の streaming 向きと言及 (定性)。

### 依存・免責・スナップショット境界

依存: Qwen3-ASR-1.7B-hf (認識), bezzam/wavlm_large_finetune_seed_tts_eval (SIM)。
品質 proxy 注意: WER/SIM は proxy であり naturalness/expressiveness/listener
preference を直接測らない (blog 明記)。比較は snapshot (as-of 記載; 普遍 ranking
化しない)。文脈値 16/92 open-weights (AA TTS 側母集団; arena 条件 UNVERIFIED)。

### 時間分割 (temporal split — backdating prohibition)

- 記事時点 (Sep 30): "We will soon open-source the evaluation scripts, much like the
  Open ASR Leaderboard repo" — script 公開は FUTURE 形。
- 今日の repo 実態 (GH API, r15 取得): huggingface/open-tts-leaderboard、
  created 2026-09-15T01:43:54Z、Apache-2.0、commits: 36b6a79e2e9a (Initial,
  2026-09-15) → 1645e63016f0 ("Initial commit of eval scripts", 2026-10-07T14:53:41Z)
  → b7bfc47addcd (readme nits, 10-07) → 2b2cd31257d2 ("Add paradee scripts (#5)",
  2026-10-09T08:25:36Z = HEAD)。
- 帰結: W40 cutoff (Oct 2 22:00Z) 時点で eval scripts は repo に存在しなかった
  (scripts 着地は Oct 7 — commit history による dated negative)。
  repo 作成 (Sep 15) をもって script 公開と読まない。backdate しない。

## 3. RL-Env Hub (SUPPORTING; F07 — reproducibility pinning)

役割・タグ・分離・現行/将来境界は r14 承継 (変更なし):
`rl-environment` filter + 4 tags (harbor/verifiers/openenv/nemo-gym);
taskset dataset ∥ runtime/reward; 新 repo type なし; tag = 互換宣言 (変換・起動なし);
per-config snippet・構造検出は forward-looking; OpenEnv 創設 (2025) でも学習結果でも
ない; bare repo ID ≠ Harbor registry pair。

### Reproduction sample pinning (exact revisions or NOT_REPRODUCIBLY_PINNED)

- API/framework pins (利用可能・保持): `harbor==0.21.0` (oracle on
  terminal-bench-2.1@2.1.0 `*regex-log`), verifiers v1 (Docker/bash harness,
  registry.json conventions), `openenv[harbor]==0.7.0` (Docker, Gradio tunnel,
  reward None semantics), NeMo Gym structured-outputs (schema adherence, not
  factuality)。いずれも Sep 28 snapshot (claim-note)。
- Taskset repository revisions: BeyondSWE / Terminal-Lego-15k / harbor-mix 100 /
  NatureBench 90 / Reverse-Text-RL / Multi-SWE-RL-Verified / R2E-Gym-Subset /
  Scale-SWE-Verified / Workplace Assistant 等の git revision/commit は
  published/retrieved されず → **NOT_REPRODUCIBLY_PINNED** (F07 対応)。
  framework version pin が dataset/taskset 全体を pin するかのように誤表示しない。
- Sample selection / config / execution substrate (Jobs/Sandboxes/local): 記事の
  per-framework 例の範囲でのみ主張し、substrate 固定の再現手順としては主張しない
  (missing inputs として明示: taskset revision, 選択基準, 実行 substrate の固定)。

## 4. Source→Claim table (P6b r15)

| 段落主張 | Primary source + pin | Class |
|---|---|---|
| roofline +30–120% (Qwen3.8-27B, 成功構成群) | AA article ("above the bandwidth-constraint roofline") | EVALUATOR_CLAIM |
| 14 configs 全投機 (MTP/DFlash/DSpark) + official/自作区別 | AA article ("Every config uses…", "developed our own…") | PRIMARY_FACT (方法) |
| HW/モデル/傾向値/価格注記 | AA article 各節 (5090 1,792GB/s 等) | EVALUATOR_CLAIM |
| local vs production (concurrent/SLO/MW) | AA article (single-user) + 同サイト AA-AgentPerf 記事 (2026-06-12) | PRIMARY_FACT (方法の差異) |
| WER/CER/RTFx/TTFA/SIM 定義・集計・TTFA protocol | HF blog (macro-average / batch size 1 / 50 prompts / 3 warm-up / median / H200) | PRIMARY_FACT (platform 定義) |
| リーダー名・16/92・proxy 免責 | HF blog (値引用なし) | PUBLISHER_CLAIM / BOUNDARY |
| scripts future (記事) vs repo 実態 (commits) | HF blog + GH API (repo/commit日時) | PRIMARY_FACT (時間分割の両側) |
| RL tags/arch/例・件数・境界 | HF blog claim-note (full-read) | PRIMARY_FACT / PUBLISHER_CLAIM |
| taskset revisions | published/retrieved なし | NOT_REPRODUCIBLY_PINNED |

## 5. NOT retrievable / NOT pinned (exact record)

- AA: 各構成の完全列挙・版ピン・repo commit SHA (存在消費のみ)。
- OpenTTS: WER 数値・Space app 内部・Listen 音声内容 (snapshot 名のみ)。
- RL-Hub: taskset git revisions・選択基準・substrate 固定 (上記)。
- 上記は UNVERIFIED / NOT_REPRODUCIBLY_PINNED のまま残し、捏造しない。

## 6. 日本語品質セルフレビュー

- 訳語: bandwidth-constraint roofline「帯域制約ルーフライン」(初出英語併記)、
  speculative decoding「投機的デコーディング」、warm-up 除外「ウォームアップ除外」、
  macro-average「マクロ平均」。
- 否定の明確化: 「対照群との差ではない」「backdate しない」を文頭否定で明示。
  dated negative (Oct 7 着地) は日付と commit を一体記述。
- 残課題: TTFA 数値・構成別表の日本語化は原文確認待ち。
