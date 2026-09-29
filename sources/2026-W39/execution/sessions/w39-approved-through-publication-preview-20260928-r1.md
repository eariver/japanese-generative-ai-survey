# Survey Production session — w39-approved-through-publication-preview-20260928-r1

Issue: `2026-W39`
Started: `2026-09-28T00:24:00Z` (remote preflight guards PASS; local fast-forwarded to remote `5b95eb36371cb722616e67f99720864c78ddf37d`)

## Starting authority

- Branch: `weekly/2026-W39-v2-work`; Exact Starting Remote SHA `5b95eb36371cb722616e67f99720864c78ddf37d` / tree `8fe440344e5435f5cd8bfd981c295f537398350f` (ls-remote verified pre-write; parent `ddb2244c4`/tree `a47fdf73` verified)
- Reviewed remote `main`: `519aed90607f6e787bb3a7c00b651777835fd657` / tree `3a59771e7e5622c4d3c4bebad55fec52b42151c4`
- Production Line: `774dd39a951c9ac3818e83dfffd4c7666efb0a20` / tree `cd46a6f7a6dcc4031e76220cea4c52c7dd1fc481`
- Execution contract: `execution/requests/sol-w39-architecture-r1-approved-through-publication-preview-20260928.md`
- Human decision in contract: Architecture r1 `APPROVED` against reviewed `9767d68e0d83aa667eaeeee6394806c612708682`
- Lifecycle at start: `ARCHITECTURE_ESTABLISHED`; arch gate `pending`; upstream counts verified (15 / 15-0 / 8-7 / 12-3 / 13-2 / 7 packages)
- No Drive access; no connector searched/installed. No merge commit; no reset/rebase/force/squash.

## Actions actually performed

- Recorded Human Architecture r1 APPROVED via canonical `survey_human_gate_v2.py record-architecture-approval` (rev 1, reviewed_by Human Owner, reviewed_at actual wall clock, reviewed commit `9767d68e...` reachability + exact-byte verification PASS); approval + r1 record + snapshot + review index verified by read-back.
- Upstream research/Architecture bytes frozen and untouched since approval (verified by diff).
- Drafting synthesis via `run_drafting_synthesis_v2_agent.py`: 7/7 packages + results + profile synthesis; validated + advanced ARCHITECTURE_ESTABLISHED → DRAFT_COMPLETE.
- Authored reader-facing TeX/Bib/ledger (7 sections + frontmatter + synthesis + source-notes, 26/26 cite-used keys, W38 style/techniques); first CI build failed on bib author underscores → repaired per W38 X-entry convention (no author field) → CI success.
- Pinned CI PDF (12 pages, 323893 bytes, run 36363430195, artifact 10946557163); PDF-extraction re-check clean.
- Built manuscript manifest (31/31 coverage) + deterministic QA (identifier/pdf-preflight/binding) + quality bundle + surface input + Worker surface-semantic PASS + lexical gate PASSED 0/0 + Worker semantic-editorial 11/11 + Worker visual 2/2 (all Worker-attributed, no Sol/Human verdict).
- Assembled publication candidate READY_FOR_PUBLICATION_PREVIEW; validated + advanced DRAFT_COMPLETE → VALIDATED_DRAFT → RELEASE_CANDIDATE (HUMAN_GATE_REACHED, next PUBLICATION_PREVIEW).
- Fresh Publication Preview r1 shell + 14-section dossier; PENDING; no decision recorded or inferred. No Freeze/Release.

## External handoff

- None. Repository-local execution per contract.

## Deterministic execution transport

- Direct exact local CLI throughout (no operator bridge). Normal commits + non-force pushes + remote read-backs; prior-SHA verified before each write group.

## Deviations / failures

- CI build failure (bib author underscores → Missing $ at printbibliography): repaired per W38 precedent, rebuilt green; repaired bytes are the reviewed bytes.
- No Core defect; no upstream invalidation event; shared-Core changed paths = 0.

## End state

- Lifecycle: `RELEASE_CANDIDATE`
- Terminal reason: `HUMAN_GATE_REACHED`
- Next action: `PUBLICATION_PREVIEW` (Human decision only)
- Review target: r1 Candidate + Candidate-bound PDF at reviewed commit `bb6eacabc86e21da77a91d46d4daa2419be5c988` in `publication-preview-r1.md`
- Session status: `COMPLETE_AT_GATE`
