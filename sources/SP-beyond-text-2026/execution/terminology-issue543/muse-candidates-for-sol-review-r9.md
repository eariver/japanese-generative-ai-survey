# Muse candidates for Sol review — TS-002 Issue #543 r9

Status: `CANDIDATE_FOR_SOL_REVIEW / NO_MUSE_DECISION`
Date: 2026-09-27 JST
Rule: unmapped or semantically uncertain occurrences are left UNCHANGED in `main.tex`. No proposed final Japanese wording is given (Sol editorial decision). Canonical English is quoted only when directly visible in already-consumed sources. Human r9 authority (Issue #543, 2026-09-26T20:25:21Z, REQUEST_CHANGES@DRAFT_COMPLETE) remains in force; no new Human revision is created. Validation/candidate regeneration is NOT performed per §8 (unresolved > 0, stop at DRAFT_COMPLETE).

All r2+r3 explicit mappings have been applied; r2/r3 LHS prohibitions are zero (bare forms). The following are ML-text-modality `文章` variants outside Sol r3 S013 bound list, plus CoDi/AnyGPT text-bridge variants. Each is left unchanged.

## R9-C001 — 文章事前分布 (VITS End-to-End, btd056)

- Term: 文章事前分布
- Sentence: `End-to-End統合が統合したものは、事後分布と文章事前分布と流れとアライメント探索とデュレーション予測とボコーダによる復号であり、流れなしではMOS$2.98$まで落ちる\autocite{btd056}。`
- Section: 音声・声の系譜 / ボコーダの分業 (L456)
- Citation: btd056
- Suspected canonical English: text prior (character/phoneme prior distribution; source-visible English not confirmed in consumed body beyond prior/posterior framing).
- Status: CANDIDATE_FOR_SOL_REVIEW

## R9-C002 — 文章精緻化層 (real-time DiT, btd132)

- Term: 文章精緻化層
- Sentence: `一方は二十二層十六頭のDiffusion Transformer (DiT)と四層の文章精緻化層を組み合わせ、揺動サンプリングとオイラー解法で推論する\autocite{btd132}。`
- Section: 音声インフィリングと実時間二系統 (L511)
- Citation: btd132
- Suspected canonical English: text refinement layers (DiT + refinement; exact source wording not confirmed).
- Status: CANDIDATE_FOR_SOL_REVIEW

## R9-C003 — 文章接頭辞 (Moshi full-duplex, btd134)

- Term: 文章接頭辞
- Sentence: `枠組みは大規模言語骨格と実時間符号化器と階層深度Transformerからなり、二系列を音響遅延つきで並列にモデル化し、時刻アライメントした文章接頭辞の内言で内容を支える\autocite{btd134}。`
- Section: 対話の同時性 / 全二重枠組み (L518)
- Citation: btd134
- Suspected canonical English: text prefix (time-aligned text prefix for inner speech; exact source wording not confirmed).
- Status: CANDIDATE_FOR_SOL_REVIEW

## R9-C004 — 文章と音楽の整合 (music intro, btd063/btd065)

- Term: 文章と音楽の整合
- Sentence: `分単位の楽曲の長域整合、文章と音楽の整合、旋律や拍や和音の可制御性、歌詞の扱い、継続と補完という独立の課題設定を持つ\autocite{btd063,btd065}。`
- Section: 音楽・一般音響の生成 / 課題設定 (L559)
- Citation: btd063, btd065
- Suspected canonical English: text-music alignment (cf. Sol S013 文章音楽 → テキスト・音楽; this と-form not in bound list).
- Status: CANDIDATE_FOR_SOL_REVIEW

## R9-C005 — 結合音楽文章符号 (MusicLM three-stage, btd063/btd065)

- Term: 結合音楽文章符号
- Sentence: `第二に、凍結音響符号と自己教師意味符号と結合音楽文章符号の三段階変換で、テキスト条件を音響条件に置換して推論し、$15$秒刻みの物語式継続や旋律条件拡張を可能にした\autocite{btd065}。`
- Section: 階層的自己回帰と意味・音響段階化 (L569; also L563見取り図, L604表)
- Citation: btd065 (also btd063)
- Suspected canonical English: joint music-text codes (MusicLM MuLan-style joint codes; exact source wording not confirmed).
- Status: CANDIDATE_FOR_SOL_REVIEW

## R9-C006 — 文章側 (MusicLM inference, btd065)

- Term: 文章側
- Sentence: `学習では意味を音響側で条件づけ、推論では文章側に置換する\autocite{btd065}。`
- Section: 意味と音響の段階化の因果 (L573)
- Citation: btd065
- Suspected canonical English: text side (vs audio side conditioning; exact source wording not confirmed).
- Status: CANDIDATE_FOR_SOL_REVIEW

## R9-C007 — 文章クロスアテンション (MusicGen, btd066)

- Term: 文章クロスアテンション
- Sentence: `$32$キロヘルツ単一信号を$640$間隔で$50$ヘルツの四重残差符号に落とし、遅延パターンの単一Transformer復号器で文章クロスアテンションとクロマ接頭辞を備え、誘導ドロップアウト$0.2$で学習し、アップサンプリングと誘導尺度$3.0$で生成し、ステレオ微調整ではコードブックを倍化する\autocite{btd066}。`
- Section: 一段階自己回帰符号音楽 (L580; also L605表)
- Citation: btd066
- Suspected canonical English: text cross-attention (cf. Sol 文章条件 → テキスト条件; this cross-attention compound not in bound list).
- Status: CANDIDATE_FOR_SOL_REVIEW

## R9-C008 — 文章のみ (MusicGen text-only baseline, btd066)

- Term: 文章のみ
- Sentence: `旋律クロマ類似は$0.66$と文章のみの$0.10$とされた\autocite{btd066}。`
- Section: 一段階自己回帰符号音楽 (L580)
- Citation: btd066
- Suspected canonical English: text-only (melody-chroma similarity text-only baseline; exact source wording not confirmed).
- Status: CANDIDATE_FOR_SOL_REVIEW

## R9-C009 — 文章と音響の整合間隙 (AudioLDM, btd067)

- Term: 文章と音響の整合間隙
- Sentence: `代償として、文章と音響の整合間隙が残り、抽象説明文は条件づけを損ない、比率$1$や$2$の学習は民生GPU 1基では不能である\autocite{btd067}。`
- Section: 波形拡散と潜在拡散の代償 (L595; also L697 対照の文章・音響間隙)
- Citation: btd067
- Suspected canonical English: text-audio alignment gap (cf. Sol S013 文章音響 → テキスト・音響; this と-form / ・-form not in bound list).
- Status: CANDIDATE_FOR_SOL_REVIEW

## R9-C010 — 文章と拍と和音 (MuSTANGO, btd069)

- Term: 文章と拍と和音
- Sentence: `第二に、潜在拡散に対照音楽ネットワークを重ね、文章と拍と和音の順次クロスアテンションで拍優先の制御学習を行い、楽理増強データで補った\autocite{btd069}。`
- Section: 時間条件・楽理制御 (L613; also L617)
- Citation: btd069
- Suspected canonical English: text-beat-chord sequential cross-attention (exact source wording not confirmed).
- Status: CANDIDATE_FOR_SOL_REVIEW

## R9-C011 — 文章や領域 (Motion Module evaluation axes, btd074)

- Term: 文章や領域
- Sentence: `motion smoothness（モーション滑らかさ）評価は$2.825$と$1.615$を上回り、文章や領域やmotion smoothness（モーション滑らかさ）の三軸で比較された\autocite{btd074}。`
- Section: AnimateDiff Motion Module (L753; also L759)
- Citation: btd074
- Suspected canonical English: text axis (evaluation axes text/region/motion-smoothness; exact source wording not confirmed).
- Status: CANDIDATE_FOR_SOL_REVIEW

## R9-C012 — 文章拡張 (video conditioning layout, btd070/btd071/btd073/btd075/btd074/btd124)

- Term: 文章拡張
- Sentence: `テキスト・動画の共同学習条件づけ、oscillating guidance（振動型ガイダンス）、毎秒フレーム数条件と微小条件、画像符号化と雑音付与フレームの連結と線形増加誘導、Domain Adapter（ドメインアダプター）とMotion LoRA と推論時尺度、文章拡張の hosted や局所利用が条件の配置である\autocite{btd070,btd071,btd073,btd075,btd074,btd124}。`
- Section: 参照・条件づけ・編集とベンチマーク評価の配置 (L804)
- Citation: btd070, btd071, btd073, btd075, btd074, btd124
- Suspected canonical English: text expansion (hosted/local text-expansion conditioning; exact source wording not confirmed).
- Status: CANDIDATE_FOR_SOL_REVIEW

## R9-C013 — 動画文章 / 画像文章 (Imagen Video training mixture, btd071)

- Term: 動画文章 / 画像文章
- Sentence: `連鎖費用は重く回転整合は不精密で、$14$M動画文章＋$60$M画像文章＋LAION-$400$Mの学習に偏り危険を伴い未公開である\autocite{btd071}。`
- Section: 読解上の境界 (L822)
- Citation: btd071
- Suspected canonical English: video-text / image-text pairs (14M video-text + 60M image-text; cf. Sol 対文章動画データ → テキスト・動画ペアデータ; this reversed-order compound not in bound list).
- Status: CANDIDATE_FOR_SOL_REVIEW

## R9-C014 — 文章と画像の条件付け (adversarial distillation, btd081)

- Term: 文章と画像の条件付け
- Sentence: `凍結DINOv2のViT-S頭に文章と画像の条件付けとR1正則化を組み合わせたhinge敵対損失に、画素空間の最終NFSD変種であるscore distillation（スコア蒸留）損失を加え、推論時は無誘導で反復精緻化する\autocite{btd081}。`
- Section: 敵対的蒸留 (L926)
- Citation: btd081
- Suspected canonical English: text-image conditioning (exact source wording not confirmed).
- Status: CANDIDATE_FOR_SOL_REVIEW

## R9-C015 — 文章映像 (VBench, btd092)

- Term: 文章映像
- Sentence: `ただし背骨偏りを継承し、静止映像が整合次元を欺き、文章映像はテキスト・画像、とりわけSDXL級の複数物体と空間構成に後れ、次元間重みは設計上ない\autocite{btd092}。`
- Section: 映像の多次元化 (L995)
- Citation: btd092
- Suspected canonical English: text-video (cf. Sol 文章動画 → テキスト・動画; this 映像-form not in bound list).
- Status: CANDIDATE_FOR_SOL_REVIEW

## R9-C016 — 文章はSentencePiece指示 (Unified-IO, btd094)

- Term: 文章はSentencePiece指示
- Sentence: `文章はSentencePiece指示、濃密地図と画像はVQ-GAN符号、箱と点は千区分位置トークンとし、純粋T5符号復号器に二次元片と位置符号で与え、スパン雑音一五％と画像雑音七五％の事前学習の後に八十超のデータセットを温度混合で多課題学習し、評価用微調整を行わない\autocite{btd094}。`
- Section: 多課題統合 Unified-IO (L1026)
- Citation: btd094
- Suspected canonical English: text as SentencePiece instructions (exact source wording not confirmed).
- Status: CANDIDATE_FOR_SOL_REVIEW

## R9-C017 — 話し言葉と文章の往復 (AudioPaLM, btd095)

- Term: 話し言葉と文章の往復
- Sentence: `話し言葉と文章の往復を一つの復号器に畳む変化が、AudioPaLMである。`
- Section: 見出し+本文 (L1028-L1029; also L1039表, L1071)
- Citation: btd095
- Suspected canonical English: speech-text roundtrip (speech and text joint modeling; exact source wording not confirmed).
- Status: CANDIDATE_FOR_SOL_REVIEW

## R9-C018 — 画像文章 (Unified-IO table, btd094)

- Term: 画像文章
- Sentence: `多課題統合 & 離散均質化・課題別頭部なし・温度混合多課題学習 & 画像文章の生成課題・VQ-GAN律速・軌道限定 \\`
- Section: 統合の対照表 (L1038)
- Citation: btd094
- Suspected canonical English: image-text generation tasks (cf. Sol 文章画像 → テキスト・画像; reversed order not in bound list).
- Status: CANDIDATE_FOR_SOL_REVIEW

## R9-C019 — 文章橋渡し (AnyGPT/CoDi, btd096/btd097)

- Term: 文章橋渡し
- Sentence: `LLaMA-2-7Bを二兆文章トークンの土台に文章橋渡しアライメントとAnyInstruct十万八千件で次トークン学習し、復号は拡散とSoundStormとEncodecで行う\autocite{btd096}。`
- Section: AnyGPT (L1050; also L1040表, L1050 CoDi 文章橋渡しプロンプト符号化)
- Citation: btd096, btd097
- Suspected canonical English: text bridge / text-bridge alignment (exact source wording not confirmed).
- Status: CANDIDATE_FOR_SOL_REVIEW

## R9-C020 — 二兆文章トークン (AnyGPT, btd096)

- Term: 二兆文章トークン
- Sentence: Same as R9-C019 (L1050).
- Section: AnyGPT (L1050)
- Citation: btd096
- Suspected canonical English: two-trillion text tokens (LLaMA-2 base; exact source wording not confirmed).
- Status: CANDIDATE_FOR_SOL_REVIEW

## R9-C021 — 文章音声 / 映像音声 (CoDi, btd097)

- Term: 文章音声 / 映像音声
- Sentence: `結合生成は凍結モデルにクロスアテンションと対比アライメントの環境符号化を加え、テキスト・画像から文章音声へ映像音声へと線形に拡張して未見組合せを可能にする\autocite{btd097}。`
- Section: CoDi 合成拡散 (L1050; also AudioCaps文章音声, 文章画像COCO in same paragraph)
- Citation: btd097
- Suspected canonical English: text-audio / video-audio (linear text-image → text-audio → video-audio expansion; exact source wording not confirmed).
- Status: CANDIDATE_FOR_SOL_REVIEW

## R9-C022 — 作成(文章・音声・画像・映像) (Suno, btd114)

- Term: 文章・音声・画像・映像
- Sentence: `Suno release notes(...)は、作成(文章・音声・画像・映像)、歌曲編集・置換・トリミング・Stem・Extend・Remix・Cover・Persona、Studio DAWという制作手順の全体を記録する\autocite{btd114}。`
- Section: 商用歌曲workflow (L1095)
- Citation: btd114
- Suspected canonical English: text/audio/image/video creation inputs (four-way modality list; Sol lists only pairwise text-image/video/audio/music, not this four-way form).
- Status: CANDIDATE_FOR_SOL_REVIEW

## R9-C023 — 対照の文章・音響間隙 (music boundary, btd067)

- Term: 対照の文章・音響間隙
- Sentence: `対照の文章・音響間隙が残り、抽象説明文はテキスト条件を損ない、比率$1$・$2$は民生GPU 1基で学習不能である\autocite{btd067}。`
- Section: 読解上の境界 (L697)
- Citation: btd067
- Suspected canonical English: text-audio contrastive gap (cf. Sol 文章音響 → テキスト・音響; ・-form not in bound list).
- Status: CANDIDATE_FOR_SOL_REVIEW

---

Unresolved candidate count: 23 distinct terms (multiple occurrences each; exact sentences/sections/citations above).
No proposed Japanese wording is given. All occurrences left unchanged in `main.tex`.
Next: Sol residual judgment within same Human r9 authority; no new Human revision; no VALIDATED_DRAFT/RELEASE_CANDIDATE.
