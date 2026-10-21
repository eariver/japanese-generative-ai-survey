# J-GAS W42 — Sol read-only check: stage-handler mismatch persists in State-pinned implementation

Date: 2026-10-20 JST
Status: `SOL_SOURCE_VERIFICATION / MISSING_DEFAULT_HANDLER_AND_VALIDATOR / R28_ROUTING_PREFLIGHT_REQUIRED / NONCANONICAL`
Fixed W42 before this decision: HEAD `d3632e046d2b3bc859f327085209a5a8409e67d4`, Tree `20356b04224b163ceffb2d7c1ec48ef2e420c338`.
Reviewed `main` HEAD `c8d0ecc1c9566a2303ad3b4c42635d4b672650e4` / Tree `801de813319f08777ab1581a5e8875fc1ac5df19`; frozen Core branch HEAD `774dd39a951c9ac3818e83dfffd4c7666efb0a20` / Tree `cd46a6f7a6dcc4031e76220cea4c52c7dd1fc481`.
**State-pinned implementation** commit `a4f25630270f029656f35771592f9ebda02fa5cc` / Tree `e68560d1542806b61b4c55f03063839fd2ec30c0` (from committed `sources/2026-W42/production-state.json`).

## Direct source evidence

At **both the reviewed-main commit and the State-pinned implementation commit**:
- `config/survey-production-v2.json`: Git blob `cffe16fec2186d5d7c1297aa49b830d639865e96`, at `orchestration.stage_plan.DRAFT_COMPLETE` requires `stage:reader-publication-validation` with `validate:reader-publication`.
- `scripts/survey_handlers_v2.py`: Git blob `510a2abada13a165d404fba57a78daa67af2ff77`. Default `register_handlers` lists `stage:semantic-publication-validation` and `validate:semantic-publication` instead; it contains NEITHER of the two configured `reader-publication` identities.
- `scripts/survey_orchestrator_v2.py`: Git blob `5019b4f3d618cae6af3bc37dd7258bc5f49e1f68`. `execute_action` looks up `registry.get(spec["handler"])` and `registry.get(spec["validator"])` and fails if either is not callable. CLI permits modules via `--handler-module` but that does **not itself** prove any eligible module exists, matches the bound stage contracts, or has a genuine semantic validator.

This is not a transient difference between latest reviewed main and the historical State-pinned implementation: relevant Git blobs are identical. It is a **dispatch/registry compatibility gap at default registration**, not proof that every separately permitted operator path fails.

`DRAFT_COMPLETE`, active human r1 Architecture Gate approved and Publication Preview pending are unchanged, so Core's formal Architecture revision APIs cannot be used to avoid this issue. The independent r26 CONTENT=PASS / PRINT=PASS_WITH_LIMITATIONS remains in force and should not be reaudited in r28.

## Sol disposition

Human Owner approved **Route A conditionally**, not canonical stage advancement. Authorize r28 to discover (read-only) a **pre-existing, genuinely Core-compliant routing module/bridge** and to prove precise handler/validator semantics using isolated synthetic dry-runs. Verify actual configuration, State-pinned implementation, output/input contract, validator evidence, and no unsupported alias. If none exists: `R28_HANDLER_ROUTING_BLOCKED`; escalate to separately reviewed, non-W42 frozen Core maintenance work, no silent changes. An implementation mismatch is NOT authorization to write modified Core.

No automatic Reader/Gate/Publication action. No remote branch mutation except edition-local decision, this Sol note, and subsequent versioned noncanonical execution.
