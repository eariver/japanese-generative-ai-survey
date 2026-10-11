# r15 provenance addendum — audit-accurate evidentiary claims (F08)

Status: `ADDENDUM_R15 / NON_CANONICAL / TRACEABILITY_ONLY`
Addendum to (r14 preserved immutable):
`../r14/evidence-source-provenance-correction.md`
Companion manifest: `retrieval-manifest-r15.json` (EDITION_LOCAL_RESEARCH_EVIDENCE).
Addresses W40-R14-F08 (ACCEPTED). No r14 bytes are altered; this file delimits what is
auditable from what is Muse-asserted.

## A1. Retained arithmetic (unchanged facts)

`19:57:25/45 +0900` = `10:57:25/45Z`, before the independently readable Git commit
`2026-10-10T11:02:43Z` (r13). Three clocks stay separate facts: article publish
(`datePublished` 15:19:50.340Z / 04:01:31.290Z) ≠ retrieval (≈10:57Z) ≠ commit
(11:02:43Z). None is moved by this addendum.

## A2. mtime evidentiary status (the F08 correction)

- The r14-cited mtimes (`19:57:25.601917670 +0900`, `19:57:45.561988218 +0900`) were
  RE-READ r15 from the surviving transport copies (`ls --time-style=full-iso`;
  byte counts and recomputed SHA-256 `49e4b99b…` / `1e5af1b3…` re-verified identical
  to r13 record — copies stable). r14's `CONFIRMED` wording for the JST→UTC
  arithmetic is RETAINED (arithmetic needs no auditor), but the mtimes themselves are
  explicitly labeled **`MUSE_LOCAL_MTIME_REPORTED / NOT_INDEPENDENTLY_REPRODUCED`**:
  the independent reviewer could NOT remeasure them from uploaded/committed files,
  because the transport copies live outside the repo and were never committed.
- Precision/semantics bound: mtime is file-WRITE time, not authoritative HTTP response
  time; claimed precision is minute-level (`10:57Z ±60s`); millisecond GET precision
  is NOT implied. The r13 `~19:57Z` string stays retracted (r14 C1).

## A3. Archival decision (allowlist manifest, NOT full pages)

- Full HTML captures are NOT archived in the repo: the pages embed community comments
  (third-party usernames/avatars = personal data) and dynamic copyrighted content;
  wholesale check-in would violate source-retention/licensing/personal-data prudence
  and the r11 no-raw-bytes policy. Hence `EXACT_RETRIEVAL_CLOCK_NOT_INDEPENDENTLY_VERIFIED`
  for the mtime component, with this reason stated (not silent).
- Instead, `retrieval-manifest-r15.json` is archived as the lawful minimal artifact:
  URL + method/UA + minute clock + byte count + SHA-256 (cryptographic bound) +
  pointer to the allowlisted JSON-LD excerpts already in ledger-r13 (factual metadata:
  dates, byline attribution, canonical URL — no personal data beyond the articles' own
  public bylines already in repo records). An auditor CAN re-fetch both pages and
  compare JSON-LD strings/byte counts; the auditor CANNOT re-derive our mtimes.
- BYTE_DIFFERENCE only (r11 vs r13): "dynamic framing proven" stays WITHDRAWN as a
  causal claim (possible untested explanation). Muse JSON-LD re-parse vs independent
  millisecond re-extraction stay DISTINCT (latter never claimed).

## A4. What remains NOT independently verified (exact list)

1. Retrieval minute itself (mtime-reported only).
2. Millisecond JSON-LD extraction (Muse-executed; auditor corroborated publisher/date).
3. Raw-byte framing causes (no forensic diff; captures unarchived by policy).
4. Items 1–3 are compatible with all committed evidence and block no downstream step
   that cites JSON-LD strings (auditor-corroborated at date level, Muse-parsed at
   millisecond level with the stated boundary).
