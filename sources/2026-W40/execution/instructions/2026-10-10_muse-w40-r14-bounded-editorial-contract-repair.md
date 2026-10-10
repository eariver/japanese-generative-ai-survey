# Muse W40 r14 — Bounded editorial/contract repair after independent r13 audit

Status: `SOL_EXECUTION_INSTRUCTION / EDITION_LOCAL_ONLY / STOP_AT_R14_SOL_REVIEW`
Date: 2026-10-10 JST
Repository: `eariver/japanese-generative-ai-survey`
Work on existing branch ONLY: `weekly/2026-W40-v2-work`
Expected reviewed main: `afdb3df3faa20af3bb5798be429bba8dbd2100b1`
Exact Starting SHA / Tree: supplied by Sol in **outer prompt** after this instruction commit.
Governing editorial authority: `sources/2026-W40/execution/reviews/sol-w40-r13-independent-audit-disposition-20261010.md`
Independent result: `REVISION_REQUIRED`, findings `W40-R13-F01`–`F08`.
Core debt: Issue #562 / CV2-DM-022 (separate Core maintenance task only).

## 0. Strict preflight, scope and prohibition

Before **any repository writes** independently verify remote W40 HEAD and tree match outer Exact Starting SHA/Tree; remote main HEAD == expected reviewed main; Production State `EVIDENCE_REVIEWED` / next `stage:selection`; upstream accepted 37 Discovery / 37 Screening / 35 Evidence Cards / 35 Views / 37 Materiality rows and exact SHA-bound prior checkpoints unchanged; Selection/Architecture pending; both Human Gates pending/provenance null; exception gate inactive.

If any identity/authority guard fails: ZERO WRITES and report expected/actual. Only normal commits and non-force push on the **already-existing W40 branch**. Never create branches or rewrite/reset/rebase history. Do not touch `.github/`, `config/`, `schemas/`, `scripts/`, Core implementation, `main`, other editions, shared Core docs, accepted upstream files, production-state or gates. Do not update Issues. Do not impersonate a Human reviewer or fabricate Core validation/provenance. r13 products stay immutable historical review evidence; create r14 successors/corrections.

This unit has NO formal Selection Acceptance, Stage transition, canonical Architecture build, Gate, Freeze, Release, or public supplement authorization.

## 1. Exact 28-candidate Role/placement repair (independent r13 F02/F03/F07)

Read `execution/selection/selection-preview-r13.json` and its exact r10 Matrix/crosswalk on reviewed-main Core. It is **28 SELECTED = 20 PRIMARY + 8 SUPPORTING**, plus 4 HOLD and 3 REJECT. Do NOT alter that Selection preview or canonical source-of-truth.

Create both:
- `execution/architecture-coverage-r14.json`: machine-generated 28-entry mapping from actual Selection bytes with fields candidate_id, publication_role, architecture_role, architecture_usage, selected disposition, one primary P1–P8 destination OR one-or-more supporting destinations; populate justified content anchor/claim/boundary pointers; calculate hashes.
- `execution/architecture-coverage-validation-r14.json`: independently calculated reconciliation against exact Selection JSON and candidate Matrix; ID uniqueness; 28/28 coverage; 20 PRIMARY and 8 SUPPORTING preserved; zero usage/Role mismatches; each PRIMARY exactly one assigned package, each SUPPORTING >=1; no HOLD/REJECT inserted; no invented candidate IDs; hashes verified; status FAIL (and stop at Sol) if any rule fails.

Derive corrected `execution/architecture-staged-outline-r14.md` from this **single authoritative map**, including precise visible candidate IDs and row-by-row Role evidence, then substantive package structure, source and must-cover relationships. Correct at minimum:
- P5: ProvenanceGuard, Open Agent Safety Platform, **SynthID Bio** = 3 PRIMARY; training safety cases and MCP OAuth v1 = 2 SUPPORTING.
- P7: FLUX 3 Image, **NVIDIA VSS Blueprint 3.3**, **Nemotron Saudi Arabic ASR adaptation** = 3 PRIMARY; NVIDIA NeMo Relay and **AMD Ross** = 2 SUPPORTING. Ross must have explicit supporting destination even if reader prose is a small embedded note.
- P1, P2, P3, P4, P6a, P6b, P8 — complete exact counts, roles, candidate IDs.
- P6a and P6b share `WEEKLY:training-eval-infra` role namespace but remain two justified editorial destination packages; no fictitious Core 'split' role.
- Maintain **two** extra conditional future P6a research topics (AstaBrief, AutoSynthData) as NON_CANONICAL HOLD — NOT in the 28 mapping or any formal package placement.
- Avoid falsely calling this staged outline a Core accepted Architecture or claiming Reader Manifest `architecture_coverage` already exists.

Produce truthful package totals and one-to-one ID audit. If a prior r13 candidate cannot be placed lawfully, state exact evidence discrepancy and STOP; do not quietly drop it.

## 2. AutoSynthData verifier semantic repair (F06)

Create `execution/editorial-supplement/r14/autosynthdata-note-r14.md` correcting r13 §3 and examples **without editing r13 historical note**:
- `consistency`: verifier must agree with prompt, system spec and initial/environment task state.
- `soundness`: invalid, unsuccessful or policy-violating outcomes MUST NOT be accepted (false-positive prevention).
- `completeness`: VALID alternative solutions MUST be accepted (false-negative prevention), independent of exact reference trajectory.
- **positive gate** exercises a valid reference/witness execution, checks consistency/feasibility/alignment for that witness; cannot by itself prove universal completeness.
- **negative gate** must reject deliberately mutated/invalid outcomes, thus chiefly exercises soundness, **NOT** completeness.
- Give distinct concrete test examples for positive, negative, and alternate-valid solution cases. A passing finite test suite does not mathematically prove universal soundness/completeness.
- Keep TARGET/MULTIPLY, difficulty bands, bounded retries, experiments (Hybrid 2,000/~18h/epoch5; ITSM 1,994/66h), license/release limits and source attribution byte-identical or semantically unchanged except where necessary.
- Preserve r13 sourced primary URL and noncanonical status; update r14 manifest pointers and claim/limit audit.

Other r13 AstaBrief technical material was found substantially accurate by the independent auditor. Preserve it; do not manufacture a new 'repair' if no cited issue remains.

## 3. Provenance correction (F04/F08)

Create `execution/editorial-supplement/r14/evidence-source-provenance-correction.md` and `execution/editorial-supplement/r14/manifest-r14.md` that explicitly supersede the **interpretations** in r13's working ledger without replacing its immutable reviewed bytes.

- Original claim `2026-10-10 ~19:57Z` conflicts with r13 commit timestamp `2026-10-10T11:02:43Z` (20:02:43 JST). Prefer inspect actual preserved local system logs containing UTC-offset timestamps/command output; if absent, `EXACT_RETRIEVAL_CLOCK_NOT_VERIFIED` instead of guessing `19:57 JST`. Separate assertion-level article publish clock (`datePublished`), retrieval time and commit time.
- Both r11/r13 captures have matching body byte counts (169199 / 210484) but different SHA-256; this demonstrates **bytes differed**. 'Dynamic framing PROVEN' must be downgraded to possible explanatory hypothesis unless exact byte diffs and attributable causes are preserved. Raw historical captures not archived; never claim a differential forensic reconstruction was performed.
- Distinguish Muse r13 assertion of re-parsing published HF JSON-LD from **independent auditor r13**, which confirmed publisher/date but could not itself directly re-extract millisecond JSON-LD. Do not claim independent exact-second confirmation.
- All claims tied to original first-party article/host/meta, no invented release clock, publication freshness or retrieved source SHA.

## 4. Correct supplement publication feasibility, with static rule evidence (F01/F05)

Create `execution/supplement-publication-feasibility-r14.md` as **corrected and evidence-bound** legal/technical topology analysis. Keep r13 study as prior historical finding, without invisible replacement.

Read actual reviewed-main files `.github/workflows/survey-production-v2-release.yml`, `scripts/survey_reader_publication_v2.py`, `schemas/reader-manuscript-v2.schema.json`, `scripts/survey_architecture_v2_base.py`, `scripts/survey_publication_v2.py`, Publication and Profile schemas + release identity.

Mandatory distinctions:
1. Release workflow inspects **count of assets whose name equals expected `ASSET_NAME`**, not the total number of Release assets. Multiple differently named assets can technically coexist; **no positive Core approval semantics for extra supplement assets** arises from this absence of a total-count guard.
2. Reader `supporting_files` are SHA-bound roles limited to `BIBLIOGRAPHY/STYLE/SUPPORTING_SOURCE`; no sanctioned Reader `SUPPLEMENT` role. Provenance of supporting TeX does NOT authorize independently published unselected subject.
3. `architecture_coverage` exact-set validation rejects missing/extra asserted coverage keys, while *unlabeled free-form prose* may not be mechanically caught; this is a semantic editorial/Human Gate integrity requirement, not always a Core syntax error.
4. `validate_architecture` places only formally SELECTED candidates; HOLDs cannot receive official roles, must-cover or normal W40 Primary subsections.
5. Publication Candidate has one authoritative source/PDF; a separate non-Core PDF may be technically hosted but lacks the existing Core release manifest/review/identity guarantees. TS-003 was an explicit one-time Human exception for already approved corrected bytes, not standing authority for W40 content expansion.

Table for Path A: independently authorized non-Core companion; Path B: ordinary W40 published supplement; Path C: no normal reader-complete option. Explicitly mark three columns: `TECHNICALLY_POSSIBLE`, `NORMAL_CORE_AUTHORIZED`, `EXPLICIT_HUMAN_OWNER_AUTHORITY_REQUIRED`. Cite exact source code line ranges and the relevant negative evidence. Avoid categorical statement 'cannot physically upload' where only normal publication permission is absent.

**Outcome may remain** `NO NORMAL SUPPLEMENT_PATH_ESTABLISHED`. Do not 'fix' the conclusion by making an unauthorized public release or exception request.

## 5. Technical depth that survives eventual Architecture (F07)

Prepare `execution/technical-prep-r14/p6a-deep-draft.md` and `execution/technical-prep-r14/p6b-deep-draft.md` as substantial, noncanonical **reader-oriented technical drafts** (not mere outlines), with:
- P6a ContextLM (file-as-context, equations 1–6, metric definitions, RL/BCP/EdgeBench and ablations); Olmo-core 3 (DDP/expert/data/tensor pipeline, grouped GEMM, MXFP8 assumptions, per-GPU result and ablation conditions); candidate IDs, primary paper/repo provenance and license conditions. Conditional AstaBrief/AutoSynthData should remain **separately labeled and excluded from official 28 selection**.
- P6b AgentPerf (serving-only benchmark, workload replay/14 configs and hardware/version limitations), OpenTTS (WER/CER vs RTFx/TTFA/SIM and preference eval limits), RL environments (actual framework tags/tasks; supporting role); reproducibility vs publisher-only metrics.
- Named parameter/benchmark numerator, denominator, hardware, baselines, versions, causal boundaries and source class per claim. Where evidence is missing, `UNVERIFIED`, not fabricated specificity.
- A matched Source→Claim table and a paragraph-level Japanese quality/self-review (no unnatural over-Kanji translations). Preserve technical depth over low page count.
- Never write official Core `architecture-v2.json`, `surveys/.../main.tex`, or artifacts claiming HUMAN APPROVED.

## 6. Correct handoff / stop

Produce `execution/SOL_W40_R14_BOUNDED_REPAIR_HANDOFF.md`, updated edition-local `execution/index.md` navigation, session log and exact change list. For each F01–F08: describe `CORRECTED / VERIFIED / PARTIAL / STILL_OPEN` with objective evidence; do not call technical depth/completeness closed merely because a plan exists.

Re-run untouched `validate_selection` on r13 preview and report exactly whether it was directly executed. For the new 28-ID coverage map, independently verify every mapping as declared in §1. Check upstream State/Gates and protected Core unchanged and remote readback after non-force push.

Final status: `SOL_W40_R14_BOUNDED_REPAIR_REVIEW_REQUIRED`.
Stop. **NO Selection Acceptance, NO Stage transition, NO Core patch, NO Human Gate, NO publication release**. Keep #562/CV2-DM-022 in the separate Core task.
