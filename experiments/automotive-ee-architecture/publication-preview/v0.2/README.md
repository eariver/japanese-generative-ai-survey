# Automotive E/E Publication Preview v0.2 source bundle

This bundle is the revised experiment-only Publication Preview source for `SP-automotive-ee-architecture-2023-2026`.

It incorporates self-review and prior AI-survey review Issue lessons: reader-facing/provenance separation, section-level TOC, mixed layout, compact bibliography presentation, supplemental AUTOSAR/OEM/Tier1 official-source coverage, semantic claim-boundary tightening, deterministic architecture diagrams, and typed reproducibility metadata.

P08 remains the final body synthesis immediately before References.

The review artifact bundle is **repository-bound plus supplemental-source-audited**: it contains the exact structured P01-P08 snapshots and validation reports used for review, while post-Architecture coverage gap-fill is recorded separately in `supplemental-source-audit-v0.2.json`. The Git branch mirrors the publication source and audit/control files, but intentionally does not commit the binary PDF or redundant exact structured-draft/validation snapshots; those are artifact members whose typed hashes are recorded in `preview-manifest.json` and `source-files-sha256.txt`. Existing repository Draft Packages, the historical draft payload, and the Automotive drafting prompt remain the authoritative repository-side dependencies.

No production AI pipeline file is modified.

## Deterministic build

The preview PDF is built with a fixed source epoch so repeated clean builds are byte-identical:

```sh
export SOURCE_DATE_EPOCH=1787053800
export FORCE_SOURCE_DATE=1
lualatex -interaction=nonstopmode -halt-on-error main.tex
biber main
lualatex -interaction=nonstopmode -halt-on-error main.tex
lualatex -interaction=nonstopmode -halt-on-error main.tex
```

`SOURCE_DATE_EPOCH=1787053800` corresponds to the editorial cutoff instant `2026-08-18T11:50:00Z`. Two independent clean builds produced the same PDF SHA-256.
