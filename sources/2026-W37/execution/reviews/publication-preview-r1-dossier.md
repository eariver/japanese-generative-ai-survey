# Human Publication Preview dossier — 2026-W37 r1 (PENDING)

Status: `RELEASE_CANDIDATE / HUMAN_GATE_REACHED / PENDING_HUMAN_DECISION`
Date: `2026-09-19`
Revision: `r1` (first Publication Preview; no prior Preview decision)

This dossier was assembled by the worker from frozen approved authority. It is not an independent Sol review and not a Human decision. Independent Sol review and Human judgment remain pending.

## 1. Exact review identity

- Edition `2026-W37` (WEEKLY + WEEKLY_MAGAZINE), target gate `PUBLICATION_PREVIEW`.
- Reviewed commit `8057a468897f67d3a11bd9287f6f56f0485877ce` (State + Candidate + Candidate-bound PDF).
- Lifecycle `RELEASE_CANDIDATE`, terminal `HUMAN_GATE_REACHED`, next `PUBLICATION_PREVIEW`.
- Candidate `sources/2026-W37/publication/v2/publication-candidate-v2.json` (candidate SHA `1dfb87957cbab69e30c08a45c66e72b28c72d74d1272a3c3815ab6844445bef6`, file SHA `31d4ec4d21e43f56678cb19f7341f11039bb03c8420d78b526fd5ac1eaf513ce`).
- PDF `surveys/weekly/2026-W37/main.pdf` (10 pages, 301238 bytes, SHA `08ceb5e9c90b2bf25541bb61e6b14e5b2cdc7fe48635d85c5ab798606b88fd4d`, CI run `35365392701`, artifact `10556277977`).
- Manuscript `sources/2026-W37/publication/v2/reader-manuscript-v2.json` (manifest SHA `a4c6990287fd9bfb284b7354b460fe7708d007dfed36a46a69a6e90171aacdb8`, file SHA `b95c24eaedf0c6ca97a52a323eaf98040bcf1c542ed67fcd55c9fd4b360f0468`).
- Architecture approval: Human r1 `APPROVED` for r2 content (reviewed `55e700a34765654cd2ced0c2a454d4fb3433dd4f`, Architecture SHA `81e87a64c2418c71340ee8cc1dec28267a55055d2c02d7dbb06e33623efdfcfb`).

## 2. Architecture approval provenance

- Human Architecture Review r1 `APPROVED` recorded canonically via `survey_human_gate_v2.py` (reviewed-by Human Owner, reviewed-at `2026-09-18T15:47:01Z`, reference binds execution request + `architecture-r2.md` + independent Sol r2 review).
- Review record `sources/2026-W37/gates/reviews/architecture-r1.json`, snapshot `sources/2026-W37/gates/reviews/approvals/architecture-r1.json`, index `sources/2026-W37/gates/review-index.json`.
- r1 Architecture surface was invalidated as unpresented (operator record `execution/operator-invalidations/architecture-invalidation-0001.json`); no Human r1 invented. First canonical Human decision revision is therefore `1`, derived from empty index.
- Frozen upstream counts preserved: Discovery 14, Screening 13 KEEP / 1 DROP, Evidence 11 VERIFIED / 2 PARTIAL, Materiality 12 MATERIAL / 1 CONTEXT / 1 EXCLUDED, Selection 12 SELECTED / 1 HOLD, Architecture 7 packages.

## 3. Actual section/package structure

Seven sections in approved drafting order plus frontmatter, synthesis and source notes:

1. `sections/10-astra-vertical.tex` — Financial Services on Astra (PRIMARY plus X supporting)
2. `sections/20-voice-frontier.tex` — GPT-Live-1 as separate delegating voice layer
3. `sections/30-harness-plane.tex` — Agents API beta plus Fusion (verified ordinary 17:00Z)
4. `sections/40-efficient-flagship.tex` — DeepSeek V4.1-Flash vendor-framed with Sep 14 future-tense
5. `sections/50-frontier-coding.tex` — SWE-2 with benchmark/cost/harness bounds
6. `sections/55-open-vertical.tex` — MiniCPM (Sep 7) + North (judge/license) + Ling (date-bound)
7. `sections/57-safety-bound.tex` — Anthropic threat report with notable-examples bounds

Frontmatter `sections/00-frontmatter.tex` carries contents, This Week in AI and cutoff. Synthesis `sections/60-week-in-review.tex` closes with center/constraint/next-watch. `sections/99-source-notes.tex` states primary sources, temporal/vendor/community boundaries and non-elevated items.

Draft identity: 7/7 Draft Packages/Results plus synthesis input/result under `sources/2026-W37/draft/v2/` (stage validation PASS, checkpoint `orchestration/v2/checkpoints/ARCHITECTURE_ESTABLISHED.json`, State `DRAFT_COMPLETE`).

No package merged or reordered against approved thesis. Resignation discourse absent from thesis/packages (HOLD/CONTEXT, no weight). GLM rumor absent (DROP/EXCLUDED).

## 4. Drafting compression

No selected material deleted for page target. Moderate 10-page length accepted. All seven packages present with per-package claim boundaries. No required caveat removed.

## 5. Exact source/citation behavior

- Primary source `surveys/weekly/2026-W37/main.tex` (file SHA `157cbfd5873c6b6818ef1a933f4b347a365b40d61d2a324443b8b3ec2bf9aa6c`) plus 10 supporting sections, `references.bib` (19 records), `jgaisurvey.sty`.
- Bibliography: 11 primary official authorities (OpenAI x3, DeepSeek x2, Cognition x2, OpenBMB, Cohere, InclusionAI, Anthropic) plus 8 direct X status URLs.
- Citation scan: 19/19 cited keys resolve with no missing or unused keys (deterministic `subject-entity-property-binding.json` PASS).
- No repository-internal Raw paths or internal GitHub blob URLs in reader citations. No `surveys/` path spans in bibliography URLs.

## 6. X/community public auditability

- Accepted Raw `sources/2026-W37/external/x/weekly-x-2026-W37/raw/grok-x-result-r3.md` (45 direct URLs: 24 ordinary / 1 pre-window / 20 late-breaking; 12 ordinary independent accounts).
- Reader uses 8 ordinary direct X status URLs as auditable citations: 2 Astra (official + independent), 2 DeepSeek (official + independent), 2 coding/harness (official + independent), 2 MiniCPM (official + independent).
- Community language confined to attention direction; no spec/benchmark/license/release fact established by posts. Pre-window/late-breaking kept outside ordinary totals. Row-level ledger governs.
- North community signal (2 thin posts) not elevated to standalone citation; covered by synthesis-level movement note only.

## 7. Vendor-claim boundary

- Financial Services benchmarks (OfficeQA 69.9 vs 60.2) vendor-reported; methodology unconsumed; pricing/limits absent.
- GPT-Live-1 bench (Full Duplex +30pp, Tau3 first) vendor-reported; language/telephone scope incomplete.
- Agents API beta scope/GA/limits absent; partner/customer claims vendor-described.
- DeepSeek ahead-of-Pro vendor-attributed with unnamed parties; Sep 14 routing future operation; in-window pricing separate; per-token image values unconsumed.
- SWE-2 all benchmarks vendor-run/compiled; list-pricing cost sensitivity.
- Fusion partnered methodology unconsumed; 39 percent maximum with per-benchmark deltas; untested pairs not generalized; published_time `2026-09-11T17:00:00Z` ordinary with 5-hour margin.
- MiniCPM/North/Ling card-reported unreproduced; North judge-model and CC BY-NC bounds; Ling hour unresolved with Sep 4/8/10 phasing.
- Threat cases vendor-reported investigations; full PDF/IOCs unconsumed; Sep 11 naming detail late-breaking excluded.

## 8. Treatment of PARTIAL/HOLD/EXCLUDED inputs

- X ledger PARTIAL used as SOCIAL_OBSERVATION only in supporting role; never technical authority.
- Resignation PARTIAL/CONTEXT (HOLD, NONE) appears nowhere in thesis/packages; excluded from safety package by boundary.
- GLM rumor DROP/EXCLUDED nowhere surfaced.
- Internal disposition tokens (HOLD/PARTIAL/VERIFIED etc.) absent from reader prose; lexical gate PASSED on all 12 TeX/Bib files.

## 9. Japanese-language quality

- Natural technical Japanese targeted; noun-stack calques and repeated positioning phrasing avoided; qualifier dumps moved to claim boundaries and source notes.
- Lexical gate PASSED (0 blocking findings, 0 suppressions) on all TeX/Bib files after one edition-local repair (Contents `Bound` to `in Context`).
- Worker-authored semantic review (Worker/Agent, 5 PASS) plus ChatGPT semantic/editorial review (11 PASS) confirm reread against frozen Drafts with no new facts and preserved precision.

## 10. Page/layout state

- Exact CI PDF: 10 pages, 301238 bytes, SHA `08ceb5e9c90b2bf25541bb61e6b14e5b2cdc7fe48635d85c5ab798606b88fd4d` (run `35365392701`, artifact `10556277977`, warning gate PASS, text extraction clean).
- Quality bundle PASS (3 deterministic: identifier-preservation, pdf-preflight, subject-entity binding).
- Visual review PASS (2 checks: rendered-page review across pages 1-10, exact-PDF visual review).
- No layout breakage, no unreadable density, no severe duplication.

## 11. Remaining non-blocking limitations

- All vendor benchmarks externally unreproduced; judge/partnered methods unverified.
- OpenAI pricing/entitlement/language/telephone scope gaps explicit.
- Fusion partnered methodology beyond vendor summary unconsumed.
- Ling hour precision unresolved; Sep 8/10 bindings carry relevance.
- Threat full PDF/IOCs unconsumed; Sep 11 detail excluded.
- Image/video lanes quiet as finding, not proof of absence.
- None requires Architecture regeneration.

## 12. Deviation from approved Architecture

None. Thesis, package order and must-cover/boundaries preserved. No upstream rerun or Architecture change after approval.

## 13. Review provenance downstream

- Worker created: worker dossier (this file), deterministic validation outputs, TeX source, manuscript/bundle/candidate bindings.
- Worker did not self-author: independent Sol review, Human review, Sol verdict. Semantic reader-surface review labeled Worker/Agent explicitly.
- Fresh Preview r1 awaits independent Sol review and Human judgment. No Preview decision recorded.

## 14. Human decision options

- `APPROVED` records against reviewed commit `8057a468897f67d3a11bd9287f6f56f0485877ce` and continues to Freeze (not authorized here).
- `REQUEST_CHANGES` requires explicit changes plus allowed boundary (`ARCHITECTURE_ESTABLISHED`, `DRAFT_COMPLETE`, `VALIDATED_DRAFT` publication-local; upstream triggers cross-gate reopen).
- Silence infers nothing.
