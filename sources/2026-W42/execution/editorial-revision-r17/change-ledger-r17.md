# W42 r17 change ledger (r16 v16.0 → r17 v17.0)

Date: 2026-10-18. No canonical overwrite. r16 files byte-identical.

## Counts (paragraph-only; PTN with headings/tables/notes in validation report)

- r16: 136 paras / 24,832 chars (P1 3,639 / P2 3,575 / P3 4,570 / P4 3,688 / P5 2,856 / P6 3,673 / P7 2,831)
- r17: 136 paras / 25,085 chars (P1 3,654 / P2 3,803 / P3 4,570 / P4 3,688 / P5 2,858 / P6 3,609 / P7 2,903)
- Delta: +253 chars total (+15 P1, +228 P2, 0 P3, 0 P4, +2 P5, −64 P6, +72 P7). Paras unchanged (136). No new blocks, no deletions; in-place retexts only. must_cover/boundary maps stable.

PTN (paragraph+table+note, headings separate; same definitions as r16 F-09): to be recorded in validation-report-r17 (frozen receipts). Headings 131 chars carried (definition unchanged).

## Changed blocks (13 total)

- P1 t1-11 (Minecraft 4+1 agents, rock/dragon phrasing, SIMA2 boundary), t1-23 (Observer, fixed-seed, failure aggregation to t1-16), t1-13 (table fixed-seed), t1-16 (dragon-fight naming)
- P2 t2-03 (1-pod 24×4=96, GB/s scope, host/memory/storage/cooling), t2-20 (full-96-config, 750GB/s band vs HBM GB/TB/s), t2-08 (§5(a)(b) + §5(c) qualified), t2-21 (entity-wide annual revenue, hosting=channel, §5(c) limits, per-artifact scope), t2-11 (table 96-accel 1-pod + US$10M entity revenue)
- P5 t5-06/t5-08 (模型→モデル, 2 instances)
- P6 t6-08 (GeoExpert aggregation note, GeoKTools/Table-5 retained)
- P7 t7-19 (comparability focus, no numeric repeat)

P3/P4 unchanged (0). Full old/new excerpts in `block-diff-r16-r17.json`.

## Bibliography / ledger

- Map: B74 bare + notes; 19 alias_of; B62/B65→一次, B88→二次; invalid 0/90.
- Ledger: 38 URL repairs (5 patterns); invalid 0/177; 177 rows retained.
- Reader JSON/MD regenerated from r17 proposals (136/136 paras in TeX verified); synthesis input rebuilt (SHA `e1d4f477…`), result re-stamped v2.0, synthesis-check PASS.

## Readability

- Translationese zero (see preflight). Dedup preserves negatives (GeoKTools/Table-5, Glimpse baselines in t7-07, failure denominators in t1-16). No padding (net +253 from required qualifications; P6 shrinks). Tables/notes intact.

## Layout

- Table-7 moved P7-end → P7-intro (after t7-04), content identical, float preserved. Approach A adopted (in-body p17), B rejected (flow break). No font/margin/whitespace-for-count change. 21pp measured (cover1/body p2–p17/bib p18–p21), Table-7 in-body, B57 minor URL carry noted.
