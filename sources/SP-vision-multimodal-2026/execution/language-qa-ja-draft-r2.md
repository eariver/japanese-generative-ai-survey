# TS-003 Language QA r2 — Draft r2 reader surface

Status: `PASS_WITH_NOTES / F1-F5_CLOSED / SOL_R2_PENDING`

Date: `2026-10-01`

Scope: all 16 r2 Draft Results (headline + deck + PARAGRAPH blocks; repaired
CLAIM_BOUNDARY blocks checked separately) + profile synthesis payload.
Reader text audited: ~52.2k chars input / ~57.6k chars with boundary blocks.

Method: full-text review via 4 repair agents (each with own duplicate + lexicon scans)
+ independent Work verification scans (duplicates, r1 lexicon before/after, bare-著者,
internal codes, boundary-block language, P09 ranking language).

## 1. Duplicate-sentence scan (contract §7)

Split on 。, stripped compare, headline/deck/PARAGRAPH text:

| Pkg | sents | dups | | Pkg | sents | dups |
|-----|------:|-----:|---|---|------|-----:|
| P01 | 30 | 0 | | P09 | 103 | 0 |
| P02 | 39 | 0 | | P10 | 44 | 0 |
| P03 | 30 | 0 | | P11 | 70 | 0 |
| P04 | 30 | 0 | | P12 | 53 | 0 |
| P05 | 90 | 0 | | P13 | 77 | 0 |
| P06 | 74 | 0 | | P14 | 80 | 0 |
| P07A | 53 | 0 | | P15 | 121 | 0 |
| P07B | 135 | 0 | | P08 | 64 | 0 |

Cross-package distinct repeats: 0. P15 (r1: 93 occurrences) now 0.
Acceptance target met (zero per package, zero P15, zero templated cross-package).

## 2. r1 failure-lexicon before → after (reader prose, r1 snapshot vs r2)

網 35→0, 処方 46→0, 証し 67→0, 躾 29→0, 構え 70→0, 運ぶ系 53→0, 棚 16→0,
凱歌 2→0, 束ねの妙 1→0, 土俵 29→0, 物差し 92→0, 顔つき 6→0, 段取り 29→0,
宿題 14→0, 持ち場 7→0, 見取り図 14→0, 務め 18→0. Total 528→0.
Replacements use established terms (モデル, 学習レシピ, 根拠, 規律/評価の決め,
アーキテクチャ/設計/仕組み, 引き継ぐ/示す, 指標/測り方, 条件, 特性).

## 3. Remaining dimensions

- Literal artifacts: clean (units kept: 31.2%→44.6%, 234ms theoretical).
- Excessive kanji: clean (模型→モデル done in r1 and held; no new kanji compounds).
- Invented terms: none (V2L glossed once; レア katakana kept).
- Over-nominalization: no chains flagged; cadence notes below.
- Source-role (F4): evaluator classes explicit everywhere (ベンダー測定 /
  モデル論文の著者測定 / ベンチマーク論文の著者による第三者測定 / 独立した第三者再現);
  forbidden r1 sentence gone; no bare-著者-as-independence (21 regex hits all inside
  the explicit class phrases).
- Internal jargon: zero (no VM-D/VM-O/G-/X-codes/PARTIAL/SELECTED/stage names in prose).
- Boundary leakage (F5): boundary blocks are concise Japanese (66–211 chars);
  only legitimate model names/years/numbers remain (ImageNet, R-CNN, Genie 3, 234ms).
- Terminology consistency: アライメント/接地 split held (P07A zero 接地);
  モデルカード, 教師信号, 軌道, v3の記録, 当初からのマルチモーダル held from r1.
- P07B: 9 mechanism groups kept, metric contracts separated, no catalogue.
- P09: three questions kept; only 2 sanctioned same-source head-to-head tables remain
  with explicit attribution; 優劣 language appears only as no-ranking discipline;
  話題の首位 framed as project announcement, not authority.
- P15: synthesis-led, 10 threads, convergence stated once with support; no connective-tissue filler.

## 4. Notes (non-blocking; no F1–F5 residue)

- N1. P01「LeNet論文の著者PDF」: author-provided-PDF provenance wording; natural, no independence claim.
- N2. P07B「チェックポイントと推論コードを開く」: standard ML katakana for model checkpoint release.
- N3. Some repetitive cadence remains in long packages (〜と報告している closers) —
  attribution closers required by the evidence contract, not filler.
- N4. Volume shortened r1 90.3k → r2 52.2k chars by dedup; no padding applied.
  If Sol judges any package technically thin after dedup, that is a depth finding for
  Sol r2, not a QA defect — reported, not padded.

Core validator PASS is not claimed as language PASS. This report is the language gate.

Terminal QA state: `TS-003_LANGUAGE_QA_R2_COMPLETE / PASS_WITH_NOTES`
