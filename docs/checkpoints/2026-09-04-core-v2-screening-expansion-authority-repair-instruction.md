# Core v2 maintenance instruction — validated Screening Discovery expansion authority

Status: **READY_FOR_LUNA_CORE_MAINTENANCE**

Repository: `eariver/japanese-generative-ai-survey`

Maintenance branch: `fix/core-v2-screening-expansion-authority-20260904`

Branch base / reviewed main: `c7a898889463b049dea4ee7337ee16ad5fbf3191`

W34 read-only reproducer branch: `weekly/2026-W34-v2-work`

W34 read-only reproducer SHA: `7350dc3b6eeaa342c3d7d4292e4d386e701c7ba5`

W34 defect authority:

`sources/2026-W34/execution/defects/core-v2-screening-expansion-authority-20260904.md`

## 1. Purpose

Repair one shared-Core contract gap discovered by live W34 production.

Current Core can formally accept an initial source-centric Discovery graph and can separately validate/accept a provenance-preserving event-level Screening expansion, but formal lifecycle validation requires the Screening package to use the original accepted Discovery path byte-for-byte.

That prevents a legitimate post-Discovery 1→N expansion from flowing into Screening/Evidence and causes W34 formal advancement to fail even though the Screening acceptance itself is valid.

The required capability is:

```text
accepted root Discovery
        ↓ mechanically validated provenance-preserving expansion
validated effective Screening Discovery basis
        ↓
Screening acceptance
        ↓
Evidence / Views / Materiality / Completeness / Selection / Architecture
```

The original accepted Discovery remains immutable root provenance authority.

This task is Core maintenance only. Do not edit W34 production artifacts.

## 2. Mandatory read order

Before editing, read at least:

1. `AGENTS.md`
2. `docs/survey-production-core-v2-session-bootstrap.md`
3. `scripts/survey_screening_v2.py`
4. `scripts/survey_evidence_v2.py`
5. `scripts/survey_stage_validation_v2.py`
6. `scripts/survey_agent_control_v2.py`
7. `scripts/survey_agent_tool_v2.py`
8. relevant existing tests, especially Screening acceptance, Evidence task generation, stage/agent-first validation, Materiality/Completeness/Selection basis validation
9. W34 defect authority from exact read-only SHA `7350dc3b6eeaa342c3d7d4292e4d386e701c7ba5`
10. W34 read-only artifacts needed to reproduce the failure:
   - `sources/2026-W34/discovery/discovery-v2.jsonl`
   - `sources/2026-W34/discovery/discovery-accepted-v2.json`
   - `sources/2026-W34/screening/input/event-discovery-v2.jsonl`
   - `sources/2026-W34/screening/input/event-discovery-crosswalk-v0.1.json`
   - `sources/2026-W34/screening/v2/accepted/2ab82c6b52b26fc01cc6a82d20da08ef4b37dadaf2ff1b0e5a570f50652b3662/screening-accepted.json`
   - `sources/2026-W34/production-state.json`

W34 is a read-only reproducer. Never commit W34 files to this maintenance branch and never write to the W34 branch during this task.

## 3. Exact observed defect

At W34 state `DISCOVERY_COLLECTED / stage:screening`, current `survey_stage_validation_v2.py` rejects the valid Screening acceptance with:

`Screening acceptance is not based on accepted Discovery authority`

because:

- accepted root Discovery path = `sources/2026-W34/discovery/discovery-v2.jsonl` (40 records)
- Screening package effective Discovery path = `sources/2026-W34/screening/input/event-discovery-v2.jsonl` (105 records)

The 105 records are valid `survey-discovery-record` records and are derived from the accepted root through existing `provenance.origin`, `parent_refs`, source identity, and Raw bindings.

## 4. Do not solve this by weakening path checks globally

A repair that simply removes the equality check is unacceptable.

Core must continue to reject an arbitrary unrelated Discovery set substituted after formal Discovery acceptance.

The solution must mechanically validate the derivation relation.

## 5. Required derivation invariant

Implement a reusable Core validation/resolution function for an **effective Screening Discovery basis**.

Naming/API shape is your choice, but keep it profile-neutral and generic.

Behavior:

### Case A — direct basis

If the Screening package Discovery path/hash is exactly the accepted root Discovery path/hash, behavior remains unchanged.

### Case B — derived expansion basis

If the Screening package points to a different Discovery set, accept it only if every requirement below passes.

At minimum:

1. root accepted Discovery and derived Discovery both validate under the current Discovery v2 contract;
2. issue identity is identical;
3. every derived record uses an expansion provenance origin that requires parent refs; arbitrary `BASE` substitution is forbidden;
4. every `parent_ref` in every derived record resolves to an ID in the accepted root Discovery set;
5. every derived record has at least one accepted-root parent;
6. every accepted root Discovery record remains downstream-accounted by at least one derived child; silent root loss is forbidden;
7. every Raw path used by a derived child is already present in the union of Raw paths of that child's declared accepted-root parents;
8. each derived top-level source identity is rooted in at least one declared parent source. At minimum compare the stable source identity tuple suitable for this contract (`source_type`, `collector_id`, `collector_run_id`, `locator`) unless existing contract code provides a stronger canonical identity;
9. derived obligation IDs must not invent unrelated obligations outside the declared accepted-parent obligation union;
10. package hashes bind exact derived bytes;
11. no derived duplicate Discovery IDs;
12. no cross-issue parent or source substitution.

If W34 reveals that one proposed invariant is inconsistent with already-valid existing provenance, do not silently relax it. Record the exact mismatch and choose the strongest generic invariant that preserves the same anti-substitution guarantee.

## 6. Root authority versus effective task basis

Preserve two separate concepts:

- **root Discovery authority**: the formally accepted Discovery set from Discovery acceptance/checkpoint;
- **effective downstream Discovery basis**: either the root itself or a mechanically validated derived expansion selected by the accepted Screening package.

Do not overwrite or reinterpret the root authority.

## 7. Required downstream propagation

Once Screening acceptance is validated against a derived effective Discovery basis, all downstream stages that consume Screening/Evidence lineage must consistently use that exact effective Discovery set.

Audit and repair at least:

- `scripts/survey_stage_validation_v2.py`
  - `DISCOVERY_COLLECTED` Screening-stage semantics;
  - `_evidence_basis()` and every later stage deriving from it.
- `scripts/survey_evidence_v2.py`
  - Screening acceptance validation;
  - Evidence package preparation/basis validation;
  - Evidence acceptance;
  - Edition Views;
  - Materiality ledger;
  - profile completeness interfaces if they pass Discovery explicitly.
- Candidate Matrix / Selection / Architecture validators that receive a Discovery path from `_evidence_basis()` or equivalent.

Prefer one shared resolution function rather than duplicating expansion logic across stages.

Do not modify semantic editorial rules.

## 8. Evidence task granularity invariant

For a valid derived Screening basis, Evidence task generation must use the **derived** Discovery IDs and non-DROP Screening decisions.

It must not fall back to the root 40 source-centric IDs.

A synthetic 1-root→multiple-derived test must prove that multiple derived events produce independently screenable/evidentiary tasks.

## 9. Required fail-close tests

Add regression tests proving at least:

1. legacy/direct Screening basis still passes unchanged;
2. valid accepted-root → derived expansion → Screening acceptance passes;
3. valid expansion can proceed through stage validation for `DISCOVERY_COLLECTED -> CANDIDATES_NORMALIZED`;
4. Evidence package preparation uses derived IDs after advancement;
5. later `_evidence_basis()` validation resolves the same effective derived Discovery set;
6. orphan derived parent fails;
7. derived parent from another/unaccepted set fails;
8. derived child with invented Raw path fails;
9. derived child with unrelated source identity fails;
10. accepted root record silently omitted from the expansion fails;
11. arbitrary unrelated valid Discovery file substituted into Screening fails;
12. direct-basis existing tests remain green;
13. agent-first compatibility tests remain green.

Use synthetic fixtures for normal regression tests. Do not make CI depend on W34 branch availability.

## 10. W34 read-only regression

In addition to synthetic tests, use exact W34 SHA `7350dc3b6eeaa342c3d7d4292e4d386e701c7ba5` as a local/read-only reproducer.

Without modifying W34:

1. confirm current-main Core reproduces the exact failure;
2. run the candidate repaired Core against a temporary checkout/worktree containing the exact W34 artifacts;
3. verify the existing W34 Screening acceptance becomes valid for formal stage semantics;
4. verify the effective Discovery basis resolves to the 105-record file;
5. verify Evidence package preparation from the accepted Screening creates tasks from W34 non-DROP derived IDs, not the 40 root IDs;
6. do not actually advance or write W34 State during Core-maintenance regression.

Expected W34 Screening decisions are fixed:

- KEEP 45
- MAYBE 19
- INSPECT 16
- DROP 25

Therefore expected Evidence task count from the effective derived set is **80** (all non-DROP records), unless current Core semantics demonstrably specify a different count. If different, report before changing semantics.

## 11. Change scope

Modify only shared-Core code/tests/documentation needed for this generic capability.

Likely implementation files include:

- `scripts/survey_screening_v2.py`
- `scripts/survey_evidence_v2.py`
- `scripts/survey_stage_validation_v2.py`
- relevant `tests/*.py`

Modify `survey_agent_control_v2.py`, schemas, config, workflows, or other Core files only if the generic contract truly requires it. Explain every such expansion.

Do not change:

- Weekly-specific semantic policy;
- W34 edition files;
- W33 or any frozen release;
- publication/editorial content;
- unrelated Core behavior.

## 12. Test requirements

At minimum run:

- targeted Screening tests;
- targeted Evidence tests;
- targeted stage/agent-first tests;
- Materiality/Completeness/Selection/Architecture tests affected by Discovery basis propagation;
- full `pytest` or the repository's canonical full Python test suite if feasible;
- repository contract/CI-equivalent checks relevant to changed shared Core.

No test should be weakened merely to accommodate the change.

## 13. Maintenance branch discipline

Work only on the existing maintenance branch:

`fix/core-v2-screening-expansion-authority-20260904`

Do not create fallback/repair/review/iteration branches.

Do not merge to `main`.

Do not modify W34.

Normal commits to this maintenance branch are allowed.

No force/reset/rewrite/rebase.

## 14. Bounded stop

Stop at:

`CORE_REPAIR_CANDIDATE_READY_FOR_SOL_REVIEW`

only if all required synthetic tests and W34 read-only regression pass.

Do not merge to main and do not resume W34 production in this task.

If a stronger architectural blocker appears, stop at `NEEDS_SOL_REVIEW` with exact failure evidence rather than weakening provenance guarantees.

## 15. Completion report

Report exactly enough to independently review:

- branch;
- Exact Starting SHA;
- Ending SHA;
- ahead/behind/commit count;
- all changed paths;
- implementation summary;
- exact effective-basis invariants implemented;
- direct-basis backward compatibility result;
- synthetic expansion positive result;
- all fail-close negative test results;
- full test summary;
- W34 current-main reproduction result;
- W34 repaired-Core read-only result;
- W34 resolved effective Discovery path/hash/count;
- W34 expected/actual Evidence task count;
- confirmation W34 was not modified;
- confirmation main was not modified/merged;
- remaining risks or unresolved semantics;
- final disposition: `CORE_REPAIR_CANDIDATE_READY_FOR_SOL_REVIEW` or `NEEDS_SOL_REVIEW`.
