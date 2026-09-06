# Survey Production Core v2 — Pre-Freeze Crosscheck Repair Validation r4

Status: READY_FOR_FRESH_SOL_PREFREEZE_CROSSCHECK  
Validated: 2026-09-06 JST  
Repository: eariver/japanese-generative-ai-survey  
Maintenance branch: fix/core-v2-pre-human-evidence-regeneration-20260905  
Target PR: #484 — Survey Production Core v2: pre-Human Evidence regeneration repair (draft / open / unmerged)  
Starting branch SHA: 580286b122877d0fa121ad64d7a94ee73a0d8cff  
Reviewed main SHA: a9f121f0d65591f52b53515712d7c0bae573b2ef

## Scope

This r4 candidate contains only the bounded Sol pre-freeze repair:

1. historical Core-config binding for immutable operator invalidation records; and
2. current-facing authority synchronization for PR #484.

No W34 production artifact, main branch, Human review, sidecar, publication, freeze, release, or merge operation is part of this candidate.

## Historical config authority

The immutable operator invalidation-record validator now loads the exact config/survey-production-v2.json bytes from invalidated_repository_commit_sha through the existing committed-file machinery. It derives current pending-Gate identity from that historical config's orchestration.gate_at_state, lifecycle, pending status, null provenance, and HUMAN_GATE_REACHED.

The live invalidation operation continues to use the admitted current Core config. Thus live execution and immutable historical validation do not silently mix config authorities.

The regression suite proves both directions:

- current worktree config drift does not change validation of a record whose invalidated commit is unchanged; and
- a record rewritten to a commit whose committed config maps ARCHITECTURE_ESTABLISHED to PUBLICATION_PREVIEW fails closed.

The existing eventual-target semantics remain covered: an edition with target_gate=PUBLICATION_PREVIEW can invalidate its pending Architecture Review to CANDIDATES_NORMALIZED; the target remains PUBLICATION_PREVIEW, the operator record gate is ARCHITECTURE_REVIEW, and no Human record is created.

## Authority documentation synchronization

The current-facing authority and worklog now identify PR #484 as the normal draft integration review surface. They explicitly retain:

- draft/open/unmerged status;
- no implication of Human approval, 7/7 PASS, freeze, or merge authorization; and
- the fact that this task does not merge the branch.

Historical narrative is unchanged.

## Fresh exact W34 read-only regression

Fixture: weekly/2026-W34-v2-work@df3d0dfe11a1cc99dd7698e1bc9b2a47e2dc3c0f.

The disposable detached fixture began at the exact W34 SHA with lifecycle ARCHITECTURE_ESTABLISHED, pending Architecture Review, null Architecture provenance, terminal reason HUMAN_GATE_REACHED, Human review records 0, and its existing W34 target gate.

The replacement candidate then executed:

- operator invalidation ARCHITECTURE_REVIEW -> CANDIDATES_NORMALIZED;
- existing W34 Evidence Authority Supplement and captured authority bodies;
- new Evidence and Edition View acceptance;
- Evidence, Materiality, Completeness, Selection, and Architecture stage validation;
- checkpoint-bound active Evidence/View resolution.

Observed immutable accepted directories coexisted:

- historical Evidence: 917f6b5d...;
- new Evidence: bcf91f31d81935e0a48c1fde55f9d6db2192776b0d15a8cc11acfcc1ff9ee561;
- historical Edition View: 9545fae...;
- new Edition View: 43724d2264da8dff4892f7114c06d57060919d9b43f5248a7a0866b7b99ea102.

The active resolver selected only the new checkpoint-bound Evidence/View artifacts. Evidence contained 80 tasks; Completeness remained LIMITED; the mechanism fixture produced one selected candidate and one Architecture package. That selection count is recorded only as a mechanism regression result, not as a semantic success criterion for production W34.

Final disposable-fixture state: ARCHITECTURE_ESTABLISHED, Architecture Review pending, Publication Preview pending, null Human provenance, terminal reason HUMAN_GATE_REACHED, Human review records 0.

Remote W34 HEAD remained exactly df3d0dfe11a1cc99dd7698e1bc9b2a47e2dc3c0f; no W34 branch or canonical artifact write occurred.

## Validation results

- focused operator invalidation, Human Gate, agent-control, stage-validation, Evidence, interactive Evidence, and Selection/Architecture tests: 57 passed;
- full operator invalidation suite: 24 passed;
- local full Python diagnostic: 773 tests, 2 failures, 3 errors, 6 skipped; the failures/errors were outside this bounded repair and came from absent W32/release/Special fixtures plus an existing incomplete-checkout operator CLI contract mismatch; the fresh repository CI above passed;
- syntax/compile validation: PASS; git diff --check: PASS;
- workflow count: exactly 7;
- main remote remained a9f121f0d65591f52b53515712d7c0bae573b2ef;
- fresh CI for candidate 7be85c2041f6481252f244e520d9255991b6e43c: PASS — Survey Production Core v2 CI run 34020270531; Pipeline contract tests run 34020270540.

## Non-actions and remaining limits

Human review records created: 0.  
Human decision: none.  
W34 canonical writes: 0.  
Main writes: 0.  
Sidecar runs: 0.  
Force push/reset/rewrite/rebase: unused.  
Publication Boundary Validator and Authority Auditor remain deferred.

This document is a validation record for a pre-freeze Sol-review candidate. It does not assert frozen status, seven-point audit completion, Human approval, or merge authorization.
