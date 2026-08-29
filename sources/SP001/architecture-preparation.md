# SP001 — Architecture preparation for clean post-redesign validation

Status: `EDITORIAL ARCHITECTURE PREPARATION / NOT CANONICAL ARCHITECTURE_ESTABLISHED`

Reviewed Core / starting `main`: `2cb52dc293484a5c2ddd3caf9c909f18f4699c49`

Basis prepared from:

- `docs/thematic-special-backlog.md` / `TS-001`
- `sources/SP001/research-scope-v2.json`
- `sources/SP001/intake/postmerge-primary-source-intake.md`

This document records the proposed editorial structure while canonical Discovery → Screening → Evidence → Completeness → Candidate Matrix → Selection validation is completed. It intentionally does not invent candidate IDs or SHA bases that only the canonical Core can establish.

## Editorial thesis

中国発Generative AIの台頭は、一つの“Chinese LLM”系譜が急成長した物語ではない。2022–2024年に形成された複数のmodel familyが、**sparse/efficient architecture、long context、reasoning/post-training、multimodality、agentic execution、open-weight distribution、serving/runtime ecosystem**という別々の競争軸を発達させ、2025–2026年にそれらが相互参照・技術再利用を伴いながらfrontier systemへ収束した、と捉えるべきである。

そのため本巻は「中国勢 vs 米国勢」の単純なbenchmark順位表ではなく、DeepSeek、Qwen、GLM、Kimiの異なる技術・distribution戦略を維持しながら、なぜopen-weight modelがfrontier競争の重要な構成要素になったのかを説明する。

## Architecture goals

1. 2022–2026のchronologyを作るが、chronologyだけで直接の技術系譜を推定しない。
2. DeepSeek / Qwen / GLM / Kimiを個別familyとして扱い、戦略差を最後まで保持する。
3. reasoning/coding/agentic化を単なるbenchmark上昇ではなく、training/post-training/runtimeの変化として説明する。
4. MoE、MLA/DSA/KDA等のefficiency・attention・serving技術を、何を節約し何を可能にしたかまでreader-facingに説明する。
5. Open Source / Open Weight / code license / model license / redistribution / commercial use / reproducibilityを混同しない。
6. Hugging Face、ModelScope、API互換性、vLLM/SGLang/KTransformers等を「配布後の付録」ではなく競争力の一部として扱う。
7. closed frontier modelとの比較は同一条件の証明がある場合に限定し、それ以外は各一次資料が報告した位置づけとして表現する。
8. 最終総括では、2026年時点の中国model ecosystemの強みと未解決境界を技術・distribution・evidenceの三層に分けてまとめる。

## Proposed package plan

### PKG-1 — 単一の系譜ではなかった：中国LLMの基盤形成

**Purpose**

GLM-130B、Baichuan 2、Yi、初期Qwen、DeepSeek LLMなどを使い、2022–2024年の基盤形成を説明する。後年の勝者だけを遡って“起源”にしない。

**Must cover**

- `SP001-O01`: 主要familyの一次資料に基づくchronology。
- `SP001-O02`: 複数familyが早期から異なるorganization / design / distributionを持っていたこと。
- bilingual / Chinese-English pretraining、base/instruct、model size、long-contextの初期差。
- Baichuan/Yiは主要4familyを理解する補助線として扱い、無理に同格chapterへ膨張させない。

**Boundaries**

- publication dateの近さだけで直接影響関係を主張しない。
- “China's first/best”型priority claimは一次資料で厳密に閉じられない限り避ける。

### PKG-2 — 四つのfamily、四つの戦略

**Purpose**

DeepSeek、Qwen、GLM、Kimiを別々の技術trajectoryとして並べ、後段の横断比較に必要なidentityを確立する。

**Must cover**

- `SP001-O02`: family identityとstrategy差。
- DeepSeek: V2 → V3 → R1 → V4 の効率・reasoning・agentic収束。
- Qwen: Qwen2 → Qwen3 → Qwen3.8のmodel breadth、thinking/non-thinking、multilingual、distribution。
- GLM: GLM-130B / ChatGLM → GLM-4 → 4.5 → 5 の研究系譜、long context/tool use、agentic engineering。
- Kimi: k1.5 → K2/K2.5 → K3 のlong-context、multimodal reasoning、efficient attention、Agent productization。

**Boundaries**

- family間で似たtechniqueが使われても、証拠なしに“派生”“追随”と書かない。
- model-name chronologyとtechnical architecture chronologyを区別する。

### PKG-3 — 計算資源をどう使うか：sparsity、attention、serving

**Purpose**

中国model競争の重要な特徴を“巨大化”ではなく、total/active parameter、KV/cache pressure、attention complexity、training/post-training throughput、runtime supportなどのsystems問題として説明する。

**Must cover**

- `SP001-O04`: training / inference efficiencyとserving。
- DeepSeekMoE + MLA、V4のsparse/long-context方向。
- GLM-5におけるDSA利用とRL infrastructure。
- Kimi KDA / high-sparsity MoE / 1M context。
- MiniMax-01を独立したLightning Attention系のcounterexampleとして必要な範囲で使用。
- vLLM / SGLang / KTransformers等のdeployment pathがmodel adoptionへ与える意味。

**Boundaries**

- FLOP/GPU-hour/costを異なるhardware・precision・accounting条件で直接比較しない。
- “efficient”はsource-local metricまたは仕組みの説明に分解する。

### PKG-4 — ChatからReasoning、Coding、Agentへ

**Purpose**

2024–2026の能力変化を、RL/post-training、thinking mode、tool use、long-horizon execution、multimodalityの統合として説明する。

**Must cover**

- `SP001-O03`: reasoning / coding / long-context / agentic transition。
- DeepSeek-R1のRL reasoningとV4のagentic/1M-context化。
- Qwen3のthinking/non-thinkingとthinking budget、Qwen3.8のlong-horizon agent emphasis。
- GLM-4.x/5のtool use / hybrid reasoning / agentic engineering。
- Kimi k1.5のmultimodal RLからK3のnative multimodal agentic systemへの展開。

**Boundaries**

- benchmark順位をchapter骨格にしない。
- “reasoning”はtraining method、inference mode、reported capabilityを分離して書く。
- Agent benchmarkと実製品Agent integrationを混同しない。

### PKG-5 — Open Weightはdistribution strategyである

**Purpose**

weights公開、license、runtime、cloud/API、model hub、fine-tuning/quantizationがどのようにdeveloper adoptionを形成したかを扱う。

**Must cover**

- `SP001-O05`: developer ecosystem / distribution。
- `SP001-O06`: open-weight / licensing boundary。
- Hugging Face + ModelScopeによる二重配布、国内外developer access。
- OpenAI-compatible API等によるmigration/integration friction低減。
- Qwenの多runtime compatibility、GLMのvLLM/SGLang/xLLM/KTransformers、DeepSeek/Kimiのserving support。
- DeepSeek-V3のcode/model license分離、R1 primary weightsとdistilled derivativeのupstream license差。
- Qwen3 Apache-2.0と、Qwen3.8各checkpointのweight licenseをartifact-levelで確認する必要性。

**Boundaries**

- “open source”という総称を使う場合はOSI的source availabilityを暗示しないよう文脈を限定する。
- training data / full recipe / optimizer detailsが非公開なら、weights公開だけでreproducibleとは書かない。

### PKG-6 — 2026年のfrontier構造：収束したもの、残った差

**Purpose**

DeepSeek V4、Qwen3.8、GLM-5、Kimi K3を使い、2026年時点で共通化した設計圧力と、なおfamilyごとに異なる戦略を総括する。

**Must cover**

- `SP001-O07`: competition and boundaries。
- 1M級context、sparse MoE、efficient/sparse attention、dual/hybrid reasoning、multimodality、agentic coding/engineering、tool/runtime ecosystemという収束軸。
- architecture convergenceがorganization / distribution / license / product strategyの同一化を意味しないこと。
- closed frontier model比較は一次資料のsource-local claimとして位置づけ、横断league tableは作らない。
- policy/geopoliticsはcompute access、distribution、international adoption等のtechnical historyに直接必要な範囲のみ。
- final synthesis: なぜ2026年までに中国発open-weight ecosystemがfrontier competitionの恒常的な構成要素になったのか。

**Boundaries**

- “frontier”を単一benchmarkの閾値として定義しない。
- 2026年8月以降の情報をas-of内へ混入させない。

## Candidate selection principle

Canonical Candidate Matrixが作られた後は、少なくとも以下を`PRIMARY`相当として選択する方向が妥当である。

- DeepSeek V2 / V3 / R1 / V4
- Qwen2 / Qwen3 / Qwen3.8
- GLM-130BまたはChatGLM-family anchor / GLM-4.x / GLM-5
- Kimi k1.5 / K2-or-K2.5 anchor / K3

Baichuan 2、Yi、MiniMax-01は`SUPPORTING`を基本とし、主要4familyでは説明できない基盤形成・alternative architectureを閉じるために使う。これは事前のeditorial hypothesisであり、canonical Matrix/Selectionが異なるmaterialityを示した場合はそちらに従う。

## Human Review attention candidates

Architecture ReviewでOwnerに特に見てもらうべき点は以下。

1. **四familyを主軸にする粒度** — MiniMaxを独立主軸へ昇格させるか、alternative architectureの補助線に留めるか。
2. **2026年比重** — 歴史巻として2026 frontier convergenceをどこまで厚くするか。現案は全体の結論として重要だが、最新model catalog化は避ける。
3. **Open Weight章の比重** — 技術性能だけでなくdistribution/license/runtimeを競争力の中核として1 package確保する方針。
4. **geopoliticsの境界** — export control等を扱う場合も、technical trajectoryを説明する直接因子に限定する。

## Current readiness assessment

Research breadth is sufficient for a six-package Architecture proposal, and all seven initial obligations have an explicit destination. Remaining work before the **canonical** Architecture Review gate is mechanical/provenance-sensitive rather than a request for new editorial direction:

1. materialize canonical Production Profile/State from the integrated Core;
2. convert intake records to Discovery with exact Raw/source provenance;
3. run Screening and Evidence verification;
4. close Profile Completeness and Materiality;
5. derive Candidate Matrix and author Candidate Selection;
6. generate `architecture-v2.json`, review summary and attention files from exact upstream bytes;
7. run exact stage validation and Stage Checkpoint.

Until those steps have actually passed, this document must not be presented as `ARCHITECTURE_ESTABLISHED`.
