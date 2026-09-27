# Terminology decision ledger — TS-002 Issue #543 (final broad normalization)

Canonical: `terminology-decision-ledger.json` (276 rows, generated; this MD is a synced view).
Scope: reader-facing terminology only. Blind global replace prohibited; semantic-risk terms verified by primary/Evidence read-back.

## Summary (recomputed from JSON actual row set, 276 rows)
- REPLACE rows: 262
- RETAIN rows: 14
- ESCALATE rows: 0
- BROAD_SCAN: 45
- ISSUE_SEED: 45
- SOL_FINAL_RESIDUAL_R3: 36
- SOL_MAP_R2: 52
- SOL_R10_R7_INDEPENDENT_FULLSCAN: 49
- SOL_R10_R8_CANDIDATE_RESOLUTION: 12
- SOL_R10_R9_FINAL_INDEPENDENT_AUDIT: 7
- SOL_R9_R4_RESOLUTION: 23
- SOL_R9_R5_RESOLUTION: 6
- SOL_R9_R6_RESOLUTION: 1
- Unresolved terms: none pending — r10 12 candidates resolved by Sol r8; r9 7 residuals resolved by Sol r9 map (post-r9 closure scan: 0 unresolved).

## Decisions
### TS543-S01 [ISSUE_SEED] — 端末間統合 → End-to-End（エンドツーエンド）統合/End-to-End [REPLACE]
- canonical: End-to-End | meaning: VITS系joint学習14件
- rationale: §6表題と整合; endpoint別義なし
- occurrences: L439,L441,L453,L454,L456,L458,L470,L476,L497,L504,L550
- sections: L435 \section{音声・声の系譜：波形からEnd-to-End、ニューラルコーデック言語モデル、全二重へ}\sectionkicker{SPEECH}\la; L453 \subsection{並列化とニューラルボコーダと端末間統合：遅さと注意破綻への応答}; L475 \subsection{何を何で表すか：言語・意味・音響・符号・波形の分担}; L496 \subsection{ゼロショット話者複製とニューラルコーデック言語モデル：未知話者への拡張}
- evidence: btd051, btd052, btd053, btd057, btd058, btd061
- before: 14 / residual: 0

### TS543-S02 [ISSUE_SEED] — 量保存流れ → normalizing flow（正規化フロー） [REPLACE]
- canonical: normalizing flow | meaning: VITS prior flow 3件
- rationale: 一次資料read-back(arXiv 2106.06103 abstract: variational inference augmented with normalizing flows); Evidence内volume-preserving記述は誤読と確定
- occurrences: L454,L470,L489
- sections: L453 \subsection{並列化とニューラルボコーダと端末間統合：遅さと注意破綻への応答}; L475 \subsection{何を何で表すか：言語・意味・音響・符号・波形の分担}
- evidence: btd054, btd055, btd056, btd057
- before: 3 / residual: 0

### TS543-S03 [ISSUE_SEED] — 集合同期 → バッチ正規化（Batch Normalization） [REPLACE]
- canonical: Batch Normalization | meaning: DCGAN batch norm 2件
- rationale: 設計ガイドライン文脈
- occurrences: L190
- sections: L189 \subsection{敵対的生成の系譜：暗黙分布から様式分離へ}
- evidence: btd013, btd014
- before: 2 / residual: 0

### TS543-S04 [ISSUE_SEED] — 日程 → 線形ノイズスケジュール/誘導スケジュール/スケジュール [REPLACE]
- canonical: (noise/guidance) schedule | meaning: schedule 6件
- rationale: 暦日程なし
- occurrences: L166,L213,L223,L239,L260
- sections: L160 \section{生成パラダイムと目的関数：自己回帰・敵対・拡散・フロー}; L212 \subsection{雑音除去の転換：拡散と短縮抽出}; L220 \subsection{連続時間への統一と潜在への移行}; L238 \subsection{本節の読解上の境界}
- evidence: btd013, btd019, btd023, btd022, btd030, btd014
- before: 6 / residual: 0

### TS543-S05 [ISSUE_SEED] — 祖先抽出 → ancestral sampling（祖先サンプリング）/祖先サンプリング [REPLACE]
- canonical: ancestral sampling | meaning: ancestral sampling 4件
- rationale: L114初出にcanonical English
- occurrences: L114,L172,L215,L218
- sections: L113 \subsection{連続潜在から離散符号へ：推論の償却化と量子化}; L171 \subsection{六軸分離の読み方：表現・骨格・目的・経路・抽出・短縮}; L212 \subsection{雑音除去の転換：拡散と短縮抽出}; L217 \subsection{条件誘導の分岐：分類器誘導と分類器なし誘導}
- evidence: btd001, btd017, btd023, btd026, btd013, btd014
- before: 4 / residual: 0

### TS543-S06 [ISSUE_SEED] — 祖先サンプリング → 祖先サンプリング [RETAIN]
- canonical: ancestral sampling | meaning: 既正規形1件(L569)
- rationale: 既にcanonical; after=5は retained 1 + S05正規化4の合流
- occurrences: L569
- sections: L568 \subsection{階層的自己回帰と意味・音響段階化：分単位楽曲への第一歩}
- evidence: btd063, btd065
- before: 1 / residual: 5

### TS543-S07 [ISSUE_SEED] — 得点整合 → score matching（スコアマッチング） [REPLACE]
- canonical: score matching | meaning: denoising score matching 3件
- rationale: btd019/btd021
- occurrences: L213,L221
- sections: L212 \subsection{雑音除去の転換：拡散と短縮抽出}; L220 \subsection{連続時間への統一と潜在への移行}
- evidence: btd019, btd030, btd021
- before: 3 / residual: 0

### TS543-S08 [ISSUE_SEED] — 得点蒸留 → score distillation（スコア蒸留）/スコア蒸留 [REPLACE]
- canonical: score distillation | meaning: NFSD score蒸留2件
- rationale: btd081
- occurrences: L926
- sections: L925 \subsection{写実性を別系統の損失で補う敵対的蒸留}
- evidence: btd081
- before: 2 / residual: 0

### TS543-S09 [ISSUE_SEED] — 得点導出 → スコア導出 [REPLACE]
- canonical: score derivation | meaning: SiT速度-スコア2件
- rationale: btd026
- occurrences: L228
- sections: L227 \subsection{Transformer denoiserと流れ・整合性モデルへの分岐}
- evidence: btd025, btd026
- before: 2 / residual: 0

### TS543-S10 [ISSUE_SEED] — 識別得点 → Inception Score（IS） [REPLACE]
- canonical: Inception Score | meaning: IS 4件
- rationale: CIFAR/ADM/CFG数値文脈
- occurrences: L215,L258,L260
- sections: L212 \subsection{雑音除去の転換：拡散と短縮抽出}; L257 \subsection{推論時誘導への転換：分類器なし誘導と文誘導拡散}
- evidence: btd030, btd020, btd019, btd032, btd033
- before: 4 / residual: 0

### TS543-S11 [ISSUE_SEED] — 分類得点 → Inception Score（IS） [REPLACE]
- canonical: Inception Score(statistical) | meaning: IS 2件+曖昧1件
- rationale: L218/L239はADM数値で確定; L158(btd003)はIS/精度曖昧のためESCALATE(残存1)
- occurrences: L158,L218,L239
- sections: L157 \subsection{本節の読解上の境界}; L217 \subsection{条件誘導の分岐：分類器誘導と分類器なし誘導}; L238 \subsection{本節の読解上の境界}
- evidence: btd006, btd008, btd001, btd004, btd002, btd007
- before: 3 / residual: 1

### TS543-S12 [ISSUE_SEED] — 知覚経路 → Perceptual Path Length（PPL／知覚経路長） [REPLACE]
- canonical: Perceptual Path Length | meaning: PPL 2件
- rationale: StyleGAN文脈; 残存1はgloss内
- occurrences: L192,L239
- sections: L189 \subsection{敵対的生成の系譜：暗黙分布から様式分離へ}; L238 \subsection{本節の読解上の境界}
- evidence: btd015, btd016, btd013, btd014, btd019, btd020
- before: 2 / residual: 1

### TS543-S13 [ISSUE_SEED] — 分布距離 → FID/FVD/FAD [REPLACE]
- canonical: FID/FVD/FAD | meaning: named 27件+generic 6件
- rationale: 数値改善主張はnamed; 方法論総括6件はRETAIN(別掲S13b)
- occurrences: L121,L150,L158,L166,L192,L213,L215,L218,L223,L225,L230,L233,L239,L255…
- sections: L118 \subsection{階層と知覚：高解像度への二つの道}; L147 \subsection{意味と音響の分離、映像の時空間短縮}; L157 \subsection{本節の読解上の境界}; L160 \section{生成パラダイムと目的関数：自己回帰・敵対・拡散・フロー}
- evidence: btd004, btd003, btd009, btd010, btd012, btd006
- before: 33 / residual: 6

### TS543-S13b [ISSUE_SEED] — 分布距離(generic) → 分布距離 [RETAIN]
- canonical: distribution distance | meaning: 方法論総括6件
- rationale: 数値主張でない対応整理
- occurrences: 
- sections: 
- before: 0 / residual: 0

### TS543-S14 [ISSUE_SEED] — 平均意見値 → Mean Opinion Score（MOS） [REPLACE]
- canonical: Mean Opinion Score | meaning: MOS 8件
- rationale: 自然さ軸; VITS abstractもMOS
- occurrences: L441,L447,L454,L497,L589
- sections: L435 \section{音声・声の系譜：波形からEnd-to-End、ニューラルコーデック言語モデル、全二重へ}\sectionkicker{SPEECH}\la; L446 \subsection{波形自己回帰と系列変換：素片結合なしの出発点}; L453 \subsection{並列化とニューラルボコーダと端末間統合：遅さと注意破綻への応答}; L496 \subsection{ゼロショット話者複製とニューラルコーデック言語モデル：未知話者への拡張}
- evidence: btd051, btd052, btd053, btd054, btd055, btd056
- before: 8 / residual: 0

### TS543-S15 [ISSUE_SEED] — 類似度意見値 → 話者類似度主観評価（SMOS相当） [REPLACE]
- canonical: speaker similarity MOS | meaning: 話者性2件
- rationale: YourTTS話者性
- occurrences: L441,L497
- sections: L435 \section{音声・声の系譜：波形からEnd-to-End、ニューラルコーデック言語モデル、全二重へ}\sectionkicker{SPEECH}\la; L496 \subsection{ゼロショット話者複製とニューラルコーデック言語モデル：未知話者への拡張}
- evidence: btd051, btd052, btd053, btd054, btd055, btd056
- before: 2 / residual: 0

### TS543-S16 [ISSUE_SEED] — 類似意見 → 話者類似度主観評価（SMOS相当） [REPLACE]
- canonical: speaker similarity MOS | meaning: SMOS表記ゆれ1件
- rationale: L533数値がL497と同一実体
- occurrences: L533
- sections: L520 \subsection{Seed-TTS（多用途・高忠実音声生成）・翻訳・全二重対話：実環境と遅延の両立}
- evidence: btd057
- before: 1 / residual: 0

### TS543-S17 [ISSUE_SEED] — 可知度 → intelligibility（明瞭度）/明瞭度 [REPLACE]
- canonical: intelligibility | meaning: 明瞭度18件
- rationale: 音声三軸の可知度
- occurrences: L378,L439,L441,L447,L451,L466,L468,L488,L490,L497,L501,L513,L525,L533…
- sections: L373 \subsection{潜在局所合成：前景と背景の分離}; L435 \section{音声・声の系譜：波形からEnd-to-End、ニューラルコーデック言語モデル、全二重へ}\sectionkicker{SPEECH}\la; L446 \subsection{波形自己回帰と系列変換：素片結合なしの出発点}; L453 \subsection{並列化とニューラルボコーダと端末間統合：遅さと注意破綻への応答}
- evidence: btd046, btd047, btd051, btd052, btd053, btd057
- before: 18 / residual: 0

### TS543-S18 [ISSUE_SEED] — 比較意見値 → 比較MOS [REPLACE]
- canonical: comparative MOS | meaning: 比較MOS 2件
- rationale: CMOS頭字語は原典未確認のためassertせず
- occurrences: L521,L544
- sections: L520 \subsection{Seed-TTS（多用途・高忠実音声生成）・翻訳・全二重対話：実環境と遅延の両立}
- evidence: btd061, btd062, btd134
- before: 2 / residual: 0

### TS543-S19 [ISSUE_SEED] — 意見値(bare) → MOS [REPLACE]
- canonical: Mean Opinion Score | meaning: MOS 12件
- rationale: 自然さ軸のbare MOS
- occurrences: L441,L447,L454,L456,L466,L467,L469,L470,L497,L521,L533,L544,L589,L591…
- sections: L435 \section{音声・声の系譜：波形からEnd-to-End、ニューラルコーデック言語モデル、全二重へ}\sectionkicker{SPEECH}\la; L446 \subsection{波形自己回帰と系列変換：素片結合なしの出発点}; L453 \subsection{並列化とニューラルボコーダと端末間統合：遅さと注意破綻への応答}; L496 \subsection{ゼロショット話者複製とニューラルコーデック言語モデル：未知話者への拡張}
- evidence: btd051, btd052, btd053, btd054, btd055, btd056
- before: 24 / residual: 0

### TS543-S20 [ISSUE_SEED] — 真値 → ground truth [REPLACE]
- canonical: ground truth | meaning: GT比較10件
- rationale: 9件自然音声GT+1件実データGT(L713修飾)
- occurrences: L454,L467,L469,L470,L497,L589,L591,L606,L660,L713
- sections: L453 \subsection{並列化とニューラルボコーダと端末間統合：遅さと注意破綻への応答}; L496 \subsection{ゼロショット話者複製とニューラルコーデック言語モデル：未知話者への拡張}; L588 \subsection{波形拡散と潜在拡散：局所忠実度と一般音響化の二系統}; L657 \subsection{評価の四分割：音質・整合・構造・人間選好}
- evidence: btd054, btd055, btd056, btd052, btd053, btd057
- before: 10 / residual: 0

### TS543-S21 [ISSUE_SEED] — 呼び水 → プライミング [REPLACE]
- canonical: priming | meaning: Jukebox priming 4件
- rationale: prompt senseなし
- occurrences: L569,L603,L630,L643
- sections: L568 \subsection{階層的自己回帰と意味・音響段階化：分単位楽曲への第一歩}; L588 \subsection{波形拡散と潜在拡散：局所忠実度と一般音響化の二系統}; L627 \subsection{生成・継続・編集・制御の分離：課題設定の区別}
- evidence: btd063, btd065
- before: 4 / residual: 0

### TS543-S22 [ISSUE_SEED] — 立体化 → ステレオ微調整/ステレオ化 [REPLACE]
- canonical: stereo | meaning: stereo 2件
- rationale: 3D用法なし
- occurrences: L580,L584
- sections: L579 \subsection{一段階可制御符号音楽：多段階層の低速への応答}
- evidence: btd066, btd067, btd069
- before: 2 / residual: 0

### TS543-S23 [ISSUE_SEED] — 流れ補完 → Flow Matching/インフィリング系(節別) [REPLACE]
- canonical: Flow Matching/infilling | meaning: flow/infilling 10件
- rationale: 目的/課題の節別分割; 節表題含む
- occurrences: L439,L476,L501,L508,L509,L511,L513,L536,L550,L553
- sections: L435 \section{音声・声の系譜：波形からEnd-to-End、ニューラルコーデック言語モデル、全二重へ}\sectionkicker{SPEECH}\la; L475 \subsection{何を何で表すか：言語・意味・音響・符号・波形の分担}; L496 \subsection{ゼロショット話者複製とニューラルコーデック言語モデル：未知話者への拡張}; L508 \subsection{流れ補完と実時間化：非自己回帰と前後文脈の統一}
- evidence: btd051, btd052, btd053, btd057, btd058, btd061
- before: 10 / residual: 0

### TS543-S24 [ISSUE_SEED] — 管線 → パイプライン [REPLACE]
- canonical: pipeline | meaning: pipeline 6件
- rationale: FluxPipeline gloss含め全件
- occurrences: L932,L939,L942,L946
- sections: L931 \subsection{機材の天井を押さえる独立計測}
- evidence: btd137, btd078, btd079, btd080, btd081, btd082
- before: 6 / residual: 0

### TS543-S25 [ISSUE_SEED] — 零初期化 → ゼロ初期化(zero convolution gloss 1件) [REPLACE]
- canonical: zero initialization | meaning: zero-init 9件
- rationale: DiT/ControlNet/LoRA
- occurrences: L228,L249,L283,L288,L290,L333
- sections: L227 \subsection{Transformer denoiserと流れ・整合性モデルへの分岐}; L241 \section{条件づけとアライメント}; L280 \subsection{音響の言語整合と空間制御の適合}; L285 \subsection{四区分の使い分け：条件と誘導と適合と参照}
- evidence: btd025, btd026, btd031, btd011, btd032, btd033
- before: 9 / residual: 0

### TS543-S26 [ISSUE_SEED] — 零終端SNR → zero-terminal SNR（ゼロ終端SNR） [REPLACE]
- canonical: zero-terminal SNR | meaning: ZT-SNR 3件
- rationale: 蒸留条件
- occurrences: L926
- sections: L925 \subsection{写実性を別系統の損失で補う敵対的蒸留}
- evidence: btd081
- before: 3 / residual: 0

### TS543-S27 [ISSUE_SEED] — 写像網 → マッピングネットワーク（mapping network） [REPLACE]
- canonical: mapping network | meaning: StyleGAN mapping 2件
- rationale: named component
- occurrences: L192
- sections: L189 \subsection{敵対的生成の系譜：暗黙分布から様式分離へ}
- evidence: btd015, btd016
- before: 2 / residual: 0

### TS543-S28 [ISSUE_SEED] — 合成網 → 合成ネットワーク（synthesis network） [REPLACE]
- canonical: synthesis network | meaning: StyleGAN synthesis 2件
- rationale: named component
- occurrences: L192
- sections: L189 \subsection{敵対的生成の系譜：暗黙分布から様式分離へ}
- evidence: btd015, btd016
- before: 2 / residual: 0

### TS543-S29 [ISSUE_SEED] — 復元網 → ポストネット系 [REPLACE]
- canonical: decoder post-net | meaning: Tacotron2 post-net 8件
- rationale: CBHG後段処理網と区別
- occurrences: L441,L447,L449,L467,L476,L487
- sections: L435 \section{音声・声の系譜：波形からEnd-to-End、ニューラルコーデック言語モデル、全二重へ}\sectionkicker{SPEECH}\la; L446 \subsection{波形自己回帰と系列変換：素片結合なしの出発点}; L453 \subsection{並列化とニューラルボコーダと端末間統合：遅さと注意破綻への応答}; L475 \subsection{何を何で表すか：言語・意味・音響・符号・波形の分担}
- evidence: btd051, btd052, btd053, btd054, btd055, btd056
- before: 8 / residual: 0

### TS543-S30 [ISSUE_SEED] — 後段処理網 → ポストプロセシングネットワーク [REPLACE]
- canonical: post-processing net | meaning: Tacotron CBHG 2件
- rationale: 復元網と区別
- occurrences: L447,L449
- sections: L446 \subsection{波形自己回帰と系列変換：素片結合なしの出発点}
- evidence: btd051, btd052, btd053
- before: 2 / residual: 0

### TS543-S31 [ISSUE_SEED] — 空間制御網 → ControlNet（空間制御ネットワーク） [REPLACE]
- canonical: ControlNet | meaning: named ControlNet 7件
- rationale: 固定U-Net+複写+zero-conv定義
- occurrences: L249,L270,L283,L286,L290,L343
- sections: L241 \section{条件づけとアライメント}; L257 \subsection{推論時誘導への転換：分類器なし誘導と文誘導拡散}; L280 \subsection{音響の言語整合と空間制御の適合}; L285 \subsection{四区分の使い分け：条件と誘導と適合と参照}
- evidence: btd031, btd011, btd032, btd033, btd034, btd035
- before: 7 / residual: 0

### TS543-S32 [ISSUE_SEED] — 音楽制御網 → 音楽制御ネットワーク [REPLACE]
- canonical: Music ControlNet-type | meaning: music adapter 3件
- rationale: ControlNet-like
- occurrences: L306,L340,L343
- sections: L298 \section{制御と参照：空間・参照・主体性の保存}; L337 \subsection{時間信号の分離制御：映像の動きと音楽の変化}; L342 \subsection{適合器の系譜：凍結本体に触れず足す}
- evidence: btd037, btd041, btd038, btd039, btd040, btd042
- before: 3 / residual: 0

### TS543-S33 [ISSUE_SEED] — 基底路 → 128ベースチャンネル（base channels） [REPLACE]
- canonical: base channels | meaning: 128ch 1件
- rationale: 百二十八→128は値同一
- occurrences: L213
- sections: L212 \subsection{雑音除去の転換：拡散と短縮抽出}
- evidence: btd019, btd030
- before: 1 / residual: 0

### TS543-S34 [ISSUE_SEED] — 残差組立て → 残差ブロック（residual blocks） [REPLACE]
- canonical: residual blocks | meaning: ADM残差ブロック1件
- rationale: 適応正規化対
- occurrences: L213
- sections: L212 \subsection{雑音除去の転換：拡散と短縮抽出}
- evidence: btd019, btd030
- before: 1 / residual: 0

### TS543-S35 [ISSUE_SEED] — 整流化線形 → ReLU/LeakyReLU（リーキーReLU） [REPLACE]
- canonical: ReLU/LeakyReLU | meaning: DCGAN活性化2件
- rationale: 生成器/識別器で区別
- occurrences: L190
- sections: L189 \subsection{敵対的生成の系譜：暗黙分布から様式分離へ}
- evidence: btd013, btd014
- before: 2 / residual: 0

### TS543-S36 [ISSUE_SEED] — 中央処理装置 → CPU [REPLACE]
- canonical: CPU | meaning: HiFi-GAN軽量版1件
- rationale: GPU対比
- occurrences: L454
- sections: L453 \subsection{並列化とニューラルボコーダと端末間統合：遅さと注意破綻への応答}
- evidence: btd054, btd055, btd056
- before: 1 / residual: 0

### TS543-S37 [ISSUE_SEED] — 多巡回 → マルチターン（multi-turn） [REPLACE]
- canonical: multi-turn | meaning: 対話multi-turn 4件
- rationale: Moshi btd134
- occurrences: L525,L547,L553
- sections: L520 \subsection{Seed-TTS（多用途・高忠実音声生成）・翻訳・全二重対話：実環境と遅延の両立}; L552 \subsection*{読解上の境界}
- evidence: btd134, btd061, btd062, btd059, btd051, btd057
- before: 4 / residual: 0

### TS543-S38 [ISSUE_SEED] — 区切評価 → ターン区切り評価 [REPLACE]
- canonical: turn-segmentation-dependent evaluation | meaning:  multi-turn評価依存2件
- rationale: btd134 PARTIALのため措辞は候補; 意味は確定
- occurrences: L525,L553
- sections: L520 \subsection{Seed-TTS（多用途・高忠実音声生成）・翻訳・全二重対話：実環境と遅延の両立}; L552 \subsection*{読解上の境界}
- evidence: btd134, btd061, btd062, btd051, btd057, btd058
- before: 2 / residual: 0

### TS543-S39a [ISSUE_SEED] — 得点(score-side) → score [REPLACE]
- canonical: score | meaning: 生成score 5件
- rationale: SDE文脈
- occurrences: L166,L221,L239
- sections: L160 \section{生成パラダイムと目的関数：自己回帰・敵対・拡散・フロー}; L220 \subsection{連続時間への統一と潜在への移行}; L238 \subsection{本節の読解上の境界}
- evidence: btd013, btd019, btd023, btd022, btd021, btd014
- before: 5 / residual: 0

### TS543-S39b [ISSUE_SEED] — 得点(general) → 得点 [RETAIN]
- canonical: score/value | meaning: 普通名詞16件
- rationale: 指標総称・方法論・X境界
- occurrences: L33,L145,L783,L867,L889,L968,L1093,L1128,L1132,L1143,L1149
- sections: L1092 \subsection{音楽：制作手順としてのworkflow記録}; L1122 \section{受容とcounter-signal：現場の27件の記録}; L1142 \subsection{境界と未決laneの保持}; L142 \subsection{音の残差量子化：低速度と遅延の両立}
- evidence: btd006, btd007, btd008, btd077, btd124, btd131
- before: 17 / residual: 17

### TS543-S39c [ISSUE_SEED] — 自然さ得点(vendor) → Naturalness MOS（自然さMOS） [REPLACE] (Sol r3 C001 resolved)
- canonical: MOS? | meaning: ベンダー自然さ2件
- rationale: Sol r3 C001 (r2 S-005 btd110 scope retained); vendor boundary retained
- occurrences: L1090,L1108
- sections: L1089 \subsection{音声・対話：実時間利用と版バインドの機能集合}; L1103 \subsection{横断の読み方：capstoneを大きく見せない}
- evidence: btd107, btd108, btd109, btd110, btd111, btd114
- before: 2 / residual: 2

### TS543-S40a [ISSUE_SEED] — 抽出(sampling) → サンプリング [REPLACE]
- canonical: sampling | meaning: sampling 29件
- rationale: 暗黙的1件含む; 節表題含む
- occurrences: L108,L114,L121,L158,L168,L171,L172,L184,L192,L197,L207,L212,L215,L218…
- sections: L100 \section{表現と圧縮：生成可能にする短縮の歴史}; L113 \subsection{連続潜在から離散符号へ：推論の償却化と量子化}; L118 \subsection{階層と知覚：高解像度への二つの道}; L157 \subsection{本節の読解上の境界}
- evidence: btd006, btd008, btd009, btd010, btd001, btd004
- before: 42 / residual: 9

### TS543-S40b [ISSUE_SEED] — 抽出(info-extraction) → 抽出 [RETAIN]
- canonical: extraction | meaning: 情報抽出8件
- rationale: 特徴/拍/計測の抽出
- occurrences: L340,L350,L617,L619,L655,L664,L678
- sections: L337 \subsection{時間信号の分離制御：映像の動きと音楽の変化}; L347 \subsection{保存と編集への橋渡し：制御忠実度と標本品質の分離}; L612 \subsection{時間条件・楽理制御と人間選好検証：開放重みと評価境界}; L650 \subsection{持続の延長と構造の維持：時間の二軸}
- evidence: btd043, btd039, btd038, btd040, btd042, btd069
- before: 8 / residual: 8

### TS543-S40c [ISSUE_SEED] — 全帯域抽出 → Balanced data sampling（均衡データサンプリング）+btd008 [REPLACE] (Sol r2 CIT-001/R-002 resolved)
- canonical: sampling? | meaning: btd007曖昧1件
- rationale: 評価sampling/特徴抽出の区別に本文要確認
- occurrences: L158
- sections: L157 \subsection{本節の読解上の境界}
- evidence: btd006, btd008, btd001, btd004, btd002, btd007
- before: 1 / residual: 1

### TS543-B01 [BROAD_SCAN] — 覆い → マスク [REPLACE]
- canonical: mask | meaning: マスク13件
- rationale: 意味覆い/覆い外し/prior/対画像/区間/潜在内外/VLM判定の全件mask
- occurrences: L158,L306,L310,L340,L632,L804,L819
- sections: L157 \subsection{本節の読解上の境界}; L298 \section{制御と参照：空間・参照・主体性の保存}; L309 \subsection{配置の前史と軽量適合：洗い流さない工夫}; L337 \subsection{時間信号の分離制御：映像の動きと音楽の変化}
- evidence: btd006, btd008, btd001, btd004, btd002, btd007
- before: 13 / residual: 0

### TS543-B02 [BROAD_SCAN] — 整列 → アライメント [REPLACE]
- canonical: alignment | meaning: アライメント32件
- rationale: 教師/単調/標識付き/注意/CLIP/分割/橋渡し/対比の全件alignment; §3表題と整合
- occurrences: L39,L454,L456,L458,L468,L470,L476,L487,L488,L489,L509,L511,L518,L549…
- sections: L1028 \subsection{話し言葉と文章の往復を一つの復号器に畳む}; L1049 \subsection{構造不変のデータ側工夫と合成拡散の対比}; L38 \subsection*{本巻の限界の要約}; L453 \subsection{並列化とニューラルボコーダと端末間統合：遅さと注意破綻への応答}
- evidence: btd022, btd059, btd083, btd089, btd098, btd106
- before: 32 / residual: 0

### TS543-B03 [BROAD_SCAN] — 適合器 → アダプター [REPLACE]
- canonical: adapter | meaning: アダプター30件
- rationale: 軽量/参照/prompt適合器+系譜節; seed ControlNet系と整合
- occurrences: L247,L270,L278,L283,L286,L288,L290,L306,L312,L328,L330,L340,L342,L343…
- sections: L241 \section{条件づけとアライメント}; L257 \subsection{推論時誘導への転換：分類器なし誘導と文誘導拡散}; L275 \subsection{段階専門家への分岐：共有 denoiser の分割}; L280 \subsection{音響の言語整合と空間制御の適合}
- evidence: btd011, btd032, btd034, btd036, btd031, btd033
- before: 30 / residual: 0

### TS543-B04 [BROAD_SCAN] — 符号帳 → コードブック [REPLACE]
- canonical: codebook | meaning: コードブック26件
- rationale: VQ codebook/崩壊/損失; glossary含む
- occurrences: L63,L106,L110,L116,L119,L121,L130,L132,L140,L145,L153,L158,L197,L571…
- sections: L100 \section{表現と圧縮：生成可能にする短縮の歴史}; L113 \subsection{連続潜在から離散符号へ：推論の償却化と量子化}; L1152 \section{結び──座標として読むメディア生成史}; L118 \subsection{階層と知覚：高解像度への二つの道}
- evidence: btd001, btd002, btd003, btd004, btd005, btd006
- before: 26 / residual: 0

### TS543-B05 [BROAD_SCAN] — 持続長 → デュレーション [REPLACE]
- canonical: duration | meaning: デュレーション20件
- rationale: TTS duration全件; 持続長モデルと整合
- occurrences: L441,L454,L456,L458,L468,L476,L488,L491,L509,L511,L523,L549,L550,L553
- sections: L435 \section{音声・声の系譜：波形からEnd-to-End、ニューラルコーデック言語モデル、全二重へ}\sectionkicker{SPEECH}\la; L453 \subsection{並列化とニューラルボコーダと端末間統合：遅さと注意破綻への応答}; L475 \subsection{何を何で表すか：言語・意味・音響・符号・波形の分担}; L508 \subsection{流れ補完と実時間化：非自己回帰と前後文脈の統一}
- evidence: btd051, btd052, btd053, btd054, btd055, btd056
- before: 20 / residual: 0

### TS543-B06 [BROAD_SCAN] — 色度 → クロマ [REPLACE]
- canonical: chroma | meaning: クロマ18件
- rationale: 音楽chroma全件; 測色用法なし
- occurrences: L580,L582,L584,L605,L613,L617,L634,L645,L664,L677,L678,L685,L697
- sections: L579 \subsection{一段階可制御符号音楽：多段階層の低速への応答}; L588 \subsection{波形拡散と潜在拡散：局所忠実度と一般音響化の二系統}; L612 \subsection{時間条件・楽理制御と人間選好検証：開放重みと評価境界}; L627 \subsection{生成・継続・編集・制御の分離：課題設定の区別}
- evidence: btd066, btd067, btd069, btd068, btd063, btd065
- before: 18 / residual: 0

### TS543-B07 [BROAD_SCAN] — 低階数/階数(rank) → 低ランク/ランク [REPLACE]
- canonical: (low-)rank | meaning: LoRA rank 24件
- rationale: 低階数17+調整2+切替え2+精度2+倍率1(重複注記); 段階数は対象外
- occurrences: L290,L304,L306,L322,L330,L332,L333,L335,L343,L345,L350,L353,L932
- sections: L285 \subsection{四区分の使い分け：条件と誘導と適合と参照}; L298 \section{制御と参照：空間・参照・主体性の保存}; L309 \subsection{配置の前史と軽量適合：洗い流さない工夫}; L327 \subsection{画像参照の分離注意：文能力を壊さない足し方}
- evidence: btd036, btd037, btd039, btd042, btd041, btd038
- before: 25 / residual: 0

### TS543-B08 [BROAD_SCAN] — 脱落(dropout) → ドロップアウト [REPLACE]
- canonical: dropout | meaning: ドロップアウト26件
- rationale: 層/条件づけ/文/画像/誘導/prompt/独立/学習時/割合法/率; 高周波細部2件は信号損失のためB08b
- occurrences: L143,L145,L153,L158,L249,L255,L258,L260,L276,L283,L286,L288,L293,L296…
- sections: L142 \subsection{音の残差量子化：低速度と遅延の両立}; L152 \subsection{三軸のまとめ：何を削り何を残したか}; L157 \subsection{本節の読解上の境界}; L241 \section{条件づけとアライメント}
- evidence: btd006, btd007, btd008, btd001, btd002, btd003
- before: 28 / residual: 2

### TS543-B08b [BROAD_SCAN] — 周波細部の脱落 → 周波細部の脱落 [RETAIN]
- canonical: detail loss | meaning: 量子化の高域損失2件
- rationale: dropout正則化ではなく情報損失
- occurrences: L153,L158
- sections: L152 \subsection{三軸のまとめ：何を削り何を残したか}; L157 \subsection{本節の読解上の境界}
- evidence: btd001, btd002, btd003, btd004, btd005, btd006
- before: 2 / residual: 2

### TS543-B09 [BROAD_SCAN] — 多層知覚器 → 多層パーセプトロン [REPLACE]
- canonical: multilayer perceptron | meaning: MLP 4件
- rationale: 版内表記と統一
- occurrences: L306,L340,L343,L353
- sections: L298 \section{制御と参照：空間・参照・主体性の保存}; L337 \subsection{時間信号の分離制御：映像の動きと音楽の変化}; L342 \subsection{適合器の系譜：凍結本体に触れず足す}; L352 \subsection{本節の読解上の境界}
- evidence: btd037, btd041, btd038, btd039, btd040, btd042
- before: 4 / residual: 0

### TS543-B10 [BROAD_SCAN] — 自己符号化器 → 条件付き変分オートエンコーダ/変分オートエンコーダ [REPLACE]
- canonical: (conditional variational) autoencoder | meaning: CVAE/VAE 4件
- rationale: 版内オートエンコーダ表記と統一
- occurrences: L376,L441,L454,L470
- sections: L373 \subsection{潜在局所合成：前景と背景の分離}; L435 \section{音声・声の系譜：波形からEnd-to-End、ニューラルコーデック言語モデル、全二重へ}\sectionkicker{SPEECH}\la; L453 \subsection{並列化とニューラルボコーダと端末間統合：遅さと注意破綻への応答}
- evidence: btd046, btd051, btd052, btd053, btd054, btd055
- before: 4 / residual: 0

### TS543-B11 [BROAD_SCAN] — 発音素 → 音素 [REPLACE]
- canonical: phoneme | meaning: G2Pフロントエンド4件
- rationale: 同一文内の音素表記と統一
- occurrences: L458,L550,L553
- sections: L453 \subsection{並列化とニューラルボコーダと端末間統合：遅さと注意破綻への応答}; L520 \subsection{Seed-TTS（多用途・高忠実音声生成）・翻訳・全二重対話：実環境と遅延の両立}; L552 \subsection*{読解上の境界}
- evidence: btd056, btd055, btd054, btd060, btd132, btd133
- before: 4 / residual: 0

### TS543-B12 [BROAD_SCAN] — 尖頭 → ピーク [REPLACE]
- canonical: peak (PSNR) | meaning: ピーク2件
- rationale: benchmark表のmetric label
- occurrences: L777,L804
- sections: L774 \subsection{閉鎖頂点・開放混合専門家と編集基準測定：基盤への到達}; L803 \subsection{参照・条件づけ・編集と基準測定の配置}
- evidence: btd138, btd070, btd071, btd073, btd075, btd074
- before: 2 / residual: 0

### TS543-B13 [BROAD_SCAN] — 様式崩壊 → モード崩壊 [REPLACE]
- canonical: mode collapse | meaning: GAN mode collapse 2件
- rationale: DCGAN文脈で確定
- occurrences: L190,L239
- sections: L189 \subsection{敵対的生成の系譜：暗黙分布から様式分離へ}; L238 \subsection{本節の読解上の境界}
- evidence: btd013, btd014, btd015, btd016, btd019, btd020
- before: 2 / residual: 0

### TS543-B14 [BROAD_SCAN] — 濾波崩壊 → 一部フィルタの単一振動モードへの崩壊 [REPLACE] (Sol r2 P-001 resolved)
- canonical: filter collapse? | meaning: 長期学習2件
- rationale: canonical termを原典未確認のため推測せず; モード崩壊との関係も含めSolへ
- occurrences: L190,L239
- sections: L189 \subsection{敵対的生成の系譜：暗黙分布から様式分離へ}; L238 \subsection{本節の読解上の境界}
- evidence: btd013, btd014, btd015, btd016, btd019, btd020
- before: 2 / residual: 2

### TS543-B15 [BROAD_SCAN] — 滑動窓 → スライディングウィンドウ [REPLACE]
- canonical: sliding window | meaning: sliding window 2件
- rationale: backbone文脈
- occurrences: L119,L158
- sections: L118 \subsection{階層と知覚：高解像度への二つの道}; L157 \subsection{本節の読解上の境界}
- evidence: btd003, btd004, btd006, btd008, btd001, btd002
- before: 2 / residual: 0

### TS543-B16 [BROAD_SCAN] — 歩幅/分数歩幅 → ストライド畳み込み/分数ストライド [REPLACE]
- canonical: (fractionally-)strided | meaning: DCGAN stride 4件
- rationale: 識別器/生成器
- occurrences: L190
- sections: L189 \subsection{敵対的生成の系譜：暗黙分布から様式分離へ}
- evidence: btd013, btd014
- before: 4 / residual: 0

### TS543-B17 [BROAD_SCAN] — 鍵語 → キーワード [REPLACE]
- canonical: keyword | meaning: CLAP keyword 2件
- rationale: 評価境界文
- occurrences: L281,L296
- sections: L280 \subsection{音響の言語整合と空間制御の適合}; L295 \subsection{本節の読解上の境界}
- evidence: btd035, btd011, btd032, btd033, btd036, btd031
- before: 2 / residual: 0

### TS543-B18 [BROAD_SCAN] — 試料 → サンプル/ステム分離 [REPLACE]
- canonical: sample/stem | meaning: 生成sample+stem分離2件
- rationale: L32定義文+Sunno stemsで節別
- occurrences: L33,L1095
- sections: L1092 \subsection{音楽：制作手順としてのworkflow記録}; L30 \section*{本巻の問いと読み方}
- evidence: btd114, btd115, btd116
- before: 2 / residual: 0

### TS543-B19 [BROAD_SCAN] — 問合せ → クエリ [REPLACE]
- canonical: query | meaning: attention/GE2E query 5件
- rationale: Q共有/値/重心
- occurrences: L306,L328,L333,L992
- sections: L298 \section{制御と参照：空間・参照・主体性の保存}; L327 \subsection{画像参照の分離注意：文能力を壊さない足し方}; L332 \subsection{主体の焼付けと低階数：少数画像と効率切替え}; L991 \subsection{耳と話し言葉の土台を切り分ける}
- evidence: btd037, btd041, btd038, btd039, btd040, btd042
- before: 5 / residual: 0

### TS543-B20 [BROAD_SCAN] — 跳躍 → スキップ生成器/スキップ変数化/スキップ接続 [REPLACE]
- canonical: skip | meaning: skip系5件
- rationale: StyleGAN2/consistency/WaveNetで節別
- occurrences: L192,L230,L236,L449
- sections: L189 \subsection{敵対的生成の系譜：暗黙分布から様式分離へ}; L227 \subsection{Transformer denoiserと流れ・整合性モデルへの分岐}; L235 \subsection{短縮と蒸留から実行費用への接続}; L446 \subsection{波形自己回帰と系列変換：素片結合なしの出発点}
- evidence: btd015, btd016, btd027, btd028, btd029, btd025
- before: 5 / residual: 0

### TS543-B21 [BROAD_SCAN] — 遅延配置 → 遅延パターン [REPLACE]
- canonical: delay pattern | meaning: MusicGen delay 4件
- rationale: named architectural pattern
- occurrences: L563,L580,L582,L605
- sections: L555 \section{音楽・一般音響の系譜：コーデック言語モデルと潜在拡散}\sectionkicker{MUSIC}\label{sec:music}; L579 \subsection{一段階可制御符号音楽：多段階層の低速への応答}; L588 \subsection{波形拡散と潜在拡散：局所忠実度と一般音響化の二系統}
- evidence: btd063, btd065, btd066, btd064, btd067, btd068
- before: 4 / residual: 0

### TS543-B22 [BROAD_SCAN] — 流れ化 → フロー化 [REPLACE]
- canonical: flow-ize | meaning: 部分入力フロー4件
- rationale: 非標準動詞の最小正規化; 流れ補完と整合
- occurrences: L516,L518,L523
- sections: L515 \subsection{因果性と遅延と全二重：速さと同時性の分離}; L520 \subsection{Seed-TTS（多用途・高忠実音声生成）・翻訳・全二重対話：実環境と遅延の両立}
- evidence: btd060, btd133, btd132, btd062, btd134, btd061
- before: 4 / residual: 0

### TS543-B23 [BROAD_SCAN] — 素片結合 → 連結合成 [REPLACE]
- canonical: concatenative synthesis | meaning: 非連結合成3件
- rationale: §6テーゼ+表題含む
- occurrences: L441,L446,L447
- sections: L435 \section{音声・声の系譜：波形からEnd-to-End、ニューラルコーデック言語モデル、全二重へ}\sectionkicker{SPEECH}\la; L446 \subsection{波形自己回帰と系列変換：素片結合なしの出発点}
- evidence: btd051, btd052, btd053, btd054, btd055, btd056
- before: 3 / residual: 0

### TS543-B24 [BROAD_SCAN] — 力学(music) → ダイナミクス [REPLACE]
- canonical: dynamics | meaning: 楽曲ダイナミクス2件
- rationale: 旋律/拍文脈
- occurrences: L340
- sections: L337 \subsection{時間信号の分離制御：映像の動きと音楽の変化}
- evidence: btd043
- before: 2 / residual: 0

### TS543-B24b [BROAD_SCAN] — 力学(physics) → 力学 [RETAIN]
- canonical: mechanics | meaning: 力学検証3件
- rationale: simulator検証の力学
- occurrences: L835,L889
- sections: L834 \subsection{物理的妥当性を二値で問う手順とその天井}; L866 \subsection{単発の主張を長時間の証拠に格上げしない}
- evidence: btd131
- before: 3 / residual: 3

### TS543-B25 [BROAD_SCAN] — 可変束縛 → 変数束縛 [REPLACE]
- canonical: variable binding | meaning: T2I-CompBench 2件
- rationale: 属性binding
- occurrences: L140,L158
- sections: L137 \subsection{文と画像の単一列：大規模条件づけの前の短縮}; L157 \subsection{本節の読解上の境界}
- evidence: btd005, btd002, btd006, btd008, btd001, btd004
- before: 2 / residual: 0

### TS543-B26 [BROAD_SCAN] — 段階専門家/専門家集成 → 段階エキスパート/エキスパートアンサンブル [REPLACE]
- canonical: (noise-level) expert/ensemble | meaning: eDiff-i系9件(段階専門家集成1件は両pat重複)
- rationale: denoiser expert; 節表題含む
- occurrences: L247,L249,L270,L275,L276,L278,L286
- sections: L241 \section{条件づけとアライメント}; L257 \subsection{推論時誘導への転換：分類器なし誘導と文誘導拡散}; L275 \subsection{段階専門家への分岐：共有 denoiser の分割}; L285 \subsection{四区分の使い分け：条件と誘導と適合と参照}
- evidence: btd011, btd032, btd031, btd033, btd034, btd035
- before: 10 / residual: 0

### TS543-B27 [BROAD_SCAN] — 凍結文符号器 → 凍結テキストエンコーダ [REPLACE]
- canonical: frozen text encoder | meaning: Imagen系3件
- rationale: #539文章符号器の綴り違い; 同一実体
- occurrences: L255,L268,L286
- sections: L252 \subsection{凍結符号器による文条件づけ：対照事前学習の継承}; L257 \subsection{推論時誘導への転換：分類器なし誘導と文誘導拡散}; L285 \subsection{四区分の使い分け：条件と誘導と適合と参照}
- evidence: btd011, btd031, btd032, btd033, btd034, btd035
- before: 3 / residual: 0

### TS543-B28 [BROAD_SCAN] — 雛形(prompt/集合/UI) → プロンプトテンプレート/テンプレート集合/下書き [REPLACE]
- canonical: prompt template/set/draft | meaning: template 8件
- rationale: CLIP文脈6+集合1+UI draft1で節別
- occurrences: L249,L253,L281,L293,L1087
- sections: L1084 \subsection{画像：生成と反復編集のworkflow表面}; L241 \section{条件づけとアライメント}; L252 \subsection{凍結符号器による文条件づけ：対照事前学習の継承}; L280 \subsection{音響の言語整合と空間制御の適合}
- evidence: btd031, btd011, btd032, btd033, btd034, btd035
- before: 8 / residual: 0

### TS543-B29 [BROAD_SCAN] — 畳み込み/安定化/設計指針 → 畳み込み/安定化/設計ガイドライン [REPLACE]
- canonical: (DCGAN) guidelines | meaning: 設計指針5件
- rationale: named guidelines
- occurrences: L168,L172,L181,L190,L205
- sections: L160 \section{生成パラダイムと目的関数：自己回帰・敵対・拡散・フロー}; L171 \subsection{六軸分離の読み方：表現・骨格・目的・経路・抽出・短縮}; L189 \subsection{敵対的生成の系譜：暗黙分布から様式分離へ}; L194 \subsection{完全自己回帰：画素の同時分布を捉える}
- evidence: btd013, btd014, btd015, btd016, btd017, btd018
- before: 5 / residual: 0

### TS543-B29b [BROAD_SCAN] — 指針(general) → 指針 [RETAIN]
- canonical: guideline | meaning: 一般指針6件
- rationale: 使い分け/結び等の一般語
- occurrences: L69,L91,L168,L172,L181,L190,L205,L288,L345,L348,L1170
- sections: L1170 \subsection{立場別の指針}; L160 \section{生成パラダイムと目的関数：自己回帰・敵対・拡散・フロー}; L171 \subsection{六軸分離の読み方：表現・骨格・目的・経路・抽出・短縮}; L189 \subsection{敵対的生成の系譜：暗黙分布から様式分離へ}
- evidence: btd013, btd014, btd015, btd016, btd017, btd018
- before: 11 / residual: 6

### TS543-B30 [BROAD_SCAN] — 照合 → マッチング/検証/フローマッチング [REPLACE]
- canonical: matching/verification | meaning: 照合12件
- rationale: cosine/多数決/勝率/flow/話者/手順で節別
- occurrences: L249,L281,L835,L867,L932,L962,L992,L995,L997,L1006
- sections: L241 \section{条件づけとアライメント}; L280 \subsection{音響の言語整合と空間制御の適合}; L834 \subsection{物理的妥当性を二値で問う手順とその天井}; L866 \subsection{単発の主張を長時間の証拠に格上げしない}
- evidence: btd031, btd011, btd032, btd033, btd034, btd035
- before: 12 / residual: 0

### TS543-B31 [BROAD_SCAN] — 札 → タグ条件/タグ事前学習/タグのみ文/タグ付き混合/副次タグ [REPLACE]
- canonical: tag/label | meaning: タグ11件
- rationale: 音楽+AudioPaLM+受容の三 sense を統一
- occurrences: L306,L340,L353,L1029,L1039,L1130,L1132,L1138
- sections: L1028 \subsection{話し言葉と文章の往復を一つの復号器に畳む}; L1122 \section{受容とcounter-signal：現場の27件の記録}; L1134 \subsection{台帳の読み方：確定側と未決側の分離}; L298 \section{制御と参照：空間・参照・主体性の保存}
- evidence: btd037, btd041, btd038, btd039, btd040, btd042
- before: 11 / residual: 0

### TS543-B32 [BROAD_SCAN] — 供給者 → 提供元 [REPLACE]
- canonical: provider | meaning: 提供元と同役17件
- rationale: ベンダー(商業)と区別し提供元へ統一
- occurrences: L513,L521,L525,L538,L543,L544,L553,L621,L707,L775,L783,L813,L822
- sections: L508 \subsection{流れ補完と実時間化：非自己回帰と前後文脈の統一}; L520 \subsection{Seed-TTS（多用途・高忠実音声生成）・翻訳・全二重対話：実環境と遅延の両立}; L552 \subsection*{読解上の境界}; L612 \subsection{時間条件・楽理制御と人間選好検証：開放重みと評価境界}
- evidence: btd132, btd133, btd060, btd061, btd062, btd134
- before: 17 / residual: 0

### TS543-B33a [BROAD_SCAN] — 膨張(inflation) → 拡張初期化/拡張 [REPLACE]
- canonical: inflation | meaning: 2D→3D inflation 7件
- rationale: dilationと区別
- occurrences: L148,L407,L705,L727,L732,L746,L765
- sections: L147 \subsection{意味と音響の分離、映像の時空間短縮}; L402 \subsection{指示追従学習と一段階動画編集：手続きの隠蔽と時間への拡張}; L699 \section{映像の系譜：時間的一貫性からメディア基盤へ}\sectionkicker{VIDEO}\label{sec:video}; L726 \subsection{因子分解の設計差：二次元＋時間と時空間とTransformer}
- evidence: btd009, btd010, btd012, btd050, btd070, btd071
- before: 7 / residual: 0

### TS543-B33b [BROAD_SCAN] — 膨張(dilated) → 膨張畳み込み/因果/循環/モデル [RETAIN]
- canonical: dilated convolution | meaning: dilated 9件
- rationale: 定着したdilated訳
- occurrences: L418,L441,L447,L449,L466,L589,L591,L606,L777
- sections: L402 \subsection{指示追従学習と一段階動画編集：手続きの隠蔽と時間への拡張}; L435 \section{音声・声の系譜：波形からEnd-to-End、ニューラルコーデック言語モデル、全二重へ}\sectionkicker{SPEECH}\la; L446 \subsection{波形自己回帰と系列変換：素片結合なしの出発点}; L453 \subsection{並列化とニューラルボコーダと端末間統合：遅さと注意破綻への応答}
- evidence: btd050, btd051, btd052, btd053, btd054, btd055
- before: 9 / residual: 9

### TS543-B33c [BROAD_SCAN] — 膨張形式 → 擬似3D畳み込みへのnetwork inflation（3×3→1×3×3） [REPLACE] (Sol r2 E-001 resolved)
- canonical: dilation/mask format? | meaning: 編集条件1件
- rationale: mask dilationか形式か原典未確認
- occurrences: L427
- sections: L402 \subsection{指示追従学習と一段階動画編集：手続きの隠蔽と時間への拡張}
- evidence: btd044, btd045, btd046, btd047, btd048, btd049
- before: 1 / residual: 1

### TS543-B34 [BROAD_SCAN] — 版バインド → 版バインド [RETAIN]
- canonical: version binding | meaning: lifecycle版束縛16件
- rationale: 版-family統一語彙; 16件churn回避; Sol判断に委ねる
- occurrences: L39,L1089,L1090,L1093,L1098,L1101,L1106,L1110,L1113,L1119,L1171
- sections: L1089 \subsection{音声・対話：実時間利用と版バインドの機能集合}; L1092 \subsection{音楽：制作手順としてのworkflow記録}; L1097 \subsection{映像：joint化と短区間・長距離の分離}; L1100 \subsection{lifecycle：提供終了・廃止・凍結の事実}
- evidence: btd022, btd059, btd083, btd089, btd098, btd106
- before: 16 / residual: 16

### TS543-B35 [BROAD_SCAN] — 検査点 → 検査点 [RETAIN]
- canonical: (version) checkpoint | meaning: 版検査点6件
- rationale: 版と検査点の固定句; 版family統一
- occurrences: L703,L705,L775,L822,L824
- sections: L699 \section{映像の系譜：時間的一貫性からメディア基盤へ}\sectionkicker{VIDEO}\label{sec:video}; L774 \subsection{閉鎖頂点・開放混合専門家と編集基準測定：基盤への到達}; L821 \subsection*{読解上の境界}
- evidence: btd070, btd071, btd073, btd074, btd075, btd077
- before: 6 / residual: 6

### TS543-B36 [BROAD_SCAN] — 誘導(guidance) → 誘導 [RETAIN]
- canonical: guidance/steering | meaning: guidance 118件
- rationale: #539 K01凍結(ガイダンス8件)と役割分担; 版内 steering 語彙
- occurrences: L213,L215,L217,L218,L225,L228,L230,L239,L247,L249,L255,L257,L258,L260…
- sections: L1052 \subsection{来歴機構の頁限定と開かれた問い}; L212 \subsection{雑音除去の転換：拡散と短縮抽出}; L217 \subsection{条件誘導の分岐：分類器誘導と分類器なし誘導}; L220 \subsection{連続時間への統一と潜在への移行}
- evidence: btd019, btd030, btd020, btd032, btd023, btd025
- before: 118 / residual: 118

### TS543-B37 [BROAD_SCAN] — 符号器/復号器 → 符号器/復号器 [RETAIN]
- canonical: encoder/decoder | meaning: 符号器/復号器系
- rationale: #539 H凍結: genericは対象外; 凍結文符号器3件のみB27で正規化(112→109の差)
- occurrences: L108,L114,L116,L119,L121,L138,L143,L145,L148,L150,L155,L158,L168,L190…
- sections: L100 \section{表現と圧縮：生成可能にする短縮の歴史}; L1025 \subsection{課題別頭部を持たない多課題統合の射程}; L1028 \subsection{話し言葉と文章の往復を一つの復号器に畳む}; L113 \subsection{連続潜在から離散符号へ：推論の償却化と量子化}
- evidence: btd006, btd008, btd009, btd010, btd001, btd002
- before: 112 / residual: 109

### TS543-B38 [BROAD_SCAN] — 上位サンプリング → アップサンプリング [REPLACE]
- canonical: upsampling | meaning: upsample 1件
- rationale: 上位/下位hierarchy自体は対象外
- occurrences: L580
- sections: L579 \subsection{一段階可制御符号音楽：多段階層の低速への応答}
- evidence: btd066
- before: 1 / residual: 0

### TS543-B39 [BROAD_SCAN] — 姿勢(pose) → ポーズ [REPLACE]
- canonical: pose | meaning: motion pose 9件
- rationale: 姿勢注釈/注入/軌跡/誤差のpose用法; stance 4件はB39b
- occurrences: L338,L342
- sections: motion control
- evidence: btd042, btd124
- before: 9 / residual: 0

### TS543-B39b [BROAD_SCAN] — 姿勢(stance) → 姿勢 [RETAIN]
- canonical: stance/attitude | meaning: 編集姿勢4件
- rationale: 一般語の姿勢(態度)として正しい
- occurrences: L835,L838,L1053,L1054
- sections: evaluation/capstone/lifecycle/synthesis
- before: 4 / residual: 4


# r2 supplement — Sol authoritative map application (Human r8 authority)

r2 rows: 51 with provenance SOL_AUTHORITATIVE_R2.
## Summary (all rows)
- BROAD_SCAN / ESCALATE: 2
- BROAD_SCAN / REPLACE: 34
- BROAD_SCAN / RETAIN: 9
- ISSUE_SEED / ESCALATE: 2
- ISSUE_SEED / REPLACE: 39
- ISSUE_SEED / RETAIN: 4
- SOL_MAP_R2 / REPLACE: 51
- r1 ESCALATE resolutions: S39c partial (L1090→Naturalness MOS; L1108→C-001), S40c (SOL-R-002/CIT-001), B14 (SOL-P-001), B33c (SOL-E-001).
- Unresolved: muse-candidates-for-sol-review-r2.md (C-001…C-011).

### TS543-R2-CIT001 [SOL-CIT-001] — 均衡ある全帯域抽出+btd007 binding → EnCodec境界+btd007 / DAC Balanced data sampling（均衡データサンプリング）+btd008 [REPLACE]
- canonical: Balanced data sampling | meaning: EnCodec/DAC split passage
- rationale: sole authorized citation change; autocite 1259→1260 (+1 btd008), keys stay 139
- occurrences: L158 | before: 1 / residual: 0
- evidence: btd006, btd008, btd001, btd004, btd002, btd007

### TS543-R2-G001 [SOL-G-001] — 標本(generated) → サンプル/生成例 [REPLACE]
- canonical: sample | meaning: 生成標本19件
- rationale: statistical 19 + L233 CAND + 一括要点 variant untouched
- occurrences: L33,L69,L168,L190,L213,L283,L304,L340,L347,L348… | before: 19 / residual: 0
- evidence: btd013, btd014, btd015, btd016, btd017, btd018

### TS543-R2-G002 [SOL-G-002] — 消費者用図形処理装置/図形処理装置 → 民生GPU/GPU [REPLACE]
- canonical: consumer GPU/GPU | meaning: HW 3件
- rationale: 中央処理装置は既に0
- occurrences: L148,L197,L239 | before: 4 / residual: 0
- evidence: btd009, btd010, btd012, btd017, btd018, btd013

### TS543-R2-G003 [SOL-G-003] — 検査点/基準測定/多回合 → チェックポイント/ベンチマーク評価/マルチターン [REPLACE]
- canonical: checkpoint/benchmark/multi-turn | meaning: V-007/C-002系
- rationale: 通貨拘束→0; 版バインドはSol retain
- occurrences: L33,L703,L705,L707,L774,L775,L779,L803,L804,L822… | before: 17 / residual: 0
- evidence: btd070, btd071, btd073, btd074, btd075, btd077

### TS543-R2-F001 [SOL-F-001] — raw系列 → 生の系列 [REPLACE]
- canonical: raw sequence | meaning: 1件
- rationale: L1160
- occurrences: L1160 | before: 1 / residual: 0
- evidence: btd002, btd023, btd032, btd039, btd049

### TS543-R2-F002 [SOL-F-002] — adapter → アダプター [REPLACE]
- canonical: adapter | meaning: bare English 1件
- rationale: L1160; bib対象外
- occurrences: L1160 | before: 1 / residual: 0
- evidence: btd002, btd023, btd032, btd039, btd049

### TS543-R2-F003 [SOL-F-003] — 集合(dataset) → データセット [REPLACE]
- canonical: dataset | meaning: 34件
- rationale: 数学集合6+候補10は不変
- occurrences: L720,L724,L838,L861,L901,L926,L929,L965,L992,L1014… | before: 31 / residual: 0
- evidence: btd073, btd129, btd130, btd078, btd081, btd082

### TS543-R2-F004 [SOL-F-004] — 生徒 → student model（生徒モデル）/生徒モデル [REPLACE]
- canonical: student model | meaning: 蒸留student 3件
- rationale: 文脈別初出
- occurrences: L901,L926 | before: 3 / residual: 0
- evidence: btd078, btd081

### TS543-R2-P001 [SOL-P-001] — 濾波崩壊 → 一部フィルタの単一振動モードへの崩壊 [REPLACE]
- canonical: filter collapse (DCGAN) | meaning: 2件
- rationale: generic mode collapseにせず
- occurrences: L190,L239 | before: 2 / residual: 0
- evidence: btd013, btd014, btd015, btd016, btd019, btd020

### TS543-R2-P002 [SOL-P-002] — 予測子修正子/修正子 → predictor-corrector（予測子・修正子）/corrector（修正子） [REPLACE]
- canonical: predictor-corrector | meaning: btd021 4件
- rationale: 同文脈のみ
- occurrences: L221,L239 | before: 5 / residual: 4
- evidence: btd021, btd013, btd014, btd015, btd016, btd019

### TS543-R2-P003 [SOL-P-003] — 規模則 → スケーリング則 [REPLACE]
- canonical: scaling law | meaning: DiT 2件
- occurrences: L228,L239 | before: 2 / residual: 0
- evidence: btd025, btd026, btd013, btd014, btd015, btd016

### TS543-R2-P004 [SOL-P-004] — 再流 → reflow（再フロー） [REPLACE]
- canonical: reflow | meaning: Rectified Flow 10件
- occurrences: L230,L233,L239 | before: 10 / residual: 0
- evidence: btd027, btd028, btd029, btd025, btd026, btd013

### TS543-R2-P005 [SOL-P-005] — 一致性 → 整合性 [REPLACE]
- canonical: Consistency | meaning: family 1件
- rationale: front-matter
- occurrences: L63 | before: 1 / residual: 0

### TS543-R2-P006 [SOL-P-006] — 単一網/級上げ器/級上げ → 単一ネットワーク/アップサンプラー/アップサンプリング [REPLACE]
- canonical: network/upsampler | meaning: ML network/upsampler 4件
- occurrences: L218,L239,L258 | before: 4 / residual: 0
- evidence: btd030, btd032, btd023, btd025, btd013, btd014

### TS543-R2-P007 [SOL-P-007] — 問い合わせ行列 → クエリ射影行列（W^Q） [REPLACE]
- canonical: query projection matrix | meaning: TAV 1件
- rationale: btd050
- occurrences: L407 | before: 1 / residual: 0
- evidence: btd050

### TS543-R2-R001 [SOL-R-001] — 分類得点 → Classification Accuracy Score（CAS） [REPLACE]
- canonical: CAS | meaning: btd003 1件
- rationale: r1 ESCALATE解消
- occurrences: L158 | before: 1 / residual: 0
- evidence: btd006, btd008, btd001, btd004, btd002, btd007

### TS543-R2-R003 [SOL-R-003] — 長い結構/鍵盤継続 → 長期構造/ピアノ継続 [REPLACE]
- canonical: long-term structure/piano continuation | meaning: btd009 2件
- rationale: ['長い結構', '鍵盤継続']
- occurrences:  | before: 0 / residual: 0

### TS543-R2-R004 [SOL-R-004] — 多峰入出力 → マルチモーダル入出力 [REPLACE]
- canonical: multimodal I/O | meaning: 1件
- rationale: ['多峰入出力']
- occurrences:  | before: 0 / residual: 0

### TS543-R2-S001 [SOL-S-001] — 位置鋭敏注意/近似波形合成/三膨張循環/十要素混合 → location-sensitive attention/Griffin-Lim/dilation cycle/logistic mixture [REPLACE]
- canonical: Tacotron canonicals | meaning: 7件
- occurrences: L447,L449,L451,L467,L487 | before: 7 / residual: 0
- evidence: btd051, btd052, btd053, btd054

### TS543-R2-S002 [SOL-S-002] — 系列網 → LSTM-RNNパラメトリック音声合成 [REPLACE]
- canonical: WaveNet RNN baseline | meaning: 1件
- rationale: 他文脈なし
- occurrences: L447 | before: 1 / residual: 0
- evidence: btd051, btd052, btd053

### TS543-R2-S003 [SOL-S-003] — 群化符号/群化 → Grouped Code Modeling（グループ化コードモデリング） [REPLACE]
- canonical: Grouped Code Modeling | meaning: VALL-E2 7件
- rationale: 群化後継2件は候補
- occurrences: L443,L499,L535,L547 | before: 12 / residual: 2
- evidence: btd059, btd134

### TS543-R2-S004 [SOL-S-004] — 多能高忠実モデル → Seed-TTS（多用途・高品質音声生成モデル） [REPLACE]
- canonical: Seed-TTS | meaning: 4件
- rationale: 初出gloss+略称
- occurrences: L441,L521,L523,L544 | before: 4 / residual: 0
- evidence: btd051, btd052, btd053, btd054, btd055, btd056

### TS543-R2-S005 [SOL-S-005] — 自然さ得点(btd110) → Naturalness MOS（自然さMOS） [REPLACE]
- canonical: Naturalness MOS | meaning: 1件
- rationale: L1108は文脈外で候補C-001
- occurrences: L1090 | before: 1 / residual: 0
- evidence: btd107, btd108, btd109, btd110

### TS543-R2-M001 [SOL-M-001] — 音楽 caps/音響 caps → MusicCaps/AudioCaps [REPLACE]
- canonical: MusicCaps/AudioCaps | meaning: 13件
- rationale: 既存英語は維持
- occurrences: L561,L563,L569,L580,L589,L604,L607,L613,L685,L688 | before: 13 / residual: 0
- evidence: btd136, btd063, btd065, btd066, btd067, btd068

### TS543-R2-M002 [SOL-M-002] — 距離/乖離/整合(btd065) → FAD/KLD/MCC [REPLACE]
- canonical: FAD/KLD/MCC | meaning: 10 labels/16 numbers
- rationale: btd065数値のみ; 他は候補C-003
- occurrences: L569,L573,L604,L662 | before: 10 / residual: 0
- evidence: btd063, btd065, btd066, btd068, btd067

### TS543-R2-M003 [SOL-M-003] — 距離/乖離/整合/全体/関係性(btd066) → FAD/KLD/CLAP score/OVL/REL [REPLACE]
- canonical: FAD/KLD/CLAP/OVL/REL | meaning: pure btd066のみ
- rationale: 混合引用は候補
- occurrences: L580,L586,L605,L685 | before: 8 / residual: 1
- evidence: btd066, btd069, btd067, btd068, btd065, btd063

### TS543-R2-M004 [SOL-M-004] — 23.31/65.91(btd067) → FD $23.31$/OVL $65.91$ [REPLACE]
- canonical: FD/OVL | meaning: 3件
- rationale: 他数値は候補
- occurrences: L589,L607,L660,L685 | before: 6 / residual: 3
- evidence: btd064, btd067, btd063, btd068, btd065, btd136

### TS543-R2-M005 [SOL-M-005] — 開放距離78.24(btd068) → FD_openl3 $78.24$ [REPLACE]
- canonical: FD_openl3 | meaning: 1件
- rationale: 他数値は候補
- occurrences: L613,L660,L685 | before: 3 / residual: 2
- evidence: btd068, btd069, btd063, btd064, btd067, btd065

### TS543-R2-M006 [SOL-M-006] — 帯域収束(btd063 metric) → spectral convergence（スペクトル収束） [REPLACE]
- canonical: spectral convergence | meaning: 3件
- rationale: L577 genericは維持
- occurrences: L569,L577,L603,L660 | before: 4 / residual: 1
- evidence: btd063, btd065, btd064, btd067, btd068, btd136

### TS543-R2-M007 [SOL-M-007] — 節/副歌(music) → ヴァース/コーラス [REPLACE]
- canonical: verse/chorus | meaning: 26件
- rationale: 132節は非音楽で維持
- occurrences: L569,L571,L573,L575,L603,L630,L651,L653,L655,L691… | before: 28 / residual: 0
- evidence: btd063, btd065, btd066, btd068, btd069, btd136

### TS543-R2-M008 [SOL-M-008] — 流派/刈込/続成 → ジャンル/トリミング/continuation（継続生成） [REPLACE]
- canonical: genre/trim/continuation | meaning: 5件
- rationale: ['流派・気分', '刈込', '続成']
- occurrences:  | before: 0 / residual: 0

### TS543-R2-M009 [SOL-M-009] — 人文系 → 人間によるside-by-side評価/人間評価・自動評価/ベンダーによる人間評価への言及 [REPLACE]
- canonical: human eval wording | meaning: 4件
- rationale: ['人文横並べ', '人文・自動評価', 'ベンダー人文言及']
- occurrences:  | before: 0 / residual: 0

### TS543-R2-V001 [SOL-V-001] — 外観凍結/網データ/長多場面 → 外観と運動の分離学習/Webデータ/長尺・マルチシーン [REPLACE]
- canonical: separation/Web/マルチシーン | meaning: 11件
- rationale: L719表題は逐語適用で冗長化(ledger注記)
- occurrences: L719,L722,L724,L744,L767,L807,L819,L822 | before: 11 / residual: 0
- evidence: btd073, btd074, btd075, btd070, btd071, btd124

### TS543-R2-V002 [SOL-V-002] — 動作接続器/運動LoRA/領域接続器/平滑/深度clause → Motion Module/Motion LoRA/Domain Adapter/motion smoothness/定性clause [REPLACE]
- canonical: AnimateDiff canonicals | meaning: 26件
- rationale: 平滑化は数学用法で候補
- occurrences: L233,L239,L376,L395,L433,L703,L705,L727,L732,L752… | before: 30 / residual: 6
- evidence: btd027, btd028, btd013, btd014, btd015, btd016

### TS543-R2-V003 [SOL-V-003] — 厳選潜在動画/LVD/人間序列 → SVD/LVD-10M-F/人間選好評価 [REPLACE]
- canonical: SVD/LVD-F/選好 | meaning: 14件
- rationale: 変異形は候補
- occurrences: L703,L705,L722,L727,L732,L752,L753,L759,L768,L807 | before: 13 / residual: 0
- evidence: btd070, btd071, btd073, btd074, btd075, btd077

### TS543-R2-V004 [SOL-V-004] — 動作接続器と厳選潜在動画表題 → AnimateDiffのMotion ModuleとStable Video Diffusion表題 [REPLACE]
- canonical: heading | meaning: 1件
- rationale: ['動作接続器と厳選潜在動画：']
- occurrences:  | before: 0 / residual: 0

### TS543-R2-V005 [SOL-V-005] — 閉鎖頂点 → 非公開モデル(表題はMoE+ベンチマーク形) [REPLACE]
- canonical: non-public models | meaning: 12件
- occurrences: L703,L705,L707,L708,L774,L775,L783,L810,L819,L822 | before: 12 / residual: 0
- evidence: btd070, btd071, btd073, btd074, btd075, btd077

### TS543-R2-V006 [SOL-V-006] — 開放混合専門家 → 開放重みのMixture-of-Experts（MoE）/開放重みMoE [REPLACE]
- canonical: MoE | meaning: 3件
- rationale: の-variantは候補
- occurrences: L703,L755,L774 | before: 3 / residual: 0
- evidence: btd070, btd071, btd073, btd074, btd075, btd077

### TS543-R2-V007 [SOL-V-007] — 基準測定/検査点/通貨拘束 → ベンチマーク評価/チェックポイント/固定句 [REPLACE]
- canonical: benchmark/checkpoint | meaning: 17件
- rationale: 通貨拘束→0
- occurrences: L703,L705,L707,L774,L775,L779,L803,L804,L822,L824 | before: 17 / residual: 0
- evidence: btd070, btd071, btd073, btd074, btd075, btd077

### TS543-R2-V008 [SOL-V-008] — 開放線2.2凍結4文 → Wan2.2確認境界文 [REPLACE]
- canonical: Wan2.2 boundary | meaning: 4件
- rationale: L39/L688別義は維持
- occurrences: L705,L734,L775,L822 | before: 4 / residual: 0
- evidence: btd070, btd071, btd073, btd075, btd074, btd077

### TS543-R2-V009 [SOL-V-009] — 単一良標本/低速高記憶/乱雑音/要点一括標本 → 生成例/低速高メモリ/ランダムノイズ/高品質動画のサンプリング [REPLACE]
- canonical: sampling wording | meaning: 22件
- rationale: ['単一良標本', '低速高記憶サンプリング', '乱雑音', '要点一括標本']
- occurrences:  | before: 0 / residual: 0

### TS543-R2-V010 [SOL-V-010] — 鋳造 → メディア基盤モデル群 [REPLACE]
- canonical: media foundation models | meaning: 1件
- rationale: abstract権威内
- occurrences: L1098 | before: 1 / residual: 0
- evidence: btd076, btd117, btd118, btd119

### TS543-R2-V011 [SOL-V-011] — 単走/多回合延長 → single pass（1回の生成）/multi-round extension（複数回の延長） [REPLACE]
- canonical: single pass/multi-round | meaning: 4件
- rationale: ['単走', '多回合延長']
- occurrences:  | before: 0 / residual: 0

### TS543-R2-V012 [SOL-V-012] — 首尾frame/外側描画 → 開始・終了フレーム/outpainting（アウトペインティング） [REPLACE]
- canonical: start-end frames/outpainting | meaning: 4件
- rationale: ['首尾frame', '外側描画']
- occurrences:  | before: 0 / residual: 0

### TS543-R2-C001 [SOL-C-001] — 並列道具 → 並列ツール呼び出し [REPLACE]
- canonical: parallel tool calls | meaning: 1件
- rationale: ['並列道具']
- occurrences:  | before: 0 / residual: 0

### TS543-R2-C002 [SOL-C-002] — 多回合振る舞い → マルチターン挙動 [REPLACE]
- canonical: multi-turn | meaning: 1件
- rationale: 延長2件はV-011
- occurrences: L33 | before: 1 / residual: 0

### TS543-R2-C003 [SOL-C-003] — 磁碟/局所実行/bench → ディスク/ローカル実行/ベンチマーク [REPLACE]
- canonical: disk/local/benchmark | meaning: 9件
- rationale: 英語benchmark3件は維持
- occurrences: L705,L777,L1093,L1098,L1108,L1130,L1132,L1135,L1143 | before: 12 / residual: 3
- evidence: btd070, btd071, btd073, btd075, btd074, btd077

### TS543-R2-C004 [SOL-C-004] — 流派(Lyria)/音声言語流派音響 → ジャンル/ジャンル・ムード・楽器・歌声などの制御 [REPLACE]
- canonical: genre | meaning: 3件
- rationale: ['流派', '音声言語流派音響']
- occurrences:  | before: 0 / residual: 0

### TS543-R2-C005 [SOL-C-005] — 包絡(capability) → 対応範囲 [REPLACE]
- canonical: envelope | meaning: 3件
- rationale: 数理包絡なし
- occurrences: L708,L740,L1110 | before: 3 / residual: 0
- evidence: btd070, btd071, btd075, btd124, btd073, btd074

### TS543-R2-C006 [SOL-C-006] — 多shot → マルチショット [REPLACE]
- canonical: multi-shot | meaning: 1件
- rationale: ['多shot']
- occurrences:  | before: 0 / residual: 0

### TS543-R2-E001 [SOL-E-001] — 膨張形式 → 擬似3D畳み込みへのnetwork inflation（3×3→1×3×3） [REPLACE]
- canonical: network inflation | meaning: 1件
- rationale: r1 ESCALATE解消
- occurrences: L427 | before: 1 / residual: 0
- evidence: btd044, btd045, btd046, btd047, btd048, btd049

### TS543-R2-BUILD [N/A (typesetting)] — W^Q / FD_openl3 (raw TeX) → W$^Q$ / FD\_openl3 [REPLACE]
- rationale: Pixel-identical visible output to Sol specification; build-necessary TeX-mode escape only, no term change. ×/→ already render in this document (pre-existing text-mode use). Sol may revert/adjust.
- occurrences: L407,L613 | before: 2 / residual: 0

# r3 supplement — Sol final residual map application (Human r9 authority)

r3 rows: 36 with provenance SOL_FINAL_RESIDUAL_R3 (discovery_source SOL_FINAL_RESIDUAL_R3).
r2 frozen retained; r3 prevails only where explicitly conflicting. Numbers/units unchanged except Sol-authorized metric label restoration. Citations: SOL-CIT-001 maintained (btd008/btd007 split); SOL-CIT-002 applied (Wan2.2 wording + btd124). No other citation change.
## Summary (all rows)
- ISSUE_SEED / REPLACE: 43
- ISSUE_SEED / RETAIN: 2
- BROAD_SCAN / REPLACE: 37
- BROAD_SCAN / RETAIN: 8
- SOL_MAP_R2 / REPLACE: 52
- SOL_FINAL_RESIDUAL_R3 / REPLACE: 35
- SOL_FINAL_RESIDUAL_R3 / RETAIN: 1
- ESCALATE: 0
- r1 ESCALATE resolutions: S39c (r3 C001), S40c (r2 CIT-001/R-002), B14 (r2 P-001), B33c (r2 E-001) — all final.
- New r9 candidates (if any): muse-candidates-for-sol-review-r9.md (CANDIDATE_FOR_SOL_REVIEW, no Muse wording).

### TS543-R3-C001 [SOL-R3-C001] — 自然さ得点 → Naturalness MOS（自然さMOS） [REPLACE]
- canonical: Naturalness MOS | meaning: Capstone L1108 | before: 1 / residual: 0 | evidence: btd110,btd111,btd112,btd113,btd114,btd115,btd116
### TS543-R3-C002 [SOL-R3-C002] — 群化後継 → VALL-E 2 / Grouped Code Modeling＋Repetition Aware Sampling [REPLACE]
- canonical: VALL-E 2 / Grouped Code Modeling / Repetition Aware Sampling | meaning: L499+L535 | before: 2 / residual: 0 | evidence: btd059
### TS543-R3-C003 [SOL-R3-C003] — AudioLDM generics → FD/IS/KL/FAD/OVL [REPLACE]
- canonical: FD/IS/KL/FAD/OVL | meaning: btd067 L589+L607+L660+L685 | before: 5 / residual: 0 | evidence: btd067
### TS543-R3-C004 [SOL-R3-C004] — Stable Audio Open generics → FD_openl3/KL_passt/CLAP score [REPLACE]
- canonical: FD_openl3/KL_passt/CLAP score | meaning: btd068 | before: 5 / residual: 0 | evidence: btd068
### TS543-R3-C005 [SOL-R3-C005] — MuSTANGO generics → FD/KL/PCM [REPLACE]
- canonical: FD/KL/PCM | meaning: btd069 | before: 5 / residual: 0 | evidence: btd069
### TS543-R3-C006 [SOL-R3-C006] — 集合 variants → datasets [REPLACE]
- canonical: datasets | meaning: StyleGAN/SVD/FID | before: 10 / residual: 0 | evidence: btd015,btd016,btd075,btd083,btd084
### TS543-R3-C007 [SOL-R3-C007] — 周辺場/標本ごとの条件付き場 → 周辺ベクトル場/条件付きベクトル場 [REPLACE]
- canonical: vector fields | meaning: btd027 L233 | before: 3 / residual: 0 | evidence: btd027
### TS543-R3-C008 [SOL-R3-C008] — 開放重みの混合専門家配置 → 開放重みのMixture-of-Experts（MoE） [REPLACE]
- canonical: Mixture-of-Experts | meaning: L705 | before: 1 / residual: 0 | evidence: btd077,btd124,btd138
### TS543-R3-C009 [SOL-R3-C009] — 一括要点標本 → 高品質動画のサンプリング [REPLACE]
- canonical: video sampling cost | meaning: btd073 L722 | before: 1 / residual: 0 | evidence: btd073
### TS543-R3-C010 [SOL-R3-C010] — 開放凍結 → lifecycle wording [REPLACE]
- canonical: lifecycle | meaning: L1101 | before: 1 / residual: 0 | evidence: btd123,btd126,btd127,btd128
### TS543-R3-C011 [SOL-R3-C011+SOL-CIT-002] — 公開系列の線引き → Wan2.2 boundary+btd124 [REPLACE]
- canonical: Wan2.2 open-weight boundary | meaning: L158 | before: 1 / residual: 0 | evidence: btd124
### TS543-R3-C012 [SOL-R3-C012] — 平滑化/過度の平滑化 → RETAIN [RETAIN]
- canonical: smoothing | meaning: btd028/btd046/btd081 6件 | before: 6 / residual: 6 | evidence: btd028,btd046,btd081
### TS543-R3-C013 [SOL-R3-C013] — 開放線 → 開放重み系 [REPLACE]
- canonical: open-weight lineage | meaning: L39+L688 | before: 2 / residual: 0 | evidence: btd125,btd068
### TS543-R3-C014 [SOL-R3-C014] — Seed-TTS variants → unification [REPLACE]
- canonical: Seed-TTS | meaning: L520+L553+L538 | before: 3 / residual: 0 | evidence: btd061,btd062,btd134
### TS543-R3-S001 [SOL-R3-S001] — 端末間 → End-to-End [REPLACE]
- canonical: End-to-End | meaning: VITS L489+L533 | before: 2 / residual: 0 | evidence: btd056,btd057
### TS543-R3-S002 [SOL-R3-S002] — 区画因果 → chunk-aware causal Flow Matching [REPLACE]
- canonical: chunk-aware causal flow matching | meaning: btd133 | before: 6 / residual: 0 | evidence: btd133
### TS543-R3-S003 [SOL-R3-S003] — 分割残差符号化/神経符号 → split RVQ/ニューラルコーデック符号 [REPLACE]
- canonical: split RVQ / neural codec codes | meaning: btd134+synthesis | before: 6 / residual: 0 | evidence: btd134,btd058
### TS543-R3-S004 [SOL-R3-S004] — 残差12帳/各帳 → RVQコードブック [REPLACE]
- canonical: RVQ codebooks | meaning: btd065/btd066 | before: 2 / residual: 0 | evidence: btd065,btd066
### TS543-R3-S005 [SOL-R3-S005] — 浮動32 → float32 [REPLACE]
- canonical: float32 | meaning: btd064 | before: 1 / residual: 0 | evidence: btd064
### TS543-R3-S006 [SOL-R3-S006] — 声素材/帯域メル/対数メル → audio/mel terminology [REPLACE]
- canonical: audio/mel | meaning: TTS/audio | before: 10 / residual: 0 | evidence: btd052,btd053,btd060,btd064,btd088,btd090
### TS543-R3-S007 [SOL-R3-S007] — 画素再帰網 → PixelRNN/PixelCNN系 [REPLACE]
- canonical: PixelRNN/PixelCNN | meaning: btd017/btd018 | before: 3 / residual: 0 | evidence: btd017,btd018
### TS543-R3-S008 [SOL-R3-S008] — 〜網 → networks [REPLACE]
- canonical: networks | meaning: bound ML contexts | before: 6 / residual: 0 | evidence: btd029,btd064,btd069,btd043
### TS543-R3-S009 [SOL-R3-S009] — 連合学習 → 共同学習 [REPLACE]
- canonical: joint training | meaning: btd070 | before: 5 / residual: 0 | evidence: btd070
### TS543-R3-S010 [SOL-R3-S010] — VDM numbers → FID/IS/FVD [REPLACE]
- canonical: FID/IS/FVD | meaning: btd070 numbers unchanged | before: 6 / residual: 0 | evidence: btd070
### TS543-R3-S011 [SOL-R3-S011] — 振動誘導/整合 → oscillating guidance/CLIP Score/Sampling Time [REPLACE]
- canonical: oscillating guidance/CLIP Score/Sampling Time | meaning: btd071 | before: 8 / residual: 0 | evidence: btd071
### TS543-R3-S012 [SOL-R3-S012] — Make-A-Video numbers → CLIP-FID/CLIPSIM/FVD/IS [REPLACE]
- canonical: CLIP-FID/CLIPSIM/FVD/IS | meaning: btd073 | before: 5 / residual: 0 | evidence: btd073
### TS543-R3-S013 [SOL-R3-S013] — 文章 compounds → テキスト [REPLACE]
- canonical: text modality | meaning: bound list ~30 | before: 30 / residual: 0 | evidence: btd073,btd067,btd069
### TS543-R3-S014 [SOL-R3-S014] — 対照言語音響整合/音響のみ混合 → CLAP/mixup [REPLACE]
- canonical: CLAP/mixup | meaning: btd067 | before: 4 / residual: 0 | evidence: btd067
### TS543-R3-S015 [SOL-R3-S015] — 塗り足し/浅い逆行 → inpainting/shallow reverse [REPLACE]
- canonical: inpainting/shallow reverse | meaning: btd067 | before: 6 / residual: 0 | evidence: btd067
### TS543-R3-S016 [SOL-R3-S016] — joint → 統合/同時生成 [REPLACE]
- canonical: video/audio integration | meaning: capstone | before: 2 / residual: 0 | evidence: btd070,btd071,btd073
### TS543-R3-S017 [SOL-R3-S017] — keyframe → キーフレーム [REPLACE]
- canonical: keyframes | meaning: btd122 | before: 2 / residual: 0 | evidence: btd122
### TS543-R3-S018 [SOL-R3-S018] — reception prose → workflow/dedup [REPLACE]
- canonical: reception prose | meaning: btd139 | before: 3 / residual: 0 | evidence: btd139
### TS543-R3-S019 [SOL-R3-S019] — synthesis residuals → canonical [REPLACE]
- note: L1158 media-list frame→フレーム applied late in r5 pass (same mapping; before total 4)
- canonical: synthesis | meaning: conclusion | before: 3 / residual: 0 | evidence: btd002
### TS543-R3-S020 [SOL-R3-S020] — product/lifecycle → canonical [REPLACE]
- canonical: product/lifecycle | meaning: capstone | before: 6 / residual: 0 | evidence: btd106,btd121,btd122
### TS543-R3-CIT001 [SOL-CIT-001] — DAC binding → btd008 [REPLACE]
- canonical: citation | meaning: maintained from r8 | before: 1 / residual: 0 | evidence: btd008,btd007
### TS543-R3-CIT002 [SOL-CIT-002] — Wan2.2 binding → btd124 [REPLACE]
- canonical: citation | meaning: L158 | before: 1 / residual: 0 | evidence: btd124

# r4 supplement — Sol r9-candidate resolution (same Human r9 authority, DRAFT_COMPLETE continuation)

r4 rows: 23 with provenance SOL_AUTHORITATIVE_R4_R9_CONTINUATION (discovery_source SOL_R9_R4_RESOLUTION).
No new Human revision (no r10). Same-source grammatical variants per r4 s4 only. Numbers/units unchanged (kanji->arabic numerals per map: 二兆->2兆, 四層->4層, values preserved). Citations: no change (SOL-CIT-001/002 only).
## Summary (all rows)
- ISSUE_SEED / REPLACE: 43
- ISSUE_SEED / RETAIN: 2
- BROAD_SCAN / REPLACE: 37
- BROAD_SCAN / RETAIN: 8
- SOL_MAP_R2 / REPLACE: 52
- SOL_FINAL_RESIDUAL_R3 / REPLACE: 35
- SOL_FINAL_RESIDUAL_R3 / RETAIN: 1
- SOL_R9_R4_RESOLUTION / REPLACE: 23
- SOL_R9_R5_RESOLUTION / REPLACE: 6
- SOL_R9_R6_RESOLUTION / REPLACE: 1
- SOL_R10_R7_INDEPENDENT_FULLSCAN / REPLACE: 49
- ESCALATE: 0

### TS543-R4-C001 [SOL-R4-C001] — 文章事前分布 → テキスト由来の事前分布 [REPLACE]
- canonical: text prior (VITS) | meaning: btd056 L456 | before: 1 / residual: 0 | evidence: btd056
### TS543-R4-C002 [SOL-R4-C002] — 文章精緻化層 → ConvNeXtによるテキスト表現精緻化 [REPLACE]
- canonical: ConvNeXt text-feature refinement (F5-TTS) | meaning: btd132 L476+L509+L511 | before: 3 / residual: 0 | evidence: btd132
### TS543-R4-C003 [SOL-R4-C003] — 文章接頭辞 → Inner Monologue wording [REPLACE]
- canonical: time-aligned text prefix (Moshi) | meaning: btd134 L518 | before: 1 / residual: 0 | evidence: btd134
### TS543-R4-C004 [SOL-R4-C004] — 文章と音楽の整合 → テキスト・音楽整合 [REPLACE]
- canonical: text-music alignment | meaning: L559 | before: 1 / residual: 0 | evidence: btd063,btd065
### TS543-R4-C005 [SOL-R4-C005] — 結合音楽文章符号 → MuLanのテキスト・音楽共同埋め込み [REPLACE]
- canonical: MuLan joint embedding | meaning: L563+L569+L604 | before: 3 / residual: 0 | evidence: btd063,btd065
### TS543-R4-C006 [SOL-R4-C006] — 文章側 → テキスト側のMuLan埋め込み [REPLACE]
- canonical: text-side MuLan | meaning: L573 | before: 1 / residual: 0 | evidence: btd065
### TS543-R4-C007 [SOL-R4-C007] — 文章クロスアテンション → テキストクロスアテンション [REPLACE]
- canonical: text cross-attention | meaning: L580+L605 | before: 2 / residual: 0 | evidence: btd066
### TS543-R4-C008 [SOL-R4-C008] — 文章のみ → テキストのみ [REPLACE]
- canonical: text-only (MusicGen) | meaning: L580 | before: 1 / residual: 0 | evidence: btd066
### TS543-R4-C009 [SOL-R4-C009] — 文章と音響の整合間隙 → テキスト・音響整合のギャップ [REPLACE]
- canonical: text-audio gap | meaning: L595 | before: 1 / residual: 0 | evidence: btd067
### TS543-R4-C010 [SOL-R4-C010] — 文章と拍と和音 → テキスト・拍・和音へ [REPLACE]
- canonical: text-beat-chord | meaning: L613+L617 | before: 2 / residual: 0 | evidence: btd069
### TS543-R4-C011 [SOL-R4-C011] — 三軸 → text alignment/domain similarity/motion smoothness [REPLACE]
- canonical: AnimateDiff axes | meaning: L753+L759 | before: 2 / residual: 0 | evidence: btd074
### TS543-R4-C012 [SOL-R4-C012] — 文章拡張 → prompt extension [REPLACE]
- canonical: prompt extension (Wan2.2) | meaning: L804 | before: 1 / residual: 0 | evidence: btd124
### TS543-R4-C013 [SOL-R4-C013] — 動画文章/画像文章 → ペア [REPLACE]
- canonical: video-text/image-text pairs | meaning: L822 | before: 2 / residual: 0 | evidence: btd071
### TS543-R4-C014 [SOL-R4-C014] — 文章と画像の条件付け → テキスト・画像条件付け [REPLACE]
- canonical: text-image conditioning | meaning: L926 | before: 1 / residual: 0 | evidence: btd081
### TS543-R4-C015 [SOL-R4-C015] — 文章映像 → テキスト・動画 [REPLACE]
- canonical: text-video (VBench) | meaning: L995 | before: 1 / residual: 0 | evidence: btd092
### TS543-R4-C016 [SOL-R4-C016] — SentencePiece指示/濃密地図 → rewrite [REPLACE]
- canonical: Unified-IO tokens | meaning: L1026 | before: 1 / residual: 0 | evidence: btd094
### TS543-R4-C017 [SOL-R4-C017] — 往復 umbrella → 双方向変換 [REPLACE]
- canonical: speech-text bidirectional (AudioPaLM) | meaning: L1023+L1028+L1029+L1039+L1054 | before: 8 / residual: 0 | evidence: btd095
### TS543-R4-C018 [SOL-R4-C018] — 画像文章 → 画像・テキスト [REPLACE]
- canonical: image-text tasks | meaning: L1038+L1054+L1026 | before: 3 / residual: 0 | evidence: btd094
### TS543-R4-C019 [SOL-R4-C019] — 文章橋渡し → split by source [REPLACE]
- canonical: text-centric alignment / bridging alignment | meaning: L1040+L1050 | before: 5 / residual: 0 | evidence: btd096,btd097
### TS543-R4-C020 [SOL-R4-C020] — 二兆文章トークン → 2兆テキストトークン [REPLACE]
- canonical: two-trillion text tokens | meaning: L1050 | before: 3 / residual: 0 | evidence: btd096
### TS543-R4-C021 [SOL-R4-C021] — 文章音声/映像音声 → テキスト・音声/動画・音声 [REPLACE]
- canonical: text-audio/video-audio pairs | meaning: L1050 | before: 9 / residual: 0 | evidence: btd097
### TS543-R4-C022 [SOL-R4-C022] — 四者リスト → テキスト・音声・画像・動画 [REPLACE]
- canonical: modality list (Suno) | meaning: L1095 | before: 1 / residual: 0 | evidence: btd114
### TS543-R4-C023 [SOL-R4-C023] — 対照の文章・音響間隙 → 対照学習におけるギャップ [REPLACE]
- canonical: contrastive text-audio gap | meaning: L697 | before: 1 / residual: 0 | evidence: btd067

# r5 supplement — Sol r9-next resolution (same Human r9 authority, DRAFT_COMPLETE continuation)

r5 rows: 6 with provenance SOL_AUTHORITATIVE_R5_R9_CONTINUATION (discovery_source SOL_R9_R5_RESOLUTION).
No new Human revision (no r10). r9-next.md retained as provenance. Citations: no change (SOL-CIT-001/002 only).
## Summary (all rows)
- ISSUE_SEED / REPLACE: 43
- ISSUE_SEED / RETAIN: 2
- BROAD_SCAN / REPLACE: 37
- BROAD_SCAN / RETAIN: 8
- SOL_MAP_R2 / REPLACE: 52
- SOL_FINAL_RESIDUAL_R3 / REPLACE: 35
- SOL_FINAL_RESIDUAL_R3 / RETAIN: 1
- SOL_R9_R4_RESOLUTION / REPLACE: 23
- SOL_R9_R5_RESOLUTION / REPLACE: 6
- SOL_R9_R6_RESOLUTION / REPLACE: 1
- SOL_R10_R7_INDEPENDENT_FULLSCAN / REPLACE: 49
- ESCALATE: 0

### TS543-R5-N001 [SOL-R5-N001] — 文章と音楽の対応 → テキスト・音楽整合 [REPLACE]
- canonical: text-music alignment | meaning: L563 | before: 1 / residual: 0 | evidence: btd063,btd065
### TS543-R5-N002 [SOL-R5-N002] — LibriSpeech sentence → prescribed wording [REPLACE]
- canonical: corpus text resources | meaning: L992 | before: 2 / residual: 0 | evidence: btd089
### TS543-R5-N003 [SOL-R5-N003] — 発話音声と文章のみ → 音声とテキストのみ [REPLACE]
- canonical: speech-and-text-only | meaning: L1029+L1039+L1071 | before: 3 / residual: 0 | evidence: btd095
### TS543-R5-N004 [SOL-R5-N004] — 文章はOPTIMUS → テキスト系はOPTIMUS [REPLACE]
- canonical: CoDi text branch | meaning: L1050 | before: 1 / residual: 0 | evidence: btd097
### TS543-R5-N005 [SOL-R5-N005] — 文章透かし → テキスト向けSynthID [REPLACE]
- canonical: text watermarking | meaning: L1053 | before: 1 / residual: 0 | evidence: btd099
### TS543-R5-N006 [SOL-R5-N006] — 文章・画像起点 → テキスト・画像入力 [REPLACE]
- canonical: text-image inputs | meaning: L1101 | before: 1 / residual: 0 | evidence: btd122
# r6 supplement — Sol r9-next2 resolution (same Human r9 authority, DRAFT_COMPLETE continuation)

r6 rows: 1 with provenance SOL_AUTHORITATIVE_R6_R9_CONTINUATION (discovery_source SOL_R9_R6_RESOLUTION).
No new Human revision (no r10). r9-next2.md retained as provenance. Citations: no change (SOL-CIT-001/002 only).
## Summary (all rows)
- ISSUE_SEED / REPLACE: 43
- ISSUE_SEED / RETAIN: 2
- BROAD_SCAN / REPLACE: 37
- BROAD_SCAN / RETAIN: 8
- SOL_MAP_R2 / REPLACE: 52
- SOL_FINAL_RESIDUAL_R3 / REPLACE: 35
- SOL_FINAL_RESIDUAL_R3 / RETAIN: 1
- SOL_R9_R4_RESOLUTION / REPLACE: 23
- SOL_R9_R5_RESOLUTION / REPLACE: 6
- SOL_R9_R6_RESOLUTION / REPLACE: 1
- SOL_R10_R7_INDEPENDENT_FULLSCAN / REPLACE: 49
- ESCALATE: 0

### TS543-R6-N2-001 [SOL-R6-N2-001] — joint化 → 音声・映像の同時生成 [REPLACE]
- canonical: audio-video joint generation | meaning: L1098+L1113 | before: 2 / residual: 0 | evidence: btd076,btd139

# r7 supplement — Sol final independent fullscan (Human r10 authority, DRAFT_COMPLETE)

r7 rows: 49 with provenance SOL_AUTHORITATIVE_R7_FINAL_FULLSCAN (discovery_source SOL_R10_R7_INDEPENDENT_FULLSCAN; map records SOL_FINAL_INDEPENDENT_R7).
No new Human revision beyond r10. Citations: SOL-CIT-003/004 applied context-bound; CIT-001/002 preserved.

### TS543-R7-T01a [SOL-R7-T01] — 文条件づけ → テキスト条件づけ [REPLACE]
- canonical: text conditioning | meaning: conditioning btd005/btd011/btd032 | before: 6 / residual: 0 | evidence: btd005,btd011,btd032

### TS543-R7-T01b [SOL-R7-T01] — 大規模な文条件づけ → 大規模なテキスト条件づけ [REPLACE]
- canonical: large-scale text conditioning | meaning: DALLE btd005 | before: 2 / residual: 0 | evidence: btd005

### TS543-R7-T01c [SOL-R7-T01] — 文条件 → テキスト条件 [REPLACE]
- canonical: text condition | meaning: guidance btd032 | before: 2 / residual: 0 | evidence: btd032

### TS543-R7-T01d [SOL-R7-T01] — 文条件超解像/文条件生成/文条件転移 → テキスト条件付き超解像/テキスト条件生成/テキスト条件への転移 [REPLACE]
- canonical: text-conditioned SR/generation/transfer | meaning: btd011/btd025/btd027 | before: 4 / residual: 0 | evidence: btd011,btd025,btd027

### TS543-R7-T01e [SOL-R7-T01] — 文誘導拡散 → テキスト誘導拡散 [REPLACE]
- canonical: text-guided diffusion | meaning: CFG btd032/btd033 | before: 3 / residual: 0 | evidence: btd032,btd033

### TS543-R7-T01f [SOL-R7-T01] — 文ドロップアウト → テキスト条件ドロップアウト [REPLACE]
- canonical: text-conditioning dropout | meaning: btd011/btd038 | before: 2 / residual: 0 | evidence: btd011,btd038

### TS543-R7-T01g [SOL-R7-T01] — 空文割合 → 空テキスト条件の割合 [REPLACE]
- canonical: empty text-condition rate | meaning: CFG btd032/btd033 | before: 2 / residual: 0 | evidence: btd032,btd033

### TS543-R7-T01h [SOL-R7-T01] — 文整合 → テキスト整合 [REPLACE]
- canonical: text-image alignment | meaning: btd005/btd011/btd032/btd042 | before: 6 / residual: 0 | evidence: btd005,btd011,btd032,btd042

### TS543-R7-T01i [SOL-R7-T01] — 文への従順さ/文有用性 → テキスト条件への追従性/テキスト条件の有用性 [REPLACE]
- canonical: text adherence/conditional usefulness | meaning: induction btd011/btd032 | before: 2 / residual: 0 | evidence: btd011,btd032

### TS543-R7-T01j [SOL-R7-T01] — 凍結大規模文符号器/大規模文符号器 → 凍結大規模テキストエンコーダ (+eDiff rewrite) [REPLACE]
- canonical: frozen/large text encoders | meaning: CLIP/eDiff-I | before: 3 / residual: 0 | evidence: btd031,btd034

### TS543-R7-T01k [SOL-R7-T01] — 文符号器 (technical) → テキストエンコーダ [REPLACE]
- canonical: text encoder | meaning: eDiff/CLAP/T2I | before: 4 / residual: 0 | evidence: btd034,btd035,btd041

### TS543-R7-T01l [SOL-R7-T01] — 文のみ条件 → テキストのみの条件 [REPLACE]
- canonical: text-only condition | meaning: IP-Adapter btd038 | before: 2 / residual: 0 | evidence: btd038

### TS543-R7-T01m [SOL-R7-T01/A01] — 文能力 → テキストプロンプト能力 (A01 prevails in btd038; T01 generic unneeded) [REPLACE]
- canonical: text(-prompt) capability | meaning: IP-Adapter btd038 | before: 4 / residual: 0 | evidence: btd038

### TS543-R7-T01n [SOL-R7-T01/A01] — 文枝/文類似 → テキスト枝/テキスト類似度 [REPLACE]
- canonical: text branch/similarity | meaning: IP-Adapter/DreamBooth | before: 7 / residual: 0 | evidence: btd038,btd039

### TS543-R7-T01o [SOL-R7-T01] — 文品質 → テキスト記述の品質 [REPLACE]
- canonical: text quality (CLAP) | meaning: CLAP btd035 | before: 4 / residual: 0 | evidence: btd035

### TS543-R7-T01p [SOL-R7-T01] — 文から画像/文と画像 → テキストから画像/テキストと画像 [REPLACE]
- canonical: text-to-image/text-image | meaning: DALLE/CFG | before: 7 / residual: 0 | evidence: btd005,btd032,btd033

### TS543-R7-T02a [SOL-R7-T02] — プロンプトテンプレートと集成/埋め込み集成 → プロンプトテンプレートとアンサンブル/埋め込みアンサンブル [REPLACE]
- canonical: prompt-template/embedding ensembling | meaning: CLIP btd031 | before: 4 / residual: 0 | evidence: btd031,btd011

### TS543-R7-T02b [SOL-R7-T02] — joint 空間 (CLIP) → 共同埋め込み空間 [REPLACE]
- canonical: joint embedding space | meaning: CLIP btd031/btd011 | before: 3 / residual: 0 | evidence: btd031,btd011

### TS543-R7-T02c [SOL-R7-T02] — eDiff-I three-encoder wording → T5テキスト、CLIPテキスト、CLIP画像の3種の埋め込みを独立ドロップアウトで条件づける [REPLACE]
- canonical: T5/CLIP-text/CLIP-image embeddings | meaning: eDiff-I btd034 | before: 1 / residual: 0 | evidence: btd034

### TS543-R7-T02d [SOL-R7-T02] — 共有 baseline → 共有ベースライン [REPLACE]
- canonical: shared baseline | meaning: eDiff-I btd034 | before: 1 / residual: 0 | evidence: btd034

### TS543-R7-T02e [SOL-R7-T02] — CLAP encoder/batch wording → prescribed mechanism + 128ペアのバッチ [REPLACE]
- canonical: contrastive audio-text encoders | meaning: CLAP btd035 | before: 3 / residual: 0 | evidence: btd035

### TS543-R7-T02f [SOL-R7-T02] — joint 空間 (CLAP) → 共同マルチモーダル埋め込み空間 [REPLACE]
- canonical: joint multimodal space | meaning: CLAP btd035 | before: 4 / residual: 0 | evidence: btd035

### TS543-R7-T02g [SOL-R7-T02] — 束規模/対規模 → バッチサイズ (1) / 学習ペア数 (4) [REPLACE]
- canonical: batch size/pair count | meaning: CLAP/IP-Adapter | before: 5 / residual: 0 | evidence: btd035,btd038

### TS543-R7-T03a [SOL-R7-T03] — jointly (ML training) → 共同で/共同学習 [REPLACE]
- canonical: joint training | meaning: btd005/btd011/btd031/btd032 | before: 8 / residual: 0 | evidence: btd005,btd011,btd031,btd032

### TS543-R7-T03b [SOL-R7-T03] — jointly (MotionCtrl) → 同時に [REPLACE]
- canonical: simultaneous use | meaning: MotionCtrl btd042 | before: 1 / residual: 0 | evidence: btd042

### TS543-R7-T03c [SOL-R7-T03] — 尺度掃引 → ガイダンススケールのスイープ [REPLACE]
- canonical: guidance-scale sweep | meaning: CFG | before: 2 / residual: 0 | evidence: btd032

### TS543-R7-T03d [SOL-R7-T03] — framing (SDE) → 定式化 forms [REPLACE]
- canonical: formulation | meaning: SDE btd021/btd022 | before: 6 / residual: 0 | evidence: btd021,btd022

### TS543-R7-T03e [SOL-R7-T03] — 単一制御の framing → 単一制御という設定 [REPLACE]
- canonical: single-control setting | meaning: ControlNet btd036 | before: 2 / residual: 0 | evidence: btd036

### TS543-R7-ADa [SOL-R7-§4] — 音響の言語整合と空間制御の適合 → 音響の言語整合と空間制御アダプター [REPLACE]
- canonical: spatial-control adapter | meaning: conditioning intro+heading | before: 2 / residual: 0 | evidence: btd011,btd032,btd036

### TS543-R7-ADb [SOL-R7-§4] — 適合の系譜/適合の形 → アダプター／適応の系譜/拡張・適応の形 [REPLACE]
- canonical: adapter lineage/table | meaning: control §4 | before: 2 / residual: 0 | evidence: btd037,btd038,btd039,btd042

### TS543-R7-ADc [SOL-R7-§4] — 軽量配置適合/画像参照適合 → 軽量制御アダプター（T2I-Adapter）/画像参照アダプター（IP-Adapter） [REPLACE]
- canonical: T2I/IP adapters | meaning: T2I btd041/IP btd038 | before: 4 / residual: 0 | evidence: btd041,btd038

### TS543-R7-ADd [SOL-R7-§4] — 低ランク適合 → Low-Rank Adaptation（LoRA／低ランク適応） [REPLACE]
- canonical: Low-Rank Adaptation | meaning: LoRA btd040 | before: 5 / residual: 0 | evidence: btd040

### TS543-R7-ADe [SOL-R7-§4] — 多適合/適合規模/参照適合/空間適合 → 複数アダプター/アダプター規模/参照アダプター/空間制御アダプター [REPLACE]
- canonical: adapter scale/reference/spatial | meaning: control §4 | before: 15 / residual: 0 | evidence: btd037,btd038,btd041

### TS543-R7-ADf [SOL-R7-§4] — 動作適合/制御適合/効率適合 → モーション制御/制御アダプター/効率的な適応 [REPLACE]
- canonical: motion/control/efficient adaptation | meaning: video/music/LoRA | before: 5 / residual: 0 | evidence: btd038,btd043,btd040,btd006

### TS543-R7-C01 [SOL-R7-C01] — 微小条件符号器 → 条件入力を潜在解像度へ写像する小規模畳み込みネットワーク [REPLACE]
- canonical: small condition-input convnet | meaning: ControlNet btd036 | before: 1 / residual: 0 | evidence: btd036

### TS543-R7-C02 [SOL-R7-C02] — 零畳み込み/零から育てる → zero convolution（ゼロ畳み込み）/ゼロ初期化された重みから学習する [REPLACE]
- canonical: zero conv / zero-init growth | meaning: ControlNet btd036/btd043 | before: 6 / residual: 0 | evidence: btd036,btd043

### TS543-R7-C03 [SOL-R7-C03] — 類別 family → タスクプロンプトとクラスラベル/時刻とクラス/クラス条件を超えるテキスト条件 [REPLACE]
- canonical: class labels | meaning: diffusion/class | before: 3 / residual: 0 | evidence: btd012,btd030,btd032

### TS543-R7-AUD [SOL-R7-AUD01] — 群衆方式/聴取得点 → クラウドソーシングによる聴取評価/主観聴取評価スコア [REPLACE]
- canonical: crowdsourced listening | meaning: codec btd006 | before: 3 / residual: 0 | evidence: btd006

### TS543-R7-M01 [SOL-R7-M01] — 間引き率 → ダウンサンプリング率8・32・128 [REPLACE]
- canonical: downsampling rates | meaning: Jukebox btd063 | before: 1 / residual: 0 | evidence: btd063

### TS543-R7-M02 [SOL-R7-M02] — MusicGen tokenizer sentence → 32 kHzモノラル音声を総ストライド640のEnCodecで、50 Hz・4コードブックの離散トークン列へ符号化し [REPLACE]
- canonical: EnCodec 50Hz/4-codebook | meaning: MusicGen btd066 | before: 1 / residual: 0 | evidence: btd066

### TS543-R7-M03 [SOL-R7-M03] — 拍弦予測/タグのみ文 →  chord mechanism removed; ジャンル・ムード等のグローバルなテキスト条件/タグ条件 [REPLACE]
- canonical: global text + time-varying control | meaning: Music ControlNet btd043 | before: 3 / residual: 0 | evidence: btd043

### TS543-R7-M04 [SOL-R7-M04] — 対照音楽ネットワーク → MuNet（Music-Domain-Knowledge-Informed UNet） [REPLACE]
- canonical: MuNet | meaning: MuSTANGO btd069 | before: 1 / residual: 0 | evidence: btd069

### TS543-R7-M05 [SOL-R7-M05] — 標識三重 → 3種類のラベル情報を持つ楽曲組合せ [REPLACE]
- canonical: triple-labelled pieces | meaning: human-pref btd136 | before: 1 / residual: 0 | evidence: btd136

### TS543-R7-V01 [SOL-R7-V01] — 三次元回転整合/回転整合 → 物体回転中の3D一貫性は厳密ではなく/回転中の3D一貫性 [REPLACE]
- canonical: 3D-consistency limitation | meaning: Imagen btd071 | before: 3 / residual: 0 | evidence: btd071

### TS543-R7-V02 [SOL-R7-V02] — 背骨 family → バックボーン/3種類のバックボーン/バックボーン依存の偏り [REPLACE]
- canonical: backbones | meaning: human-pref/VBench | before: 7 / residual: 0 | evidence: btd087,btd092

### TS543-R7-V03 [SOL-R7-V03] — 自然文区間編集 → 自然言語による区間編集 [REPLACE]
- canonical: NL-based segment edit | meaning: Suno btd115 | before: 1 / residual: 0 | evidence: btd115

### TS543-R7-U09 [SOL-R7-§9] — 金字塔 sentence → 単一Transformerで多様な入出力を離散トークン列へ統一するため、密な予測もトークナイザ／VQ-GANの表現上限に依存する [REPLACE]
- canonical: tokenizer bottleneck | meaning: Unified-IO btd094 | before: 1 / residual: 0 | evidence: btd094

### TS543-R7-CIT3 [SOL-CIT-003] — SPADE claims bound to btd037 → btd041 (bib-verified Park et al.) [REPLACE]
- canonical: SPADE/GauGAN btd041 | meaning: Section 4 | before: 6 / residual: 0 | evidence: btd041

### TS543-R7-CIT4 [SOL-CIT-004] — T2I-Adapter claims bound to btd041 → btd037 (bib-verified Mou et al.; L304 mixed cites both) [REPLACE]
- canonical: T2I-Adapter btd037 | meaning: Section 4 | before: 8 / residual: 0 | evidence: btd037

# r8 supplement — Sol r10-candidate resolution (same Human r10 authority, DRAFT_COMPLETE continuation)

r8 rows: 12 with provenance SOL_AUTHORITATIVE_R8_R10_CONTINUATION (discovery_source SOL_R10_R8_CANDIDATE_RESOLUTION).
No new Human revision (no r11). r10 candidates file retained as provenance. Citations: no change (SOL-CIT-001–004 only); copy-edit 、、 fixed per Sol r8 s4.

### TS543-R8-C001 [SOL-R8-C001] — 条件と誘導と適合と参照 → 四区分の使い分け：条件づけ・ガイダンス・アダプター・参照 [REPLACE]
- canonical: four categories | meaning: conditioning heading L285 | before: 1 / residual: 0 | evidence: 

### TS543-R8-C002 [SOL-R8-C002] — 軽量適合 → 軽量制御アダプター [REPLACE]
- canonical: lightweight adapter (T2I) | meaning: T2I lineage L304/L309/L353 | before: 3 / residual: 0 | evidence: btd037,btd041

### TS543-R8-C003 [SOL-R8-C003] — 画像参照 → SPLIT: enum L304 to 画像参照アダプター; ordinary L290/L327/L353 RETAIN [REPLACE]
- canonical: image reference (IP-Adapter) | meaning: IP-Adapter lineage | before: 1 / residual: 0 | evidence: btd038

### TS543-R8-C004 [SOL-R8-C004] — 適合の視点 → アダプター／適応の視点 [REPLACE]
- canonical: adaptation viewpoint | meaning: control summary L343 | before: 1 / residual: 0 | evidence: 

### TS543-R8-C005 [SOL-R8-C005] — 訓練や反転なしの適合の条件 → 学習・反転不要の編集条件で [REPLACE]
- canonical: training/inversion-free editing | meaning: FiVE btd138 L804 | before: 1 / residual: 0 | evidence: btd138

### TS543-R8-C006 [SOL-R8-C006] — 誘導尺度の掃引 → ガイダンススケールのスイープ [REPLACE]
- canonical: guidance-scale sweep | meaning: CFG btd032 L260 | before: 1 / residual: 0 | evidence: btd032

### TS543-R8-C007 [SOL-R8-C007] — 画像と文 → 画像とテキスト [REPLACE]
- canonical: image and text | meaning: DALLE btd005/CLIP btd031 | before: 2 / residual: 0 | evidence: btd005,btd031

### TS543-R8-C008 [SOL-R8-C008] — 二百五十六トークン以内のバイト対符号化文 → 最大256トークンのBPE符号化テキスト [REPLACE]
- canonical: BPE text tokens | meaning: DALL-E btd005 L138 | before: 1 / residual: 0 | evidence: btd005

### TS543-R8-C009 [SOL-R8-C009] — 文や配置 → テキストやレイアウト [REPLACE]
- canonical: text-or-layout conditioning | meaning: LDM btd023 L225 | before: 2 / residual: 0 | evidence: btd023

### TS543-R8-C010 [SOL-R8-C010] — 文から絵や音を生むとき → テキストから画像や音を生成するとき [REPLACE]
- canonical: rhetorical modality intro | meaning: conditioning intro L247 | before: 1 / residual: 0 | evidence: btd005

### TS543-R8-C011 [SOL-R8-C011] — 稀少識別子と類名詞の文 → 稀少識別子とクラス名詞を含むプロンプト [REPLACE]
- canonical: a [identifier] [class noun] | meaning: DreamBooth btd039 | before: 2 / residual: 0 | evidence: btd039

### TS543-R8-C012 [SOL-R8-C012] — テキスト・画像多層網 → 事前学習済みText-to-Image（T2I）モデルに擬似3D畳み込みと時間方向のアテンション [REPLACE]
- canonical: pretrained T2I + modules | meaning: Make-A-Video btd073 L720 | before: 1 / residual: 0 | evidence: btd073

# r9 supplement — Sol final independent audit (same Human r10 authority, no r11)

r9 rows: 7 with provenance SOL_AUTHORITATIVE_R9_FINAL_AUDIT (discovery_source SOL_R10_R9_FINAL_INDEPENDENT_AUDIT).
No new Human revision. Citations: no change (SOL-CIT-001–004 only); references.bib frozen.

### TS543-R9-C001 [SOL-R9-C001] — 恒等や零初期値 (Make-A-Video init) → 擬似3D畳み込みの時間1D畳み込みを恒等写像で初期化し、時間アテンションの時間方向射影をゼロ初期化 [REPLACE]
- canonical: identity/zero init (btd073) | meaning: Make-A-Video init L720 | before: 1 / residual: 0 | evidence: btd073

### TS543-R9-C002 [SOL-R9-C002] — 空間初期値 family → 事前学習済み画像モデル＋時間層挿入 forms [REPLACE]
- canonical: pretrained spatial layers + temporal insert (SVD) | meaning: SVD btd075 x4 | before: 4 / residual: 0 | evidence: btd075

### TS543-R9-C003 [SOL-R9-C003] — 零初期値残差 → 正弦位置符号化＋ゼロ初期化した出力射影と残差接続 [REPLACE]
- canonical: zero-init output proj + residual (AnimateDiff) | meaning: AnimateDiff btd074 | before: 1 / residual: 0 | evidence: btd074

### TS543-R9-C004 [SOL-R9-C004] — 係数を操作し零で除去 → 推論時の係数を0にすると除去 [REPLACE]
- canonical: scaler 1→0 removal (AnimateDiff DA) | meaning: AnimateDiff btd074 | before: 1 / residual: 0 | evidence: btd074

### TS543-R9-C005 [SOL-R9-C005] — 誤りは零 → 誤りは$0$ (NONSEMANTIC_COPY_EDIT) [REPLACE]
- canonical: zero count (FastSpeech) | meaning: FastSpeech btd060 | before: 1 / residual: 0 | evidence: btd060

### TS543-R9-C006 [SOL-R9-C006] — 難文誤り零 → 難文誤り$0$ (NONSEMANTIC_COPY_EDIT) [REPLACE]
- canonical: zero count table (FastSpeech) | meaning: FastSpeech btd060 table | before: 1 / residual: 0 | evidence: btd060

### TS543-R9-C007 [SOL-R9-C007] — 画像処理装置 (HiFi-GAN) → V100 GPUで$3701$キロヘルツ [REPLACE]
- canonical: V100 GPU | meaning: HiFi-GAN btd055 | before: 1 / residual: 0 | evidence: btd055
