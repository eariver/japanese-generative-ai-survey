# Muse W40 r15 — Lossless Architecture Boundary staging + P6a/P6b source-grounded repair

Status: `SOL_EXECUTION_REQUEST / EDITION_LOCAL_ONLY / BOUNDED_AT_R15_SOL_REVIEW`  
Date: 2026-10-10 JST  
Repository: `eariver/japanese-generative-ai-survey`  
Existing branch ONLY: `weekly/2026-W40-v2-work`  
Reviewed main: `afdb3df3faa20af3bb5798be429bba8dbd2100b1`  
Exact Starting HEAD/Tree: receive from outer Sol handoff **after** this instruction commit.  
Governing editorial disposition: `sources/2026-W40/execution/reviews/sol-w40-r14-independent-audit-disposition-20261010.md`.  
Independent read-only r14 audit: `REVISION_REQUIRED`, F01–F08.  
Shared-Core separate debt only: GitHub Issue #562 / CV2-DM-022.

## 0. Mandatory start guard, exclusions and exit point

BEFORE any repository writes verify read-only:
1. remote existing W40 HEAD == outer exact Starting SHA AND commit tree == outer expected Starting Tree;
2. remote main HEAD == `afdb3df3faa20af3bb5798be429bba8dbd2100b1`;
3. production-state lifecycle `EVIDENCE_REVIEWED`, next `stage:selection`, Selection/Architecture checkpoints pending, both Human Gates pending with provenance null, exception gate inactive;
4. the existing accepted Discovery 37 / Screening 37 / Evidence Cards 35 / Views 35 / Materiality 37 + Completeness, accepted SHA/checkpoints/reader-authority unchanged;
5. r13 Selection SHA `dc0247781b0401e62eb8b17980050769b743f2aa313ffda3f5b5704235db0cb1` and r10 Matrix SHA `f07b1166eef02598a1d57ebd7d0068119678fcfc17f1d118ef2b582594a736f6` match actual bytes.

If ANY mismatch: ZERO WRITES, report expected vs actual and stop. No new branch or fallback, no reset/rebase/force/rewrite. Normal commits and non-force push to same existing branch only. No `scripts/`, `schemas/`, `config/`, `.github/`, shared Core docs, `main`, other Editions, already accepted upstream, `production-state.json`, checkpoint, Issue or Gate mutation. No human approval/Release decisions. Do not edit r14 prior-audit artifacts in place: r15 edition-local successors/addenda only.

r15 **MUST stop** at `SOL_W40_R15_BOUNDARY_AND_TECHNICAL_REVIEW_REQUIRED`. NO formal Selection Acceptance, Stage transition, canonical `architecture-v2.json`, canonical Architecture checkpoint, Human Gate, Freeze, public release or ad hoc supplement. NO Core fix from this edition.

## 1. Highest priority F01 — 28 selected / 113 remaining_boundaries exact preservation

Sources of truth:
- `sources/2026-W40/execution/selection/selection-preview-r13.json` (28 selected, 20 PRIMARY, 8 SUPPORTING; 4 HOLD, 3 REJECT);
- `sources/2026-W40/execution/selection/candidate-matrix-r10-staging.json` (`rows[].remaining_boundaries`);
- `sources/2026-W40/execution/architecture-coverage-r14.json` (accepted 28-ID/Role/destination mapping);
- reviewed-main `scripts/survey_architecture_v2_base.py::validate_architecture` (each placed candidate's `remaining_boundaries` must all appear as **literal elements** of containing Package's `boundaries` array; placement and role checks independently apply).

Read actual data. Recompute 113 total raw candidate-to-boundary relationships, **not** from hand-edited counts. Confirm 28 selected IDs and unchanged 20P/8S roles against Selection + Matrix + r14 mapping.

Create:
A. `execution/architecture-boundaries-r15.json`: SHA-bound noncanonical preparation structure with:
  - exact Selection/Matrix/Coverage source paths, raw SHA-256s, issue identity, status `STAGED_ONLY`;
  - 28 entries `{candidate_id, architecture_usage, package_ids, remaining_boundaries:[original exact strings]}`, including each candidate's list (do not normalize case/punctuation/encoding or paraphrase);
  - package aggregates (P1, P2, P3, P4, P5, P6a, P6b, P7, P8), each with `primary_candidate_ids`, `supporting_candidate_ids`, and **`boundaries` exact-string array** (unique within package; allow shared string to appear once if identical);
  - package mapping derived from accepted r14 Coverage, not manual inference;
  - explicit count distinction: 113 raw relationships vs potentially fewer de-duplicated package strings;
  - unresolved provenance flags for any source text not understood; keep originals intact.
B. `execution/architecture-boundaries-validation-r15.json`: independent second-pass reconciliation computed from source bytes, not trusting the just-generated arrays:
  - 28/28 IDs, 20P/8S, assignment/Matrix/coverage equality, 0 HOLD/REJECT placed, Primary exactly one destination, Supporting >=1;
  - literal membership check for ALL 113 raw candidate-boundary relationships in EVERY destination package; missing count must be 0, unexpected unsupported strings count separately (explain accepted de-dup);
  - package primary/supporting membership equality to selected exact usages;
  - duplicate-safe aggregation, idempotent roundtrip, stable sorted identity and SHA-256 of actual source and output files;
  - report per-package raw relationship count and unique `boundaries` count; report exact mismatch path/string on FAIL;
  - validate against the **actual unmodified reviewed-main Core rule** (static equivalent check); if dynamically running `validate_architecture` on an ephemeral fully formed in-memory `PROPOSED` object is feasible WITHOUT writing canonical artifacts or invoking Gate actions, perform and disclose any broader-contract limitations. Do NOT fabricate an Architecture PASS if only the membership subcheck was tested.

C. `execution/architecture-staged-outline-r15.md`: use the corrected 28 mapping and attach exact package boundary arrays or exact references to the SHA-bound JSON. Include explicit package roles and content requirements. Ensure no fictional separate `WEEKLY:training-eval-infra` role for P6a/P6b; P6a/P6b remain editorial split within existing role. Preserve noncanonical COND-A/B notes without placing the two HOLD candidates.

Failure of the literal check is a STOP-at-Sol condition, not a reason to alter upstream authority or edit Shared Core.

## 2. F02/F03 — ContextLM: correct Eq.6 and actually explain the mechanism

Make substantial `execution/technical-prep-r15/p6a-deep-draft.md` as r14 successor (preserve r14 record):
- Re-read primary **arXiv:2609.37725 v1** / first-party technical source at adequate depth (equations/tables/figures where accessible). Pin exact version and direct link. Do not rely solely on the independent auditor's prose.
- Correct Eq.6: efficiency advantage `A_i^{eff}` may be zero for fewer than 2 successes; total `A_i = A_i^{out} + w_eff A_i^{eff}` can retain `A_i^{out}`. Explain effects on RL learning signal; quote exact symbols after source verification; label unresolved maths `UNVERIFIED` rather than introducing a confident erroneous equation.
- Explain actual path-based editable context operations, model-controlled file changes, sync back to next turn, how this contrasts with append-only/summary, and operational guardrails.
- Eq.1–5 roles, prefix reuse FLOPs accounting, Suffix Cache Reuse mechanism and limits, not confused with wall time or full-cache hit-rate.
- Distinguish paper-defined relative accuracy improvement (+11.4% vs Codex-style summarization), -21.5% FLOPs vs Codex and -28.9% vs MEM1; paper-defined 35.9 points ContextBench, not percentage with unknown units. Cite named table/section and baseline; do not silently merge comparisons.
- Differentiate paper CC BY 4.0 from *specific checked revision* of repository license CC BY-NC 4.0. Use first-party repo LICENSE/README content if available, else be explicit about scope and uncertainty.
- Preserve other reported benchmark conditions/denominators and source attribution; do not turn calculations without source into independently reproduced findings.

## 3. F04 — Olmo-core 3: extend primary-sourced systems detail

In same P6a deep draft, repair:
- MXFP8 BF16 comparison: check B300 **4 GPUs**, equal expert load, measured throughput +21%, peak-memory 103→95 GiB, and exact configuration; report provenance and whether test is controlled or observed anecdote.
- Describe why FSDP→DDP with experts resident alters dispatch and communication; grouped GEMM, rowwise expert parallelism, distributed optimizer, pipeline overlap; system mechanisms without inventing code internals.
- Negative results: token gerrymandering, expert learning-rate reduction, pipeline/stage overlap slowdown — mechanism, attempted optimization, observed failure, what evidence does/doesn't show. Avoid a list of labels.
- Clearly separate 47B measured configuration, 1.2T total/58.36B active/512 GPUs with random routing/858 TFLOP/s/GPU, and 2.38T **short-capacity test** vs completed large-model training. Do not infer end-to-end model quality.
- Read official Ai2 blog and technical report/code where available; if a large report cannot be retrieved, state exact access failure and do not manufacture internals or blanket-pass completeness.

## 4. F05 — AgentPerf baseline and P6b full technical repair

Make `execution/technical-prep-r15/p6b-deep-draft.md` as substantive r14 successor. Use the W40-period Artificial Analysis AA-AgentPerf-Local article and a pinned implementation snapshot; distinguish later code from Sep29 announcement:
- Correct reported speculative +30–120% **above bandwidth-constrained decode roofline**, NOT delta from a speculative-off control group.
- Verify 14 measured configuration mix, their use of MTP/DFlash/DSpark and what the paper actually says about all/strongest initial configs. Do not overgeneralize claim beyond first-party source.
- Supply source-specific metrics definitions and hardware/model/quantization, replay tasks/turns/context, prefill/tool-skip, baseline and coverage limits.
- Distinguish this *local* single-agent serving workload from production AA-AgentPerf concurrent capacity benchmarking (different methods); no conflated metrics.

## 5. F06 — OpenTTS evaluation details and clocks

In P6b successor:
- Define WER vs CER aggregation (English Seed-TTS-Eval + CV3-Eval, multilingual per-language macro, Japanese/Chinese/Korean CER), RTFx/TTFA/SIM metrics as the announcement defines them.
- H200/GPU throughput configuration, TTFA batch size 1, 50 English prompts, three discarded warmup iterations, median; verify original source for each clause.
- Model/ASR/embedding dependencies (Qwen3-ASR-1.7B, WavLM), quality proxy caveats, human MOS/preference non-equivalence and snapshot comparison boundaries.
- Maintain **temporal split**: Sep30 W40 announcement phrased scripts as future publication, while a GitHub repo is discoverable today. Confirm repo creation/commit SHA/license/contents where possible; do not retroactively assert script availability at W40 cutoff.

## 6. F07 — RL Environments Hub reproducibility

In P6b successor:
- Retain the correct SUPPORTING role and the four framework filter/tags, dataset/runtime separation and current-vs-future boundary.
- For `harbor==0.21.0`, `openenv[harbor]==0.7.0`, or any reproduction sample, specify referenced taskset repository + immutable revision/commit (where available), sample selection, config and execution substrate.
- If the exact revision was not published/retrieved, explicitly `NOT_REPRODUCIBLY_PINNED`; keep API/framework pins but do not mislabel total reproducibility.

## 7. F08 — provenance correction to an audit-accurate evidentiary claim

Create `execution/editorial-supplement/r15/evidence-source-provenance-correction.md` and accompanying provenance/manifest addendum:
- Retain factual UTC arithmetic: `19:57 +0900` = `10:57Z`, before independently read Git commit `2026-10-10T11:02:43Z`.
- r14 asserts locally surviving HTML file mtimes `2026-10-10 19:57:25.601917670 +0900` and `19:57:45.561988218 +0900`. Independent reviewer could **NOT** remeasure them from uploaded/committed files; explicitly label `MUSE_LOCAL_MTIME_REPORTED / NOT_INDEPENDENTLY_REPRODUCED`. If the original files can be lawful to archive as **edition-local research evidence** without violating source retention/licensing/personal-data policy, save a minimal reproducible manifest/log or cryptographically bounded artifact using content allowlist (not the entire dynamic webpage by default); otherwise mark `EXACT_RETRIEVAL_CLOCK_NOT_INDEPENDENTLY_VERIFIED` and explain why.
- mtime is file write timestamp, not authoritative HTTP response time; do not imply millisecond GET precision.
- r11 vs r13 same byte count/different hash proves BYTE_DIFFERENCE only; 'dynamic framing proven' stays withdrawn (possible untested explanation).
- Muse JSON-LD re-parse and independent auditor millisecond re-extraction remain DISTINCT. Preserve article publish, retrieval and Git commit clocks as three separate facts.

## 8. Source fidelity & reviewable closeout

For P6a/P6b r15:
- Meaningfully expand explanatory Japanese paragraphs (why/how/measured/limitations), not merely more bullet points and a large table.
- Cite a primary source URL + pinned revision/section/table for every substantive quantitative claim. For uncertain named models/benchmarks or source-specific explanations do not use model recollection as authority.
- Supply exact Source→Claim table; list new source retrievals and what was NOT retrievable.
- Distinguish source author/vendor/evaluator claims from independent replication; do not mark `VERIFIED` where it only means article text confirmed.
- Prepare a source-to-Finding matrix: F01–F08 `CORRECTED / PARTIAL / STILL_OPEN`, with exact file and evidence anchors. No blanket 'all closed' claims while missing primary equations, table cells or pinning. Preserve PASS areas r14 as-is: 28-ID Role map, AutoSynthData verifier logic and supplement contract analysis. New Issue/Shared Core fixes are **not** authorized.

Deliver:
- `execution/SOL_W40_R15_BOUNDARY_AND_TECHNICAL_REVIEW_HANDOFF.md`
- `execution/sessions/muse-w40-r15-20261010.md` (use actual execution date if not Oct 10)
- append `execution/index.md` navigation without deleting history
- the new exact-boundary JSON and validation, r15 outline, r15 P6a/P6b prose, provenance addendum and source ledger.

Final read-only verification after normal non-force push: actual remote HEAD/Tree, changed files W40-local only, branch ancestry, review main, Production State/accepted SHAs and both Human Gates unchanged. Direct untouched Core `validate_selection` execution may be performed read-only against r13 preview, but do not call a static simulated Architecture boundary check 'formal Architecture PASS'. Terminal `SOL_W40_R15_BOUNDARY_AND_TECHNICAL_REVIEW_REQUIRED`.

**STOP, NO formal State transition or publication action.**
