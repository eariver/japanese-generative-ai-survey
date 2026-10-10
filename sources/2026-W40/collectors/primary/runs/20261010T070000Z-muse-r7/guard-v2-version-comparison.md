# SOURCE VERSION COMPARISON — ProvenanceGuard r5 excerpt vs primary v2 (SC-E09)

- artifact_class: CLAIM_LEVEL_DERIVED_NOTE__VERSION_COMPARISON
- r5_excerpt: `collectors/primary/runs/20261010T060000Z-muse-r5/provenanceguard-paper-ar5iv-260618037.source-excerpt.md`
  (consumed via unversioned `https://ar5iv.org/html/2606.18037`, assumed v3-latest)
- v2_primary: `https://arxiv.org/html/2606.18037v2` (Muse webfetch text 2026-10-10T06:14:21Z; rendered HTML, NOT PDF bytes)
- v2 header (verbatim): `arXiv:2606.18037v2 [cs.AI] 26 Jul 2026`; `License: CC BY-NC-SA 4.0`
- v2 authors (verbatim, FOUR): Ander Alvarez, Santhiya Rajan, Samuel Mugel, Román Orús
  (matches r5 excerpt exactly; abs current page adds Genuardi/Wirjadi = LATER v3-era metadata, NOT consumed)
- abs history (verified 2026-10-10): v1 2026-06-16T15:10:29Z / v2 2026-07-26T10:47:53Z / v3 2026-08-27T16:15:34Z (current)

## Field-by-field match (r5 excerpt content vs v2 primary body)

| # | r5 excerpt claim | v2 primary text | Verdict |
|---|---|---|---|
| 1 | 281 frozen medical traces; 266-trace / 2,325-label subset; 40-trace 361-claim held-out; 260 source-eligible | §IV.1–IV.2 + Fig.4 identical structure/counts | MATCH |
| 2 | block F1 0.802 (P 0.673 / R 0.993), source acc 0.858/260, src+rel 0.681; CI [0.664, 0.900]; Table 3 | Table 3 identical (V. acc. 0.812, M. F1 0.406, Rej P/R/F1 0.673/0.993/0.802, Src. 0.858, Src+rel 0.681) + Fig.5 confusion matrix (True Block 138/139; False Block 67/222) | MATCH |
| 3 | Multi-source 59Q / 254 cases / 2,587 rows / 263 frozen claims; 0.846 / 0.503 / 0.229; stress slices | Tables 4–6 identical (incl. same-topic wrong-chart 0.127, count 0.179 slices) | MATCH |
| 4 | Baselines MiniCheck 0.783 / RAGAS 0.758 / AlignScore 0.662 / SummaC 0.436 (support-only, no source IDs) | §IV.6 + V.1 identical values and support-only scope | MATCH |
| 5 | RF calibrator 400 trees / d5 / leaf8 / balanced / Gini / seed 20260607 / threshold 0.65 (val F1 0.841); Table 1 | Table 1 identical (train 1,597 / val 367 / held-out 361; class balance rows) | MATCH |
| 6 | Routing centroid Eq + NLI DeBERTa + alignment τ=0.35 / ratio 0.70 + rescue 0.55/0.85 + 512-token budget (256 historical) | Eq.(3)–(8), Table 2 constants identical (incl. 1,500-char premise cap, historical-256 labeling) | MATCH |
| 7 | Repair 173 blocked → all (144 fallback); rerun 59 → 59 (2 fallback); 50/50 swaps detected | §III.8 + §V identical (47 evidence-only rewrites / 10 pruning / 2 terminal in rerun detail) | MATCH |
| 8 | Scope bound (attribution factuality ONLY) | §III intro + contribution 4 identical | MATCH |
| 9 | RQ2 raw-verdict head 0.839 acc; router-only 0.858 Top-1 | §V.3 identical (Table 11) | MATCH |

## Material differences found (r5 excerpt vs v2) — CORRECTED in r7

- D1. Adjudication models: r5 excerpt names `local Gemma 4 E4B` two-judge path; v2 §IV.8 says only `two independent model judge passes` (NO Gemma name). → Gemma specifics WITHDRAWN as version-unconfirmed.
- D2. Multi-source adjudication: r5 excerpt names `gpt-5.4 adjudication path`; v2 §IV.3 describes grouped/blind packets + two-judge positive-boost rows WITHOUT gpt-5.4 name. → gpt-5.4 specifics WITHDRAWN as version-unconfirmed.
- D3. Terminology: r5 excerpt uses `block F1`; v2 uses `reject/block F1` (same values). → Cosmetic; values identical.
- D4. v2-only additions now confirmed present: §V.4–V.7 RQs, §§VI–IX, Appendices A–C, Fig.5 matrix, Table 7–10 latencies, 1,500-char premise cap, `20 pages, 4 figures` comment. → Cited as v2-confirmed where consumed; tail beyond truncation still unread.
- D5. License: v2 page `CC BY-NC-SA 4.0` — recorded (rights note for supplement relation).

## Conclusion

- NO genuine contrary evidence: r5 consumed content MATCHES primary v2 on all material equations/tables/metrics/authors. PIN V2 (`published_at=2026-07-26T10:47:53Z`).
- v3-existence alternative REJECTED for this evidence (no v3 primary body compared; later catalog author metadata not consumed).
- v1 Jun 16 noted as original first submission; Sep 29 team-blog exposition REMAINS the W40 event (unchanged).
