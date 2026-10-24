# W43 Sol Discovery Completeness Review r2 — bounded normalization ruling

Status: `SOL_SUPERVISORY_REVIEW / LIMITED_REQUEST_CHANGES`
Date: 2026-10-24 JST
Repository: `eariver/japanese-generative-ai-survey`
Reviewed Muse r2 exact HEAD: `ab69aed74c1c6418ece2842796830134d63fbc30`
Reviewed root Tree: `dda0b894194a6ee27cebc11dea458cc7bc167e3d`
Reviewed main: `041a08dfef3112643cbf85b4a86a7b6f9128aed6` / Tree `a134dc36a407d08ab1de416324229b3955e0325a`
Frozen Core v2: `774dd39a951c9ac3818e83dfffd4c7666efb0a20` / Tree `cd46a6f7a6dcc4031e76220cea4c52c7dd1fc481`

This is an edition-local Sol **editorial** ruling, not independent Sol audit or Human Gate.

## 1. Positive findings

- Muse r2 respected exact remote HEAD/Tree, protected Frozen Core and 2 Human Gates. The commit is a normal descendant of the r2 instruction, changes are W43 edition-local only. W43 State remains `ISSUE_INITIALIZED`, all checkpoints pending; no spurious `ADVANCE_STAGE`.
- Proposal grows from 36 to 51 IDs; 15 new records cover r1 important omissions (OpenAI training containment, biology agents, low-resource languages; 1Password agent credential plane; MOSS trainer/report distribution/API; MemT, Ming), and separate pre-window release vs in-window availability/revision events.
- Consumption notes provide substantive mechanisms, baselines, conditions, numerical results and caveats, materially beyond r1 claim-level source locators. Muse specifically distinguishes **rendered markdown read** from original HTML byte-archival, and reports zero independent reproductions.
- Kimi public X HTML is archived and the corrected UTC clock `2026-10-23T17:15:24Z` is documented. arXiv version UTC timestamps disambiguate original out-of-window vs revision in-window.
- W42 seven HOLD/five INSPECT preserved without automatic promotion; X manifest still `AWAITING_GROK`. Google Drive folder `Grok_X_SourseIntake/Weekly/2026-W43/weekly-x-2026-W43` was read as of this review; only `grok-task.md` is present, **no Grok result**.

**Editorial coverage result: `SUBSTANTIALLY IMPROVED / RESEARCH PASS WITH OPEN RISKS`. Formal Discovery readiness: NOT ACCEPTED due to the blockers below. Do not repeat the whole Source Intake sweep.**

## 2. Blocking normalization/provenance issues

### W43-DC2-01 — Contradictory active Discovery graph (BLOCKING)
`discovery/discovery-v2-proposal-r2.jsonl` has 51 IDs, including **all 36 r1 records unmodified** plus 15 appended. As a result, canonical r2 still contains:
- `w43-primary-kimi-20261023` with stale claim "API live Oct 23 **21:15Z**", while `w43-r2-kimi-corrected-20261023` separately says **17:15:24Z**. This is ONE announcement/API event, not two independent candidates.
- `w43-lead-ambench-20261016` "time unproven" together with separate `w43-r2-ambench-v2-20261020`; the original v1's actual UTC OUT and possible substantive v2 revision must be expressed consistently by event/version.
- `w43-lead-orlicense-20261016` "time unproven" next to `w43-r2-out-orlicense-20261016` with proven 18:13:25Z OUT.
- `w43-primary-nemotron-e4b-20261023` still points to r1 claim-only bundle, even though r2 body corrected E4B context length to 64K (rather than 1M attributed to a different family).

A schema PASS / unique discovery IDs does **not** prove event-family deduplication or consistency. `BASE` + no parent references on r2 correction IDs also fails to encode their relationship to r1 originals. **Do not accept the 51 records as 51 distinct meaningful discovery events**.

Required: produce one coherent active r3 canonical proposal; retain r1 and r2 files as immutable historical proposals. Preserve stable identity for a corrected event where possible; apply factual amendments to its active row, bind r2 evidence source(s), and remove/reclassify redundant correction rows or explicitly prove genuinely distinct event identities. For version/announcement events, show exact parent/version lineage, no double counting. Give a reconciliation table mapping old 51 IDs → corrected active IDs/dispositions. Validate graph, raw_paths, dedup and chronology, not only JSON schema.

### W43-DC2-02 — Time/provenance integrity (BLOCKING)
- GitHub r1 commit `57afcd292d946078ae03900bd242b6f0b4f7de60` was committed **2026-10-24T11:20:22Z**, yet its 36 Discovery rows uniformly report `source.observed_at: 2026-10-24T12:00:00Z`, **39m38s after** the commit that already contains them. r1 source bundle headers also use `12:00Z`.
- r2 commit `ab69aed74c1c6418ece2842796830134d63fbc30` was committed **2026-10-24T11:56:58Z**, yet the collector run ID / folder `20261024T133000Z-muse-r2` purports to use `13:30Z`, **1h33m02s after** the commit. r2 ledgers separately say `observed_at: 11:50Z`, plausible; nevertheless run naming misrepresents chronology unless explicitly stated to be an opaque synthetic label.
- Five files called "raw GitHub API JSON" each comprise a brief six-key projection (~240 bytes), not a demonstrated byte-for-byte full GitHub API HTTP response. Treat them as `API_FIELD_PROJECTION` unless exact body provenance and bytes prove otherwise. Do not call these full original API raw bytes. The archived Kimi X HTML is different: raw page bytes appear present, with original content to verify.

Required: independently audit actual collector event logs / system clock, annotate the impossible r1 observed_at and r2 future-coded run ID **without falsifying historical source bytes**. Correct active Discovery records from logged original observed times when provable; if no clock evidence exists, perform new truthful bounded re-observation with recorded real UTC and label prior fields invalid/unknown. Keep historical r1/r2 as immutable evidence and create an explicit errata/provenance bridge. Never silently pretend `Git commit time` is an actual observation time. For r2 run ID, if retaining literal label, mark it an opaque misleading identifier (not real execution UTC); create an exact correction record. For six-key JSON, name the extraction method and call it a projection unless complete original bytes are available.

### W43-DC2-03 — Grok/X mandatory acceptance dependency (BLOCKING FOR STAGE, not reason to redo r2)
W43 Weekly policy requires a fresh Grok/X result. Google Drive transport task exists:
https://docs.google.com/document/d/1BubHtxps3Lg711pDJKfoNwe8AyeND7miT9hMQwSnsjw/edit
The actual result `weekly-x-2026-W43.md` is not in the designated Drive run folder as of this review. `x-source-intake-v2.json` is `AWAITING_GROK`, correct. Sol must receive/import/validate result when available; Muse must not synthesize it. No accepted Discovery/checkpoint or Screening until it is complete and reviewed.

## 3. Nonblocking follow-ups for Evidence phase

- AM-Bench v2 substantive delta is unchecked; leave HOLD/background until verified, do not call the original v1 a fresh W43 discovery.
- Most material bodies were read in rendered form, with note-level paraphrases; few source originals captured as immutable bytes. The 19 rendered-consumption count is a worker-reported methodological count, not 19 independent raw captures.
- Weight/model-card and exact license bytes not fully acquired; some product/model benchmarks remain vendor-only and independent reproductions zero. Core Evidence stage MUST verify important claims before Selection, and may reject any missing authority; not necessarily a blocker to provisional Discovery candidate coverage.
- Robotics/pretraining lanes remain thin, but limited non-coverage is disclosed and does not justify endless Discovery rounds if a bounded sweep has no credible in-window primary technical event.

## 4. Sol decision

`LIMITED_REQUEST_CHANGES`: one **r3 metadata/dedup/provenance correction only**, not a new broad research round. Preserve all r1/r2 archived files; create r3 active proposal and explicit reconciliation/errata. Stop at `SOL_DISCOVERY_COMPLETENESS_REVIEW_READY_R3`. No `ADVANCE_STAGE`, Screening, Evidence, Selection, Human Gate, or Frozen Core modifications.

Sol may determine provisional research completeness after r3; canonical Discovery acceptance additionally depends on genuine Grok result and required trusted operator workflow.
