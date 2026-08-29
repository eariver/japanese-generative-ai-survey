# 2026-W33 Luna Screening materialization session r1

Issue: `2026-W33`
Worker: `Work GPT-5.6 Luna`
Recorded: `2026-08-29T16:24:41Z`
Handoff: `sources/2026-W33/execution/handoffs/w33-screening-materialization-luna-r1.md`

## Authority and start

- Branch: `weekly/2026-W33-v2-work`
- Exact caller-supplied starting SHA: `3efd960e06f731cae4e2e6d671f99aff88a58c19`
- Reviewed `main`: `6267de3f6876f491950139757bfdf1085fc07bdc`
- Lifecycle before materialization: `DISCOVERY_COLLECTED`
- Machine next action before materialization: `stage:screening`
- Production State SHA-256 before materialization: `d2c1e856dbfa31e45d27a423cd103ba70088f3ca260dd1e86bade9cc1764ef96`
- Production State size before materialization: 3042 bytes

## Frozen semantic inputs

- Discovery path: `sources/2026-W33/discovery/discovery-v2.jsonl`
- Discovery record count: 41
- Discovery SHA-256: `632ba2335e5b937e9c6401c965edba735637631c7ef66551a070d7455a82f3b0`
- Discovery acceptance: `sources/2026-W33/discovery/discovery-accepted-v2.json`
- Discovery acceptance SHA-256: `62a37710b4f41df752fecf03b987baff423a40849bcfeb6e2f72f2d13fa39302`
- Sol semantic seed: `sources/2026-W33/screening/sol-screening-decisions-r1.json`
- Sol semantic-authority commit: `f9803239613f2208eb5eaf7ff56826031268728f`
- Sol semantic-authority blob: `ba649d6e805bac5316b88a78d259a3de97f839b2`
- Sol seed decision count: 41
- Sol seed aggregate: KEEP 26 / INSPECT 8 / MAYBE 3 / DROP 4
- Decision objects were copied without changing `discovery_id`, `decision`, `reason`, `scope_tags`, `duplicate_group`, `verification_targets`, or `confidence`.

## Actions actually performed

- Read the required reviewed-main authority and exact-start W33 authority in the order prescribed by the handoff.
- Fetched the remote branch read-only and confirmed that the supplied starting SHA was the current remote branch head.
- Preserved the prior local-only W33 Luna branch at `backup/w33-luna-discovery-local-e8`; created the requested local work branch at the exact supplied starting SHA without discarding prior commits.
- Created only an execution-local interactive wrapper in `/tmp`; no semantic Screening seed file was edited.
- Ran `scripts/run_screening_v2_interactive.py` with the current agent-first basis override. The runner generated one batch for all 41 records, created the content-addressed accepted run, and did not advance Production State.

## Generated candidate

- Accepted run directory: `sources/2026-W33/screening/v2/accepted/648a1e8861c8edccb19d27623ba7dd8107d890c6f12fc88b7193ad99eb661706/`
- Result-set SHA-256: `648a1e8861c8edccb19d27623ba7dd8107d890c6f12fc88b7193ad99eb661706`
- Sol r7 expected result-set ID comparison: `MATCH`
- Record count: 41
- Batch count: 1 (`batch-001`)
- Decision aggregate: KEEP 26 / INSPECT 8 / MAYBE 3 / DROP 4

Generated file hashes and sizes:

| File | SHA-256 | Bytes |
|---|---|---:|
| `package.json` | `186b2c0227af0faa405d0618c7fa5e0849075ec51d51d7da013f626801a10da7` | 1749 |
| `input/batches/batch-001.jsonl` | `3625115ac29672e7d33eb0691a8d5717cc49ee9e40cfda0ad326a90d31bda711` | 41832 |
| `results/batch-001.json` | `27f9a20441aa8c47f9d26eeb3474abc41ce5ac848dbade2b74ad0d100dd38baf` | 21724 |
| `screening-accepted.json` | `3ca7c986bb5857fe71ba9348dfda69b8e96320a36eda021b2a5dff39462ce84b` | 21661 |
| `interactive-decisions.json` | `259d73e35e52712f1985d633c42e779f05e2ebbe01752fbf9d66896117ed8607` | 21330 |
| `interactive-audit.json` | `24c4caf2a1c0e9cc40cd148e196d5f278c35eceabbd1d52df3ca8d8e68e4261c` | 853 |

## Validation

- Preflight State/Profile validation: `PASS`
- Discovery acceptance validation: `PASS`
- Current-Core interactive runner: `PASS`
- Accepted Screening validation under `current_stage_basis_override()`: `PASS`
- Accepted decisions equal the exact Sol seed after `discovery_id` sorting: `PASS`
- Exact 41-ID coverage and aggregate: `PASS`
- Package Discovery SHA and one-batch provenance: `PASS`
- Content-addressed directory name equals `result_set_sha256`: `PASS`
- Production State after materialization: unchanged, 3042 bytes, SHA-256 `d2c1e856dbfa31e45d27a423cd103ba70088f3ca260dd1e86bade9cc1764ef96`
- No Screening checkpoint was recorded.
- No Evidence, Materiality, Completeness, Selection, or Architecture artifact was created or modified.

The direct legacy validator path reports an implementation-basis mismatch if called without the handoff-prescribed `current_stage_basis_override()`; the runner and independent validation both used the prescribed override and passed. `jsonschema==4.23.0` and the repository requirements were installed only under `/tmp/w33-screening-r1-pydeps`.

## Candidate commit boundary

- Candidate materialization commit / ending SHA: `5c42802e954e0c48881e77a02e80f12f291b5edd`.
- Candidate commit parent: `3efd960e06f731cae4e2e6d671f99aff88a58c19`.
- Candidate commit includes exactly these seven paths:
  - `sources/2026-W33/screening/v2/accepted/648a1e8861c8edccb19d27623ba7dd8107d890c6f12fc88b7193ad99eb661706/package.json`
  - `sources/2026-W33/screening/v2/accepted/648a1e8861c8edccb19d27623ba7dd8107d890c6f12fc88b7193ad99eb661706/input/batches/batch-001.jsonl`
  - `sources/2026-W33/screening/v2/accepted/648a1e8861c8edccb19d27623ba7dd8107d890c6f12fc88b7193ad99eb661706/results/batch-001.json`
  - `sources/2026-W33/screening/v2/accepted/648a1e8861c8edccb19d27623ba7dd8107d890c6f12fc88b7193ad99eb661706/screening-accepted.json`
  - `sources/2026-W33/screening/v2/accepted/648a1e8861c8edccb19d27623ba7dd8107d890c6f12fc88b7193ad99eb661706/interactive-decisions.json`
  - `sources/2026-W33/screening/v2/accepted/648a1e8861c8edccb19d27623ba7dd8107d890c6f12fc88b7193ad99eb661706/interactive-audit.json`
  - `sources/2026-W33/execution/sessions/w33-luna-screening-materialization-20260830-r1.md`
- No `production-state.json`, Discovery, Sol semantic seed, Core implementation, checkpoint, or execution index path was changed.

## End state

- Stop status: `READY_FOR_SOL_REVIEW`
- Exact next owner: Sol semantic review of the committed Screening candidate.
- `ADVANCE_STAGE` was not executed.
- The candidate is not labeled as lifecycle-complete; Production State remains `DISCOVERY_COLLECTED` with next action `stage:screening`.
