# Muse W40 r21 — owner-approved Architecture through fresh Human Publication Preview

Status: SOL_EXECUTION_AUTHORITY / OWNER_HUMAN_ARCHITECTURE_APPROVED / EXISTING_W40_ONLY / BOUNDED_AT_FRESH_PUBLICATION_PREVIEW
Date: 2026-10-11 JST
Repository: eariver/japanese-generative-ai-survey
Existing branch: weekly/2026-W40-v2-work
Exact starting HEAD AND TREE are supplied by the OUTER INVOCATION after this docs-only contract commit.
Reviewed main HEAD afdb3df3faa20af3bb5798be429bba8dbd2100b1 / tree fe3f07c653f255f67087b4b46d006f8943df7115.
Owner authorization: sources/2026-W40/execution/human-authorization/2026-10-11_owner-w40-r20-architecture-approved.md
Sol focused review PASS: sources/2026-W40/execution/reviews/sol-w40-r20-focused-architecture-review-pass-20261011.md
Core precedent for governance only: sources/2026-W39/execution/requests/sol-w39-architecture-r1-approved-through-publication-preview-20260928.md

## 0. Read-only preflight, no exceptions to guard

First verify exact remote W40 HEAD/tree against OUTER SHA/tree and remote main HEAD/tree against the values above. Existing branch only, clean tracked worktree at exact start. Stop with expected/actual and ZERO WRITES on mismatch. No new/fallback/repair/review branch, force/reset/rebase/squash/history rewrite.

Verify actual raw-byte SHA-256:
- pending pre-approval Production State 19bd1a9749108cf61ff29159dac216922b7316e5a91ee41c2f82f2f20e4bcb89
- r20 Architecture a9b5c1182671bb913fbf56972907e19731e5ba4a928deaca9903a0d3a1461a44
- Review Summary 32f39de0b7cb3e469acf74668c420c246fb67f273ecd0c37bda91557eaa98d30
- Review Attention 70ac43bdd0da014009f99abaf3aff00db8bdfbd9e44940ba087abf4cb5949319
- Selection b7d20be2fb273ba3c4a0ab66bb8818452591000805be90f9bcd75ce565bee225
- Matrix f07b1166eef02598a1d57ebd7d0068119678fcfc17f1d118ef2b582594a736f6
- Selection checkpoint 817075850a9390f735f9a9a4a35ebc9d391793b3ecd7907ba7d2308ebadfa678
- Architecture checkpoint 95b7755a663e1dcfe33f3983e166cd8e549430bfde1bbda343d6852057423a8c
- mandatory first-read current r20 erratum 564799edf0679c2fade1094139580e7c5d116a4abd3be2453de297f0ebcf3833

Verify State ARCHITECTURE_ESTABLISHED, next ARCHITECTURE_REVIEW, terminal HUMAN_GATE_REACHED, machine Selection and Architecture passed, Draft pending; BOTH Human gates pending/null, Exception inactive. No actual previous Human review record/index, no Architecture approval snapshot, no existing Draft/candidate authority. Confirm repo ancestry to reviewed canonical Muse r20 3711d777f8c447d25c6e0bfb3212450974afe8ab, all gate bytes identical at that commit and current. Check 35 Matrix, 28 SELECTED (20P/8S), 4 HOLD, 3 REJECT, 9 Packages and 113 literal Candidate-to-boundary relationships (105 package unique). Stop if any preflight fails.

## 1. Record official Owner Human Architecture Approval FIRST

Owner explicitly approved Architecture in ChatGPT after seeing 37 Discovery, 39 summed source references, 28 selected, 9 packages, technical depth and omissions. Original exact words and reviewed SHA/Tree are in owner authorization above. Source for actual Owner permission is the active conversation; durable repo memo is a faithful transcription, not a made-up Human decision.

Execute unchanged reviewed-main scripts/survey_human_gate_v2.py record-architecture-approval. Pin:
- reviewed_by: Human Owner
- gate ARCHITECTURE_REVIEW, decision APPROVED
- expected_revision=1 ONLY after confirming no review-index/history conflict
- reviewed-commit-sha=3711d777f8c447d25c6e0bfb3212450974afe8ab (exact canonical r20 user-reviewed files, still ancestor)
- reviewed-at: REAL current UTC ISO-8601 instant of formal recording, NOT an invented chat timestamp.
- review-reference: include repo path + actual SHA256 of this Owner authorization, Sol focused PASS note + SHA and mandatory r20 erratum + SHA.
- state: sources/2026-W40/production-state.json.

Inspect actual Core CLI syntax and validation; no hand-editing gates or production-state. Verify canonical gates/architecture-approval.json, gates/reviews/architecture-r1.json, gates/reviews/approvals/architecture-r1.json, gates/review-index.json (one real r1 APPROVED), architecture approval snapshot, exact Gate triple SHA, reviewed_repository_commit_sha, State approved with correct provenance and Publication Preview still pending. New next action should be stage:drafting-synthesis (confirm actual Core derivation).

Make a dedicated normal APPROVAL commit and non-force push; remote readback HEAD/Tree/provenance before starting Draft. If any official validator rejects decision, STOP and do not fabricate approval or begin drafting.

## 2. Approved scope, sources and depth contract

After approval, never semantically modify approved Discovery, Screening, Evidence, Views, Materiality, Completeness, Matrix/Selection, Architecture, its Review Summary/Attention or checkpoints. No Core/schema/config/workflow/main/Issue #562 or other edition changes. Frozen 28 IDs with 20 PRIMARY, 8 SUPPORTING distributed P1 3P; P2 2P; P3 3P; P4 2P+1S; P5 3P+2S; P6a 2P; P6b 2P+1S; P7 3P+2S; P8 0P+2S. P6a/P6b share WEEKLY:training-eval-infra official role. All 113 literal boundary relationships and 105 unique package strings remain enforceable. HOLD Pixel Canary, TBC/AWS, AstaBrief, AutoSynthData and REJECT x-ledger, DGX Spark standalone, LIFT cannot become reader chapters, annexes or companion PDF. Two in-window AstaBrief/AutoSynthData material omissions explicitly acknowledged; Core #562 separate.

Draft naturally technical, fluent Japanese with sufficient depth (NO arbitrary page cap). For each primary candidate: what changed, implementation/how, why significant, published metrics with correct denominators/units/conditions, relevant baseline, licensing/timing/availability, provenance, limitations, editorial implications. Supporting candidates smaller as approved. Keep publisher figures clearly attributed; VERIFIED is claim/source confirmed, not independently benchmark reproduced. Cite each external technical assertion to accepted Evidence/legitimately checked first-party r15/r16 technical prep. Never invent source facts, URLs or run results; do not pass off noncanonical prep as automatically approved fact outside its verified scope. No excessive kanji translation, literal machine translation, decorative buzzword fillers or internal pipeline IDs/status/jargon in reader-facing text.

Mandatory technical crosschecks:
P1 frontier per-vendor pricing/model availability with Gemini OUTPUT 1M boundary, vendor-run benchmarks only.
P2 Holo4 27B/35B-A3B license split; ELYZA 33B/MoE, SHAs and Japanese benchmark denominators; no replay claimed.
P3 Ollama INTERFACE distinct from Clef WEIGHTS/API and Strands DECIDER pointer-head; source-scoped Jev and latency claims.
P4 computer use changelog != reliability proof; dots availability bounds; bundle merely supporting.
P5 five independent protection/evaluation/guidance/auth domains; ProvenanceGuard v2 only; spec != security assurance.
P6a ContextLM Eq.1–Eq.6 explained meaningfully, Eq.5 EXACT objective VERIFIED in r16 (frozen model weights; skill-document optimization with training/development/held-out), Eq.6 RL parameter-training separate; Eq.3 FLOPs not wall-time; SCR/BCP distinct baselines; Olmo-core 3 DDP/expert routing/MXFP8 measured 4xB300 21% and 103->95GiB, 47B vs 1.2T vs 2.38T not conflated, negative tests and unretrieved report disclosed.
P6b AgentPerf all 14 configs speculative, bandwidth roofline comparison NOT speculative-off control, local-single-user != production-concurrent; OpenTTS TTFA 50 English prompts batch1 first3 warmups excluded median default H200, published Sep30 versus eval-script first confirmed Oct7; RL Environment Hub framework version != taskset revision pin.
P7 FLUX 3 editing/pricing/promo window; VSS reference/demo scope; ASR adaptation language/task constraints; Relay tracing vs correctness; Ross unmeasured embedded supporting.
P8 AMD/World Labs DEFINITIVE AGREEMENT not completed acquisition, AI Search service billing terms not model benchmarks.

MANDATORY first-read r20 erratum corrects inherited false TIME_UNRESOLVED for AstaBrief/AutoSynthData hosted article clocks. DO NOT repeat stale Review Summary sentence in published body. Article clocks do not prove standalone weight/code/dataset release.

## 3. Stage path and publication quality

Use unchanged Core proper CLI/handlers and official checkpoint path:
ARCHITECTURE_ESTABLISHED (Human approved) -> DRAFT_COMPLETE via stage:drafting-synthesis;
DRAFT_COMPLETE -> VALIDATED_DRAFT via stage:reader-publication-validation;
VALIDATED_DRAFT -> RELEASE_CANDIDATE via stage:publication-candidate.

Before TeX, personally inspect all nine package drafts/reader authority for substantive Japanese prose, explicit source-claim mapping, formula/table needs, complete must-cover/boundaries, proper Primary-vs-Supporting depth, no empty placeholders, overly terse text or unsupported numbers. JSON schema PASS is necessary NOT sufficient; check real prose. If thin, expand within approved authority, revalidate; if substantive upstream contradiction appears stop for Sol rather than altering approved authority. Use r15 P6a/P6b deep drafts + r16 verified Eq5 note as source-bounded inputs, NEVER import the outdated r15 Eq5 UNVERIFIED statement.

Create durable reader-manuscript/reader-facing source in the normal official Core route, render TeX and actual PDF (do not synthesize fake artifacts). Run original schema, Core/reader-surface, source/citation/subject-entity binding, semantic, visual QA, quality bundle and production stage checks. Inspect EVERY PDF page for Japanese glyphs, math, tables overflow/clipping, bibliography and link placements, page count relative to technical material, title/index consistency. No hard page count or blind reliance on a PDF_PREFLIGHT PASS. Fix edition-local Draft/TeX issues lawfully and rerun QA until defensible. Commit sequential stage evidence with real checkpoint and direct FF/non-force pushes; verify remote after each major stage, never modify old accepted authority, manual State/checkpoint spoof, false validated review or rewrite history. Record actual CLI diagnostics and separate historical legacy validate-state exit1 from governing agent-first validator PASS (not automatically Core #562).

## 4. Stop at new Human Publication Preview

Target: canonical RELEASE_CANDIDATE / next PUBLICATION_PREVIEW / terminal HUMAN_GATE_REACHED, Architecture Human gate approved with formal review-index r1 and exact provenance, Publication Preview Human gate pending/null, draft and validation checkpoints passed, current Candidate bound to actual publication PDF and required reader manuscript, TeX, quality bundle, semantic and visual reviews. No preview decision, no Freeze, Release or main merge, no PR.

Provide a real GitHub blob AND raw view URL for surveys/2026-W40/main.pdf (verify path from publication profile; do not invent), real PDF SHA256/page count, plus candidate/quality/manuscript exact SHAs, per-package article coverage/depth and all 28/113 invariants. Deliver edition-local execution/SOL_W40_R21_PUBLICATION_PREVIEW_HANDOFF.md and execution/sessions/muse-w40-r21-20261011.md (actual date if different) with start/gate-approval-stage/final SHA/Tree and evidence, plus details of self-contained content review and visual QA. If blocked at an intermediate lawful stage, STOP with exact blocker and current remote head/tree; do not fake final preview.

Terminal success FRESH_HUMAN_PUBLICATION_PREVIEW_PENDING / W40_R21_READY_FOR_SOL_AND_OWNER_PDF_REVIEW. Otherwise SOL_REVIEW_REQUIRED_WITH_EXACT_BLOCKER.
