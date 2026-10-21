# W42 Muse r11 — Bounded Japanese Draft editorial repair proposals and immutable-adoption proof

**Status:** `EXECUTION_AUTHORITY / EDITION_LOCAL_DRAFT_PROPOSALS_ONLY / FROZEN_CORE_UNCHANGED / STOP_AT_SOL_REVIEW`  
Date: 2026-10-18 JST  
Repo: `eariver/japanese-generative-ai-survey`  
Existing branch: `weekly/2026-W42-v2-work`

## 1. Mandatory guarded start

Sol dispatch provides Exact remote Starting HEAD/Tree. Independently check **remote branch HEAD AND tree**, reviewed `main` HEAD `c8d0ecc1c9566a2303ad3b4c42635d4b672650e4` / tree `801de813319f08777ab1581a5e8875fc1ac5df19`, frozen `production/survey-core-v2` HEAD `774dd39a951c9ac3818e83dfffd4c7666efb0a20` / tree `cd46a6f7a6dcc4031e76220cea4c52c7dd1fc481`. Any mismatch: **ZERO WRITES / STOP** and report actual. No new/review/fallback branch, Core edit, shared `scripts/`/`schemas/`/`config/`/`.github/` edit, Force/rebase/reset/silent rewrite.

Before work read completely:
1. `sources/2026-W42/execution/reviews/sol-w42-r10-independent-japanese-draft-audit-REQUEST_CHANGES-20261018.md` — **authoritative B01–B05 and M01–M05 findings**.
2. Human Architecture r1 approval `sources/2026-W42/execution/human-architecture-approval-basis-r1.md`, Sol r9 Human dossier, Sol `sol-w42-r9-claim-provenance-editorial-errata-20261017.md`, accepted r9 Architecture and source crosswalk.
3. All seven canonical `sources/2026-W42/draft/v2/packages/P*/draft-result.json`, their bound package JSONs, Core Draft validators, synthesis input/result, actual State/checkpoint/provenance and `execution/draft-reader-preview-r10.json` + `execution/draft-citation-ledger-r10.json`.
4. Read-only W41 r11–r15 editorial repair, adoption and publication records to understand how its frozen `DRAFT_COMPLETE` stage was later used without rewriting checkpoint-bound canonical content. Do not assume a W41 workaround is lawful for W42 until exact Core contract/provenance validation is demonstrated.

## 2. Immutable boundary

Current W42 machine State **`DRAFT_COMPLETE`**, Architecture Human Gate **approved**, Publication Preview **pending**. The r10 Canonical Draft 7 Results, packages, synthesis, architecture, reviews, gate records and all accepted checkpoints are SHA-bound. They MUST stay untouched. **Do not run a Core stage rewind or re-advance by hand**; do not overwrite, delete or relocate `draft/v2/packages/P*/draft-result.json`, `draft/v2/profile-synthesis-*.json`, `draft/v2/interactive-drafting-synthesis-input.json`, `production-state.json`, checkpoint `ARCHITECTURE_ESTABLISHED.json`, or any prior accepted data.

All amended drafts must reside under NEW distinct **edition-local, non-authoritative** `sources/2026-W42/execution/editorial-revision-r11/` paths. Clearly label `PROPOSED / NOT_CANONICAL`. No assumption a proposed result may replace an accepted Core artifact in a later production step; assess allowed adoption separately.

## 3. Unit A — repair all Sol mandatory findings while retaining technical substance

**D10-B01 OSI correctness (mandatory).**
- Replace P3 `p3-n1` blanket false `OSI承認は本号のいずれのライセンスにも成立していない`. The OSI itself lists `Apache License Version 2.0` as an **approved** license (https://opensource.org/license/apache-2.0). For Beam, the repository `LICENSE` is read as Apache 2.0; Granite/MiniCPM API tags say Apache 2.0 but model repository license-file evidence remains missing. OSI-approved **license text** does not automatically prove all model weights/third-party components are covered. For Muse/FLUX/LFM/OpenMDW distinguish custom/partially verified terms and OSI approval not established. Keep the license correctness and retrieval-evidence tiers separate.
- P3 `p3-p10` `Beamのように何でもできる` is too broad: Apache 2.0 requires preservation of notices/license/copyright/modified-state, subject to patent rules and third-party restrictions. Replace with meaningful bounded permissions, no unconditional use promise.

**D10-B02 no machine trace on the reader surface.**
- Preserve original Core `CLAIM_BOUNDARY` machine blocks as-is only in bound canonical r10 Draft. Create a revised editorial reader projection in the proposed sidecar filtering/block-mapping **by permitted reader block types** (HEADLINE/DECK/HEADING/PARAGRAPH/TABLE/NOTE) while retaining a separate private QA crosswalk of boundary IDs and actual limitations.
- Explicitly prove new proposed reader preview contains **zero** pipeline fragments `r7 card authority`, `No r7 finding recorded`, `AUTHORITY_CONSUMED`, `CLAIM_BOUNDARY`, internal checksum/validator status, non-reader English provenance. Do not blindly discard *substantive* cautionary content: preserve important license/benchmark limits in readable Japanese paragraphs or note blocks (with factual URLs).

**D10-B03 remove padded/metadata-like prose and replace with real explanatory reporting.**
- Rewrite all P1–P7, prioritizing exact flagged r10 blocks. Eliminate verbatim `実務への含意を書く。`, `もう一段読む`, `もう一度書く`, `良い記事だ`, `本号の仕事`, `P3に据えた理由`, `anchor`, draft-operator commentary, repeated numeric recaps, artificial statements about "how the author is writing". Keep professional analytical voice and actual reader utility. Retain full comparative depth and negative findings.
- Source-limited mechanism content instead: clarify memory vs focus state; numeric efficiency denominator; license differences/tradeoffs; Scion's WAL/lock-free/cache architecture and AI Scan vs AutoFix; Anthropic incident claim/independent limits; wet-lab G4/MSA artifacts/HITL and Earth autorater; independent legal model rank vs vendor-selected chart; no invented knowledge.
- Do not use paragraph count/page quota to pad or truncate. Record **paragraph/character counts after** revisions, the distinct new explanatory content vs deleted duplication, and estimated plan viability (not fabricated final PDF pages).

**D10-B04 Japanese lexicon/encoding.**
- Correct P4 `무制限` to `無制限`, P4 `疎疎チェックアウト` to accurate terminology from Scion source (sparse/virtual checkout), P5 table `误検出` to `誤検出`. Search Hangul, simplified forms, malformed runs and unnecessary lower-case generic English across ALL reader-visible headline, deck, notes, tables, paragraphs and synthesis reader summary.
- Human-readable Japanese generic terms: `独立評価の根拠` instead of `anchor`, `確認水準` instead of `tiers`, `部分的裏づけ` instead of `corroboration`, `評価方法` for generic `workflow` where accurate. Named techniques and proper nouns (MoE/HITL/QAD/MTP/MOPD/Minecraft) should retain exact form if appropriate. Avoid adding ungrounded explanatory definitions.

**D10-B05 provenance/publication conflation.**
- P6 passages speaking about `16ページの全文が抽出されている`, `39ページの報告は…全文`, `全文3報抽出` and similar must be changed to what the underlying academic paper *reports* with the accurate dated source URL, claims' experiment denominator and limitation. The r8 91 source records are derived short excerpts, **not 91 archived original full texts**. Move reader-irrelevant extraction/whether-a-PDF-was-downloaded into internal bibliographic/QA layer, not article body; do not hide genuine uncertainty or original-source gap.
- Treat mere vendor announcement and paper method evaluations as author evidence, not independently replicated. No independent EXO Pareto or unsupported AA model rank. Future/previous-window dates must be correct.

## 4. Unit B — resolve Sol major issues

- **M01** align P5 `三層` vs FOUR actual rows; clarify mechanism/safety/independent evidence/access. If retaining 4 dimensions, name them correctly and explain different objects instead of misleading 3-layer headline.
- **M02** review source-referent per **numerical/license** clause; inherited Core Evidence refs can include many all-task sources, but reader citations must point directly to the one-best matching official original source (and independent Vals original when truly sourced), never bulk random refs. Record every corrected source/use category in a machine-readable `citation-repair-ledger-r11.json`, 28 candidates/7 chapters. Split composite sentences when Meta release, independent evaluator, X poster observations have different provenance.
- **M03** improve substantive depth and identify omitted counter-evidence without raising unsupported/new launch items. P3 rights/model table, P6 science methods, P2 Maia architecture, P4 engineering operations, P7 law/robotics/perception must stay in good shape. Add a domain/robotics comparison TABLE for P7 if it truly improves reader comprehension, not a formal table quota; calculate approx body char/space.
- **M04** produce coherent reading order and block ID mapping; do not auto-sort numeric IDs if it damages narrative flow. Remove duplicative late 'pN-p8/p9' conclusion appended after 'pN-p15...' in all seven; preserve stable provenance or explicitly reconcile old→new.
- **M05** distinguish 'no independent reproduction of claimed vendor benchmarks' vs 'Vals independently performed its separate GLM-Legal evaluation'; specify which chart omits six higher-scoring systems and who chose that display. De-ambiguous 'Maia 200 vs unnamed baseline', dates/units and wet-lab conclusions using source text only.

## 5. Unit C — proof and acceptable stopping point

Produce under `execution/editorial-revision-r11/`:
1. Seven proposed `P1..P7/draft-result-r11.PROPOSED.json` or path-equivalent with all complete canonical-shaped Draft Result fields, no shrinking to excerpts. When Draft validator can accept alternative results against the existing bound `draft-package.json`, run the **unmodified frozen** validator for each, and profile extension equivalence. No re-generation of source material changing accepted Authority.
2. Human-readable `reader-preview-r11.PROPOSED.json` and `reader-preview-r11.PROPOSED.md` as real seven full chapters (readable prose + tables + notes), **with reader-facing metadata filtered**. Reader preview and proposed Draft Results must have a documented equality/mapping for every visible block. If source schema *requires* internal `CLAIM_BOUNDARY`, retain it **within the proposed Draft Result for validator** and filter only the publication projection; do not change Core schema.
3. Proposed synthesis result and any required complete proposal input; exact original-vs-revision binding, SHA and diff ledger. Draft/source citation+confidence crosswalk repaired claim-by-claim. B01–B05/M01–M05 closure table, textual counterexample evidence, OSI official URL and negative scans, paragraph/characters/tables by chapter, research source gaps.
4. **Adoption feasibility proof**: read-only inspect unchanged Core Stage/Publication/Reader validators and W41 release precedent. Report specific permissible public Reader/Publication stage API(s) capable of consuming edition-local corrected reader prose **without modifying checkpoint-bound r10 Draft or lying about basis**. Test using a temporary copy/sandbox when possible; do not touch live `DRAFT_COMPLETE`. If no lawful stage adoption exists, mark `BLOCKED_CORE_CONTRACT` and propose a bounded alternate implementation through later authorized surface—**no Core edit** and no fake approval.

Stop boundary: **`SOL_W42_JAPANESE_DRAFT_REVISION_R11_REVIEW_READY`** for seven credible substantive amended proposals, or earlier exact documented Core incompatibility. Do NOT mutate canonical Draft, State, Gate, checkpoint or accepted upstream bytes. Do not create TeX, PDF, publication candidate, visual/reader-surface Gate, Publication Preview, Freeze, Release or main merge. No user-Human Architecture amendment is implied: approved architecture unchanged.

Use **normal commit and non-force push to existing W42 branch** and report final exact HEAD/Tree, validator results, editorial changed-blocks count, licence/reader technical blockers resolved, and limitations. If the rewritten article changes 28 selected candidates, package placement or page_plan, STOP for Sol decision instead of secretly changing Architecture.
