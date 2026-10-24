# W43 Sol → Muse — Core v2 Screening r1 (accepted Discovery → Screening acceptance only)

Status: `EXECUTION_CONTRACT / BOUNDED_SCREENING / STOP_BEFORE_STAGE_ADVANCE`
Date: 2026-10-25 JST
Repository: `eariver/japanese-generative-ai-survey`
Existing branch only: `weekly/2026-W43-v2-work`

**Exact Starting HEAD and Root Tree are supplied in the dispatch message after this instruction/index are committed.** Preflight read-only check of 6 remote identity values:
- W43 work branch HEAD and Root Tree: dispatch values (MUST match exactly).
- Reviewed main HEAD `041a08dfef3112643cbf85b4a86a7b6f9128aed6`, Root Tree `a134dc36a407d08ab1de416324229b3955e0325a`.
- Frozen Core branch HEAD `774dd39a951c9ac3818e83dfffd4c7666efb0a20`, Root Tree `cd46a6f7a6dcc4031e76220cea4c52c7dd1fc481`.

Any mismatch → **ZERO WRITES, stop, report expected vs actual**. No fallback/new/review/repair branches, no reset/rebase/force push.

## 1. Current authorized authority

- Trusted operator request `sources/2026-W43/execution/requests/sol-w43-discovery-advance-20261025.json`, request commit `e67099d534cb2975e111592d00fe0e626a6ea07a`, Issue #448 executed via workflow run `40116386580` (preflight and execute PASS).
- Authoritative machine State `sources/2026-W43/production-state.json`: **`DISCOVERY_COLLECTED`**, next `stage:screening`, Discovery machine checkpoint `passed`; both Human Gates pending.
- Trusted stage commit `ab30004ead9aea480fac8c243d98af92925dcfa9`, Root Tree `be512ea8a7e76a9ebdf1bc4f23c7462dd85005e3`; `orchestration/v2/checkpoints/ISSUE_INITIALIZED.json` contains Discovery acceptance SHA256 `edad13b1a90fa4965fe2ef37f9ce522c110ffed7727d839e4e62fde04ec93f1b`.
- Accepted authority `sources/2026-W43/discovery/discovery-accepted-v2.json`: **51 normalized records**, graph SHA256 `5a94b7574b9d59f05bd82e00cb464512b359a45eae00a2721b1d119abc4bd43a`. Root source `discovery/discovery-v2.jsonl` immutable, sha256 `f62d8459b18bba9e939db3547a24c56722b7d59c97e7dc609cd3be6a42907ae2`.
- X manifest `external/x/x-source-intake-v2.json`: `COMPLETE` registration of genuine Grok `PARTIAL` observation; raw `weekly-x-2026-W43.md` sha256 `4571e0de469a7143fb1c46710c2e419a91404ff2d9538ae4d9a31a8b8f0be54a`. Vendor performance claims and most X post IDs NOT independently reproduced. This is not Editorial Selection.

## 2. Mission — exactly 51 complete provenance-bound Screening decisions

Read frozen Core v2 contract **from existing protected main**:
- `config/prompts/source-screening-v2.md`
- `scripts/survey_screening_v2.py`
- `schemas/screening-v2-run-package.schema.json`
- `schemas/screening-v2-batch-result.schema.json`
- `scripts/survey_stage_validation_v2.py` (screening stage)
- W42 accepted Screening flow in `sources/2026-W42/screening/v2/` strictly as mechanical precedent, never as W43 editorial authority.

Apply production Profile WEEKLY research question and exact ordinary period UTC `[2026-10-16T22:00:00Z, 2026-10-23T22:00:00Z)`. Do not use a fixed A–L lane list, quota, arbitrary minimum KEEP count, or article Selection. Do not synthesize prose/draft.

Use official `survey_screening_v2.py prepare` on **exact accepted W43 Discovery** and verified `DISCOVERY_COLLECTED` State; create a new W43 Screening package under `screening/v2/packages/r1`, preferably memory-safe batches (e.g. ≤12–15 records per batch, Core batch/hash rules respected). For EVERY record, emit exactly one schema-valid decision `KEEP / MAYBE / DROP / INSPECT`, reason, profile-derived free-form scope_tags, duplicate_group or null, concrete verification_targets, low/medium/high confidence. Preserve original IDs and exact input/result basis SHA. Never omit an ID, alter Source Intake, or invent authority beyond accepted records.

## 3. Critical editorial disposition rules

- Strict chronology: distinguish IN ordinary release, IN version/revision/integration, OUT original event, after-window observation, and W42 carry-over. Original **Beam weights Oct16 13:01Z OUT**, Muse Spark initial weights Oct15 OUT, MOSS-Image base/weights Oct16 pre-window OUT, DeepInfer initial repo Oct16 pre-window OUT, AM-Bench v1/OR-License pre-window OUT. Their distinct Oct17–23 trainer/API/announcement or arXiv v2 may be in-window ONLY when independently traceable as distinct events.
- Treat exact Grok sensor ledger `w43-r4-grok-x-ledger-20261024` as **X provenance/audit binder** (`source_type=X_OBSERVATION`), not a new technology launched Oct24 or first-party technical performance source. It receives a normal explicit Screening decision, with provenance role and verification limits, but MUST NOT inflate technical candidate ranking or release-family counts.
- Flint Oct21 verified official Recursive/HF weights is **one technical event**, Grok is corroborating observation and not a second release. Keep separate if material. Kimi Oct23 API live is IN, promised Nov4 weights **not** currently available; model vendor performance claims are unreplicated; no invented local run.
- OpenAI Oct19/21/23 primary studies, 1Password agent credential boundary, MemT GDN-2/MoS, MOSS trainer/API, DeepSeek 1017, Nemotron Bolt E4B **64K** context, Voxtral/Eleven audio, FLUX video and other source families must be assessed as independent technical candidates; don't favor X signal frequency over technical novelty.
- The **12 W42 HOLD/INSPECT carry-over** records must all receive an explicit disposition. Do not silently promote uncertain names/claims, red-date earlier releases, or drop them solely to reduce count. Distinguish prior unresolved identity vs substantive new weekly material.
- Evidence targets should be concrete (e.g. vendor-vs-independent benchmark baseline/denominator, full license/weight/card bytes, edition-window timestamp, security/safety conditions, reproducible repository/harness config, AM-Bench v2 change significance, empirical scope of robotics & memory). `KEEP` permits later Evidence scrutiny, NOT proof; `INSPECT/MAYBE` preserves unresolved sources; `DROP` is justified only for profile scope/duplicative noise/insufficient credible relevance and must be recorded.
- Avoid previous errors: no future `observed_at` placeholders, no fake raw GitHub API bytes (r2 API metadata are field projections), no mistakenly classified Grok sensor source; never repair original historical source records to hide provenance defects.

## 4. Mechanical acceptance and QA

- Write one result JSON file per expected package batch using exact Core schema, complete decision count, no extra/missing IDs, exact basis hashes. Evaluate decisions using real accepted content, not generic boilerplate.
- Run official `survey_screening_v2.py accept` into content-addressed `sources/2026-W43/screening/v2/accepted/<result_set_sha256>/screening-accepted.json`. Validate accepted result set via Core `validate_acceptance` and run `survey_stage_validation_v2` precheck where safely possible **without altering State**.
- Record a Sol-facing summary: 51 decisions grouped KEEP/MAYBE/DROP/INSPECT; weak/OUT/carry-over counts, duplicate groups, exact high-priority verification targets, any conflict with immutable Discovery/Source Intake; data volume and original raw/source count separately, no conflation.
- Track all batch IDs, SHA256s, exact accepted path, package SHA, input graph binding, actual CLI stdout+exit codes, source-to-screening identity, remote Git HEAD and Root Tree.
- Update W43 edition-local `execution/index.md`, add one proper session record and `execution/SOL_SCREENING_REVIEW_HANDOFF-r1.md` (no new editorial Human Gate review file). Re-run Core `survey_execution_record_v2.py` validate.
- Failure of Core acceptance, missing source/raw, duplicate ID, impossible timestamp, graph drift or other validation = STOP / report `BLOCKED` with truthful diagnostics; never mark PASS by manual edits.

## 5. Hard boundaries and stop

- **Do NOT `ADVANCE_STAGE`, issue operator request, or change `production-state.json` / `orchestration/v2/checkpoints`.** Sol will independently review complete Screening and request trusted Stage movement later.
- Do not run Evidence or downstream materiality/completeness/Selection/Architecture; those are later bounded contracts.
- No W42 mutation; no `AGENTS.md` change; no protected .github/config/schemas/scripts/tests, Frozen Core or main changes; no Human Gate creation, no PDF/Release.
- No extra branch. Normal edition-local commits and non-force push only with readback.
- Stop at `SOL_SCREENING_REVIEW_READY_R1`. Report final remote HEAD+Root Tree, exact content-addressed Screening acceptance path, decision distribution, Validation, missing authority and remaining risks.
