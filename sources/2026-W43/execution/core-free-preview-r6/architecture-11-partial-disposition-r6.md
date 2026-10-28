# r6 Architecture 31-recount disposition (independent, no promotion)

Task (user instruction §3 + contract §2.8): recount the 31 individual rows
of `core-free-preview-r2/architecture-coverage-and-volume-diagnosis-r2.md`,
compare against the approved determination record, change no verdict, and
report grounds for editorial Sol adjudication.

## 1. Independent recount of the r2 diagnosis rows (worker-computed)

Method: each of the 31 numbered entries (§1.1–§8.3) carries exactly one
trailing verdict token. Counted 2026-10-27 from the committed file bytes:

| Row | ID | Row verdict |
|---|---|---|
| 1 | §1.1 | SUBSTANTIVE |
| 2 | §1.2 | SUBSTANTIVE |
| 3 | §1.3 | SUBSTANTIVE |
| 4 | §1.4 | PARTIAL |
| 5 | §1.5 | SUBSTANTIVE |
| 6 | §2.1 | SUBSTANTIVE |
| 7 | §2.2 | SUBSTANTIVE |
| 8 | §2.3 | SUBSTANTIVE |
| 9 | §2.4 | SUBSTANTIVE |
| 10 | §2.5 | SUBSTANTIVE |
| 11 | §2.6 | PARTIAL |
| 12 | §3.1 | SUBSTANTIVE |
| 13 | §3.2 | SUBSTANTIVE |
| 14 | §3.3 | PARTIAL |
| 15 | §3.4 | SUBSTANTIVE |
| 16 | §4.1 | PARTIAL |
| 17 | §4.2 | SUBSTANTIVE |
| 18 | §4.3 | PARTIAL |
| 19 | §5.1 | PARTIAL |
| 20 | §5.2 | PARTIAL |
| 21 | §5.3 | PARTIAL |
| 22 | §5.4 | PARTIAL |
| 23 | §6.1 | SUBSTANTIVE |
| 24 | §6.2 | PARTIAL |
| 25 | §6.3 | SUBSTANTIVE |
| 26 | §7.1 | PARTIAL |
| 27 | §7.2 | SUBSTANTIVE |
| 28 | §7.3 | PARTIAL |
| 29 | §8.1 | SUBSTANTIVE |
| 30 | §8.2 | SUBSTANTIVE |
| 31 | §8.3 | PARTIAL |

Recount total: **SUBSTANTIVE 18 / PARTIAL 13 / NOT_VISIBLE 0**.
PARTIAL set (13): §1.4, §2.6, §3.3, §4.1, §4.3, §5.1, §5.2, §5.3, §5.4,
§6.2, §7.1, §7.3, §8.3.

The same file's header (line 3) and footer (line 60) both state
`20 SUBSTANTIVE_COMPLETE / 11 PARTIAL`. **The header/footer claim is
inconsistent with the file's own 31 row verdicts by exactly 2 rows**
(18/13 observed vs 20/11 claimed).

## 2. Approved determination records (what the worker could verify in-repo)

- Human-approved `architecture-v2.json` (sha pinned in the r1 APPROVED
  review + `gates/architecture-approval.json`): lists the 31
  must-cover requirements with titles only. **It carries no
  SUBSTANTIVE/PARTIAL tier field.** The Human approval therefore does not
  adjudicate the 20/11 vs 18/13 question at row level.
- r3.1 independent audit receipt: `SUBSTANTIVE_COMPLETE=26 / PARTIAL=5`
  with the PARTIAL set named explicitly
  (§1.4, §2.2, §4.1, §5.1, §5.2). This is the only in-repo per-row
  independent grading the worker could verify byte-for-byte.
- r3.2 comprehensive independent receipt (`20261026022400_SolReview.md`,
  external, 45,043 bytes): `SUBSTANTIVE_COMPLETE 20 / PARTIAL 11`.
  **The per-row composition of that 20/11 is not present in the
  repository** (receipt only; the external report was user-submitted, not
  committed). The worker cannot verify which 2 of the r2 diagnosis's 13
  PARTIAL rows the 20/11 baseline counts as SUBSTANTIVE.
- Contract §2 item 8's illustrative ID list actually enumerates 13 IDs
  while saying "all 11", and the contract itself orders the worker not to
  trust that sentence's count — the worker does not.

## 3. Disposition (no promotion, no demotion, no extra writing)

- The r6 validator records S15 as informational only; no Architecture
  verdict was changed by any r6 artifact.
- The 18/13 recount is worker-observed row arithmetic, not a new audit
  authority and not a revision of the 20/11 baseline.
- The 2-row gap cannot be paired to specific requirement IDs from
  in-repo evidence alone. Candidates for the difference are unknowable
  without the authoritative 20/11 row list (external r3.2 report) or an
  explicit Sol ruling.

## 4. Per-PARTIAL evidence classification (for Sol adjudication)

All 13 observed PARTIAL rows are **evidence-limited** (missing originals /
independent reproduction), none is a fillable prose gap. No additional
technical writing is authorized in r6 on coverage grounds.

| ID | Print anchor (r3 22p) | Ground | Class |
|---|---|---|---|
| §1.4 | p4, p1-t3 + prose | vendor harness only; no independent rerun | evidence-limited |
| §2.6 | p7-8, reading note | no independent run; 65pp unread | evidence-limited |
| §3.3 | p9-10, prose | vendor-described layers; classifier untested | evidence-limited |
| §4.1 | p11, prose | UNRESOLVED_FAQ_ATTRIBUTION; live unconfirmed | evidence-limited |
| §4.3 | p11-12, prose | +47/+50 not unified; AA unfetched | evidence-limited |
| §5.1 | p12, p5-t1 | TTS counts unresolved; 11-lang sample ≠ coverage | evidence-limited |
| §5.2 | p12-13, prose + p5-f1 | vendor-selected judge; units qualified | evidence-limited |
| §5.3 | p13, p5-t2 | MIT confirmed; AA originals unfetched | evidence-limited |
| §5.4 | p13-14, prose | compat listed; guide unopened; AA via blog | evidence-limited |
| §6.2 | p14-15, prose | vendor-described isolation; RSS secondary | evidence-limited |
| §7.1 | p15-16, p7-t1 | team-internal; wet-lab unconfirmed | evidence-limited |
| §7.3 | p17, prose | bias/unverified retained | evidence-limited |
| §8.3 | p19-20, p8-t2/p8-f3 | MIT vendor-declared (SHA unseen); bench vendor harness | evidence-limited |

Sol decision needed: (a) confirm the authoritative 20/11 row composition,
(b) rule whether the r2 diagnosis header/footer (20/11) or its rows
(18/13) govern downstream references, (c) authorize any correction as a
separate editorial act — not as an r6 side effect.
