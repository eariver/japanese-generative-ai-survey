# W43 Core-free editorial QA r3.1 (UNVALIDATED, noncanonical)

Status: `EDITION_LOCAL_EDITORIAL_BYPASS / UNVALIDATED / NOT_DRAFT_COMPLETE`
Date: 2026-10-25. Branch: `weekly/2026-W43-v2-work`.
r3.1 preview: `execution/editorial-bypass/w43-r3-1-reader-preview-UNVALIDATED-20261025.md`
Ledger: `execution/editorial-bypass/w43-r3-1-citation-confidence-ledger.json` (96 rows, p8-f1 updated; SHA256 `e418a8772cce32a1a2cef7c94f7b9c3ea11edc628ff22da7d901cdc47b78726c`)
Crosswalk: `execution/editorial-bypass/w43-r3-1-source-crosswalk.md` (34 keys, full repo-relative paths, 17 archive files existence-verified)
Snapshot: `execution/source-intake/w43-r31-decisions-guide-snapshot-20261025.md` (37,326B, SHA256 `70f106a9a7f1ed57bb80bf209603bf2270c405d3467e4e44a4aa962b6c5fa1fa`, observed 2026-10-25T15:34:09Z)
Basis: Sol r3 verdict R3-SOL-01–04. r1/r2/r3 preserved unchanged.

## 1. Character recount + correction note (R3-SOL-02)

One documented consistent method — whole-file character count plus prose-only count:

```text
python3 -c "
import pathlib
for v in ['r2','r3','r3-1']:
    t = pathlib.Path(f'sources/2026-W43/execution/editorial-bypass/w43-{v}-reader-preview-UNVALIDATED-20261025.md').read_text(encoding='utf-8')
    full = len(t)
    in_fence = False; prose = 0
    for line in t.splitlines():
        s = line.strip()
        if s.startswith('\`\`\`'):
            in_fence = not in_fence; continue
        if in_fence or not s: continue
        if s.startswith(('#','>','- ')): continue
        prose += len(line)
    print(v, 'full:', full, 'prose-only:', prose)
"
```

| rev | full-file chars | prose-only chars |
|---|---|---|
| r2 | 26,678 | 20,207 |
| r3 | 32,065 | 20,803 |
| r3.1 | 33,155 | 21,431 |

Deltas (same method): r2→r3 full +5,387 (incl. Markdown layout/refs/fences), prose-only +596. r3→r3.1 full +1,090, prose-only +628.
**Correction note (r3 history NOT rewritten):** r3 QA/session/handoff claim of "+9,900 substantive characters" is UNSUPPORTED and hereby corrected. The 22,185 baseline was interactive-input block-text chars (different denominator: input JSON text fields, no Markdown/tables-as-fences/headers). Comparable whole-file growth r2→r3 is +5,387 code units, of which prose-only +596; the rest is tables/code/figures markup. Substantive additions (direct-archive citations, row keys, 10 artifacts) are real but must not be expressed as +9,900 prose chars.

## 2. Reader-facing cleanup (R3-SOL-03)

Removed from r3.1 reader ending: `（了。運用メモ・編集注記は \`w43-r3-editorial-qa.md\` に移管した。）`
Evidence of deletion kept here (this section). Five `今週の総括` paragraphs intact after P8, no editor-only comments remain in reader view (verified: no 編集注記/留意事項/予定検証/主体/目録残留 — grep clean).

## 3. Archive paths (R3-SOL-04)

All crosswalk archive entries expanded to full repo-relative paths (15 `sources/2026-W43/collectors/...` + snapshot + ledger paths); 17 archive files existence-verified on this commit; not-yet-archived originals stay `—`/UNRESOLVED. Tables/figures remain fenced text (DRAFT_TEXT, layout unvalidated). Oct25 guide read is NOT promoted to an Oct22 raw snapshot (see §4).

## 4. P8 official example provenance (R3-SOL-01)

- Guide fetched+read by Muse 2026-10-25: `https://developers.openai.com/api/docs/guides/decisions` (snapshot hash above). TS reference `.../api/reference/typescript/resources/decisions/methods/create` read same day (TTL 30m・usage fields as observation-time detail only). Plain reference `.../api/reference/resources/decisions/methods/create` 404s (moved) → ARCHIVE_UNAVAILABLE.
- p8-f1 now: verbatim guide choice request JSON (paired scenario, syntax-validated by parse, probabilities sum 1.0) + guide's official illustrative choice response excerpt, explicitly labeled NOT a run result. No invented endpoint/version/TTL/outputs. Publisher Oct22 GA description (changelog bytes + card) kept distinct from Oct25 guide observation.
- New-doc-novelty check: used atoms (3 types, text/image/JSON, 400/req, cache, session.triggers, pricing) all lie within the W43-selected Decisions topic; newer guide additions (conversation history, Private Link, voice, org reporting) NOT included. No SOURCE_CONFLICT → no consult-stop needed.
- Ledger p8-f1: exact doc URL, tier SOURCE_REPORTED (not VERIFIED_DIRECT), snapshot path+hash, sample provenance (instruction example vs illustrative output).
- §8.1 truth value: PARTIAL → **SUBSTANTIVE_COMPLETE** (official example present, NOT_RUN tracked). New 31-matrix: **29 SUBSTANTIVE_COMPLETE / 2 PARTIAL** (§4.1, §5.1 — design-level UNRESOLVED).

## 5. Residual risks (carried + new)

1. FAQ/AA/original-URL gaps unchanged (UNRESOLVED, no invention). 2. All vendor numbers unreproduced; p2-f1/p8-f1 NOT_EXECUTED/NOT_RUN. 3. Layouts DRAFT_TEXT. 4. Core Draft Stage still BLOCKED; `runner.generated_at` never provenance. 5. TTL 30m and newer guide features are Oct25 observations, not W43 facts. 6. Original `20261025212008_SolReview.md` still unread in-session (standing limitation).

## 6. Invariants

r1/r2/r3 outputs byte-untouched (this run adds r3.1 files only). State `ARCHITECTURE_ESTABLISHED`, Gate approval, Architecture/Selection/Evidence, main/Frozen Core, shared roots untouched. No native validation/TeX/PDF/Preview/Release/ADVANCE.
