# W41 Sol Independent Evidence Authority-Consumption Review r1

Date: 2026-10-12 JST
Status: `DISCOVERY_SCREENING_PASS / EVIDENCE_SUBSTANCE_PARTIAL_PASS / EVIDENCE_AUTHORITY_BINDING_REVISION_REQUIRED / NO_EVIDENCE_ACCEPTANCE`

Exact reviewed HEAD: `fa7f7a5b091e5edea539b1ea91728b53f4656279`
Exact reviewed Tree: `1395dfae6277416d000920f646530aebc5e22266`
Work branch: `weekly/2026-W41-v2-work`
Reviewed main SHA/Tree: `83f581ebc0dd8945ca7116f65bf6b853ca1fe6c8` / `31c0adc5b57761e5073d100554279a8adc5a18f4`
Frozen Core SHA/Tree: `774dd39a951c9ac3818e83dfffd4c7666efb0a20` / `cd46a6f7a6dcc4031e76220cea4c52c7dd1fc481`

## Stage/identity verdict

- From Sol r2d instruction SHA `1f497fb5f2425b58d524bf9738e1f76cb2075e3e` to reviewed HEAD: 2 normal commits, 135 W41-edition-local files, zero out-of-edition changes. Last commit is handoff/session closure only. Remote main/Core unchanged.
- Exact W41 State: `CANDIDATES_NORMALIZED / stage:evidence-materiality-completeness`; Discovery and Screening checkpoints PASS, Evidence/Materiality/Completeness/Selection/Architecture pending, both Human gates pending.
- Discovery Acceptance: 37 unique records, graph `ce99f523cc43044623240141ccb705ec798935ac50ec7cb481d77d78921f5428`, X Manifest source SHA `e49a67cdec1fa69acbfc7b50597c6476eac942ab8b79858ca7d0562da61548c7`; accepted Screening: 37 records (KEEP19, INSPECT15, MAYBE2, DROP1). Canonical stage-validation artifacts report PASS and actual State is advanced.
- Evidence r1 package: 36 tasks/cards/provisional views; Evidence input statuses VERIFIED3/PARTIAL21/NEEDS_MORE12; proposed materiality MATERIAL21/HOLD13/CONTEXT2. No accepted Evidence manifest/checkpoint exists. Stopping boundary correctly respected.
- Partial first-party content actually consumed: OpenAI textGrain and API changelog direct Muse reads; three delegated bundles summarize original OpenAI, Google/Anthropic and open-weight/vendor sources. Sources are claim-level/delegated excerpts, not original-byte HTML archives. Independent Sol spot-reading of original OpenAI Oct5 text provenance, Google DeepMind Nano Banana 2.1 model card, and Cloudflare Oct9 Clef-omni blog supports major headline/release-scope facts; publisher metrics remain vendor assertions.

## Blocking findings

**SC-E41-01 / CORE SOURCE CLASS COMPATIBILITY — BLOCKER**
Frozen `scripts/survey_evidence_v2.py::SOURCE_CLASS_MAP` has NO key `SECONDARY_OBSERVATION`. Nine W41 accepted Discovery sources have this type. The frozen unmodified task source-binding path raises `unsupported source_type`. Muse explicitly generated nine draft cards using a narrow runtime-only fallback to `SECONDARY`. This is NOT a valid canonical Evidence acceptance path. The nine sources include Agr, Nemotron HF distribution, Nace Drex/NDI, ElevenLabs, Tencent HOLD, Pixel Canary and TBC Video HOLD, and ELYZA pre-window. No Core patch is authorized. W40 previously documented and reviewed bounded edition-local derived-task source-class projection as a possible precedent, **not an automatic permission to change W41 accepted Discovery or task authority**. Investigate and independently prove a W41-only source-equivalent projection mapping exactly `SECONDARY_OBSERVATION -> SECONDARY` for these nine and no other values, with a typed provenance ledger, deterministic hashes, unknown-type negative tests, and real frozen-Core task/binding validator PASS; STOP if it cannot be expressed lawfully.

**SC-E41-02 / PRIMARY MATERIAL ACTUALLY READ IS NOT BOUND TO CARD — BLOCKER**
At least these real Card examples use only the old Discovery `src-1` locator as authority for subsequently retrieved FIRST-PARTY research:
- `w41-x-nanobanana21-20261006`: Card claims Google DeepMind model-card details but its sole source URL is `grok-task:weekly-x-2026-W41#11` with `source_class=SOCIAL`.
- `w41-dailyx-synthid-portal-20261008`: Card claims Google official blog content, but sole source URL is a GoogleAI X post with `source_class=SOCIAL`.
- `w41-dailyx-nace-drex-20261010`: Card asserts product-page details, but sole source is a secondary X locator. The original technical launch article is dated Sep24/28, not necessarily a newly released W41 model.
The source notes under `collectors/evidence/runs/20261012T003000Z-muse-r3` are not task-bound Evidence Authority Supplements in r1. A prose mention of a model card or fetch bundle is not an accepted source binding. Build edition-local, issuer-URL/version/claim-bound excerpts, SHA/byte-accurate source entries, and use frozen Core's `build_evidence_authority_supplement` / `validate_evidence_authority_supplement` to add PRIMARY source IDs to the correct task. Revise Card `source_ids` for claims that rely on those sources. Do not turn unverified X claims into publisher-proven statements.

**SC-E41-03 / VERIFICATION TARGET OVERSTATEMENT AND TECHNICAL DEPTH — REQUIRED**
Review all 36 Cards, especially 21 MATERIAL candidates. Example: Clef-omni Card target `weight-repo-status=VERIFIED` while finding says only vendor states HF open weights and download was not verified. Relabel as issuer claim / unresolved actual downloadable bytes. The Decisions API Card has `status=VERIFIED` but price `UNRESOLVED`; scope VERIFIED to official changelog features rather than pricing. Distinguish dated release, API/router preview, source availability, card/license/benchmark, actual independent measurements and promised future weight files. The textGrain technical-report PDF is linked but unread; avoid publishing method internals based on secondhand excerpts without consuming the actual PDF. Prioritize primary body + methodology for highly material items before quality approval. An edition-local sample source note is NOT a one-to-one complete original-source corpus.

**SC-E41-04 / HOLD AND CUTOFF — REQUIRED**
Keep W40 inherited four HOLDs; Microsoft Decision-1 Oct9 official day-only still TIME_UNRESOLVED; Tencent month-only upload still HOLD; Anthropic unintended-actions Oct9 X post is after 22:00Z; Cloudflare Clef-omni *official blog* 18:27:34Z is in-window even though later X was out-of-window. Maintain exact split. Do not conflate post-time with original event-time. Nace Drex original GA Sep24 with Oct9 renewed vendor post: require new W41 technological change before normal-release role.

## Decision and authorized next step

The 37-record Discovery and 37-record Screening CANONICAL checkpoints are not reopened by this review. W41 Evidence has useful technical material but **is not approved for acceptance**. Approve a bounded W41 edition-local preacceptance r4 source-binding/compatibility substantiation and material-claim correction, modeled narrowly on W40's approved derived Task + source supplement pattern. The W40 precedent is not a new Core implementation. Keep original r1 package/cards and historical accepted Discovery/Screening untouched. No generic rerun of discovery or screening, no new branch, no Core/workflow/schema/config modifications.

The next unit must: (1) prove whether the nine-way projection is legally reproducible under **unmodified Core** without changing Discovery/Screening; (2) bind consumed first-party materials by genuine validated supplements; (3) re-create independent 36/36 candidate Task/Card set with source classes/claims correctly attached; (4) run all frozen Core task-source/card/package validators and record failures; (5) stop BEFORE `accept_evidence_results`, Views Acceptance, Evidence/Materiality/Completeness State transition, Selection, Architecture, or Human Gate. If source mapping remains blocked, report `CORE_COMPATIBILITY_BLOCKED` and separately defer the Core repair rather than hiding the incompatibility.

Result: `EVIDENCE_R1_REVIEW_PARTIAL_PASS / EDITION_LOCAL_BINDING_REPAIR_REQUIRED`.
