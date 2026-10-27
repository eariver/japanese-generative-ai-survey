# J-GAS W43 — Owner-authorized bounded runtime-only Draft basis compatibility, fast recovery

Status: EXECUTION_AUTHORITY / HUMAN_OWNER_AUTHORIZED_W43_ONLY_RUNTIME_COMPAT / WRITE_ENABLED_DELIVERABLES / NO_CORE_SOURCE_MUTATION / NO_EXTRA_COMPREHENSIVE_TEST_CAMPAIGN
Date: 2026-10-28 JST
Operator: Muse/OpenCode. Supervisor: editorial Sol.
Use existing branch only: weekly/2026-W43-v2-work.
No ChatGPT Work dependency.

## 0. Owner's new authorization and its limit

Following the earlier feasibility investigation, the Human Owner explicitly stated: 「仕様修正ではなく迂回で構いません。そのための慎重なテストも不要です。」

Interpretation:
- The Owner authorizes a **W43-only temporary runtime compatibility** to work around the already diagnosed immutable-history \`state_sha256\` basis mismatch and bridge-originated State validator convention mismatch. Do NOT initiate a cross-edition shared-Core design/repair project.
- The Owner waives **new comprehensive regression suites, multi-round negative testing and another independent full PDF audit** solely for the compat. Keep only minimal factual admission/hash identity checks, actual tool exit status, output manifest and a few existing native validations; none are an independent audit.
- Do NOT interpret this as permission to forge canonical checkpoint results, change State history, replace a Human approval, silently publish the proof, edit Frozen Core v2, weaken unrelated scientific/semantic checks, or automatically Freeze/Release. If an essential integrity invariant fails, stop and describe it, not a fabricated PASS.
- Human's prior r8 content/layout approval remains pinned to r8 PDF SHA256 \`abd5b99bd051703dbdc9420c19965ed039585c0436090ae219be665c6d17dc72\`, a NONCANONICAL proof. This waiver is not exact-byte canonical Publication Preview gate approval.
- The completion objective is **native P1–P8 Draft/Synthesis actual artifact generation** using the accepted W43 source chain with the W43-only compatibility, then Sol evaluation/next stage. Avoid a fresh r9/PDF rebuild for the compatibility unit.

## 1. Exact remote guard and local sync

Expected pre-contract W43 HEAD: \`b8631f5d25fd67c6d996bb17f8e2d9a649ffb9bc\`
Expected pre-contract Root Tree: \`3e9b0d7c7f3a1800b86a1d4e4d5d1d61c5d08a13\`
The final contract-only commit HEAD/Tree are supplied by editorial Sol at dispatch; current remote work HEAD and Root Tree must equal that exact final contract SHA/Tree, with single parent exactly pre-contract SHA. Mismatch: do not write; report expected vs actual.

Protected main HEAD/Tree:
\`041a08dfef3112643cbf85b4a86a7b6f9128aed6\` /
\`a134dc36a407d08ab1de416324229b3955e0325a\`.
Protected production/survey-core-v2 HEAD/Tree:
\`774dd39a951c9ac3818e83dfffd4c7666efb0a20\` /
\`cd46a6f7a6dcc4031e76220cea4c52c7dd1fc481\`.
The approved W43 Architecture and Human architecture review receipt must still bind current trusted bytes. The W43 Production State remains ARCHITECTURE_ESTABLISHED with architecture_review=approved and publication_preview=pending.

**Writable deliverables, not a read-only task.** \`git fetch origin\` is authorized; from clean local existing W43 checkout, \`git merge --ff-only origin/weekly/2026-W43-v2-work\` is authorized to synchronize when behind (or \`git pull --ff-only\`). Do not use ordinary uncontrolled pull, force push, branch creation, reset or rebase. After producing outputs, normal \`git add\`, commit, **non-force push to existing W43 branch**, then remote read-back of final SHA/Tree are REQUIRED. No "IN CHAT ONLY" output substitution.

## 2. Recover Draft through edition-local transient admission, not a persistent Core change

Confirmed failure:
- \`scripts/run_drafting_synthesis_v2_interactive.py\` → \`survey_drafting_v2_base._resolve_effective_screening_discovery\` → \`survey_screening_v2.validate_package_basis\` at approximately lines 629–650 → \`Screening package basis drift: state_sha256\`.
- Historical accepted screening r1/r2 \`basis.state_sha256 = 885927bd98e1ade491bc88e666aa0f39233ba7f0fb93f8ed87c9d2760ac22596\`, compared with current trusted W43 State SHA \`b0450d25b9dd4db8424d1c92d713d28c1b268b4e6a3b960a053f9684bb3eebb6\`. Verify actual bytes; these are expected historical pins.
- \`profile_sha256\` and \`discovery_sha256\` must still MATCH original accepted package; package itself must match the accepted Screening acceptance \`package_sha256\`.
- \`verify_state_basis\` also demands a single \`implementation.repository_commit_sha\` for all history and old checkpoint attestation path convention, while agent-first bridge records distinct executing SHAs and FROM-state checkpoint paths. The same State must still PASS **agent-first** \`survey_agent_control_v2.validate_agent_state\` before compatibility.

Implementation:
1. Put a small clearly labelled W43-only adapter/launcher in \`sources/2026-W43/execution/runtime-compat/\` (or \`sources/2026-W43/execution/tools/\` if already standard). Use Python in-process wrapper/monkey patch/adapter around **only the listed W43 Draft-entry Screening basis validation and its incompatible direct-local \`verify_state_basis\` invocation**, or an equivalent bounded adapter to the trusted agent-first State resolver. No changes to tracked \`scripts/\`, \`config/\`, \`schemas/\`, \`tests/\`, \`.github/\`, main or frozen branch, and no persistent rewrite of accepted Screening/State/Architecture/Approval inputs.
2. Pre-admission: read actual current W43 state, profile, accepted Screening package and acceptance, Discovery, current approved Architecture; check W43 identity and Stage, active approvals, both State-vs-package expected hashes exactly as diagnosed, original profile/discovery/prompt/schema hashes, accepted package/hash, and call **existing agent-first State validator**. If any of these differ, bypass is DISABLED and aborts.
3. Bypass only the **known false-positive historical State equality and the old direct-local validator convention**. Preserve original Screening's checks for prompt, result contract, archived batch files, accepted Discovery root/effective resolver and raw SHA binding; preserve ordinary Draft package derivation checks for Matrix/Selection/Architecture and result/schema evaluation. Do not use catch-all exception suppression, blanket disable all validation, tamper with \`core.sha256_file\` globally, substitute a fake State or put an invisible changed \`package.json\` on disk.
4. Execute the existing \`run_drafting_synthesis_v2_interactive.py\` in the process after inserting temporary wrapper(s). Reuse previously prepared \`sources/2026-W43/execution/defects/w43-draft-r1-interactive-input-UNVALIDATED-20261025.json\` as a **provisional input** only; validate package count eight, schema, provenance and current P1–P8 claims. Since it precedes the r8 editorial PDF, do not assume its prose equals approved r8. If approved r8 PDF's exact reader prose would be compromised by any new publication rendering, STOP before preview; do not silently substitute this Draft result for the Human-approved proof.
5. Preserve honest \`EDITION_LOCAL_RUNTIME_COMPAT_USED\` marker and precise bypassed function names/reason in a new W43 execution report. Call native result/Schema checks wherever feasible. Produce real Draft Packages/Results, synthesis output and actual return code. If another independent mismatch surfaces outside the same known legacy-vs-agent-first authority convention, do not expand the bypass unboundedly: stop with actual error.
6. Do **not** run an additional large test suite or ask for another comprehensive independent audit. Minimal acceptance = exact upstream pins, agent State validity, eight genuine P1–P8 produced result files and synthesis, schema/validator outcome, SHA-256 of outputs, no source/State/Gate mutation. Do not label compatibility-assisted validation as a clean default frozen-Core pass.

## 3. Reader content boundary

Already Human-accepted r8 PDF is 22 pages with 20 tables, 3 figures, 5 code, 36 bibliography items and final five-paragraph 「今週の総括」. Human-approved r8 immutable PDF remains sole approved *content/layout proof*, NOT a canonical Preview. Do not silently downgrade content to the earlier provisional Draft input's ~22,185 chars, invent late claims, remove the recap, or reissue PDF to force a pipeline checkpoint.

If actual native draft results are generated, explicitly compare their reader content to the fixed r8 proof or report that faithful equivalence is not established; **any new canonical Candidate/PDF needs its own exact-byte Human Publication Preview approval** before Freeze/Release. Keep all 15 CURATED_REVIEW_REQUIRED source caveats.

Use the original Draft instruction as source for accepted P1–P8 architecture, substantive coverage and separate final 「今週の総括」:
\`sources/2026-W43/execution/instructions/sol-w43-approved-r6-substantive-japanese-draft-with-closing-recap-20261025.md\`.

## 4. Outputs and terminal

Allowed new or append-only EDITION paths only:
- \`sources/2026-W43/execution/runtime-compat/*\` — single-use launcher and byte-bound admission note, no generic Core patch.
- \`sources/2026-W43/draft/v2/*\` — actual outputs only if native runner genuinely produced them; the fixed r8 proof and earlier accepted research unchanged.
- \`sources/2026-W43/execution/compat-w43-draft-run-evidence-20261028.md\` — commands, input SHA, actual exit code and validator results, module names temporarily adapted, artifact paths + SHA, exact accepted State values and provenance boundary.
- \`sources/2026-W43/execution/SOL_W43_RUNTIME_COMPAT_DRAFT_HANDOFF.md\`, \`sources/2026-W43/execution/sessions/muse-w43-runtime-compat-draft-20261028.md\`;
- append-only \`sources/2026-W43/execution/index.md\`.

Never modify other edition files incl. \`production-state.json\`, \`gates/\`, canonical \`scripts/\` or the fixed r8 PDF/TeX/checker/sidecars; never add a new branch or push to main. No Stage advancement/ADVANCE_STAGE, no auto Human Preview approval, no Freeze, Release or merge, as none was authorized for this *compatibility unit*. All fixed files remain byte-identical.

Normal terminal: \`MUSE_W43_RUNTIME_COMPAT_DRAFT_ARTIFACTS_READY_FOR_SOL\` with real generated Draft/Synthesis paths, hashes and remote SHA/Tree. On failure: \`MUSE_W43_RUNTIME_COMPAT_BLOCKED\` with actual cause and any safe bounded outputs (report pushed). No claimed success if no native artifact created. Never block merely because “read-only” was misread to forbid fetch, local fast-forward, documentation output or push.

This instruction implements the Human's explicit preference: W43-only workaround and quick execution, without design refactoring or a new rigorous regression/audit cycle.
