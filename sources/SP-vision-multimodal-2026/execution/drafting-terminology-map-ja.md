# TS-003 Drafting Terminology Map — Japanese reader-facing prose

Status: `EDITION_LOCAL / CUMULATIVE_TERMINOLOGY_AUTHORITY / DRAFT_R9_BINDING`

Date: `2026-10-02 JST`

Issue: `SP-vision-multimodal-2026`

Policy:

`sources/SP-vision-multimodal-2026/execution/drafting-language-policy-ja.md`

Review authorities incorporated:

- `sources/SP-vision-multimodal-2026/execution/sol-draft-review-r1.md`
- `sources/SP-vision-multimodal-2026/execution/sol-draft-review-r2.md`

This cumulative authority supersedes earlier map revisions for Draft r9 and later TS-003 reader-surface work.

## 0. Authority and maintenance rule

This file is the cumulative terminology authority for TS-003.

It has two jobs:

1. define the preferred reader-facing form of load-bearing technical terms;
2. preserve every known over-translation / over-domestication / metaphorical-substitution failure discovered during actual TS-003 drafting and Sol review so that the same failure does not reappear under a new synonym.

Rule of precedence:

1. established Japanese technical usage;
2. established katakana usage;
3. the English technical term when it preserves precision better;
4. a short natural-Japanese explanation on first use.

`KEEP_ENGLISH_OR_KATAKANA` is valid and is preferable to an invented translation.

Do not coin a kanji compound, literary metaphor, school-personification, or ordinary-life analogy merely to avoid English/katakana.

### 0.1 Cumulative-update rule

When Sol or Human review discovers a new terminology failure, add it to this file before the next drafting execution. Do not leave known failures only in review prose.

The map therefore functions as a cumulative regression-prevention authority, not a one-time preflight list.

r3 cumulative update log (2026-10-02, during r3 Pass C, before prose repair):
`§3.3 added (encoder-目, pipeline-管, 多作物, 汎用手, fusion variants); §3.2 fusion rows refined; terminal state unchanged`.

### 0.2 Context rule — this is not a blind banned-word list

An Avoid form is blocking only when it substitutes for the identified technical concept or creates the same reader-surface defect.

Ordinary literal Japanese may still be valid.

Examples:

- `符号化` is valid for actual encoding, but `符号を公開した` is not a valid rendering of “released the code”.
- `切り分ける` is valid for “distinguish two cases”, but must not replace the technical task `segmentation`.
- `仕事` is valid for literal work/task, but not as repeated rhetorical filler such as “〜するのがこの節の仕事だ”.
- `方策` is established Japanese in reinforcement learning and may be used for RL policy; do not mechanically replace it with `ポリシー` when the source/domain uses the established Japanese term.

Every QA scan must therefore classify hits semantically rather than replacing strings globally.

First-use pattern: natural Japanese + term once when useful (for example `接地（grounding）`), then the shortest unambiguous established form. Do not repeat English glosses mechanically.

---

## 1. Load-bearing distinctions — never collapse

| English / concept | Preferred reader-facing form | Avoid / regression forms | Note |
|---|---|---|---|
| grounding | 接地（grounding）→ 以後は接地 | 接地化、grounding と alignment の混用 | 言語概念を位置・領域・座標へ結びつける操作 |
| alignment | アライメント | 整列化、整合化、接地との混用 | 画像全体とテキストの意味対応づけ。grounding と別契約 |
| perception | 知覚（perception）→ 以後は知覚 | 知覚化、recognition との混用 | reasoning と対置するときは英語併記可 |
| reasoning | 推論 | 推論化、知覚との混用 | 考える側 |
| detection | 検出 | 検知への寄せ、recognition との混用 | 位置をボックス等で求める操作 |
| recognition | 認識 | detection との混用 | 何であるかを定める操作 |
| segmentation | セグメンテーション | 技術用語としての切り分け、塗り分け、単なる分割への還元 | genericな「区別する」の切り分けは可。画素・領域課題は technical term を保持 |
| semantic segmentation | セマンティックセグメンテーション | セマンティックな塗り分け | semantic / instance の区別を保つ |
| instance segmentation | インスタンスセグメンテーション | インスタンスの切り分け | detection と混同しない |
| benchmark | ベンチマーク | 評価との混用 | 具体的課題・データ・手順の束 |
| evaluation | 評価 | ベンチマークとの混用 | 測る行為一般 |
| World Model | ワールドモデル | 世界模型、世界モデルへの過剰漢語化 | predictive representation と区別 |
| predictive representation | 予測表現（predictive representation） | 予測的表象、ワールドモデルとの混用 | 生成せず表現を予測する系 |
| capability | 能力 | 性能との混用 | できること。速度/効率は性能 |
| evidence / support | 根拠 / 裏付け | 証し、証拠への不要な寄せ | 主張を支える材料 |
| architecture | アーキテクチャ / 文脈上定着した「設計」 | genericな構え、模型の構成を指す不自然な漢語化 | データ構造等の通常の「構造」は可 |
| deployment | デプロイ / 実運用（文脈で使い分け） | 配備化、展開化、technical termとしての不統一な配備 | volume-levelで意味を固定する |
| source role / evaluator role | ベンダー測定 / モデル論文著者測定 / ベンチマーク論文著者による第三者測定 / 独立した第三者再現 | bare 著者を独立性の代理にする表現 | “author-reported” は自動的に independent ではない |

---

## 2. Core technical vocabulary

| English / concept | Preferred reader-facing form | Avoid / regression forms |
|---|---|---|
| model | モデル | 模型 |
| neural network | ニューラルネットワーク | 技術用語としての網 |
| CNN | CNN / 畳み込みニューラルネットワーク | 畳み込み網、基幹網 |
| multimodal | マルチモーダル | 多様式、多模式 |
| modality | モダリティ | 技術用語としての様式 |
| VLM | 視覚言語モデル（VLM）→ 以後はVLM | 視覚言語模型 |
| Vision-Language-Action / VLA | Vision-Language-Action（VLA）→ 以後はVLA | 視覚言語行動模型 |
| Computer Use | Computer Use（コンピュータ操作）→ 以後はComputer Use | 計算機利用、電脳使用 |
| open-vocabulary | オープンボキャブラリー | 開放語彙、開語彙、開かれた語彙、開いた語彙 |
| referring expression | 指示表現 | 参照表現への機械的寄せ |
| phrase grounding | フレーズの接地 | 句接地 |
| REC / OVD / OVS | REC / OVD / OVS（初出のみ説明） | 漢語略称の新造 |
| zero-shot | ゼロショット | 無学習推論 |
| prompt / promptable | プロンプト / プロンプトで指示できる | プロンプト可能 |
| instruction tuning | 指示チューニング | 命令調整 |
| self-supervised | 自己教師あり | 自己統制 |
| contrastive learning | 対照学習 | 対比化 |
| masked modeling / MAE | マスクモデリング / マスク再構成 / MAE（文脈に応じる） | 仮面化、当て戻し |
| teacher model | 教師モデル | 教員、教員モデル、教員役 |
| student model | 生徒モデル | bare 生徒、領域の生徒 |
| teacher signal / supervision signal | 教師信号 | 教員の信号、監督化 |
| distillation | 蒸留 / 知識蒸留 | 抽出化、学校比喩による説明 |
| fine-tuning | ファインチューニング | 全巻での無秩序な微調整との揺れ |
| pretraining | 事前学習 | — |
| post-training | ポストトレーニング | 事後学習 |
| encoder / decoder / backbone | エンコーダ / デコーダ / バックボーン | 符号器、復号器、architecture/component senseのbare 復号、基幹網、technical backbone senseの背骨 |
| resampler / Q-Former / cross-attention | リサンプラ / Q-Former / cross-attention | 交差注意への機械的漢語化 |
| attention / window attention / attention map | アテンション / ウィンドウアテンション / アテンションマップ | mechanism名としての注意、窓注意 |
| query / query vector | クエリ / クエリベクトル | Q-Former/Transformer文脈の問い合わせ、問い合わせベクトル |
| shortcut / shortcut connection | ショートカット接続 | ResNet機構名としての近道 |
| one-stage / two-stage detector | one-stage / two-stage（初出のみ「1段型/2段型」併記可） | detector architecture名としての一段・二段 |
| feature map | 特徴マップ | feature mapを表す特徴量地図、特徴地図 |
| dual encoder / two-tower | デュアルエンコーダ / two-tower（初出のみ説明） | 二塔、塔をarchitecture名として使うこと |
| Mixture-of-Experts / MoE | Mixture-of-Experts（MoE）→ 以後はMoE | 混合専門家、専門家混合を固有architecture名の代用にすること |
| dense model / dense architecture | denseモデル / dense構成（初出のみ説明） | model typeを表す稠密 |
| model checkpoint | チェックポイント | モデル検査点、検査点 |
| trainable parameters | 学習可能パラメータ / trainable parameters（初出のみ併記可） | 学習変数 |
| model/configuration variant | バリアント / 派生モデル（文脈に応じる） | model/configuration senseの変種 |
| category / base category / novel category | カテゴリ / ベースカテゴリ / novelカテゴリ（初出のみ説明可） | ML/CV taxonomyを表す範疇 |
| cold start | コールドスタート | 冷間始動 |
| masked label / masked token | マスクされたラベル / マスクされたトークン | mechanism説明としての覆ったラベル・覆ったトークン |
| speech / ASR | 音声 / 音声認識（ASR） | speech modalityのprimary technical labelとしての話し言葉 |
| architecture component / module | 構成要素 / モジュール / 具体的なcomponent名 | architecture senseの部品 |
| frozen (encoder/model) | 凍結した〜 | 固定化の名詞連鎖 |
| token / tokenizer | トークン / トークナイザ | 符号、字句化 |
| source code / software code | コード / ソースコード / 推論コード / 学習コード（文脈に応じる） | 符号 |
| encoding | 符号化 / エンコーディング（文脈に応じる） | source code と混同 | 
| repository | リポジトリ | 保管庫への過剰訳 |
| context window / context length | コンテキスト / コンテキスト長 | 文脈長への機械的寄せ |
| KV cache / memory pressure | KVキャッシュ / メモリ負荷 | 鍵値緩衝 |
| resolution | 解像度 | 解像化 |
| box / mask / coordinate | ボックス / マスク / 座標 | technical boxとしての箱・枠、覆面をtechnical termの代用にすること |
| anchor / NMS / region proposal | アンカー / NMS / 領域提案 | 非極大抑制の毎回展開 |
| set prediction / dense prediction | 集合予測 / 密な予測 | 集合化 |
| panoptic / instance / semantic | パノプティック / インスタンス / セマンティック | 汎分割 |
| keypoint / pose | キーポイント / ポーズ / 姿勢推定（文脈に応じる） | — |
| depth estimation | 深度推定 / 文中では「深さを推定」も可 | 深さ化 |
| calibration-free | キャリブレーション不要の〜 | 較正なし、無較正化をtechnical labelとして使うこと |
| hallucination | ハルシネーション | technical termとしての幻覚 |
| CoT / scaffold / judge | CoT / scaffold（補助的手順） / 判定（judge） | 思考連鎖の機械的漢語化、審査員 |
| contamination | 汚染 / データ汚染 | 混入化 |
| ablation | アブレーション | 除去実験への機械的寄せ |
| latency | 遅延 | 潜時 |
| streaming / online / offline | ストリーミング / オンライン / オフライン | 実時間化 |
| timestamp / proactive response | タイムスタンプ / 能動応答 | 先回り化 |
| omni | オムニ | 全様式 |
| screenshot | スクリーンショット | 画面撮影化 |
| GUI element grounding | GUI要素の接地 | 図形界面要素接地化 |
| trajectory | 軌道 | ロボット文脈での無秩序な軌跡との揺れ |
| planner | プランナ / 計画器（分野で定着している方を選び全巻で揃える） | 文脈を無視した新造語 |
| RL policy | 方策 / policy（必要なら初出併記） | 一律に日常語「方針」へ落とすこと |
| embodiment / embodied | エンボディメント / 身体をもつ〜 | 具現化 |
| cross-embodiment | 異なる機体にまたがる〜（cross-embodiment） | 機体横断化 |
| latent dynamics | 潜在ダイナミクス | 潜在力学化 |
| simulator | シミュレータ | 模擬器 |
| action token | 行動トークン | 動作符号化 |
| open weights | オープンウェイト | 開かれた重み、公開重み化 |
| vendor claim / independent result | ベンダー主張 / 独立した再現・評価 | 供給者説 |
| model card | モデルカード | 模型証 |
| OCR / layout / chart | OCR / レイアウト / 図表 | 光学文字認識の毎回展開 |
| objective | 目的関数 | 目的化 |
| interface | インターフェース / 界面（分野で定着した用法のみ） | 受け口 |
| input side / input path | 入力側 / 入力経路 / 入力インターフェース | 受け口 |
| interface contract | 入出力の契約 | 契約化 |
| claim strength | 主張の強さ | 主張強度化 |
| provenance | 出所 / 由来 | 来歴化 |
| reliability | 信頼性 | — |
| convergence (unified vs modular) | 収束（一本化か分業か） | 融合化 |
| lineage / predecessor / successor | 系譜 / 先行 / 後継 | 系統化 |
| capstone | 到達点の事例 | 集大成化 |
| operating point | 動作点 | 稼働点化 |
| trade-off | トレードオフ | 交換化 |
| training recipe | 学習レシピ / レシピ | 処方、調製法化 |
| scaling | スケーリング | scaling概念を表す規模化・大規模化 |
| methodological discipline / constraint | 方法上の規律 / 制約 / 前提（意味に応じる） | 躾 |
| evidence/evaluation category | 根拠の区分 / 評価区分 / source role等を具体的に書く | 棚 |
| criterion / metric / yardstick | 評価基準 / 指標 / 測定条件（意味に応じる） | technical termとしての物差し |
| preserve / carry forward | 維持する / 引き継ぐ / 保つ | genericな運ぶ |
| state management | 状態管理 | — |
| temporal state | 時間的な状態（初出のみ説明） | 時間状態化の連鎖 |
| egocentric | エゴセントリック（一人称視点） / 一人称視点 | 自己中心化 |
| Document Intelligence | 文書理解（document understanding） | 文書知能化 |
| pointing (Molmo) | 指さし出力（pointing） | 点示化 |

---

## 3. Cumulative known-failure registry

This registry records observed TS-003 failures. It is a regression list, not merely examples.

### 3.1 r1 failures — observed and prohibited as technical substitutions

| Observed form | Intended concept / function | Preferred repair | First formalized |
|---|---|---|---|
| 網 | neural network / CNN | ニューラルネットワーク / CNN | Sol Draft Review r1 |
| 処方 | training recipe / method | 学習レシピ / レシピ / 方法 | Sol Draft Review r1 |
| 運ぶ | preserve/carry a claim, limitation, representation | 引き継ぐ / 維持する / 保つ / 具体的動詞 | Sol Draft Review r1 |
| 構え | architecture / design / method / stance | アーキテクチャ / 設計 / 方法 / 前提を意味に応じて明示 | Sol Draft Review r1 |
| 証し | evidence / support | 根拠 / 裏付け | Sol Draft Review r1 |
| 躾 | methodology / discipline | 方法上の規律 / 制約 / 前提 | Sol Draft Review r1 |
| 棚 | evidence category / classification | 根拠の区分 / 評価区分 / source roleを明示 | Sol Draft Review r1 |
| 務め / 仕事 | rhetorical paragraph/section purpose | 「本節では〜を扱う」等の直接表現。literal task/workは可 | Sol Draft Review r1 |
| 凱歌 | rhetorical superiority claim | 具体的な評価結果・位置づけを書く | Sol Draft Review r1 |
| 束ねの妙 / 束ね | rhetorical recipe praise | 組み合わせ / 構成 / 学習レシピを具体化 | Sol Draft Review r1 |
| 土俵 | evaluation context / protocol | 評価条件 / 評価設定 / プロトコル | r1 repair scan |
| 物差し | metric / criterion | 指標 / 評価基準 / 測定条件 | r1 repair scan |
| 顔つき | characteristic / behavior | 特性 / 振る舞い | r1 repair scan |
| 段取り | procedure / pipeline / sequence | 手順 / 処理順序 | r1 repair scan |
| 宿題 | open issue / future work | 課題 / 未解決点 / 今後の課題 | r1 repair scan |
| 持ち場 | role / scope | 役割 / 範囲 / 担当する内容 | r1 repair scan |
| 見取り図 | overview / map / structure | 全体像 / 構成 / 整理 | r1 repair scan |
| 模型 | model | モデル | pre-r1 terminology repair |

### 3.2 r2 failures — observed after r1 repair

| Observed form | Intended concept / function | Preferred repair | First formalized |
|---|---|---|---|
| 多様式 / 多模式 | multimodal | マルチモーダル | Sol Draft Review r2 |
| 教員 / 教員モデル / 教員役 | teacher model | 教師モデル / 教師信号 | Sol Draft Review r2 |
| bare 生徒 / 領域の生徒 | student model | 生徒モデル | Sol Draft Review r2 |
| 事後学習 | post-training | ポストトレーニング | Sol Draft Review r2 |
| 幻覚 | hallucination | ハルシネーション | Sol Draft Review r2 |
| segmentationを表す切り分け / 塗り分け | segmentation | セグメンテーション / semantic/instance segmentation | Sol Draft Review r2 |
| software/source codeを表す符号 | code | コード / ソースコード / 推論コード / 学習コード | Sol Draft Review r2 |
| 受け口 | interface / input side | インターフェース / 入力側 / 入力経路 | Sol Draft Review r2 |
| 当て戻し | masked reconstruction | マスク再構成 / 再構成 | Sol Draft Review r2 |
| 袋詰め / 袋にまとめて照らす | global image-text alignment / bag-like loss of composition | 画像全体のアライメント / compositional limitationを直接説明 | Sol Draft Review r2 |
| 受け皿 | successor mechanism / role | 後継 / 対応する方法 / 役割を直接説明 | Sol Draft Review r2 |
| 契約の家 | benchmark/task definition | 評価条件を定めるベンチマーク / データセットを直接明示 | Sol Draft Review r2 |
| 語彙の足し | vocabulary expansion / supervision | 語彙拡張 / 教師信号の追加等を直接明示 | Sol Draft Review r2 |
| 遅い渡し | late fusion / transfer | late fusion / 後段融合 / 文脈上正確なtechnical term | Sol Draft Review r2 |
| 固い混ぜ / 固く混ぜる | tight/deep fusion | deep fusion / 密な融合 / 文脈上正確なtechnical term | Sol Draft Review r2; Sol Draft Review r8 refinement |
| 規模の回し | scaling / large-scale training | スケーリング / 大規模学習 | Sol Draft Review r2 |
| レア側の埋め | rare-category coverage/performance | レアカテゴリのカバレッジ / 性能等を直接説明 | Sol Draft Review r2 |
| 幻のふるい | hallucination screening/diagnosis | ハルシネーション診断 / 投票型評価を直接説明 | Sol Draft Review r2 |
| editorialな錨 | organizing anchor / reference point | 起点 / 基準事例 / 方法上の参照点を直接説明 | Sol Draft Review r2 |
| 投票の素描 | polling-style hallucination evaluation | 投票型評価の範囲を直接説明 | Sol Draft Review r2 |
| 二言語の輪切り | bilingual evaluation slice | 英語・中国語の評価範囲を直接説明 | Sol Draft Review r2 |
| 配りの極 | deployment/distribution endpoint | デプロイ形態 / 提供形態 / 端末実行の位置づけ | Sol Draft Review r2 |
| 値打ち（editorial praise） | significance | 意義 / 位置づけ / 技術的効果を具体化 | r2 Sol inspection |

### 3.3 r3 failures — discovered during r3 Pass C full-text review

| Observed form | Intended concept / function | Preferred repair | First formalized |
|---|---|---|---|
| エンコーダの意味での目（視覚言語モデルの目、SigLIP系の目、目を凍らせる、他の目を借りる） | vision encoder / backbone | 視覚エンコーダ / エンコーダを直接書く | r3 Pass C |
| データ管 / 較正の配管 | data / calibration pipeline | データパイプライン / パイプライン | r3 Pass C |
| 多作物 | multi-crop | マルチクロップ | r3 Pass C |
| 汎用手 | general-purpose model | 汎用モデル | r3 Pass C |
| 早い融合 / 遅い融合 / 固い融合（§3.2の遅い渡し・固い混ぜと同系） | early / late / tight fusion | 早期融合 / 後段融合 / 密な融合 | r3 Pass C (§3.2 refinement) |

Ordinary non-encoder 目 (見る目、目の前、項目等), ordinary 管轄・管理, and 枠組み/枠数 senses remain allowed per the context rule (§0.2).

### 3.4 Sol r3 residual failures — discovered by independent post-r3 review

These items were still present after the Worker r3 PASS_WITH_NOTES and are now part of the cumulative regression authority.

| Observed form | Intended concept / function | Preferred repair | First formalized |
|---|---|---|---|
| technical segmentation rendered as 分割（例: 分割の枝、汎用分割、指示分割、パノプティック分割、固定ラベル分割器） | segmentation family | セグメンテーション / オープンボキャブラリーセグメンテーション / パノプティックセグメンテーション等 | Sol Draft Review r3 |
| bare 測り used as a noun for metric/evaluation contract（例: 三つ目の測り、レアの測り、測りは契約ごと） | metric / evaluation protocol | 指標 / 評価指標 / 評価方法 / 評価条件 / 測定方法 | Sol Draft Review r3 |
| 決めなし / 〜の決め（評価・抽出文脈） | evaluation/extraction rule or protocol | 評価条件 / 抽出規則 / 手順 / 定義 | Sol Draft Review r3 |
| OVD評価の家 / 第二の家 / model-family senseの家系 | benchmark home / model family / lineage | 評価基準・評価対象を直接書く / モデル系列 / モデルファミリー / 系譜 | Sol Draft Review r3 |
| data augmentation senseの水増し | data augmentation | データ拡張 | Sol Draft Review r3 |
| scaffold senseの足場 | scaffold / auxiliary procedure | scaffold（補助的手順） / 補助的手順 | Sol Draft Review r3 |
| foundation/base/backbone senseの土台（例: 拡散土台、識別土台、学習の土台の名） | foundation model / base model / backbone / base representation | 基盤モデル / 基盤 / バックボーン / 基盤表現を文脈に応じて明示 | Sol Draft Review r3 |
| 載せ方 / 組み方 / 式と移し をtechnical axis名として使う | tokenization/formulation / architecture / objective / distillation or transfer | 実際の技術軸（トークン化、アーキテクチャ、目的関数、蒸留、転移等）を直接書く | Sol Draft Review r3 |
| 呼びの到達 / 結びの仕組み | global alignment / grounding transition | アライメント / 接地 / 位置・領域への対応づけを直接書く | Sol Draft Review r3 |
| 教師モデルの写しの産物 | teacher-model / pseudo-label dependence | 教師モデルの出力に依存 / 疑似ラベルに依存 / 教師モデル由来を具体化 | Sol Draft Review r3 |
| streaming senseの流れの契約 / 流れのオムニ | streaming input/processing/deployment | ストリーミング入力 / ストリーミング処理 / ストリーミング対応 | Sol Draft Review r3 |
| release/availability senseの配り方 / 配りの範囲 | availability / release / deployment scope | 提供形態 / 提供範囲 / 公開形態 / デプロイ形態 | Sol Draft Review r3 |
| 軸の勘定 | separate evaluation axes / trade-off accounting | 別々の評価軸として扱う / 評価軸を分ける | Sol Draft Review r3 |
| 一つの芸 | single-task specialization | 単一タスク / 特定能力 / 特定タスクへの特化 | Sol Draft Review r3 |
| additional-sample senseの追加試料 | additional training/evaluation samples | 追加の学習データ / 追加サンプル | Sol Draft Review r3 |
| few-shot senseのフューショット | few-shot | few-shot / 少数例学習（first useで説明可） | Sol Draft Review r3 |
| neural-unit senseの素子 | neuron / unit | ニューロン / ユニット | Sol Draft Review r3 |
| openness mixture senseのまだら | mixed openness / mixed dependency | 開放性が混在する / 依存関係が混在する | Sol Draft Review r3 |

Context exceptions:

- ordinary `分割` remains valid for dataset/train-test split, partitioning, or generic division;
- ordinary verbs `測る` / natural `測り方` may remain when they literally describe measurement and do not replace a metric/protocol name;
- ordinary `水増し` may remain only when it literally means numerical inflation, not data augmentation;
- ordinary `土台になる` may remain as nontechnical prose only when it does not name a foundation/base/backbone concept;
- literal family/house meanings are unaffected; model-family/benchmark-role contexts must use technical wording.

### 3.5 Sol r4 residual failures — discovered by independent post-r4 review

These expressions survived r4 despite the cumulative map and therefore become explicit regression cases for r5.

| Observed form | Intended concept / function | Preferred repair | First formalized |
|---|---|---|---|
| self-supervised senseの自己教師（例: headline「Transformerと自己教師の土台」） | self-supervised learning | 自己教師あり学習 / 自己教師あり | Sol Draft Review r4 |
| technical foundation senseのheadline土台（例: 「Transformerと自己教師の土台」） | foundation / base representation | 基盤 / 基盤表現 / 基盤モデルを文脈に応じて明示 | Sol Draft Review r4 |
| 言葉側だけを締める調整 | text-side-only tuning / adjustment | テキスト側のみを調整する / テキストエンコーダのみを調整する等、実際の対象を明示 | Sol Draft Review r4 |
| 一対の判定に還す | pairwise independent sigmoid classification / objective | 各画像・テキスト対を独立に判定する等、目的関数の動作を直接説明 | Sol Draft Review r4 |
| 引用の結び / 典拠の結び | citation/source linkage | 引用対応 / 一次資料との対応 / 典拠との対応 | Sol Draft Review r4 |
| 手順の借り | reuse/adoption of training recipe | 学習手順を採用する / 学習レシピを利用する | Sol Draft Review r4 |
| 仕組みの消費 | evidence consumption / supported mechanism coverage | 根拠が抄録レベルに限られる / 機構説明の根拠範囲を直接書く | Sol Draft Review r4 |
| 文と絵の組を大量に当て / 4億ペアの当て | contrastive image-text training | 大量の画像・テキスト対で対照学習する / 画像・テキスト対による学習 | Sol Draft Review r4 |
| 固定クラス分類を表す表引き | closed-set / fixed-class classification | 固定クラス分類 / 事前定義クラスによる分類 | Sol Draft Review r4 |
| dataset collectionを表す30超の束 | 30+ datasets/tasks | 30以上のデータセット / 30以上の評価課題 | Sol Draft Review r4 |
| ODinWを野外の補い | in-the-wild / diverse-domain supplementary evaluation | ODinWによる実世界・多様ドメイン評価を直接説明 | Sol Draft Review r4 |
| sequence representationを表す列に変える契約 | token/sequence representation | トークン列へ変換する / 系列表現へ変換する | Sol Draft Review r4 |
| evaluation separationを表す別の列に置く | separate evaluation axis/condition | 別の評価軸として扱う / 別条件として扱う | Sol Draft Review r4 |
| technical transitionを表す「〜へ渡す役割」「次の節への渡し」 | transition / applicability / handoff | 適用範囲を広げる / 次節では〜を扱う等、技術的関係を直接書く | Sol Draft Review r4 |

Context exceptions:

- ordinary literal `締める`, `当てる`, `束`, `列`, `渡す` are not banned;
- `引用を結ぶ` can be ordinary Japanese, but source-provenance discussion must name citation/source correspondence precisely;
- ordinary `土台になる` may remain under §3.4 context exception when it is clearly nontechnical and does not name a foundation/base/backbone concept.

### 3.6 Sol r5 residual failures — direct map miss and P09 modality wording

These residuals were discovered by independent Sol review after r5.

| Observed form | Intended concept / function | Preferred repair | First formalized |
|---|---|---|---|
| self-supervised senseの自己教師（例: 「音全般の自己教師」「音の自己教師」） | self-supervised learning | 自己教師あり学習 / 自己教師あり | Sol Draft Review r5 |
| model-family senseの家族（例: 「1Bから78Bの家族」） | model family / model series | モデル群 / モデルファミリー / モデル系列 | Sol Draft Review r5 |
| modality/input-pipeline senseの入口（例: 「話し言葉の入口」「音全般の…入口」「音の入口を組み合わせる」） | speech/audio input path / modality encoder role | 音声入力 / 音声処理 / 音声エンコーダ / 音響表現学習など実際の役割を直接書く | Sol Draft Review r5 |
| deployment senseの末端（例: 「末端からクラウドまで」） | edge-to-cloud deployment range | エッジデバイスからクラウドまで / エッジからクラウドまで | Sol Draft Review r5 |
| architecture senseの部品（例: 「三つの部品の積み重ね」） | architecture components | 構成要素 / モジュール / アーキテクチャ構成 | Sol Draft Review r5 |

Context exceptions:

- literal family/household `家族` is unaffected;
- ordinary physical `入口` and literal `部品` are unaffected;
- `自己教師あり` is the approved established term; substring scans must not misclassify it as bare `自己教師`.

### 3.7 Sol reader/publication candidate r1 residual failures — preferred-form conformance gap

The first exact PDF materialization exposed a QA defect: prior rounds searched known bad strings aggressively but did not enforce the preferred-form side of Section 2 consistently across headlines, decks, body blocks and boundaries. These are therefore cumulative blocking regression cases for r7.

| Observed form | Intended concept / function | Preferred repair | First formalized |
|---|---|---|---|
| technical bounding box senseの箱（P02/P03/P07B等、headline含む） | bounding box / box | ボックス / 初出で必要ならバウンディングボックス（ボックス） | Sol Reader/Publication Review r1 |
| 開かれた語彙 / 開いた語彙 | open-vocabulary | オープンボキャブラリー | Sol Reader/Publication Review r1 |
| decoder senseの汎用復号 / 復号設計 | decoder / decoder design | 汎用デコーダ / デコーダ設計 | Sol Reader/Publication Review r1 |
| calibration-free senseの較正なし | calibration-free | キャリブレーション不要 | Sol Reader/Publication Review r1 |
| scaling senseの大規模化 | scaling | スケーリング | Sol Reader/Publication Review r1 |
| open-weights senseの開かれた重み | open weights | オープンウェイト | Sol Reader/Publication Review r1 |
| architecture senseの部品（例: P08 headline「凍結した部品をつなぐ橋」、部品の選び方、凍結した部品） | component / module | 構成要素 / モジュール / 画像エンコーダ等の具体名 | Sol Reader/Publication Review r1 |
| technical transition/interfaceのprimary labelとしての橋 / 橋渡し | connection / transition / interface role | 接続方式 / 統合 / 適用拡張など実際の技術的役割を直接書く | Sol Reader/Publication Review r1 |
| model-lineageのprimary organizerとしての一本の鎖 / 鎖のなか | lineage / staged progression | 系譜 / 連続する変化 / 段階的な変化 | Sol Reader/Publication Review r1 |
| Q-Former/Transformerの問い合わせ / 問い合わせベクトル | query / query vector | クエリ / クエリベクトル | Sol Reader/Publication Review r1 |
| mechanism senseの窓注意 / 注意マップ | window attention / attention map | ウィンドウアテンション / アテンションマップ | Sol Reader/Publication Review r1 |
| ResNet shortcut senseの近道 | shortcut connection | ショートカット接続 | Sol Reader/Publication Review r1 |
| detector architecture senseの一段 / 二段 | one-stage / two-stage detector | one-stage / two-stage（初出のみ説明可） | Sol Reader/Publication Review r1 |
| feature map senseの特徴量地図 | feature map | 特徴マップ | Sol Reader/Publication Review r1 |
| dual-encoder senseの二塔 / 塔 | dual encoder / two-tower | デュアルエンコーダ / two-tower | Sol Reader/Publication Review r1 |
| MoE senseの混合専門家 | Mixture-of-Experts / MoE | Mixture-of-Experts（MoE） / MoE | Sol Reader/Publication Review r1 |
| dense-model senseの稠密 | dense model | denseモデル / dense構成 | Sol Reader/Publication Review r1 |
| cold-start senseの冷間始動 | cold start | コールドスタート | Sol Reader/Publication Review r1 |
| model-checkpoint senseの検査点 | model checkpoint | チェックポイント | Sol Reader/Publication Review r1 |
| trainable-parameter senseの学習変数 | trainable parameters | 学習可能パラメータ | Sol Reader/Publication Review r1 |
| model/configuration senseの変種 | model/configuration variant | バリアント / 派生モデル | Sol Reader/Publication Review r1 |
| CV/ML category senseの範疇 | category | カテゴリ / ベースカテゴリ / novelカテゴリ等 | Sol Reader/Publication Review r1 |
| masked-label senseの覆った離散ラベル | masked discrete labels | マスクされた離散ラベル | Sol Reader/Publication Review r1 |
| speech/ASRのprimary labelとしての話し言葉 | speech / ASR | 音声 / 音声認識（ASR） | Sol Reader/Publication Review r1 |

Context exceptions:

- literal physical boxes, household/family objects, ordinary bridges and literal chains are unaffected;
- ordinary Japanese `問い合わせ` for a user request remains valid; only model-query terminology is normalized;
- ordinary `注意` meaning caution remains valid; only attention mechanisms/maps use アテンション;
- ordinary `近道` meaning shortcut/heuristic remains valid; only ResNet-style shortcut connections are normalized;
- learning phases described as first/second stage may use 第一段階/第二段階; detector architecture labels use one-stage/two-stage;
- ordinary `変種` outside model/configuration terminology is unaffected;
- ordinary spoken-language explanation may use descriptive Japanese, but when the concept is the speech modality/ASR task, use 音声/音声認識;
- Architecture-defined P14 `四つの極` remains an explicit approved exception.

QA consequence:

**Preferred form is normative, not merely advisory.** Pass A must semantically classify every load-bearing concept in Section 2. A surface does not conform merely because the Avoid column has zero literal hits. A nonpreferred synonym, calque, domesticating paraphrase, or metaphor that replaces a preferred technical term is blocking unless the QA report records a specific context exception.

Headlines and decks receive no relaxed terminology standard.

### 3.8 Sol Draft Review r7 residual failures — bidirectional semantic binding

Draft r7 substantially improved terminology, but independent Sol review found a different class of failure: a preferred token can itself be wrong when it is applied to the wrong underlying concept, and a stale synthesis can escape a package-focused audit.

| Observed form | Intended concept / function | Preferred repair | First formalized |
|---|---|---|---|
| P13の比喩的な container sense を blind repair した「別のボックスに閉じ込めず」「別のボックスを置かず」 | separation between subsystems / intermediate module boundary, not bounding box | 「別系統に分離せず」「視覚入力から行動出力までを一つのモデルで扱う」等、実際のarchitecture relationを直接書く | Sol Draft Review r7 |
| lineage summary の「鎖を通して見ると」 | lineage / staged progression | 「この系譜を通して見ると」「段階的な変化を見ると」 | Sol Draft Review r7 |
| P14以外のprimary technical organizerとしての「密な極」「もう一極」「融合の両極」「OpenVLA…極」「マルチモーダルの極」 | dense prediction family / alternate specialization / fusion strategies / open-weight example / native-multimodal example | 実際の技術分類・方式・到達点の事例を直接書く | Sol Draft Review r7 |
| P09 boundaryでspeech/ASR scopeを表す「話し言葉の範囲」 | speech / ASR scope | 「音声認識の範囲」「音声入力の範囲」 | Sol Draft Review r7 |
| synthesisの「個別学習済み部品の橋渡し」「個別部品の組み立て」 | connecting separately pretrained components / modular composition | 「個別に事前学習した構成要素の接続」「モジュール構成」等、component/connectionを直接書く | Sol Draft Review r7 |

Context exceptions:

- P14のArchitecture-defined「四つの極 / 四極」は引き続き明示的な例外;
- 「極端」「極めて」など通常の副詞・形容表現は対象外;
- bounding boxとしての「ボックス」は正しい。禁止するのは、非-box概念を「ボックス」で代用すること;
- coreference chain等のtechnical termとして正当な「共参照鎖」は対象外;
- ordinary spoken-language prose may use descriptive Japanese, but a scope boundary for Whisper/ASR should use 音声/音声認識.

QA consequence:

Preferred-form conformance is **bidirectional**.

1. concept -> preferred form: a technical concept must use the preferred term;
2. preferred form -> concept: a preferred token must not be inserted where the underlying concept is different.

For example, every technical bounding box must be 「ボックス」, but not every metaphorical 「箱」 should become 「ボックス」.

The same semantic pass must cover the **canonical profile synthesis result**, not only package prose. A synthesis that still contains stale component/bridge metaphors blocks PASS even if all 16 package Results pass.

### 3.9 Sol Draft Review r8 residual failures — final micro-cleanup

Independent Sol review found four small residuals after the r8 bidirectional audit.

| Observed form | Intended concept / function | Preferred repair | First formalized |
|---|---|---|---|
| 「拡散の背骨としての来歴」 | diffusion backbone | 「拡散モデルのバックボーンとしての来歴」等、backboneを標準用語で書く | Sol Draft Review r8 |
| 「特徴増強と言語誘導クエリ選択とcross-modalityデコーダの三段で固く混ぜる」 | multi-stage tight/deep fusion | 三つの機構で密に融合する / 三段階の密な融合を直接説明 | Sol Draft Review r8 |
| 「構成を足さず、学習手順で検出に渡す」 | adapting a pretrained vision-language model to detection without added modules | 追加モジュールなしで検出へファインチューニングする / 学習手順のみで検出へ適応する等、実際のtechnical relationを直接書く | Sol Draft Review r8 |
| reader-facing punctuation defect「で、、文と画像…」 | punctuation / copy defect | 「で、文と画像…」 | Sol Draft Review r8 |

Context exceptions:

- anatomical/literal 「背骨」 is unaffected; only model/backbone terminology is normalized;
- ordinary 「混ぜる」 is allowed when literally combining data/conditions, but fusion architecture/mechanism must use 融合;
- ordinary 「渡す」 is allowed; technical adaptation/transition must name the actual adaptation, fine-tuning, or transfer;
- punctuation defects are not terminology concepts, but are recorded here because they were introduced by a terminology-only repair and must be regression-checked before publication regeneration.

### 3.10 Regression principle

Do not “fix” one known form by inventing another metaphor.

Examples of invalid repair patterns:

- `網` → another everyday object metaphor for network;
- `教員` → another human-role metaphor for teacher model;
- `符号` → another uncommon Japanese synonym for code;
- `袋詰め` → another container metaphor for global alignment;
- `物差し` → another object metaphor for metric.

The repair target is the underlying technical concept, not merely the character string.

---

## 4. Reader-surface anti-metaphor rule

Technical survey prose may use an occasional ordinary metaphor only when it genuinely clarifies and the technical concept is still stated explicitly.

Do not use metaphor as the primary name of a mechanism, evaluator, source role, interface, benchmark contract, limitation, or architecture.

Particularly avoid recurring editorial connective tissue such as:

- `〜の仕事 / 〜の務め`;
- `〜の錨`;
- `〜の受け皿`;
- `〜の家`;
- `〜の極` when the axis is not explicitly defined;
- `〜を運ぶ`;
- `〜を棚に置く`;
- `〜の物差し`.

Prefer direct statements:

- what changed;
- what is input/output;
- what is trained/frozen;
- what metric is used;
- who measured it;
- what limitation remains;
- which evaluation protocol the number belongs to.

---

## 5. Sentence-level guards — all packages

- 主語と動詞を具体的に書く。名詞の連鎖で因果を済ませない。
- 「〜における」「〜に対する」「〜を通じた」の連続を避け、短く切る。
- 数字・年・モデル名は原表記のまま（AlexNet、CLIP、Qwen3-VLなど）。
- ベンダー・論文・プロジェクトの主張は帰属を明示する。
- 未解決（G01–G06、PARTIAL）は言い切らない。分からないものは分からないと書く。
- 内部用語（candidate、checkpoint、gate、SELECTED、PRIMARY等）は通常の読者文に出さない。
- ベンチマーク名は原語のまま。
- 比較は同一条件のものだけ。条件の異なる数値を並べて優劣をつけない。
- page allocationは文字数quotaではない。重複・言い換えで埋めない。
- 一つの悪い語を消すために新しい独自語を作らない。

---

## 6. Mandatory terminology QA protocol

Draft r3以降のlanguage QAは、単純なregex countだけでPASSを出してはならない。

### Pass A — preferred-form semantic conformance + avoid scan

For every row in Sections 1 and 2:

- preferred formをconcept単位で確認する;
- preferred tokenの各出現が実際にそのconceptを指すか逆向きにも確認する（bidirectional binding）;
- Avoid / regression formを検索する;
- Avoid欄に文字列がなくても、preferred technical termを別の独自訳・意訳・比喩で置換していないか確認する;
- headline / deck / PARAGRAPH / BULLET / TABLE / CLAIM_BOUNDARY / canonical profile synthesis resultを対象にする;
- headline/deckにも本文と同じterminology authorityを適用する;
- preferred form以外を維持する場合は、QA reportにexact sentenceとcontext exceptionの根拠を記録する。

### Pass B — known-failure regression scan

Section 3の全failureについて検索し、各hitを次のいずれかに分類する:

- `TECHNICAL_SUBSTITUTION_BLOCKING`;
- `ORDINARY_JAPANESE_ALLOWED`;
- `SOURCE_QUOTE_OR_FIXED_NAME`;
- `NOT_APPLICABLE`.

`ORDINARY_JAPANESE_ALLOWED` を付ける場合は、QA reportに文脈と理由を残す。

### Pass C — semantic manual read

全16 package + synthesis + CLAIM_BOUNDARYを人間向け技術文として通読し、リストにない新しい独自訳・比喩がないか確認する。

新しいfailureを見つけた場合:

1. Draftを修正;
2. 本Terminology Mapのknown-failure registryへ追記;
3. 再scan;
4. その後にのみPASS/PASS_WITH_NOTESを出す。

Core validator PASSはlanguage PASSではない。

---

## 7. Package-specific notes

- P01: neural network / CNN / segmentationを一般語へ置き換えない。AlexNet/ResNetの技術説明を直接書く。
- P03: segmentation / semantic segmentation / instance segmentationを`切り分け/塗り分け`で代用しない。
- P06: teacher/student/distillationを学校比喩にしない。masked reconstructionを`当て戻し`と呼ばない。
- P07A: alignmentとgroundingを混ぜない。P07Aではgroundingを先取りしない。global alignmentの限界を`袋詰め`で説明しない。
- P07B: teacher/studentを標準用語で書く。`契約の家`, `語彙の足し`, `遅い渡し`, `固い混ぜ`, `規模の回し`, `レア側の埋め`を使わない。
- P08/P09/P10/P11: repository/software codeを`符号`と書かない。actual encodingの`符号化`とは区別する。
- P09: `マルチモーダル`, `ポストトレーニング`, `デプロイ`をmapどおり使う。解像度・融合・時刻の三問で整理する。
- P10: benchmark名とdiagnostic roleを分ける。`幻のふるい`等の比喩で役割を表さない。
- P12: GUI要素の接地とタスク成功を分ける。
- P13: 機体の運動や制御則の中身に踏み込まない。
- P14: 四極の分類自体はArchitectureに従うが、`錨`などのeditorial metaphorで接続しない。
- P15: benchmark catalogueにしない。`幻覚`, `投票の素描`, `二言語の輪切り`, `配りの極`を使わない。source/evaluator roleを明示する。

---

Terminal map state:

`TS-003_TERMINOLOGY_MAP_CUMULATIVE_R9_BINDING`

`KNOWN_FAILURES_THROUGH_SOL_DRAFT_REVIEW_R8_INCORPORATED`

`SEMANTIC_QA_REQUIRED`

`NO_BLIND_GLOBAL_REPLACEMENT`
