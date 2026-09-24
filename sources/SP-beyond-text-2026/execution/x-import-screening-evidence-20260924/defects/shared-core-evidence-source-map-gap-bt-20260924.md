# TS-002 shared-Core defect — Evidence SOURCE_CLASS_MAP lacks BT Discovery vocabulary

Status: `OPEN_CORE / EDITION_WORKAROUND`

Date: `2026-09-24`

Issue: `SP-beyond-text-2026` / `#526`

Branch: `special/beyond-text-2026-work`

## Symptom

Canonical Evidence package preparation (`survey_evidence_v2.prepare_evidence_package`
via `task_authority_sources`) fails closed on 37 of 139 TS-002 Evidence tasks:

```text
ValueError: unsupported source_type for Evidence authority: 'PRIMARY_REPO'
```

## Scope

Accepted canonical Discovery (`discovery-v2.jsonl`, 139 records) uses seven
`source_type` values. Only two exist in
`scripts/survey_evidence_v2.py::SOURCE_CLASS_MAP`:

| Discovery `source_type` | n | MAP entry | Projected class |
|---|---|---|---|
| `PRIMARY_PAPER` | 101 | yes (`PRIMARY_PAPER`) | passthrough |
| `x-community-signal` | 1 | yes (`SOCIAL`) | passthrough |
| `PRIMARY_REPO` | 3 | no | `PRIMARY_REPOSITORY` |
| `PRIMARY_DOC` | 16 | no | `PRIMARY_OFFICIAL` |
| `PRIMARY_ANNOUNCEMENT` | 13 | no | `PRIMARY_OFFICIAL` |
| `PRIMARY_SPEC` | 2 | no | `PRIMARY_OFFICIAL` |
| `PRIMARY_MODEL_CARD` | 3 | no | `PRIMARY_OFFICIAL` |

Projected: 37. Passthrough: 102. Total: 139.

The Discovery schema (`schemas/survey-discovery-record.schema.json`) places no
closed vocabulary on `source_type`, so all seven values are schema-valid
accepted Discovery. The Evidence map is closed and has not kept up with the
Discovery vocabulary. Same defect family as TS-001 CV2-DM-016 (67/160 tasks;
`execution/defects/shared-core-evidence-source-map-gap-20260922.md`).

## Precedent analysis

TS-001's released Discovery uses the same vocabulary family (`PRIMARY_DOC`,
`PRIMARY_REPO`, `PRIMARY_ANNOUNCEMENT`, `PRIMARY_MODEL_CARD`, `PRIMARY_SPEC`
plus `SECONDARY_*`/`RUNTIME_*`/`PACKAGING_DOCS`). Its Evidence run failed
closed the same way and was completed through a reviewed
`KEEP_CORE_V2_FROZEN / USE_REPRODUCIBLE_EDITION_LOCAL_COMPATIBILITY` decision:
an edition-local adapter projecting ONLY `source_records[*].source_type` per a
reviewed map, with per-field identity assertion, unexpected-vocabulary
fail-close, frozen validation, and byte-identical reproducibility proof. Shared
Core was not modified.

## Bounded handling in this run

1. Shared Core untouched (no edits under `AGENTS.md` read-only roots).
2. Reproducible edition-local compatibility adapter under
   `sources/SP-beyond-text-2026/execution/x-import-screening-evidence-20260924/compat/`:
   frozen `prepare_evidence_package` over canonical bytes, projection of ONLY
   `source_records[*].source_type` per the table above, recomputed task SHAs,
   frozen `validate_evidence_package_basis` PASS, two clean-temp builds
   byte-identical.
3. Evidence Cards/Views built against the compat package with the canonical
   card/view validators; evidence + views acceptance via the canonical
   append-only acceptors. Materiality Ledger, Profile Completeness, and any
   Production State advance are NOT performed (stop boundary).
4. This compat-derived Evidence is `EVIDENCE_BUILT` awaiting the fresh Sol
   Evidence Semantic Review, which also judges the compat validity.

## Resume criteria

Reviewed Core repair adding the five BT Discovery `source_type` values (or
their canonical equivalents) to `SOURCE_CLASS_MAP` (or a reviewed vocabulary
registry) → rerun the preserved
`evidence-interactive-input.json` cleanly without compat → clean validators
PASS → only then advance toward `EVIDENCE_REVIEWED`. Nothing from the compat
run may be carried forward as clean-Core evidence after repair except as
historical provenance.

Shared-Core repair itself is out of scope for this edition run.
