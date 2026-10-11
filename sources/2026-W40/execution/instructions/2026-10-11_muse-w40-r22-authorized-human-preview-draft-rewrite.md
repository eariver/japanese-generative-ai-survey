# Muse W40 r22 — authorized Human Publication Preview REQUEST_CHANGES; redo Draft to fresh Preview

Status: `HUMAN_OWNER_AUTHORIZED / CORE_V2_IMMUTABLE / EXISTING_BRANCH_ONLY / FRESH_PREVIEW_HUMAN_GATE_STOP`
Date: 2026-10-11 JST
Repo: `eariver/japanese-generative-ai-survey`, EXISTING branch `weekly/2026-W40-v2-work`
**Exact Starting HEAD/TREE: values from OUTER Muse invocation after this docs-only commit**.
Reviewed main HEAD/Tree: `afdb3df3faa20af3bb5798be429bba8dbd2100b1` / `fe3f07c653f255f67087b4b46d006f8943df7115`.
Explicit Owner decision: `sources/2026-W40/execution/human-authorization/2026-10-11_owner-w40-r21-publication-preview-request-changes.md`
Dual Sol editorial audits: `sources/2026-W40/execution/reviews/sol-w40-r21-publication-preview-editorial-audit-20261011.md` and `sources/2026-W40/execution/reviews/w40-r21-independent-publication-editorial-audit-adoption-20261011.md`.
P7 source chronology correction: `sources/2026-W40/execution/reviews/2026-10-11_w40-r21-p7-evidence-temporal-correction-note.md`.
Previous conditional draft contract: `sources/2026-W40/execution/instructions/2026-10-11_muse-w40-r22-proposed-post-human-preview-revision.md` (subsumed where consistent, NOT by itself an execution authority).

## 0. Strict freeze and preflight

Core v2 means **NO MODIFICATION** to any shared scripts/Core implementation, schemas, configs, workflows, code, tests, Issue #562, main, or other editions. No new/fallback/repair/review branch. No history rewriting, reset, force/rebase, and no hand-edited State/Gate/Checkpoint/Review record.

Before any writes, read remote exact work HEAD/TREE from OUTER invocation and `main` exact HEAD/TREE above; verify clean tracked working tree; verify ancestry to canonical Muse r21 `832808af95df29547d7050452fdac7bb3df80f2e` with no intervening changes to approved Authority. Check State `RELEASE_CANDIDATE / PUBLICATION_PREVIEW / HUMAN_GATE_REACHED`; Architecture APPROVED, Preview PENDING and provenance null, Draft/Validation passed; Freeze/Release pending. Verify one Architecture review r1 APPROVED and **zero** prior Preview decisions, original PDF and Candidate SHA exactly:
- PDF `surveys/weekly/2026-W40/main.pdf`: SHA-256 `f93d15f838cddf9489cc7ed6e73f3eb2cbe551044ac84a45cc41441fabf202ab`, 369,980 bytes, 12 recorded pages.
- Candidate `sources/2026-W40/publication/v2/publication-candidate-v2.json` SHA-256 `157c464481392b66387cb5b0cb7ba4d0bde53cffacc9d404aac1eede17ab15b2`.
- Approved Architecture `a9b5c1182671bb913fbf56972907e19731e5ba4a928deaca9903a0d3a1461a44`, Review Summary `32f39de0b7cb3e469acf74668c420c246fb67f273ecd0c37bda91557eaa98d30`, Review Attention `70ac43bdd0da014009f99abaf3aff00db8bdfbd9e44940ba087abf4cb5949319`, Architecture Approval `953f682a98d6a97687475cef84d3f094131fbcd4f18b21a4aac3b515011f5eb8`.
- Selection 28 (20P/8S) /4 HOLD/3 REJECT, 9 packages, **31 must-cover**, 113 original Candidate-boundary relations, 105 package-level entries, 97 globally distinct Boundary strings.
- Read-first r20 article-timestamp erratum and new P7 chronology correction note; do not carry stale inherited statements into body.

Any violation => ZERO WRITES, report expected/actual, do not silently 'repair'.

## 1. FIRST: record official Human Publication Preview REQUEST_CHANGES

The Owner explicitly authorized `PUBLICATION_PREVIEW / REQUEST_CHANGES` in conversation, recorded faithfully in `sources/2026-W40/execution/human-authorization/2026-10-11_owner-w40-r21-publication-preview-request-changes.md`, for the r21 candidate reviewed. After all preflight PASS, invoke the **unchanged** `scripts/survey_human_gate_v2.py request-publication-preview-revision` with:
`--state sources/2026-W40/production-state.json`
`--regeneration-boundary ARCHITECTURE_ESTABLISHED`
`--expected-revision 1` ONLY if review-index confirms no prior Preview revision.
`--reviewed-by 'Human Owner'`
`--reviewed-at`: **actual now UTC instant of formal record**, never fabricated message timestamp.
`--review-reference`: SHA-anchored Owner authorization doc, BOTH editorial audits, plus P7 correction.
`--reviewed-commit-sha`: current exact **previously reviewed** branch commit whose State and Preview Candidate match preflight; `7ca317615076d287945b56c09184cb7cab4609cd` is the reviewed content commit and ancestor of this docs-only authorization, whose files must still be byte-identical. For further docs-only commit, pass its own exact SHA only if Core mandates HEAD equivalence; otherwise use `7ca317615076d287945b56c09184cb7cab4609cd`.

`--requested-changes`: meaningful description of 31 unmet semantic must-covers, prose rewrite, terminology repair, profile synthesis, missing tables/formulae, publisher/repro boundaries, P7 in-window chronology correction (as bounded erratum preserving approved Authority), revised real PDF and meaningful QA. This is a **formal Human decision**, not operator invalidation. Core v2 remains immutable; do NOT implement Gate by direct JSON editing.

Review the actual CLI help and postconditions. Require official `gates/reviews/publication-r1.json` or the actual Core-version location, review-index with one Preview r1 `REQUEST_CHANGES`, State `ARCHITECTURE_ESTABLISHED` with Architecture approval/provenance preserved and Draft/Validation pending, and lawful cleanup of stale checkpoints. Establish normal FF approval/revision commit and remote readback before any article work. If expected filenames differ per CLI, derive them rather than inventing.

## 2. Reauthor Draft and Profile Synthesis, not a superficial TeX refresh

Correct genesis: previous **Draft** r21 had only 29 prose blocks over 9 packages (about 5,681 Japanese prose characters) and an unnatural calque lexicon, so TeX transformation faithfully emitted insufficient text. Do not regenerate from previous `draft-result.json` as the sole prose source or perform mechanical substitution. Author FULL natural technical Japanese from approved Evidence and r15/r16 technical prep, check against the editorial style guide `docs/editorial-style-guide.md` §1/3/8/11. Preserve model names, exact terms, numbers/denominators and source-scope; do not over-Hanji-translate. *No arbitrary page cap or target; no filler.*

Use a package-by-package **31-row actual semantics coverage ledger**: for EACH original `must_cover_requirements` text, link exact new Draft block ID and quote of real technical explanation plus any table/formula and exact source/limitation. Labels or references alone do NOT constitute fulfilment; each non-vacuous requirement must be satisfied in prose. A Worker PASS without demonstrated explanation is invalid; review actual prose before committing stage, invite source-specific contradiction checks and fail on thin paragraphs or math references without equations/definitions.

- P1: complete Sonnet 5.5 and Gemini 4 Argon price/availability cards plus GPT-6.1 Sol price, correct units, model-specific source/bench setup, grounded **actual** comparison table.
- P2: Holo4 27B/35B-A3B license distinction, actual ELYZA exact pinned SHAs, benchmark names/denominators, separate generalist/JA method, table physically present.
- P3: Ollama `/v1/systemone` interface vs Clef weights/API vs Strands Decider pointer-head, inputs/outputs, measured latency conditions, Sep29 vs Oct1 chronology, license.
- P4: Agents API computer use flow/approval/sign-in responsibility and scopes supported by source; dots operational constraints, DevDay only secondary; don't invent safety proof.
- P5: five individually meaningful subsections: ProvenanceGuard RARR/NLI and measure interpretations/limitations; OpenShell/Sentry roles; SynthID Bio experimental conditions; safety-case proposal != proof; OAuth spec != threat-resistance. Not one omnibus 'safety' paragraph.
- P6a: deep ContextLM Eq.3 (defined variables/FLOPs vs wall time), Eq.5 EXACT verified optimizer of skill `s` with frozen model params and heldout split, Eq.6 parameter updating GRPO and <2-success efficiency term behavior; SCR vs BCP baselines and denominators; Olmo-core 3 DDP/GPU expert routing/grouped GEMM/MXFP8 mechanisms and test conditions, 47B/1.2T/2.38T distinct, failed experiments and report-body limits. Actual equation(s)/comparison visuals where warranted, not mere name drops.
- P6b: AgentPerf serving-only scope/14 configurations, roofline comparison, TTFA, WER/CER/RTFx/SIM definitions and OpenTTS 50 prompts/warmups/median H200; Sep30 public statement vs Oct7 repo-scripts; RL Hub runnable reproducibility limitations and version/taskset/seed differences.
- P7: map all FLUX four prices to *correct exact source verified* resolutions and promo terms, VSS 17%/46%/-80% with metric name and vendor config, Najdi/Hijazi WER with SADA/FLEURS evaluation split, Relay ATOF/ATIF tracing and source limits, Ross SUPPORTING only. **P7 Oct1 scheduled event is IN WINDOW**, not post-cutoff; dedicated first-party correction note supersedes only erroneous inherited timing inference. DO NOT alter frozen approved Architecture or Evidence. Should formal compliance require editing approved Architecture, STOP and escalate for an additional Human-authorized earlier boundary, rather than faking 31/31.
- P8: supporting-only concise enterprise digest, unambiguous definitive agreement vs completed acquisition and service/pricing terms; no forced deep length.
- Whole issue: rebuild **profile-synthesis** and opening/closing sections using the rewritten conventional terminology and actual technical connections; separate analysis from fact, keep four-row X observation context-only.

No HOLD/REJECT promotion; Core #562 handled elsewhere. External source clarification required only for already approved source subjects; do not insert new candidate, post-cutoff announcements or invented new conclusions. If a core accepted claim itself proves false beyond bounded P7 erratum, STOP with truthful source evidence and lawful gate options.

## 3. Lawful regeneration and quality-review constraints

Published Draft/TeX/PDF quality must improve substantially before validating. Inspect the exact Core behavior of `request_changes`: it clears stage checkpoints/provenance but may **NOT delete all old immutable Draft/publication singleton JSON and PDF bytes**. DO NOT overwrite immutable values illicitly, spoof/checkpoint State, or invoke operator pending-Gate invalidation (explicitly forbidden for `PUBLICATION_PREVIEW`). Determine whether existing edition-local supersession/revalidation/archival path supports new output. Where a singleton legitimately needs replacement after the official Human Gate revision, retain original bytes/hashes in Git ancestor and a documented authoritative supersession/cleanup report, use normal non-force commits, rerun unchanged Core validators. Do not claim supersession works before demonstrated; if frozen Core cannot lawfully regenerate Draft at same paths, STOP with exact blocker and propose a solution requiring *no Core v2 modifications* before any bypass.

Stages: `ARCHITECTURE_ESTABLISHED -> DRAFT_COMPLETE -> VALIDATED_DRAFT -> RELEASE_CANDIDATE`, each official CLI Stage report+Checkpoint from CURRENT authentic inputs, normal FF/non-force commits and readback. No shortcut `VALIDATED_DRAFT` on empty/recycled previous artifacts. Maintain State/provenance consistency.

Validate independent of worker self-confidence:
- Sentence/paragraph-level correctness and readability against original primary Evidence.
- 31 real must-cover requirements including matrices/formulae/tabular comparisons and source limitations.
- Citation-to-claim, source/subject/metric binding, publisher-vs-independent attribution and exact date/cutoff.
- TeX content is the actually reviewed rewritten text, not compressed derivative. Semantic review must mention spot-checked passage evidence and differences from r21.
- Build real PDF, independently compute bytes and SHA; render **every page at readable resolution** to inspect tables, math, Japanese glyphs, clipping, page hierarchy; don’t report a visual test solely from TeX/CI log.
- Correct old `370,741` narrative discrepancy; bind actual **new** PDF digest to Candidate/QA/TeX. Keep P7/Oct1 erratum and r20 hosted-timestamp erratum in reviewer packet.

## 4. Terminal / escalation

Normal successful terminal: **fresh `RELEASE_CANDIDATE / PUBLICATION_PREVIEW / HUMAN_GATE_REACHED` with fresh Candidate/PDF, Architecture APPROVED, recorded Human Preview r1 REQUEST_CHANGES in immutable review index, new Preview Gate PENDING/null, Draft/Validation PASSED based on newly authored bodies**, all 28/31/113, core-v2 exact tree/source frozen. Deliver `execution/SOL_W40_R22_PUBLICATION_PREVIEW_HANDOFF.md` and session log with remote SHA/tree, Gate revision result, 31-row content-coverage evidence, Japanese editorial QA, PDF URL, actual size/pages/hash, full visual proof and any limitations. Human Owner needs to review this new PDF; do **not** approve Preview, Freeze, Release or merge.

If a source/P7 immutable-approved Architecture conflict, unsuccessful regeneration because of Core's immutable file path ownership, or guard mismatch occurs, STOP. Give precise file/line, attempted lawful CLI and correct documented alternatives, not fake success. Never modify Core v2 to complete W40. Never open new branch. Other work not authorized.
