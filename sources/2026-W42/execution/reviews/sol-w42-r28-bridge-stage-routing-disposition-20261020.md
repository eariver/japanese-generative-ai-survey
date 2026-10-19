# W42 Sol r28 disposition — bridge route verified; canonical build still requires separate Human authorization

Date: 2026-10-20 JST
Status: `SOL_W42_R28_ROUTING_PREFLIGHT_ACCEPTED_WITH_DOCUMENTATION_ERRATA / HUMAN_R29_AUTHORIZATION_PENDING / NO_CANONICAL_ADVANCE`
Repository: `eariver/japanese-generative-ai-survey`
Fixed r28 HEAD: `84e109c6f27eab83419bd64cc89415d8ac2e10de`
Root Tree: `3cb708e0e592c169d8a4d71f7943636872f34cb2`
Starting r28 authority HEAD/Tree: `4cd1ad90daf543fa15676e94e27b0fcd1f69839a` / `b05ca63337af6839608547565bca6306caafb57f`
State-pinned Core implementation: `a4f25630270f029656f35771592f9ebda02fa5cc` / `e68560d1542806b61b4c55f03063839fd2ec30c0`

## 1. Scope and evidence

Read-only GitHub verification: r28 is exactly one normal fast-forward from approved instruction baseline. Changed paths: four `execution/governance/handler-routing-r28/` reports, one session, append-only `execution/index.md`. Main/Frozen Core heads unchanged. W42 protected `production-state.json` Git blob `63edc922e9cb94b3de9c0fc01d9ed01aa0d87afb`, Architecture r1 blob `14e17d80c148747ef1804ac7d80a3cf4e5d12bbf`, Gate review index blob `6682579c135fc72599bfdbb883621da726e09f83`, r18 Reader master blob `fc4fd9f263c0865fd98e1c3f979c7a127bf6a439` all matched at r28.

Worker terminal `SOL_W42_R28_HANDLER_ROUTING_REVIEW_READY / NONCANONICAL`, evidence files:
- `execution/governance/handler-routing-r28/default-and-pinned-registry-map-r28.md`
- `execution/governance/handler-routing-r28/operator-module-bridge-search-r28.md`
- `execution/governance/handler-routing-r28/read-only-stage-contract-feasibility-r28.md`
- `execution/governance/handler-routing-r28/sol-human-next-stage-routing-decision-packet-r28.PROPOSED.md`.

## 2. Sol's direct source corroboration — separate dispatch transports

At State-pinned implementation `a4f25630270f029656f35771592f9ebda02fa5cc` (identical relevant blobs at reviewed main `c8d0ecc1c9566a2303ad3b4c42635d4b672650e4`):
- `config/survey-production-v2.json` stage DRAFT_COMPLETE names `stage:reader-publication-validation` and `validate:reader-publication`.
- `scripts/survey_handlers_v2.py.register_handlers` lacks BOTH, so default `survey_orchestrator_v2.execute_action` would fail closed.
- Existing **authorized** `.github/workflows/survey-production-v2-operator-bridge.yml` runs trusted-reviewed `survey_core_execution_bridge_v2.py` directly, not `survey_orchestrator_v2.py`.
- `scripts/survey_core_execution_bridge_v2._advance_stage` invokes `survey_stage_validation_v2.validate_stage` directly, then checkpoint validation via `survey_agent_control_v2.build_stage_checkpoint`; no handler registry involved. This is an EXISTING first-party Core transport, not an invented alias or bypass.
- `survey_stage_validation_v2.REQUIRED_CURRENT['DRAFT_COMPLETE']` requires **seven** current artifacts: manuscript, validated-source, PDF, quality bundle, semantic review, visual review, reader-surface-gate. `_current_artifacts` requires them exactly, no extras, and validates source/PDF/reviews/Gate.
- Frozen config lists only the first **six** as canonical `stage_plan` artifacts. The agent `_validate_stage_artifacts` verifies that all configured artifacts are supplied and their paths match; **it does not reject an additional seventh** (verified direct source). Thus this configuration asymmetry need not block a correctly supplied seven-artifact Bridge request; independent end-to-end execution with real reviewed artifacts has NOT occurred.
- `schemas/operator-execution-request-v2.schema.json` permits artifact array entries (not a six-only fixed tuple); Bridge `_artifact_map` verifies unique names and repo-local existing files.

**Editorial disposition:** accept `ROUTING_PREFLIGHT_PASS / NONCANONICAL`, with a strict distinction between proof of correct routing and proof that an assembled **real** seven-artifact stage will pass. Human Route A's routing condition is satisfied at the preflight level; substantive semantic/visual and Reader-Surface Gate acceptance remain future evidence. No canonical Stage/Gate transition is authorized by this Sol note.

## 3. Worker report clerical errata (retain historical files)

- r28 registry map reports `action_kind: LOCAL_STAGE` for `DRAFT_COMPLETE`; actual frozen config reads `action_kind: LOCAL_SCRIPT`. This is a documentation transcription error; the Bridge's exact stage semantics were correctly examined and do not depend on the mistaken label in the worker report.
- r28 session's "Dispatched remote ... Tree" string is mistyped as `b05ca63337af6839608547565ca6336aafb57f`, which differs from actual accepted start Tree `b05ca63337af6839608547565bca6306caafb57f`. Independent Git history/branch-tree comparisons establish the true baseline; **the session text alone cannot be cited as correct exact-tree evidence**. Preserve raw r28 session unchanged, correct in this Sol annotation, and explicitly require next Worker to verify full SHA live.
- r28 sandbox diagnostic log was saved under `/tmp/r28-sandbox` only, not included in GitHub. Repro commands/observations are recorded, but independent byte reexecution of that local log is unavailable. This is a limitation, not a reason to invent evidence or label tested full-stage success.

These are nonblocking evidence-documentation limitations for routing preflight, not waivers of no-reset policy. No further self-audit of r26 CONTENT/PRINT occurred, respecting the Human's independent-audit decision.

## 4. Future safe sequence requiring Human permission

The next useful unit is a **bounded formal-artifact build only** (provisionally r29): materialize canonical Reader Manuscript and publication TeX/PDF from the independently audited r18/r26 sources, plus deterministic evidence and **PROPOSED** review surfaces. STOP BEFORE fabricating or accepting any semantic/editorial/visual PASS or Reader-Surface Gate record, and BEFORE Bridge `ADVANCE_STAGE`. Separate independent Sol review of exact newly generated canonical Reader/PDF bytes is required; this may be followed by additional Human authorization and a bounded Bridge stage request after all seven true authorities exist and validate.

This cleanly separates Worker production from independent review: Muse cannot mark its own printed product as independently certified. Do not silently inherit the independent r26 noncanonical diagnostic audit as if it bound a different formal PDF SHA.

**Next Human decision requested:** authorize this bounded canonical build-to-independent-review unit under unchanged Architecture r1 and the accepted ~21-page editorial plan. A new precise Worker execution contract must be created only after Human acceptance. Any later stage execution is a separate permission boundary.

STOP: `SOL_W42_R28_ROUTE_FEASIBILITY_ACCEPTED / R29_HUMAN_AUTHORIZATION_PENDING / CORE_FROZEN`.
