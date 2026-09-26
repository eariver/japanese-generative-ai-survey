# Terminology decision ledger — TS-002 Issue #543 (final broad normalization)

Canonical: `terminology-decision-ledger.json` (88 rows, generated; this MD is a synced view).
Scope: reader-facing terminology only. Blind global replace prohibited; semantic-risk terms verified by primary/Evidence read-back.

## Summary
- ISSUE_SEED decisions: 45
- BROAD_SCAN added candidates: 43
- REPLACE rows: 72
- RETAIN rows: 12
- ESCALATE rows: 4
- Unresolved terms (ESCALATE, text unchanged, returned to Sol): 分類得点 L158 (btd003 IS/精度曖昧); 自然さ得点 L1090/L1108 (vendor MOS束縛未確認); 全帯域抽出 L158 (btd007 sampling/extraction区別に本文要確認); 濾波崩壊×2 (canonical未確定); 膨張形式×1 (mask/format未確定).

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

### TS543-S39c [ISSUE_SEED] — 自然さ得点(vendor) → 自然さ得点(維持) [ESCALATE]
- canonical: MOS? | meaning: ベンダー自然さ2件
- rationale: MOS束縛は原典未確認
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

### TS543-S40c [ISSUE_SEED] — 全帯域抽出 → 全帯域抽出(維持) [ESCALATE]
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

### TS543-B14 [BROAD_SCAN] — 濾波崩壊 → 濾波崩壊(維持) [ESCALATE]
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

### TS543-B33c [BROAD_SCAN] — 膨張形式 → 膨張形式(維持) [ESCALATE]
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

## Frozen regression: #533 (17 terms) + #539 (模型/模型票/U網/波形網/得点網/枠間/民生画像処理装置/文章符号器/交叉注意/交差注意) all remain 0.
## Invariants: autocite 1259 identical; keys 139 identical; labels identical; PARTIAL 12; bib byte-identical. Section titles updated by terminology only (order/count 116 unchanged). Acronym introductions (FID/IS/MOS/SNR) are intended normalizations. Numeric +128 one (百二十八→128, value-preserved).