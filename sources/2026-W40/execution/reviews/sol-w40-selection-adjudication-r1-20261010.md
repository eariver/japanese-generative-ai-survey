# Sol W40 Independent Selection Audit — adjudication r1

Status: **SOL_SELECTION_REVISION_REQUIRED / BOUNDED_MUSE_R10**  
Date: 2026-10-10 JST  
Repository: `eariver/japanese-generative-ai-survey`  
Branch: `weekly/2026-W40-v2-work`  
Reviewed Muse r9 HEAD: `e2940790ede6f29796f3b9885e7262fd3c086622`; Tree: `36881abe1aeebf742d1e5af15fd9c9d92cf59652`  
Reviewed main SHA: `afdb3df3faa20af3bb5798be429bba8dbd2100b1`  
External independent audit: `sources/2026-W40/execution/reviews/independent-selection-audit-w40-r9-20261010.md` (original attachment SHA-256 `31384bf92e6825efa29d1d5add6b28122ca8f6e19a951ac45d4d52e1a1c67278`).  
Fixed period: `[2026-09-25T22:00:00Z, 2026-10-02T22:00:00Z)`.

## Assessment

Adopt independent reviewer verdict `SELECTION_REVISION_REQUIRED`. The reviewer found Git/Stage Integrity PASS from repository-saved authority and preserved 37 accepted Discovery, 37 Screening, 35 Evidence (29 VERIFIED/6 PARTIAL), 35 Edition Views (29 MATERIAL/4 HOLD/2 CONTEXT), 37 Materiality Ledger (+2 EXCLUDED) and LIMITED Completeness with 11 residuals. Its report is **read-only**, not evidence of fresh execution of all deterministic tests. Remote Core State remains `EVIDENCE_REVIEWED`, next `stage:selection`, Selection/Architecture/Human pending. **No Core rollback/rewrite is authorized.**

Sol independently checked frozen `main`:
- `schemas/candidate-selection-v2.schema.json` requires `ESTABLISHED` status, only its listed 9 fields, basis `candidate_matrix_sha256`, numeric-object `summary`;
- `schemas/candidate-matrix-v2.schema.json` requires exact Evidence/View/Materiality/Completeness SHA basis and derived candidate IDs;
- `scripts/survey_architecture_v2_base.py::validate_selection` requires assignment of all Matrix candidates exactly once; non-SELECTED uses `architecture_usage=NONE` and both roles null; SELECTED needs namespaced roles and valid PRIMARY/SUPPORTING;
- `scripts/survey_completeness_v2.py::validate_profile_completeness` requires every Discovery record declaring a named obligation to be traceable in its `discovery_ids`. Thus 37-item traceability differs from task-based **31/29/2** substantive scopes.

## Adjudicated findings

**F-W40-S01 [MAJOR/BLOCKING Selection semantics]:** r9 `selection-proposal-r9.json` has **35 assignments, 28 SELECTED = 20 PRIMARY / 8 SUPPORTING, 1 INSPECT, 4 HOLD, 2 REJECT** but prose summary says **23 PRIMARY / 5 SUPPORTING**. Fix new r10 reviewer proposal and dossier using reproducible counts; preserve r9 as history.

**F-W40-S02 [MAJOR/BLOCKING formal Core Selection]:** r9 reviewer proposal is not a Core Candidate Selection; it has custom `candidate_discovery_map`, text summary, `basis.candidate_matrix_sha256=null`, human-readable candidate IDs, DGX `architecture_usage=INSPECT`. New Core-valid candidate matrix/selection preview must use true hashes, schema fields/IDs, numeric counts, and nonselected NONE. **Do not re-label the r9 proposal as formally accepted.**

**F-W40-T01 [MAJOR/high priority targeted research]:** Oct2 Ai2 AstaBrief 8B and ServiceNow AutoSynthData remain `HOLD/TIME_UNRESOLVED`. Original Oct2 dates alone do not prove before the 22:00Z exclusive boundary. External RSS `2026-10-02T04:01:31Z` for AutoSynthData is an **unverified secondary clue**, not accepted first-party proof. Search publisher-original RSS/Atom, release/tag/commit, changelog version, archival first-publication instants; distinguish event release, publication, update and feed ingest. Cloudflare Oct2 Web Search API and Pi Durable Harness are two further credible, **not-yet-canonical** technical announcement leads with unproven exact hour. If a materially eligible in-window source emerges, **stop for Sol canonical-scope decision**, do not mutate already accepted Discovery/Screening/Evidence/Materiality or Selection silently.

**F-W40-E01 [MAJOR/technical depth]:** deepen actual source consumption, especially Ai2 Olmo-core 3 technical report (prior 5MB fetch failure; use official segmented HTML/PDF/docs/code), and bounded CLM appendices, ProvenanceGuard v2 remainder, FLUX 3 Image model/release/license materials and Cloudflare MCP Auth specification. Record exact consumed sections/metrics/limitations, vendor attribution and what remains unread. Existing canonical Card changes require separately reviewed upstream amendment, not r10 overwrite.

**F-W40-A01 [MAJOR/anti-compression]:** P6 currently aggregates ContextLM, Olmo-core 3, AgentPerf, Open TTS and RL Environments under `medium`, risking loss of methods, ablations and evaluation scope. Split P6 into training-methods/systems vs evaluation/execution infrastructure, or demonstrate meaningful independent subsections/tables with relative space. P2 should separate Holo4 general agents vs Japanese-specialist ELYZA; P5 distinct runtime safety, governance, bio watermark, provenance, MCP auth; P7 image/video/audio vs observability; P8 has no PRIMARY, prefer short digest. Depth over arbitrary page minimization.

**F-W40-N01 [MINOR/conditional]:** Cloudflare two Oct2 first-party calendar entries need first-original UTC time before W40 inclusion; check topic/overlap only if date proven.

**F-W40-C01 [MINOR/no Stage rollback]:** historical checkpoint summary/reviews mention MATERIAL30 while canonical authority MATERIAL29. Free-text nonauthority erratum only. Preserve checkpoint SHA; log correction in r10 and future dossiers.

**F-W40-C02 [NOTE/no correction required]:** Completeness all 37 Discovery IDs result from frozen Core provenance obligation traceability; substantive obligations bound by 31/29/2 Evidence Tasks. Explicitly distinguish in Selection and Architecture.

## Guardrails and next decision

Freeze **accepted upstream Core Stage `EVIDENCE_REVIEWED`**, Human Gates pending, Core CV2-DM-016 OPEN. The independent reviewer did not find grounds for `SELECTION_HOLD` requiring global reintake; `SELECTION_REVISION_REQUIRED` warrants bounded r10 corrections only.

Muse r10 must produce a full corrected proposal, exact Core Candidate Matrix crosswalk/preview, four bounded time investigations, five targeted technical-primary consumption logs, and an information-dense alternative package plan. If time proof or new original method evidence materially changes accepted candidates, return a **separate upstream-delta report and STOP** pending Sol direction; otherwise stop at fresh Sol Selection Semantic Review. **No formal Selection Acceptance, `SELECTION_COMPLETE`, Architecture, Human decision or Publication.**

Next Muse contract: `sources/2026-W40/execution/instructions/2026-10-10_muse-w40-selection-audit-bounded-revision-r10.md`.
