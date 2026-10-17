# Defect CV2-W42-002 — closed Evidence source_type vocabulary vs proposal-legal types (shared-Core, frozen)

Exact affected tasks (17): `COMMUNITY_BLOG_LINKED`(lfm25), `COMMUNITY_LEAD`×3(qwen-turbo, sulphur2, splashboard), `COMMUNITY_PRICE_PAGE`(rosalind-discovery), `COMMUNITY_ROUNDUP`(oss-roundup), `DEV_POST`(aspire), `PAPER_LEAD`×4(agenthorizon, sakana-mlr, harness-paper, amazon-worldmodel), `SECONDARY_CLAIM`(fish-drama3), `SECONDARY_VENDOR_ROUNDUP`(aws-bedrock), `X_OBSERVATION`×3(grok-purchasing, ms-decision1-carry, grok-scale), `X_VENDOR_STATEMENT`(openai-security). Census re-derived 2026-10-17; the '18' in session notes was an addition slip, corrected here.

Date: 2026-10-17 JST. Session: muse r7. Severity: BLOCKING (Unit B).

## Observation
`survey_evidence_v2.task_authority_sources` eagerly applies closed `SOURCE_CLASS_MAP` to every task's discovery `source_type`. 17 of 50 canonical W42 Discovery records use proposal-legal but Evidence-unmapped types (`X_OBSERVATION`×3, `PAPER_LEAD`×4, `COMMUNITY_LEAD`×3, `X_VENDOR_STATEMENT`, `COMMUNITY_BLOG_LINKED`, `COMMUNITY_PRICE_PAGE`, `COMMUNITY_ROUNDUP`, `DEV_POST`, `SECONDARY_CLAIM`, `SECONDARY_VENDOR_ROUNDUP`). Any Core-schema Evidence card on those tasks raises before claim checks run. Supplement manifests cannot cure it (same eager evaluation). Affected discovery IDs: see exact census above (17 tasks).

 census method: `discovery-v2.jsonl` source_type values checked against frozen `SOURCE_CLASS_MAP`; script output archived in session log. Sol may re-derive independently before authorizing regen.

## Reproduction boundary
Pure function of frozen map + accepted bytes; deterministic. Discovery acceptance itself does not check source_type (built fine); Screening ignores it; only Evidence card validation enforces it.

## Impact
Even with defect 001 fixed, 17 tasks need vocabulary remediation before Core Evidence acceptance.

## Safe edition-local workaround
None without waiver. NOT worked around (no silent type rewriting — that would mutate accepted Discovery + Screening + checkpoints + state, requiring a Human-gated rewind).

## Core-maintenance pointer (separate track)
Either (a) extend the closed map with the proposal-legal X/community/paper/dev/secondary strings (mapping to SOCIAL/SECONDARY/PRIMARY_PAPER by provenance semantics), or (b) Sol-gated bounded upstream regeneration normalizing the 18 strings (meaning-preserving, e.g. X_*/COMMUNITY_*→SOCIAL, SECONDARY_*→SECONDARY) with full re-acceptance + checkpoint re-advance through the Human-gated revision path.

## Production disposition
Blocked with concrete error; remediation option (b) proposed for Sol/Human decision. r7 provisional sketch (below) derives from UNACCEPTED r7 cards and carries no authority.
