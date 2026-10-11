# Muse W40 r22 — PROPOSED correction after a new explicit Human Publication Preview REQUEST_CHANGES

Status: `CONDITIONAL_NOT_YET_AUTHORIZED / DO_NOT_EXECUTE_UNTIL_HUMAN_PREVIEW_REQUEST_CHANGES`
Date: 2026-10-11 JST
Repo: `eariver/japanese-generative-ai-survey`
Existing branch only: `weekly/2026-W40-v2-work`
r21 canonical PDF/State review target commit: `832808af95df29547d7050452fdac7bb3df80f2e`, tree `fbedf5e070a6816e83affe429dbaa8454c544873`.
Sol audit: `sources/2026-W40/execution/reviews/sol-w40-r21-publication-preview-editorial-audit-20261011.md`.
Reviewed main: `afdb3df3faa20af3bb5798be429bba8dbd2100b1`.

**NOT AN EXECUTION PERMISSION.** This is a draft repair contract only. User's last statement reported Muse completion and does NOT decide the Human Publication Preview. Do not run a Core Gate change, delete files or publish anything until the Human Owner explicitly decides `REQUEST_CHANGES` after reading this audit, and a separately SHA-guarded Muse invocation authorizes work.

## Repair target

Human-preserved Architecture r20, 28 SELECTED (20 PRIMARY/8 SUPPORTING), 9 packages, all 113 original Candidate-to-boundary relations, 105 package-level entries and 97 globally distinct strings, full r15/r16 technical prep and r20 timing erratum. Keep all accepted upstream/Selection/Architecture/Architecture approval and Core #562 unchanged.

Redo Draft article prose **substantively**, not by padding or word swapping:
- P1 all 3 price cards and availability/benchmark provenance, with a grounded per-vendor table.
- P2 Holo4/ELYZA variant/license/benchmark table with explicit denominators/split/attribution.
- P3 accurate Sep29/Oct1 chronology, interface vs weights/API vs pointer head distinct, sources, reference metrics and constraints.
- P4 actual computer-use workflow vs changelog-only bounds, dots product and hub supporting role.
- P5 five meaningful subsections (provenance evaluator, runtime and reference architecture, bio watermark laboratory evaluation, safety-case guidance, OAuth spec).
- P6a ContextLM Eq.3/Eq.5/Eq.6 precisely explained including fixed θ vs RL updates and data split, distinct SCR/BCP baselines/denominators; Olmo MoE experts/grouped GEMM/MXFP8 systems, numeric experiments, 47B/1.2T/2.38T controlled scope + negative experiments. Add appropriate explanation tables/formulae.
- P6b AgentPerf serving-only measurements/roofline, OpenTTS protocol plus article/script dated availability and RL Hub framework version vs taskset revision.
- P7 show which FLUX resolution corresponds to each of four prices, separate VSS demo, ASR WER/setup, Relay tracing, Ross small supported note.
- P8 brief digest may remain short, but accurate and natural.
- Replace systematic overtranslation with clear professional Japanese. Refer to the actual project style guide. `模型`→model, `市庭`→企業・業界, `口` in technical API contexts→API interface, `写し`→script/repo file per actual fact, `団子記事`→publisher/team blog, `協定時`→UTC. Rewrite semantically, not string substitution. Preserve exact proper names and source reference vocabulary. Eliminate meaningless metaphor.
- No hard page cap; assess content-first by article structure, full must-cover explanation, evidence-bound metrics/denominators, readability, contextual synthesis, comparison visuals and user-meaningful implications. Candidate count alone and a short paragraph per primary MUST NOT be accepted as editorial completion.

## Legal path, only AFTER Owner REQUEST_CHANGES

1. Preflight remote work HEAD/tree and reviewed main, current `RELEASE_CANDIDATE / PUBLICATION_PREVIEW / HUMAN_GATE_REACHED`, Architecture APPROVED/provenance pinned, Preview pending/null; exactly one Architecture approval review, zero Preview reviews; valid candidate and PDF; clean worktree, no new branches.
2. Official frozen Core `scripts/survey_human_gate_v2.py request-publication-preview-revision` with `--state sources/2026-W40/production-state.json`, `--expected-revision 1` if formally checked, `--regeneration-boundary ARCHITECTURE_ESTABLISHED`, exact issue change request, `--reviewed-by 'Human Owner'`, real formal-record `--reviewed-at`, audit+owner decision `--review-reference`, SHA-pinned `--reviewed-commit-sha` at real reviewed Candidate bytes. Must officially produce Human review record `REQUEST_CHANGES`, review-index revision, lawful State `ARCHITECTURE_ESTABLISHED` while preserving Architecture approval. NO operator pending-Gate invalidation: config expressly forbids it after Architecture approval.
3. Commit normal FF and read back; then investigate exact Core Draft version/immutable singleton rules, self-contained validation and allowed regeneration strategy. No illegal overwrite/checkpoint editing. Draft body must be reauthored with explicit coverage+style audits BEFORE TeX. Keep authoritative claims/source bounds. Generate new staged official Review and PDF, revalidate SHA-anchored authorities in stages, and stop at FRESH pending Human Publication Preview; do not re-APPROVE previous review.
4. Independently inspect actual per-package prose and source-to-claim mappings, TeX comparisons, actual PDF all pages (render with full-resolution renderer, not 60dpi only). Correct prior stale 370,741-byte documentation on new actual binary. QA must be materially defensible, not only PASS tags.
5. No Core/schema/config/main/other editions changes, no HOLD promotion (AstaBrief, AutoSynthData, Pixel Canary, TBC/AWS), no Preview approval, Freeze, Release.

If anything cannot be lawfully reauthored without modifying frozen Core: STOP with exact blocker and concrete legal options. Do not fabricate or overstate user permission.


## Independent Sol High audit addendum — BEFORE Human authorization (2026-10-11)

This document remains `CONDITIONAL_NOT_YET_AUTHORIZED`. The blind-first, read-only independent reviewer concluded `SUBSTANTIVE_REWRITE_REQUIRED`; Sol adopted the independent findings in `execution/reviews/w40-r21-independent-publication-editorial-audit-adoption-20261011.md`. Do NOT treat the independent verdict as the Human Owner's `REQUEST_CHANGES` decision.

1. **Boundary unit correction:** 113 per-candidate original literal relations, 105 architecture entries summed across packages, 97 globally distinct strings. Earlier phrasing '105 unique strings' meant unique only within each package. Preserve identical content.
2. **All 31 must-cover:** Require direct on-page paragraph/table/equation evidence for each individual requirement. File-level `FULFILLED` annotations are insufficient. Explicitly verify model/variant licenses, pricing tables, benchmark denominator/method/baseline, Eq3/Eq5/Eq6, five safety subsystems, evaluation metric definitions and the source-bound operation of major technologies.
3. **Synthesis repair:** Rebuild profile-level synthesis and frontmatter/week-in-review, not merely nine individual package bodies, because unnatural vocabulary propagated beyond Draft packages.
4. **P7 time escalation:** Original approved Architecture's P7 requirement itself says `Oct 1 session post-window` but W40 cutoff is Oct 2 22:00 UTC. Verify the specific issuer source/event and timezone before any textual chronology change; do not silently alter frozen approved Authority. If Architecture factually contradicts the source, STOP and request separate lawful cross-gate human revision with an appropriately earlier boundary; `ARCHITECTURE_ESTABLISHED` would not authorize changing approved Architecture.
5. **PDF metadata:** Correct stale worker narrative 370,741 bytes vs canonical 369,980; after regenerated PDF recompute and bind NEW exact raw-byte length/hash; independent visual review of all pages remains to be done.
6. **Published Japanese:** Prefer natural technically precise terms to coined synonyms. Qualitative editorial review must independently examine actual prose, not merely evidence refs, schema validity or a static lexical dictionary PASS. Supporting-only P8 stays concise.
