# 2026-W33 Sol→Luna handoff — Selection runtime correction r2

Status: `READY_FOR_LUNA / CORRECTIVE_OVERLAY_FOR_SELECTION_R1`

Issue: `2026-W33`  
Canonical branch: `weekly/2026-W33-v2-work`  
Reviewed main: `6267de3f6876f491950139757bfdf1085fc07bdc`  
Base Selection handoff: `sources/2026-W33/execution/handoffs/w33-selection-luna-r1.md`

This file is a narrow corrective overlay. Read r1 in full, then apply this r2. **r2 wins on every conflict.** All Selection semantics, frozen authorities, allowed writes, validation rules, stop conditions, and Sol/Luna responsibilities from r1 remain unchanged except for the Candidate Matrix runtime route described below.

## 1. Why this correction exists

The direct `survey_architecture_v2.py matrix` command shown in r1 is not the canonical agent-first execution route after Production State has advanced beyond the lifecycle boundary recorded inside the accepted Screening/Evidence packages.

Those accepted content-addressed packages intentionally retain the historical `state_sha256` from the stage where they were created. Current Core allows that exact historical State-SHA difference only through the fail-closed `scripts.survey_agent_tool_v2.current_stage_basis_override()` context.

That override:

- requires the implementation SHA supplied to helper validation to equal the **actual current work-branch commit**;
- validates the current agent-first Production State;
- permits only the historical `state_sha256` difference for an already content-addressed accepted Screening/Evidence package whose archived package hash is still exactly bound by its sibling acceptance;
- reruns the remaining package/contract/source checks against current repository bytes.

Therefore:

- do **not** use the r1 direct Matrix CLI with `--implementation-sha 6267de3...`;
- do **not** weaken or bypass package-basis validation manually;
- do **not** edit archived package State hashes;
- use the current-stage override and the actual current work-branch implementation SHA.

Reviewed main `6267de3...` remains the reviewed Core authority for reading the implementation. It is not the runtime implementation identity passed to the agent-first Matrix derivation at this stage.

## 2. Additional mandatory read

In r1 required-read order, immediately after `scripts/survey_stage_validation_v2.py`, also read:

`scripts/survey_agent_tool_v2.py`

Pay particular attention to:

- `verify_current_stage_basis()`;
- `_historical_state_basis_wrapper()`;
- `_historical_screening_basis_wrapper()`;
- `_historical_evidence_basis_wrapper()`;
- `current_stage_basis_override()`.

If current reviewed Core no longer provides equivalent fail-closed semantics, stop with `CORE_OR_AUTHORITY_DRIFT_NEEDS_SOL_REVIEW`.

## 3. Correct Candidate Matrix derivation route

The Candidate Matrix path remains:

`sources/2026-W33/candidate-matrix-v2.json`

Derive it from the exact frozen W33 authorities under the current-stage basis override. Equivalent Python logic:

```python
from pathlib import Path

from scripts import survey_agent_tool_v2 as runtime_tool
from scripts import survey_architecture_v2 as architecture
from scripts import survey_production_v2 as core

repo = Path(".").resolve()
implementation_sha = core.repository_commit_sha(repo)

profile = repo / "sources/2026-W33/production-profile.json"
discovery = repo / "sources/2026-W33/discovery/discovery-v2.jsonl"
screening = repo / "sources/2026-W33/screening/v2/accepted/648a1e8861c8edccb19d27623ba7dd8107d890c6f12fc88b7193ad99eb661706/screening-accepted.json"
evidence = repo / "sources/2026-W33/evidence/v2/accepted/c86f49f8cb9a627fe45ebc9ae49826bdec83de5ab9061c0ee7236f1a2a0ba524/evidence-accepted.json"
views = repo / "sources/2026-W33/evidence/v2/views/accepted/51f4dda8e565a67ea514c02aa5bff22f60d8f22237a6040bd3916cdf121b194f/edition-views-accepted.json"
ledger = repo / "sources/2026-W33/materiality-ledger-v2.json"
completeness = repo / "sources/2026-W33/profile-completeness-v2.json"
output = repo / "sources/2026-W33/candidate-matrix-v2.json"

with runtime_tool.current_stage_basis_override():
    payload = architecture.derive_candidate_matrix(
        repo,
        profile,
        discovery,
        screening,
        evidence,
        views,
        ledger,
        completeness,
        implementation_sha,
    )

architecture.write_candidate_matrix(output, payload)
```

At the time of derivation, `implementation_sha` must resolve to the exact current checked-out work-branch HEAD supplied by the caller. If it does not, stop rather than substituting reviewed-main SHA or another commit.

## 4. Fresh Matrix equality check

After writing the Matrix, independently derive the payload again under the same override and actual current work-branch implementation identity, then require exact JSON-object equality with the stored Matrix.

Equivalent logic:

```python
stored = core.load_json(output)
with runtime_tool.current_stage_basis_override():
    expected = architecture.derive_candidate_matrix(
        repo,
        profile,
        discovery,
        screening,
        evidence,
        views,
        ledger,
        completeness,
        implementation_sha,
    )
assert stored == expected
```

The expected counts remain exactly:

- 37 candidates;
- MATERIAL 25 / CONTEXT 6 / HOLD 6 / NON_MATERIAL 0;
- VERIFIED 20 / PARTIAL 11 / NEEDS_MORE 6 / REJECTED 0.

Do not hand-edit the Matrix after derivation.

## 5. Selection validation remains as r1

The Candidate Selection semantic contract and r1 rubric are unchanged.

After creating `sources/2026-W33/candidate-selection-v2.json`:

1. validate its JSON schema;
2. run `survey_architecture_v2.py selection-check` as specified by Core;
3. run `scripts/survey_stage_validation_v2.py` with exactly `candidate-matrix` and `candidate-selection` as current artifacts.

The stage validator itself already enters `current_stage_basis_override()` for current-stage semantic validation, so do not wrap it in an additional custom relaxation.

Expected validation target:

`EVIDENCE_REVIEWED -> SELECTION_COMPLETE`

Validation only. Do not create a checkpoint and do not advance State.

## 6. Session-record requirement added by r2

In the Luna Selection session record, explicitly record:

- actual current implementation SHA used for Matrix derivation;
- confirmation that `current_stage_basis_override()` was used;
- confirmation that the reviewed-main SHA was **not** substituted as runtime implementation identity;
- fresh derivation equality result;
- confirmation archived Screening/Evidence package bytes and historical State hashes were not edited.

## 7. Stop condition

All r1 stop conditions remain unchanged.

Successful stop remains:

`SELECTION_CANDIDATE_READY_FOR_SOL_REVIEW`

No Selection checkpoint, `ADVANCE_STAGE`, Architecture work, or upstream semantic mutation is authorized.