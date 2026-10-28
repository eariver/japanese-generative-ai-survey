# W43 r2 chronology repairs + authority ledger (DC-05/DC-06/DC-08/DC-09)

## DC-05 Kimi correction (BLOCKING fixed)
- r1 error: `17:15 ET = 21:15Z` + malformed 22-digit status `2113680701770068068067` + 45-min cutoff claim.
- Verified original: X HTML `x-kimi-k31pro-2113680701770068067-20261024T115000Z.html` (208731 bytes, SHA 0891bc1e…, fetched 2026-10-24T11:50Z via urllib, HTTP 200) contains `2026-10-23T17:15:24.000Z` + `Oct 23, 2026` + status `2113680701770068067` (19 digits).
- Correct reading: **13:15:24 EDT = 17:15:24Z Oct 23**, **4h44m36s before exclusive 22:00Z cutoff** → safely IN (not edge). Related threadreader corroborates K3.1 Pro topic. Blog `kimi.ai/blog/kimi-k3-1-pro` consumed (post-trained K3, RL stack, Terminal-Bench 65.7 vs Astra 58.2 vs Opus 5.5 66.4, Code Bench Long-horizon 61.2 vs 55.95, BenchCAD 92.7 with-tools, OfficeQA Pro v2 64.4, Hallu 23.4→8.3%, xdev 81.0 vs 90.5 unmitigated, cyber data removal, weights by Nov 4, Highspeed 2-3x, channels apps/Work/Code/API/Business, footnotes harnesses/temps). No date header on blog page; date proof via X + TNW Oct 23 + Simon Willison Oct 23. API Oct 23 = W43 event; weights Nov 4 = future, NOT current availability.

## DC-06 arXiv times (BLOCKING fixed, via arXiv API 2026-10-24)
- 2610.24264 AM-Bench: v1 `2026-10-16T21:46:19Z` OUT (13m41s before start) ; v2 `2026-10-20T15:40:19Z` IN as revision event. v1 OUT as research; v2 is potential revision event only if substantive delta examined (delta check still open — do not auto-promote).
- 2610.24087 OR-License: v1 `2026-10-16T18:13:25Z` OUT (only version). OUT background.
- 2610.23374 MOSS-Image report: submitted `2026-10-16T12:27:37Z` OUT as research; README Oct 19 announcement is IN as distribution (kept distinct).
- 2610.26825 MemT-1.0: v1 `2026-10-19T17:54:35Z` IN; v2 `2026-10-20T14:30:38Z` IN revision. Clean IN.
- No `EDGE time unknown` retained.

## Repo-creation vs announcement separation (new in r2)
- MOSS-Image repo created Oct 16 01:18:13Z OUT → Oct 16 Base/SFT release OUT; Oct 18 trainer IN; Oct 19 report-announce IN; Oct 20 API IN.
- DeepInfer repo created Oct 16 07:47:23Z OUT → repo OUT; Oct 20 X/PyPI announce IN as distribution.
- MemT repo created Oct 19 03:29:30Z IN; Ming repo created Oct 19 07:03:25Z IN; Kohaku trainer created Oct 18 11:08:53Z IN. All IN.
- GitHub API meta JSONs archived as raw (5 files, ~240B each).

## DC-08 leads disposition
- Ming-3.0-tts: repo Oct 19 IN; News month-only [2026.10] (day unproven); AA + vendor tables consumed; roadmap (vLLM-Omni, report) pending. IN lead with month-precision caveat.
- ARC Argon Oct 13: page consumed (v1 98.5%/v2 91.2% high, v3 49.8% low Standard / 97.5% Provider; incomplete v3 Standard coverage 42/55/19; $2/$10). Date Oct 13 = OUT. ARC leaderboard lists Qwen3.8-27B as a row — NOT issuer proof for W42 HOLD name; quarantine holds. Parked as OUT background with reason, not redated.
- Rejected/parked with reason: Mercury/MiniMax/Flint/Mammoth (secondary listings only, no primary); OrcaCyber Abliterated (vendor page only); Agentic AI Foundation governance move (Oct 24 report, primary undated/post-cutoff risk); JLS/Bear/Unitree/FLAIR (trade-press only).

## DC-09 carry preservation
- All 12 W42 HOLD/INSPECT rechecks preserved from r1 (no promotion, no repetition of allegation/name as fact). MOSS/FLUX/DeepInfer/VOX families explicitly distinguished from LTX/Fish/Le Chonk/SMLIB gaps.

## Raw-authority ledger (r2 run)
| # | Source URL | Method | HTTP | Bytes | SHA256 (archived) | Publisher/date proof | Class |
|---|---|---|---|---|---|---|---|
| 1 | x.com/Kimi_Moonshot/status/2113680701770068067 | urllib direct HTML | 200 | 208731 | 0891bc1e… | embedded 2026-10-23T17:15:24.000Z + Oct 23 2026 | RAW_CAPTURED (page shell + JSON; tweet text via embedded data) |
| 2-6 | github api repos (MOSS/MemT/Ming/DeepInfer/Kohaku) | GitHub API JSON | 200 | ~240 ea | per-file sha | created_at/pushed_at | RAW_CAPTURED (API JSON) |
| 7-19 | openai x3, 1password x2, MOSS README, MemT abs+README, Ming README, Duet, DeepSeek docs, DeepInfer README, Nemotron, Voxtral, Eleven, FLUX(PR/model/X/VB), TanStack, GitHub x2, ARC | webfetch rendered markdown (read in full) | 200* | note-file bytes | note-file sha | page headers + cross-links | SUBSTANTIVELY_CONSUMED (rendered body; original HTML NOT archived) |
| 20 | openai curl x3 | curl generic UA | 403 | ~9.9k challenge | discarded | none | AUTHORITY_RETRIEVAL_FAILED (bot wall; webfetch succeeded instead) |
| 21 | X authorship (all other X locators) | none (no X-HTML) | — | 0 | — | secondary excerpts only | NOT_CAPTURED (existence/authorship unvalidated) |
*webfetch transport status; original HTML bytes not preserved. Derivative notes are NOT original source bytes — never double-count a notes file as 10 original bodies.
