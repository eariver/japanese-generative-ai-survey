# r13 ledger provenance correction (superseding interpretations, NOT bytes)

Status: `CORRECTION_R14 / NON_CANONICAL / TRACEABILITY_ONLY`
Scope: explicitly supersedes the INTERPRETATIONS in
`../r13/evidence-source-ledger-r13.md` §0 (and dependent wording in r13 notes/manifest).
The r13 ledger's reviewed bytes, hashes, JSON-LD tables, and dataset-card annex are
PRESERVED IMMUTABLE as historical review evidence — this file corrects readings, it does
not silently rewrite them (W40-R13-F08). Addresses W40-R13-F04 (ACCEPTED) + F08 (MINOR).

## C1. Retrieval clock — JST/UTC confusion CONFIRMED with preserved log evidence (F04-a)

- r13 ledger §0 claimed `2026-10-10 (~19:57Z shown by transport)`. That UTC reading is
  WRONG and CONFLICTS with the r13 commit timestamp `2026-10-10T11:02:43Z` (a capture
  allegedly at 19:57Z cannot precede an 11:02Z commit of notes citing it).
- Preserved evidence inspected r14 (per instruction: actual local logs with UTC-offset
  timestamps): the transport work-copies SURVIVE outside the repo with filesystem
  mtimes `2026-10-10 19:57:25.601917670 +0900` (astabrief.html, 169,199 bytes) and
  `2026-10-10 19:57:45.561988218 +0900` (autosynthdata.html, 210,484 bytes); system
  timezone verified JST (`date` = JST, `date -u` = UTC, offset +0900, checked r14).
- Corrected reading: retrieval completed **2026-10-10 10:57:25Z / 10:57:45Z**
  (19:57:25 / 19:57:45 JST), ~5 minutes BEFORE the r13 commit at 11:02:43Z. The
  sequence is now causally coherent (retrieve → draft notes → commit).
- Precision honesty: file mtime = write-completion time; the GET responses completed
  seconds before. Claimed clock precision is therefore minute-level
  (`EXACT_RETRIEVAL_SECOND: 10:57Z ±60s`), NOT millisecond. The `~19:57Z` string in r13
  is retracted as a timezone-labeling error, with Sol's hypothesized JST/UTC confusion
  now CONFIRMED by the +0900-offset mtimes — not asserted without logs.
- Separation preserved: assertion-level article publish clocks (`datePublished`
  15:19:50.340Z / 04:01:31.290Z) ≠ retrieval time (10:57Z) ≠ commit time (11:02:43Z).
  No claim in this file moves any of the three clocks.

## C2. Byte-count/SHA reading — "dynamic framing PROVEN" DOWNGRADED to hypothesis (F04-b)

- Facts (unchanged, re-verified r14 from the ledger): r11 vs r13 captures share exact
  byte counts (169,199 / 210,484) with different SHA-256
  (r11 `d440b90083…`/`d84a35e696…` vs r13 `49e4b99b…`/`1e5af1b3…`).
- Corrected inference: this demonstrates **bytes differed** — nothing more. The r13
  phrase "dynamic framing PROVEN" is RETRACTED as overstated. Candidate explanatory
  causes (request IDs, relative-time strings, vote/comment counts — all observed to
  render dynamically, e.g. upvote count 28, "Updated N days ago" strings) remain a
  POSSIBLE explanatory hypothesis, explicitly UNATTESTED: raw historical captures were
  not archived in the repo, and no differential forensic reconstruction (byte diff with
  attributable causes) was performed — nor is one claimed here.
- Consequence for citation practice (unchanged from r13, reasoning corrected): raw-byte
  hashes MUST NOT be cited as clocks. The JSON-LD strings remain the citable clock
  ONLY on the strength of their verbatim re-parse (§C3 scope below), not on any claim
  about the surrounding bytes.

## C3. Whose re-parse — Muse assertion vs independent auditor boundary (F04-c)

- Muse r13 DID directly re-parse both pages' JSON-LD (curl bytes → regex extract →
  JSON parse; values match r12 tables). That is a Muse-executed assertion, preserved
  as such in the r13 ledger.
- The independent r13 auditor confirmed publisher/date at review level but **could not
  itself directly re-extract millisecond JSON-LD**. This file therefore distinguishes:
  (i) Muse re-parse: executed, values recorded; (ii) independent exact-second
  confirmation: NOT performed, NOT claimed. Any downstream prose saying "independently
  confirmed to the second" would be false; the correct form is "Muse re-parsed
  millisecond JSON-LD strings 2026-10-10 (10:57Z retrieval); independent review
  corroborated publisher/date without its own millisecond extraction."
- No new re-retrieval is performed in r14 (no network claims beyond the preserved
  mtimes above); the r13 values stand as Muse-asserted, auditor-uncorroborated at
  millisecond precision.

## C4. Negative attestations (F04-d)

- No invented release clock: neither article's JSON-LD nor this file asserts model
  weight upload, dataset creation, code release, or corporate-page clocks.
- No publication-freshness claim: "publicly readable 2026-10-10" describes access at
  retrieval, not content novelty or update recency.
- No retrieved-source SHA authority: the r13 capture hashes (`49e4b99b…`,
  `1e5af1b3…`) are recorded transport observations, not canonical evidence SHAs; the
  files themselves are NOT committed to the repo (r11 policy preserved).
