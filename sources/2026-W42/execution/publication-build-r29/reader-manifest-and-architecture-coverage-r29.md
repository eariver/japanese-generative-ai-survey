# W42 r29 Reader manifest and Architecture coverage

Status: deterministic build evidence (PROPOSED, not a Human/independent PASS)
Date: 2026-10-20 JST
Manifest: `sources/2026-W42/publication/v2/reader-manuscript-v2.json`
Manifest content digest: `78d9928ded5ec663c7f25a028135fa05cf5411a2ecc0a0c1bb407eb9f02708e0`
Manifest file SHA256: `47634ae3ac347dd9529e796e01ed3661defa89e5f31b164dfe9752155b23c76f` (15908 bytes)

## 1. Builder

Frozen Core official builder `survey_reader_publication_v2.build_manuscript_manifest` + `validate_manuscript_manifest` + schema `reader-manuscript-v2.schema.json`. No hand-fabricated digest; `manifest_sha256` computed by builder.

- `status`: `READER_FACING_AUTHORED` (authored, not Human/Publication approved)
- `research_profile`: WEEKLY, `publication_profile`: WEEKLY_MAGAZINE
- `production_profile`: `sources/2026-W42/production-profile.json`
- `architecture`: `sources/2026-W42/architecture-v2.json` (r1 approved)
- `architecture_approval`: `sources/2026-W42/gates/architecture-approval.json` (APPROVED 2026-10-17)
- `primary_source`: `surveys/weekly/2026-W42/main.tex` (96790 bytes, SHA256 `2ed5848aeaedccdadd80c14f23967ee4017f562fd7409eda412439cb3281ecd3`)
- `supporting_files` (4, genuine roles/paths/sizes):
  - STYLE `surveys/weekly/2026-W42/preview.sty` (6132 bytes, `f0492fb6...`)
  - SUPPORTING_SOURCE r18 Reader JSON (blob `fc4fd9f2...`)
  - SUPPORTING_SOURCE bibliography-map-r18.json (90 keys)
  - SUPPORTING_SOURCE citation-repair-ledger-r18.json (177 rows)
- `authored_by`: `Muse Spark (W42 r29 canonical build, READER_FACING_AUTHORED, not Human approved)`

Validation: `validate_manuscript_manifest` PASS (schema + content digest + profile/architecture identity + coverage completeness + reader-requirement set + surface gate on primary/supporting/details).

## 2. Architecture coverage (27/27, all FULFILLED author assertions)

Packages P1–P7 with must_cover counts 4/4/4/4/4/4/3. Each row maps to genuine `Section N — <title>` reader location; detail is author accountability prose (not machine proof of substantive adequacy).

- P1 (Section 1): Wonder/Focus definitions vs Argon anecdotes; eval/pricing with pending reports; Copilot as distribution; Minecraft limits
- P2 (Section 2): Maia mechanisms; vendor-only deltas; LFM non-comparability; $10M cap + weight-file gap
- P3 (Section 3): one-table architecture comparison; operative license quotes + tag-only marking; Nemotron disclosure; OSS/weights/OSI separation
- P4 (Section 4): Codex boundary + cost table; Scion placement; HydraFusion vs autofix vs AI Scan; Decider chain vs W41 v1.1
- P5 (Section 5): four action categories + Oct 12 fix; distillation vendor-measured; ECDSA method; METR mechanism-only
- P6 (Section 6): wet-lab denominators + MSA caveat; Earth AI design + cost-with-failures; Deep Review method + June background; Rosalind access-only
- P7 (Section 7): GLM-Legal Vals anchor + caveats; ASPIRE Oct vs June + frozen-LLM limit; Glimpse HSS shortfall + non-open boundary

No invented evidence; counts are traceability, not semantic validation. Substantive adequacy remains for independent semantic review.

## 3. Reader requirements (2/2)

- `FINAL_SYNTHESIS` → Section 7 concluding synthesis (“三件の共通点は「使える条件」の記事…”)
- `WEEKLY_COMMUNITY_MOVEMENT` → Sections 1/2/3 X-post locations; posts treated as announcement-existence evidence, not measurement (consistent with TeX discipline)

Details avoid prohibited internal vocabulary/paths; scanned by surface gate as part of manifest validation (no BLOCKING findings).
