# W43 Grok X post-ID errata r5 (CR-02, 2026-10-25)

Historical documents are preserved unchanged. This scoped erratum corrects the record without mutating history or Grok Raw.

## Exact Raw citation
- Grok Raw: `sources/2026-W43/external/x/weekly-x-2026-W43/weekly-x-2026-W43.md` (13425B, SHA `4571e0de…`), pinned post line:
- `https://x.com/lm_zheng/status/2110889410615234942` (Lianmin Zheng/Meta-affiliated, ~Oct 16) — Muse Spark Open release note + SGLang inference pairing (adoption signal for OUT Oct 15 weights, NOT a new weights release).

## Before / after
- BEFORE (r4 crosswalk `collectors/primary/runs/20261024T133000Z-muse-r4/notes/r4-note-03-grok-crosswalk.md` §"Representative X posts" item 2, preserved as-is): `https://x.com/lm_zheng/status/2110889415895234942`, presented as the Grok Raw pinned URL.
- AFTER (exact): `https://x.com/lm_zheng/status/2110889410615234942`. The two IDs are distinct; the r4 transcription does not match Grok Raw.
- Active Discovery JSONL never contained either second-post ID (grep 0 hits in r4/r5 proposals), so no JSONL fix was required beyond this erratum.

## Verification limits (no fabrication)
- The linked X post itself was not independently fetched beyond the Grok sensor citation; no X timestamp, like count, or content is asserted here beyond what Grok Raw states ("~Oct 16", Muse Spark + SGLang pairing).
- Neither the Raw ID nor the erroneous ID establishes any new in-window model weights release; no X-only candidate is promoted. Kimi official post `2113680701770068067` remains correctly represented.
