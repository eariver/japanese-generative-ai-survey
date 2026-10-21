# r8 frozen-Core validation report (2026-10-17; all calls unmodified frozen APIs)

Runner: edition-local `execution/compat/evidence-source-class-projection/` (builder + interactive input + chain driver). Override used: ONLY frozen `survey_agent_tool_v2.current_stage_basis_override()` (restores on exit; verified by re-import check).

## Passes (compat path)
- X manifest validate (COMPLETE) + discovery `build_acceptance` equivalent re-validated intact (50 records, graph 5818d9d2).
- Supplement manifest: 91 entries validate (frozen schema + raw sha/bytes + basis SHAs).
- Compat package: 50 tasks (17 projected SOCIAL/SECONDARY + 33 passthrough; invariant ONLY-source_type-differs enforced per task; ledger with original/projected SHAs).
- Compat basis validate (override): PASS. `task_authority_sources` resolvable for all 50 tasks.
- Interactive input: 50 records validate (status 43 PARTIAL/7 NEEDS_MORE; materiality 28/14/7/1; completeness 3 obligations + residual + null closure).
- 50 Core cards built + `validate_evidence_card` PASS each; acceptance `f2429e27…` (50 results) + revalidate PASS.
- 50 Core views built + validated; views acceptance `4296ffd0…` PASS.
- Materiality ledger written + validated; profile-completeness LIMITED validated (obligations 2 SATISFIED/1 LIMITATION).
- Agent-state clean BEFORE and AFTER (N1/N6). Source/checkpoint SHAs confirmed current (acceptance files re-read by hash at each step).

## Fails-closed (default path, distinctly logged)
- N2 default-path `prepare_evidence_package` (no override): `ValueError: implementation commit differs from authoritative state` (r7 run at older HEAD failed later at checkpoint/history semantics — same fail-closed family, HEAD-dependent message).
- N3 tampered State copy (temp, isolated): rejected with errors.
- N4 wrong implementation SHA into override: refused (must equal current work-branch HEAD).
- N5 unknown source_type: `unsupported source_type for Evidence authority` (projection allowlist enforced; 17 mapped, all else fail).

## Command log
- `python3 .../build_compat_evidence_package.py` → package 4b34578f (50/17/33).
- `python3 .../run_frozen_evidence_chain.py` → evidence f2429e27 (50), views 4296ffd0, ledger, completeness LIMITED.
- Bridge ADVANCE requests (separate commits): discovery (31c9a9a9, r5), screening (9c4da532, r5), evidence (this unit, next).
