# Feedback — Publication Boundary Validator (first real W34 production run)

Tool: `eariver/publication-boundary-redteam@7b9de2105c690daaafa6698c1791d51ca84a92c0`
Scanned artifact: `surveys/weekly/2026-W34/main.tex` + sections + `references.bib` (Weekly profile, JSON output)
Run: 2026-09-12, exit 1, aggregate `FAIL` (164 hard fails in `references.bib`, 1 needs-review in section 20, 9/11 targets PASS)

## Usability

- Pinned-SHA clone plus `PYTHONPATH=src` invocation worked without installation. CLI flags (`--profile weekly --format json`) matched the prescribed form. JSON output is machine-readable with per-target status, rule IDs, categories, severities, and line-precise locations — easy to triage.
- Scanning `main.tex` alone would have missed everything (it only `\input`s sections); the section/bib extension was necessary for a meaningful first run. Consider documenting multi-file invocation for modular TeX layouts.

## Resource behavior

- Negligible: seconds of CPU, no heavy dependencies observed.

## Useful findings

- The `references.bib` FAIL is a genuine reader-facing defect in our artifact: all 41 notes expose `Core v2 Evidence: VERIFIED; materiality: MATERIAL`. This directly violates the publication boundary and would have shipped internal dispositions to readers.
- Per-target PASS results on `main.tex`, frontmatter, and 7 of 8 content sections corroborate the prose-side editorial guards (no internal paths/hashes/labels/review language detected).

## Suspected false positives / negatives

- `RULE-BOUNDARY-MISSING-EXPECTED-FRAMING` on section 20 looks like a false positive: the boundary explicitly says `Mistral-reported` with `no independent reproduction`. The rule seems to want a narrower phrasing pattern and does not cover this equivalent framing. No prose change made on this signal alone.
- No assessment of missed detections beyond noting that English-language boundary blocks passed without comment on their reader accessibility (Japanese readers get English limitation text) — a possible recall gap for mixed-language publications, flagged for Sol awareness rather than asserted.

## Output / context issues

- Findings on `references.bib` repeat 4 rules × 41 entries (164 rows) with no roll-up; an aggregated per-pattern summary would speed triage.
- `matched_text`/`context_snippet` truncation is fine at this volume but the suggestion text is cut off mid-sentence in JSON (`...must be r`).

## Operational usefulness

- High as a pre-candidate gate: it caught a real defect class (bib disposition leak) that deterministic Core validation does not check (Core binds bytes, not reader-facing wording).
- Recommend keeping it NON-AUTHORITATIVE: one of its two non-PASS signals appears to be a false positive, and the tool cannot judge Japanese-reader accessibility of English boundary prose. Its value is detection + triage, with Sol/human disposition.

## Recommended improvements

1. Roll up repeated identical rule hits per file/pattern.
2. Document multi-file scanning for `\input`-modular TeX.
3. Recognize `X-reported` / `maker-reported` / `no independent reproduction` as valid vendor-framing equivalents.
4. Add a mixed-language readability note (informational, not hard-fail) when long English blocks appear in Japanese publications.

## Shared-Core observation (no edit made)

- The bib note template originates from the current Core weekly renderer's `_bib_text` (`note = {Core v2 Evidence: …; materiality: …}`). Any future artifact rendered through that helper would reproduce this sidecar FAIL. Left untouched per production/Core boundary; Sol disposition required.

Disposition: tool should REMAIN NON-AUTHORITATIVE read-only second opinion.

Markers: `SIDECAR_A_FEEDBACK_RECORDED`.
