# TypeSafe/Jev temporal correction (Issue #511, append-only, edition-local)

Status: `EDITION_LOCAL / APPEND_ONLY_CORRECTION / ORIGINAL_BYTES_PRESERVED / PRE_PREVIEW_R2`

Issue: `2026-W38` — Human Publication Preview r1 `REQUEST_CHANGES`, Issue #511

Recorded: `2026-09-19T17:05:00+09:00` (`2026-09-19T08:05:00Z`, actual system wall clock at generation)

## 1. Bound original authority (preserved, not rewritten)

- Original collector record: `sources/2026-W38/collectors/primary/runs/20260919T000000Z/typesafe-jev-20260915.md`
- Original collector SHA-256: `9f9c904dfb473c25b338c4869022ae4412ae6ee0cda9d230c3328679ec1b542e`
- Accepted Evidence task: `sources/2026-W38/evidence/v2/accepted/2fb0718c2e3feba332258adaf49db3d78235624ba2d661ac93ec09953d73bc99/tasks/task-e94d9079ebe049497f16.json`
  (task SHA-256 `0b8277876ecc8873ea46dffba932f994ff3e89115aea5053640fa24af53490df`)
- Original collector filename/date suffix (`typesafe-jev-20260915`) is historical and non-authoritative; it is not being rewritten.

## 2. Superseded temporal statement

Original collector line:

```text
published_date_on_page: Sep 15, 2026
```

is **invalid as the blog displayed-date authority** and is superseded by §3 below. All non-temporal
technical claim boundaries in the original record (System One framing, RLCD, pricing/speed vendor-stated
bounds, schema-guarantee scope, no-params/topology invention) are preserved unchanged.

## 3. Normalized two-date model (execution-request §8 authority)

- `blog_displayed_publication_date = 2026-09-14`
  - precision: `DAY`
  - authority: TypeSafe first-party blog page (`https://typesafe.ai/blog/introducing-system-one-models-and-jev`,
    “Company News” displayed date per Sol re-read bound by execution request §8)
- `founder_launch_announcement_at = 2026-09-15T18:17:52.151Z`
  - authority: direct public X status by Diogo Almeida / `@CompleteSkeptic`
    (`https://x.com/CompleteSkeptic/status/2099925682726002904`, Snowflake-derived UTC, already retained as
    row 16 of the accepted W38 X ledger as the Jev launch announcement)
  - relationship: distinct public launch announcement; **not** the blog publication-date field
- W38 relation: both dates fall inside the ordinary W38 window `[2026-09-11T22:00:00Z, 2026-09-18T22:00:00Z)`.
- Event identity, materiality, selection, package identity/order and approved Architecture: **unchanged**.

No speculation is recorded about why the two dates differ, and neither is reinterpreted as a timezone
conversion of the other.

## 4. Worker re-read observation (disclosed, non-overriding)

At repair execution time the worker independently fetched the first-party page twice (text and markdown
transforms). Both renders showed body text `Sep 15, 2026` with front matter `published: Sep 18, 2026,
11:44 PM UTC`. The front-matter value is demonstrably a fetch/transform artifact (it contradicts the body
in the same fetch), and this exact page already carried documented fetch-date artifacts in the original
collector record. The worker renders therefore cannot establish displayed-date authority and do **not**
override the §3 contract model; they are disclosed here so Sol can independently verify.

## 5. Downstream effect

Where approved Architecture text carries the old “Sep 15 date” limitation language, that temporal phrase is
superseded for downstream Drafting by this correction authority. Approved Architecture bytes themselves are
not modified. Regenerated Draft/publication surfaces must follow §6.

## 6. Required reader-facing wording (execution-request §10)

- TypeSafe blog: `9月14日付`
- founder/creator launch announcement: `9月15日` (only when labeled as such, citing the direct X status)
- No regenerated sentence may call the TypeSafe blog itself a Sep 15 publication.
- Bibliography TypeSafe blog date must be Sep 14.

## 7. Shared-Core implication

None. No shared-Core modification.
