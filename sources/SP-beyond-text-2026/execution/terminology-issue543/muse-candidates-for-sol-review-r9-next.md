# Muse candidates for Sol review — TS-002 Issue #543 r9-next (post-r4 residual)

Status: `CANDIDATE_FOR_SOL_REVIEW / NO_MUSE_DECISION`
Date: 2026-09-27 JST
Rule: Sol r4 (R9-C001〜R9-C023) has been applied without reinterpretation under the same Human r9 REQUEST_CHANGES@DRAFT_COMPLETE. The following reader-facing occurrences are outside r2/r3/r4 bound mappings (different noun, different source/context, or unmapped product/corpus wording). Each is left UNCHANGED in `main.tex`. No proposed final Japanese wording is given. Canonical English is quoted only when directly visible in already-consumed sources. No new Human revision is created; no VALIDATED_DRAFT/RELEASE_CANDIDATE.

r2/r3/r4 left-hand sides: zero (bare forms). #533 (242 entries) zero. #539 REPLACE left-hand sides zero; 母数 (statistical) and 案内 (ordinary guide) occurrences are RETAIN senses. Citations unchanged in this pass (1261 commands, 139 keys). `文章化` (verbalize into sentences, L722/L724/L807/L822) is ordinary prose per r4 s4 and is retained, not listed here.

## R9N-001 — 文章と音楽の対応 (music metric boundary, btd063/btd065)

- Term: 文章と音楽の対応
- Sentence: `距離指標は音響分布の隔たりの代理であり、対照整合指標は文章と音楽の対応の代理である。`
- Section: 音楽・一般音響の生成 / 系譜の見取り図 (L563)
- Citation: btd063, btd065
- Suspected canonical English: text-music correspondence (cf. Sol r4 C004 文章と音楽の整合 → テキスト・音楽整合; this 対応-form not in bound list).
- Status: CANDIDATE_FOR_SOL_REVIEW

## R9N-002 — 文章と言語モデル (LibriSpeech release, btd089)

- Term: 文章と言語モデル
- Sentence: `LibriSpeechは約千時間十六キロヘルツのLibriVox読書英語を分割アライメントし、Kaldi手順と文章と言語モデルをopenSLR-12で公開した事実が確認される。`
- Section: 耳と話し言葉の土台 / LibriSpeech (L992)
- Citation: btd089
- Suspected canonical English: transcripts/text and language model (corpus release contents; exact source wording not confirmed).
- Status: CANDIDATE_FOR_SOL_REVIEW

## R9N-003 — 発話音声と文章のみ (AudioPaLM scope, btd095)

- Term: 発話音声と文章のみ
- Sentence (L1029): `ただし発話音声と文章のみで画像と映像と音楽を含まず、翻訳目標は合成が多く、三秒プロンプト転移は短尺で劣化する\autocite{btd095}。`
- Sentence (L1039 table): `発話音声と文章の往復 & 語彙拡張・タグ付き混合・一復号思考連鎖 & 発話音声と文章のみ・合成目標多・短尺転移は劣化 \\`
- Sentence (L1071): `AudioPaLMは発話音声と文章のみで翻訳目標は合成が多く、短尺プロンプト転移は劣化する。`
- Section: AudioPaLM 射程/対照表/結び (L1029/L1039/L1071)
- Citation: btd095
- Suspected canonical English: speech-and-text-only (scope limitation; cf. Sol r4 C008 文章のみ → テキストのみ scoped to MusicGen btd066; this AudioPaLM source/context not in bound list).
- Status: CANDIDATE_FOR_SOL_REVIEW

## R9N-004 — 文章はOPTIMUS (CoDi text branch, btd097)

- Term: 文章はOPTIMUS
- Sentence: `画像はSD1.5、映像は擬時間と潜在シフト、音声はメル画像化とAudioLDM-VAEとボコーダ、文章はOPTIMUSとGPT-2という様式別潜在拡散を独立に置き、bridging alignment（ブリッジング・アライメント）プロンプト符号化を重み補間で融合する。`
- Section: CoDi 合成拡散 (L1050)
- Citation: btd097
- Suspected canonical English: text branch uses OPTIMUS+GPT-2 modality-specific latents (exact source wording not confirmed; r4 C021 covers modality pairs, not this branch description).
- Status: CANDIDATE_FOR_SOL_REVIEW

## R9N-005 — 文章透かし (SynthID, btd099)

- Term: 文章透かし
- Sentence: `ただし製品頁のみで独立頑健評価がなく、音声はLyriaとNotebookLMに紐付き、文章透かしの品質影響は未定量化で、検出率と曲線と容量と音楽固有評価は頁にない\autocite{btd099}。`
- Section: 来歴機構 C2PA/SynthID (L1053)
- Citation: btd099
- Suspected canonical English: text watermarking (quality impact unquantified; exact source wording not confirmed).
- Status: CANDIDATE_FOR_SOL_REVIEW

## R9N-006 — 文章・画像起点 (Ray3 product inputs, btd122)

- Term: 文章・画像起点
- Sentence: `Ray3(日付非開示の頁)は文章・画像起点と映像間変換(人物参照・開始・終了キーフレーム含む)、衣装・環境・光・配置のModifyを備えるが、頁内bannerと記事の日付は区別して版バインドする\autocite{btd122}。`
- Section: lifecycle / Ray3 (L1101)
- Citation: btd122
- Suspected canonical English: text-/image-start inputs (cf. r3 S013 文章画像 → テキスト・画像; this ・-form product-input wording not in bound list).
- Status: CANDIDATE_FOR_SOL_REVIEW

---

Unresolved candidate count: 6 distinct terms (8 occurrences). All left unchanged.
Next: Sol judgment within same Human r9 authority; no new Human revision; remain at DRAFT_COMPLETE.
