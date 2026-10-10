# R10 bounded October-2 first-publication investigations (T01/N01)

Method: first-party originals only (publisher RSS/Atom, page JSON-LD/metadata, repo tags/commits).
Fixed window `[2026-09-25T22:00:00Z, 2026-10-02T22:00:00Z)`. Day-only `2026-10-02` is NEVER
enough to assign an hour. Retrieval: curl + webfetch, 2026-10-10Z; exact anchors below.

## 1. Ai2 AstaBrief 8B (`https://allenai.org/blog/astabrief`) — HOLD PRESERVED

- Ai2 official RSS (`https://allenai.org/rss.xml`, 25 items, curl-read): AstaBrief item
  `pubDate 2026-10-02T00:00:00-08:00` — DAY-ONLY granularity (midnight default), same as every
  other Ai2 item (Olmo-core 3 `2026-10-01T00:00:00-08:00`, etc.). No hour evidence.
- Ai2 page HTML head: meta/OG tags carry NO timestamp (verified by grep: description, canonical,
  og:title/image only; RSS alternate link present but no date meta).
- HF mirror (`https://huggingface.co/blog/allenai/astabrief`, curl-read full head): JSON-LD
  `"datePublished": "2026-10-02T15:19:50.340Z"`, `"dateModified": "2026-10-02T15:22:07.584Z"`.
  This is the MIRROR platform timestamp (community article by Ai2Comms), NOT the Ai2 original —
  cannot prove the original's hour.
- Verdict: TIME_UNRESOLVED stands. HOLD preserved. NO scope change, NO reclassification.

## 2. ServiceNow AutoSynthData (`https://huggingface.co/blog/ServiceNow-AI/autosynthdata`) — HOLD PRESERVED

- HF page JSON-LD (curl-read full head): `"datePublished": "2026-10-02T04:01:31.290Z"`,
  `"dateCreated": "2026-10-02T04:01:31.290Z"`, `"dateModified": "2026-10-02T04:05:48.837Z"`.
  Same instant as the external RSS clue Sol already ruled on.
- Per Sol adjudication (binding): secondary external RSS `04:01:31Z` is a lead, NOT issuer-proof.
  The JSON-LD timestamp is the SAME platform-generated metadata (HF platform, not a ServiceNow-owned
  clock); no ServiceNow-owned page/commit/tag with an hour was found in this bounded pass.
- Verdict: TIME_UNRESOLVED stands. HOLD preserved. NO scope change, NO completeness manufacture.

## 3. Cloudflare Web Search API (`.../2026-10-02-introducing-web-search-api/`) — UNADMITTED PRESERVED

- Page JSON-LD (curl-read): `"datePublished":"2026-10-02"`, `"dateModified":"2026-10-02"` — DAY-ONLY.
- Cloudflare changelog RSS (`/changelog/rss/index.xml`, 1326 items, curl-read): item pubDate
  `Fri, 02 Oct 2026 13:00:00 GMT` (13:00Z < 22:00Z cutoff on its face).
- CONTROL against RSS reliability: Oct 1 Clef entry shows RSS `13:00:00 GMT` while the page's own
  JSON-LD proves actual `2026-10-01T15:34:02Z` — RSS times do NOT equal first-publication instants
  (13:00 recurs as a likely feed default). Therefore 13:00:00 is NOT accepted as proof.
- Topic note (N01, no admission): beta Web Search API via AI Gateway (Ceramic/Exa/Linkup, ZDR, BYOK);
  technically material IF ever time-proven; overlaps P8 enterprise surface, would need scope decision then.
- Verdict: hour UNPROVEN. Unadmitted preserved. NO scope change (no `selection-scope-delta` file needed).

## 4. Cloudflare Pi Durable Harness (`.../2026-10-02-pi-harness/`) — UNADMITTED PRESERVED

- Page JSON-LD: day-only `2026-10-02` (same pattern as above).
- Cloudflare RSS: `Fri, 02 Oct 2026 00:00:00 GMT` — DAY-ONLY (midnight default).
- Topic note: Agents SDK `PiHarness` (Pi 1.0 + Pi Durable, beta, Lifecycle/Durable Objects); overlaps P3/P6
  agent-harness surface; material IF ever time-proven.
- Verdict: hour UNPROVEN. Unadmitted preserved. NO scope change.

## Conclusion

- Proven in-window (hour-level, first-party): NONE of the four. HOLD/HOLD/unadmitted/unadmitted preserved.
- No `selection-scope-delta-r10.md` written (nothing proven → nothing to scope-change; per contract the file
  exists only on positive proof). No Discovery/Screening/Evidence/Materiality reclassification performed.
- Negative-space side effect: Cloudflare RSS unreliability is now itself evidenced (Clef 13:00 vs 15:34:02Z
  control) and must be cited if future RSS times are ever offered as proofs.

- artifact_class: CLAIM_LEVEL_DERIVED_NOTE__TIME_INVESTIGATION_LOG
