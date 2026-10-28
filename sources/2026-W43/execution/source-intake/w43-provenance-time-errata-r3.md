# W43 provenance / time errata r3 (2026-10-24)

No r1/r2 bytes altered. Corrections live only in r3 active rows + this bridge. "Commit time" is never substituted for observation time.

## E1 — r1 `observed_at: 2026-10-24T12:00:00Z` is INVALID (all 36 rows + bundle headers)
- Proof: r1 commit `57afcd292d946078ae03900bd242b6f0b4f7de60` authored/committed `2026-10-24T11:20:22Z` (GitHub + local). Content cannot be observed 39m38s after the commit that contains it.
- Cause: uniform placeholder written instead of measured clock. No session/collector log with true read times exists in r1 artifacts.
- Impact: r1 rows' `observed_at` must not be cited as evidence of when sources were read. Historical bundles remain byte-identical provenance of *what* was recorded, not *when*.
- r3 remedy: all r3 active rows carry `observed_at = 2026-10-24T12:36:18Z` (real measured UTC at r3 build, `date -u`), meaning "re-verified bundle bytes + locator/raw_paths existence at r3 time". Original web-read instants remain UNKNOWN and are not backfilled.

## E2 — r2 run ID `20261024T133000Z-muse-r2` is OPAQUE/MISNAMED, not a timestamp
- Proof: r2 commit `ab69aed74c1c6418ece2842796830134d63fbc30` committed `2026-10-24T11:56:58Z`; the `13:30Z` label is 1h33m02s later. A directory label cannot postdate its committing run.
- r2 `observed_at: 11:50Z` is legitimate (pre-commit, 6m58s before commit, consistent with a fetch-then-commit session) and is retained as plausible; the *folder/run-ID string* is the defect.
- r3 remedy: literal r2 path preserved (immutable); every reference labels it **OPAQUE/MISNAMED — not real execution UTC**. r3 rows use measured `12:36:18Z`. No new r2-style future-coded paths created.

## E3 — Five "raw GitHub API JSON" files are DERIVED FIELD PROJECTIONS, not full response bytes
- Proof: each file is ~237–248 bytes with six keys (`full_name/created_at/pushed_at/updated_at/default_branch/stargazers/forks`), recorded from `api.github.com/repos/*` via a field-selecting script — not an archived HTTP response body.
- r3 remedy: reclassified `DERIVED_GITHUB_API_FIELD_PROJECTION` everywhere (run-ledger r2 already honest about counts; r3 rows/metadata use the projection label). Byte hashes remain valid for the local projection files, never claimed as original API exact-byte capture. Created/pushed dates consumed from the projection are corroborated by independent README/arXiv dates where available.

## E4 — Kimi X HTML IS authentic raw capture (distinguished from Grok)
- Proof: `x-kimi-k31pro-2113680701770068067-20261024T115000Z.html` (208731 bytes, SHA `0891bc1e…`), fetched `2026-10-24T11:50Z` via urllib (HTTP 200), embeds `2026-10-23T17:15:24.000Z` + `Oct 23, 2026` + 19-digit status ID (grep-verified). Raw page shell + embedded JSON present.
- Boundary: this is public X capture by the worker, NOT the Grok/X intake result. `x-source-intake-v2.json` stays `AWAITING_GROK`; no Grok bytes claimed.

## E5 — Observation-clock status per legacy batch
| Batch | Stored `observed_at` | Status | r3 treatment |
|---|---|---|---|
| r1 36 rows + 6 bundles | `2026-10-24T12:00:00Z` | INVALID (post-commit) | r3 rows re-verified at `12:36:18Z`; original instants UNKNOWN |
| r2 15 rows + notes | `2026-10-24T11:50:00Z` | PLAUSIBLE/SUPPORTED (pre-commit) | Retained as plausible; r3 rows re-verified at `12:36:18Z` |
| r2 run-ID string `133000Z` | — | OPAQUE/MISNAMED | Labeled, never parsed as time |
| r2 GitHub JSONs | — | PROJECTION (not full body) | Reclassified, hashes scoped to projection |
| r2 X HTML | fetched 11:50Z | RAW_CAPTURED | Accepted as raw page bytes |
| r3 49 rows | `2026-10-24T12:36:18Z` | MEASURED r3 re-verification | Real `date -u` at build |

If any missing original timestamp cannot be reconstructed (r1 web reads), it stays UNKNOWN per this errata — never forged. Canonical acceptance additionally waits on genuine Grok result + trusted workflow.
