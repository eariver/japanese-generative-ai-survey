# W33 Luna Selection proposal — session

Status: `SELECTION_CANDIDATE_READY_FOR_SOL_REVIEW`

Issue: `2026-W33`
Branch: `weekly/2026-W33-v2-work`
Handoffs: `sources/2026-W33/execution/handoffs/w33-selection-luna-r1.md` → `sources/2026-W33/execution/handoffs/w33-selection-luna-r2.md`

## Starting authority

- Caller-supplied exact starting SHA: `63ebd6ce57c7d8867a45e5cadd4f0dd37d8b772a`.
- Per **Owner instruction**, the specified branch HEAD was cloned into a new working directory before task execution. Clone-time branch was `weekly/2026-W33-v2-work`; clone-time local HEAD and remote tracking HEAD both matched the supplied SHA.
- Reviewed main: `6267de3f6876f491950139757bfdf1085fc07bdc`.
- Production State before and after the worker task: SHA-256 `c9287b2e6f4d1e5a083db11787ac4f73b4a83b5c5cc1f4bfec87d2c96b0c8728`; lifecycle `EVIDENCE_REVIEWED`; next action `stage:selection`; terminal reason `null`.
- The required Selection handoff r1 was read in full before corrective overlay r2. r2 was applied as the controlling correction only for the Candidate Matrix runtime route.

## Actions actually performed

- Read the reviewed-main Core/bootstrap/record/schema/script authorities, including `survey_architecture_v2.py`, `survey_architecture_v2_base.py`, `survey_stage_validation_v2.py`, and the r2-required `survey_agent_tool_v2.py`; read the current Profile/State/index, prior Sol/E/M/C authorities, and the exact frozen Evidence, repaired Edition View, Materiality Ledger, and Profile Completeness artifacts.
- Performed no new research, source acquisition, Discovery/Screening/Evidence/View/Ledger/Completeness change, or semantic upstream repair.
- Derived the Candidate Matrix only from the frozen 37-result Evidence and repaired 37-view authority. The run used `scripts.survey_agent_tool_v2.current_stage_basis_override()` and `core.repository_commit_sha(repo)` from the checked-out work branch. At derivation time the actual implementation identity was the checked-out starting HEAD `63ebd6ce57c7d8867a45e5cadd4f0dd37d8b772a`; the reviewed-main SHA was not substituted.
- Proposed a complete Selection assignment for every Matrix candidate under the frozen W33 rubric. Materiality was treated as a pool rather than automatic inclusion; duplicate/index/channel records were single-homed; X remained context-only.
- Used a second fresh clone at canonical candidate HEAD for final equality and stage-contract verification. No Selection checkpoint, `ADVANCE_STAGE`, Architecture, Draft, publication, or Human Gate operation was run.

## Candidate Matrix

- Path: `sources/2026-W33/candidate-matrix-v2.json`
- SHA-256: `1b660291564bda5f30debd86bb6911eb53edf06e8f735710f84652d972c4d198`
- Candidate count: 37.
- Materiality: `MATERIAL 25 / CONTEXT 6 / HOLD 6`.
- Evidence: `VERIFIED 20 / PARTIAL 11 / NEEDS_MORE 6 / REJECTED 0`.
- Basis binds Profile `19303fcc8499a9cd7303991e69cfc0777a716db897537f50c5a9cff8dcb3f72b`, Completeness `9ac456d53a5a5195fc4925a72b3576ebe848a127ad0d5de2275f7d12752e8aea`, Ledger `cd29a1f640ce94229ed8c7f0734ddab9554ea5ffb8d4375900fe89f3a31f1891`, Evidence acceptance `b76be501746c814f0f646050706e92b21143be7046c745a35b6ec2ad03b8bdef`, and Edition View acceptance `6c94ede36420b1fe4b283481d141bb7dc8b6dcd1d7b5266060cebfd64e1a8632`.
- Matrix schema validation: `PASS`.
- Fresh deterministic re-derivation under the r2 override at the starting implementation identity: `PASS` (exact JSON equality).
- Fresh deterministic re-derivation under the same override at canonical candidate HEAD `d1dbfd1d58d61d11acf863e3845d7828adf9301a`: `PASS` (exact JSON equality; output remains byte-identical).

## Candidate Selection

- Path: `sources/2026-W33/candidate-selection-v2.json`
- SHA-256: `9c6997d2ed3921a847db5e001ec9377189bb25d5475454593f23016308557005`
- Selection version: `w33-selection-luna-r1`; status: `ESTABLISHED`.
- Exactly 37 assignments: `PASS`; unique candidate IDs: `PASS`.
- Distribution: `SELECTED 28` (`PRIMARY 21 / SUPPORTING 7`), `HOLD 6`, `REJECT 3`, `INSPECT 0`.
- All selected candidates are `MATERIAL` or `CONTEXT` with `VERIFIED` or `PARTIAL` Evidence. All six fixed HOLD candidates remain non-selectable. Selected CONTEXT candidates are SUPPORTING only. Non-selected candidates carry `NONE` architecture usage and null roles.
- Fixed HOLD candidates: RepoWise, MiniMax index, Copilot cloud-agent, GPT-5.6 update, Kimi K3 Copilot availability, and Claude Opus 4.1 retirement re-check.
- REJECT decisions: the post-cutoff Z.ai GLM index duplicate, the lower-marginal-value broad Transformers release after runtime/model consolidation, and Open-EA where the bound abstract cannot separate novelty from earlier ACL work.
- Single-home/consolidation decisions: the dedicated GLM, Gemini, and Grok records own substantive event coverage while their indices are chronology/support; GPT-5.6-Cyber/Daybreak Red owns the cyber event while Bedrock and partner records are supporting access/governance context; FlashInfer supports the selected serving-runtime story; X is a community-signal support only.
- Candidate-specific rationales preserve the accepted limitations for GLM-5.3, GPT-5.6-Cyber, GPT-5.6 Sol Ultrafast, VoiceDesigner, vendor/project/author-reported claims, and chronology boundaries. No generic rationale was used.

## Frozen upstream bindings

| Authority | Path | SHA-256 / identity |
|---|---|---|
| Production Profile | `sources/2026-W33/production-profile.json` | `19303fcc8499a9cd7303991e69cfc0777a716db897537f50c5a9cff8dcb3f72b` |
| Production State | `sources/2026-W33/production-state.json` | `c9287b2e6f4d1e5a083db11787ac4f73b4a83b5c5cc1f4bfec87d2c96b0c8728` |
| Discovery JSONL | `sources/2026-W33/discovery/discovery-v2.jsonl` | `632ba2335e5b937e9c6401c965edba735637631c7ef66551a070d7455a82f3b0` |
| Screening acceptance | `sources/2026-W33/screening/v2/accepted/648a1e8861c8edccb19d27623ba7dd8107d890c6f12fc88b7193ad99eb661706/screening-accepted.json` | `3ca7c986bb5857fe71ba9348dfda69b8e96320a36eda021b2a5dff39462ce84b` |
| Evidence acceptance | `sources/2026-W33/evidence/v2/accepted/c86f49f8cb9a627fe45ebc9ae49826bdec83de5ab9061c0ee7236f1a2a0ba524/evidence-accepted.json` | `b76be501746c814f0f646050706e92b21143be7046c745a35b6ec2ad03b8bdef`; result-set `c86f49f8cb9a627fe45ebc9ae49826bdec83de5ab9061c0ee7236f1a2a0ba524` |
| Edition View acceptance | `sources/2026-W33/evidence/v2/views/accepted/51f4dda8e565a67ea514c02aa5bff22f60d8f22237a6040bd3916cdf121b194f/edition-views-accepted.json` | `6c94ede36420b1fe4b283481d141bb7dc8b6dcd1d7b5266060cebfd64e1a8632`; view-set `51f4dda8e565a67ea514c02aa5bff22f60d8f22237a6040bd3916cdf121b194f` |
| Materiality Ledger | `sources/2026-W33/materiality-ledger-v2.json` | `cd29a1f640ce94229ed8c7f0734ddab9554ea5ffb8d4375900fe89f3a31f1891` |
| Profile Completeness | `sources/2026-W33/profile-completeness-v2.json` | `9ac456d53a5a5195fc4925a72b3576ebe848a127ad0d5de2275f7d12752e8aea`; accepted status `INCOMPLETE` |

## Deterministic validation

- Candidate Matrix schema: `PASS`.
- Candidate Matrix current-Core derivation under `current_stage_basis_override()`: `PASS`.
- Candidate Matrix fresh equality: `PASS`.
- Candidate Selection schema: `PASS`.
- `survey_architecture_v2.py selection-check`: `PASS`.
- Complete 37-assignment/eligibility/HOLD/context-support/manual semantic checks: `PASS`.
- Current-stage validator with exactly Matrix and Selection as current artifacts, run before candidate commit: `CORE_STAGE_CONTRACT PASS`, `EVIDENCE_REVIEWED -> SELECTION_COMPLETE`, implementation identity `63ebd6ce57c7d8867a45e5cadd4f0dd37d8b772a`; scratch report SHA-256 `a0939234444ed923203882ad1d986e61aa715aa34a360813b241ceaa8a63f785`, 1639 bytes.
- Current-stage validator in the fresh canonical candidate clone: `CORE_STAGE_CONTRACT PASS`, implementation identity `d1dbfd1d58d61d11acf863e3845d7828adf9301a`; scratch report SHA-256 `6cc70fd220a52893206c7eba78cab4fcadfb9643db05736f52667c3286746390`, 1639 bytes.
- `git diff --check`: `PASS`.
- Production State byte identity: unchanged from preflight through final canonical candidate clone (`c9287b2e6f4d1e5a083db11787ac4f73b4a83b5c5cc1f4bfec87d2c96b0c8728`).
- Selection checkpoint: not created. `ADVANCE_STAGE`: not run. Architecture work: not started.

## Git boundary and transport

- Local candidate commit: `7e46390b5cc7f40f2b570230958e4ea43bd53d5f`.
- Canonical GitHub candidate commit: `d1dbfd1d58d61d11acf863e3845d7828adf9301a`.
- Both candidate commits are direct children of `63ebd6ce57c7d8867a45e5cadd4f0dd37d8b772a` and have identical tree `786c928758b61abbcabeea30b4d7207cb48a9003`.
- The candidate commit changed exactly `sources/2026-W33/candidate-matrix-v2.json` and `sources/2026-W33/candidate-selection-v2.json`.
- The canonical candidate ref update was performed through the authenticated GitHub connection with `force=false`, after confirming the remote branch still pointed to the exact starting SHA. No force push, rebase, merge, or history rewrite was used.
- This file is the only bookkeeping path in the final commit. The local bookkeeping commit is created from canonical candidate `d1dbfd1d58d61d11acf863e3845d7828adf9301a`; because the authenticated connector reconstructs the equivalent commit, its canonical bookkeeping SHA is reported in the final closeout alongside the local SHA. The bookkeeping commit changes only this session record.

## End state / Sol handoff

- Successful bounded-worker stop: `SELECTION_CANDIDATE_READY_FOR_SOL_REVIEW`.
- Sol is the next owner for semantic review of the exact Matrix/Selection bytes, including the 28 selected proposals, six fixed HOLDs, three rejects, and single-home rationale.
- No Selection checkpoint or lifecycle transition was created. The branch remains at lifecycle `EVIDENCE_REVIEWED` with `stage:selection` pending.
