# Earth benchmark source-discrepancy audit (F-02; r15, read-only)

Date: 2026-10-18 JST. Status: `UNRESOLVED_DOCUMENT_DIFFERENCE — reported side-by-side, NOT reconciled by guessing`.

## Claim under audit
r14 P6 text (and accepted card claim-2) states GeoKTools `305 = 85 dev + 220 test`.

## Source A — arXiv paper 2610.15750v1 (S2/S6)
- GeoKTools: **305** templated queries, **220 held out** for testing, drawn from **92** expert-written templates, 24 tool types.
- Dev: **18 templates (2/12/2/2)** → **85 queries (10/50/15/10)**.
- Test: **74 templates (7/52/9/6)** → **220 queries (30/110/50/30)**.
- GeoExpertQueries: 101 = 25 dev + 76 test. CBGB: expert-curated external set, count 45 per accepted Evidence (no conflicting count in fetched paper text).
- Access: webfetch text 2026-10-18 (S2 retained + S6 re-grep).

## Source B — public repo README (S4)
- URL: https://github.com/google-research/geospatial-reasoning-benchmarks (1 commit history visible; SHA unknown, NOT fabricated).
- GeoKTools: **85 dev** queries (K=1:10, K=2:50, K=3:15, K=4:10; **19 templates**) + **210 held-out test** queries (K=1:30, K=2:100, K=3:50, K=4:30; **72 templates**). Tests kept private.
- Released: dev JSON ×2, 19 template specs + pseudocode solvers, autorater prompts + runners, deterministic scorer, tests/, docs/PROVENANCE.md, CITATION.bib.
- GeoExpertQueries: 25 dev + 76 test = 101 (MATCHES paper).
- Licenses: Apache-2.0 (code) / CC-BY-4.0 (data); Google Maps Data + third-party data excluded with own terms.

## Difference table (do NOT merge)
| scope | paper | repo README | status |
|---|---|---|---|
| GeoKTools total | 305 | 295 implied (85+210) | DIFFERS — origin unknown |
| dev queries | 85 (10/50/15/10) | 85 (10/50/15/10) | MATCH |
| dev templates | 18 (2/12/2/2) | 19 | DIFFERS — origin unknown |
| test queries | 220 (30/110/50/30) | 210 (30/100/50/30) | DIFFERS — K=2: 110 vs 100 |
| test templates | 74 (7/52/9/6) | 72 | DIFFERS — origin unknown |
| GeoExpertQueries | 101 = 25+76 | 101 = 25+76 | MATCH |
| CBGB | expert-curated, 45 per Evidence | n/a (external) | NO CONFLICT FOUND |

## What was actually released (positive statements only)
- Downloadable now: 85 GeoKTools dev queries + 25 GeoExpertQueries dev queries with golden answers/workflows, 19 template specs, autorater prompts/runners, deterministic scorer, provenance docs.
- Withheld (private, never released): GeoKTools test split + 72 test-only templates; GeoExpertQueries test split. The text "210 withheld test" is the repo's number; the paper's "220" is the paper's number. Neither is called open.
- Evaluator/code available: yes (prompts, runners, scoring module, tests/).

## r15 prose rule adopted
Draft states the paper numbers WITH the repo numbers side-by-side and labels the test-set delta unresolved (see P6 new discrepancy note block). Withheld tests are never called released or open. CBGB stated as external expert-curated set, count per Evidence.
