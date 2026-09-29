# Survey Production session — w39-publication-preview-r1-request-changes-r2-20260928-r1

Issue: `2026-W39`
Started: `2026-09-28T13:53:00Z` (remote preflight guards PASS; local fast-forwarded to remote `9890805808f422619315166b72598def49bba57b`)

## Starting authority

- Branch: `weekly/2026-W39-v2-work`; Exact Starting Remote SHA `9890805808f422619315166b72598def49bba57b` / tree `f1ba4166cb0c2c62540a7ace5f6f01f8aaab5223` (ls-remote verified pre-write; supplement `7b844cadf` and r1 reviewed `bb6eacab` in lineage; main/production unmodified)
- Reviewed remote `main`: `519aed90607f6e787bb3a7c00b651777835fd657` / tree `3a59771e7e5622c4d3c4bebad55fec52b42151c4`
- Production Line: `774dd39a951c9ac3818e83dfffd4c7666efb0a20` / tree `cd46a6f7a6dcc4031e76220cea4c52c7dd1fc481`
- Execution contract: `execution/requests/sol-w39-publication-preview-r1-request-changes-issue501-full-corpus-and-pdf-binding-20260928.md`
- Human decision in contract: Publication Preview r1 `REQUEST_CHANGES`, boundary `DRAFT_COMPLETE` (RC-1 full-corpus terminology + RC-2 PDF byte binding)
- Lifecycle at start: `RELEASE_CANDIDATE`; pub gate `pending`; upstream counts verified
- No Drive access; no connector searched/installed. No merge commit; no reset/rebase/force/squash.

## Actions actually performed

- Recorded Human Publication Preview r1 REQUEST_CHANGES via canonical `request-publication-preview-revision` (rev 1, boundary DRAFT_COMPLETE, reviewed `bb6eacab`, full RC text in requested_changes); publication-local invalidation only (DRAFT_COMPLETE/VALIDATED_DRAFT checkpoints removed; Architecture approval preserved); state returned to DRAFT_COMPLETE.
- RC-1: enumerated combined corpus (BASE 178 + SUPPLEMENT 177 = 352 forms, atomized from every observed cell); searched all reader surfaces pre-repair (r1 bytes) and post-repair; 649 occurrences adjudicated (REPLACE 335 / RETAIN 314); 171 forms ZERO_HIT_CHECKED; occurrence ledger + human companion written.
- Repaired TeX sections/main/cover (wording-only; facts/numbers/dates/attribution/caveats/citations/structure unchanged); no auto-replacement (every hit read in context; source read-back where identity was ambiguous).
- Seed-external residual scan over rewritten TeX: repaired additional literary metaphors (切れ味, 頂点, 対話欄, 書き残した, 身につけさせた, 補いの学び, 射程, 速さ比べ, 書きぶり, 建て付け, 作り比べ, 出し先, 解きほぐし, 加入見立て); reviewed-and-retained ordinary words logged; no new generic defect requiring supplement addition (residual count 0).
- Draft/synthesis bytes frozen under sealed ARCHITECTURE_ESTABLISHED checkpoint + Core overwrite refusal (documented per occurrence in ledger); repair applied at TeX/manuscript layer per DRAFT_COMPLETE boundary.
- RC-2: rebuilt via CI (run 36434164543, artifact 10975205959); independently downloaded artifact and hashed all four surfaces: repo PDF == sidecar == artifact PDF == artifact sidecar == bffda201 (328743 bytes, 12 pages). IDENTITY PASS. Adjacent-run byte variance documented (7700ad9b vs 4e6bf513) to justify same-run-only provenance.
- Regenerated manuscript (31/31 coverage) + deterministic QA + bundle + surface input (corrected blocks) + Worker surface-semantic PASS + lexical gate PASSED 0/0 + Worker semantic-editorial 11/11 + Worker visual 2/2 (PDF-extraction re-check on exact r2 bytes) + fresh candidate READY_FOR_PUBLICATION_PREVIEW.
- Validated + advanced DRAFT_COMPLETE → VALIDATED_DRAFT → RELEASE_CANDIDATE (HUMAN_GATE_REACHED, next PUBLICATION_PREVIEW).
- Fresh Publication Preview r2 shell + 14-section dossier; PENDING; no decision recorded or inferred. No Freeze/Release.

## External handoff

- None. Repository-local execution per contract.

## Deterministic execution transport

- Direct exact local CLI throughout (no operator bridge). Normal commits + non-force pushes + remote read-backs; prior-SHA verified before each write group.

## Deviations / failures

- No Core defect; no upstream invalidation event; no build failure in r2 cycle; shared-Core changed paths = 0.

## End state

- Lifecycle: `RELEASE_CANDIDATE`
- Terminal reason: `HUMAN_GATE_REACHED`
- Next action: `PUBLICATION_PREVIEW` (Human decision only)
- Review target: r2 Candidate + Candidate-bound PDF at reviewed commit `d95a811abd014ad4476d8f305b792920aa6e87fe` in `publication-preview-r2.md`
- Session status: `COMPLETE_AT_GATE`
