# Main Structural-Recovery Reconciliation

Status: `CURRENT-FACING AUTHORITY RECONCILED / PRE-FREEZE / PRE-SEVEN-POINT-AUDIT`  
Date: 2026-09-06 JST  
Repository: `eariver/japanese-generative-ai-survey`  
Maintenance branch: `fix/core-v2-pre-human-evidence-regeneration-20260905`  
Candidate before reconciliation: `be9417967b3c5e58c92d406ce8e3c45232e4fc23`  
Target PR: `#484` — Survey Production Core v2: pre-Human Evidence regeneration repair

## Main authority distinction

The current production `main` HEAD is:

`d8fa79ef2affacec49a47e6fc88018fb99f36899`

The pre-incident reviewed semantic/tree baseline is:

`a9f121f0d65591f52b53515712d7c0bae573b2ef`

The expected exact tree for both commits is:

`b6c1b2cbc13165e64ac1d88d4d36b7515f7494da`

Read-only comparison confirmed:

- changed files: `0`;
- content delta: `0`;
- exact tree identity: PASS;
- `d8fa79ef...` is the structural-recovery descendant used as the current main authority.

The structural-recovery commits repair an accidental main-history incident. They do not introduce new Survey Production Core semantics. Current repository reality must name `d8fa79ef...` as current main; historical validation records that were correct at their time remain unchanged and may continue to name `a9f121f...` as the reviewed baseline.

## Candidate and PR boundary

PR `#484` remains the normal draft integration review surface:

- state: `open`;
- draft: `true`;
- merged: `false`;
- base ref: `main`;
- current base authority: `d8fa79ef2affacec49a47e6fc88018fb99f36899`;
- pre-incident reviewed baseline retained separately: `a9f121f0d65591f52b53515712d7c0bae573b2ef`.

The maintenance candidate remains pre-freeze and pre-seven-point-audit. No Human full-candidate approval and no merge authorization exists. The candidate tree must receive fresh validation after this authority-only mutation.

## Scope and non-actions

This reconciliation is an authority/documentation change only. Core implementation, schemas, lifecycle, Human Gate policy, Evidence Authority Supplement semantics, pending-Gate invalidation semantics, and W34 artifacts are unchanged.

Main writes: `0`  
W34 writes: `0`  
Human review records created: `0`  
Sidecar runs: `0`  
Force/reset/rewrite/rebase: unused

The exact W34 fixture remains `weekly/2026-W34-v2-work@df3d0dfe11a1cc99dd7698e1bc9b2a47e2dc3c0f`. Fresh W34 read-only regression, exact-head CI, and merge-candidate CI must be performed against the post-reconciliation candidate before any later review decision.
