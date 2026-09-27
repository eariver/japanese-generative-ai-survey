# Muse candidates for Sol review — TS-002 Issue #543 r10 (post-r7 residual)

Status: `CANDIDATE_FOR_SOL_REVIEW / NO_MUSE_DECISION`
Date: 2026-09-27 JST
Rule: Sol r7 (plus SOL-CIT-003/004) has been applied without reinterpretation under Human r10 REQUEST_CHANGES@DRAFT_COMPLETE. The following reader-facing occurrences are outside r2–r7 bound mappings (different order/noun/particle, different source/context, or unmapped wording). Each is left UNCHANGED in `main.tex`. No proposed final Japanese wording is given. Canonical English is quoted only when directly visible in already-consumed sources. No new Human revision is created; remain at DRAFT_COMPLETE. Do not create r11.

r2–r7 left-hand sides: zero (bare forms; `文条件`/`回転整合` bare zero; `jointly`/`framing`/`baseline` zero). #533 zero. #539 REPLACE left-hand sides zero. `文章` remains only as ordinary `文章化`. `端末` remains only as endpoint-latency/mobile-terminal senses. `帳` remains only as reception `台帳`. Citations changed only per SOL-CIT-003/004; `references.bib` untouched.

## R10-C001 — 条件と誘導と適合と参照 (four-category heading)

- Term: 条件と誘導と適合と参照
- Sentence: `\subsection{四区分の使い分け：条件と誘導と適合と参照}`
- Section: 条件づけとアライメント (L285)
- Citation: none on heading (section cites btd011–btd036)
- Suspected canonical English: learning-time condition / inference-time guidance / adapter / context reference (cf. Sol r7 §4 adapter-context 適合 mappings; this bare category label not in bound list).
- Status: CANDIDATE_FOR_SOL_REVIEW

## R10-C002 — 軽量適合 bare (T2I-Adapter lineage, no 配置)

- Term: 軽量適合
- Sentence (L304): `本節がたどるのは、凍結モデルに触れず空間と参照と主体を足すアダプター／適応の系譜であり、配置前史から軽量適合、画像参照、少数主体、低ランク、映像と音楽の時間信号まで接続する\autocite{btd041,btd037,btd039,btd042}。`
- Sentence (L309 heading): `\subsection{配置の前史と軽量適合：洗い流さない工夫}`
- Sentence (L353a): `複数アダプターの手動合成と粗い素描の分散は軽量適合の境界である\autocite{btd037}。`
- Section: 制御と参照 (L304/L309/L353)
- Citation: btd041+btd037+btd039+btd042 / heading / btd037
- Suspected canonical English: lightweight adapter (T2I-Adapter lineage; cf. Sol r7 軽量配置適合 → 軽量制御アダプター（T2I-Adapter）; this 配置-less form not in bound list).
- Status: CANDIDATE_FOR_SOL_REVIEW

## R10-C003 — 画像参照 bare (IP-Adapter lineage, no 適合)

- Term: 画像参照
- Sentence (L290): `ゼロ初期化で固定側を壊さず育てる考えは、画像参照の分離注意や低ランク因子のゼロ初期化にも通じる。`
- Sentence (L304): same lineage enumeration as R10-C002.
- Sentence (L327 heading): `\subsection{画像参照の分離注意：テキストプロンプト能力を壊さない足し方}`
- Sentence (L353): `画像参照は内容と様式の類似に留まり、少数画像の主体一貫には届かない\autocite{btd038}。`
- Section: 制御と参照 (L290/L304/L327/L353)
- Citation: btd038 (L353; L327 subsection cites btd038)
- Suspected canonical English: image reference (IP-Adapter lineage; cf. Sol r7 画像参照適合 → 画像参照アダプター（IP-Adapter）; this 適合-less form not in bound list).
- Status: CANDIDATE_FOR_SOL_REVIEW

## R10-C004 — 適合の視点 (section summary framing)

- Term: 適合の視点
- Sentence: `本節の五転換を適合の視点で振り返る。`
- Section: 制御と参照 / アダプターの系譜 (L343)
- Citation: paragraph cites btd037–btd043
- Suspected canonical English: adaptation viewpoint (cf. Sol r7 適合の系譜 → アダプター／適応の系譜; this 視点-form not in bound list).
- Status: CANDIDATE_FOR_SOL_REVIEW

## R10-C005 — 訓練や反転なしの適合 (edit benchmark, btd138)

- Term: 訓練や反転なしの適合
- Sentence: `訓練や反転なしの適合の条件で距離$94.61$と類似$82.55$とピーク$25.57$で忠実度$89.43$、毎フレーム$3.07$秒と$1.44$秒や$25.98$秒、精度$46.97$と$43.84$や$48.42$が報告された\autocite{btd138}。`
- Section: 参照・条件づけ・編集とベンチマーク評価の配置 (L804)
- Citation: btd138
- Suspected canonical English: adaptation without training or inversion (tuning-free editing condition; exact source wording not confirmed; not in Sol r7 bound list).
- Status: CANDIDATE_FOR_SOL_REVIEW

## R10-C006 — 誘導尺度の掃引 (CFG, btd032)

- Term: 誘導尺度の掃引
- Sentence: `誘導尺度の掃引で得られた分布類似とInception Score（IS）の交換も、報告された小解像の条件に結びつく\autocite{btd032}。`
- Section: 推論時誘導への転換 (L260)
- Citation: btd032
- Suspected canonical English: guidance-scale sweep (cf. Sol r7 bare 尺度掃引 → ガイダンススケールのスイープ; this 誘導-prefixed possessive form not in bound list).
- Status: CANDIDATE_FOR_SOL_REVIEW

## R10-C007 — 画像と文 symmetric reversal (DALL-E / CLIP)

- Term: 画像と文
- Sentence (L110): `大規模なテキスト条件づけとの結合は、画像と文を単一ストリームに載せる離散化によって先駆けられた\autocite{btd005}。`
- Sentence (L253): `アーキテクチャとしては画像と文の二符号器と学習温度が前者であり、目的関数は対称交差エントロピーである\autocite{btd031}。`
- Section: 表現と圧縮 (L110, btd005) / 凍結符号器によるテキスト条件づけ (L253, btd031)
- Citation: btd005 / btd031
- Suspected canonical English: image and text (cf. Sol r7 technical 文と画像 → テキストと画像; this reversed order not in bound list).
- Status: CANDIDATE_FOR_SOL_REVIEW

## R10-C008 — バイト対符号化文 (DALL-E BPE text, btd005)

- Term: バイト対符号化文
- Sentence: `表現の側では二百五十六画素を三十二掛ける三十二の千二十四トークンへ離散化し、語彙八千超の画像符号と二百五十六トークン以内のバイト対符号化文を単一ストリームとして連結する短縮が採られた\autocite{btd005}。`
- Section: 文と画像の単一列 (L138)
- Citation: btd005
- Suspected canonical English: byte-pair-encoded text (BPE text tokens; exact source wording not confirmed; not in Sol r7 bound list).
- Status: CANDIDATE_FOR_SOL_REVIEW

## R10-C009 — 文や配置 (LDM cross-attention, btd023)

- Term: 文や配置
- Sentence: `アーキテクチャは知覚と敵対項の符号器、時刻条件付きU-Net、文や配置のcross-attention（クロスアテンション）であり、目的関数は潜在雑音整合である\autocite{btd023}。` (also `文や配置の条件は領域符号器とクロスアテンションで入る`, same line L225)
- Section: 連続時間への統一と潜在への移行 (L225)
- Citation: btd023
- Suspected canonical English: text-or-layout conditioning (cf. Sol r7 technical 文と画像 → テキストと画像; this や-disjunction with 配置 not in bound list).
- Status: CANDIDATE_FOR_SOL_REVIEW

## R10-C010 — 文から絵や音 (section intro, rhetorical)

- Term: 文から絵や音
- Sentence: `文から絵や音を生むとき、条件づけはどこで行われるのか。`
- Section: 条件づけとアライメント / intro (L247)
- Citation: none (intro sentence)
- Suspected canonical English: text-conditioned generation of images/sounds (cf. Sol r7 文から画像 → テキストから画像; this colloquial 絵や音 form not in bound list).
- Status: CANDIDATE_FOR_SOL_REVIEW

## R10-C011 — 類名詞の文 (DreamBooth prompts, btd039)

- Term: 類名詞の文
- Sentence: `少数画像個人化が三から五枚に稀少識別子と類名詞の文を添え、全層微調整と自動生成類損失で主体を焼き付けつつ類を保つ転換を示し\autocite{btd039}...` (L306; same sentence repeated L333)
- Section: 主体の焼付けと低ランク (L306/L333)
- Citation: btd039
- Suspected canonical English: class-noun prompt text (identifier + class prompt wording; exact source wording not confirmed; ambiguous between ordinary sentence and ML prompt text).
- Status: CANDIDATE_FOR_SOL_REVIEW

## R10-C012 — 多層網 (video data-efficiency, btd073)

- Term: 多層網
- Sentence: `テキスト・画像多層網に擬似三次元畳み込みと注意を拡張し、毎秒フレーム数条件を加え、外観事前分布を固定したまま動画データセットだけで運動を学習し、事前分布から時間復号、遮蔽補間、時間空間超解像へ共有雑音で進む\autocite{btd073}。`
- Section: データ効率化 (L720)
- Citation: btd073
- Suspected canonical English: multilayer network (T2I backbone network expanded with pseudo-3D conv; cf. Sol r2/r3 網→ネットワーク family: 単一網/既存拡散網/雑音予測網; this 多層網 form not in bound list).
- Status: CANDIDATE_FOR_SOL_REVIEW

---

Unresolved candidate count: 12 distinct terms (18 occurrences). All left unchanged.
Next: Sol judgment within same Human r10 authority; no new Human revision; remain at DRAFT_COMPLETE. Do not create r11.
