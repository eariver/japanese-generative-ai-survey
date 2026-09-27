# Terminology decision ledger — TS-002 Issue #539 (second-pass reader-facing normalization)

Canonical: `terminology-decision-ledger.json` (68 rows, generated; this MD is a synced view).
Scope: reader-facing terminology only. Blind global replace prohibited; every occurrence judged source/entity/context-bound.
After-state residuals: 模型 0 / 模型票 0 / 票 0 / U網 0 / 波形網 0 / 得点網 0 / 枠間 0 / 民生画像処理装置 0 / 文章符号器 0 / 交叉注意 0 / 交差注意 0 / 母数 3 (RETAIN) / 案内 6 (RETAIN) / 資料 14 (RETAIN) / 枠 40 (RETAIN).
ESCALATE: 0 rows (no unresolved items).

## Summary counts (before → after, main.tex)
| term | before | after (residual) | disposition |
|---|---|---|---|
| 模型 (ML model系, 票系5件含む総数142) | 142 | 0 | 全件REPLACE→モデル系; 非ML用法なし |
| 模型票 | 4 | 0 | →モデルカード |
| 票 (model-card照応, 模型票4件と別計で11件) | 11 | 0 | →カード系 |
| U網 (U網14件中3件は時刻条件U網と重複) | 14 | 0 | →U-Net / 時刻条件付きU-Net |
| 波形網 | 5 | 0 | →WaveNet (named, btd051) |
| 得点網 | 2 | 0 | →score network（スコアネットワーク）/スコアネットワーク |
| 枠間 | 6 | 0 | →フレーム間 |
| 枠 (frame単位43件 / RETAIN 40件) | 82 | 40 | REPLACE 43→フレーム系; RETAIN 40 |
| 民生画像処理装置 | 5 | 0 | →24GBの民生GPU 1基 / 民生GPU 1基 (数値不変) |
| 文章符号器 | 4 | 0 | →text encoder（テキストエンコーダ）/テキストエンコーダ |
| 交叉注意 21 + 交差注意 5 | 26 | 0 | →cross-attention（クロスアテンション）/クロスアテンション |
| 母数 (ML重み8 / 統計3) | 11 | 3 | REPLACE 8→パラメータ; RETAIN 3 |
| 案内 (guidance 8 / 誘導画像13 / 一般6) | 27 | 6 | REPLACE→ガイダンス/誘導画像; RETAIN 6 |
| 資料 (データ系72 / 典拠14) | 86 | 14 | REPLACE 72→データ系; RETAIN 14 |

## Decisions
### TS539-A01 — 言語模型 → 言語モデル [REPLACE]
- canonical source term: language model
- meaning: ML言語モデル
- rationale: 全件ML sense; 検索性のためカタカナへ
- substitutions: 言語模型→言語モデル ×23
- occurrences: L145, L155, L197, L403, L405, L433, L441, L443, L476, L478, L497, L499, L509, L511, L516, L521, L523, L534, L992, L1023, L1026, L1053, L1071
- sections: L1017 \section{収束問題：統合モデルか連携する専門家群か}; L1025 \subsection{課題別頭部を持たない多課題統合の射程}; L1052 \subsection{来歴機構の頁限定と開かれた問い}; L142 \subsection{音の残差量子化：低速度と遅延の両立}; L152 \subsection{三軸のまとめ：何を削り何を残したか}; L194 \subsection{完全自己回帰：画素の同時分布を捉える}; L402 \subsection{指示追従学習と一段階動画編集：手続きの隠蔽と時間への拡張}; L432 \subsection*{読解上の境界}; L435 \section{音声・声の系譜：波形からEnd-to-End、ニューラルコーデック言語モデル、全二重へ}\sectionkicker{SPEECH}\labe; L475 \subsection{何を何で表すか：言語・意味・音響・符号・波形の分担}; L496 \subsection{ゼロショット話者複製とニューラルコーデック言語モデル：未知話者への拡張}; L508 \subsection{流れ補完と実時間化：非自己回帰と前後文脈の統一}; L515 \subsection{因果性と遅延と全二重：速さと同時性の分離}; L520 \subsection{Seed-TTS（多用途・高忠実音声生成）・翻訳・全二重対話：実環境と遅延の両立}; L991 \subsection{耳と話し言葉の土台を切り分ける}
- evidence: btd006, btd007, btd008, btd005, btd009
- before: 23 / residual original: 0

### TS539-A02 — 言語模型化 → 言語モデル化 [REPLACE]
- canonical source term: language-model-ization
- meaning: 残差符号等の言語モデル化
- rationale: A01の言語模型23件に包含; 正味は表記統一のみ
- substitutions: 言語模型化→言語モデル化 ×2
- occurrences: L441, L534
- sections: L435 \section{音声・声の系譜：波形からEnd-to-End、ニューラルコーデック言語モデル、全二重へ}\sectionkicker{SPEECH}\labe; L520 \subsection{Seed-TTS（多用途・高忠実音声生成）・翻訳・全二重対話：実環境と遅延の両立}
- evidence: btd051, btd052, btd053, btd054, btd055
- before: 2 / residual original: 0

### TS539-A03 — 模型化(一般) → モデル化 [REPLACE]
- canonical source term: modeling
- meaning: 音響のみ/並列/表頭のmodeling 3件
- rationale: 言語模型化を除く残り; 定着表記モデル化
- substitutions: 音響のみの模型化→音響のみのモデル化 ×1; 並列に模型化→並列にモデル化 ×1; 何を模型化→何をモデル化 ×1
- occurrences: L158, L484, L518
- sections: L157 \subsection{本節の読解上の境界}; L475 \subsection{何を何で表すか：言語・意味・音響・符号・波形の分担}; L515 \subsection{因果性と遅延と全二重：速さと同時性の分離}
- evidence: btd006, btd008, btd001, btd004, btd002, btd134
- before: 3 / residual original: 0

### TS539-A04 — 生成模型 → 生成モデル [REPLACE]
- canonical source term: generative model
- meaning: 直接予測対象の生成モデル (内2件はA05有向生成模型と重複計上)
- rationale: ML sense
- substitutions: 生成模型→生成モデル ×3
- occurrences: L106, L110, L114
- sections: L100 \section{表現と圧縮：生成可能にする短縮の歴史}; L113 \subsection{連続潜在から離散符号へ：推論の償却化と量子化}
- evidence: btd001, btd002, btd003, btd004, btd005
- before: 3 / residual original: 0

### TS539-A05 — 有向生成模型 → 有向生成モデル [REPLACE]
- canonical source term: directed generative model
- meaning: 連続潜在の有向生成モデル(VAE系譜)
- rationale: ML sense
- substitutions: 有向生成模型→有向生成モデル ×2
- occurrences: L110, L114
- sections: L100 \section{表現と圧縮：生成可能にする短縮の歴史}; L113 \subsection{連続潜在から離散符号へ：推論の償却化と量子化}
- evidence: btd001, btd002, btd003, btd004, btd005
- before: 2 / residual original: 0

### TS539-A06 — 拡散模型 → 拡散モデル [REPLACE]
- canonical source term: diffusion model
- meaning: 拡散モデル (内1件はA08基盤拡散模型と重複計上)
- rationale: ML sense
- substitutions: 拡散模型→拡散モデル ×5
- occurrences: L168, L213, L363, L367, L405
- sections: L160 \section{生成パラダイムと目的関数：自己回帰・敵対・拡散・フロー}; L212 \subsection{雑音除去の転換：拡散と短縮抽出}; L355 \section{生成から編集へ：保存を伴う改変の系譜}\sectionkicker{EDITING}\label{sec:editing}; L366 \subsection{部分拡散とマスク合成：再学習なしの保存手続き}; L402 \subsection{指示追従学習と一段階動画編集：手続きの隠蔽と時間への拡張}
- evidence: btd013, btd014, btd015, btd016, btd017
- before: 5 / residual original: 0

### TS539-A07 — 基盤模型 → 基盤モデル [REPLACE]
- canonical source term: foundation model
- meaning: 基盤モデル2件
- rationale: ML sense
- substitutions: 基盤模型→基盤モデル ×2
- occurrences: L385, L405
- sections: L380 \subsection{注意写像と最適化編集：内部表現を界面にする}; L402 \subsection{指示追従学習と一段階動画編集：手続きの隠蔽と時間への拡張}
- evidence: btd047, btd048, btd049, btd050
- before: 2 / residual original: 0

### TS539-A08 — 基盤拡散模型 → 基盤拡散モデル [REPLACE]
- canonical source term: base diffusion model
- meaning: 基盤拡散モデル1件
- rationale: ML sense
- substitutions: 基盤拡散模型→基盤拡散モデル ×1
- occurrences: L405
- sections: L402 \subsection{指示追従学習と一段階動画編集：手続きの隠蔽と時間への拡張}
- evidence: btd049, btd050
- before: 1 / residual original: 0

### TS539-A09 — 認識模型 → 認識モデル [REPLACE]
- canonical source term: recognition model
- meaning: VAE認識モデル3件
- rationale: ML sense
- substitutions: 認識模型→認識モデル ×3
- occurrences: L114, L129
- sections: L113 \subsection{連続潜在から離散符号へ：推論の償却化と量子化}; L118 \subsection{階層と知覚：高解像度への二つの道}
- evidence: btd001
- before: 3 / residual original: 0

### TS539-A10 — 持続長模型 → 持続長モデル [REPLACE]
- canonical source term: duration model
- meaning: 音素持続長モデル3件
- rationale: ML sense
- substitutions: 持続長模型→持続長モデル ×3
- occurrences: L476, L509, L511
- sections: L475 \subsection{何を何で表すか：言語・意味・音響・符号・波形の分担}; L508 \subsection{流れ補完と実時間化：非自己回帰と前後文脈の統一}
- evidence: btd051, btd052, btd053, btd054, btd055
- before: 3 / residual original: 0

### TS539-A11 — 判定模型 → 判定モデル [REPLACE]
- canonical source term: (LLM-as-)judge model
- meaning: 評価器としての判定モデル3件
- rationale: source-bound: judgeのため分類モデル不採用
- substitutions: 判定模型→判定モデル ×3
- occurrences: L832, L864, L867
- sections: L826 \section{長時間・同期・編集：標本の鮮明さを超える時間軸}; L863 \subsection{多ターン対話の区切り手順と逓減の記録}; L866 \subsection{単発の主張を長時間の証拠に格上げしない}
- evidence: btd131, btd135, btd129, btd130
- before: 3 / residual original: 0

### TS539-A12 — 模型判定 → モデル判定 [REPLACE]
- canonical source term: model-based judgment
- meaning: モデルによる判定3件
- rationale: judge依存
- substitutions: 模型判定→モデル判定 ×3
- occurrences: L864, L867, L889
- sections: L863 \subsection{多ターン対話の区切り手順と逓減の記録}; L866 \subsection{単発の主張を長時間の証拠に格上げしない}
- evidence: btd135, btd131, btd129, btd130
- before: 3 / residual original: 0

### TS539-A13 — 模型依存 → モデル依存 [REPLACE]
- canonical source term: model dependence
- meaning: モデル依存2件(L832はA11と重複計上)
- rationale: ML sense; L832重複はA11/BT系譜と同一箇所
- substitutions: 模型依存→モデル依存 ×2
- occurrences: L832, L995
- sections: L826 \section{長時間・同期・編集：標本の鮮明さを超える時間軸}; L994 \subsection{映像の多次元化と単一値の拒否}
- evidence: btd131, btd135, btd129, btd130, btd092
- before: 2 / residual original: 0

### TS539-A14 — 選好模型 → 選好モデル [REPLACE]
- canonical source term: preference model
- meaning: 選好モデル1件
- rationale: ML sense
- substitutions: 選好模型→選好モデル ×1
- occurrences: L971
- sections: L970 \subsection{人手選好を公開資産化する手順と母集団の天井}
- evidence: btd087
- before: 1 / residual original: 0

### TS539-A15 — 潜在整合模型 → 潜在整合モデル [REPLACE]
- canonical source term: Latent Consistency Model
- meaning: LCM蒸留2件
- rationale: #533凍結の流れ整合/整流流れとは別概念
- substitutions: 潜在整合模型→潜在整合モデル ×2
- occurrences: L898, L904
- sections: L892 \section{実行と配備：サンプリング・遅延・記憶・公開性}; L903 \subsection{潜在整合蒸留と低負担のLoRA化}
- evidence: btd078, btd079, btd080, btd081, btd082
- before: 2 / residual original: 0

### TS539-A16 — 尤度模型系 → 尤度モデル [REPLACE]
- canonical source term: likelihood model
- meaning: 他尤度モデル1件
- rationale: ML sense
- substitutions: 尤度模型→尤度モデル ×1
- occurrences: L239
- sections: L238 \subsection{本節の読解上の境界}
- evidence: btd013, btd014, btd015, btd016, btd019
- before: 1 / residual original: 0

### TS539-A17 — スコア模型 → スコアモデル [REPLACE]
- canonical source term: (learned) score model
- meaning: 学習済みスコアモデル1件
- rationale: 得点網→スコアネットワークと整合
- substitutions: スコア模型→スコアモデル ×1
- occurrences: L367
- sections: L366 \subsection{部分拡散とマスク合成：再学習なしの保存手続き}
- evidence: btd044, btd045
- before: 1 / residual original: 0

### TS539-A18 — 多能高忠実模型 → 多能高忠実モデル [REPLACE]
- canonical source term: versatile high-fidelity model
- meaning: 多能高忠実モデル4件
- rationale: #533凍結「多能模型」とは別文字列
- substitutions: 多能高忠実模型→多能高忠実モデル ×4
- occurrences: L441, L521, L523, L544
- sections: L435 \section{音声・声の系譜：波形からEnd-to-End、ニューラルコーデック言語モデル、全二重へ}\sectionkicker{SPEECH}\labe; L520 \subsection{Seed-TTS（多用途・高忠実音声生成）・翻訳・全二重対話：実環境と遅延の両立}
- evidence: btd051, btd052, btd053, btd054, btd055
- before: 4 / residual original: 0

### TS539-A19 — 個人化模型系 → 個人化モデル [REPLACE]
- canonical source term: personalized model
- meaning: 個人化/画像/同一 計8件
- rationale: ML sense
- substitutions: 個人化模型→個人化モデル ×5; 個人化画像模型→個人化画像モデル ×2; 同一個人化模型→同一の個人化モデル ×1
- occurrences: L705, L722, L753, L755, L759, L807, L822
- sections: L699 \section{映像の系譜：時間的一貫性からメディア基盤へ}\sectionkicker{VIDEO}\label{sec:video}; L719 \subsection{資料効率化：外観凍結と運動学習の分離}; L752 \subsection{動作接続器と厳選潜在動画：個人化の動作化と段階学習}; L803 \subsection{参照・条件づけ・編集と基準測定の配置}; L821 \subsection*{読解上の境界}
- evidence: btd073, btd074, btd075, btd124, btd070, btd071
- before: 8 / residual original: 0

### TS539-A20 — 対象画像模型 → 対象画像モデル [REPLACE]
- canonical source term: subject-image model
- meaning: 対象画像モデル2件
- rationale: ML sense
- substitutions: 対象画像模型→対象画像モデル ×2
- occurrences: L409, L433
- sections: L402 \subsection{指示追従学習と一段階動画編集：手続きの隠蔽と時間への拡張}; L432 \subsection*{読解上の境界}
- evidence: btd050, btd044, btd045, btd046, btd047
- before: 2 / residual original: 0

### TS539-A21 — 独立学習模型 → 独立学習モデル [REPLACE]
- canonical source term: independently-trained model
- meaning: IS参照モデル2件
- rationale: ML sense
- substitutions: 独立学習模型→独立学習モデル ×2
- occurrences: L965, L1014
- sections: L964 \subsection{分布類似の起点を本文境界付きで押さえる}; L994 \subsection{映像の多次元化と単一値の拒否}
- evidence: btd083, btd084
- before: 2 / residual original: 0

### TS539-A22 — 統合模型 → 統合モデル [REPLACE]
- canonical source term: unified model
- meaning: 統合モデル2件
- rationale: ML sense
- substitutions: 統合模型→統合モデル ×2
- occurrences: L775, L1023
- sections: L1017 \section{収束問題：統合モデルか連携する専門家群か}; L774 \subsection{閉鎖頂点・開放混合専門家と編集基準測定：基盤への到達}
- evidence: btd077, btd124, btd094, btd097, btd095
- before: 2 / residual original: 0

### TS539-A23 — 凍結模型系 → 凍結モデル [REPLACE]
- canonical source term: frozen model
- meaning: 凍結/凍結画像モデル5件
- rationale: ML sense
- substitutions: 凍結模型→凍結モデル ×4; 凍結画像模型→凍結画像モデル ×1
- occurrences: L304, L753, L1023, L1050
- sections: L1017 \section{収束問題：統合モデルか連携する専門家群か}; L1049 \subsection{構造不変の資料側工夫と合成拡散の対比}; L298 \section{制御と参照：空間・参照・主体性の保存}; L752 \subsection{動作接続器と厳選潜在動画：個人化の動作化と段階学習}
- evidence: btd037, btd039, btd042, btd094, btd097, btd075
- before: 5 / residual original: 0

### TS539-A24 — 実時間模型系 → 実時間モデル [REPLACE]
- canonical source term: real-time model
- meaning: 実時間モデル (内1件は開放型実時間模型と重複計上) + 開放型1件
- rationale: ML sense
- substitutions: 実時間模型→実時間モデル ×2; 開放型実時間模型→開放型実時間モデル ×1
- occurrences: L509
- sections: L508 \subsection{流れ補完と実時間化：非自己回帰と前後文脈の統一}
- evidence: btd060, btd132, btd133
- before: 3 / residual original: 0

### TS539-A25 — 音響言語模型 → 音響言語モデル [REPLACE]
- canonical source term: audio language model
- meaning: 音響言語モデル2件
- rationale: ML sense
- substitutions: 音響言語模型→音響言語モデル ×2
- occurrences: L155, L197
- sections: L152 \subsection{三軸のまとめ：何を削り何を残したか}; L194 \subsection{完全自己回帰：画素の同時分布を捉える}
- evidence: btd005, btd009, btd010, btd004, btd006
- before: 2 / residual original: 0

### TS539-A26 — 遅延模型 → 遅延モデル [REPLACE]
- canonical source term: delay(-pattern) model
- meaning: 遅延内訳モデル1件
- rationale: ML sense
- substitutions: 遅延模型→遅延モデル ×1
- occurrences: L516
- sections: L515 \subsection{因果性と遅延と全二重：速さと同時性の分離}
- evidence: btd060, btd133, btd132, btd062, btd134
- before: 1 / residual original: 0

### TS539-A27 — 専門模型 → 専門モデル [REPLACE]
- canonical source term: domain-specialist model
- meaning: 専門モデル1件
- rationale: ML sense
- substitutions: 専門模型→専門モデル ×1
- occurrences: L140
- sections: L137 \subsection{文と画像の単一列：大規模条件づけの前の短縮}
- evidence: btd005, btd002
- before: 1 / residual original: 0

### TS539-A28 — 膨張模型 → 膨張モデル [REPLACE]
- canonical source term: dilated(-attention) model
- meaning: 膨張モデル1件
- rationale: ML sense
- substitutions: 膨張模型→膨張モデル ×1
- occurrences: L777
- sections: L774 \subsection{閉鎖頂点・開放混合専門家と編集基準測定：基盤への到達}
- evidence: btd138
- before: 1 / residual original: 0

### TS539-A29 — 模型毎 → モデル毎 [REPLACE]
- canonical source term: per-model
- meaning: モデル毎5件
- rationale: ML sense
- substitutions: 模型毎→モデル毎 ×5
- occurrences: L904, L953, L968, L1014
- sections: L903 \subsection{潜在整合蒸留と低負担のLoRA化}; L931 \subsection{機材の天井を押さえる独立計測}; L967 \subsection{全体点から分離診断への移動}; L994 \subsection{映像の多次元化と単一値の拒否}
- evidence: btd079, btd080, btd085, btd086
- before: 5 / residual original: 0

### TS539-A30 — 模型表 → モデル表 [REPLACE]
- canonical source term: model (score) table
- meaning: 未消費モデル表3件
- rationale: ML sense
- substitutions: 模型表→モデル表 ×3
- occurrences: L968, L981, L1014
- sections: L967 \subsection{全体点から分離診断への移動}; L970 \subsection{人手選好を公開資産化する手順と母集団の天井}; L994 \subsection{映像の多次元化と単一値の拒否}
- evidence: btd085, btd086
- before: 3 / residual original: 0

### TS539-A31 — 模型群 → モデル群 [REPLACE]
- canonical source term: model group
- meaning: モデル群 (模型群5件中1件はAPI音声模型群と重複計上)
- rationale: ML sense
- substitutions: 模型群→モデル群 ×5; API音声模型群→API音声モデル群 ×1
- occurrences: L849, L867, L889, L1023, L1090
- sections: L1017 \section{収束問題：統合モデルか連携する専門家群か}; L1089 \subsection{音声・対話：実時間利用と版バインドの機能集合}; L837 \subsection{凍結専門家で同期を罰する構成}; L866 \subsection{単発の主張を長時間の証拠に格上げしない}
- evidence: btd131, btd129, btd130, btd135, btd094, btd107
- before: 6 / residual original: 0

### TS539-A32 — 模型公開 → モデル公開 [REPLACE]
- canonical source term: model release
- meaning: モデル公開2件
- rationale: ML sense
- substitutions: 模型公開→モデル公開 ×2
- occurrences: L575, L697
- sections: L568 \subsection{階層的自己回帰と意味・音響段階化：分単位楽曲への第一歩}; L696 \subsection*{読解上の境界}
- evidence: btd065, btd063, btd066, btd067, btd068
- before: 2 / residual original: 0

### TS539-A33 — 模型評点 → モデル評点 [REPLACE]
- canonical source term: model score
- meaning: モデル評点2件
- rationale: ML sense
- substitutions: 模型評点→モデル評点 ×2
- occurrences: L864
- sections: L863 \subsection{多ターン対話の区切り手順と逓減の記録}
- evidence: btd135
- before: 2 / residual original: 0

### TS539-A34 — 模型予測 → モデル予測 [REPLACE]
- canonical source term: model prediction
- meaning: モデル予測2件
- rationale: ML sense
- substitutions: 模型予測→モデル予測 ×2
- occurrences: L369, L394
- sections: L366 \subsection{部分拡散とマスク合成：再学習なしの保存手続き}; L380 \subsection{注意写像と最適化編集：内部表現を界面にする}
- evidence: btd045, btd044
- before: 2 / residual original: 0

### TS539-A35 — 模型計算 → モデル計算 [REPLACE]
- canonical source term: model compute
- meaning: モデル計算1件
- rationale: ML sense
- substitutions: 模型計算→モデル計算 ×1
- occurrences: L228
- sections: L227 \subsection{Transformer denoiserと流れ・整合性モデルへの分岐}
- evidence: btd025, btd026
- before: 1 / residual original: 0

### TS539-A36 — 模型掛ける → モデル [REPLACE]
- canonical source term: models × (count)
- meaning: $12$模型掛ける2件
- rationale: 数量表現のモデル
- substitutions: 模型掛ける→モデル掛ける ×2
- occurrences: L621, L623
- sections: L612 \subsection{時間条件・楽理制御と人間選好検証：開放重みと評価境界}
- evidence: btd136
- before: 2 / residual original: 0

### TS539-A37 — 模型の形/位置づけ/到達/事前分布 → モデルの〜 [REPLACE]
- canonical source term: model shape/placement
- meaning: 骨格・系譜のモデル7+1件
- rationale: ML sense
- substitutions: 模型の形→モデルの形 ×4; 模型の位置づけ→モデルの位置づけ ×2; 模型の到達→モデルの到達 ×1; 模型の事前分布→モデルの事前分布 ×1
- occurrences: L166, L172, L181, L205, L367, L441, L476, L968
- sections: L160 \section{生成パラダイムと目的関数：自己回帰・敵対・拡散・フロー}; L171 \subsection{六軸分離の読み方：表現・骨格・目的・経路・抽出・短縮}; L194 \subsection{完全自己回帰：画素の同時分布を捉える}; L366 \subsection{部分拡散とマスク合成：再学習なしの保存手続き}; L435 \section{音声・声の系譜：波形からEnd-to-End、ニューラルコーデック言語モデル、全二重へ}\sectionkicker{SPEECH}\labe; L475 \subsection{何を何で表すか：言語・意味・音響・符号・波形の分担}; L967 \subsection{全体点から分離診断への移動}
- evidence: btd013, btd019, btd023, btd022, btd017, btd051
- before: 8 / residual original: 0

### TS539-A38 — 模型(歌曲構造・裸・助詞接続の残り) → モデル [REPLACE]
- canonical source term: (song-structure/statistical) model
- meaning: 節/副歌/歌の構造モデル8件+裸残り
- rationale: 99-context dumpで全件ML確認; 物理・建築・鋳型等の非ML用法なし; RETAIN 0
- substitutions: 節等の模型→節等のモデル ×1; 節や副歌の模型→節や副歌のモデル ×3; 歌の模型→歌のモデル ×3; 節・副歌模型→節・副歌モデル ×1
- occurrences: L573, L575, L655, L691, L697
- sections: L568 \subsection{階層的自己回帰と意味・音響段階化：分単位楽曲への第一歩}; L650 \subsection{持続の延長と構造の維持：時間の二軸}; L657 \subsection{評価の四分割：音質・整合・構造・人間選好}; L696 \subsection*{読解上の境界}
- evidence: btd065, btd063, btd066, btd069, btd136, btd067
- before: 8 / residual original: 0

### TS539-B01 — 模型票 → モデルカード [REPLACE]
- canonical source term: model card
- meaning: model card文書 4件
- rationale: 過剰直訳の正規化; 機種名保持
- substitutions: 模型票→モデルカード ×4
- occurrences: L1087, L1090, L1093
- sections: L1084 \subsection{画像：生成と反復編集のworkflow表面}; L1089 \subsection{音声・対話：実時間利用と版バインドの機能集合}; L1092 \subsection{音楽：制作手順としてのworkflow記録}
- evidence: btd102, btd103, btd104, btd105, btd107
- before: 4 / residual original: 0

### TS539-B02 — 票内 → カード内 [REPLACE]
- canonical source term: within-card scope
- meaning: カード内制約3件
- rationale: B01に伴う照応維持
- substitutions: 票内→カード内 ×3
- occurrences: L1087, L1106
- sections: L1084 \subsection{画像：生成と反復編集のworkflow表面}; L1103 \subsection{横断の読み方：capstoneを大きく見せない}
- evidence: btd102, btd103, btd104, btd105, btd100
- before: 3 / residual original: 0

### TS539-B03 — 票外 → カード外 [REPLACE]
- canonical source term: outside-card scope
- meaning: カード外 (票外2件中1件は票外模型と重複計上)
- rationale: 照応維持
- substitutions: 票外模型→カード外モデル ×1; 票外→カード外 ×2
- occurrences: L1087
- sections: L1084 \subsection{画像：生成と反復編集のworkflow表面}
- evidence: btd102, btd103, btd104, btd105
- before: 3 / residual original: 0

### TS539-B04 — Gemini音声票 → Gemini音声モデルカード [REPLACE]
- canonical source term: Gemini audio model card
- meaning: 音声モデルカード1件
- rationale: shorthand明示化
- substitutions: Gemini音声票→Gemini音声モデルカード ×1
- occurrences: L1090
- sections: L1089 \subsection{音声・対話：実時間利用と版バインドの機能集合}
- evidence: btd107, btd108, btd109, btd110
- before: 1 / residual original: 0

### TS539-B05 — Gemini票 → Geminiモデルカード [REPLACE]
- canonical source term: Gemini model card
- meaning: モデルカード1件
- rationale: shorthand明示化
- substitutions: Gemini票→Geminiモデルカード ×1
- occurrences: L1106
- sections: L1103 \subsection{横断の読み方：capstoneを大きく見せない}
- evidence: btd100, btd101, btd102, btd103, btd104
- before: 1 / residual original: 0

### TS539-B06 — 票範囲 → カード範囲 [REPLACE]
- canonical source term: card scope
- meaning: カード範囲1件
- rationale: 照応維持
- substitutions: 票範囲→カード範囲 ×1
- occurrences: L1090
- sections: L1089 \subsection{音声・対話：実時間利用と版バインドの機能集合}
- evidence: btd107, btd108, btd109, btd110
- before: 1 / residual original: 0

### TS539-B07 — 票(裸照応) → カード [REPLACE]
- canonical source term: (model) card
- meaning: 裸のカード照応 (HEAD6件中3件はB01/B04/B05で消費; 正味3件: 票は/票の/票へ)
- rationale: モデルカード確立後の照応; 投票用法なし; apply順でB01/B04/B05の後に残余3件へ適用
- substitutions: 票(?=[はのへ]) after B01/B04/B05→カード ×3
- occurrences: L1087, L1090, L1093, L1106
- sections: L1084 \subsection{画像：生成と反復編集のworkflow表面}; L1089 \subsection{音声・対話：実時間利用と版バインドの機能集合}; L1092 \subsection{音楽：制作手順としてのworkflow記録}; L1103 \subsection{横断の読み方：capstoneを大きく見せない}
- evidence: btd102, btd103, btd104, btd105, btd107
- before: 6 / residual original: 0

### TS539-C01 — 時刻条件U網 → 時刻条件付きU-Net [REPLACE]
- canonical source term: time-conditioned U-Net
- meaning: 時刻条件付きU-Net 3件
- rationale: Issue例示どおり; canonical保持
- substitutions: 時刻条件U網→時刻条件付きU-Net ×3
- occurrences: L172, L181, L225
- sections: L171 \subsection{六軸分離の読み方：表現・骨格・目的・経路・抽出・短縮}; L220 \subsection{連続時間への統一と潜在への移行}
- evidence: btd017, btd023, btd026, btd013, btd014
- before: 3 / residual original: 0

### TS539-C02 — U網(一般) → U-Net [REPLACE]
- canonical source term: U-Net
- meaning: U-Net (U網14件中3件はC01時刻条件U網と重複計上; 正味適用11件)
- rationale: 全件U-Net; 版内既存表記と統一
- substitutions: U網→U-Net ×14
- occurrences: L166, L168, L172, L181, L205, L213, L225, L228, L239, L249, L283, L306, L340
- sections: L160 \section{生成パラダイムと目的関数：自己回帰・敵対・拡散・フロー}; L171 \subsection{六軸分離の読み方：表現・骨格・目的・経路・抽出・短縮}; L194 \subsection{完全自己回帰：画素の同時分布を捉える}; L212 \subsection{雑音除去の転換：拡散と短縮抽出}; L220 \subsection{連続時間への統一と潜在への移行}; L227 \subsection{Transformer denoiserと流れ・整合性モデルへの分岐}; L238 \subsection{本節の読解上の境界}; L241 \section{条件づけとアライメント}; L280 \subsection{音響の言語整合と空間制御の適合}; L298 \section{制御と参照：空間・参照・主体性の保存}; L337 \subsection{時間信号の分離制御：映像の動きと音楽の変化}
- evidence: btd013, btd019, btd023, btd022, btd014
- before: 14 / residual original: 0

### TS539-D01 — 波形網 → WaveNet [REPLACE]
- canonical source term: WaveNet
- meaning: named WaveNet 5件(btd051)
- rationale: 膨張因果/256値softmax/4.43MOSがいずれもWaveNet; generic波形生成と混同なし
- substitutions: 波形網→WaveNet ×5
- occurrences: L441, L447, L449, L476, L589
- sections: L435 \section{音声・声の系譜：波形からEnd-to-End、ニューラルコーデック言語モデル、全二重へ}\sectionkicker{SPEECH}\labe; L446 \subsection{波形自己回帰と系列変換：素片結合なしの出発点}; L475 \subsection{何を何で表すか：言語・意味・音響・符号・波形の分担}; L588 \subsection{波形拡散と潜在拡散：局所忠実度と一般音響化の二系統}
- evidence: btd051, btd052, btd053, btd054, btd055
- before: 5 / residual original: 0

### TS539-E01 — 得点網 → score network（スコアネットワーク）/スコアネットワーク [REPLACE]
- canonical source term: (time-dependent) score network
- meaning: score-based SDE (得点網2件中1件は時間依存得点網と重複計上; 正味適用: 初出1+一般1)
- rationale: 初出のみcanonical English
- substitutions: 時間依存得点網→時間依存score network（スコアネットワーク） ×1; 得点網→スコアネットワーク ×2
- occurrences: L221
- sections: L220 \subsection{連続時間への統一と潜在への移行}
- evidence: btd021
- before: 3 / residual original: 0

### TS539-F01 — 枠間 → フレーム間 [REPLACE]
- canonical source term: inter-frame (consistency)
- meaning: video frame間6件
- rationale: 全件動画文脈
- substitutions: 枠間→フレーム間 ×6
- occurrences: L409, L430, L777, L790
- sections: L402 \subsection{指示追従学習と一段階動画編集：手続きの隠蔽と時間への拡張}; L774 \subsection{閉鎖頂点・開放混合専門家と編集基準測定：基盤への到達}
- evidence: btd050, btd138, btd070, btd073
- before: 6 / residual original: 0

### TS539-F02 — 枠(frame単位) → フレーム [REPLACE]
- canonical source term: (video/audio) frame
- meaning: frame単位37件(ミリ秒/整列/忠実度/別/毎秒数/同一化/雑音付与/各内/毎/数値/八)
- rationale: 音声50/80ms含めframe単位は一律; 版内既存表記と統一
- substitutions: ミリ秒枠→ミリ秒フレーム ×2; 枠整列→フレーム整列 ×1; 枠忠実度→フレーム忠実度 ×1; 枠別→フレーム別 ×2; 毎秒枠数→毎秒フレーム数 ×3; 同一枠化→同一フレーム化 ×1; 雑音付与枠→雑音付与フレーム ×2; 各枠内→各フレーム内 ×1; 毎枠→毎フレーム ×3; 八枠→八フレーム ×1; $N$枠→$N$フレーム ×19
- occurrences: L449, L511, L518, L662, L708, L713, L717, L720, L724, L727, L732, L734, L742, L759, L765, L777, L790, L801, L804, L822
- sections: L446 \subsection{波形自己回帰と系列変換：素片結合なしの出発点}; L508 \subsection{流れ補完と実時間化：非自己回帰と前後文脈の統一}; L515 \subsection{因果性と遅延と全二重：速さと同時性の分離}; L657 \subsection{評価の四分割：音質・整合・構造・人間選好}; L699 \section{映像の系譜：時間的一貫性からメディア基盤へ}\sectionkicker{VIDEO}\label{sec:video}; L712 \subsection{分解型拡散と多重超解像：時間整合の出発点}; L719 \subsection{資料効率化：外観凍結と運動学習の分離}; L726 \subsection{因子分解の設計差：二次元＋時間と時空間とTransformer}; L731 \subsection{潜在と圧縮の軸：空間潜在と時間圧縮}; L752 \subsection{動作接続器と厳選潜在動画：個人化の動作化と段階学習}; L774 \subsection{閉鎖頂点・開放混合専門家と編集基準測定：基盤への到達}; L800 \subsection{短断片の壁と長域・同一性・同期の未確立領域}; L803 \subsection{参照・条件づけ・編集と基準測定の配置}; L821 \subsection*{読解上の境界}
- evidence: btd051, btd052, btd053, btd134, btd062, btd060
- before: 36 / residual original: 0

### TS539-F03 — 枠組み → 枠組み [RETAIN]
- canonical source term: framework
- meaning: framework 18件
- rationale: framework一般語
- occurrences: L39, L371, L378, L441, L443, L518, L525, L538, L547, L553, L978, L1004
- sections: L366 \subsection{部分拡散とマスク合成：再学習なしの保存手続き}; L373 \subsection{潜在局所合成：前景と背景の分離}; L38 \subsection*{本巻の限界の要約}; L435 \section{音声・声の系譜：波形からEnd-to-End、ニューラルコーデック言語モデル、全二重へ}\sectionkicker{SPEECH}\labe; L515 \subsection{因果性と遅延と全二重：速さと同時性の分離}; L520 \subsection{Seed-TTS（多用途・高忠実音声生成）・翻訳・全二重対話：実環境と遅延の両立}; L552 \subsection*{読解上の境界}; L970 \subsection{人手選好を公開資産化する手順と母集団の天井}; L994 \subsection{映像の多次元化と単一値の拒否}
- evidence: btd022, btd059, btd083, btd089, btd098
- before: 18 / residual original: 18

### TS539-F04 — 枠内/枠外/条件枠/話者の枠 → 枠(維持) [RETAIN]
- canonical source term: scope/bounds
- meaning: 範囲・境界 22件
- rationale: boundary/box/conceptual-frame一般語; 各枠内1件のみF02
- occurrences: L451, L458, L497, L509, L511, L513, L521, L523, L538, L544, L561, L563, L619, L634, L642, L645, L662, L685, L688, L694
- sections: L446 \subsection{波形自己回帰と系列変換：素片結合なしの出発点}; L453 \subsection{並列化とニューラルボコーダと端末間統合：遅さと注意破綻への応答}; L496 \subsection{ゼロショット話者複製とニューラルコーデック言語モデル：未知話者への拡張}; L508 \subsection{流れ補完と実時間化：非自己回帰と前後文脈の統一}; L520 \subsection{Seed-TTS（多用途・高忠実音声生成）・翻訳・全二重対話：実環境と遅延の両立}; L555 \section{音楽・一般音響の系譜：コーデック言語モデルと潜在拡散}\sectionkicker{MUSIC}\label{sec:music}; L612 \subsection{時間条件・楽理制御と人間選好検証：開放重みと評価境界}; L627 \subsection{生成・継続・編集・制御の分離：課題設定の区別}; L657 \subsection{評価の四分割：音質・整合・構造・人間選好}
- evidence: btd051, btd052, btd053, btd054, btd056, btd063
- before: 24 / residual original: 24

### TS539-G01 — 民生画像処理装置(24GB) → 24GBの民生GPU 1基 [REPLACE]
- canonical source term: single 24GB consumer GPU
- meaning: 24GB民生GPU 3件(btd124)
- rationale: 数値不変; 単一→1基
- substitutions: 民生画像処理装置の単一$24$GB九分未満での→24GBの民生GPU 1基で九分未満の ×2; 民生画像処理装置の単一$24$GB九分未満の→24GBの民生GPU 1基で九分未満の ×1
- occurrences: L734, L775, L813
- sections: L731 \subsection{潜在と圧縮の軸：空間潜在と時間圧縮}; L774 \subsection{閉鎖頂点・開放混合専門家と編集基準測定：基盤への到達}; L803 \subsection{参照・条件づけ・編集と基準測定の配置}
- evidence: btd124, btd073, btd075, btd071, btd138, btd077
- before: 3 / residual original: 0

### TS539-G02 — 単一民生画像処理装置 → 民生GPU 1基 [REPLACE]
- canonical source term: single consumer GPU
- meaning: VRAMなし2件
- rationale: device count保持
- substitutions: 単一民生画像処理装置→民生GPU 1基 ×2
- occurrences: L595, L697
- sections: L588 \subsection{波形拡散と潜在拡散：局所忠実度と一般音響化の二系統}; L696 \subsection*{読解上の境界}
- evidence: btd067, btd064, btd068, btd063, btd065
- before: 2 / residual original: 0

### TS539-H01 — 文章符号器 → text encoder（テキストエンコーダ）/テキストエンコーダ [REPLACE]
- canonical source term: text encoder
- meaning: frozen text encoder (文章符号器4件中1件は初出と重複計上; 正味適用: 初出1+一般3)
- rationale: 初出のみcanonical; VAE/codec符号器は対象外
- substitutions: 文章符号器と時刻接頭辞付き→text encoder（テキストエンコーダ）と時刻接頭辞付き ×1; 文章符号器→テキストエンコーダ ×4
- occurrences: L613, L705, L713, L766
- sections: L612 \subsection{時間条件・楽理制御と人間選好検証：開放重みと評価境界}; L699 \section{映像の系譜：時間的一貫性からメディア基盤へ}\sectionkicker{VIDEO}\label{sec:video}; L712 \subsection{分解型拡散と多重超解像：時間整合の出発点}; L752 \subsection{動作接続器と厳選潜在動画：個人化の動作化と段階学習}
- evidence: btd068, btd069, btd070, btd071, btd073
- before: 5 / residual original: 0

### TS539-I01 — 交叉注意/交差注意 → cross-attention（クロスアテンション）/クロスアテンション [REPLACE]
- canonical source term: cross-attention
- meaning: cross-attention (交叉注意21件中1件は初出と重複計上; 正味適用: 初出1+交叉20+交差5=26)
- rationale: 初出のみcanonical; 分離/楽理/順次/文章/拍和音/写像の複合も同一概念で統一
- substitutions: 文や配置の交叉注意であり→文や配置のcross-attention（クロスアテンション）であり ×1; 交叉注意→クロスアテンション ×21; 交差注意→クロスアテンション ×5
- occurrences: L225, L239, L255, L268, L278, L286, L288, L328, L363, L381, L563, L580, L584, L586, L605, L613, L617, L634, L645, L929, L1050
- sections: L1049 \subsection{構造不変の資料側工夫と合成拡散の対比}; L220 \subsection{連続時間への統一と潜在への移行}; L238 \subsection{本節の読解上の境界}; L252 \subsection{凍結符号器による文条件づけ：対照事前学習の継承}; L257 \subsection{推論時誘導への転換：分類器なし誘導と文誘導拡散}; L275 \subsection{段階専門家への分岐：共有 denoiser の分割}; L285 \subsection{四区分の使い分け：条件と誘導と適合と参照}; L327 \subsection{画像参照の分離注意：文能力を壊さない足し方}; L355 \section{生成から編集へ：保存を伴う改変の系譜}\sectionkicker{EDITING}\label{sec:editing}; L380 \subsection{注意写像と最適化編集：内部表現を界面にする}; L555 \section{音楽・一般音響の系譜：コーデック言語モデルと潜在拡散}\sectionkicker{MUSIC}\label{sec:music}; L579 \subsection{一段階可制御符号音楽：多段階層の低速への応答}; L588 \subsection{波形拡散と潜在拡散：局所忠実度と一般音響化の二系統}; L612 \subsection{時間条件・楽理制御と人間選好検証：開放重みと評価境界}; L627 \subsection{生成・継続・編集・制御の分離：課題設定の区別}; L928 \subsection{構造自体を圧縮する携帯級の再設計}
- evidence: btd023, btd013, btd014, btd015, btd016, btd044
- before: 27 / residual original: 0

### TS539-J01 — 母数(ML重み) → パラメータ [REPLACE]
- canonical source term: (neural) parameters
- meaning: 変調/効率/学習/万分の一 8件
- rationale: NN重み文脈
- substitutions: 変調母数→変調パラメータ ×2; 母数効率→パラメータ効率 ×2; 学習母数→学習パラメータ ×2; 万分の一の母数→万分の一のパラメータ ×2
- occurrences: L306, L310, L328, L333, L335, L343
- sections: L298 \section{制御と参照：空間・参照・主体性の保存}; L309 \subsection{配置の前史と軽量適合：洗い流さない工夫}; L327 \subsection{画像参照の分離注意：文能力を壊さない足し方}; L332 \subsection{主体の焼付けと低階数：少数画像と効率切替え}; L342 \subsection{適合器の系譜：凍結本体に触れず足す}
- evidence: btd037, btd041, btd038, btd039, btd040, btd042
- before: 8 / residual original: 0

### TS539-J02 — 母数(統計) → 母数 [RETAIN]
- canonical source term: global statistical parameters
- meaning: VAE変分推論3件
- rationale: 統計学的population parameterとして妥当; #529凍結域
- occurrences: L114, L129, L158
- sections: L113 \subsection{連続潜在から離散符号へ：推論の償却化と量子化}; L118 \subsection{階層と知覚：高解像度への二つの道}; L157 \subsection{本節の読解上の境界}
- evidence: btd001, btd006, btd008, btd004, btd002
- before: 3 / residual original: 3

### TS539-K01 — 案内(guidance機構) → ガイダンス [REPLACE]
- canonical source term: (inference-time) guidance
- meaning: 条件づけ対ガイダンス8件
- rationale: glossary「推論時の外挿操作」=guidance
- substitutions: 推論時案内→推論時ガイダンス ×2; 案内の分離→ガイダンスの分離 ×3; 条件づけと案内、→条件づけとガイダンス、 ×1; 案内は推論時の外挿操作→ガイダンスは推論時の外挿操作 ×1; 条件と案内、制御と参照→条件とガイダンス、制御と参照 ×1
- occurrences: L42, L45, L63, L79, L1158, L1160, L1162, L1171
- sections: L1152 \section{結び──座標として読むメディア生成史}; L1170 \subsection{立場別の指針}; L41 \subsection*{この巻で比較するもの}; L44 \subsection*{座標としての通史}; L62 \subsection*{記号と表記の約束}; L68 \subsection*{読者への道案内}
- evidence: btd002, btd023, btd032, btd039, btd049
- before: 8 / residual original: 0

### TS539-K02 — 案内画像系 → 誘導画像 [REPLACE]
- canonical source term: guide image
- meaning: SDEdit等の誘導画像13件
- rationale: guide image
- substitutions: 案内画像→誘導画像 ×6; 案内への忠実さ→誘導画像への忠実さ ×1; 案内の構造→誘導画像の構造 ×1; 妥当な案内→妥当な誘導画像 ×2; 白画素主体の案内→白画素主体の誘導画像 ×3
- occurrences: L359, L367, L369, L393, L403, L433
- sections: L355 \section{生成から編集へ：保存を伴う改変の系譜}\sectionkicker{EDITING}\label{sec:editing}; L366 \subsection{部分拡散とマスク合成：再学習なしの保存手続き}; L380 \subsection{注意写像と最適化編集：内部表現を界面にする}; L402 \subsection{指示追従学習と一段階動画編集：手続きの隠蔽と時間への拡張}; L432 \subsection*{読解上の境界}
- evidence: btd044, btd045, btd046, btd049, btd047, btd048
- before: 13 / residual original: 0

### TS539-K03 — 案内(一般語) → 案内 [RETAIN]
- canonical source term: guide/notice
- meaning: 道案内/案内面/終了案内等6件
- rationale: 一般語
- occurrences: L39, L68, L1053, L1101, L1119
- sections: L1052 \subsection{来歴機構の頁限定と開かれた問い}; L1100 \subsection{lifecycle：提供終了・廃止・凍結の事実}; L1103 \subsection{横断の読み方：capstoneを大きく見せない}; L38 \subsection*{本巻の限界の要約}; L68 \subsection*{読者への道案内}
- evidence: btd022, btd059, btd083, btd089, btd098, btd099
- before: 6 / residual original: 6

### TS539-L01 — 資料(学習データ) → データ [REPLACE]
- canonical source term: training data
- meaning: 学習/共有許諾/商用/楽理増強 13件
- rationale: training-data sense
- substitutions: 学習資料→学習データ ×2; 共有許諾資料→共有許諾データ ×7; 商用資料→商用データ ×3; 楽理増強資料→楽理増強データ ×1
- occurrences: L575, L613, L619, L685, L688, L691, L694, L697
- sections: L568 \subsection{階層的自己回帰と意味・音響段階化：分単位楽曲への第一歩}; L612 \subsection{時間条件・楽理制御と人間選好検証：開放重みと評価境界}; L657 \subsection{評価の四分割：音質・整合・構造・人間選好}; L696 \subsection*{読解上の境界}
- evidence: btd065, btd063, btd066, btd069, btd136, btd068
- before: 13 / residual original: 0

### TS539-L02 — 資料(データセット) → データセット [REPLACE]
- canonical source term: dataset
- meaning: 公開データセット等3件
- rationale: named/countable dataset
- substitutions: 選別済み公開資料→選別済み公開データセット ×1; LAION-Aestheticsという資料→LAION-Aestheticsというデータセット ×1; 八十超の資料→八十超のデータセット ×1
- occurrences: L296, L904, L1026
- sections: L1025 \subsection{課題別頭部を持たない多課題統合の射程}; L295 \subsection{本節の読解上の境界}; L903 \subsection{潜在整合蒸留と低負担のLoRA化}
- evidence: btd011, btd032, btd033, btd036, btd031, btd079
- before: 3 / residual original: 0

### TS539-L03 — 資料(データ一般) → データ [REPLACE]
- canonical source term: (training/eval) data
- meaning: 動画/厳選/対/内外/規模/偏り/不足/選別/網/当該/特定/条件/構成等 38件
- rationale: data sense
- substitutions: 動画資料→動画データ ×7; 厳選資料→厳選データ ×3; 対資料→対データ ×3; 内外資料→内外データ ×2; 資料規模→データ規模 ×4; 条件別資料規模→条件別データ規模 ×2; 資料偏り→データ偏り ×2; 資料不足→データ不足 ×2; 資料選別→データ選別 ×2; 網資料→網データ ×2; 当該資料→当該データ ×1; 異なる資料→異なるデータ ×1; 資料や画素数→データや画素数 ×2; 特定の資料→特定のデータ ×1; 資料構成→データ構成 ×1; 選別資料→選別データ ×1; 報告された制御と資料→報告された制御とデータ ×1; 資料条件→データ条件 ×2; 英語の資料不均衡→英語のデータ不均衡 ×1; 資料不均衡→データ不均衡 ×3
- occurrences: L255, L260, L283, L293, L296, L310, L353, L513, L550, L553, L563, L688, L705, L713, L715, L720, L722, L729, L732, L753, L755, L807, L819, L822, L904, L929, L1050
- sections: L1049 \subsection{構造不変の資料側工夫と合成拡散の対比}; L252 \subsection{凍結符号器による文条件づけ：対照事前学習の継承}; L257 \subsection{推論時誘導への転換：分類器なし誘導と文誘導拡散}; L280 \subsection{音響の言語整合と空間制御の適合}; L292 \subsection{符号器規模と誘導尺度：報告された交換の整理}; L295 \subsection{本節の読解上の境界}; L309 \subsection{配置の前史と軽量適合：洗い流さない工夫}; L352 \subsection{本節の読解上の境界}; L508 \subsection{流れ補完と実時間化：非自己回帰と前後文脈の統一}; L520 \subsection{Seed-TTS（多用途・高忠実音声生成）・翻訳・全二重対話：実環境と遅延の両立}; L552 \subsection*{読解上の境界}; L555 \section{音楽・一般音響の系譜：コーデック言語モデルと潜在拡散}\sectionkicker{MUSIC}\label{sec:music}; L657 \subsection{評価の四分割：音質・整合・構造・人間選好}; L699 \section{映像の系譜：時間的一貫性からメディア基盤へ}\sectionkicker{VIDEO}\label{sec:video}; L712 \subsection{分解型拡散と多重超解像：時間整合の出発点}; L719 \subsection{資料効率化：外観凍結と運動学習の分離}; L726 \subsection{因子分解の設計差：二次元＋時間と時空間とTransformer}; L731 \subsection{潜在と圧縮の軸：空間潜在と時間圧縮}; L752 \subsection{動作接続器と厳選潜在動画：個人化の動作化と段階学習}; L803 \subsection{参照・条件づけ・編集と基準測定の配置}; L821 \subsection*{読解上の境界}; L903 \subsection{潜在整合蒸留と低負担のLoRA化}; L928 \subsection{構造自体を圧縮する携帯級の再設計}
- evidence: btd070, btd071, btd073, btd075, btd074, btd037
- before: 43 / residual original: 0

### TS539-L04 — 資料側 → データ側 [REPLACE]
- canonical source term: data-side
- meaning: AnyGPT等のデータ側9件+節表題2件
- rationale: model-side対比
- substitutions: 資料側→データ側 ×9
- occurrences: L1023, L1040, L1049, L1050, L1054
- sections: L1017 \section{収束問題：統合モデルか連携する専門家群か}; L1028 \subsection{話し言葉と文章の往復を一つの復号器に畳む}; L1049 \subsection{構造不変の資料側工夫と合成拡散の対比}; L1052 \subsection{来歴機構の頁限定と開かれた問い}
- evidence: btd094, btd097, btd095, btd096, btd098
- before: 9 / residual original: 0

### TS539-L05 — 資料効率化 → データ効率化 [REPLACE]
- canonical source term: data efficiency
- meaning: データ効率化8件+節表題
- rationale:  lineage
- substitutions: 資料効率化→データ効率化 ×8
- occurrences: L703, L705, L715, L719, L720, L727, L767, L807
- sections: L699 \section{映像の系譜：時間的一貫性からメディア基盤へ}\sectionkicker{VIDEO}\label{sec:video}; L712 \subsection{分解型拡散と多重超解像：時間整合の出発点}; L719 \subsection{資料効率化：外観凍結と運動学習の分離}; L726 \subsection{因子分解の設計差：二次元＋時間と時空間とTransformer}; L752 \subsection{動作接続器と厳選潜在動画：個人化の動作化と段階学習}; L803 \subsection{参照・条件づけ・編集と基準測定の配置}
- evidence: btd070, btd071, btd073, btd074, btd075
- before: 8 / residual original: 0

### TS539-L06 — 資料(典拠・文献) → 資料 [RETAIN]
- canonical source term: primary source/reference
- meaning: 一次/後継/混合型/音楽/比較/modality/コミュニティ14件
- rationale: source/document/reference
- occurrences: L63, L66, L158, L223, L239, L1143, L1145, L1168
- sections: L1142 \subsection{境界と未決laneの保持}; L1167 \subsection{失敗の診断学}; L157 \subsection{本節の読解上の境界}; L220 \subsection{連続時間への統一と潜在への移行}; L238 \subsection{本節の読解上の境界}; L62 \subsection*{記号と表記の約束}; L65 \subsection*{引用の約束}
- evidence: btd139, btd006, btd008, btd001, btd004, btd002
- before: 14 / residual original: 14

## Frozen #533 regression: all 17 terms remain 0.
## Invariants: autocite 1259 blocks identical; citation-key multiset identical (139 unique); unit multiset identical; labels identical; vendors identical; PARTIAL 12 unchanged; references.bib byte-identical (a639eca3…). Two subsection titles updated by terminology; section order/count (116) unchanged. Numeric token diff fully explained by sanctioned GPU rewording (−$24$×3, +24×3, +1×5; numerals preserved).