# Retrieval provenance (edition-local carry-over verification note, secondary excerpts)
- verification_date: 2026-09-19T00:00:00Z (worker websearch excerpts; primary DeepSeek docs not refetched in this pass)
- collector_id: secondary-websearch
- collector_run_id: w38-carryover-20260919-r1
- external_parents:
  - external:2026-W37:w37-primary-deepseek-v41-flash-20260910
  - external:2026-W37:w37-primary-deepseek-api-20260910
- authority_class: SECONDARY (press + tracker excerpts; primary docs re-verification still open)

# W38 carry-over verification: DeepSeek V4-Pro -> V4.1-Flash routing (occurred Sep 14)

## Findings
- The routing cutover announced pre-window (Sep 10) OCCURRED in-window: from 04:00 UTC Sep 14, 2026 every deepseek-v4-pro request is served by V4.1-Flash at Flash pricing until V4.1-Pro ships (Pandaily Sep 14; TNW Sep 10 pre-announcement; Apidog migration guide Sep 14; hi-tech.ua Sep 13).
- V4.1-Pro has NOT launched as of this verification (no date published; orcarouter Sep 9 leak-discussion notes "until V4.1-Pro goes live" as future condition; platform.deepseek.com still markets V4-Pro agent/Responses capability).
- V4.1-Flash: 552B MoE, asymmetric Causal-Encoder-Decoder (8B encoder/16B decoder active), MIT weights on Hugging Face, native image input, Transformers/vLLM/SGLang support (per aibase Sep 10 + hi-tech.ua Sep 13, secondary).
- Practical impact (Pandaily): Pro-ID traffic inherits Flash peak/off-peak tables; operators must regress against deepseek-flash, update monitoring/cost dashboards, treat deepseek-v4-pro as deprecated routing.

## W38 disposition
- Occurrence in-window (Sep 14 04:00Z) is VERIFIED at secondary level; primary-docs confirmation (api-docs.deepseek.com changelog/models page capture) remains OPEN gap.
- Evidence status: PARTIAL (secondary-only). Selection: CONTEXT at most (serving/systems operational note, H lane); NOT a new model release.
- Do NOT claim V4.1-Pro launch, pricing, or retirement of Pro weights beyond routing.

# W38 carry-over verification: GLM-5.5 rumor (rechecked absence)

## Findings
- No official Z.ai announcement of GLM-5.5 as of latest checked sources (glm5.app tracker Aug 12: "not released, zero official announcements"; felloai Jul 3: CGTN June-30 "expected August" is sole timing basis; ofox Aug 14-19: GLM-5.3 shipped Aug 14 as post-training refresh of 5.2, weights pending).
- Name "GLM 5.5" is community shorthand, unconfirmed by Z.ai. Current flagship per checked pages: GLM-5.3 (API) / GLM-5.2 (weights MIT).
- W38 window: no in-window GLM-5.x release evidenced. Re-verification check SATISFIED as negative finding.

## W38 disposition
- DROP (rumor-only, absence re-verified). Record explicitly; do not carry further.
