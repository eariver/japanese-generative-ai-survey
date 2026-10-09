# TS-003 Language QA — Draft r1 Japanese reader prose

Status: `PASS_WITH_NOTES / QA_REPAIR_LOOP_COMPLETE / SOL_FINDINGS_RECORDED`

Date: `2026-10-01`

Scope: all 16 reader-facing Draft Results (`draft/v2/packages/*/draft-result.json`,
headline + deck + PARAGRAPH blocks; auto CLAIM_BOUNDARY blocks excluded from prose QA
but noted in §4). Total reader text audited: ~104.8k chars (P01–P15 + synthesis).

Policy: `execution/drafting-language-policy-ja.md`.
Map: `execution/drafting-terminology-map-ja.md` (`TS-003_TERMINOLOGY_MAP_R1_FIXED`).

Method: full read of all 16 packages + programmatic scans for (a) internal-jargon
patterns, (b) kanji-stack chains, (c) repeated English glosses, (d) kanji-numeral mixes,
(e) lane/obligation codes, (f) unmapped English technical terms.

## 1. Verdict per audit dimension

1. excessive kanji / Sino-Japanese translation — FOUND AND REPAIRED (模型 62x, supervision 12x, 生来/生まれながら, 商業の最良, 百B級). Residual: none in authorable prose.
2. invented/nonstandard translations — none found (V2L gloss added where a bare acronym stood).
3. literal translation artifacts — one fixed (31.2% unit drop); kanji numerals clean.
4. noun stacking / over-nominalization — no chains flagged by scan; spot-read clean.
5. English→Japanese semantic drift — none; load-bearing pairs kept distinct throughout
   (P07A has zero 接地 occurrences; P13/P14/P15 keep planner/policy, four-pole, vendor/independent splits).
6. inconsistent terminology across packages — one class fixed (model renderings);
   GoldG proper-noun usage consistent (P04/P07B); LVIS-rare/レア normalized in P07B.
7. unnecessary repeated English parentheticals — none (first-use-only pattern held;
   perception/predictive-representation/grounding glosses appear once each).
8. machine-translated-sounding syntax — acceptable; some repetitive cadence remains (see §4 R3).
9. internal workflow jargon leakage — FOUND AND REPAIRED (D-lane codes P04 5x,
   本カード P03, Evidenceのv3/受け入れ時/正準の範囲 P11, カード P13/P15 7x,
   版の修復/対応版 P14, 証拠時点 P15). Residual: auto boundary-block English (§4 R1).
10. semantic-distinction loss via translation — none; grounding/alignment,
    detection/recognition, benchmark/evaluation, world-model/predictive-representation,
    capability/evidence, architecture/deployment kept distinct.

## 2. Corrections applied (all prose-only; no meaning/evidence/binding/coverage change)

Mechanism: fixed in `execution/draft-r1-20261001/specs/*.json` (+ `apply_qa_repairs.py`
record), reassembled input, deleted `draft/v2`, re-ran canonical
`run_drafting_synthesis_v2_agent.py` (all 16 results re-validated PASS by the runner),
re-ran stage validation → `validation/draft-r1-stage-validation-r2.json` PASS.
Spot-verified in canonical result bytes (P04/P07B/P13/P15).

- 模型→モデル 62x (P02 2, P03 10, P04 2, P07B 2, P09 2, P10 3, P11 11, P13 9, P14 6, P15 15).
- supervision→教師信号 12x + spacing normalization (P07A 5, P07B 7).
- P04 lane codes → section names (D10/D12/D13→推論/画面操作/行動の節; D09/D13→統合/行動の節).
- P06 百B級→100B級. P07B 脚注→脇に置く; V2L gloss; rare→レア 4x; 31.2% 2x.
- P03 本カード→本節. P11 Evidenceのv3→v3の記録, 受け入れ時→記録の範囲, 正準の範囲→記録の範囲.
- P13/P15 カード→モデルカード 7x. P14 版の修復→本節, 対応版→版.
- P15 証拠時点→v3の記録, 商業の最良→商用モデルの最良, 生来/生まれながら→当初から, duplicate-sentence removal.

## 3. Positive confirmations

- P05 qualitative specialist comparison holds with zero numeric rankings (G03).
- P07B/P09 mechanism-grouped, no one-paper-one-paragraph catalogue.
- P15 synthesis-led across D15 + X01–X04 threads; convergence left open.
- P12 grounding/task-success separation; P13 hard-cap respected; P14 four-pole + non-ancestry guard.
- G01–G06 + 5 PARTIAL carried as limitations; vendor claims attributed; no cross-task rankings authored.

## 4. Residual Sol-review findings (NOT self-repaired; need semantic/Architecture authority)

- R1. Auto CLAIM_BOUNDARY blocks render Architecture boundary strings in English
  (G01–G06 codes, PARTIAL labels, evidence-boundary English). Canonical Core output,
  identical in kind to TS-002 precedent. Japanese-izing requires Architecture change → Sol decision.
- R2. P09 b3/b2 paper-internal head-to-head numbers (Molmo 2 vs Qwen3-VL/Gemini 3 Pro;
  InternVL3 vs 4o/Sonnet/Gemini-2.5-Pro) are attributed in-paper reports, not authored
  rankings, but sit near the no-ranking rule → Sol confirmation requested.
- R3. Repetitive cadence (〜と読む/〜と運ぶ closings) in long packages — style polish
  candidate for a later prose pass; not a correctness defect.

Core validator PASS is not claimed as language PASS. This report is the language gate.

Terminal QA state: `TS-003_JAPANESE_LANGUAGE_QA_COMPLETE / PASS_WITH_NOTES`
