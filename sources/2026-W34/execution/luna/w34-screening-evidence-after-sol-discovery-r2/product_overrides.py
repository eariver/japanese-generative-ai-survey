#!/usr/bin/env python3
"""Hand-written evidence specs for product/non-paper tasks after direct body reading.

Execution agent: Muse Spark 1.3 / EXPERIMENTAL_LUNA_ROLE_SUBSTITUTION
Each spec's claims/limitations/findings were written from the captured
supplement body (or local raw where noted). verification lists are positional
against the task's screening verification_targets.
Status/materiality rule (provisional, Sol reviews):
  NEEDS_MORE->HOLD; VERIFIED+KEEP->MATERIAL; VERIFIED+MAYBE/INSPECT->CONTEXT;
  PARTIAL->CONTEXT except chronology-sensitive PARTIAL->HOLD; maker-claim-heavy
  research/preview bodies->PARTIAL+CONTEXT even when KEEP-screened.
"""
from __future__ import annotations

# key: discovery_id -> spec
OVERRIDES: dict[str, dict] = {

"w34-event-c001": {
  "status": "PARTIAL", "materiality": "CONTEXT",
  "mat_r": "Provisional: GLM-5.3 release confirmed in-window via Z.ai changelog, but exact Aug 14 time vs 22:00Z boundary unresolved and coding-benchmark figures are vendor-reported; editorial weight is Sol's call.",
  "window": "MAIN_EVENT",
  "entity": ("zai-glm-5-3", "GLM-5.3", "MODEL", "Z.ai", "https://docs.z.ai/release-notes/new-released"),
  "artifact": "MODEL",
  "claims": [
    ("VENDOR_CLAIM", "Z.ai's release-notes body carries a 2026-08-18 GLM-5.3 entry describing stronger coding capabilities.", " dated changelog entry text; the Discovery basis cited an Aug 14 ZCode changelog entry, so entry-level dating differs."),
    ("VENDOR_CLAIM", "The same body claims roughly 50% gain over GLM-5.2 on Z.ai Code Bench and SOTA among compared models.", "Maker-reported benchmark figure; no independent reproduction in captured bytes."),
    ("PRIMARY_FACT", "The captured page also contains a 2026-08-26 GLM-5.3-Flash entry, which is post-cutoff and excluded from W34.", "Dated entry text; used only as an exclusion boundary."),
  ],
  "lims": [
    "Exact Aug 14 time vs 22:00Z W34-start boundary remains unresolved: captured entry is dated 2026-08-18 while the Discovery basis cited an Aug 14 ZCode changelog signal.",
    "Coding-benchmark figures (50% gain, SOTA) are Z.ai-reported with no methodology or independent reproduction in captured bytes.",
    "Aug 26 GLM-5.3-Flash content on the same page is post-cutoff and was not consumed as W34 evidence.",
  ],
  "verif": [("VERIFIED", "Release confirmed in captured Z.ai changelog body (Aug 18 entry with coding-capability description); exact Aug 14 time vs 22:00Z boundary still unresolved per limitation; W34 adoption/free-access/coding-agent delta retained for Sol materiality judgment.")],
},

"w34-event-c002": {
  "status": "VERIFIED", "materiality": "MATERIAL",
  "mat_r": "Provisional: first-party Anthropic article dated Aug 14 confirms token-choice watermarking for EU AI Act compliance; page-time precision is the only residual.",
  "window": "MAIN_EVENT",
  "entity": ("anthropic-claude-watermark", "Claude text watermarking", "PRODUCT", "Anthropic", "https://www.anthropic.com/news/claude-text-watermark"),
  "artifact": "PRODUCT",
  "claims": [
    ("VENDOR_CLAIM", "Anthropic's Aug 14 article states future Claude models will generate text containing a watermark to estimate likelihood of Claude involvement, implemented with other major providers for EU AI Act compliance.", "Article lede and summary bullets."),
    ("VENDOR_CLAIM", "The article states the method uses token-choice watermarking with no practical impact on output quality and no reader-distinguishable difference.", "Vendor mechanism description; no independent verification in captured bytes."),
    ("PRIMARY_FACT", "The article is dated Aug 14, 2026 on the page; no clock time is published.", "Page dateline text."),
  ],
  "lims": [
    "Exact page publication time vs the Aug 14 22:00Z W34-start boundary is unresolved: the page carries a date only.",
    "Watermark robustness/detection-tool claims are vendor-described; no independent test or detector in captured bytes.",
  ],
  "verif": [("VERIFIED", "Captured Anthropic first-party body confirms token-choice watermarking for EU AI Act compliance; ordinary-window X discussion corroborates timing; only exact page-time-vs-W34-start precision remains open.")],
},

"w34-event-c003": {
  "status": "VERIFIED", "materiality": "MATERIAL",
  "mat_r": "Provisional: both first-party pages confirm the Aug 19 Stripe-OpenRouter transaction/integration event; gateway scale figures are company-reported.",
  "window": "MAIN_EVENT",
  "entity": ("openrouter-stripe", "OpenRouter joining Stripe", "PRODUCT", "Stripe / OpenRouter", "https://stripe.com/newsroom/news/stripe-agrees-to-acquire-openrouter"),
  "artifact": "PRODUCT",
  "claims": [
    ("VENDOR_CLAIM", "Stripe's Aug 19 newsroom post states it agreed to acquire OpenRouter, a model gateway/routing platform.", "First-party announcement text."),
    ("VENDOR_CLAIM", "OpenRouter's companion post states it will continue operating with the same mission, name, product, and roadmap, and cites 10+ trillion tokens/day across 400+ models.", "Company-reported scale figures; not independently audited in captured bytes."),
  ],
  "lims": [
    "Transaction price/terms are not stated on either first-party page; widely reported $7-8B figures are press-reported and were not consumed as facts.",
    "Gateway scale figures (tokens/day, model counts) are company-reported without disclosed methodology in captured bytes.",
  ],
  "verif": [("VERIFIED", "Both first-party bodies confirm the Aug 19 transaction/integration event; model-gateway scale and routing-economics context confirmed as company-reported.")],
},

"w34-event-c004": {
  "status": "VERIFIED", "materiality": "MATERIAL",
  "mat_r": "Provisional: OpenAI first-party body confirms teen-specific experience, automatic age routing, safeguards, and Study Mode; core regression repaired (no generic unresolved placeholder).",
  "window": "MAIN_EVENT",
  "entity": ("openai-chatgpt-teens", "ChatGPT for Teens", "PRODUCT", "OpenAI", "https://openai.com/index/chatgpt-for-teens"),
  "artifact": "PRODUCT",
  "claims": [
    ("VENDOR_CLAIM", "OpenAI's page states users estimated under 18, or stating age 13-17, are automatically placed into ChatGPT for Teens.", "Age-routing statement in captured body."),
    ("VENDOR_CLAIM", "For under-18 users the page states age-appropriate safeguards that reduce exposure to harmful or developmentally inappropriate content while preserving learning/creation.", "Safeguards description in captured body."),
    ("VENDOR_CLAIM", "The captured body references Study Mode among teen-support features (12 mentions) alongside parental controls, the Under-18 Model Spec, Teen Safety Blueprint, and age prediction.", "Feature-list spans in captured body."),
  ],
  "lims": [
    "Effectiveness of age estimation and safeguards is vendor-described; no independent test data in captured bytes.",
    "Page publication date was not extracted from captured bytes; W34 timing rests on the Aug 18 first-observation record plus page content, not a captured dateline.",
  ],
  "verif": [("VERIFIED", "Captured OpenAI first-party body directly supports teen-specific experience, automatic age routing, stronger safeguards, and Study Mode; prior contradictory generic limitation is removed.")],
},

"w34-event-c005": {
  "status": "VERIFIED", "materiality": "MATERIAL",
  "mat_r": "Provisional: OpenAI first-party Aug 18 pacing post confirms frontier-RL slowdown, Astra Critical-cyber trigger, and containment/monitoring/alignment measures.",
  "window": "MAIN_EVENT",
  "entity": ("openai-frontier-pacing", "OpenAI frontier development pacing (Astra cyber)", "PRODUCT", "OpenAI", "https://openai.com/index/pacing-model-development-cyber-capabilities/"),
  "artifact": "SAFETY_EVENT",
  "claims": [
    ("VENDOR_CLAIM", "OpenAI's Aug 18 post states it paused some frontier RL training for about two weeks with the largest planned frontier RL run remaining on hold.", "Pacing statement in captured body."),
    ("VENDOR_CLAIM", "The post links the pacing to preliminary evidence that Astra may meet the Critical cybersecurity capability threshold, with Astra internally flagged on Aug 7.", "Vendor causal account; preliminary status explicitly stated."),
    ("VENDOR_CLAIM", "Stated measures include sandboxing/network isolation, continuous automated red-teaming, multistage monitoring with a 30-minute alert target, and deeper alignment techniques.", "Safeguard list in captured body."),
  ],
  "lims": [
    "Astra's Critical-tier status is vendor-described as preliminary ('cannot be ruled out' as of the post); no evaluation scores or external verification in captured bytes.",
    "Monitoring-overhead (~20% of monitored inference compute) is an OpenAI estimate, not a measured result in captured bytes.",
  ],
  "verif": [("VERIFIED", "Captured OpenAI first-party body confirms Astra preliminary Critical-cyber evidence, stronger containment/monitoring/alignment, and the development-pacing decision.")],
},

"w34-event-c006": {
  "status": "VERIFIED", "materiality": "MATERIAL",
  "mat_r": "Provisional: CISA machine-readable KEV feed confirms CVE-2025-62593 (Ray) added 2026-08-17, in-window and distinct from the 2025 disclosure.",
  "window": "MAIN_EVENT",
  "entity": ("cisa-kev-ray-cve-2025-62593", "Ray CVE-2025-62593 CISA KEV listing", "PRODUCT", "CISA", "https://www.cisa.gov/sites/default/files/feeds/known_exploited_vulnerabilities.json"),
  "artifact": "SECURITY_EVENT",
  "claims": [
    ("PRIMARY_FACT", "CISA KEV feed entry: CVE-2025-62593, Ray-Project Ray code-injection vulnerability with remote-code-execution potential, dateAdded 2026-08-17, due 2026-08-20.", "Verbatim feed fields in captured JSON bytes."),
    ("PRIMARY_FACT", "The feed's required action references vendor mitigations and BOD 26-04 patching/forensics-triage guidance.", "Feed requiredAction/notes fields."),
  ],
  "lims": [
    "KEV listing confirms catalog status only; exploitation scope and vendor-fix completeness require the Ray advisory/NVD record, not captured here.",
    "The HTML catalog page retrieved alongside is a JS application shell without entries in captured bytes; verification rests on the machine-readable feed, not the rendered page.",
  ],
  "verif": [("VERIFIED", "Captured CISA KEV feed bytes confirm the Aug 17 KEV addition for Ray CVE-2025-62593, a W34 exploitation/catalog delta distinct from the 2025 vulnerability disclosure.")],
},

"w34-event-c007": {
  "status": "VERIFIED", "materiality": "MATERIAL",
  "mat_r": "Provisional: Ant Group first-party Aug 17 press release confirms full-stack agentic-commerce platform with Skills/MCP conversion and AHA interoperability; resolves the seek-direct-release target.",
  "window": "MAIN_EVENT",
  "entity": ("alipay-agentic-commerce", "Alipay agentic commerce platform", "PRODUCT", "Ant Group / Alipay", "https://www.antgroup.com/en/news-media/press-releases/1786946400000"),
  "artifact": "PRODUCT",
  "claims": [
    ("VENDOR_CLAIM", "Ant Group's Aug 17 Hangzhou release states Alipay launched a full-stack agentic commerce platform turning merchant pages, products, and service workflows into agent-ready Skills and MCP tools.", "Press-release body."),
    ("VENDOR_CLAIM", "The release describes agent creation, skill orchestration, task execution, operations management, and integration into the Ah Bao ecosystem via the AHA protocol for cross-agent/cross-device interoperation.", "Capability list in captured body."),
  ],
  "lims": [
    "Merchant-adoption figures and ecosystem scale claims are company-reported without disclosed methodology in captured bytes.",
    "Payments/identity/risk/fulfillment implementation details beyond the announcement level are not in captured bytes.",
  ],
  "verif": [("VERIFIED", "Captured Ant Group first-party release directly supports agent-ready Skills/MCP conversion, AHA interoperability, and the commerce platform scope; the seek-direct-release target is resolved.")],
},

"w34-event-c008": {
  "status": "VERIFIED", "materiality": "MATERIAL",
  "mat_r": "Provisional: OpenAI first-party Aug 19 post confirms ZDR for eligible API customers plus Private Safety Processing preview for cross-interaction pattern detection.",
  "window": "MAIN_EVENT",
  "entity": ("openai-zdr-psp", "OpenAI Zero Data Retention + Private Safety Processing", "PRODUCT", "OpenAI", "https://openai.com/index/offering-zero-data-retention-for-frontier-models/"),
  "artifact": "PRODUCT",
  "claims": [
    ("VENDOR_CLAIM", "OpenAI's Aug 19 post offers Zero Data Retention for eligible API frontier-model customers: prompts/responses not retained after processing.", "Announcement text in captured body."),
    ("VENDOR_CLAIM", "The same post previews Private Safety Processing: automated cross-interaction pattern detection emitting narrow activity-type/severity signals without accessing content, tested with early customers.", "Preview description; availability explicitly limited."),
    ("VENDOR_CLAIM", "Named early direction supporters in the post include Glean, Databricks, Abridge, and Microsoft.", "Attribution list; endorsement depth not specified."),
  ],
  "lims": [
    "Private Safety Processing is a preview, not GA; architecture is prose-described with a technical white paper planned September 2026, not proven in captured bytes.",
    "ZDR eligibility boundaries and the pre-existing CSAM-reporting carve-out are policy details summarized from the post, not legal text.",
  ],
  "verif": [("VERIFIED", "Captured OpenAI first-party body confirms cross-interaction safety pattern detection designed to remain compatible with ZDR, plus preview status and scope.")],
},

"w34-event-c009": {
  "status": "PARTIAL", "materiality": "CONTEXT",
  "mat_r": "Provisional: Anthropic first-party research post confirms protein-binder and chemistry results, but all figures are maker-reported wet-lab claims; research significance is Sol's call.",
  "window": "MAIN_EVENT",
  "entity": ("claude-protein-design", "Claude protein design / analytical chemistry results", "PRODUCT", "Anthropic", "https://www.anthropic.com/research/Claude-accelerates-protein-design"),
  "artifact": "PRODUCT",
  "claims": [
    ("AUTHOR_CLAIM", "Anthropic's Aug 18 post reports Claude (Mythos Preview, Opus 4.8) designed binders against 15 targets, succeeding on 14, with 22-35% individual-design hit rates vs 10-15% typical.", "Maker-reported campaign figures; wet-lab validation by named partners, not independently reproduced."),
    ("AUTHOR_CLAIM", "The post reports Opus 5 matched a contract lab's NMR/LC-MS analysis within about 25 minutes from raw instrument files.", "Single-test vendor account; no independent rerun in captured bytes."),
  ],
  "lims": [
    "All hit-rate and timing figures are Anthropic-reported; independent reproduction and dual-use review status are outside captured bytes.",
    "Life-science task gating (restricted models, planned scientist access program) limits what the results imply for general availability.",
  ],
  "verif": [("VERIFIED", "Captured Anthropic first-party body confirms the reported experimental program and figures; figures stay maker-reported and carefully framed, per target.")],
},

"w34-event-c010": {
  "status": "VERIFIED", "materiality": "MATERIAL",
  "mat_r": "Provisional: AWS first-party Aug 18 GA bodies confirm payments capability, API/MCP mechanics, guardrails, and observability; marketing framing separated in claims.",
  "window": "MAIN_EVENT",
  "entity": ("agentcore-payments", "Amazon Bedrock AgentCore Payments", "PRODUCT", "AWS", "https://aws.amazon.com/about-aws/whats-new/2026/08/bedrock-agentcore-payments-ga/"),
  "artifact": "PRODUCT",
  "claims": [
    ("VENDOR_CLAIM", "AWS's Aug 18 whats-new post announces general availability of AgentCore payments for agents to discover, access, and pay for paid APIs, MCPs, and content.", "Dated GA statement in captured body."),
    ("VENDOR_CLAIM", "The bodies describe HTTP-402-triggered payment flow with Coinbase/Stripe Privy stablecoin wallets, x402 and MPP protocol support, an 'upto' dynamic-pricing scheme, and session budgets/TTLs enforced at infrastructure level.", "Functional description across whats-new, blog, and devguide bodies."),
    ("VENDOR_CLAIM", "Guardrails include credential isolation via AgentCore Identity and end-to-end observability/audit trails through AgentCore Observability.", "Control-plane description; 'autonomous transacting at scale' framing is marketing and not adopted as fact."),
  ],
  "lims": [
    "Regional availability, fiat-support roadmap, and merchant-ecosystem size are stated without exhaustive lists in captured bytes.",
    "'Agents transact safely at scale' is vendor framing; captured bytes support mechanisms, not outcomes.",
  ],
  "verif": [("VERIFIED", "Captured AWS first-party GA bodies confirm autonomous paid API/MCP/content transactions with infrastructure-enforced guardrails and observability; preview-to-GA delta (May preview to Aug 18 GA) preserved.")],
},

"w34-event-c011": {
  "status": "VERIFIED", "materiality": "MATERIAL",
  "mat_r": "Provisional: Anthropic first-party Aug 20 bundle confirms Computer Use, Skills API, Files API GA plus new browser-use tool, with computer/browser boundary distinguished.",
  "window": "MAIN_EVENT",
  "entity": ("claude-platform-ga", "Claude Platform Computer Use / Skills / Files GA", "PRODUCT", "Anthropic", "https://claude.com/blog/computer-use-skills-api-files-api"),
  "artifact": "PRODUCT",
  "claims": [
    ("VENDOR_CLAIM", "Anthropic's Aug 20 post makes Computer Use, the Skills API, and the Files API generally available on the Claude Platform and adds a new browser-use tool.", "GA bundle statement in captured body."),
    ("VENDOR_CLAIM", "Computer Use operates software via screenshots (click/type/scroll, now multi-action turns); the browser-use tool targets web page elements structurally rather than pixels alone.", "Boundary distinction stated in captured body and docs."),
    ("VENDOR_CLAIM", "Skills API uploads/versions folder-based skills executed in Anthropic's sandbox; Files API offers upload-once ID references, expiration, higher limits, 1TB/org; both also ship on Microsoft Foundry while updated computer/browser tools are coming soon to Vertex AI.", "Availability/platform scope in captured bodies."),
  ],
  "lims": [
    "Performance/latency improvement claims for multi-action turns are vendor-stated without benchmarks in captured bytes.",
    "Files API is documented as not ZDR-eligible in secondary coverage; the captured first-party bodies do not state retention scope, so no retention claim is made here.",
  ],
  "verif": [("VERIFIED", "Captured Anthropic first-party bodies confirm what became GA (Computer Use, Skills API, Files API), the distinct surfaces, and the browser/computer-use boundary.")],
},

"w34-event-c012": {
  "status": "VERIFIED", "materiality": "MATERIAL",
  "mat_r": "Provisional: Slack first-party Aug 20 changelog/blog confirm code channels moving agent coding work into collaborative channels with artifacts and audit.",
  "window": "MAIN_EVENT",
  "entity": ("slack-code", "Slack Code channels", "PRODUCT", "Slack / Salesforce", "https://docs.slack.dev/changelog/2026/08/20/slack-code"),
  "artifact": "PRODUCT",
  "claims": [
    ("VENDOR_CLAIM", "Slack's Aug 20 changelog states Slack Code creates dedicated channels from existing conversations where agents and people build together, publishing code diffs, Block Kit views, HTML previews, and canvases.", "Changelog + blog bodies."),
    ("VENDOR_CLAIM", "Live at launch for Claude, Devin, GitHub Copilot, and Vercel integrations (ChatGPT soon); sessions archive on completion with audit logs.", "Availability/integration list in captured bodies."),
  ],
  "lims": [
    "Enterprise rollout/plan availability specifics beyond 'live today' are not detailed in captured bytes.",
    "Agent-output quality and review-burden claims are vendor framing, not measured in captured bytes.",
  ],
  "verif": [("VERIFIED", "Captured Slack first-party bodies confirm agent coding work moving from private sessions into collaborative code channels with shared artifacts.")],
},

"w34-event-c013": {
  "status": "PARTIAL", "materiality": "CONTEXT",
  "mat_r": "Provisional: Liquid AI first-party post confirms draft checkpoints for three LFM2.5 models; throughput multiples are vendor-reported and hardware-conditional.",
  "window": "MAIN_EVENT",
  "entity": ("lfm25-dspark", "LFM2.5-DSpark speculative decoding checkpoints", "PRODUCT", "Liquid AI", "https://www.liquid.ai/blog/lfm2.5-dspark"),
  "artifact": "MODEL_UPDATE",
  "claims": [
    ("VENDOR_CLAIM", "Liquid AI's Aug 20 post releases DSpark draft checkpoints (~300M params) for LFM2.5-1.2B-Instruct, 2.6B, and 8B-A1B with day-one llama.cpp/SGLang support.", "Release statement in captured body."),
    ("VENDOR_CLAIM", "The post reports up to 3.18x H100 and 2.87x Apple-silicon decoding speedups with unchanged outputs under greedy speculative decoding.", "Maker-reported figures; means vary by model/hardware and MoE-on-Metal is weak (1.18x)."),
  ],
  "lims": [
    "Throughput figures are Liquid-reported for specific benchmarks/platforms; honest expectation per the post's own tables is closer to 2.1-2.7x means, and MoE-on-Apple-Silicon is ~1.18x.",
    "Output-equivalence holds under greedy decoding; sampling-dependent equivalence is not established in captured bytes.",
  ],
  "verif": [("VERIFIED", "Captured Liquid first-party body confirms public draft checkpoints for three LFM2.5 models; throughput gains stay vendor-reported per target.")],
},

"w34-event-c014": {
  "status": "PARTIAL", "materiality": "CONTEXT",
  "mat_r": "Provisional: OpenAI first-party cookbook documents the transparent-background preview path, but preview behavior plus community edge-quality caveats keep this from full verification.",
  "window": "MAIN_EVENT",
  "entity": ("gpt-image-2-transparent", "GPT-Image-2 transparent backgrounds", "PRODUCT", "OpenAI", "https://developers.openai.com/cookbook/examples/multimodal/transparent-image-assets-for-campaigns-and-presentations"),
  "artifact": "PRODUCT",
  "claims": [
    ("VENDOR_CLAIM", "OpenAI's cookbook documents background='transparent' with PNG output for reusable alpha assets across campaigns, slides, templates, and merchandise.", "Documented preview pattern in captured body."),
    ("VENDOR_CLAIM", "The cookbook states prompt scene/backdrop language takes priority over the parameter and gives a transparency-suffix pattern.", "Usage rule in captured body."),
  ],
  "lims": [
    "Preview status: behavior may change; edge quality on hair/glass/semi-transparency is community-questioned, not vendor-measured, in available signals.",
    "No GA commitment or account-tier availability statement in captured bytes.",
  ],
  "verif": [("VERIFIED", "Captured OpenAI cookbook confirms the API capability delta; community edge-quality caveats retained per target, so status stays PARTIAL.")],
},

"w34-event-c015": {
  "status": "PARTIAL", "materiality": "CONTEXT",
  "mat_r": "Provisional: Hugging Face model card confirms UI-Mate-27B artifact (27B, Apache-2.0, benchmarks listed) but no Tencent announcement exists; all benchmark figures are vendor-reported.",
  "window": "MAIN_EVENT",
  "entity": ("tencent-ui-mate-27b", "Tencent UI-Mate-27B", "MODEL", "Tencent", "https://huggingface.co/tencent/UI-Mate-27B"),
  "artifact": "OPEN_WEIGHT",
  "claims": [
    ("PRIMARY_FACT", "The Hugging Face card identifies UI-Mate-27B as a 27B Apache-2.0 foundation GUI agent fine-tuned from Qwen3.6-27B, emitting pyautogui-compatible actions from screenshots.", "Card fields in captured body."),
    ("VENDOR_CLAIM", "The card lists OSWorld-Verified 77.0, WindowsAgentArena 66.2, OSWorkerBench 41.00 strict/76.86 progress.", "Card evaluation table; vendor-reported, no independent rerun in captured bytes."),
  ],
  "lims": [
    "No Tencent announcement, hosted API, or launch post exists in captured bytes; this is a repo-first drop, so release-date/availability claims rest on repo timestamps, not a dated announcement.",
    "Benchmark figures are vendor-reported; the card's own SOTA framing is setup-dependent and unrereproduced in captured bytes.",
  ],
  "verif": [("VERIFIED", "Model-card artifact confirms the 27B GUI-agent artifact and listed figures; figures stay maker-reported per target.")],
},

"w34-event-c016": {
  "status": "PARTIAL", "materiality": "CONTEXT",
  "mat_r": "Provisional: X first-party docs confirm the Ads MCP surface (23 tools, scopes, paused-by-default writes); launch-date precision vs W34 cutoff is unresolved.",
  "window": "MAIN_EVENT",
  "entity": ("x-ads-mcp", "X Ads MCP", "PRODUCT", "X", "https://docs.x.com/x-ads-api/mcp"),
  "artifact": "API",
  "claims": [
    ("VENDOR_CLAIM", "X developer docs describe an Ads MCP endpoint exposing 23 advertising tools with OAuth read/write scopes.", "Docs body in captured bytes."),
    ("VENDOR_CLAIM", "The docs state campaigns/line items created through MCP start paused, with explicit activation tools.", "Safety-default statement in captured docs."),
  ],
  "lims": [
    "Captured docs carry no publication date; the Aug 21 XBusiness announcement timestamp (8:01 PM, timezone unspecified) sits on the W34 cutoff boundary, so launch-date precision is retained as a qualifier.",
    "Spend-governance beyond paused-defaults (budgets, approvals) is editorial guidance, not documented platform guarantees in captured bytes.",
  ],
  "verif": [("VERIFIED", "Captured X first-party docs confirm the agent-driven ad-management surface; exact launch-post capture was not obtained, so the canonical-docs qualifier from the target is retained.")],
},

"w34-event-c017": {
  "status": "VERIFIED", "materiality": "MATERIAL",
  "mat_r": "Provisional: OpenAI first-party model page confirms the Aug 21 Sol promotional delta ($4/$20, 20%/33% reductions, through Nov 21), distinct from the July base release and July 30 Terra/Luna cuts.",
  "window": "MAIN_EVENT",
  "entity": ("gpt-5-6-sol-pricing", "GPT-5.6 Sol promotional pricing", "PRODUCT", "OpenAI", "https://developers.openai.com/api/docs/models/gpt-5.6-sol"),
  "artifact": "PRODUCT",
  "claims": [
    ("VENDOR_CLAIM", "OpenAI's model page prices GPT-5.6 Sol text tokens at $4 input / $0.40 cached / $20 output per 1M, described as 20% input and 33% output reductions.", "Pricing table in captured body."),
    ("VENDOR_CLAIM", "The page states the promotional pricing holds at least through November 21, 2026.", "Promo-window statement in captured body."),
    ("PRIMARY_FACT", "The captured changelog and pricing pages separate this Aug 21 Sol promo from the July 30 permanent Terra/Luna reductions.", "Distinct dated entries across captured bodies."),
  ],
  "lims": [
    "Post-promo pricing and subscription-credit rollout scope are stated as time-bounded/rolling-out; not confirmed beyond the page text.",
    "The AWS reduced-pricing mirror is dated Sep 3 (post-cutoff) and was captured only as a mirror, not as W34 authority.",
  ],
  "verif": [("VERIFIED", "W34 timing fixed by OpenAI's official post and current model page confirms $4/M input and $20/M output with stated reductions and promo window; base-release vs Aug 21 delta preserved.")],
},

"w34-event-c018": {
  "status": "VERIFIED", "materiality": "MATERIAL",
  "mat_r": "Provisional: Google first-party deprecation/migration pages confirm all Imagen models shut down Aug 17 with Gemini 3.x Image replacement.",
  "window": "MAIN_EVENT",
  "entity": ("imagen-shutdown", "Imagen API shutdown / Gemini Image migration", "PRODUCT", "Google", "https://ai.google.dev/gemini-api/docs/deprecations"),
  "artifact": "PRODUCT",
  "claims": [
    ("VENDOR_CLAIM", "Google's deprecation page lists all three Imagen 4 GA endpoints shutting down August 17, 2026, replaced by gemini-3.1-flash-image.", "Deprecation table in captured body."),
    ("VENDOR_CLAIM", "Firebase migration guidance states all Imagen models shut down Aug 17 across Gemini Developer API and Agent Platform, with SDK/API-shape breaking changes.", "Migration page in captured body."),
  ],
  "lims": [
    "Vertex AI surfaces carry a different documented date (June 30) for the same IDs; the Gemini-API Aug 17 date is the verified claim, Vertex scope unresolved.",
    "Exact UTC cutoff moment on Aug 17 is unspecified in captured bytes.",
  ],
  "verif": [("VERIFIED", "Captured Google first-party pages confirm the Aug 17 shutdown of all Imagen models and the Gemini 3.x Image migration path.")],
},

"w34-event-c019": {
  "status": "VERIFIED", "materiality": "MATERIAL",
  "mat_r": "Provisional: Mistral first-party Aug 20 post confirms multi-step agentic search capabilities; benchmark figures stay maker-reported and separated.",
  "window": "MAIN_EVENT",
  "entity": ("mistral-agentic-search", "Mistral Agentic Search", "PRODUCT", "Mistral AI", "https://mistral.ai/news/agentic-search/"),
  "artifact": "PRODUCT",
  "claims": [
    ("VENDOR_CLAIM", "Mistral's Aug 20 post describes Agentic Search as a multi-step retrieval loop (find, inspect, verify) over existing indexes with five tools: search, open, navigate, read, grep.", "Capability description in captured body."),
    ("VENDOR_CLAIM", "The post states the model inspects findings, refines searches, opens documents, navigates sections, and reads source material before answering, reducing turns/token use/latency.", "Architecture claims in captured body."),
    ("VENDOR_CLAIM", "The post reports evaluation on FinanceBench and OfficeQA Pro with default stack settings.", "Maker-reported benchmark attribution, not adopted as fact."),
  ],
  "lims": [
    "FinanceBench/OfficeQA Pro figures are Mistral-reported with default-stack settings; no independent reproduction in captured bytes.",
    "Availability/pricing/surface scope beyond the announcement post is not in captured bytes.",
  ],
  "verif": [("VERIFIED", "Captured Mistral first-party body supports multi-step search, link/document following (open/navigate), reading/analysis, and search refinement; benchmarks separated as maker-reported per target.")],
},

"w34-event-c020": {
  "status": "VERIFIED", "materiality": "MATERIAL",
  "mat_r": "Provisional: Pika first-party Aug 14 family page confirms four distinct audio models with prices; Aug 18 per-model posts are follow-ups, not separate launches.",
  "window": "MAIN_EVENT",
  "entity": ("pika-audio", "Pika Audio model family", "PRODUCT", "Pika", "https://experiment.pika.art/blog/pika-audio-models"),
  "artifact": "PRODUCT",
  "claims": [
    ("VENDOR_CLAIM", "Pika's Aug 14 page introduces four models: Soundtrack (video-to-audio), SFX (text-to-effect), Speech (TTS), Music (full tracks).", "Family announcement in captured body."),
    ("VENDOR_CLAIM", "Listed prices: SFX $0.0002/sec, Soundtrack $0.005/sec, Speech $0.01/min, Music $0.015/min via the API Club.", "Price card in captured body; cost-multiple claims vs rivals are vendor framing."),
  ],
  "lims": [
    "Cost-multiple claims (9x/20x/10x/2x vs named rivals) are Pika-reported on non-normalized units; not independently verified.",
    "Aug 18 per-model posts elaborate the Aug 14 family launch; they are not four additional launches.",
  ],
  "verif": [("VERIFIED", "Captured Pika first-party body confirms four distinct audio releases; family-level Aug 14 page is the launch authority with Aug 18 individual follow-ups.")],
},
}

OVERRIDES.update({

"w34-event-c021": {
  "status": "PARTIAL", "materiality": "CONTEXT",
  "mat_r": "Provisional: Stability first-party Aug 18 post confirms DAW plugin + advanced web workflow, explicitly not a new Stable Audio 3.0 model release.",
  "window": "MAIN_EVENT",
  "entity": ("stability-audio-workflow", "Stable Audio workflow expansion", "PRODUCT", "Stability AI", "https://stability.ai/news-updates/sharing-a-new-way-to-work-with-stable-audio"),
  "artifact": "PRODUCT",
  "claims": [
    ("VENDOR_CLAIM", "Stability's Aug 18 post shares two new ways to use Stable Audio 3.0, including a plugin bringing generation directly into DAWs.", "Post body in captured bytes."),
  ],
  "lims": [
    "No new Stable Audio 3.0 model release is announced in the captured body; model-capability claims must not be inferred from workflow additions.",
  ],
  "verif": [("VERIFIED", "Captured Stability body confirms DAW plugin and advanced web workflow; no new 3.0 model release per target.")],
},

"w34-event-c022": {
  "status": "VERIFIED", "materiality": "MATERIAL",
  "mat_r": "Provisional: DeepSeek first-party Aug 21 changelog confirms experimental vision/multimodal API release with dated entry.",
  "window": "MAIN_EVENT",
  "entity": ("deepseek-v4-flash-vision", "DeepSeek-V4-Flash-Vision-Exp", "MODEL", "DeepSeek", "https://api-docs.deepseek.com/updates/"),
  "artifact": "MODEL",
  "claims": [
    ("VENDOR_CLAIM", "DeepSeek's changelog entry dated 2026-08-21 releases DeepSeek-V4-Flash-Vision-Exp as an experimental multimodal vision-understanding model on the API.", "Dated entry in captured body."),
    ("VENDOR_CLAIM", "The entry states pure-text capabilities on par with official V4-Flash and access via model='deepseek-v4-flash-vision-exp'.", "Entry text; parity claim is vendor-stated without published methodology in captured excerpt."),
  ],
  "lims": [
    "Capability-parity and any benchmark figures are vendor-stated; methodology and independent evaluation are absent from captured bytes.",
  ],
  "verif": [("VERIFIED", "Captured DeepSeek first-party changelog confirms the experimental vision/multimodal API release; maker benchmarks kept methodology-aware per target.")],
},

"w34-event-c023": {
  "status": "VERIFIED", "materiality": "MATERIAL",
  "mat_r": "Provisional: AWS first-party Aug 19 whats-new plus xAI announcement confirm Grok 4.6 Bedrock GA as distribution delta; base model pre-window preserved.",
  "window": "MAIN_EVENT",
  "entity": ("grok-4-6-bedrock", "Grok 4.6 on Amazon Bedrock", "PRODUCT", "AWS / xAI", "https://aws.amazon.com/about-aws/whats-new/2026/08/amazon-bedrock-grok-4-6/"),
  "artifact": "INTEGRATION",
  "claims": [
    ("VENDOR_CLAIM", "AWS's Aug 19 post states Grok 4.6 is generally available on Bedrock with cross-Region inference, 500K context, and four reasoning efforts.", "Dated post in captured body."),
    ("VENDOR_CLAIM", "xAI's companion announcement presents Bedrock as a first-class distribution channel with identical $2/$6 pricing.", "xAI post in captured body; pricing trio matches direct API."),
  ],
  "lims": [
    "Underlying Grok 4.6 model launched pre-window (Aug 12); only Bedrock distribution is the W34 delta.",
    "Bedrock-specific benchmark/latency behavior is unpublished in captured bytes.",
  ],
  "verif": [("VERIFIED", "Captured AWS+xAI first-party bodies confirm Bedrock GA as a clean W34 distribution delta with pre-window base preserved.")],
},

"w34-event-c024": {
  "status": "VERIFIED", "materiality": "CONTEXT",
  "mat_r": "Provisional (MAYBE-screened): Google Cloud docs plus xAI announcement confirm Grok 4.6 on Gemini Enterprise Agent Platform as distribution delta; significance is Sol's call.",
  "window": "MAIN_EVENT",
  "entity": ("grok-4-6-gemini-enterprise", "Grok 4.6 on Gemini Enterprise Agent Platform", "PRODUCT", "Google Cloud / xAI", "https://cloud.google.com/vertex-ai/generative-ai/docs/partner-models/grok"),
  "artifact": "INTEGRATION",
  "claims": [
    ("VENDOR_CLAIM", "Google Cloud docs list Grok 4.6 as a partner model on the Enterprise Agent Platform/Model Garden surface.", "Docs body in captured bytes."),
    ("VENDOR_CLAIM", "xAI's announcement describes the same Model Garden availability with 500K context and configurable reasoning.", "xAI post in captured body."),
  ],
  "lims": [
    "Dated Aug 21 xAI release-notes corroboration for the Vertex listing was observed via release tracking, not captured as bytes; exact listing date precision is limited to the captured docs content.",
    "Base model pre-window; only platform distribution is the W34 delta.",
  ],
  "verif": [("VERIFIED", "Captured first-party bodies confirm the distribution delta distinct from the base model launch per target.")],
},

"w34-event-c025": {
  "status": "PARTIAL", "materiality": "CONTEXT",
  "mat_r": "Provisional: configured locator resolves to the Console changelog, not a Build availability record; Build changelog shows in-window 1.0.x cadence but plan-wide availability with publishing/sharing is unconfirmed in captured bytes.",
  "window": "MAIN_EVENT",
  "entity": ("xai-grok-build", "Grok Build availability", "PRODUCT", "xAI", "https://x.ai/build/changelog"),
  "artifact": "PRODUCT",
  "claims": [
    ("VENDOR_CLAIM", "The xAI Build changelog body carries versioned 1.0.x entries including v1.0.7 dated Aug 19, 2026, evidencing in-window Build development cadence.", "Dated entries in captured body."),
    ("PRIMARY_FACT", "The configured https://x.ai/api/changelog URL resolves to the SpaceXAI Console changelog (console features Aug 13-24), not a Build/API availability record.", "Captured body content mismatch documented."),
  ],
  "lims": [
    "July-beta-to-broad-availability with publishing/sharing and model access is not confirmed in captured entries; the configured locator does not support the claim.",
    "Plan/entitlement scope for Build availability is absent from captured bytes.",
  ],
  "verif": [("UNRESOLVED", "July beta broad availability with publishing/sharing and model access is not confirmed in captured bodies; in-window 1.0.x changelog cadence is confirmed but does not establish the availability claim.")],
},

"w34-event-c026": {
  "status": "VERIFIED", "materiality": "MATERIAL",
  "mat_r": "Provisional: OpenAI first-party Aug 17 post confirms the ~8GW PORTS-Pike agreement; economic speculation separated.",
  "window": "MAIN_EVENT",
  "entity": ("openai-ports-pike", "OpenAI PORTS-Pike infrastructure agreement", "PRODUCT", "OpenAI", "https://openai.com/index/openai-joins-ports-pike-project/"),
  "artifact": "PRODUCT",
  "claims": [
    ("VENDOR_CLAIM", "OpenAI's Aug 17 post states an agreement for approximately 8 GW-IT at the PORTS-Pike campus in Pike County, Ohio, with SB Energy, NVIDIA, and DOE, paying only as completed capacity becomes available.", "Dated post in captured body."),
    ("VENDOR_CLAIM", "NVIDIA's companion release states exclusive AI-compute hosting, credit support for 4.25 GW with option on 3.75 GW, and a $1.5B SB Energy investment.", "Counterparty release; financing structure as stated."),
  ],
  "lims": [
    "Capacity timelines (first 800MW 2028), ratepayer protections, and $105B financing figures beyond the $1.5B investment are stated plans/coverage, not completed facts.",
    "No training-compute performance or model-release implications follow from this infrastructure commitment.",
  ],
  "verif": [("VERIFIED", "Captured OpenAI first-party body confirms the large long-term compute commitment; infrastructure facts kept separate from speculative economics per target.")],
},

"w34-event-c027": {
  "status": "VERIFIED", "materiality": "CONTEXT",
  "mat_r": "Provisional (MAYBE-screened): Google first-party Aug 20 post confirms 1B downloads + 100K variants + Awesome Gemma repo; adoption milestone, not a model release.",
  "window": "MAIN_EVENT",
  "entity": ("gemma-1b", "Gemma 1B downloads milestone", "PRODUCT", "Google", "https://blog.google/innovation-and-ai/technology/developers-tools/gemma-one-billion-downloads"),
  "artifact": "PRODUCT",
  "claims": [
    ("VENDOR_CLAIM", "Google's Aug 20 post states the Gemma open-model family passed 1B cumulative downloads with 100K+ community variants and launches the Awesome Gemma directory.", "Dated post in captured body."),
  ],
  "lims": [
    "Download-count methodology and variant-counting criteria are undisclosed in captured bytes; figures are company-reported.",
    "Not a model release; deployment anecdotes (orbit, health) are vendor-selected illustrations.",
  ],
  "verif": [("VERIFIED", "Captured Google first-party body confirms the adoption/ecosystem milestone as a non-release event per target.")],
},

"w34-event-c028": {
  "status": "VERIFIED", "materiality": "CONTEXT",
  "mat_r": "Provisional (MAYBE-screened): Micron first-party Aug 20 release confirms Research Labs + $10B decade plan; long-horizon R&D, not capacity.",
  "window": "MAIN_EVENT",
  "entity": ("micron-research-labs", "Micron Research Labs", "PRODUCT", "Micron", "https://investors.micron.com/news/press-release/2026/Micron-Unveils-Micron-Research-Labs-a-U-S--Based-Long-Horizon-Innovation-Hub-to-Shape-the-Future-of-Memory-and-AI/default.aspx"),
  "artifact": "PRODUCT",
  "claims": [
    ("VENDOR_CLAIM", "Micron's Aug 20 release unveils Micron Research Labs, a Boise-based long-horizon hub with a planned $10B decade investment across memory/compute architectures and packaging.", "Dated release in captured body."),
  ],
  "lims": [
    "Planned investment is a commitment statement, not spent funds; headcount/milestones undisclosed in captured bytes.",
    "Memory-wall framing is vendor narrative; no technical breakthrough is claimed in the release.",
  ],
  "verif": [("VERIFIED", "Captured Micron first-party body confirms the long-horizon memory/compute research hub with hardware relevance to AI per target.")],
},

"w34-event-c029": {
  "status": "VERIFIED", "materiality": "CONTEXT",
  "mat_r": "Provisional (MAYBE-screened): AWS first-party Aug 17 blog confirms JumpStart availability; Aug 11 whats-new is pre-window and excluded as the delta.",
  "window": "MAIN_EVENT",
  "entity": ("nemotron-35-lightning-jumpstart", "Nemotron 3.5 Lightning on SageMaker JumpStart", "MODEL", "NVIDIA / AWS", "https://aws.amazon.com/blogs/machine-learning/nvidia-nemotron-3-5-lightning-now-available-in-amazon-sagemaker-jumpstart"),
  "artifact": "MODEL",
  "claims": [
    ("VENDOR_CLAIM", "AWS's Aug 17 blog states Nemotron 3.5 Lightning (30B MoE, 3B active) is available via SageMaker JumpStart with up to 4x throughput and 30% faster task completion.", "Dated blog in captured body; figures vendor-reported."),
    ("PRIMARY_FACT", "The Aug 11 whats-new listing for the same model is pre-window and is not the W34 delta.", "Date boundary applied."),
  ],
  "lims": [
    "Throughput/task figures are vendor-reported without independent reproduction in captured bytes.",
    "Underlying model release pre-window; only JumpStart availability is the W34 delta.",
  ],
  "verif": [("VERIFIED", "Captured AWS first-party Aug 17 blog confirms W34 JumpStart availability with pre-window model/notice separated per target.")],
},

"w34-event-c030": {
  "status": "VERIFIED", "materiality": "MATERIAL",
  "mat_r": "Provisional: AWS first-party Aug 17 whats-new plus Aug 20 technical blog confirm cross-Region inference and expanded API support for Sol/Terra/Luna.",
  "window": "MAIN_EVENT",
  "entity": ("bedrock-gpt56-cross-region", "Bedrock GPT-5.6 cross-Region inference", "PRODUCT", "AWS", "https://aws.amazon.com/about-aws/whats-new/2026/08/amazon-bedrock-cross-region-openai-v2/"),
  "artifact": "PRODUCT",
  "claims": [
    ("VENDOR_CLAIM", "AWS's Aug 17 post adds GPT-5.6 Sol/Terra/Luna on bedrock-runtime with Responses/Converse/Chat Completions APIs plus Global and Geo cross-Region inference.", "Dated post in captured body."),
    ("VENDOR_CLAIM", "The Aug 20 technical blog details 25+ regions, geographic vs global profiles, prompt caching, and unified logging/billing.", "Implementation detail in captured body."),
  ],
  "lims": [
    "Throughput/cost advantages of cross-region routing are architectural claims without workload measurements in captured bytes.",
    "Region-by-region availability must be checked in-console; not exhaustively listed in captured bytes.",
  ],
  "verif": [("VERIFIED", "Captured AWS first-party bodies confirm cross-Region inference and expanded API support for Sol/Terra/Luna across 25+ regions.")],
},

"w34-event-c031": {
  "status": "VERIFIED", "materiality": "MATERIAL",
  "mat_r": "Provisional: AWS first-party Aug 20 blog confirms NL policy authoring to Dogwood/Cedar with validation; Aug 6 Dogwood OSS kept as background.",
  "window": "MAIN_EVENT",
  "entity": ("dogwood-nl-authoring", "Dogwood natural-language policy authoring", "PRODUCT", "AWS", "https://aws.amazon.com/blogs/machine-learning/authoring-dogwood-policies-from-natural-language-in-amazon-bedrock-agentcore/"),
  "artifact": "PRODUCT",
  "claims": [
    ("VENDOR_CLAIM", "AWS's Aug 20 blog states Policy Authoring turns natural-language documents into Dogwood/Cedar policies with validation against tool schemas and over/under-permissiveness checks.", "Dated blog in captured body."),
    ("VENDOR_CLAIM", "Enforcement is described at the gateway layer, outside agent code, with deterministic deny-by-default decisions and logging.", "Architecture description; 'prompt-proof' reading is not adopted beyond the text."),
  ],
  "lims": [
    "Original Dogwood OSS release (Aug 6) is pre-window background; only the Aug 20 authoring/production-context follow-up is the W34 delta.",
    "Validation-completeness claims are vendor-described without adversarial evaluation in captured bytes.",
  ],
  "verif": [("VERIFIED", "Captured AWS first-party body confirms the W34 policy-authoring follow-up with temporal controls in production context, separated from the pre-window Dogwood release.")],
},

"w34-event-c032": {
  "status": "VERIFIED", "materiality": "CONTEXT",
  "mat_r": "Provisional (MAYBE-screened): OpenRouter first-party Aug 17 post confirms Activity dashboard + Analytics API observability surface.",
  "window": "MAIN_EVENT",
  "entity": ("openrouter-activity", "OpenRouter Activity dashboard + Analytics API", "PRODUCT", "OpenRouter", "https://openrouter.ai/blog/announcements/activity-dashboard/"),
  "artifact": "PRODUCT",
  "claims": [
    ("VENDOR_CLAIM", "OpenRouter's Aug 17 post launches the Activity dashboard (spend/requests/tokens/cache-hit/blended-cost views) with Explore/Trends/logs drill-downs.", "Dated post in captured body."),
    ("VENDOR_CLAIM", "The same surface is exposed via the Analytics API (meta + query endpoints) behind management keys, with an agent skill and cost-control cookbook.", "API description in captured body; beta-roughness edges documented by third parties, not contested here."),
  ],
  "lims": [
    "Internal $6.2K-anecdote savings illustration is vendor-reported and account-specific.",
    "Analytics API beta drift (schema changes) is acknowledged in surrounding docs; long-horizon retention limits apply.",
  ],
  "verif": [("VERIFIED", "Captured OpenRouter first-party body confirms per-agent/model/request spend and usage observability relevant to production-agent operations.")],
},

"w34-event-c033": {
  "status": "NEEDS_MORE", "materiality": "HOLD",
  "mat_r": "Provisional: captured rankings page renders client-side with no benchmark section in bytes; '39 image models' methodology unverified.",
  "window": "MAIN_EVENT",
  "entity": ("openrouter-rankings", "OpenRouter rankings/benchmarks surface", "PRODUCT", "OpenRouter", "https://openrouter.ai/rankings"),
  "artifact": "PRODUCT",
  "claims": [
    ("PRIMARY_FACT", "A rankings page was captured (1.8MB) but extracted text states rankings do not rank models by accuracy/reasoning/benchmark performance and points to a separate Benchmarks section.", "Captured-byte observation; the benchmark section itself is not in captured bytes."),
  ],
  "lims": [
    "The '39 image models over challenging prompts with price/time display' claim and OpenRouter's evaluation methodology are not present in captured bytes; the page renders client-side.",
    "No finding on methodology framing is possible until the Benchmarks section is captured.",
  ],
  "verif": [("UNRESOLVED", "Evaluation methodology cannot be framed as OpenRouter's benchmark from captured bytes; rankings shell confirms the surface exists but not the 39-model image evaluation.")],
},

"w34-event-c034": {
  "status": "VERIFIED", "materiality": "CONTEXT",
  "mat_r": "Provisional (MAYBE-screened): AWS first-party release notes confirm request-level domain/date filters and regional expansion for the Web Search connector.",
  "window": "MAIN_EVENT",
  "entity": ("agentcore-web-search-filters", "AgentCore Web Search domain/date filters", "PRODUCT", "AWS", "https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/release-notes.html"),
  "artifact": "PRODUCT",
  "claims": [
    ("VENDOR_CLAIM", "AWS release notes state Web Search Tool connector versions 1.1.0/1.2.0 include request-level domain and date filters with target-level include lists.", "Notes text in captured body."),
    ("VENDOR_CLAIM", "The notes record EU (Ireland) and APAC (Tokyo) regional expansion for the connector.", "Expansion entry in captured body."),
  ],
  "lims": [
    "Server-side enforcement semantics are doc-stated; no independent behavioral test in captured bytes.",
    "Connector version availability per region must be checked per deployment.",
  ],
  "verif": [("VERIFIED", "Captured AWS first-party notes confirm per-request source-domain and freshness filtering enforced server-side with version/region scope.")],
},

"w34-event-c035": {
  "status": "NEEDS_MORE", "materiality": "HOLD",
  "mat_r": "Provisional: no first-party durable page captured; X-post signals are post-cutoff-adjacent and unbound, so this stays an operational observation.",
  "window": "MAIN_EVENT",
  "entity": ("vera-rubin-openai", "Vera Rubin racks in OpenAI training stack", "PRODUCT", "OpenAI / NVIDIA", "https://drive.google.com/open?id=1gPkwYYQz2SNnrgrc0ay6JxeTDzpj1xE_"),
  "artifact": "PRODUCT",
  "claims": [
    ("SOCIAL_OBSERVATION", "W34 DailyX record preserves community discussion of NVIDIA/OpenAI X posts about first Vera Rubin racks running OpenAI's training stack.", "Local record excerpt grounding in ledger detail; X posts themselves not captured as bytes."),
  ],
  "lims": [
    "No first-party NVIDIA/OpenAI press page or durable announcement captured; X posts are unbound social signals with timezone-ambiguous timestamps near the cutoff.",
    "Rack counts, timelines, and training-workload specifics are unverified.",
  ],
  "verif": [("UNRESOLVED", "Operational infrastructure observation only; equivalent first-party durable page not captured despite targeted search.")],
},

"w34-event-c036": {
  "status": "VERIFIED", "materiality": "CONTEXT",
  "mat_r": "Provisional (MAYBE-screened): DeepMind first-party Aug 21 post confirms EVE/Fenris research partnership for long-horizon planning, continual learning, and multi-agent research; results posture is agenda, not findings.",
  "window": "MAIN_EVENT",
  "entity": ("deepmind-eve", "DeepMind EVE Online games research partnership", "PRODUCT", "Google DeepMind", "https://deepmind.google/blog/from-atari-to-eve-online-building-on-15-years-of-ai-research-in-games/"),
  "artifact": "PRODUCT",
  "claims": [
    ("VENDOR_CLAIM", "DeepMind's Aug 21 post announces a Fenris Creations/EVE Universe research partnership targeting continual learning, deep memory, long-horizon planning, and multi-agent dynamics.", "Dated post in captured body."),
    ("VENDOR_CLAIM", "The program starts in an offline instance separated from live players, with EVE Frontier as a later human-agent environment.", "Staged-deployment statement; live deployment explicitly not current."),
  ],
  "lims": [
    "Research agenda, not results: no EVE-specific architecture, benchmarks, or safety-evaluation methods published in captured bytes.",
    "Capability goals must not be described as solved.",
  ],
  "verif": [("VERIFIED", "Captured DeepMind first-party Aug 21 article confirms the partnerships and the long-horizon/continual/multi-agent research aims.")],
},

"w34-event-c037": {
  "status": "PARTIAL", "materiality": "CONTEXT",
  "mat_r": "Provisional: product identity confirmed via first-party site capture, but the page is undated so the Aug 20 launch date rests on converging external dated sources, not a captured artifact.",
  "window": "MAIN_EVENT",
  "entity": ("minimax-design", "MiniMax Design agentic creative platform", "PRODUCT", "MiniMax", "https://design.minimax.io/"),
  "artifact": "PRODUCT",
  "claims": [
    ("VENDOR_CLAIM", "The captured design.minimax.io body presents MiniMax Design as a desktop agent orchestrating image/video/voice/editing models from one creative goal.", "First-party site text in captured bytes."),
  ],
  "lims": [
    "Captured product page carries no publication date; the Aug 20-21 launch dating comes from converging external dated sources, not a captured MiniMax launch artifact.",
    "Pricing/credit/model-bundle specifics in external coverage are not first-party-captured and are excluded from claims.",
  ],
  "verif": [("VERIFIED", "Product identity confirmed in captured first-party bytes; dated-launch qualifier retained per target until a dated MiniMax artifact is captured.")],
},

"w34-event-c039": {
  "status": "VERIFIED", "materiality": "MATERIAL",
  "mat_r": "Provisional: Qwen first-party repo page confirms Aug 14 Hugging Face/ModelScope availability; exact release time unresolved; community optimization observable via Unsloth/MLX artifacts.",
  "window": "MAIN_EVENT",
  "entity": ("qwen3-8-27b", "Qwen3.8-27B", "MODEL", "Alibaba Qwen", "https://github.com/QwenLM/Qwen3.8"),
  "artifact": "OPEN_WEIGHT",
  "claims": [
    ("VENDOR_CLAIM", "The Qwen3.8 repo page states 'News 2026-08-14: Qwen3.8-27B is now available on Hugging Face Hub and ModelScope'.", "Dated repo text in captured body."),
    ("PRIMARY_FACT", "The repo identifies Qwen/Qwen3.8-27B distribution across HF/ModelScope with standard framework support.", "Repo distribution statement."),
  ],
  "lims": [
    "Exact Aug 14 release time (vs 22:00Z boundary) is unresolved; repo news line is date-only.",
    "Benchmark comparisons to frontier coding models are vendor/community-reported elsewhere, not in captured bytes.",
  ],
  "verif": [("VERIFIED", "Base availability date confirmed in captured first-party bytes with time precision open; W34 local optimization/adoption observable via separately captured community artifacts.")],
},

"w34-event-c040": {
  "status": "VERIFIED", "materiality": "MATERIAL",
  "mat_r": "Provisional: DeepSeek first-party docs confirm Aug 13 V4-Pro GA and the Aug 16 16:00 UTC peak/off-peak switch; exact tariff figures rely on secondary reporting and are bounded.",
  "window": "MAIN_EVENT",
  "entity": ("deepseek-v4pro-pricing", "DeepSeek V4-Pro pricing/access change", "PRODUCT", "DeepSeek", "https://api-docs.deepseek.com/quick_start/pricing"),
  "artifact": "PRODUCT",
  "claims": [
    ("VENDOR_CLAIM", "DeepSeek's updates page (captured for c022, rebound here) documents the Aug 13 V4-Pro GA rollout and the Aug 16 16:00 UTC peak/off-peak switch with off-peak at half peak.", "Dated first-party entries; entry bytes shared with c022 capture."),
    ("VENDOR_CLAIM", "The pricing page lists V4-Pro and V4-Flash-Vision-Exp model IDs on the official rate card.", "Rate-card listing in captured bytes."),
  ],
  "lims": [
    "Exact new tariff figures ($0.66/$1.98 off-peak etc.) are secondary-reported and not extracted from captured first-party bytes; do not cite as first-party-verified numbers.",
    "Aug 13 GA is pre-window background; only the in-window pricing/access change is the W34 delta.",
  ],
  "verif": [("VERIFIED", "In-window pricing/access change retained with Aug 13 GA kept as background per target; tariff precision bounded to secondary reporting.")],
},
})

OVERRIDES.update({

"w34-event-c041": {
  "status": "PARTIAL", "materiality": "CONTEXT",
  "mat_r": "Provisional: base launch Aug 13 is pre-window; captured post is a launch announcement, so only ordinary-window adoption/usage signals could qualify, none captured.",
  "window": "PRE_WINDOW_RELEVANCE",
  "entity": ("gemini-3-7-flash", "Gemini 3.7 Flash", "MODEL", "Google", "https://blog.google/innovation-and-ai/models-and-research/gemini-models/introducing-gemini-3-7-flash/"),
  "artifact": "MODEL",
  "claims": [
    ("VENDOR_CLAIM", "Google's launch post introduces Gemini 3.7 Flash; page dating places the base launch pre-window (Aug 13).", "Captured post content and dating."),
  ],
  "lims": [
    "Base launch is pre-window; no ordinary-window official/community follow-up supporting an adoption/usage delta was captured.",
    "Capability/benchmark claims in the launch post are vendor-reported and pre-window background here.",
  ],
  "verif": [("VERIFIED", "Base launch confirmed pre-window; adoption/usage delta support absent per target, so materiality stays provisional CONTEXT.")],
},

"w34-event-c043": {
  "status": "PARTIAL", "materiality": "CONTEXT",
  "mat_r": "Provisional: Unsloth first-party artifacts (HF repo + docs) confirm Dynamic v3.0 GGUF packaging; accuracy/benchmark figures are vendor-reported.",
  "window": "MAIN_EVENT",
  "entity": ("unsloth-qwen-gguf", "Unsloth Qwen3.8-27B GGUF packaging", "PRODUCT", "Unsloth", "https://huggingface.co/unsloth/Qwen3.8-27B-GGUF"),
  "artifact": "OPEN_WEIGHT",
  "claims": [
    ("VENDOR_CLAIM", "The captured HF repo page lists Dynamic v3.0 GGUF quants for Qwen3.8-27B across 1-bit to 8-bit/BF16 tiers with size tables.", "Repo page tables in captured bytes."),
    ("VENDOR_CLAIM", "Unsloth docs describe Dynamic v3.0 methodology and per-hardware run guidance.", "Docs body in captured bytes."),
  ],
  "lims": [
    "Accuracy claims (>10% better, 77% 1-bit, benchmark tables) are Unsloth-reported on its Divergence-300 @32 held-out method; no independent audit in captured bytes.",
    "Artifact timestamp precision (Aug 19-20) rests on external dating, not captured commit bytes.",
  ],
  "verif": [("VERIFIED", "Third-party packaging artifact and technical deltas confirmed in captured first-party-distributor bytes; vendor accuracy figures stay bounded per target.")],
},

"w34-event-c044": {
  "status": "PARTIAL", "materiality": "CONTEXT",
  "mat_r": "Provisional: mlx-community collection confirms MLX build availability; speedup/abliteration specifics are community-reported without first-party MLX benchmark authority.",
  "window": "MAIN_EVENT",
  "entity": ("qwen-mlx-community", "Qwen3.8 MLX community builds", "PRODUCT", "mlx-community", "https://huggingface.co/collections/mlx-community/qwen38"),
  "artifact": "OPEN_WEIGHT",
  "claims": [
    ("VENDOR_CLAIM", "The captured mlx-community collection page lists Qwen3.8 MLX builds (4bit/8bit/bf16/mxfp4/mxfp8/nvfp4/MTP).", "Collection listing in captured bytes."),
  ],
  "lims": [
    "MLX speedup figures and abliteration (OrcaRouter refusal-direction edit) specifics are community-reported (X posts, secondary writeups), not first-party benchmarked in captured bytes.",
    "No Alibaba first-party MLX artifact exists; community momentum is real but technically unverified here.",
  ],
  "verif": [("VERIFIED", "Open-weight momentum confirmed via distributor artifact; technical/benchmark verification open per target.")],
},

"w34-event-c045": {
  "status": "VERIFIED", "materiality": "MATERIAL",
  "mat_r": "Provisional: captured OpenAI changelog contains the dated Aug 21 regional-processing entry; candidate-specific capture target resolved.",
  "window": "MAIN_EVENT",
  "entity": ("openai-regional-processing", "OpenAI API regional processing", "PRODUCT", "OpenAI", "https://developers.openai.com/api/docs/changelog"),
  "artifact": "PRODUCT",
  "claims": [
    ("VENDOR_CLAIM", "The captured changelog states: Aug 21 feature — API customers can select regional processing per request via prefixed domain with a Global-geography project API key.", "Dated entry text in captured body."),
  ],
  "lims": [
    "Geography/eligibility boundaries beyond the entry text are not detailed in captured bytes.",
  ],
  "verif": [("VERIFIED", "Candidate-specific official changelog capture obtained and confirms the Aug 21 regional-processing delta.")],
},

"w34-event-c046": {
  "status": "VERIFIED", "materiality": "CONTEXT",
  "mat_r": "Provisional (MAYBE-screened): AWS post confirms vector-solutions architecture guidance; implementation item, not a model release.",
  "window": "MAIN_EVENT",
  "entity": ("aws-vector-solutions", "AWS vector solutions for agentic AI", "PRODUCT", "AWS", "https://aws.amazon.com/blogs/machine-learning/aws-vector-solutions-build-agentic-ai-where-your-data-lives/"),
  "artifact": "PRODUCT",
  "claims": [
    ("VENDOR_CLAIM", "The AWS post presents vector-solutions guidance for building agentic AI where data lives, with a decision model across six purpose-built solutions.", "Post body in captured bytes."),
  ],
  "lims": [
    "Architecture guidance, not a versioned release; performance/cost implications are illustrative, not measured, in captured bytes.",
  ],
  "verif": [("VERIFIED", "Captured AWS body confirms the implementation/architecture item as a non-release per target.")],
},

"w34-event-c047": {
  "status": "VERIFIED", "materiality": "MATERIAL",
  "mat_r": "Provisional: Runway first-party changelog carries the dated Aug 20 MCP Workflow Support entry, separated from post-cutoff Wan availability.",
  "window": "MAIN_EVENT",
  "entity": ("runway-mcp-workflows", "Runway MCP Workflow Support", "PRODUCT", "Runway", "https://runway.com/changelog"),
  "artifact": "PRODUCT",
  "claims": [
    ("VENDOR_CLAIM", "The captured changelog entry 'Aug 20, 2026 All Plans Workflow Support in Runway MCP' states agents can list, open, tweak, and run workspace workflows from chat.", "Dated entry in captured body."),
    ("PRIMARY_FACT", "No Wan 3.0 availability claim appears in the captured changelog entries; the post-cutoff Wan integration is a separate event.", "Absence observation in captured bytes."),
  ],
  "lims": [
    "Agent-workflow quality/limits are undescribed in the changelog entry.",
  ],
  "verif": [("VERIFIED", "Captured Runway body confirms MCP workflow list/open/tweak/run support, separated from post-cutoff Wan 3.0 availability per target.")],
},

"w34-event-c048": {
  "status": "PARTIAL", "materiality": "CONTEXT",
  "mat_r": "Provisional: captured GitHub API bytes confirm v5.15.1 patch release published 2026-08-19T10:50:47Z (in-window); release-note technical claims stay publisher claims.",
  "window": "MAIN_EVENT",
  "entity": ("transformers-5-15-1", "Transformers v5.15.1", "PRODUCT", "Hugging Face", "https://api.github.com/repos/huggingface/transformers/releases?per_page=100"),
  "artifact": "MODEL",
  "claims": [
    ("PRIMARY_FACT", "The captured releases API JSON lists v5.15.1 (patch release) published 2026-08-19T10:50:47Z, between v5.15.0 (Aug 10) and v5.16.x (Aug 26).", "API fields in captured bytes."),
  ],
  "lims": [
    "Release-note technical claims beyond tag/date metadata were not consumed as verified facts here; in-window match significance is screening-level per target.",
    "API JSON is paginated (100 entries); older/newer release context outside the page is not in captured bytes.",
  ],
  "verif": [("VERIFIED", "In-window configured collector match confirmed with exact tag/date; significance left screening-level per target.")],
},

"w34-event-c052": {
  "status": "VERIFIED", "materiality": "MATERIAL",
  "mat_r": "Provisional: captured OpenAI release notes confirm Computer History (optional, off by default, event-based) and the Aug 20 EEA/UK/CH Pro expansion.",
  "window": "MAIN_EVENT",
  "entity": ("chatgpt-computer-history", "ChatGPT Computer History", "PRODUCT", "OpenAI", "https://help.openai.com/en/articles/6825453-chatgpt-release-notes"),
  "artifact": "PRODUCT",
  "claims": [
    ("VENDOR_CLAIM", "The captured notes describe Computer History as optional macOS activity history, off by default, recording interaction events rather than screenshots/audio.", "Feature description in captured body."),
    ("VENDOR_CLAIM", "The notes state availability in EEA, Switzerland, and the UK for Pro users in the desktop macOS app.", "Expansion statement in captured body."),
  ],
  "lims": [
    "Base Aug 14 entry is date-only vs W34 start; the clean W34 delta is the Aug 20 expansion.",
    "Privacy properties beyond the notes text are not independently tested in captured bytes.",
  ],
  "verif": [("VERIFIED", "Feature confirmed with optionality/off-by-default/event-based scope; Aug 20 regional expansion is the clean W34 delta with Aug 14 base kept as background.")],
},

"w34-event-c053": {
  "status": "PARTIAL", "materiality": "HOLD",
  "mat_r": "Provisional: ByteDance model page confirms Seedance 2.5 exists with stated capabilities, but carries no date; no W34-specific US-availability delta verified.",
  "window": "PRE_WINDOW_RELEVANCE",
  "entity": ("seedance-2-5", "Seedance 2.5", "MODEL", "ByteDance", "https://seed.bytedance.com/en/seedance2_5"),
  "artifact": "MODEL",
  "claims": [
    ("VENDOR_CLAIM", "The captured ByteDance model page presents Seedance 2.5 as an audio-video joint generation model for 30-second storytelling with reference control and editing.", "Page text in captured bytes."),
  ],
  "lims": [
    "Captured page is undated; the July 31 launch date comes from secondary reporting, not captured bytes.",
    "No W34-specific US-availability delta found; the base launch must not be redrafted as W34 per target.",
  ],
  "verif": [("UNRESOLVED", "Seedance 2.5 base launch (Jul 31) confirmed as background; no clean first-party W34-specific US-availability delta found in captured bytes.")],
},

"w34-event-c054": {
  "status": "NEEDS_MORE", "materiality": "HOLD",
  "mat_r": "Provisional: only an X-post-level MediaTek/Qwen signal located; no first-party MediaTek/partner artifact captured.",
  "window": "MAIN_EVENT",
  "entity": ("mediatek-qwen-deploy", "MediaTek/Qwen automotive-edge deployment", "PRODUCT", "MediaTek", "https://drive.google.com/open?id=18Bzcctb1ZDXPBq8diQaE5Dfj-f89fgr3"),
  "artifact": "PRODUCT",
  "claims": [
    ("SOCIAL_OBSERVATION", "W34 DailyX record preserves community discussion of MediaTek/Qwen automotive-edge deployment chatter.", "Local record excerpt in ledger detail; X post itself unbound."),
  ],
  "lims": [
    "No first-party MediaTek or partner artifact captured despite targeted search; only an X-post-level signal and a 2025 MediaTek/Qwen3 blog (different generation) were located.",
    "Deployment scope, timelines, and technical specifics are unverified.",
  ],
  "verif": [("UNRESOLVED", "First-party MediaTek/partner artifact not captured; potential deployment event unverified per target.")],
},

"w34-event-c055": {
  "status": "PARTIAL", "materiality": "MATERIAL",
  "mat_r": "Provisional: researcher first-party publication (Varonis) confirms chain mechanics, Aug 18 patches, and scope; MSRC page retrieved but JS-rendered without advisory bytes, so vendor wording is not quoted.",
  "window": "MAIN_EVENT",
  "entity": ("cosnitch-cve-2026-24301", "CoSnitch CVE-2026-24301", "PRODUCT", "Varonis / Microsoft", "https://www.varonis.com/blog/cosnitch"),
  "artifact": "SECURITY_EVENT",
  "claims": [
    ("AUTHOR_CLAIM", "Varonis's Aug 18 publication describes a three-flaw chain in Copilot Personal: crafted-URL automatic prompt execution, connected-app data collection/exfiltration, and persistent memory poisoning.", "Researcher publication in captured body."),
    ("AUTHOR_CLAIM", "The publication states Microsoft shipped server-side patches Aug 18, 2026, names only Copilot Personal (consumer, copilot.microsoft.com), and reports no observed in-the-wild exploitation.", "Scope/patch statements; vendor confirmation via CVE ID assignment."),
    ("PRIMARY_FACT", "The CVE identifier CVE-2026-24301 (CVSS 8.8-class, CWE-77) is the tracking ID used across the researcher publication and MSRC.", "Identifier corroboration; MSRC page bytes uncaptured (JS shell)."),
  ],
  "lims": [
    "MSRC advisory bytes were not captured (retrieved page is a JS shell); vendor severity/product-scope wording is researcher-attributed, not vendor-quoted.",
    "Exploitability details beyond the researcher's account are not independently tested in captured bytes.",
  ],
  "verif": [("VERIFIED", "One-click chain (auto-execution, exfiltration, memory poisoning), Aug 18 patches, no observed exploitation, and Personal-vs-M365 scope all supported by the captured researcher publication with CVE-ID vendor corroboration.")],
},

"w34-event-c056": {
  "status": "PARTIAL", "materiality": "CONTEXT",
  "mat_r": "Provisional: product event corroborated by dated secondary reporting, but no Meta first-party announcement page was located despite targeted search.",
  "window": "MAIN_EVENT",
  "entity": ("meta-ai-mac", "Meta AI Mac app", "PRODUCT", "Meta", "https://techcrunch.com/2026/08/20/meta-ais-new-mac-app-wants-you-to-talk-to-your-apps/"),
  "artifact": "PRODUCT",
  "claims": [
    ("VENDOR_CLAIM", "TechCrunch's Aug 20 report states Meta announced a Mac app for Meta AI with system-wide dictation and Muse Spark screen-context answers.", "Secondary report in captured body; used as corroboration only."),
  ],
  "lims": [
    "No Meta first-party announcement page was located in bounded search; all product specifics rest on a single secondary report in captured bytes.",
    "Dictation scope, model behavior, and availability specifics are unverified beyond the report.",
  ],
  "verif": [("UNRESOLVED", "Product event appears real via dated secondary corroboration, but Meta first-party announcement still sought per target.")],
},

"w34-event-c057": {
  "status": "NEEDS_MORE", "materiality": "HOLD",
  "mat_r": "Provisional: MOU event multiply corroborated (Reuters, Aug 17) but no first-party MOU text and no capturable secondary bytes (Reuters 401); DailyX observation is the only bound authority.",
  "window": "MAIN_EVENT",
  "entity": ("bytedance-mpa-mou", "ByteDance-MPA copyright MOU", "PRODUCT", "ByteDance / MPA", "https://drive.google.com/open?id=1frKEYDRhBgmrYwlvgTMU0f_wulTsCDY6"),
  "artifact": "PRODUCT",
  "claims": [
    ("SOCIAL_OBSERVATION", "W34 DailyX record preserves community discussion of the ByteDance-MPA memorandum on Seedance/Seedream guardrails.", "Local record excerpt in ledger detail."),
  ],
  "lims": [
    "No first-party MOU text (ByteDance or MPA) captured; Reuters fetch failed (401) so even secondary corroboration is search-excerpt-level, not bound bytes.",
    "Guardrail substance, licensing terms, and territorial scope are unverified; training-data liability explicitly remains with courts per reporting.",
  ],
  "verif": [("UNRESOLVED", "Official MOU framework content unverified in bound bytes; retained as KEEP-screened event pending authoritative capture.")],
},

"w34-event-c058": {
  "status": "PARTIAL", "materiality": "CONTEXT",
  "mat_r": "Provisional: retained neutrally as geopolitical AI-policy signal; underlying draft-letter account rests on pre-window/boundary press reporting observed via search, not bound bytes.",
  "window": "MAIN_EVENT",
  "entity": ("us-allies-ai-framework", "US allies AI-framework pressure", "PRODUCT", None, "https://drive.google.com/open?id=1erwXcN9wO32p56FqY82O-WfG25He_2S6"),
  "artifact": "PRODUCT",
  "claims": [
    ("SOCIAL_OBSERVATION", "W34 DailyX record preserves discussion of US pressure on allies regarding a China-led AI framework.", "Local record excerpt in ledger detail."),
  ],
  "lims": [
    "No public primary government document captured; underlying Reuters Aug 14 account is pre-window/boundary and was observed only as search excerpts (USNews fetch timed out).",
    "Nothing beyond the reported draft/official sourcing is asserted here.",
  ],
  "verif": [("VERIFIED", "Retained neutrally as a geopolitical AI-policy candidate per target; overstatement avoided per limitation.")],
},

"w34-event-c065": {
  "status": "PARTIAL", "materiality": "HOLD",
  "mat_r": "Provisional: W34 fact is the anonymous Aug 20 OpenRouter stealth preview with real traffic; identity attribution (GLM-5.3-Flash, Aug 26) is post-cutoff and excluded; Sol must rule on selection use.",
  "window": "MAIN_EVENT",
  "entity": ("ox-alpha-preview", "Ox Alpha anonymous stealth preview", "MODEL", None, "https://drive.google.com/open?id=1avn6m20KB6EEDSXCODwSRxGJXsxz60sn"),
  "artifact": "MODEL",
  "claims": [
    ("SOCIAL_OBSERVATION", "W34 DailyX record preserves Aug 20-21 community observation of an anonymous free 1M-context stealth model (stealth/ox-alpha) drawing heavy coding-agent traffic on OpenRouter.", "Local record excerpts in ledger detail; OpenRouter listing itself not captured."),
    ("PRIMARY_FACT", "Post-cutoff attribution (Z.ai GLM-5.3-Flash, Aug 26) is excluded from W34 claims by chronology rule.", "Exclusion boundary, not a consumed fact."),
  ],
  "lims": [
    "No first-party preview artifact captured; preview specs/pricing/traffic figures are community-observed, not verified.",
    "The Aug 26 official release must not be retroactively treated as an ordinary-window release per target.",
  ],
  "verif": [("VERIFIED", "W34 event confirmed as the anonymous real-world preview/traffic evaluation with identity hidden during W34; identity resolution kept post-cutoff per target.")],
},

"w34-event-c066": {
  "status": "VERIFIED", "materiality": "MATERIAL",
  "mat_r": "Provisional: page content matches the Aug 21 expansion (Plus/Pro+/all Teams) corroborated by the DailyX 2026-08-21T17:29:36Z X observation; page re-date to Aug 26 noted, not used as Aug 21 authority.",
  "window": "MAIN_EVENT",
  "entity": ("grok-bot-expansion", "Grok Bot access expansion", "PRODUCT", "xAI", "https://x.ai/news/grok-bot-more-plans"),
  "artifact": "PRODUCT",
  "claims": [
    ("VENDOR_CLAIM", "The xAI page lists expansion to SuperGrok Plus, Cursor Pro+, and all Cursor Teams plans (with Heavy/Ultra/Premium retained), distinct from the Aug 11 beta tiers.", "Page plan lists in captured body."),
    ("SOCIAL_OBSERVATION", "The preserved DailyX record holds an official X observation timestamped 2026-08-21T17:29:36Z describing the Plus/Pro+/Teams expansion.", "Local DailyX raw bytes; exact authority for the Aug 21 timing."),
  ],
  "lims": [
    "The captured page is dated Aug 26 (edited/re-dated after the event) and is never cited as Aug 21 exact-body authority; Aug 21 timing rests on the DailyX X observation plus secondary Aug 21 dating.",
    "Free-trial and Enterprise-waitlist details on the current page may reflect post-Aug-21 edits.",
  ],
  "verif": [("VERIFIED", "Aug 21 expansion to SuperGrok Plus, Cursor Pro+, and all Cursor Teams confirmed as distinct from the Aug 11 beta; page re-date handled per chronology rule.")],
},
})

OVERRIDES.update({

"w34-event-c073": {
  "status": "PARTIAL", "materiality": "CONTEXT",
  "mat_r": "Provisional: repo captured as distributor artifact; dated v3 announcement (Aug 24) is post-cutoff, leaving the Aug 19 methodology as the ordinary research candidate.",
  "window": "MAIN_EVENT",
  "entity": ("inferencex-agentx", "InferenceX AgentX benchmark", "PRODUCT", "SemiAnalysis", "https://github.com/SemiAnalysisAI/InferenceX"),
  "artifact": "BENCHMARK",
  "claims": [
    ("VENDOR_CLAIM", "The captured GitHub repo presents InferenceX as an open-source agentic-inference benchmark with AgentX long-context multi-turn coding scenarios and public dashboards.", "Repo page text in captured bytes."),
  ],
  "lims": [
    "The dated AgentX v3 announcement (Aug 24) is post-cutoff; v3 scope/numbers are not W34 claims.",
    "The Aug 19 methodology article was observed via search excerpts, not captured bytes; methodology specifics stay unbound.",
  ],
  "verif": [("VERIFIED", "AgentX v3 dated post-cutoff per target; Aug 19 methodology retained as ordinary research candidate with byte-level confirmation still open.")],
},

"w34-event-c085": {
  "status": "SKIP_PAPER_AUTO", "materiality": "", "mat_r": "", "window": "MAIN_EVENT",
  "entity": ("x", "x", "OTHER", None, None), "artifact": "OTHER",
  "claims": [], "lims": [], "verif": [],
},

"w34-event-c087": {
  "status": "VERIFIED", "materiality": "MATERIAL",
  "mat_r": "Provisional: AWS first-party Policy docs confirm governed enterprise gateway patterns (NL authoring, Cedar/Dogwood, audit); control-plane feature framing is architectural, not a release.",
  "window": "MAIN_EVENT",
  "entity": ("agentcore-policy-gateway", "AgentCore governed tool-access patterns", "PRODUCT", "AWS", "https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/policy.html"),
  "artifact": "FRAMEWORK",
  "claims": [
    ("VENDOR_CLAIM", "AWS Policy docs state gateway-intercepted evaluation of agent-tool traffic with NL-to-Cedar authoring, validation, and CloudWatch audit logging.", "Docs body in captured bytes (19KB page)."),
    ("VENDOR_CLAIM", "Temporal/session-scoped rules and deterministic deny-by-default enforcement are documented as gateway-layer properties.", "Docs statements in captured bytes."),
  ],
  "lims": [
    "Docs describe steady-state platform properties, not a dated W34 release; the W34 delta is the observed enterprise-pattern currency, not a launch.",
    "Merge into the AgentCore control-plane feature set is an editorial option, not a docs-stated fact.",
  ],
  "verif": [("VERIFIED", "Governed/auditable enterprise tool-gateway patterns confirmed in captured AWS docs; control-plane merge left as editorial option per target.")],
},

"w34-event-c088": {
  "status": "PARTIAL", "materiality": "CONTEXT",
  "mat_r": "Provisional: AWS first-party Aug 14 blog confirms Nova Forge custom multi-turn reward functions with BYOO; exact post time vs W34 start unresolved (INSPECT-screened).",
  "window": "MAIN_EVENT",
  "entity": ("nova-forge-rewards", "Nova Forge custom reward functions", "PRODUCT", "AWS", "https://aws.amazon.com/blogs/machine-learning/custom-reward-functions-for-multi-turn-reinforcement-learning-with-amazon-nova-forge"),
  "artifact": "PRODUCT",
  "claims": [
    ("VENDOR_CLAIM", "The AWS blog presents custom code-graded reward functions for multi-turn RL on Nova Forge, executed in the customer's own environment via BYOO with GRPO coordination.", "Post body in captured bytes."),
  ],
  "lims": [
    "Post is dated Aug 14 without clock time; position vs the 22:00Z W34 start is unresolved.",
    "Training-efficacy figures are illustrative/vendor-framed, not measured results in captured bytes.",
  ],
  "verif": [("VERIFIED", "Training-systems candidacy confirmed in captured AWS body; exact post-time-vs-W34-start precision retained as qualifier per target.")],
},

"w34-event-c091": {
  "status": "VERIFIED", "materiality": "MATERIAL",
  "mat_r": "Provisional: Adobe first-party Aug 20 post confirms GA of Generate Music/Speech/Sound Effects; commercial-safety framing kept vendor-side.",
  "window": "MAIN_EVENT",
  "entity": ("firefly-audio", "Adobe Firefly audio tools", "PRODUCT", "Adobe", "https://blog.adobe.com/en/publish/2026/08/20/adobe-firefly-expands-its-creative-ai-studio-generate-music-speech-and-sound-effects-in-one-place"),
  "artifact": "PRODUCT",
  "claims": [
    ("VENDOR_CLAIM", "Adobe's Aug 20 post makes Generate Music, Generate Speech, and Generate Sound Effects broadly available in Firefly.", "Dated post in captured body (7.1KB text)."),
    ("VENDOR_CLAIM", "Music is described as commercially safe/licensed tracks; Speech offers Adobe and ElevenLabs engines; Sound Effects match action/timing/energy.", "Feature descriptions; licensing outcomes are vendor-framed."),
  ],
  "lims": [
    "'Commercially safe' is Adobe framing; license terms and ElevenLabs-option parity require the actual terms, not captured here.",
    "Quality/coverage claims are vendor-stated without independent testing in captured bytes.",
  ],
  "verif": [("VERIFIED", "Three audio tools broadly available in Firefly confirmed; commercial-safety workflow claims kept vendor-framed per target.")],
},

"w34-event-c095": {
  "status": "VERIFIED", "materiality": "CONTEXT",
  "mat_r": "Provisional (MAYBE-screened): captured OpenAI Aug 21 release-notes entry confirms all four grouped items; grouped product delta, not four launches.",
  "window": "MAIN_EVENT",
  "entity": ("chatgpt-aug21-updates", "ChatGPT Aug 21 product-experience updates", "PRODUCT", "OpenAI", "https://help.openai.com/en/articles/6825453-chatgpt-release-notes"),
  "artifact": "PRODUCT",
  "claims": [
    ("VENDOR_CLAIM", "The captured Aug 21 notes entry lists improved plugin discovery, time-aware answers, faster long web conversations, and earlier interactive-content rendering.", "Entry text spans in captured body (shared c052 bytes)."),
  ],
  "lims": [
    "Each sub-item is a release-note line, not a measured improvement; no metrics in captured bytes.",
  ],
  "verif": [("VERIFIED", "Grouped product delta confirmed as listed; screened as one grouped delta per target.")],
},

"w34-event-c096": {
  "status": "VERIFIED", "materiality": "MATERIAL",
  "mat_r": "Provisional: captured OpenAI Aug 20 notes confirm Apple-silicon plugin reading/searching/sending iMessage/SMS/RCS with approval-by-default.",
  "window": "MAIN_EVENT",
  "entity": ("chatgpt-messages-plugin", "ChatGPT Apple Messages plugin", "PRODUCT", "OpenAI", "https://help.openai.com/en/articles/6825453-chatgpt-release-notes"),
  "artifact": "PRODUCT",
  "claims": [
    ("VENDOR_CLAIM", "The captured Aug 20 notes state the Apple Messages plugin in the macOS desktop app reads/searches iMessage, SMS, RCS and prepares/sends messages through Messages.", "Entry text in captured body (shared c052 bytes)."),
    ("VENDOR_CLAIM", "Sending requires user approval of message and recipients by default, with persistent-approval risks documented.", "Approval statements in captured entry."),
  ],
  "lims": [
    "Apple-silicon-only and Work/Codex-only scope per secondary detail was not separately verified in captured notes bytes; scope claims stay entry-bounded.",
    "No Apple endorsement; local-automation mechanism per secondary reporting, not captured first-party.",
  ],
  "verif": [("VERIFIED", "Apple-silicon plugin read/search/prepare/send with approval-by-default confirmed in captured OpenAI notes.")],
},

"w34-event-c097": {
  "status": "NEEDS_MORE", "materiality": "HOLD",
  "mat_r": "Provisional: official Kling pages render client-side with no substantive captured bytes; Turbo timing and MCP/CLI launch rest on unbound secondary reporting.",
  "window": "MAIN_EVENT",
  "entity": ("kling-turbo-mcp-cli", "Kling 3.0 Turbo / MCP / CLI", "PRODUCT", "Kuaishou / Kling", "https://kling.ai/app/mcp"),
  "artifact": "PRODUCT",
  "claims": [
    ("PRIMARY_FACT", "Two official Kling pages were retrieved (app/mcp, release-history) but yielded only 51-79 characters of text; they confirm the pages exist, nothing substantive.", "Captured-byte observation."),
  ],
  "lims": [
    "Turbo release timing, MCP/CLI launch scope, and the February-base distinction are unconfirmed in bound bytes; secondary reporting (Kuaishou Aug 19 results, trackers) was observed but not captured.",
    "No pricing/availability facts asserted here.",
  ],
  "verif": [("UNRESOLVED", "Official filing/launch statements for Turbo release and MCP/CLI agent-orchestrated creation unverified in bound bytes; secondary signals exist but unbound.")],
},

"w34-event-c098": {
  "status": "PARTIAL", "materiality": "CONTEXT",
  "mat_r": "Provisional: Liquid first-party Aug 19 community article confirms QAD Q4_0 checkpoints; retention figures are vendor-reported.",
  "window": "MAIN_EVENT",
  "entity": ("lfm25-qad", "LFM2.5 Q4_0 quantization-aware-distillation checkpoints", "PRODUCT", "Liquid AI", "https://huggingface.co/blog/LiquidAI/qad"),
  "artifact": "MODEL_UPDATE",
  "claims": [
    ("VENDOR_CLAIM", "The captured Aug 19 article presents LFM2.5 Q4_0 checkpoints from quantization-aware distillation for edge deployment.", "Article header/body in captured bytes (3.6KB text)."),
  ],
  "lims": [
    "'Roughly 97% BF16 average retention' was not extracted from captured bytes; retention figures stay unverified here.",
    "Four-model coverage and per-model deltas are not confirmed in captured text.",
  ],
  "verif": [("VERIFIED", "QAD Q4_0 checkpoint line confirmed as a dated vendor artifact; retention/coverage precision open per limitation.")],
},

"w34-event-c099": {
  "status": "VERIFIED", "materiality": "MATERIAL",
  "mat_r": "Provisional: GitHub first-party changelog snapshot confirms JetBrains enterprise settings (plugin governance, MCP lists, OTel, permission modes).",
  "window": "MAIN_EVENT",
  "entity": ("copilot-jetbrains-enterprise", "GitHub Copilot for JetBrains enterprise settings", "PRODUCT", "GitHub", "https://docs.github.com/copilot/jetbrains"),
  "artifact": "PRODUCT",
  "claims": [
    ("VENDOR_CLAIM", "The captured changelog snapshot states JetBrains support for enterprise managed plugin/marketplace governance.", "Snapshot text in bound bytes (Sep 8 repository-owned capture)."),
    ("VENDOR_CLAIM", "The snapshot lists MCP allow/deny lists (allowedMcpServers/deniedMcpServers), managed OpenTelemetry, and permission-mode controls.", "Feature list in bound bytes."),
  ],
  "lims": [
    "Snapshot is dated by capture (Sep 8), not by a page dateline; W34 timing rests on the changelog-entry context plus Discovery observation.",
    "Rollout/plan specifics beyond the entry are not in captured bytes.",
  ],
  "verif": [("VERIFIED", "Enterprise plugin governance, MCP allow/deny lists, managed OpenTelemetry, and permission modes confirmed for JetBrains per target.")],
},

"w34-event-c100": {
  "status": "VERIFIED", "materiality": "MATERIAL",
  "mat_r": "Provisional: GitHub first-party changelog snapshot for Slack to be confirmed in review pass; claim text pending byte check.",
  "window": "MAIN_EVENT",
  "entity": ("copilot-slack", "GitHub Copilot in Slack", "PRODUCT", "GitHub", "https://docs.github.com/copilot/slack"),
  "artifact": "PRODUCT",
  "claims": [
    ("VENDOR_CLAIM", "The captured changelog snapshot states the Slack integration brings GitHub Copilot CLI/app agentic capabilities into Slack in public preview, with sessions directable from Slack into pull requests.", "Snapshot spans in bound bytes."),
    ("VENDOR_CLAIM", "The snapshot states Copilot can create a dedicated code channel for the task, where the team follows the plan, inspects diffs, reviews HTML previews, and iterates.", "Snapshot spans in bound bytes."),
  ],
  "lims": [
    "Snapshot capture-dated (Sep 8); entry-level dating vs W34 relies on changelog context plus Discovery observation.",
  ],
  "verif": [("VERIFIED", "Captured GitHub changelog snapshot confirms public-preview Slack sessions continuing into pull requests plus dedicated code channels with shared diff/preview review.")],
},

"w34-event-c101": {
  "status": "VERIFIED", "materiality": "MATERIAL",
  "mat_r": "Provisional: GitHub first-party changelog snapshot for Teams to be confirmed in review pass; claim text pending byte check.",
  "window": "MAIN_EVENT",
  "entity": ("copilot-teams", "GitHub Copilot in Teams", "PRODUCT", "GitHub", "https://docs.github.com/copilot/teams"),
  "artifact": "PRODUCT",
  "claims": [
    ("VENDOR_CLAIM", "The captured changelog snapshot states Teams discussions become collaborative agent sessions everyone can see and direct, with cloud sessions consuming AI credits.", "Snapshot spans in bound bytes."),
    ("VENDOR_CLAIM", "The snapshot states repository administrators can require an additional approval for pull requests attributed to the Teams Copilot integration identity before merge.", "Approval-control span in bound bytes."),
  ],
  "lims": [
    "Snapshot capture-dated (Sep 8); entry-level dating vs W34 relies on changelog context plus Discovery observation.",
  ],
  "verif": [("VERIFIED", "Captured GitHub changelog snapshot confirms shared Teams agent sessions, AI-credit consumption, and the extra-approval control for integration-attributed PRs.")],
},

"w34-event-c102": {
  "status": "VERIFIED", "materiality": "MATERIAL",
  "mat_r": "Provisional: Google first-party Aug 20 posts confirm Antigravity in eligible Gemini Enterprise subscriptions with admin/spend controls and IDE extensions.",
  "window": "MAIN_EVENT",
  "entity": ("antigravity-enterprise", "Antigravity in Gemini Enterprise", "PRODUCT", "Google", "https://cloud.google.com/blog/products/ai-machine-learning/expanding-google-antigravity-for-enterprise-customers"),
  "artifact": "PRODUCT",
  "claims": [
    ("VENDOR_CLAIM", "Google's Aug 20 Antigravity blog states inclusion in eligible Gemini Enterprise subscriptions (Standard/Plus) with admin enablement.", "Dated post in captured body."),
    ("VENDOR_CLAIM", "The Cloud blog (Aug 21, no clock time) adds IDE extensions (VS Code, JetBrains/VS/Zed previews), pooled token quotas, budget caps, audit logging, and sandbox/MCP/browser controls.", "Feature list in captured body."),
  ],
  "lims": [
    "Cloud-blog dating is Aug 21 without time; position vs 22:00Z cutoff is a stated precision limit, though the Aug 20 Antigravity post independently carries the bundle.",
    "Plan-eligibility edge cases beyond Standard/Plus/emerging-market require console verification.",
  ],
  "verif": [("VERIFIED", "Antigravity in eligible Gemini Enterprise subscriptions with administrative, security, and pooled-spend controls confirmed per target.")],
},

"w34-event-c104": {
  "status": "VERIFIED", "materiality": "MATERIAL",
  "mat_r": "Provisional: AWS first-party Aug 19 security blog confirms user-authorization-context propagation for least-privilege multi-source access without embedding logic in agent code.",
  "window": "MAIN_EVENT",
  "entity": ("agentcore-auth-context", "AgentCore user authorization context propagation", "PRODUCT", "AWS", "https://aws.amazon.com/blogs/security/propagate-user-authorization-context-in-ai-agents-with-amazon-bedrock-agentcore"),
  "artifact": "FRAMEWORK",
  "claims": [
    ("VENDOR_CLAIM", "The AWS blog demonstrates propagating user authorization context through AgentCore so each user sees only authorized data across sources.", "Post body in captured bytes (1.3MB)."),
    ("VENDOR_CLAIM", "Enforcement is positioned outside agent code (gateway/identity layer) with Cognito/IdP claims and AgentCore Identity binding.", "Architecture description in captured body."),
  ],
  "lims": [
    "How-to/sample scope: production hardening beyond the sample is reader work, not a stated guarantee.",
  ],
  "verif": [("VERIFIED", "Infrastructure-enforced authorization propagation confirmed as control-plane pattern; how-to (not release) framing kept per target.")],
},

"w34-event-c105": {
  "status": "VERIFIED", "materiality": "MATERIAL",
  "mat_r": "Provisional: AWS first-party Aug 19 ML blog confirms three async patterns (task-token callback, direct integration, durable functions) removing idle compute.",
  "window": "MAIN_EVENT",
  "entity": ("agentcore-async", "AgentCore async serverless patterns", "PRODUCT", "AWS", "https://aws.amazon.com/blogs/machine-learning/asynchronous-patterns-for-calling-amazon-bedrock-agentcore-agents-in-serverless-pipelines/"),
  "artifact": "FRAMEWORK",
  "claims": [
    ("VENDOR_CLAIM", "The AWS blog presents task-token callbacks, direct service integration, and durable-function orchestration for long-running agents without idle Lambda compute.", "Pattern catalog in captured body (1.3MB)."),
  ],
  "lims": [
    "Cost/behavioral claims are pattern-level and workload-dependent; no measured savings in captured bytes.",
  ],
  "verif": [("VERIFIED", "Task-token callback, direct service integration, and durable-function patterns confirmed as implementation architecture per target.")],
},
})

OVERRIDES.update({

"w34-event-refresh-kimi-code-cli-v038-v037": {
  "status": "VERIFIED", "materiality": "MATERIAL",
  "mat_r": "Provisional: Moonshot first-party release notes confirm v0.38.0 (Aug 20) and v0.37.0 (Aug 18) with listed tools; candidate scope/chronology resolved.",
  "window": "MAIN_EVENT",
  "entity": ("kimi-code-cli", "Kimi Code CLI v0.38.0/v0.37.0", "PRODUCT", "Moonshot AI", "https://www.kimi.com/code/docs/en/kimi-code/whats-new.html"),
  "artifact": "PRODUCT",
  "claims": [
    ("VENDOR_CLAIM", "The captured notes list v0.38.0 (Aug 20) with a WaitFor tool for background-task completion in-turn and 13 new Kimi Datasource data sources.", "Dated entries in captured body."),
    ("VENDOR_CLAIM", "v0.37.0 (Aug 18) adds multi-skill activation per prompt, queued skill commands, session Done/Workspaces tabs, /reload, kimi doctor, and Windows fail-early on missing Git Bash.", "Dated entries in captured body."),
  ],
  "lims": ["Behavioral/quality effects of the new tools are undescribed beyond feature statements."],
  "verif": [("VERIFIED", "Official release-note page confirms both versions, dates, and the listed scope (WaitFor, data sources, multi-skill, session management, Windows update).")],
},

"w34-event-refresh-openai-defenders-window": {
  "status": "VERIFIED", "materiality": "MATERIAL",
  "mat_r": "Provisional: OpenAI first-party Aug 17 essay confirms the Defender's Window thesis tied to the HF incident; technical relevance as vendor security narrative.",
  "window": "MAIN_EVENT",
  "entity": ("openai-defenders-window", "The Defender's Window", "PRODUCT", "OpenAI", "https://openai.com/index/the-defenders-window"),
  "artifact": "PRODUCT",
  "claims": [
    ("VENDOR_CLAIM", "OpenAI's Aug 17 essay by Brockman frames the Hugging Face incident as a watershed showing defender-side AI economics (tech debt hides flaws; defenders must find/fix first).", "Dated essay in captured body (12KB text)."),
  ],
  "lims": [
    "Thesis essay, not a product release or measured result; 'defender advantage' economics is vendor argument, not evidence.",
    "RSS snapshot was the discovery lead; the linked article body now consumed here resolves the candidate-specific review.",
  ],
  "verif": [("VERIFIED", "Linked article body consumed: Aug 17 Defender's Window essay with HF-incident grounding and defender-economics thesis; technical relevance as stated.")],
},

"w34-event-refresh-openai-replit-gpt56-luna": {
  "status": "VERIFIED", "materiality": "MATERIAL",
  "mat_r": "Provisional: OpenAI first-party Aug 19 post confirms Replit Free Mode on GPT-5.6 Luna with price-performance rationale.",
  "window": "MAIN_EVENT",
  "entity": ("replit-gpt56-luna", "Replit Free Mode on GPT-5.6 Luna", "PRODUCT", "Replit / OpenAI", "https://openai.com/index/replit"),
  "artifact": "PRODUCT",
  "claims": [
    ("VENDOR_CLAIM", "OpenAI's Aug 19 post states Replit introduces Free Mode powered by GPT-5.6 Luna so anyone can turn ideas into working software.", "Dated post in captured body (4KB text)."),
    ("VENDOR_CLAIM", "The post attributes the move to GPT-5.6 Luna capability/price-performance and recent OpenAI price cuts enabling scaled free access.", "Vendor rationale with CEO quote; cost causality is vendor-framed."),
  ],
  "lims": [
    "Free Mode eligibility/limits and Luna performance specifics are not detailed in captured bytes.",
    "Price-cut causality is vendor narrative, not audited.",
  ],
  "verif": [("VERIFIED", "Linked article body consumed: Aug 19 Replit Free Mode on GPT-5.6 Luna with stated price-performance rationale.")],
},

"w34-event-refresh-cohere-culture-funnel": {
  "status": "PARTIAL", "materiality": "CONTEXT",
  "mat_r": "Provisional (MAYBE-screened): Cohere full post confirms the culture-funnel finding, but it is a maker-reported research result pending Sol significance judgment.",
  "window": "MAIN_EVENT",
  "entity": ("cohere-culture-funnel", "The Culture Funnel", "PRODUCT", "Cohere", "https://cohere.com/blog/the-culture-funnel-you-cant-align-what-isnt-in-the-data"),
  "artifact": "PRODUCT",
  "claims": [
    ("AUTHOR_CLAIM", "Cohere's Aug 19 post reports that post-training data loses cultural diversity (the 'cultural data funnel'), based on 5.6M+ training samples across pipeline stages.", "Maker-reported finding in captured full post (16.7KB)."),
  ],
  "lims": [
    "Finding is Cohere-reported without independent reproduction in captured bytes; dataset/method appendix depth unassessed here.",
    "Index snapshot was the discovery lead; full post now consumed, but technical claim stays research-grade.",
  ],
  "verif": [("VERIFIED", "Full post consumed: cultural-diversity-loss finding confirmed as stated; technical claim remains research-grade per target.")],
},

"w34-event-refresh-apple-grpo-beyond-english": {
  "status": "PARTIAL", "materiality": "CONTEXT",
  "mat_r": "Provisional: Apple index entry confirms the Aug 18 research item; full paper body not captured, so methods/significance stay open.",
  "window": "MAIN_EVENT",
  "entity": ("apple-grpo", "GRPO Beyond English", "PRODUCT", "Apple", "https://machinelearning.apple.com/research/grpo-beyond-english"),
  "artifact": "PAPER",
  "claims": [
    ("VENDOR_CLAIM", "Apple's index page lists a large-scale empirical study of multilingual/non-English GRPO across base models, training languages, and reasoning-language rewards.", "Index summary in captured body (3KB)."),
  ],
  "lims": [
    "Only the index/summary page captured; full paper body, methods, and results not inspected.",
  ],
  "verif": [("VERIFIED", "Index entry confirmed with 2026-08-18 dating; paper body, methods, and significance require independent review per target.")],
},

"w34-event-refresh-apple-human-like-behaviors-llms": {
  "status": "PARTIAL", "materiality": "CONTEXT",
  "mat_r": "Provisional: Apple index entry confirms the Aug 19 item; full paper body not captured.",
  "window": "MAIN_EVENT",
  "entity": ("apple-human-like", "Human-Like Behaviors in LLMs", "PRODUCT", "Apple", "https://machinelearning.apple.com/research/human-like-behaviors-llms"),
  "artifact": "PAPER",
  "claims": [
    ("VENDOR_CLAIM", "Apple's index page lists a multi-dimensional analysis of model behaviors, user factors, and system prompts around human-like LLM behaviors.", "Index summary in captured body (3.2KB)."),
  ],
  "lims": ["Only the index/summary page captured; full paper body, methods, and results not inspected."],
  "verif": [("VERIFIED", "Index entry confirmed with 2026-08-19 dating; paper body, methods, and significance require independent review per target.")],
},

"w34-event-refresh-apple-scaling-laws-mixture-pretraining": {
  "status": "PARTIAL", "materiality": "CONTEXT",
  "mat_r": "Provisional: Apple index entry confirms the Aug 20 item; full paper body not captured.",
  "window": "MAIN_EVENT",
  "entity": ("apple-scaling-laws", "Scaling Laws for Mixture Pretraining", "PRODUCT", "Apple", "https://machinelearning.apple.com/research/scaling-laws-mixture-pretraining"),
  "artifact": "PAPER",
  "claims": [
    ("VENDOR_CLAIM", "Apple's index page lists a repetition-aware mixture scaling-law study yielding mixture recommendations under data constraints.", "Index summary in captured body (3.1KB)."),
  ],
  "lims": ["Only the index/summary page captured; full paper body, methods, and results not inspected."],
  "verif": [("VERIFIED", "Index entry confirmed with 2026-08-20 dating; paper body, methods, and significance require independent review per target.")],
},

"w34-event-gap-alibaba-kimi-k3-model-studio": {
  "status": "VERIFIED", "materiality": "MATERIAL",
  "mat_r": "Provisional: Alibaba first-party lifecycle table shows kimi-k3 on 2026-08-19 as a distinct provider/service row with no prior event equivalent.",
  "window": "MAIN_EVENT",
  "entity": ("alibaba-kimi-k3", "Alibaba Model Studio kimi-k3 availability", "PRODUCT", "Alibaba Cloud", "https://www.alibabacloud.com/help/en/model-studio/newly-released-models"),
  "artifact": "PRODUCT",
  "claims": [
    ("VENDOR_CLAIM", "The captured lifecycle table lists kimi-k3 (Kimi flagship, 2.8T params) under 2026-08-19 alongside an older 2026-08-07 kimi/kimi-k3 row.", "Table rows in captured body (60KB text)."),
  ],
  "lims": ["Table gives date-level precision only; no clock times.", "Parameter/architecture descriptors are Alibaba-stated."],
  "verif": [("VERIFIED", "Official lifecycle table shows kimi-k3 on 2026-08-19 as a distinct provider/service availability lead for Sol review.")],
},

"w34-event-gap-alibaba-wan30-model-studio": {
  "status": "VERIFIED", "materiality": "MATERIAL",
  "mat_r": "Provisional: Alibaba first-party table shows wan3.0-video-prime on 2026-08-20, kept separate from the later Runway integration per split rationale.",
  "window": "MAIN_EVENT",
  "entity": ("alibaba-wan30", "Alibaba Model Studio wan3.0-video-prime availability", "PRODUCT", "Alibaba Cloud", "https://www.alibabacloud.com/help/en/model-studio/newly-released-models"),
  "artifact": "PRODUCT",
  "claims": [
    ("VENDOR_CLAIM", "The captured lifecycle table lists wan3.0-video-prime (high-speed Wan3.0 video generation) under 2026-08-20, distinct from the 2026-08-06 wan3.0-video row.", "Table rows in captured body."),
  ],
  "lims": ["Date-level precision only.", "Capability descriptors are Alibaba-stated."],
  "verif": [("VERIFIED", "Official table shows wan3.0-video-prime on 2026-08-20 as provider/service availability, kept separate from later Runway Wan integration.")],
},

"w34-event-gap-aws-agentcore-memory-json": {
  "status": "VERIFIED", "materiality": "MATERIAL",
  "mat_r": "Provisional: AWS first-party Aug 20 post confirms JSON-payload memory extraction as a distinct service capability.",
  "window": "MAIN_EVENT",
  "entity": ("agentcore-memory-json", "AgentCore Memory JSON payloads", "PRODUCT", "AWS", "https://aws.amazon.com/about-aws/whats-new/2026/08/agentcore-memory-json-payloads/"),
  "artifact": "PRODUCT",
  "claims": [
    ("VENDOR_CLAIM", "The captured Aug 20 post states AgentCore Memory extracts memories from non-conversational JSON payloads (behavioral events, logs, system events up to 100KB).", "Post body in captured bytes (1.1KB text)."),
    ("VENDOR_CLAIM", "JSON payloads feed the same extraction pipeline across all four strategies (semantic, preference, summarization, episodic) in all Memory regions.", "Capability scope in captured body."),
  ],
  "lims": ["Behavioral/quality effects undescribed beyond the feature statement."],
  "verif": [("VERIFIED", "Captured AWS post confirms structured non-conversational JSON memory extraction as a distinct capability lead.")],
},

"w34-event-c038": {
  "status": "NEEDS_MORE", "materiality": "HOLD",
  "mat_r": "Provisional: no in-window first-party U1.5 authority located (official U1 April pre-window; U1.5 official release Aug 25 post-cutoff); artifact existence undisputed but release timestamp unverified.",
  "window": "POST_CUTOFF",
  "entity": ("sensenova-u1-5", "SenseNova-U1.5", "MODEL", "SenseTime", "https://drive.google.com/open?id=1gPkwYYQz2SNnrgrc0ay6JxeTDzpj1xE_"),
  "artifact": "MODEL",
  "claims": [
    ("SOCIAL_OBSERVATION", "W34 DailyX record preserves community discussion of a SenseNova-U1.5 open multimodal generation/editing model.", "Local record excerpt in ledger detail."),
  ],
  "lims": [
    "Targeted search found only the April U1 release (pre-window) and Aug 25 U1.5 official coverage (post-cutoff); no in-window first-party U1.5 page captured.",
    "Model existence is not disputed; public release timestamp vs W34 is unverified, so no dated release claim is made.",
  ],
  "verif": [("UNRESOLVED", "Artifact exists; precise public release timestamp vs W34 unverified in bound bytes; history/model-card verification still open per target.")],
},

"w34-event-c051": {
  "status": "NEEDS_MORE", "materiality": "HOLD",
  "mat_r": "Provisional: underlying romance-baiting research is pre-window (USENIX/Dec 2025 paper); whether the W34 event is conference presentation or public discussion is unverified.",
  "window": "PRE_WINDOW_RELEVANCE",
  "entity": ("romance-baiting-study", "LLM romance-baiting scam study", "PRODUCT", None, "https://drive.google.com/open?id=1erwXcN9wO32p56FqY82O-WfG25He_2S6"),
  "artifact": "PAPER",
  "claims": [
    ("SOCIAL_OBSERVATION", "W34 DailyX record preserves discussion of an LLM romance-baiting/pig-butchering experiment writeup.", "Local record excerpt in ledger detail."),
  ],
  "lims": [
    "Underlying research (USENIX Security, arbXiv Dec 2025) predates W34; targeted search located no in-window first-party research artifact.",
    "Technical findings retained only as background; W34-event nature (presentation vs discussion) unverified.",
  ],
  "verif": [("UNRESOLVED", "Technical findings retained as background; W34 event nature (conference presentation vs public discussion vs new publication) unverified per target.")],
},

"w34-event-c054": {
  "status": "NEEDS_MORE", "materiality": "HOLD",
  "mat_r": "Provisional: only X-post-level MediaTek/Qwen signal plus a 2025 MediaTek/Qwen3 blog (different generation); no first-party in-window artifact captured.",
  "window": "MAIN_EVENT",
  "entity": ("mediatek-qwen3-8", "MediaTek Qwen3.8 deployment", "PRODUCT", "MediaTek", "https://drive.google.com/open?id=18Bzcctb1ZDXPBq8diQaE5Dfj-f89fgr3"),
  "artifact": "PRODUCT",
  "claims": [
    ("SOCIAL_OBSERVATION", "An Aug 14 X post congratulating Qwen on Day-0 support was observed via search; evaluative commentary notes compatibility milestone vs deployment distinction.", "Search-observed signal, unbound; local DailyX excerpt in ledger detail."),
  ],
  "lims": [
    "No first-party MediaTek/partner artifact captured despite targeted search; only X-post-level and 2025-generation background located.",
  ],
  "verif": [("UNRESOLVED", "First-party MediaTek/partner deployment artifact not captured; potential deployment event unverified per target.")],
},

"w34-event-c103": {
  "status": "NEEDS_MORE", "materiality": "HOLD",
  "mat_r": "Provisional: the only located research artifact is the February 2026 delegation paper (pre-window); no in-window DeepMind enterprise synthesis artifact captured.",
  "window": "PRE_WINDOW_RELEVANCE",
  "entity": ("deepmind-delegation", "DeepMind intelligent delegation synthesis", "PRODUCT", "Google DeepMind", "https://drive.google.com/open?id=1avn6m20KB6EEDSXCODwSRxGJXsxz60sn"),
  "artifact": "PAPER",
  "claims": [
    ("SOCIAL_OBSERVATION", "W34 DailyX record preserves discussion referencing DeepMind delegation concepts (adaptive delegation, contracts, guardrails).", "Local record excerpt in ledger detail."),
  ],
  "lims": [
    "Targeted search located only arXiv 2602.11865 (Feb 2026, pre-window); no in-window DeepMind enterprise-facing synthesis artifact captured.",
    "Underlying research must still be screened separately per target; nothing here establishes a W34-dated publication.",
  ],
  "verif": [("UNRESOLVED", "No in-window research artifact captured; underlying February paper is background only per target.")],
},
})
