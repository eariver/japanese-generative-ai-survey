# TS-003 Drafting Terminology Map — Japanese reader-facing prose

Status: `EDITION_LOCAL / MANDATORY_PREFLIGHT / DRAFT_R1_BINDING`

Date: `2026-10-01`

Policy: `execution/drafting-language-policy-ja.md` (`TS-003_DRAFTING_LANGUAGE_POLICY_ACTIVE`)

Rule of precedence: established Japanese → established katakana → English where precision wins →
short natural explanation on first use. Never coin a kanji compound to avoid English.
`KEEP_ENGLISH_OR_KATAKANA` is a valid disposition and is used below wherever it wins.

First-use pattern: natural Japanese + term once (e.g. 接地（grounding）), then the shortest
unambiguous form. Do not repeat the English gloss in parentheses on every occurrence.

## 1. Load-bearing distinctions (never collapse; Human-mandated)

| English | Reader-facing form | Avoid | Note |
|---|---|---|---|
| grounding | 接地（grounding）→ 以後は接地 | 接地化、グラウンディングの漢語化 | 言語概念を位置・領域・座標へ結びつける操作を指す |
| alignment | アライメント | 整列化、整合化、接地との混用 | 画像全体とテキストの意味対応づけ。grounding とは別の契約 |
| perception | 知覚（perception）→ 以後は知覚 | 知覚化、認識との混用 | 見る・捉える側。reasoning と対置するときは英語併記を残す |
| reasoning | 推論 | 推論化、知覚との混用 | 考える側。タイトルの語と同じ |
| detection | 検出 | 検知への寄せ、recognition との混用 | 物の位置をボックスで求める操作 |
| recognition | 認識 | detection との混用 | 何であるかを定める操作 |
| segmentation | セグメンテーション | 分割への還元（文脈により分割可だが画素・領域の構造を指す語として区別） | detection とは別の密な構造化 |
| benchmark | ベンチマーク | 評価との混用 | 具体的な課題・データセット・手順の束を指す |
| evaluation | 評価 | ベンチマークとの混用 | 測る行為一般。benchmark はその具体物 |
| World Model | ワールドモデル | 世界模型、世界モデルへの漢語化 | 四極の一角としての呼称。predictive representation と区別 |
| predictive representation | 予測表現（predictive representation） | 予測的表象、予測符号化への寄せ | 生成せず予測する表現。ワールドモデルと区別 |
| capability | 能力 | 性能との混用（速度・効率は性能、できることは能力） | モデルができること |
| evidence | 根拠 | 証拠への寄せ（法的含みを避ける） | 主張を支える材料 |
| architecture | アーキテクチャ | 構造・機構への漢語化（模型の構成を指すとき） | データ構造など一般の構造は構造でよい |
| deployment | デプロイ | 配備化、展開化 | 実運用に載せること。配備も可だが全巻ではデプロイに統一 |

## 2. Core technical vocabulary

| English | Reader-facing form | Avoid |
|---|---|---|
| multimodal | マルチモーダル | 多様式、多模式 |
| VLM | 視覚言語モデル（VLM）→ 以後はVLM | 視覚言語模型 |
| Vision-Language-Action / VLA | Vision-Language-Action（VLA）→ 以後はVLA | 視覚言語行動モデル |
| Computer Use | Computer Use（コンピュータ操作）→ 以後はComputer Use | 計算機利用、電脳使用 |
| open-vocabulary | オープンボキャブラリー | 開放語彙、開語彙 |
| referring expression | 指示表現 | 参照表現への寄せ（参照は reference 用に残す） |
| phrase grounding | フレーズの接地 | 句接地 |
| REC / OVD / OVS | REC / OVD / OVS（初出のみ説明） | 漢語略称の新造 |
| zero-shot | ゼロショット | 無学習推論 |
| prompt / promptable | プロンプト / プロンプトで指示できる | プロンプト可能（名詞化の連鎖にしない） |
| instruction tuning | 指示チューニング | 命令調整 |
| self-supervised | 自己教師あり | 自己統制 |
| contrastive learning | 対照学習 | 対比化 |
| masked modeling / MAE | マスク再構成 / MAE | 仮面化 |
| distillation | 蒸留（知識蒸留） | 抽出化 |
| fine-tuning | ファインチューニング | 微調整の漢語化は可だが全巻ではファインチューニングに統一 |
| pretraining / post-training | 事前学習 / ポストトレーニング | 事後学習 |
| encoder / decoder / backbone | エンコーダ / デコーダ / バックボーン | 符号器・復号器・基幹網 |
| resampler / Q-Former / cross-attention | リサンプラ / Q-Former / cross-attention | 交差注意への漢語化 |
| frozen (encoder) | 凍結した〜 | 固定化の連鎖 |
| token / tokenizer | トークン / トークナイザ | 符号、字句化 |
| context (window) | コンテキスト（長さ） | 文脈長への寄せ（文脈は意味的文脈に残す） |
| KV cache / memory pressure | KVキャッシュ / メモリ負荷 | 鍵値緩衝 |
| resolution | 解像度 | 解像化 |
| box / mask / coordinate | ボックス / マスク / 座標 | 枠・覆面 |
| anchor / NMS / region proposal | アンカー / NMS / 領域提案 | 非極大抑制の毎回展開（初出のみ） |
| set prediction / dense prediction | 集合予測 / 密な予測 | 集合化 |
| panoptic / instance / semantic | パノプティック / インスタンス / セマンティック | 汎分割 |
| keypoint / pose | キーポイント / ポーズ | 姿勢推定は定着語として可 |
| depth estimation | 深度推定 | 深さ化 |
| calibration-free | キャリブレーション不要の〜 | 無較正化 |
| hallucination | ハルシネーション | 幻覚への寄せ（臨床含みを避ける） |
| CoT / scaffold / judge | CoT / scaffold（補助的手順） / 判定（judge） | 思考連鎖の漢語化、審査員 |
| contamination | 汚染（データ汚染） | 混入化 |
| ablation | アブレーション | 除去実験への寄せ |
| latency | 遅延 | 潜時 |
| streaming / online vs offline | ストリーミング / オンライン・オフライン | 実時間化 |
| timestamp / proactive response | タイムスタンプ / 能動応答 | 先回り化 |
| omni | オムニ | 全様式 |
| screenshot | スクリーンショット | 画面撮影化 |
| GUI element grounding | GUI要素の接地 | 図形界面要素接地化 |
| trajectory | 軌道 | 軌跡への寄せ（ロボット文脈では軌道に統一） |
| planner / policy | プランナ / ポリシー | 計画器・方策への漢語化 |
| embodiment / embodied | エンボディメント / 身体をもつ〜 | 具現化 |
| cross-embodiment | 異なる機体にまたがる〜（cross-embodiment） | 機体横断化 |
| latent dynamics | 潜在ダイナミクス | 潜在力学化 |
| simulator | シミュレータ | 模擬器 |
| action token | 行動トークン | 動作符号化 |
| open weights / repo | オープンウェイト / リポジトリ | 公開重み化 |
| vendor claim / independent result | ベンダー主張 / 独立した再現・評価 | 供給者説 |
| model card | モデルカード | 模型証 |
| OCR / layout / chart | OCR / レイアウト / 図表 | 光学文字認識の毎回展開 |
| supervision (signal) | 教師信号 | 監督化 |
| objective / interface contract | 目的関数 / 入出力の契約 | 契約化 |
| claim strength | 主張の強さ | 主張強度化 |
| provenance | 出所・由来 | 来歴化 |
| reliability | 信頼性 | —（定着語として可） |
| convergence (unified vs modular) | 収束（一本化か分業か） | 融合化 |
| lineage / predecessor / successor | 系譜 / 先行 / 後継 | 系統化 |
| capstone | 到達点の事例 | 集大成化 |
| operating point | 動作点 | 稼働点化 |
| trade-off | トレードオフ | 交換化 |
| training recipe | レシピ | 調製法化 |
| scaling | スケーリング | 規模化 |
| state management | 状態管理 | —（定着語として可） |
| temporal state | 時間的な状態（初出のみ説明） | 時間状態化の連鎖 |
| egocentric | エゴセントリック（一人称視点） | 自己中心化 |
| Document Intelligence | 文書理解（document understanding） | 文書知能化 |
| pointing (Molmo) | 指さし出力（pointing） | 点示化 |
| modality | モダリティ | 様式化 |

## 3. Sentence-level guards (all packages)

- 主語と動詞を具体的に書く。名詞の連鎖で因果を済ませない。
- 「〜における」「〜に対する」「〜を通じた」の連続を避け、短く切る。
- 数字・年・モデル名は原表記のまま（AlexNet、CLIP、Qwen3-VL など）。
- ベンダー・論文・プロジェクトの主張は帰属を明示する（〜と報告している、〜によれば）。
- 未解決（G01–G06、PARTIAL）は言い切らない。分からないものは分からないと書く。
- 内部用語（candidate、checkpoint、gate、SELECTED、PRIMARY など）は読者文に出さない。
- ベンチマーク名は原語のまま（MMMU、HallusionBench、OCRBench v2 など）。
- 比較は同一条件のものだけ。条件の違う数値を並べて優劣をつけない。

## 4. Package-specific notes

- P07A/P07B: アライメントと接地の語を混ぜない。P07A では接地を使わない。
- P09: モデル名の羅列にしない。解像度・融合・時刻の三つの問いごとに束ねる。
- P10: ベンチマーク名と診断内容を分ける（例：HallusionBench は制御ペアによる診断、という書き方）。
- P12: 要素の位置（接地）と課題の成否（タスク成功）は別の文で書く。
- P13: 機体の運動や制御則の中身に踏み込まない（Architecture の境界）。
- P14: 四極の呼称（歴史的定式 / 潜在ダイナミクス / 予測表現 / 生成的環境）を混ぜない。
- P15: ベンチマーク名の列挙にしない。契約ごとの統合の文にする。

Terminal map state: `TS-003_TERMINOLOGY_MAP_R1_FIXED`
