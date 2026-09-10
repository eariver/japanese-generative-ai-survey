# W34 Sol Architecture Directive r1

Status: `SOL_ARCHITECTURE_DIRECTIVE_R1 / MATERIALIZATION_AUTHORIZED / STOP_AT_FRESH_HUMAN_ARCHITECTURE_REVIEW`

Date: `2026-09-10 JST`

## Authority and basis

This is the Sol-owned Architecture decision following:

- Sol Discovery Review r2 PASS;
- Sol Evidence Authority-Consumption Review r1 PASS;
- Human-approved Core source-class repair PR #486 and integration;
- Sol Selection Directive r2;
- Sol Selection Review r2 PASS.

Canonical Selection is `w34-sol-selection-r2`:

- candidates = 409
- SELECTED = 41
- HOLD = 368
- PRIMARY = 10
- SUPPORTING = 31

The executor may materialize this directive into the canonical Architecture / Review Summary / Review Attention artifacts and stage checkpoint. The executor must not change the semantic decisions below.

Human remains the decision authority at the resulting Architecture Review.

---

## Editorial thesis

W34の生成AIは、単体モデルの性能競争よりも、agentが実際の業務・取引・共同作業の中で「何を実行できるか」、その実行を「どのpolicy・authorization・memory・security境界で制御するか」、さらに「どの価格・region・provider・multimodal surfaceで配備できるか」へ重心が移った週として読む。

Payments、Computer Use、Slack code channels、Agentic Searchを中心に、個別releaseを羅列するのではなく、**agent executionのproductionization**を主軸とする。その外周としてsafety/security governance、model economics/distribution、creative multimodal production、gateway/infrastructure economicsを配置し、「モデルが賢くなったか」から「何が、どこで、いくらで、どの統制下で実行可能になったか」へ読者の問いを移す。

---

## Architecture goals

1. 41 selected candidatesを41本の記事へ展開せず、相互関係が読める6つのsubstantive packageへ圧縮する。
2. AgentのproductionizationをW34の中心に置き、payments / computer use / policy / memory / authorizationとcollaborative workflow / retrieval / tool orchestrationを別の技術層として見せる。
3. `collaborative-agent-workflows`と`retrieval-tool-orchestration`は、共同作業surface上でagentが検索・navigation・tool/MCPを実行する一続きのreader questionとして1 packageへ統合する。
4. Model base releaseと、pricing / provider availability / regional processing / cross-region inference / local accessibilityを混同しない。
5. Security/safetyではvendor safety narrative、independent vulnerability research、CISA/official operational evidenceをsource roleごとに分離する。
6. Creative/multimodalでは個別model launchの列挙ではなく、production availability・migration・audio/image/video/vision surfaceの変化として束ねる。
7. Infrastructure/economicsはmodel/product updateから切り離し、gateway consolidationとcompute commitmentがdeployment economicsへ与える構造変化として扱う。
8. Evidence statusがPARTIALのselected supporting candidateをVERIFIED相当に書き換えず、各packageでsource-specific limitationを保持する。
9. 368 HOLD candidatesを「調査しなかったもの」にせず、Human Architecture Reviewでnegative space / omission rationaleとして可視化する。
10. 最後に独立した`WEEKLY_SYNTHESIS / WEEK_IN_REVIEW` packageを置き、6 substantive packageを横断して「今週何が変わったか・なぜ重要か・次に何を見るか」を総括する。

---

## Page plan

Canonical page plan:

- `target_pages = 20`
- `max_pages = 26`

Interpretation:

- six substantive packages: approximately 15 pages total
- WEEKLY_SYNTHESIS: approximately 2 pages
- cover / contents / source notes / layout slack: approximately 3 pages

Selected-candidate count must not mechanically determine page count.

Package target guidance:

1. Agent Control Plane: 3 pages
2. Collaborative Agent Workflows & Retrieval: 3 pages
3. Safety & Security Governance: 3 pages
4. Model Economics & Distribution: 3 pages
5. Creative Multimodal Production: 2 pages
6. Ecosystem & Infrastructure Economics: 1 page
7. WEEKLY_SYNTHESIS / WEEK_IN_REVIEW: 2 pages

These are editorial targets, not a reason to silently drop selected evidence.

---

# Package architecture

## Package 1 — `w34-agent-control-plane`

Title:

`Agent Control Plane — 取引・Computer Use・policy・memoryを誰が統制するか`

Purpose:

Agentが単なるtool-calling demoから、payment、computer/browser use、durable execution、memory、authorization、policy enforcementを伴うproduction execution surfaceへ移る変化を示す。

Candidate placement rule:

- include every selected candidate whose `architecture_role == WEEKLY:agent-control-plane`
- preserve Selection `architecture_usage` exactly
- expected: PRIMARY 2 / SUPPORTING 6 / total 8

Must cover:

- Amazon Bedrock AgentCore Paymentsを、payment API/MCP、guardrail、observabilityの実装surfaceとして説明し、vendorの「safe at scale」表現は結果事実として採用しない。
- Claude Platform Computer Use / Skills API / Files APIのGA surfaceを分け、computer useとbrowser-use toolを同一語で潰さない。
- authorization context、policy authoring、memory extraction、async executionを個別releaseとして増殖させず、control-plane capabilitiesとして接続する。
- Alipay agentic commerceはmerchant/ecosystem規模のcompany claimと、Skills/MCP/AHA等の確認可能なmechanismを分離する。

Boundaries to preserve:

- regional coverage / merchant scale / outcome claims where not exhaustively established;
- vendor-described safety or scalability is not independently demonstrated;
- supporting AWS policy/memory records may describe capability architecture rather than a distinct launch event.

Publication guidance:

- section kind: `FEATURE`
- target: 3 pages
- use a compact control-plane diagram or table conceptually separating execution / authorization / memory / transaction / observability; do not invent implementation details beyond Evidence.

---

## Package 2 — `w34-collaborative-agent-workflows-retrieval`

Title:

`Agent Workflows — Slack・IDE・Search・MCPが一つの作業面へ近づく`

Purpose:

Agent executionが1人のchat/sessionから、Slack、IDE、team collaboration、search/navigation、MCP/workflow surfaceへ広がる流れを一つのreader questionとして整理する。

Candidate placement rule:

Include every selected candidate whose architecture role is either:

- `WEEKLY:collaborative-agent-workflows`
- `WEEKLY:retrieval-tool-orchestration`

Preserve Selection `architecture_usage` exactly.

Expected combined placement:

- PRIMARY 2
- SUPPORTING 10
- total 12

Primary anchors:

- Slack Code channels
- Mistral Agentic Search

Must cover:

- Slack code channelsをagent coding workのshared channel化、artifact/audit/collaboration surfaceとして説明する。
- Mistral Agentic Searchをsearch/open/navigate/read/refineのmulti-step retrieval loopとして説明し、vendor benchmarkはmaker-reportedと明示する。
- Runway MCP workflow support、Kimi Code CLI、Gemini/Antigravity、OpenAI/Replit、GitHub Slack/Teams/JetBrainsなどを、個別ニュースの列ではなく「agent work surfaceの拡張」として配置する。
- Grok BotはAug 21 first-party X observationと現行Aug 26 page re-dateのchronology conflictを保持し、Aug 26 pageをAug 21 exact datelineとして使用しない。
- GitHub Slack/Teams supporting rowsでcandidate-specific body wordingが限定的な場合、機能をEvidence以上に具体化しない。

Boundaries to preserve:

- maker-reported benchmark figures for Agentic Search;
- Grok Bot Aug 21 / Aug 26 chronology provenance;
- GitHub Slack/Teams claim-text capture limitations where applicable;
- regional processing is NOT part of this package after Selection r2; it belongs to Package 4.

Publication guidance:

- section kind: `FEATURE`
- target: 3 pages
- organize around `shared work surface -> retrieval/navigation -> tool/MCP execution -> collaboration/audit` rather than provider-by-provider chronology.

---

## Package 3 — `w34-safety-security-governance`

Title:

`Safety & Security Governance — 利用者routingからagent attack chainまで`

Purpose:

W34のsafety/security変化を、teen routing、frontier capability pacing、privacy/retention、provenance/compliance、operational vulnerability evidenceという異なるgovernance layerに分解する。

Candidate placement rule:

- include every selected candidate whose `architecture_role == WEEKLY:safety-security-governance`
- preserve Selection `architecture_usage` exactly
- expected: PRIMARY 2 / SUPPORTING 5 / total 7

Primary anchors:

- ChatGPT for Teens
- CoSnitch / CVE-2026-24301 chain

Must cover:

- ChatGPT for Teensのage routing、teen safeguards、Study Mode等をfirst-party supported claimsとして扱い、旧generic-placeholder欠陥を再発させない。
- CoSnitchをindependent researcher evidenceとして扱い、vendor advisory bytesが取得できていない箇所をMicrosoft公式断定へ変換しない。
- CISA KEV、OpenAI pacing、ZDR/Private Safety Processing、watermarking、Defender's Windowをそれぞれoperational / vendor governance / compliance narrativeとしてsource roleを分ける。
- safety claimとsecurity mechanismのどちらも「安全になった」という一語へ圧縮しない。

Boundaries to preserve:

- age-estimation/safeguard effectivenessはvendor-described;
- independent exploit researchとvendor confirmationの区別;
- pacing/security essaysはtechnical narrativeでありindependent outcome evidenceではない;
- dateline/page-time precision limits where recorded.

Publication guidance:

- section kind: `SECURITY_GOVERNANCE`
- target: 3 pages
- use a layered framing: user routing / model capability governance / data handling / provenance / vulnerability response.

---

## Package 4 — `w34-model-economics-distribution`

Title:

`Model Economics & Distribution — 新モデルより「どこで、いくらで使えるか」`

Purpose:

Base-model announcementと、価格、provider availability、region coverage、regional processing、cross-region inference、local/open deploymentを明確に分け、deployabilityの変化として比較する。

Candidate placement rule:

- include every selected candidate whose `architecture_role == WEEKLY:model-economics-distribution`
- preserve Selection `architecture_usage` exactly
- expected: PRIMARY 2 / SUPPORTING 5 / total 7

Primary anchors:

- GPT-5.6 Sol W34 pricing/access delta
- Qwen3.8-27B availability/local adoption

Must cover:

- GPT-5.6 SolのAug 21 promotional pricing/access deltaをbase releaseや以前のTerra/Luna pricing changeと分離する。
- Qwen3.8-27Bはofficial availabilityとcommunity/local optimizationを分け、exact release timeが未確定ならその境界を残す。
- Grok 4.6 Bedrock、AWS cross-region inference、DeepSeek V4-Pro、Alibaba kimi-k3 Model Studioをdistribution/service deltasとして扱う。
- `OpenAI API regional processing` (`w34-event-c045`)をこのpackageのSUPPORTINGとして必ず配置する。retrieval/tool packageへ戻してはいけない。
- provider distribution dateとmodel base release dateをmodel名だけでcollapseしない。

Boundaries to preserve:

- exact Qwen release timing where unresolved;
- DeepSeek tariff figures relying partly on secondary reporting;
- provider availability is not equivalent to new model release;
- promotional pricing has a bounded validity period.

Publication guidance:

- section kind: `MARKET_TECHNICAL`
- target: 3 pages
- prefer a deployability comparison table: model/base event vs provider/service availability vs region vs price/access boundary.

---

## Package 5 — `w34-creative-multimodal-production`

Title:

`Creative Multimodal Production — 生成機能からproduction surfaceへ`

Purpose:

Audio/image/video/visionの動向を個別モデル名の列ではなく、実際のproduction availability、migration、API/tool surfaceの更新として整理する。

Candidate placement rule:

- include every selected candidate whose `architecture_role == WEEKLY:creative-multimodal-production`
- preserve Selection `architecture_usage` exactly
- expected: PRIMARY 1 / SUPPORTING 4 / total 5

Primary anchor:

- Adobe Firefly audio tools

Must cover:

- Firefly Generate Music / Speech / Sound EffectsのGAを中心に置く。
- Imagen shutdown -> Gemini image migrationをavailability/migration eventとして扱う。
- Pika audio model family、Alibaba wan3.0-video-prime、DeepSeek experimental vision/multimodal APIをproduction surfaceの比較として扱う。
- Alibaba wan3.0-video-prime Aug 20 service availabilityとlater Runway integrationを混同しない。

Boundaries to preserve:

- commercial-safety claims remain vendor framing;
- capability quality is not inferred from availability alone;
- migration/deprecation event and new-model launch are distinct identities.

Publication guidance:

- section kind: `MULTIMODAL`
- target: 2 pages
- emphasize workflow surface and migration paths rather than benchmark ranking.

---

## Package 6 — `w34-ecosystem-infrastructure-economics`

Title:

`Ecosystem & Infrastructure Economics — Gateway統合と8GW級compute commitment`

Purpose:

AI stackの構造変化を、gateway consolidation / payments ecosystemと大規模compute commitmentの二点から短く示し、個別モデル記事とは別レイヤとして位置づける。

Candidate placement rule:

- include every selected candidate whose `architecture_role == WEEKLY:ecosystem-infrastructure-economics`
- preserve Selection `architecture_usage` exactly
- expected: PRIMARY 1 / SUPPORTING 1 / total 2

Primary anchor:

- OpenRouter joining Stripe

Supporting:

- OpenAI PORTS-Pike ~8GW agreement

Must cover:

- Stripe/OpenRouter transaction/integration eventはfirst-party confirmationに限定し、gateway scale figuresはcompany-reportedと帰属させる。
- PORTS-Pike agreementはcompute/infrastructure commitmentとして扱い、将来価格や競争優位を事実として推定しない。
- 両者を「AI infrastructure economics」の上下流として接続するが、直接因果を捏造しない。

Boundaries to preserve:

- company-reported scale figures;
- economic implications are analysis, not directly proven outcomes;
- contract/agreement capacity is not identical to deployed capacity.

Publication guidance:

- section kind: `ECOSYSTEM`
- target: 1 page
- keep concise; this is structural context, not the issue's dominant package.

---

## Package 7 — `w34-week-in-review`

Title:

`WEEKLY_SYNTHESIS / WEEK_IN_REVIEW — Agent productionizationが変えた今週の読み方`

Purpose:

六つのsubstantive packageを横断し、W34を「agent productionization」「governed execution」「deployability」という三つの軸で総括する。

Candidate placement rule:

- `primary_candidate_ids = []`
- `supporting_candidate_ids = []`

This is the single permitted empty-placement cross-package synthesis package.
It must be final in drafting order.

Must cover:

- 今週の中心変化: agentがpayment/computer use/collaboration/searchまでproduction surfaceへ進んだこと。
- 制約側の変化: policy/authorization/memory/safety/securityがfeatureではなくexecution architectureの一部になったこと。
- deployability側の変化: pricing/region/provider/local availabilityがbase-model releaseと同じ程度に実用性を左右すること。
- next watch: agent transaction governance、browser/computer control boundaries、collaborative-agent auditability、regional deployment economics、security incident response。
- 368 HOLD candidatesを背景researchとして扱い、未選択=不存在とはしない。

Publication guidance:

- section kind: `WEEKLY_SYNTHESIS`
- target: 2 pages
- drafting_order must be last.

---

# Exact placement invariants

Architecture materialization must verify:

- every 41 SELECTED candidate appears exactly once across Packages 1-6;
- no HOLD candidate appears in any package;
- each selected candidate preserves its Selection usage:
  - PRIMARY -> package `primary_candidate_ids`
  - SUPPORTING -> package `supporting_candidate_ids`
- Package 7 contains no candidate placement;
- no `selected_exceptions` are required; expected `selected_exceptions = []`;
- total factual placement = 41;
- no candidate is duplicated across packages.

Expected package counts:

- Package 1: 2 PRIMARY + 6 SUPPORTING = 8
- Package 2: 2 PRIMARY + 10 SUPPORTING = 12
- Package 3: 2 PRIMARY + 5 SUPPORTING = 7
- Package 4: 2 PRIMARY + 5 SUPPORTING = 7
- Package 5: 1 PRIMARY + 4 SUPPORTING = 5
- Package 6: 1 PRIMARY + 1 SUPPORTING = 2
- Package 7: 0 + 0 = 0

Total: 10 PRIMARY + 31 SUPPORTING = 41.

---

# Negative-space / omission policy

Human Architecture Review must not show only the 41 selected candidates.

It must explain that 368 Matrix candidates remain HOLD because they are principally:

- researched CONTEXT that did not cross current W34 materiality;
- research-paper leads with partial/maker-reported evidence or insufficient weekly significance;
- unresolved authority/chronology cases retained as HOLD;
- product/provider deltas that are useful context but do not merit architecture placement.

Do not infer a target story count from 41 MATERIAL or 368 HOLD.

---

# Known limitations to expose at Human Architecture Review

The review dossier must explicitly expose at least:

- Evidence summary: VERIFIED 49 / PARTIAL 352 / NEEDS_MORE 8 across 409 non-DROP tasks;
- authority-consumption result from Sol Evidence Review, including the small residual non-consumed/not-found/retrieval-failed set;
- Profile Completeness remains `LIMITED`, not FULL;
- Grok Bot Aug 21 first-party X observation vs current Aug 26 page re-date chronology boundary;
- Qwen exact release-time boundary;
- maker/vendor-reported performance/safety/economic claims are not independent outcomes;
- selected supporting candidates with partial evidence must retain source-specific limitations;
- the prior r1/r2 sparse-architecture failure and the reason this architecture now keeps all 41 MATERIAL candidates available as primary/supporting placements.

---

# Counterfactual architectures considered by Sol

Human review must include these plausible alternatives and rejection rationale.

## Alternative A — one package per seven Selection clusters

Rejected because `collaborative-agent-workflows` and `retrieval-tool-orchestration` answer one reader-level question about where agents perform shared work and how they retrieve/navigate/invoke tools. Keeping them separate would over-fragment a Weekly issue.

## Alternative B — model/provider-first organization

Rejected because it would revert to provider-by-provider release-note enumeration and obscure the stronger W34 pattern: production agent execution plus its control/deployment surfaces.

## Alternative C — safety/security-first issue

Rejected because safety/security is materially important but does not subsume payments, collaborative workflows, pricing/distribution, multimodal availability, and infrastructure economics.

## Alternative D — one large `agent stack` package

Rejected because it would over-compress distinct layers. Control-plane mechanisms, collaborative/retrieval work surfaces, and model deployment economics need separate reader questions and Evidence boundaries.

---

# Human Gate boundary

Authorized machine path:

`SELECTION_COMPLETE -> materialize Architecture r3 under this directive -> validate current-Core Architecture -> ARCHITECTURE_ESTABLISHED -> generate Architecture Review Summary/Attention -> fresh Human Architecture Review -> STOP`

Do not draft articles.
Do not run sidecar QA.
Do not build PDF.
Do not enter Publication Preview.

The final Human-facing Architecture Review is owned by Sol. Machine `READY_FOR_ARCHITECTURE_REVIEW` is necessary but not sufficient for approval.

Required executor stop marker:

`SOL_ARCHITECTURE_REVIEW_REQUIRED`

and:

`HUMAN_ARCHITECTURE_REVIEW_READY`
