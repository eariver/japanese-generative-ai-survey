# W43 source-key audit r4 (programmatic, exclusive, corrected)

Generator: `source-key-classify-r4.py` (reads r3 TeX body pre-bibliography, strips `%` comments + `\label`, counts exact key strings in reader-visible spans). Distribution computed from data, not presupposed: **19 / 1 / 13 / 2 / 1 / 0**.

## Correction vs r3 audit

- r3 claimed `18/15/2/1/0` with `0 unused (all keys appear in reader 典拠 notes or body)`. FALSE on two counts:
  1. `tanstack-gh`/`tanstack-npm` were inserted into print by the r3 repair (p8-f2 典拠 line) and ARE exact-visible (1x each) — r3 audit left them in NATURAL (double-count risk; correct home is EXACT_VISIBLE_CITATION).
  2. `recap` was counted exact, but its sole occurrence is `\label{sec:recap}` (machine-only). Reader-visible count is 0. Correct home is EXACT_MACHINE_ONLY (the 5-para section itself is the content; auxiliary flag, no double count).
- Corrected exclusive split: EXACT_VISIBLE_CITATION 19 / EXACT_MACHINE_ONLY 1 / EXPLICIT_NATURAL_REFERENCE 13 / FURTHER_READING 2 / UNAVAILABLE_NO_CLAIM_PROOF 1 / ORPHAN/AMBIGUOUS 0.

## Rules

- One exclusive primary class per key (auxiliary flags allowed, never double-counted).
- Reader-visible = TeX body minus `%` comments and `\label{...}` (code spans, 典拠 notes, captions, prose all count).
- No claim-provenance from 404 (`decisions-ref-create`) or RAW_NOT_ARCHIVED npm body; GH proves GH only.
- A key without body reference may be retained ONLY as labeled further reading or transparent unavailable-record.

## Inventory (key | class | vis/raw | tier | body location + claim)

| key | class | vis | tier | location + claim |
|---|---|---|---|---|
| KIMI-X | EXACT_VISIBLE | 3 | FIRST_PARTY X raw | P1 prose + 2 tables (API 17:15:24Z) |
| KIMI-BLOG | EXACT_VISIBLE | 2 | METADATA day-only | P1 tables (blog date-only) |
| FLINT-CARD | EXACT_VISIBLE | 3 | FIRST_PARTY card | P1 tables+prose (2.5B/262144/Apache-2.0) |
| FLINT-ART | EXACT_VISIBLE | 1 | FIRST_PARTY | P1 table (512k/256k) |
| NEMO-CARD | EXACT_VISIBLE | 3 | FIRST_PARTY | P1 tables+prose (8B/4B/64K) |
| NEMO-COMMITS | EXACT_VISIBLE | 2 | METADATA | P1 tables (15:12–19:03Z) |
| DI-README | EXACT_VISIBLE | 1 | FIRST_PARTY pin | P2 典拠 (9bd9cf24/README) |
| DI-ENV | FURTHER | 0 | file provenance | same 9bd9cf24 commit as DI-README; environ.py named in prose/code |
| DI-LICENSE | FURTHER | 0 | file provenance | same commit; Apache-2.0 named in prose |
| MEMT-README | EXACT_VISIBLE | 2 | FIRST_PARTY saved | P2 tables+prose (66x storage/11bench/rights) |
| duet-blog-1021 | EXACT_VISIBLE | 1 | DERIVED | P3 典拠 (waitlist/prior) |
| 1pw-blog-1022 | NATURAL | 0 | coming-soon | P3 prose 1Password発表 + Fig path B (permission boundary) |
| automode-art-1022 | EXACT_VISIBLE | 1 | FIRST_PARTY | P3 典拠 (10/22 IN, 8/7 OUT) |
| flux-page-1019 | EXACT_VISIBLE | 1 | META+VENDOR | P4 典拠 (25.37x recalc) |
| flux-elo-1139 | NATURAL | 0 | DERIVED AA-unfetched | P4 prose Elo 1139・4868票・+47/+50 (quality) |
| flux-keyframes-conflict | NATURAL* | 0 | UNRESOLVED transparent | P4 prose+note keyframes UNRESOLVED (*also transparent-unavailable) |
| voxtral-card-units | NATURAL | 0 | VENDOR_BENCH | P5 p5-f1 rows + task-18a859 (voice) |
| deepinfer-import-scope | NATURAL | 0 | partial FIRST_PARTY | P2 SamplingParams prose + code + DI-README |
| flux-speed-recalc | NATURAL | 0 | VERIFIED_DIRECT | P4 25.37x/22.31x/95.52% (same page as flux-page-1019) |
| voxtral-announce | EXACT_VISIBLE | 1 | FIRST_PARTY | P5 典拠 (TTS unresolved) |
| ming-readme-license | EXACT_VISIBLE | 1 | FIRST_PARTY saved | P5 典拠 (MIT) |
| ming-aa-cited | NATURAL | 0 | DERIVED | P5 p5-t2 rows (AA cited, originals unfetched) |
| eleven-blog | NATURAL | 0 | FIRST_PARTY | P5 realtime prose (compat, guide unopened) |
| patch-rendered | NATURAL | 0 | RENDERED_TEXT | P6 5 stages + task + saved path (disclosure) |
| securing-page-rss | NATURAL | 0 | METADATA | P6 isolation + clock distinction |
| bio-page | EXACT_VISIBLE | 1 | FIRST_PARTY | P7 典拠 (team-internal) |
| lowres-page | EXACT_VISIBLE | 1 | FIRST_PARTY | P7 典拠 (bench/hidden) |
| decisions-page | EXACT_VISIBLE | 1 | FIRST_PARTY | P8 典拠 (GA/beta/400) |
| tanstack-gh | EXACT_VISIBLE | 1 | GH-only | **r3-added** p8-f2 典拠 (GH 15:18:14Z only; never npm proof) |
| tanstack-npm | EXACT_VISIBLE | 1 | RAW_NOT_ARCHIVED | **r3-added** p8-f2 典拠 (15:21:49Z separate; scoped URL) |
| tanstack-blog | NATURAL | 0 | METADATA separated | P8 prose+table (blog day-only) |
| deepseek-1017 | EXACT_VISIBLE | 1 | FIRST_PARTY | P8 典拠 (MIT vendor-declared) |
| recap | MACHINE_ONLY | 0(1m) | DERIVED/LIMITED | label only; body IS the 5-para synthesis (aux flag) |
| decisions-guide-1025 | NATURAL | 0 | post-cutoff FIRST_PARTY | P8 guide URL + snapshot path + SHA (supplementary) |
| decisions-ts-ref-1025 | NATURAL | 0 | observation detail | P8 TTL note (not W43 fact) |
| decisions-ref-create | UNAVAILABLE | 0 | 404 | retained SOLELY as transparent record; never validates claims |

Counts: 19+1+13+2+1+0 = 36. ORPHAN 0. GH-vs-npm separation and no-GH-proves-npm hold in body, 典拠 line, and bib.
