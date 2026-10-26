# r6 print-only diff (r3 TeX -> r6 TeX, single authorized deletion)

Source: `sources/2026-W43/execution/core-free-preview-r3/main.tex`
  raw SHA-256 `bb0e7e1df1a0cb84af49b49e0c1f6092bfff7e5ee43f1aaa45c3fed02e861fed`
  (91053 bytes)
Target: `sources/2026-W43/execution/core-free-preview-r6/main.tex`
  raw SHA-256 `7c052f05227228332fecec469b3b90e1b8952d4c3ab44ea65f180cecd4dd662b`
  (90920 bytes, delta -133 bytes)

Unified diff (full file, exactly one hunk):

```diff
@@ -835,7 +835,6 @@
 \section*{今週の総括}
 \label{sec:recap}
-{\small\color{SurveyMuted}P8の後に置く独立した締めくくり（5段落）。新規のP9パッケージではない。\par}
 \bigskip
```

## Why this is the only permitted reader-visible change

- The deleted line is an internal production note ("place an independent
  closing recap after P8; not a new P9 package") that the r5 independent
  audit (P2 AUD-04) found visibly printed on PDF p20 just after the
  `今週の総括` title. It is not one of the five recap paragraphs and not a
  reader-worthy technical sentence.
- All five recap paragraphs are byte-identical before/after (S07a/S07b
  PASS on the real r6 file, tex-role r6).
- No other prose, table, figure, code, qualifier, clock, URL, or
  bibliography byte changed. `preview.sty` and the print projection are
  byte-identical copies (SHA `46326113…`, `63ad2617…`).
- No layout repair was needed: the deletion removed one short muted line;
  pagination is unchanged (22 pages before/after, recap still p20,
  bibliography still p21-22). No TeX layout fix beyond the deletion was
  applied; had any real print defect been found, this build would have
  STOPped for Sol instead (none found).

## Provenance of the target bytes

- Built by `lualatex` x2 (LuaHBTeX 1.24.0, TeX Live 2026) from the versioned
  r6 `main.tex`; see `build-manifest-r6.json` for commands, exit codes,
  log/output hashes, and diagnostics.
- The r6 verifier (`tex-role r6`, real files) confirms the full segment
  join with exactly the AUTHORIZED_PRINT_ONLY_DELETION allowlist, and the
  N-PRINT-NOTE-LEAK negative confirms reinsertion fails.
- Old r3 PDF (`d0fa8b56…`, 483305 bytes) is NOT asserted for r6; new print
  hash `113b179a…` (482659 bytes) is the pinned r6 subject.
