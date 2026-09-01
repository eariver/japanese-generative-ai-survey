# SP001 shared-Core defect — cross-package synthesis Draft input

Date: 2026-08-25 JST  
Edition: `SP001`  
Classification: `SHARED_CORE_DEFECT`  
Production status: `PAUSED_AFTER_ARCHITECTURE_APPROVAL`

## Symptom

The Human-approved SP001 Architecture contains a final synthesis package with no direct `primary_candidate_ids` or `supporting_candidate_ids`. This is valid under the Architecture contract because the package synthesizes Evidence already assigned to the preceding packages rather than creating another candidate destination.

The pre-repair Draft builder nevertheless rejects every package with no direct placements using:

`Architecture package has no factual Evidence inputs`

Therefore the Architecture contract and Drafting contract disagree for a legitimate cross-package synthesis/conclusion package.

## Production evidence

- Canonical lifecycle: `ARCHITECTURE_ESTABLISHED`
- Architecture Review: `approved`
- Exact Human-reviewed Architecture commit: `3be63ff5a79a274b1d99f061c1ef8cf80c803d62`
- Architecture approval bridge request: `postintegration-sp001-architecture-approval-r2`
- Approval receipt State SHA-256: `8d83099133289450c644624da310f2492d10484794ad6089cbbd85659274e653`
- Next canonical action remains `stage:drafting-synthesis`; it is intentionally not executed against the defective shared Core.

No failed Draft stage is salvaged as successful evidence.

## Generic repair

Shared Core maintenance PR #465 (`Core v2: support bounded cross-package synthesis Draft references`) repairs the mismatch generically:

- ordinary evidence-owning packages retain the previous Drafting path;
- exactly one empty-placement package may act as cross-package synthesis only when it is last in drafting order;
- its Draft Evidence inputs are de-duplicated references to candidates already placed by the other Architecture packages;
- those references are Draft-time `SUPPORTING` inputs only and do not create additional Architecture destinations;
- multiple empty packages, a non-final empty package, or synthesis without prior factual placements fail closed.

No SP001/topic-specific Core adapter is introduced.

## Resume condition

Production remains paused until PR #465 has:

1. fixed-head Core and Pipeline CI success;
2. fresh seven-point Core audit success;
3. explicit Human approval of that exact repair head;
4. unchanged merge to reviewed `main`;
5. synchronization of that reviewed Core into `special/SP001-v2-work`.

After synchronization, materialize fresh Draft Package/Result and Synthesis artifacts and validate the `ARCHITECTURE_ESTABLISHED -> DRAFT_COMPLETE` transition cleanly under the reviewed Core. The existing Architecture approval remains historical/current authority unless a later exact-byte validation demonstrates otherwise.
