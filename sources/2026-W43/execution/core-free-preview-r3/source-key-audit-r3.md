# W43 source-key audit r3 (exhaustive, reproducible)

Method: exact `\bibitem[label]` (36) vs TeX body before `\begin{thebibliography}` (exact string count) + explicit natural-language claim mapping + crosswalk tier/URL. r2 claim `0 unused (all keys appear in reader 典拠 notes or body)` is CORRECTED: 18 keys have zero exact body occurrences. No new citations invented; unavailable originals not forcibly cited.

Categories: (a) EXACT_IN_BODY / (b) CLAIM_SUPPORTED_BY_EXPLICIT_NATURAL_LANGUAGE_REFERENCE / (c) SECONDARY_OR_FURTHER_READING / (d) SOURCE_UNAVAILABLE_DO_NOT_CITE / (e) ORPHAN/AMBIGUOUS (must be 0).

## (a) EXACT_IN_BODY — 18 keys

KIMI-X (3x: p1 prose + 2 tables), KIMI-BLOG (2x), FLINT-CARD (3x), FLINT-ART (1x), NEMO-CARD (3x), NEMO-COMMITS (2x), DI-README (1x: p2 典拠), MEMT-README (2x: p2-t2 典拠 + prose), duet-blog-1021 (1x), automode-art-1022 (1x), flux-page-1019 (1x), voxtral-announce (1x), ming-readme-license (1x), bio-page (1x), lowres-page (1x), decisions-page (1x), deepseek-1017 (1x: p8-t2 典拠), recap (1x: recap prose self-ref).

## (b) NATURAL-LANGUAGE supported — 15 keys (no exact string, explicit prose/table/value + crosswalk)

- 1pw-blog-1022: body “1Password発表（2026-10-22、coming soon）” + Duet figure path B; tier FIRST_PARTY coming-soon. Material (permission boundary). No new cite added (existing prose sufficient).
- flux-elo-1139: body Elo 1139・4868票・+47/+50 with AA-unfetched qualifiers; tier DERIVED_ONLY. Material (quality). No new cite (same page as flux-page-1019).
- flux-keyframes-conflict: body keyframes UNRESOLVED prose + table note; tier UNRESOLVED, both originals unfetched (transparent record, not validating source). Material (availability). Retained as (b)+(d) transparent.
- voxtral-card-units: body p5-f1 WER/cpWER/recall/prices with comparator/unit qualifiers + task-18a859 line; tier VENDOR_BENCH. Material (voice). No new cite (same announcement as voxtral-announce).
- deepinfer-import-scope: body SamplingParams import discussion + code comments + DI-README fixed commit; tier FIRST_PARTY partial. Material (code). Code verbatim not edited (would corrupt source).
- flux-speed-recalc: body 25.37x/22.31x/95.52% arithmetic + flux-page-1019 典拠; tier VERIFIED_DIRECT. Material. Same-page key covers recalc.
- ming-aa-cited: body AA three rows “発行元引用（原表未取得）” + ming-readme-license line; tier DERIVED_ONLY. Secondary-leaning but explicit.
- eleven-blog: body realtime-compat prose + SDK/unguided notes; tier FIRST_PARTY. Explicit.
- patch-rendered: body 5-stage prose + task-5d21d93e + saved-extraction path 17-22行; tier RENDERED_TEXT. Material (disclosure). Key labels the cited file; exact string absent but file path + task explicit.
- securing-page-rss: body isolation prose + page/RSS clock distinction; tier METADATA. Explicit.
- tanstack-gh: body GH 15:18:14Z prose (2x) + p8-f2 table + **r3 NEW 典拠 line `安定核=tanstack-gh（GH 15:18:14Zのみ）`**; tier FIRST_PARTY GH-only. Material — REPAIRED with exact key display (F-R3-03 minimal fix).
- tanstack-npm: body npm 15:21:49Z prose (3x) + p8-f2 table + **r3 NEW `npm=tanstack-npm（15:21:49Z・別典拠・原本未取得）`**; tier FIRST_PARTY_METADATA RAW_NOT_ARCHIVED. Material — REPAIRED. GH≠npm separation explicit in same line.
- tanstack-blog: body “blog10月23日は日付のみ” (2x); tier METADATA separated. Explicit (date-only, not product clock).
- decisions-guide-1025: body URL + snapshot path + SHA `70f106a9…`; tier post-cutoff FIRST_PARTY. Supplementary (post-window observation, not W43 fact).
- decisions-ts-ref-1025: body “TTL 30m (Oct25 TS ref, not W43)” note; tier observation-detail. Supplementary.

## (c) SECONDARY_OR_FURTHER_READING — 2 keys

- DI-ENV (environ.py 8738B provenance for same 9bd9cf24 commit as DI-README): file-level provenance, natural language (`environ.py（8738バイト）`, code comments) present; retained as further reading, not a separate claim validator.
- DI-LICENSE (Apache-2.0 bytes): natural language (`LICENSEはApache-2.0`) present; retained as further reading.
- (flux-elo-1139 / ming-aa-cited / securing-page-rss could double as (c); primary category above is (b) due to explicit claim text.)

## (d) SOURCE_UNAVAILABLE_DO_NOT_CITE — 1 key (+1 transparent)

- decisions-ref-create: 404 on 2026-10-25, ARCHIVE_UNAVAILABLE. Retained SOLELY as transparent unavailable-record (“典拠に用いない”), never validating claims.
- flux-keyframes-conflict doubles here (both originals unfetched) but retained as transparent UNRESOLVED record per (b).

## (e) ORPHAN/AMBIGUOUS — 0

No bibitem lacks body/audit traceability after r3 repair. Previously false `0 unused` is replaced by 18/15/2/1/0 split above.

## TanStack absolute rule (re-verified)

- tanstack-gh JSON proves GH `published_at` 15:18:14Z ONLY; never npm. tanstack-npm time 15:21:49.491Z is accepted crosswalk-derived, RAW_NOT_ARCHIVED, scoped URL. r3 body (prose 2x + table + new 典拠 line) and bibitems state this explicitly. PDF text extraction verified in QA.
