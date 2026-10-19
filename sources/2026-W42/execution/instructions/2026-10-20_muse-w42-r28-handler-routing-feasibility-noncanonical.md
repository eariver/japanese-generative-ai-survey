# J-GAS W42 Muse r28 — Core v2 handler/validator routing feasibility ONLY

Date: 2026-10-20 JST
Status: `SOL_EXECUTION_AUTHORITY / HUMAN_ROUTE_A_CONDITIONAL / R28_ROUTING_PROOF_READONLY_CANONICAL / NONCANONICAL_ONLY`
Repository: `eariver/japanese-generative-ai-survey`
Existing work branch ONLY: `weekly/2026-W42-v2-work`

## 0. Exact guards; no destructive local alignment

Sol dispatch supplies **Exact Starting Remote HEAD** and **Expected Starting Root Tree** for the commit containing THIS contract. Before any files/write, read remote W42 ref and root tree and prove identical full SHAs; also read reviewed main HEAD `c8d0ecc1c9566a2303ad3b4c42635d4b672650e4` / Tree `801de813319f08777ab1581a5e8875fc1ac5df19`; Frozen Core v2 HEAD `774dd39a951c9ac3818e83dfffd4c7666efb0a20` / Tree `cd46a6f7a6dcc4031e76220cea4c52c7dd1fc481`; State-pinned implementation `a4f25630270f029656f35771592f9ebda02fa5cc` / Tree `e68560d1542806b61b4c55f03063839fd2ec30c0`; fixed audited r26 `2981b30b783e858737fc69cf439afbbfe19d5105` / Tree `617a52200d82575b91a3cd345037daad2e8fbbbd`. Verify the pinned SHA from actual Production State, not from this instruction alone.

Any mismatch / missing ref / dirty checkout threatening existing work => ZERO WRITES STOP, expected vs actual; do not use `reset --hard` even locally. An isolated, newly-created clean worktree/clone may be used **without creating a new branch**, but the existing checkout must not be reset/rebased/re-written. No force, reset, rebase, new/fallback/review/repair branch. Before push recheck exact remote HEAD lease; normal commit and non-force fast-forward only.

Protected BYTE-EXACT: all shared Core/config/scripts/schemas; canonical W42 Architecture r1, approval/gates/review-index, Discovery through Draft, r18 Reader master (blob `fc4fd9f263c0865fd98e1c3f979c7a127bf6a439`), official documents; `production-state.json` (blob `63edc922e9cb94b3de9c0fc01d9ed01aa0d87afb`); all orchestration checkpoints and authoritative stage artifacts; all historical execution r11–r27; all r26 diagnostic PDF/TeX/PNG evidence. NO Stage/Gate/Candidate/Publication/Freeze/Release action. New write allowlist ONLY `sources/2026-W42/execution/governance/handler-routing-r28/`, a new `execution/sessions/muse-w42-r28-20261020.md`, and a truthful append-only `execution/index.md`. Do not modify the Human decision or Sol review that authorized this unit.

## 1. Read-first authority and precise research question

In order:
1. `execution/governance/pageplan-r27/human-w42-r27-conditional-route-a-approval-20261020.md` and `execution/reviews/sol-w42-r27-state-pinned-handler-mismatch-20261020.md`; Sol r27 conditional decision and Muse r27 Core route report, r26 independent audit, approved r1 Architecture and its Gate chain.
2. `production-state.json` implementation pin / next_action / lifecycle; state-pinned and reviewed-main `config/survey-production-v2.json`, `scripts/survey_handlers_v2.py`, `scripts/survey_orchestrator_v2.py`, `scripts/survey_agent_control_v2.py`, `scripts/survey_reader_fidelity_v2.py`, `scripts/survey_reader_publication_v2.py`, `scripts/survey_publication_v2.py`, stage/action-spec schema and actual operator-bridge protocols.
3. Search the existing, **already-authorized** repository modules/bridge executions for potential registered `stage:reader-publication-validation` / `validate:reader-publication`, not only default `register_handlers`. Inspect whether any outside module can be supplied via documented `--handler-module` without bypassing frozen Core or violating the pinned implementation contract; record actual path, ref, function signatures, semantics and provenance.

Question: **Is there an existing, authorized, safe dispatch path that can execute the exact DRAFT_COMPLETE stage/validator identities of the frozen State-pinned Core without changing canonical Core/config/state or substituting unmatched semantic functions?**

## 2. Required technical proof, strictly isolated and noncanonical

- Report the DRAFT_COMPLETE stage action handler/validator and registered identities; validate against the actual frozen action-spec contract, `stage_plan`, `next_action` and schema. Include all relevant exact file paths, functions and Git blob SHAs. Both handler AND validator must be accounted for.
- Evaluate (a) normal default `survey_handlers_v2` registry (expected missing names), (b) any genuine pre-existing `--handler-module` registrars, and (c) any first-party operator bridge that lawfully supplies compatible identities. Do not invent or hot-patch aliases, rebind names to semantically unproven implementation, hand-write checkpoint attestations, or claim a registry entry alone equals verified stage semantics.
- If a candidate is found, run **only non-mutating import/static calls and tests in a separate disposable local copy with synthetic/mock State and output paths outside canonical repo**; show callable signatures, exact handler output schema, validator result semantics, initial and next lifecycle, failure cases, and whether an actual accepted registry is documented. Treat writes in the isolated test sandbox as NONCANONICAL, do not accidentally load the live edition state as an output target.
- If no candidate exists, prove negative scope precisely: which registry/modules/bridge descriptions were searched and what remains unknowable, provide `BLOCKED`, not a fake workaround. Distinguish missing default mapping from wider impossibility.
- Specifically analyze whether the existing `stage:semantic-publication-validation` / `validate:semantic-publication` can lawfully apply to the `reader-publication` configuration; assume NOT interchangeable unless matching Core contract and registration are proven.
- Check whether State `implementation.repository_commit_sha` and historical frozen config blobs are identical to reviewed main for relevant files; record hashes. Identify the proper separate Core-maintenance owner/repository workflow if stage identities truly mismatch. No maintenance implementation or W42 stage advancement in r28.
- NO Reader/PDF build and NO content/print re-audit. The independent r26 report already adjudicated that separately.

## 3. Reviewable outputs and exact stopping points

Write new:
- `execution/governance/handler-routing-r28/default-and-pinned-registry-map-r28.md`: two identities vs actual registrations, immutable refs and functions, proven mismatch.
- `execution/governance/handler-routing-r28/operator-module-bridge-search-r28.md`: candidate modules, registration interfaces, provenance and bounded source search, explicit negative findings.
- `execution/governance/handler-routing-r28/read-only-stage-contract-feasibility-r28.md`: if candidate viable, isolated proof with reproducible commands and object hashes; if blocked, specific fatal missing dependency + proposed independent Core triage.
- `execution/governance/handler-routing-r28/sol-human-next-stage-routing-decision-packet-r28.PROPOSED.md`: decision tree, earliest safe canonical operation IF separately authorized, no promise of publication.
- `execution/sessions/muse-w42-r28-20261020.md` and truthful append-only index.

Terminal only:
- `SOL_W42_R28_HANDLER_ROUTING_REVIEW_READY / NONCANONICAL` if an **existing Core-compliant dispatch path** is demonstrably proven at handler + validator + Stage contract levels, without canonical effects; still STOP for separate Sol/Human authorization before implementing a canonical stage.
- `R28_HANDLER_ROUTING_BLOCKED / CORE_MAINTENANCE_REQUIRED` if no such path has been demonstrated, or proof is incomplete. Do not claim that a workaround/alias has passed.
- `R28_GIT_GUARD_STOP` if preflight identities do not match: zero writes.

Perform normal FF commit/non-force push of only allowlisted files, remote read-back of final SHA/tree, list evidence and limitations. Human's conditional Route A approval stays recorded, Core r1 remains active, no Reader, Gate, Publication, Freeze or Release.
