# Shared-Core defect record — Evidence source-class map gap (edition-found)

Execution agent: Muse Spark 1.3
Execution mode: EXPERIMENTAL_LUNA_ROLE_SUBSTITUTION
Date: 2026-09-09 UTC
Status: `RECORDED / MINIMAL_REPAIR_APPLIED / SOL_RULING_REQUIRED`

## Defect

`scripts/survey_evidence_v2.py::SOURCE_CLASS_MAP` does not cover Discovery
`source_type` values introduced by edition-local (Luna) Discovery
materialization and accepted into canonical W34 Discovery:

- `arxiv_atom_snapshot` (319 fresh tasks)
- `official_web_fallback_observation` (3 tasks)
- `official_research_index_snapshot` (4 tasks)
- `official_release_notes_snapshot` (1 task)
- `official_rss_index_snapshot` (2 tasks)

`task_authority_sources()` raises `unsupported source_type for Evidence
authority` (fail-closed, per commit `5b1f72c7`), so `run_evidence_v2_interactive`
cannot build any Evidence package touching the 329 fresh tasks. The map predates
the fresh Discovery collectors; the new types come from edition-local scripts
(`w34-discovery-gapfill-after-sol-review-r1/materialize_discovery_gapfill.py`,
`w34-architecture-r2-research-sufficiency-revision-r1/materialize_fresh_discovery.py`),
not from shared Core. This is a seam defect, found by a formal
production-validation run (fresh Evidence after Sol Discovery Review r2).

## Why not worked around in-edition

The Core expansion contract requires each derived Screening record's source
identity to equal one accepted parent's identity exactly. Re-pointing the 329
fresh children at old mapped parent identities would fabricate provenance
(all 311 arXiv papers sharing the Sol baseline locator) and break the
Sol-reviewed 434-identity reconciliation. That would be bypassing
task/source-binding rules, explicitly forbidden by the execution request.
No edition-local path preserves both validation and provenance honesty.

## Minimal repair applied (separate commit, Sol must rule)

Five additive mappings in `SOURCE_CLASS_MAP`, mirroring existing siblings,
fail-closed behavior preserved for all other unknown types:

- `arxiv_atom_snapshot` -> `PRIMARY_PAPER` (cf. `arxiv_primary`, `paper`)
- `official_web_fallback_observation` -> `PRIMARY_OFFICIAL` (cf. `official_publisher_page`)
- `official_release_notes_snapshot` -> `PRIMARY_OFFICIAL`
- `official_rss_index_snapshot` -> `PRIMARY_OFFICIAL`
- `official_research_index_snapshot` -> `PRIMARY_OFFICIAL`

No validator, schema, lifecycle, or workflow logic touched. No existing
mapping altered. No behavior change for any previously accepted run
(the five types never previously reached Evidence).

## Required Sol ruling (before Selection/Architecture may trust this Evidence)

1. ACCEPT the repair as correct shared-Core maintenance (to be integrated via
   the normal Core process later), or
2. REVERT it and order a separately-branched/reviewed Core repair, in which
   case this Evidence run is failed evidence and must be rerun cleanly, or
3. SUBSTITUTE an alternative repair with instructions.

Evidence below was produced by rerunning the clean Core path with the repair
in place. The repair commit is isolated from all edition/Evidence commits so
Sol can revert it without touching edition bytes.
