# r6 reference-claim tier curation (13 NATURAL + 2 FURTHER, exact spans)

Status: `CURATED_REVIEW_REQUIRED` for all 15 keys below. Nothing here
upgrades a natural-language mention or an unarchived URL into archived
source proof or independent verification. Missing originals (AA tables,
FLUX PR/FAQ, Voxtral units, Decisions 404) and unreproduced benchmarks
stay caveated. The other 21 keys (19 EXACT_VISIBLE + 1 EXACT_MACHINE_ONLY
`recap` + 1 UNAVAILABLE_NO_CLAIM_PROOF `decisions-ref-create`) retain
their exact category transparency; `decisions-ref-create` is a 404 record
only and is never used as a claim proof.

Programmatic span basis: S12 (`19/1/13/2/1/0`, ORPHAN 0) + per-key exact
quotes asserted in both projection and TeX visible text by the r6
validator. Reader locations below are the audited prose/figure/table
positions; print positions are the r3 22-page map (cover1/TOC1/body+recap18/bib2).

## 13 EXPLICIT_NATURAL_REFERENCE (all CURATED_REVIEW_REQUIRED)

1. `1pw-blog-1022` — quote `1Password発表（2026-10-22、coming soon）`
   in P3 prose + Fig p3-f1 path B; printed as natural mention, not an
   exact-key citation. Official URL
   `https://1password.com/blog/1password-for-ai-agents` <-> bytes:
   read, not archived (accepted Evidence record only). Confidence: the
   span supports "provided-soon, not live"; it never proves integration
   or live status.
2. `flux-elo-1139` — quote `Elo 1139 は暫定値` in P4 prose; printed with
   +47/+50 non-unification qualifiers. URL = flux-page-1019
   (snapshot differs). Bytes: AA original tables unfetched. Confidence:
   span-verified vendor citation, not an independent measurement.
3. `flux-keyframes-conflict` — quote `Two at launch` in P4 prose + table
   note; printed as UNRESOLVED_FAQ_ATTRIBUTION. URL: none fetched.
   PR original + FAQ original both unfetched. Confidence: transparent
   record of an uncollated discrepancy, never a confirmed contradiction.
4. `voxtral-card-units` — quote `cpWER 18.4/18.6` in P5 p5-f1 rows
   (WER/cpWER/recall/prices). URL `https://mistral.ai/news/voxtral-3`
   <-> bytes: read, not archived; comparators/units unconfirmed.
   Confidence: span-verified natural support, not exact-key proof.
5. `deepinfer-import-scope` — quote `SamplingParams` in P2 prose + code
   comments + DI-README commit scope. URL = DI-README fixed 9bd9cf24
   (fixed bytes archived). Import path unconfirmed in saved first-party
   material. Confidence: name/scope verified in fixed bytes; the call
   shape is README-range description, never an executed run.
6. `flux-speed-recalc` — quote `277.80秒÷10.95秒` in P4 prose/table
   (25.37x/22.31x/95.52% arithmetic). URL = flux-page-1019.
   Confidence: arithmetic independently recomputed from vendor numbers;
   still vendor numbers, not independent measurement.
7. `ming-aa-cited` — quote `AA三行=発行元引用` in P5 p5-t2 rows.
   URL = ming repo (roadmap retained). AA original tables unfetched.
   Confidence: natural-language support with explicit unfetched caveat.
8. `eleven-blog` — quote `移行指南は未開封` in P5 prose (realtime
   compat + unopened-guide notes). URL elevenlabs realtime blog <-> bytes:
   read, not archived. Confidence: span-verified; guide ease never
   asserted.
9. `patch-rendered` — quote `五段階` in P6 prose (coordinated-disclosure
   stages + task-5d21d93e evidence path). URL openai coordinated-disclosure
   page <-> bytes: RENDERED_ONLY (bot-wall, 9946B drawn-text extraction;
   original HTML never viewed). Confidence: stage wording follows the
   saved extraction lines 17-22; never original-view proof.
10. `securing-page-rss` — quote `RSS` in P6 prose (isolation + page/RSS
    clock distinction). URL securing page <-> bytes: page-date only;
    RSS 10:00Z is secondary. Confidence: natural-language support; RSS
    never proves page time.
11. `tanstack-blog` — quote `blog10月23日は日付のみ` in P8 prose+table.
    URL: not fetched. Treated as date-only existence, never a product
    clock; GH (15:18:14Z) and npm (15:21:49Z) clocks stay separated.
    Confidence: span-verified separation note, not source proof.
12. `decisions-guide-1025` — quote `70f106a9` in P8 典拠 (guide URL +
    snapshot path + SHA). URL developers.openai.com guide <-> bytes:
    2026-10-25 post-cutoff observation. Confidence: supplementary
    post-cutoff only; never promoted to a W43 fact.
13. `decisions-ts-ref-1025` — quote `30m` in P8 prose (TTL observation
    note). URL typescript reference <-> bytes: 2026-10-25 read, post
    cutoff. Confidence: observation-time detail; never a W43 fact and
    never used for specification claims.

## 2 FURTHER_READING (both CURATED_REVIEW_REQUIRED)

- `DI-ENV` — quote `environ.py` in P2 code comments + provenance line;
  same fixed 9bd9cf24 commit as DI-README (8738B file provenance).
  Natural language present. Confidence: file-level provenance only.
- `DI-LICENSE` — quote `Apache-2.0` in rights prose; same-commit LICENSE
  bytes. Patent/trademark scope unexamined. Confidence: license-byte
  provenance only.

## 21 remaining keys (unchanged categories)

19 EXACT_VISIBLE_CITATION (reader-visible spans counted programmatically;
presence is not claim-support proof): KIMI-X, KIMI-BLOG, FLINT-CARD,
FLINT-ART, NEMO-CARD, NEMO-COMMITS, DI-README, MEMT-README, duet-blog-1021,
automode-art-1022, flux-page-1019, voxtral-announce, ming-readme-license,
bio-page, lowres-page, decisions-page, tanstack-gh, tanstack-npm,
deepseek-1017. 1 EXACT_MACHINE_ONLY: `recap` (label only).
1 UNAVAILABLE_NO_CLAIM_PROOF: `decisions-ref-create` (404 on 2026-10-25;
transparent record, never a proof). 0 ORPHAN.

## Editorial rule (binding)

No key above changes status on the basis of this curation. Any future
upgrade requires archived original bytes + independent re-read, recorded
separately. GH timestamps prove GH only; npm registry data stays
RAW_NOT_ARCHIVED; the 404 never validates a claim; post-cutoff
observations never become W43 facts.
