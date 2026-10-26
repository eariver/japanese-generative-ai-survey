# J-GAS 2026-W43 — Independent Sol r3.4 bounded closure audit request

Status: `INDEPENDENT_AUDIT_REQUEST / READ_ONLY / FIXED_SHA / HUMAN_GATE_UNCHANGED`
Date: 2026-10-26 JST. Repository: `eariver/japanese-generative-ai-survey`
Requester: editorial Sol. Executor: **another independent Sol chat/session**, NOT editorial Sol and NOT Muse Worker.
No GitHub writes by independent auditor. This file is an audit contract, **not** a passed audit, editorial acceptance of all 10 issues, PDF authorization, or Human Gate.

## 0. Exact fixed subject and guard

Subject is the **Muse r3.4 content commit**, NOT the later commit that adds this audit request:

- Existing branch: `weekly/2026-W43-v2-work`
- **Fixed audit HEAD:** `1a4cfedb95692ae481c241594e24231680a9a01d`
- **Fixed root Tree:** `a79c26efcbb8c7a2a6555c485b243be6c9746a18`
- Parent (editorial r3.4 instruction): `881a5169ddd26e6962e9f5a8ff8947dab6a86293`
- Reviewed main: `041a08dfef3112643cbf85b4a86a7b6f9128aed6`, tree `a134dc36a407d08ab1de416324229b3955e0325a`
- Frozen Core v2: `774dd39a951c9ac3818e83dfffd4c7666efb0a20`, tree `cd46a6f7a6dcc4031e76220cea4c52c7dd1fc481`.

First fetch and independently verify the exact **fixed subject** commit and root Tree, parent, normal ff ancestry, and its 10 changed paths (9 added, 1 index edit), then verify main/Core are unchanged at the stated versions. If the branch has advanced, **do not shift the audit subject**; identify branch tip separately, and audit only the fixed commit. If the fixed object or tree does not match, stop with an explicit `AUDIT_SUBJECT_MISMATCH`. All activity read-only.

## 1. Blind-first scope and authority

This is **one bounded closure audit of the original independent r3.2 10 findings**, against the r3.4 final reader/ledger/manifest/checker and r3.3 repairs. Do NOT re-run an unconstrained new full weekly survey audit. Independently inspect actual reader and source artifacts **before reading Muse r3.3/r3.4 QA verdicts and before inspecting the editorial concerns in §5**. Record an initial conclusion. Then compare with self-QA, the prior original independent report, and editorial concerns. The requester may not declare its own review an independent audit.

Original independent audit:
- Google Drive `GPT-Sol_Review/20261026022400_SolReview.md`, 45,043 B in prior report, SHA256 `78a61517d59c8140f1c32eff21376657374ab2d7d37af7a4939e63f7bfb1846f`.
- Original r3.2 subject `efac8324ff7a9f35ad34be391ba2ea328cfc1722`, tree `61e33ad8c9b8bb1a3a5e51dbc1d9d5b5b2222c43`; prior verdict REQUEST_CHANGES, P0 0/P1 3/P2 7.
- Original report full text is authoritative for finding IDs/acceptance; preserve their severity. No proof may be invented where raw originals are inaccessible.

r3.4 fixed assets:
- `sources/2026-W43/execution/editorial-bypass/w43-r3-4-reader-preview-UNVALIDATED-20261026.md`
- `.../w43-r3-4-citation-confidence-ledger.json`
- `.../w43-r3-4-physical-row-manifest.json`
- `.../w43-r3-4-strict-row-join-check.py`
- `.../w43-r3-4-row-join-result.json`
- `.../w43-r3-4-source-crosswalk-delta.md`
- r3.3 source-crosswalk and archived primary files. Do not treat the crosswalk or derived Evidence as a directly re-read raw source.

## 2. Ten stable audit findings — original severity unchanged

- `R32-FULL-001` **P1:** MemT 66x at 128K is **storage footprint reduction vs full-context KV**, not throughput/sustained speed; 11-benchmark rank is only among evaluated parametric-memory methods and textual-memory caveat; 1.86x without archived raw remains SOURCE_UNVERIFIED. Check prose/table/ledger/recap against archived MemT README lines 24 and 55.
- `R32-FULL-002` **P1:** Patch 5 stages 1–5 match saved **RENDERED_TEXT**, particularly stage4 product updates and stage5 post-patch guidance/deployment; Daybreak/checker are outside stages; Calif/Wiz/maintainer roles and CVE-not-identified != nonexistent. Do not label rendered extraction original HTML.
- `R32-FULL-003` **P1:** All 20 physical reader tables, 80 physical rows **including exactly 2 NOTE rows**, 78 DATA rows and 3 out-of-scope figure rows; manifest ↔ ledger with exact per-row mapping, 29 claims ↔ correct **DATA row/product/metric/unit/comparator/source**. Independently review the checker logic, row counts/types, table/header identification, negative test strength, row aliases (13), source tiers. Re-check the actual semantics of all 29 claim attachments, not only field presence and token overlap. Detect if any claim is linked to a row where its value is absent or applies to a different product/context. Verify exact SHA256 over the actual reader and ledger **bytes** versus normalized JSON hashes. Distinguish exact byte hash from serialization/content digest. Invariants: 96 blocks, no r3.2/r3.3 mutation. Only an actual proof permits P1 closure.
- `R32-FULL-004` **P2:** TanStack `@tanstack/ai` scoped npm URL vs unrelated `/ai`; GitHub 15:18:14Z and npm 15:21:49.491Z separate sources; npm response RAW_NOT_ARCHIVED.
- `R32-FULL-005` **P2:** Remove operator meta from reader-facing opening; preserve QA governance elsewhere.
- `R32-FULL-006` **P2:** FLUX keyframes `Two at launch` FAQ origin unresolved; no confirmed official-official contradiction. Preserve verified arithmetic vs unverified real hardware performance, keyframes live/schema/GA UNKNOWN, all P4 appearances and recap.
- `R32-FULL-007` **P2:** Duet VM/browser permission live claims separated from 1Password coming-soon secret injection; do not overclaim live integration/safety.
- `R32-FULL-008` **P2:** Voxtral WER/recall comparators/samples, cpWER vs Pyannote, Small/Realtime/agent price units; only evidence-backed amounts/units confirmed. Keep missing raw/AA labels.
- `R32-FULL-009` **P2:** P7 cost differences do not imply equal quality, COBOL 72.1% exception to 19/20 ≥83%; hidden tests vendor-held. DeepSeek MIT vendor-asserted but weight artifact LICENSE bytes/SHA unseen; do not transfer license automatically to API/harness.
- `R32-FULL-010` **P2:** DeepInfer `SamplingParams` snippet must be plainly NONRUNNABLE/PSEUDOCODE/NOT_EXECUTED/IMPORT_UNVERIFIED, not falsely copy-paste executable; unnatural Japanese/duplicated reservations corrected adequately for reader quality.

Preserve independent baseline of 31 Architecture requirements as **20 substantive complete, 11 partial** unless new evidence independently justifies changing it. No arbitrary upgrade to 31/31.

## 3. Direct testing and provenance

Read, independently reconcile and annotate r3.4 subject reader + all ledger/manifest 20 tables and 29 claims. Review Python source logic; where safe, run **only edition-local** read-only checks, then try adversarial mutations in a separate ephemeral local area. **Never run Frozen Core**. Report whether tests actually mutate the physical reader and whether checker can miss row removal, corrupted header, claim count decline, fabricated claim content, swapped source_url or misleading provenance.
Inspect archived MemT README and Patch rendered extraction, plus selected DeepInfer/Flint/Ming/TanStack snapshots to the necessary severity level. Confirm original vs archived-rendered vs accepted-derived vs mere URL. A positive `EDITION_LOCAL_ROW_JOIN_PASS` asserts only structural proof, **not** true raw source, stage validation, Human approval, or PDF readiness by itself.

## 4. Required output

Write one independent report in Google Drive folder `GPT-Sol_Review`, named `YYYYMMDDHHMMSS_SolReview.md` if access allows (or return complete Markdown for placement without claiming upload). Provide actual exact subject HEAD/root Tree; original r3.2 issue-by-issue P0/P1/P2 closure matrix (FIXED / OPEN / QUALIFIED_WITH_LIMITATION); precise reader/ledger row IDs, primary source evidence paths, source type, raw SHA where available, and explicit evidence limitations. Deliver an overall editorial closure disposition: `PASS`, `PASS_WITH_LIMITATIONS`, or `REQUEST_CHANGES` for entry into the **NONCANONICAL Core-free PDF PREVIEW only**. This is NOT a decision to publish/freeze. Any new P0/P1 that survives requires `REQUEST_CHANGES` with minimal bounded repair acceptance tests; distinguish defects that block preview from limitations honestly disclosed.

Do not write GitHub, modify Core, mutate State or Human Gates, create branches, start TeX/PDF, or approve anything as the Human Owner.

## 5. Editorial Sol's *post-blind-first* cautions — compare only after independent inspection

Editorial inspection found 20↔80 manifest and hash guards greatly strengthened relative to r3.3; 9/9 negative tests reported, FAQ language corrected, but did **not** grant full P1 closure. Specific residual inquiries:
1. A `p7-f1` claim `40%+` (COBOL enterprise share) is bound to `p7-f1-01` although that physical table row does not print a 40% number; COBOL 40% appears elsewhere in P7. Decide if binding meets original physical-row requirement, or needs an explicit local fix.
2. A `p8-f2` npm registry clock claim is bound to `p8-f2-03` (版固定) although the exact clock string is printed in `p8-f2-01`. Ledger has npm URL/clock attached to row 03, but the paper's row 03 does not show the clock. Consider exact semantic claim-to-row proof, not just scoped URL.
3. In the checker, claim count 29 is reported by QA/ledger but `validate()` does not directly assert the count; variant binding uses **any token match** or numeric value-core match, not a per-claim expected target; table headers and manifest/ledger row_type equality are not exhaustively checked. Normalized JSON digest is computed rather than raw ledger file bytes for the key named `ledger_sha256`. Judge materiality and whether those omissions can create misleading positive claims.
4. Nine negative mutations primarily manipulate **manifest or ledger** (reader unchanged) even though physical reader manipulations were requested. Distinguish a meaningful detection demonstration from a complete adversarial test suite.
These are **editorial observations, not pre-adjudicated independent findings**. Verify independently and avoid mechanically counting them as four new defects.

Stop at independent audit report. The editorial Sol adjudicates any resulting issues and is responsible for any new Muse contract; **do not autonomously commission Muse or advance Preview**.
