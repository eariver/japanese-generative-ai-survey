# Core v2 maintenance instruction — active Screening acceptance authority

Status: **LUNA EXECUTION AUTHORITY**

## 1. Repository / branch guard

Repository:
`eariver/japanese-generative-ai-survey`

Branch:
`fix/core-v2-screening-expansion-authority-20260904`

This task continues the existing Core maintenance branch. Do not create another branch.

At task start, verify the remote branch HEAD exactly matches the SHA supplied by Sol in the execution prompt. If it does not match, perform no writes and stop with the actual remote HEAD.

## 2. Mandatory authority

Read in this order:

1. `AGENTS.md`
2. `docs/survey-production-core-v2-session-bootstrap.md`
3. `docs/checkpoints/2026-09-04-core-v2-screening-expansion-authority-repair-instruction.md`
4. `docs/checkpoints/2026-09-04-core-v2-screening-expansion-authority-repair-validation-r2.md`
5. `docs/checkpoints/2026-09-04-core-v2-screening-active-acceptance-sol-review.md`

The Sol review is the controlling delta for this iteration. Do not weaken the strict root-closure repair already present.

## 3. Problem to solve

Core now correctly rejects a derived Screening Discovery set that silently omits accepted root Discovery records.

W34 proves a second generic recovery requirement: content-addressed Screening acceptances may legitimately have more than one immutable historical run before one run is successfully adopted by the Screening Stage Checkpoint.

Current interactive downstream helpers still discover Screening authority by scanning `screening/v2/accepted/*/screening-accepted.json` and requiring exactly one run. This makes immutable retry/recovery impossible without deleting prior evidence.

Core needs an explicit **active Screening acceptance authority** selected by the successful Screening Stage Checkpoint, not by accepted-directory cardinality or a latest-file heuristic.

## 4. Required semantic model

Preserve these distinct concepts:

1. historical immutable Screening acceptance run
   - content-addressed accepted run on disk;
   - may be valid under the Core version that created it but may later be rejected by stronger authority validation;
   - never selected merely because it exists.

2. proposed current Screening acceptance
   - explicit acceptance artifact supplied to current-stage validation while State is `DISCOVERY_COLLECTED`;
   - not yet active until the Stage Checkpoint adopts it.

3. active Screening acceptance
   - after successful `DISCOVERY_COLLECTED -> CANDIDATES_NORMALIZED` advancement;
   - the exact `screening-acceptance` artifact recorded in the passed `screening` Stage Checkpoint;
   - the only Screening acceptance downstream interactive helpers may treat as active authority.

Never select by mtime, lexicographic digest, directory order, or "latest" heuristic.

## 5. Implement reusable checkpoint-artifact resolution

Implement a generic, fail-closed resolver for an artifact carried by a passed Stage Checkpoint, or an equivalent reusable API.

Preferred location is `scripts/survey_agent_control_v2.py` if that avoids duplication, but exact API naming is your choice.

Given:

- repository root;
- current validated Production State;
- checkpoint name, e.g. `screening`;
- artifact name, e.g. `screening-acceptance`;

it must:

1. require the machine checkpoint to be `passed`;
2. require exactly one checkpoint provenance authority for that checkpoint;
3. validate the checkpoint authority path/hash and Stage Checkpoint schema/issue identity;
4. require exactly one artifact row with the requested artifact name;
5. verify that artifact's repository path is regular/non-symlink and exact SHA matches;
6. return the exact artifact path/authority;
7. fail closed on missing, duplicate, drifted, or malformed authority.

Reuse existing agent checkpoint validation primitives rather than inventing parallel semantics where possible.

Do not alter lifecycle history or checkpoint semantics.

## 6. Implement active Screening acceptance resolution

Implement a reusable Screening-level resolver, e.g. `resolve_active_screening_acceptance(...)`.

When called for downstream work after Screening advancement it must:

1. use the passed `screening` Stage Checkpoint authority;
2. resolve exactly one `screening-acceptance` artifact from that checkpoint;
3. run current `survey_screening_v2.validate_acceptance()` against that exact path;
4. return that path/payload as active authority;
5. never scan all accepted runs to choose one.

If State says Screening is passed but checkpoint authority is absent or invalid, fail closed.

Do not add a fallback that chooses the sole directory entry. Existing direct callers that explicitly pass a Screening acceptance path remain supported separately.

## 7. Replace ambiguous directory discovery

Audit shared Core for accepted-Screening directory scans.

At minimum update:

- `scripts/run_evidence_v2_interactive.py`
- `scripts/run_selection_architecture_v2_interactive.py`

so that, once lifecycle semantics require an already-adopted Screening authority, they use the active Stage-Checkpoint resolver rather than `glob(...accepted...)` cardinality.

Audit all `scripts/` callers for equivalent scans and repair any other active-authority ambiguity found.

Do not change editorial semantics or Evidence/Selection contracts beyond authority selection.

Existing stage validators/handoffs may continue to validate an explicitly bound proposed acceptance during `DISCOVERY_COLLECTED`, because that path becomes active only if the generated Stage Checkpoint adopts the exact same artifact.

## 8. Preserve strict derived Discovery authority

The previous repair remains mandatory:

- accepted root closure must be complete;
- arbitrary unrelated Discovery substitution must fail;
- parent refs must resolve to accepted root IDs;
- Raw paths and stable source identity must be rooted in declared parents;
- obligation invention remains forbidden;
- direct basis remains backward compatible;
- Evidence uses effective derived IDs.

Do not relax any of these invariants to make W34 pass.

## 9. Synthetic multiple-run regressions

Add tests covering at least:

1. two immutable Screening acceptance run directories may coexist;
2. explicit current-stage validation can validate a proposed corrected run without deleting the historical run;
3. after a simulated passed Screening Stage Checkpoint, active resolver returns the checkpoint-bound corrected run;
4. the historical run is not selected merely because it also exists;
5. reversing directory creation/order does not change active selection;
6. missing `screening` checkpoint fails closed;
7. checkpoint status not passed fails closed;
8. zero `screening-acceptance` artifact rows fails closed;
9. duplicate `screening-acceptance` rows fail closed;
10. checkpoint artifact path/hash drift fails closed;
11. direct explicit acceptance validation remains backward compatible;
12. existing agent-first State validation remains green.

Prefer a dedicated test file if that keeps concerns clear.

## 10. W34 exact read-only regression

W34 authority is read-only:

Branch:
`weekly/2026-W34-v2-work`

Exact SHA:
`7350dc3b6eeaa342c3d7d4292e4d386e701c7ba5`

Do not write W34.

Use the exact fixture to construct a temporary corrected Screening recovery only.

### 10.1 Existing immutable facts

Preserve exactly:

- accepted root Discovery count: 40;
- existing event-derived count: 105;
- `W34-C001`–`W34-C105`: 105/105;
- existing event decisions: KEEP 45 / MAYBE 19 / INSPECT 16 / DROP 25;
- historical accepted run digest: `2ab82c6b52b26fc01cc6a82d20da08ef4b37dadaf2ff1b0e5a570f50652b3662`.

### 10.2 Five missing coverage roots

Add five temporary coverage passthrough derived records, one for each missing accepted root:

- `w34-github-releases-comfy-org-comfyui`
- `w34-github-releases-ggml-org-llama-cpp`
- `w34-github-releases-nvidia-tensorrt-llm`
- `w34-github-releases-sgl-project-sglang`
- `w34-github-releases-vllm-project-vllm`

Use deterministic temporary derived IDs. Suggested IDs:

- `w34-coverage-comfy-org-comfyui`
- `w34-coverage-ggml-org-llama-cpp`
- `w34-coverage-nvidia-tensorrt-llm`
- `w34-coverage-sgl-project-sglang`
- `w34-coverage-vllm-project-vllm`

Each coverage child must:

- use a parent-requiring expansion origin already allowed by the Discovery contract;
- parent exactly the corresponding accepted root;
- preserve that parent's stable source identity tuple;
- use only that parent's existing Raw paths;
- invent no obligations;
- clearly state that it is a collector coverage passthrough, not a new Weekly event.

Corrected temporary derived count must be **110** and strict root accounting must be **40/40**.

### 10.3 Five coverage decisions

Retain the existing 105 Screening decisions semantically unchanged.

Add five decisions:

- decision: `DROP`;
- reason: coverage-only GitHub Releases root with no separately qualifying W34 event represented by this root;
- confidence: high;
- duplicate_group: null;
- scope_tags may include `coverage-only` and `github-releases`;
- verification_targets may be empty unless the schema requires otherwise.

Corrected totals:

- KEEP 45
- MAYBE 19
- INSPECT 16
- DROP 30
- TOTAL 110

Non-DROP Evidence tasks must remain **80**.

### 10.4 Temporary corrected acceptance + active selection

In a temporary regression environment containing current maintenance Core plus exact W34 source artifacts:

1. retain the historical 105-run acceptance directory;
2. prepare/accept the corrected 110-record Screening run as a second immutable content-addressed run;
3. validate corrected strict expansion 40/40;
4. simulate a Screening Stage Checkpoint whose `screening-acceptance` artifact binds the corrected run;
5. simulate post-advance State/checkpoint provenance sufficiently to exercise the active resolver without mutating W34;
6. prove active resolver selects the corrected run while historical run remains present;
7. prepare Evidence against the active corrected run and verify exactly 80 tasks using derived IDs.

If archived W34 State/history defects prevent exact full State reuse, create a synthetic valid agent State/Stage Checkpoint fixture while retaining exact W34 Discovery/Screening bytes for the 40->110 and corrected-acceptance portions. Record that boundary explicitly. Do not weaken State validation.

## 11. Tests

Run at minimum:

- new active-authority tests;
- `tests/test_screening_expansion_authority_v2.py`;
- `tests/test_survey_screening_v2.py`;
- `tests/test_survey_screening_archive_v2.py`;
- `tests/test_accept_screening_results.py`;
- `tests/test_survey_agent_control_v2.py`;
- `tests/test_survey_agent_tool_v2.py`;
- `tests/test_survey_stage_validation_v2.py`;
- `tests/test_survey_evidence_v2.py`;
- `tests/test_run_evidence_v2_agent_first.py`;
- `tests/test_run_selection_architecture_v2_interactive.py`;
- affected completeness/selection/architecture tests;
- repository/schema syntax tests.

Run the full Python suite as a diagnostic and classify any pre-existing unrelated failures without modifying unrelated code.

## 12. Durable validation record

Create:

`docs/checkpoints/2026-09-04-core-v2-screening-active-acceptance-repair-validation-r3.md`

Record:

- exact Starting SHA;
- Ending SHA;
- changed paths;
- main comparison;
- test commands and pass/fail counts;
- strict expansion status;
- active-authority synthetic regressions;
- W34 temporary 40->110 result;
- historical run retained;
- active corrected run selected;
- corrected decision counts 45/19/16/30;
- Evidence task count 80;
- W34/main write status;
- remaining limitations.

## 13. Write boundary

Allowed changes are only shared-Core files necessary for this authority resolver, directly affected tests, and the validation record.

Expected candidate paths include, as needed:

- `scripts/survey_agent_control_v2.py`
- `scripts/survey_screening_v2.py`
- `scripts/run_evidence_v2_interactive.py`
- `scripts/run_selection_architecture_v2_interactive.py`
- directly affected tests
- `docs/checkpoints/2026-09-04-core-v2-screening-active-acceptance-repair-validation-r3.md`

Do not modify:

- W34;
- W33;
- `main`;
- unrelated Core/editorial/publication files;
- schemas unless an unavoidable generic contract gap is proven first and recorded for Sol review.

Do not force/reset/rewrite/rebase.

## 14. Stop condition

If all required authority and regressions pass, stop at:

`CORE_REPAIR_CANDIDATE_READY_FOR_SOL_REVIEW`

Do not merge main.

If a larger semantic conflict is discovered, preserve strict provenance guarantees and stop at:

`NEEDS_SOL_REVIEW`.
