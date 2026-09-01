# Generative AI Foundations — Thematic Special Series Plan

Status: `SCOPED / living design memo`  
Established: 2026-08-20  
Updated: 2026-08-21

## 1. Purpose

This document records the design of a long-running Thematic Special series that reconstructs the technical and intellectual lineages leading to modern generative AI and multimodal AI.

It is intentionally separate from `docs/thematic-special-backlog.md`.

- `docs/thematic-special-backlog.md` records mostly stand-alone Thematic Special candidates such as TS-001 through TS-003.
- This document describes a **multi-volume series** whose volumes depend on one another and whose overall architecture is expected to evolve while research and drafting proceed.

The series is not intended to be a comprehensive history of artificial intelligence, machine learning, computer vision, natural language processing, reinforcement learning, or robotics. Its primary scope is narrower:

> **Re-read the papers, methods, and research transitions that materially contributed to the conceptual or technical foundations of today's generative AI and multimodal AI, and explain what was inherited, what was replaced, and what was later recombined.**

Agentic AI, world models, and Physical AI may appear near the downstream edge of the series, but only where they arise naturally from generative, multimodal, sequence-model, search, or learned-world-model lineages. They are convergence endpoints and bridge topics, not a license to expand the project into a general history of agents or robotics.

The series should remain compatible with the Evidence-first philosophy of the Special pipeline. Historical significance is not a substitute for source verification.

---

## 2. Core editorial thesis

Modern generative AI did not emerge from a single linear sequence such as:

```text
Perceptron -> Backpropagation -> CNN -> Attention -> Transformer -> LLM
```

That story is too simple. Several partly independent traditions developed in parallel and later converged. The diagrams below are planning maps rather than claims of strict one-paper-to-one-paper descent.

```text
Learning / optimization
  adaptive learning + gradient methods + multilayer differentiation
    -> practical backprop-based multilayer learning
    -> scalable deep-network optimization

Vision
  Cognitron / Neocognitron
    -> gradient-trained CNNs
    -> ImageNet-era deep visual representation

Language / sequence
  neural language models -> distributed representations
  recurrent sequence models -> LSTM / encoder-decoder -> Seq2Seq -> neural Attention
  Attention + sequence representation -> Transformer -> large-scale language pretraining

Generative modeling (several related but non-identical branches)
  energy-based / stochastic models -> Boltzmann / RBM / DBN
  latent-variable neural generation -> VAE
  adversarial generation -> GAN
  diffusion probabilistic modeling -> DDPM -> latent / conditioned diffusion

Cross-architecture transfer
  Transformer + mature large-scale vision practice -> Vision Transformer
  learned visual representation + learned language representation
    -> image-language alignment -> multimodal foundation models

Search / decision / action
  classical search + reinforcement learning -> deep RL / neural-guided search
  learned generative environment models -> world-model approaches
  Transformer sequence modeling + offline decision data -> sequence decision models
  these lines may later recombine in agentic / embodied / Physical-AI systems
```

The series should therefore be understood as a **directed graph of research lineages**, not as a single chronological ladder.

Chronology remains important inside each lineage and when explaining cross-lineage influence, but chronology alone does not determine volume order. An arrow in a planning diagram means “useful technical or conceptual inheritance to investigate,” not automatically “direct historical ancestry.”

A second series-level thesis is equally important:

> **A dominant architecture may survive by absorbing many later ideas. Architectural continuity does not imply technical stasis.**

The Transformer used in frontier AI of the mid-2020s should therefore not be treated as an unchanged 2017 block diagram. MoE routing, modified or sparse attention, long-context mechanisms, residual-path redesign, multimodal inputs, post-training, test-time reasoning, tools, memory, and agentic orchestration may produce systems that are functionally far removed from the original paper while still remaining Transformer-derived at the neural substrate.

This distinction becomes especially important in the planned final volume.

---

## 3. Scope and inclusion rule

### 3.1 Primary scope

A topic belongs in the main series when its connection to today's generative AI or multimodal AI can be explained without inventing a retrospective relationship that the evidence does not support.

As a planning heuristic, prefer topics for which a meaningful path to current systems can be drawn in roughly two or three major conceptual transitions.

Examples:

```text
Neural distributed word representation / Word2Vec
  -> learned embeddings as reusable representation
  -> contextual token representation
  -> Transformer / LLM systems

Neocognitron
  -> hierarchical local visual processing
  -> trainable deep visual representation
  -> modern multimodal perception

Diffusion probabilistic modeling
  -> denoising diffusion
  -> latent / conditioned diffusion
  -> modern image and video generation

Deep RL + neural-guided search
  -> learned planning / search
  -> selected modern agentic inference patterns
```

These examples express conceptual continuity, not a claim that every later system directly descends from the named earlier work. In particular, Word2Vec is a representative landmark in distributed representation rather than the unique source of Transformer embeddings, and modern agent systems need not descend directly from AlphaGo-style search.

The two-or-three-transition rule is **not a mechanical gate**. Historically important bridge technologies may be included when the connection requires more steps but remains technically substantive.

### 3.2 Three planning tiers

Candidate material should be classified informally as:

- **Core** — the technical DNA remains clearly visible in current generative or multimodal systems.
- **Bridge** — not itself a generative-AI technique, but it handed over a major idea, architecture, learning paradigm, problem formulation, or engineering capability.
- **Context** — important for explaining why later research changed direction, but not a subject that needs its own volume by default.

Examples of likely Context material include parts of classical symbolic AI, expert systems, and early search research. They matter to the overall story, but the series must not expand into a general AI-history encyclopedia.

### 3.3 Explicit non-goal

Do not include a field simply because it is important to AI history.

For example, computer vision, game AI, reinforcement learning, robotics, knowledge representation, or expert systems should only receive detailed treatment where they clarify a lineage that reaches modern generative or multimodal AI, or where they provide a tightly bounded bridge into contemporary agentic, world-model, or Physical-AI systems.

The downstream bridge topics must remain subordinate to the series' central question:

> **How did today's generative and multimodal systems become technically possible, and what assumptions are now being challenged at the frontier?**

---

## 4. Unit of publication and page policy

The unit of the series is **not one paper**.

The preferred unit is:

> **one technical transition, one research question, or one coherent lineage segment per volume**.

Therefore:

- one volume may cover several papers;
- one paper may be revisited in several volumes from different lineages;
- one large theme may be split across several volumes;
- a planned volume may later be merged, split, inserted, removed, or renumbered;
- volume numbering is editorial structure, not a claim that the history itself is linear.

The current target is **roughly 40 pages or fewer per published volume**. This is a readability target rather than a rule that a single paper must fit in 40 pages. If a theme cannot be explained responsibly within that budget, split the theme instead of compressing away the necessary history or evidence.

---

## 5. Historical and evidence rules

### 5.1 Primary sources first

For technical claims, prioritize:

1. the original paper / proceedings / journal version;
2. author-maintained or institutional copies;
3. contemporaneous follow-up papers when needed to clarify what the original work did and did not establish;
4. later retrospectives only for historical interpretation, attribution disputes, or context that the original paper could not contain.

### 5.2 Hindsight is allowed, retroactive credit is not

The series is explicitly retrospective. Later knowledge may be used to explain significance.

However:

> **Use hindsight to explain a paper; do not use hindsight to assign the paper achievements it did not make.**

This rule is especially important for words such as `first`, `invented`, `origin`, `direct ancestor`, and `the same as today's ...`.

It also applies to terminology. Terms such as `foundation model`, `generative AI`, `self-supervised learning`, or `Physical AI` may be useful retrospective categories even when the historical paper did not use them. Reader-facing prose must distinguish a modern editorial label from the authors' original vocabulary when the distinction matters.

Examples of claims that require care:

- Backpropagation has a pre-1986 history; Rumelhart, Hinton, and Williams (1986) is a major dissemination and demonstration point, not a safe universal answer to “who invented backpropagation?”.
- Attention predates the Transformer; Bahdanau-style neural attention and the Transformer are distinct transitions.
- Natural gradient is historically and mathematically important, but it did not become the default optimizer for modern Transformer training.
- Neocognitron is an important ancestor in hierarchical visual modeling, but modern trainable CNNs also depend on later gradient-based formulations and engineering developments.
- Vision Transformer should not be presented as a simple architectural descendant of CNNs; it is better understood as a convergence of Transformer architecture with a mature large-scale vision ecosystem.
- Diffusion should not be presented as if it were merely the successor algorithm to VAE or GAN. These are distinct deep-generative approaches whose histories intersect but are not one simple chain.
- World Models and Decision Transformer are useful bridges for explaining learned environments and action-as-sequence modeling, but modern VLA / embodied foundation models must not be given a direct genealogy from those papers without evidence.
- A modern frontier model should not be called “post-Transformer” merely because it has heavily modified attention, MoE routing, very long context, or a sophisticated agentic stack. The neural substrate and the surrounding system architecture must be distinguished.

### 5.3 Explain both inheritance and abandonment

Each volume should ask:

- What problem existed before this work?
- How did the authors themselves formulate the problem?
- What did the proposed method actually do?
- What did the experiments establish at the time?
- Which ideas survived into later systems?
- Which parts were replaced, abandoned, or proved less central than expected?
- What did later researchers reinterpret about the work?
- Where, if anywhere, is its technical DNA visible in modern generative or multimodal AI?

---

## 6. Relationship to the first volume

The first volume is a special case.

### 6.1 Publication order

**Do not write the final manuscript of Volume 1 first.**

The current plan is:

1. maintain the Volume 1 draft in this document as a series-level architectural guide;
2. research and write Volume 2 onward;
3. while doing so, revise the Volume 1 draft whenever the detailed historical work changes the understanding of the overall lineage;
4. use the current Volume 1 draft as a policy and architecture reference when making scope decisions in later volumes;
5. only after the major Volume 2+ lineages have been written should Volume 1 be written as the final reader-facing overview.

This avoids locking the overview to assumptions that later primary-source work may overturn.

Here, “write Volume 1 last” means **last among the historical/foundational synthesis work**. It does not override the separate rule that the provisional frontier volume in Section 14 is the final scheduled publication of the series. The intended endgame is therefore:

```text
major Vol. 2+ foundational volumes substantially complete
  -> final architecture pass on the series
  -> write/finalize reader-facing Vol. 1 overview
  -> refresh the contemporary endpoint volumes as needed
  -> perform fresh frontier-wide Source Intake
  -> publish the Section 14 frontier volume last
```

### 6.2 Role of the draft

The Volume 1 draft below is therefore **not publication prose and not the first manuscript**. It is a living synopsis of the story the series currently expects to tell.

---

## 7. Volume 1 draft — series overview

### Provisional title

**生成AIの源流 — 探索・学習・表現・生成が合流するまで**

Alternative working title:

**生成AIはどこから来たのか — 現代AIを形作った複数の研究系譜**

### Draft purpose

Today's generative AI is often narrated as a recent sequence beginning with the Transformer and accelerating through large language models. That account is useful for current product history but insufficient as a technical history.

The systems now called generative AI inherit ideas from several older research programs: machine learning from examples, optimization under uncertainty, distributed representation, hierarchical visual processing, recurrent sequence models, probabilistic generative modeling, adversarial learning, attention, large-scale pretraining, reinforcement learning, and search.

Some of those traditions competed with one another. Some appeared to fail and later returned in new forms. Some did not directly survive but changed the questions the field asked.

Volume 1 should give the reader a map of those lineages before the later volumes examine them in detail.

### Draft section 1 — Before “deep learning”: competing ideas of intelligence

The opening should avoid pretending that early AI was simply an immature form of today's neural AI.

Early AI research explored several different answers to the question “what makes a machine intelligent?”

One answer emphasized **search**: enumerate possible actions or states, evaluate them, and choose a promising path. Game-playing research makes this idea especially visible. Minimax and heuristic search should appear here as examples of intelligence implemented through explicit exploration of alternatives rather than learned representation.

A second answer emphasized **symbolic reasoning**: represent facts and manipulate symbols according to rules.

A third answer emphasized **knowledge engineering**. Expert systems such as DENDRAL are useful not because modern generative AI directly descends from their implementation, but because they embody a contrasting design philosophy: much of the intelligence is supplied as explicit domain knowledge and heuristics.

A fourth answer emphasized **learning from examples**. This is the branch that eventually became dominant in deep learning, but Volume 1 should present it as one branch among several rather than as an inevitable winner known in advance.

The Japanese-language framing of a **first AI boom**, subsequent disappointment / winter, and a **second AI boom** centered strongly on expert systems and knowledge engineering should be used as historical orientation, because it helps explain the changing expectations placed on AI. However, these labels are retrospective periodizations whose dates and emphases vary by source and region. The volume must not imply that either an AI boom or an AI winter had one cause, one decisive paper, or one globally synchronized boundary.

In particular, the decline of early neural-network enthusiasm should not be reduced to a story in which one critique “killed” neural networks, and the later limits of expert systems should not be reduced to one technical failure. Funding, available computation and data, knowledge-acquisition cost, generalization limits, research fashion, and institutional context may all matter; the detailed claims should be fixed only after dedicated evidence work.

The reader-facing question for this section is:

> How much intelligence should the programmer explicitly specify, and how much should the machine acquire from data or interaction?

That question remains relevant even in modern systems through retrieval, tools, search, planning, external memory, and reinforcement learning.

### Draft section 2 — The neural branch: from units to adaptive learning

The neural lineage should begin with brief context on mathematical neuron models and then move quickly to the Perceptron and adaptive pattern classification.

Rosenblatt's Perceptron is important not merely as an old classifier, but as a concrete expression of the idea that behavior can be changed by an update rule driven by examples.

Shun-ichi Amari's 1967 work on adaptive pattern classifiers belongs here as a major Japanese contribution to the theory of learning under general pattern distributions, including convergence analysis under nonseparable distributions for the conditions treated in the paper. The later detailed volume must distinguish carefully between Amari's probabilistic/stochastic descent ideas, later stochastic-gradient terminology, and the many independent lines that contributed to modern stochastic optimization.

The limitation story around perceptrons must also be handled carefully. `Perceptrons` by Minsky and Papert is historically important, but the series should avoid the simplistic legend that a single book “killed neural networks.” The more useful question is what classes of systems were being analyzed, what limitations were actually established, and why multilayer learning remained technically difficult.

### Draft section 3 — Hidden representations become learnable

The next transition is not just “backpropagation was invented.”

The important shift for this series is that multilayer networks became a practical framework in which internal hidden units could learn task-relevant representations through error-driven optimization.

The 1986 Rumelhart-Hinton-Williams paper is a major landmark because it clearly demonstrates learning useful internal representations through back-propagated error. Its historical treatment should include earlier precursors rather than attributing the entire mathematical idea to 1986.

In parallel, Hopfield networks and Boltzmann machines developed another neural tradition: collective dynamics, energy functions, stochastic units, and probabilistic modeling. This lineage later connects to restricted Boltzmann machines, deep belief networks, energy-based modeling, and the broader history of generative learning.

### Draft section 4 — Vision and time create specialized architectures

General multilayer networks were not enough. Different data structures created different architectural pressures.

For vision, Fukushima's Cognitron and Neocognitron provide a major bridge toward hierarchical local feature processing and tolerance to positional variation. Later gradient-trained convolutional networks and LeNet turned related architectural ideas into trainable systems, and the ImageNet era showed what happens when architecture, data, computation, and optimization scale together.

For sequences, recurrent networks represented time through internal state. LSTM addressed the difficulty of learning long-range dependencies and became a central architecture for sequence modeling before the Transformer.

The point of this section is not to tell complete CNN or RNN history. It is to show that **representation was becoming structured around the modality and the dependency pattern of the data**.

### Draft section 5 — Deep learning returns, then scales

The 2000s revival should not begin at AlexNet alone.

Layer-wise unsupervised pretraining and deep belief networks helped re-establish the practical feasibility and research value of learning multiple levels of representation. They also belong to the generative-model lineage, not only to an optimization story.

AlexNet then marks a different transition: a large convolutional model, a large labeled dataset, GPU computation, rectifying nonlinearities, and practical regularization combined to produce a decisive ImageNet result.

Subsequent techniques such as improved initialization and activations, dropout, adaptive optimization, normalization, and residual connections helped turn deep networks from difficult research artifacts into a reusable engineering substrate.

Volume 1 should present “deep learning” not as one algorithm, but as the point at which representation learning, optimization, data scale, and compute scale became mutually reinforcing.

### Draft section 6 — Language becomes representation learning at scale

Language provides another route into modern generative AI.

Neural probabilistic language models made learned distributed word representations part of the language-modeling problem itself. Word2Vec then made continuous word-vector learning efficient and widely reusable at very large corpus scale. The later series should treat Word2Vec as a landmark in distributed representation, not as the unique origin of the embedding mechanisms used by Transformers.

RNN/LSTM encoder-decoder systems generalized neural models from fixed labels toward sequence generation. Seq2Seq made end-to-end sequence transformation a central neural problem, but encoding an entire source sequence into a fixed-dimensional vector made the representational bottleneck especially visible.

Bahdanau-style attention changed that problem formulation by allowing the decoder to dynamically use relevant parts of the source representation. Transformer then made a second and distinct move: attention became the principal computational architecture rather than an auxiliary mechanism attached to recurrence.

This distinction is central to the series:

> **Attention is not synonymous with Transformer.**

The later Transformer volume should show why removing recurrence mattered for dependency modeling and training parallelism, while avoiding a claim that all later Transformer advantages can be reduced to one property.

### Draft section 7 — Generative modeling was developing on several branches

Modern generative AI should not be narrated as an LLM-only history, nor should deep generative modeling be reduced to one succession in which VAE was replaced by GAN and GAN was replaced by Diffusion.

Energy-based and latent-variable models had long addressed the problem of learning distributions. In the 2010s, VAE and GAN provided two influential deep-generative frameworks with very different training principles.

Diffusion probabilistic models form another branch. Sohl-Dickstein et al. (2015) formulated a deep generative approach that progressively destroys structure with a forward diffusion process and learns a reverse process that restores it. DDPM later demonstrated a particularly influential denoising formulation for high-quality image synthesis; latent diffusion made high-resolution conditioned generation substantially more practical and used cross-attention as a flexible conditioning mechanism.

These branches influence one another and coexist in later systems, but the series should not draw a false direct genealogy among them simply because they can be arranged chronologically.

The series should therefore describe modern media generation as the convergence of multiple traditions rather than as a direct derivative of language models.

### Draft section 8 — Large-scale pretraining and multimodal convergence

Transformer-based generative pretraining made it possible to reuse one learned model across many language tasks. GPT-style generative pretraining, BERT-style bidirectional pretraining, ELMo-style contextual representation, and later text-to-text approaches should be treated as distinct answers to the same larger question: how much task-specific structure can be replaced by large-scale reusable pretraining?

The term `foundation model` is later than several works in this lineage. It may be useful editorially, but the final prose should not imply that early GPT, BERT, or ELMo papers described themselves using later terminology.

Scaling-law work made scaling behavior itself an explicit quantitative object of study, and GPT-3 demonstrated striking few-shot and in-context behavior at much larger model scale. This changed how users could specify some tasks: adaptation that previously required parameter updates could sometimes be expressed through examples or instructions placed in inference-time context.

In vision, ViT showed that image patches could be processed by a Transformer architecture at sufficient data scale. This should be explained as a transfer/convergence of Transformer methods into vision, not as a simple continuation of CNN architecture. CLIP then showed that large-scale natural-language supervision and contrastive learning could align image and text representations. Together with related work, these developments are major bridges from separate vision and language pipelines toward modern multimodal systems.

Instruction tuning and human-feedback methods form another required transition. A next-token model is not automatically a useful assistant; post-training changes the relationship between base-model capability and user-directed behavior.

This section should also prepare the reader for a later distinction:

> **A frontier AI product is increasingly a system around a foundation model, not merely a neural network considered in isolation.**

Reasoning effort, context management, tool use, retrieval, code execution, memory, multi-agent decomposition, and external environments may change effective capability without constituting a new neural backbone. The final volume should treat this system layer separately from claims about post-Transformer architecture.

### Draft section 9 — Search returns; generation reaches action

The final part of the overview should reconnect modern AI to the classical AI ideas introduced at the beginning.

Deep reinforcement learning demonstrated that neural networks could learn representations and actions together from high-dimensional inputs. AlphaGo then combined learned policy/value networks with tree search: learning did not simply replace search; it made search dramatically more effective in that system.

World-model research reframed generative modeling as learning aspects of an environment in which future trajectories can be generated or imagined. Decision Transformer showed that offline reinforcement-learning tasks could be recast as conditional sequence modeling over returns, states, and actions.

These works provide useful conceptual bridges toward current agentic and embodied systems, but the final series must not imply that contemporary VLA or Physical-AI systems are direct descendants of World Models or Decision Transformer unless later Source Intake establishes the specific connection.

The bridge to explore is broader:

```text
predict / generate text
  -> predict / generate perceptual content
  -> model possible future world states or trajectories
  -> model / generate actions conditioned on observations and goals
```

Physical AI should only be followed as far as this connection remains technically meaningful. The series is not intended to become a complete robotics history.

### Draft conclusion

The first volume should end by replacing the idea of a single “AI family tree” with a map of intersecting research rivers.

Modern generative and multimodal AI combines ideas that once belonged to separate communities:

- neural learning and stochastic optimization;
- representation learning;
- hierarchical perception;
- sequential prediction;
- probabilistic, latent-variable, adversarial, and diffusion-based generation;
- attention and Transformer architectures;
- large-scale pretraining and scaling;
- human-feedback post-training;
- search, reinforcement learning, and world modeling;
- increasingly, system-level reasoning, tool use, memory, and test-time computation.

The later volumes then revisit the turning points one by one, using original sources to distinguish what the work actually established from what later history made possible.

The series should finally return to the same map at the frontier and ask a different question:

> **Which of the assumptions inherited from the Transformer era are still structural foundations, which have become implementation details, and which are being replaced?**

---

## 8. Provisional volume architecture

This allocation is intentionally provisional. During research and drafting, volumes may be merged, split, inserted, removed, or renumbered.

The table describes **current editorial units**, not final publication commitments. Volume order is designed around reader prerequisites and coherent lineage segments; it is not a strict calendar chronology. A later-numbered volume may therefore revisit an earlier historical period when the series switches from one research lineage to another.

| Provisional volume | Working theme | Main material currently expected | Why it belongs in this series |
|---|---|---|---|
| **Vol. 1** | **生成AIの源流 — 総説** | Classical AI context and boom/winter framing; neural learning; representation; vision; sequence; generative modeling; Transformer; scaling; multimodal; search/action | Reader map for the complete series. Final manuscript is written after the major later volumes. |
| **Vol. 2** | **機械が学ぶという発想 — Perceptronと適応学習** | mathematical-neuron context; Rosenblatt; perceptron learning; Widrow-Hoff/ADALINE as needed; Amari 1967; separability and adaptation | Establishes learning-from-data and adaptive / stochastic-update ideas before deep networks without retroactively collapsing them all into modern SGD. |
| **Vol. 3** | **多層ネットワークを学習する — Backpropagationと内部表現** | multilayer-network problem; early gradient/backprop precursors; Rumelhart-Hinton-Williams; hidden representations | Connects error-driven optimization to learned internal representation. Avoid single-inventor mythology. |
| **Vol. 4** | **記憶・エネルギー・確率生成 — HopfieldからBoltzmannへ** | Hopfield networks; Boltzmann machines; stochastic units; energy functions; RBM / contrastive divergence as bridge | Important branch toward probabilistic neural generation, deep belief nets, and later energy-based thinking. |
| **Vol. 5** | **視覚を階層化する — NeocognitronからCNNへ** | Cognitron/Neocognitron; local receptive processing; LeCun-era trainable CNN / LeNet | Core ancestry of learned visual representation and later multimodal perception. |
| **Vol. 6** | **時間を記憶する — RNN、BPTT、LSTM** | recurrent representation; temporal credit assignment; vanishing/long-lag problem; LSTM | Necessary prehistory for Seq2Seq, Attention, and the meaning of replacing recurrence. |
| **Vol. 7** | **Deep Learning再興 — Unsupervised PretrainingとDeep Belief Nets** | RBM/DBN; greedy layer-wise training; autoencoder-related context; representation learning | Separates the 2006-era deep-learning revival from the later ImageNet/GPU revolution. |
| **Vol. 8** | **ImageNet Shock — データ・GPU・深いCNN** | ImageNet context; AlexNet; ReLU; GPU training; dropout/regularization as used in the transition | Shows how data scale, compute, architecture, and training practice jointly changed the field. |
| **Vol. 9** | **深いネットを実用基盤にする — Optimization、Normalization、Residual** | improved activations/initialization as needed; Adam; BatchNorm; LayerNorm; ResNet; residual pathways | These techniques form much of the engineering substrate later inherited or adapted by Transformer-scale models. |
| **Vol. 10** | **単語をベクトルにする — Neural Language ModelとWord2Vec** | Bengio et al. 2003; distributed representation; CBOW/Skip-gram; negative sampling; GloVe/contextual embeddings as needed | Makes the shift from symbolic word IDs toward learned continuous language representation explicit without treating Word2Vec as the sole origin of Transformer embeddings. |
| **Vol. 11** | **系列から系列へ — Encoder–DecoderとSeq2Seq** | neural machine translation context; recurrent encoder-decoder; Sutskever et al.; fixed-dimensional sequence representation | Establishes the problem setting that directly motivates Bahdanau-style neural attention. |
| **Vol. 12** | **Attention — 必要な場所を見るという転換** | Bahdanau et al.; alignment; attention before Transformer; Luong-style variants if useful; self-attention precursors | Attention is treated as its own conceptual transition rather than retrospectively collapsed into Transformer. No claim that Bahdanau is the first use of every concept called attention. |
| **Vol. 13** | **Transformer — Attentionを中心アーキテクチャにする** | `Attention Is All You Need`; self-attention; multi-head attention; positional information; residual/normalization; training parallelism | Principal architectural bridge into modern LLMs and many multimodal models. |
| **Vol. 14** | **事前学習が基盤になる — ELMo、GPT、BERT、T5周辺** | contextual representations; generative pretraining; bidirectional pretraining; transfer/fine-tuning; text-to-text unification as needed | Explains the shift from task-specific models toward reusable pretrained models. Use `foundation model` only as later editorial terminology where appropriate. |
| **Vol. 15** | **ScalingとIn-Context Learning — 大きくすると何が変わるのか** | GPT-2; empirical scaling laws; GPT-3; compute/data/model tradeoffs; Chinchilla-style revision if required | Treats scaling behavior as a quantitative design problem and follows the emergence of strong inference-time task specification. |
| **Vol. 16** | **Deep Generative Models — VAEとGANが示した二つの答え** | AEVB/VAE; adversarial training/GAN; latent spaces; conditional variants as needed | Establishes two major non-LLM deep-generative paradigms while avoiding a claim that one is a direct ancestor of diffusion. |
| **Vol. 17** | **Diffusion — 壊して戻す生成モデル** | Sohl-Dickstein et al.; score/denoising connections as needed; DDPM; guidance; Latent Diffusion | Direct lineage into modern image generation and an important branch of video/multimodal generation; treated as its own branch rather than “the successor to GAN.” |
| **Vol. 18** | **画像をTokenにし、言語と結ぶ — ViTとCLIP** | Vision Transformer; contrastive image-text pretraining; CLIP; related alignment work as needed | Major convergence point between Transformer methods, mature visual representation learning, and language supervision. |
| **Vol. 19** | **指示に従うモデル — Instruction TuningとHuman Feedback** | supervised instruction tuning; preference/reward modeling; RLHF; InstructGPT and important precursors | Distinguishes base-model capability from assistant-like behavior and post-training. |
| **Vol. 20** | **音声を生成する — 統計的音声合成からNeural Speechへ** | HMM-based speech synthesis; Tokuda et al.; WaveNet; Tacotron-family developments; neural codec / speech-generation bridges as needed | Prevents “generative AI” from becoming text/image-only history and creates a Japanese-research bridge into multimodality. |
| **Vol. 21** | **Multimodal Foundation Models — 理解と生成の合流** | vision-language models; cross-attention/projector/Q-former style bridges as appropriate; image/audio/video integration; unified modeling | Follows the convergence of previously separate modality-specific representation and generation systems. Exact papers should be selected near production time because this area changes quickly. |
| **Vol. 22** | **探索と学習の再会 — Deep RL、DQN、AlphaGo** | classical search context; Q-learning/RL context; DQN; AlphaGo/AlphaZero; neural-guided search | Bridge volume explaining why learning did not eliminate search and how selected ideas reconnect to modern reasoning/agent systems without claiming a universal direct ancestry. |
| **Vol. 23** | **World ModelからPhysical AIへ — 予測から行動へ** | World Models; model-based learned environments; Decision Transformer; later multimodal / VLA anchors as appropriate | Explores conceptual and architectural bridges from learned environments and sequence-modeled action toward embodied systems. Direct genealogy must be established case by case. |
| **Final (number TBD)** | **次のTransformer、その先へ — 現在の基盤パラダイムと次の転換** | first identify the actual practical substrate at series completion; reconstruct any already-established post-Transformer transition; then compare the strongest directions beyond it | Keeps the series open to the real frontier rather than freezing a 2026 forecast. This volume is always published last. |

### 8.1 Likely merge/split pressure

The following decisions should remain open until Source Intake / Architecture work for the corresponding volumes:

- Vol. 2 and Vol. 3 may need more space if the history of stochastic learning and backpropagation attribution cannot be handled responsibly in one volume each.
- Vol. 4 and Vol. 7 overlap through RBM / deep belief nets; intentional cross-reference is preferable to forcing artificial exclusivity.
- Vol. 8 and Vol. 9 may merge if the engineering story is short enough, or split further if optimization history becomes too dense.
- Vol. 10 may split `Neural Language Model` and `Word2Vec / distributed representation` if the representation-learning lineage requires more room.
- Vol. 12 should remain separate from Vol. 13 unless evidence work shows that a combined Attention/Transformer issue can preserve the conceptual distinction within the page budget.
- Vol. 14 and Vol. 15 may need a third volume if generative pretraining, transfer learning, scaling laws, and in-context learning cannot be treated without compression.
- Vol. 16 may split VAE and GAN if either requires a full generative-model treatment.
- Vol. 17 will probably span multiple papers by design; `diffusion` should not be represented as beginning with DDPM alone.
- Vol. 18 must explicitly distinguish the visual-representation lineage inherited from CNN-era research from the Transformer architecture imported into vision.
- Vol. 20 may expand beyond speech into audio/music only if doing so remains technically coherent; otherwise music/audio generation can be handled in a later multimodal or media-generation Special.
- Vol. 21 and Vol. 23 must be re-scoped near their production dates because their frontier reference points may change materially.
- The final volume has no stable paper list or number. Its content is determined only after a fresh frontier-wide Source Intake near series completion.

---

## 9. Cross-cutting Japanese research volume

### Status

`SCOPED concept / volume number TBD`

### Provisional title

**日本から生成AIへ — 学習・視覚・音声の源流**

### Editorial purpose

This should not become a “great Japanese researchers” catalogue and should not isolate Japanese work from the main technical history.

Instead, the volume should revisit research already placed in the main lineages and ask what becomes visible when those lineages are crossed from the perspective of research conducted in Japan or by Japanese researchers.

Current anchors include:

### Shun-ichi Amari — learning theory and geometry

Likely material:

- adaptive pattern classification;
- probabilistic / stochastic descent ideas;
- multilayer-network learning context where supported by primary sources;
- information geometry;
- natural gradient.

Editorial caution:

Do not collapse Amari's 1967 work into the modern optimizer label `SGD` without explaining differences in terminology, formulation, and historical development. Do not imply that natural gradient became the standard training method of today's LLMs.

### Kunihiko Fukushima — hierarchical visual representation

Likely material:

- Cognitron;
- Neocognitron;
- local feature extraction and hierarchical integration;
- tolerance to positional variation;
- later relation to trainable CNNs.

This material should also appear in the main vision lineage (Vol. 5). Repetition is acceptable when the question is different.

### Keiichi Tokuda and collaborators — statistical speech generation

Likely material:

- HMM-based speech synthesis;
- parameter generation from probabilistic speech models;
- audio-visual speech synthesis where useful;
- transition from statistical parametric synthesis to neural speech generation.

This gives the series a concrete way to show that generative modeling of speech had a mature research history before the current LLM/image-generation era.

### Further candidates

Additional Japanese researchers or groups should only be added after evidence work establishes a meaningful path to the series scope. Nationality alone is not an inclusion criterion.

The Japanese cross-cutting volume may be published after the relevant foundational volumes so that it can synthesize rather than prematurely duplicate them. If it remains part of the main series, the provisional final volume still follows it.

---

## 10. Game AI and Physical AI boundary

Game AI and Physical AI are allowed only as **bridge themes** into current generative/multimodal systems.

### Game AI

Do not write a general history of chess, Go, search algorithms, or reinforcement learning.

Use the lineage primarily to explain:

```text
classical explicit search
  + learned value / policy representations
  -> neural-guided search
  -> selected modern inference-time search / planning patterns
```

AlphaGo is particularly useful because policy/value networks and tree search are explicitly combined rather than presented as mutually exclusive paradigms. This is a conceptual bridge; later agent systems must not automatically be described as descendants of AlphaGo.

### Physical AI

Do not write a general robotics history.

Follow the branch only where generative and sequence-model ideas remain central:

```text
learn representations of observations
  -> learn/predict aspects of environment dynamics
  -> model possible future trajectories
  -> condition action generation on observations and goals
  -> multimodal / vision-language-action systems
```

World Models and Decision Transformer are currently useful bridge points, not presumed unique ancestors. The exact embodied/VLA papers used in the final volume should be selected during later Source Intake because this area is still changing rapidly.

---

## 11. Planning-level source anchors

This is **not** a completed Evidence inventory. These references were checked only to keep the present series architecture historically and technically plausible. Each production volume must perform its own complete Source Intake and Evidence work.

### 11.1 Classical / neural foundations

- Warren S. McCulloch, Walter Pitts, “A Logical Calculus of the Ideas Immanent in Nervous Activity” (1943), *Bulletin of Mathematical Biophysics* 5, 115–133.
- Frank Rosenblatt, “The Perceptron: A Probabilistic Model for Information Storage and Organization in the Brain” (1958), *Psychological Review* 65(6), 386–408. DOI: `10.1037/h0042519`.
- Shun-ichi Amari, “A Theory of Adaptive Pattern Classifiers” (1967), *IEEE Transactions on Electronic Computers* EC-16(3), 299–307. DOI: `10.1109/PGEC.1967.264666`.
- Marvin Minsky and Seymour Papert, *Perceptrons* (1969), MIT Press.
- John J. Hopfield, “Neural networks and physical systems with emergent collective computational abilities” (1982), *Proceedings of the National Academy of Sciences* 79(8), 2554–2558.
- David H. Ackley, Geoffrey E. Hinton, Terrence J. Sejnowski, “A Learning Algorithm for Boltzmann Machines” (1985), *Cognitive Science* 9, 147–169.
- David E. Rumelhart, Geoffrey E. Hinton, Ronald J. Williams, “Learning representations by back-propagating errors” (1986), *Nature* 323, 533–536. DOI: `10.1038/323533a0`.
- Shun-ichi Amari, “Natural Gradient Works Efficiently in Learning” (1998), *Neural Computation* 10(2), 251–276. This is a later Japanese cross-cutting anchor, not evidence that natural gradient became the default optimizer for modern LLMs.

### 11.2 Vision and deep learning

- Kunihiko Fukushima, “Neocognitron: A self-organizing neural network model for a mechanism of pattern recognition unaffected by shift in position” (1980), *Biological Cybernetics* 36, 193–202. DOI: `10.1007/BF00344251`. A Japanese precursor paper appeared in IEICE in 1979.
- Yann LeCun et al., “Gradient-Based Learning Applied to Document Recognition” (1998), *Proceedings of the IEEE* 86(11), 2278–2324.
- Geoffrey E. Hinton, Simon Osindero, Yee-Whye Teh, “A Fast Learning Algorithm for Deep Belief Nets” (2006), *Neural Computation* 18, 1527–1554.
- Alex Krizhevsky, Ilya Sutskever, Geoffrey E. Hinton, “ImageNet Classification with Deep Convolutional Neural Networks” (2012), NeurIPS 25.
- Kaiming He et al., “Deep Residual Learning for Image Recognition” (2015/2016), CVPR 2016 / arXiv:1512.03385.

### 11.3 Language / sequence / Transformer

- Sepp Hochreiter, Jürgen Schmidhuber, “Long Short-Term Memory” (1997), *Neural Computation* 9(8), 1735–1780.
- Yoshua Bengio et al., “A Neural Probabilistic Language Model” (2003), *JMLR* 3, 1137–1155.
- Tomas Mikolov et al., “Efficient Estimation of Word Representations in Vector Space” (2013), arXiv:1301.3781.
- Kyunghyun Cho et al., “Learning Phrase Representations using RNN Encoder–Decoder for Statistical Machine Translation” (2014), arXiv:1406.1078 / EMNLP 2014.
- Ilya Sutskever, Oriol Vinyals, Quoc V. Le, “Sequence to Sequence Learning with Neural Networks” (2014), arXiv:1409.3215 / NeurIPS 2014.
- Dzmitry Bahdanau, Kyunghyun Cho, Yoshua Bengio, “Neural Machine Translation by Jointly Learning to Align and Translate” (2014), arXiv:1409.0473 / ICLR 2015.
- Ashish Vaswani et al., “Attention Is All You Need” (2017), NeurIPS 30.
- OpenAI, “Improving Language Understanding by Generative Pre-Training” / accompanying 2018 research release.
- Jacob Devlin et al., “BERT: Pre-training of Deep Bidirectional Transformers for Language Understanding” (2018/2019), NAACL 2019.
- Jared Kaplan et al., “Scaling Laws for Neural Language Models” (2020), arXiv:2001.08361.
- Tom B. Brown et al., “Language Models are Few-Shot Learners” (2020), arXiv:2005.14165.

### 11.4 Deep generative modeling

- Diederik P. Kingma, Max Welling, “Auto-Encoding Variational Bayes” (2013), arXiv:1312.6114 / ICLR 2014.
- Ian Goodfellow et al., “Generative Adversarial Nets” (2014), NeurIPS 27.
- Jascha Sohl-Dickstein et al., “Deep Unsupervised Learning using Nonequilibrium Thermodynamics” (2015), ICML 2015 / PMLR 37:2256–2265.
- Jonathan Ho, Ajay Jain, Pieter Abbeel, “Denoising Diffusion Probabilistic Models” (2020), arXiv:2006.11239 / NeurIPS 2020.
- Robin Rombach et al., “High-Resolution Image Synthesis with Latent Diffusion Models” (2021/2022), arXiv:2112.10752 / CVPR 2022.

### 11.5 Multimodal / alignment / action

- Alexey Dosovitskiy et al., “An Image is Worth 16x16 Words: Transformers for Image Recognition at Scale” (2020/2021), arXiv:2010.11929 / ICLR 2021.
- Alec Radford et al., “Learning Transferable Visual Models From Natural Language Supervision” (2021), arXiv:2103.00020.
- Nisan Stiennon et al., “Learning to summarize from human feedback” (2020), arXiv:2009.01325.
- Long Ouyang et al., “Training language models to follow instructions with human feedback” (2022), arXiv:2203.02155.
- Volodymyr Mnih et al., “Human-level control through deep reinforcement learning” (2015), *Nature* 518, 529–533.
- David Silver et al., “Mastering the game of Go with deep neural networks and tree search” (2016), *Nature* 529, 484–489.
- David Ha, Jürgen Schmidhuber, “World Models” (2018), arXiv:1803.10122.
- Lili Chen et al., “Decision Transformer: Reinforcement Learning via Sequence Modeling” (2021), arXiv:2106.01345.

### 11.6 Japanese speech-generation anchor

- Keiichi Tokuda et al., “Speech Parameter Generation Algorithms for HMM-Based Speech Synthesis” (2000), ICASSP 2000, vol. 3, pp. 1315–1318.
- Related HMM-based speech-synthesis and audio-visual-synthesis publications should be collected from the authors' institutional publication lists during the eventual volume Source Intake.

### 11.7 Classical-AI context anchors

- Claude Shannon, “Programming a Computer for Playing Chess” (1950), *Philosophical Magazine*.
- Edward Feigenbaum, Bruce Buchanan, Georgia Sutherland and related Stanford Heuristic Programming Project work on DENDRAL (late 1960s / early 1970s).
- The exact periodization and evidence for `first AI boom`, `AI winter`, and `second AI boom` will be selected during Volume 1 Source Intake rather than fixed from retrospective shorthand in this planning memo.

### 11.8 2026 frontier baseline and final-volume watch anchors

These are planning anchors for the provisional final volume, checked as of 2026-08-21. They are deliberately separated from the historical canon because their eventual significance is unresolved.

#### Current Transformer-derived frontier baseline

- Kimi Team, `Kimi K3: Open Frontier Intelligence` (2026), arXiv:2607.24653. Publicly described as a 2.8T-parameter / 104B-active MoE with native vision, 1M context, Kimi Delta Attention, Attention Residuals, and Stable LatentMoE.
- DeepSeek-V4 (released 2026-04-24), official DeepSeek model card / technical report and release materials. The public report describes MoE models at 1.6T total / 49B active (Pro) and 284B total / 13B active (Flash), 1M context, a hybrid attention design combining Compressed Sparse Attention (CSA) and Heavily Compressed Attention (HCA), manifold-constrained hyper-connections (mHC), and Muon-based optimization.
- GPT-5.6, Claude 5-family, and current Grok-family systems may be used as product/system-level comparison points, but their public model/system cards do not provide enough block-level architectural detail for this memo to classify them confidently as post-Transformer successors. Do not infer a regime change from capability gains alone.

These models are useful because they show the elasticity of the Transformer era: major gains can come from heavily modified attention, MoE, residual-path changes, context scaling, post-training, reasoning effort, tools, and agentic infrastructure without public evidence of a clean architectural regime change.

#### Current “assumption-breaking” watchlist

- Yu Sun et al., `Learning to (Learn at Test Time): RNNs with Expressive Hidden States` (2024; ICML 2025), arXiv:2407.04620.
- Ali Behrouz, Peilin Zhong, Vahab Mirrokni, `Titans: Learning to Memorize at Test Time` (2025), arXiv:2501.00663.
- Ali Behrouz et al., `Nested Learning: The Illusion of Deep Learning Architectures` (2025), arXiv:2512.24695.
- Shibo Hao et al., `Training Large Language Models to Reason in a Continuous Latent Space` / Coconut (2024), arXiv:2412.06769.
- Jonas Geiping et al., `Scaling up Test-Time Compute with Latent Reasoning: A Recurrent Depth Approach` (NeurIPS 2025).
- Albert Gu, Tri Dao and collaborators, Mamba / selective state-space modeling; Tri Dao, Albert Gu, `Transformers are SSMs: Generalized Models and Efficient Algorithms Through Structured State Space Duality` (2024), arXiv:2405.21060.
- Shen Nie et al., `Large Language Diffusion Models` / LLaDA (2025), arXiv:2502.09992.
- Shen Nie et al., `Improved Large Language Diffusion Models` / iLLaDA (2026), arXiv:2606.25331.
- Artidoro Pagnoni et al., `Byte Latent Transformer: Patches Scale Better Than Tokens` (2024 / ACL 2025), arXiv:2412.09871.
- Julie Kallini et al., `Fast Byte Latent Transformer` (2026), arXiv:2605.08044.
- Mido Assran et al., `V-JEPA 2: Self-Supervised Video Models Enable Understanding, Prediction and Planning` (2025), arXiv:2506.09985.

---

## 12. Open editorial questions

These are intentionally unresolved and should be revisited during later work:

1. How should the first/second AI-boom and AI-winter periodization be defined for a Japanese readership without presenting region-dependent retrospective labels as globally exact boundaries?
2. Should Vol. 2 explicitly include ADALINE / Widrow-Hoff, or keep the volume centered on Perceptron and Amari with other adaptive rules as context?
3. How much of the pre-1986 backpropagation history is necessary in Vol. 3 to make attribution accurate without turning the volume into a history-of-calculus detour?
4. Should RBM / contrastive divergence live primarily in Vol. 4 or Vol. 7?
5. Does the CNN lineage need two volumes (`Neocognitron -> LeNet` and `AlexNet -> ResNet`), or are Vol. 5, 8, and 9 sufficient?
6. Should Word2Vec receive a dedicated volume after a separate neural-language-model volume?
7. Does Attention require more than one volume before Transformer? Current assumption: one volume is sufficient, but it should remain separate from Transformer.
8. Should VAE and GAN remain one comparative volume or become two volumes?
9. How much score-based modeling is required to explain the modern diffusion lineage responsibly?
10. Should speech/audio generation become a broader audio/music volume, or remain speech-focused and leave music to a separate Thematic Special?
11. Which multimodal foundation-model papers will still represent the decisive transitions when Vol. 21 enters production?
12. Which embodied/VLA papers will best connect multimodal foundation models to Physical AI when Vol. 23 enters production, and which apparent connections are merely retrospective analogy rather than documented lineage?
13. When should the Japanese cross-cutting volume be published so that it synthesizes enough completed foundational volumes without becoming repetitive?
14. At series completion, what is actually the dominant practical substrate: Transformer-derived neural architecture, a post-Transformer backbone, a hybrid architecture, or a system-level stack whose novelty can no longer be localized to one model block?
15. Which current “Next Transformer” candidates have actually survived independent replication, scaling, deployment economics, and cross-modal use?
16. If a post-Transformer successor is already mainstream by then, which ideas meaningfully point beyond that successor rather than merely optimizing it?

---

## 13. Maintenance rule

This file is a **living series architecture document**.

During work on Volume 2 onward:

- update the Volume 1 draft when primary-source findings change the overall story;
- update volume boundaries when a theme proves too large or too small;
- record newly discovered cross-lineage dependencies;
- distinguish direct historical lineage, parallel invention, later convergence, and retrospective analogy rather than representing all relationships with the same kind of arrow;
- distinguish neural-backbone changes from system-level changes such as tools, memory, routing, external search, multi-agent orchestration, and test-time compute;
- do not preserve numbering merely for stability if a different grouping produces a more accurate history;
- keep abandoned ideas visible in Git history rather than retaining weak volumes solely because they once appeared in this table.

The dated frontier snapshots in this memo should be preserved as historical observations. If later frontier updates are added before final-volume production, add a new dated snapshot rather than silently rewriting the old one. The purpose is to make it possible to compare what looked promising at the time with what actually survived.

When the core later volumes are substantially complete, perform a dedicated architecture pass over this document and only then begin the reader-facing manuscript of Volume 1.

The provisional final volume is different: near series completion it must perform a **new frontier-wide Source Intake from scratch** rather than treating the accumulated watchlist as its evidence base.

---

## 14. Provisional final volume — Beyond the current paradigm

### Status

`PLANNED FINAL VOLUME / content deliberately deferred`

This volume must remain the **last scheduled publication in this series**, even if additional foundational or cross-cutting volumes are inserted and all volume numbers are later changed.

Its final number should therefore not be fixed yet.

### Provisional title

**次のTransformer、その先へ — 現在の基盤パラダイムと次の転換**

Alternative working title:

**Beyond the Current Paradigm — 次の基盤モデルを探す**

### 14.1 Editorial purpose

The final volume should not freeze a 2026 prediction and later pretend that the prediction remained current. Its job is to stand at the **actual frontier when the series approaches completion**.

The first question at production time is therefore:

> **What architecture, learning paradigm, representation unit, inference process, or system design has actually become the practical substrate of frontier AI by then?**

Only after that question is answered should the issue ask what comes next.

Three outcomes are explicitly allowed:

1. **Transformer-derived substrate still dominant**  
   The issue asks what may finally displace or fundamentally reshape it.

2. **A credible post-Transformer successor already established**  
   The issue first reconstructs that transition as the current endpoint of the historical series, then asks what lies beyond the successor.

3. **No single successor; hybrid or system-level convergence dominates**  
   The issue explains why the next durable paradigm is better described as a composition of changes than as one replacement paper.

`Next Transformer` is therefore editorial shorthand for:

> **a transition that changes the assumptions under which general-purpose AI systems are built.**

It does not necessarily mean “a new attention replacement.”

### 14.2 The 2026 baseline — Transformer as substrate, not as frozen architecture

As of 2026-08-21, public frontier evidence supports a useful distinction.

Some leading open or openly documented systems remain recognizably **Transformer-derived**, while being heavily reconstructed internally.

Kimi K3 is a particularly clear example: its public report describes a 2.8T-parameter MoE with 104B activated parameters, native vision, 1M context, Kimi Delta Attention, Attention Residuals, Stable LatentMoE, large-scale agentic post-training, and substantial systems co-design.

DeepSeek-V4 likewise remains a Transformer-family scaling story rather than a clean architectural break: its public report describes MoE scaling, 1M context, hybrid compressed/sparse attention (CSA + HCA), manifold-constrained hyper-connections, and Muon-based optimization.

These are not “the 2017 Transformer with more parameters.” They demonstrate that the Transformer era has become an extensible **architectural substrate**.

A useful working picture is:

```text
Transformer-era neural substrate
  + modified / sparse / compressed attention
  + MoE routing
  + residual-path redesign
  + long-context mechanisms
  + multimodal representation
  + large-scale pretraining
  + instruction / preference / RL post-training
  + test-time reasoning
  + tools / search / code execution
  + memory / context management
  + agentic orchestration
= modern frontier AI system
```

This is the “giant castle” problem in editorial terms: enormous technical change can accumulate without a clean replacement of the underlying substrate.

For proprietary frontier systems such as current GPT, Claude, or Grok families, the public model/system cards do not expose enough block-level architecture to infer a regime change with confidence. Product-level capability, reasoning, tool use, or agentic gains must therefore **not** be treated as evidence that a post-Transformer neural architecture has already won.

This baseline prevents two opposite mistakes:

- calling every heavily modified Transformer “basically the same model”;
- calling every frontier capability jump “post-Transformer” without architectural evidence.

### 14.3 Separate the layers of possible transition

The final volume should classify candidates by **which assumption they are actually changing**.

#### Layer A — Sequence backbone / memory operator

Question:

> Must full token-to-token attention remain the principal sequence memory mechanism?

Current examples: Mamba, Mamba-2 / SSD, recurrent-state-space hybrids.

This is the closest category to a conventional “Transformer replacement.”

#### Layer B — Inference-time model state / memory

Question:

> Must the model remain effectively fixed while it is being used?

Current examples: TTT layers, Titans, Nested Learning / self-modifying or continuum-memory approaches.

A successful transition here could make inference itself partly a learning process.

#### Layer C — Computational depth and reasoning representation

Question:

> Must reasoning depth be fixed by architecture, or purchased by emitting more visible tokens?

Current examples: Coconut-style latent reasoning and recurrent-depth models.

A successful transition could decouple parameter count, nominal network depth, reasoning depth, and output length.

#### Layer D — Generation factorization

Question:

> Must language generation proceed left-to-right autoregressively?

Current examples: LLaDA / iLLaDA and other diffusion or parallel-refinement language models.

Important distinction:

> **Post-autoregressive does not automatically mean post-Transformer.**

A diffusion language model may still use a Transformer-family backbone while changing the generative factorization.

#### Layer E — Representation unit / tokenization

Question:

> Must a fixed subword tokenizer define the basic unit of computation?

Current examples: BLT and Fast BLT.

This is a representation and compute-allocation transition, not necessarily a backbone replacement.

#### Layer F — Learning objective / world representation

Question:

> Must a predictive model reconstruct observable pixels or tokens, or can it learn the latent structure needed for understanding and action?

Current example: V-JEPA 2 / latent predictive world models.

This may matter more for multimodal and Physical AI than for language-model backbone replacement.

#### Layer G — System architecture and test-time compute

Question:

> Is the next major transition located outside the neural block diagram altogether?

Current frontier systems increasingly combine models with reasoning effort, search, tools, code execution, memory, context compression, routing, verifiers, environments, and multiple agents.

A future “Transformer-level” change could therefore occur at the **architecture of the complete intelligent system**, while the neural core remains partly Transformer-derived.

This possibility must be treated seriously without conflating system architecture with neural architecture.

### 14.4 Production-time classification

At final-volume Source Intake, each candidate direction should be classified into one of four states:

- **Established substrate** — already broad enough in production or frontier research that it should be treated as history-in-the-making.
- **Scaled contender** — credible large-scale evidence, independent follow-up, and a plausible systems path, but not yet the default substrate.
- **Exploratory frontier** — intellectually important and potentially transformative, but evidence remains narrow, benchmark-specific, or implementation-dependent.
- **Absorbed innovation** — did not replace the incumbent paradigm but became an important component inside it.

The fourth category is essential. Many promising ideas may “lose” as independent architectures while still becoming part of the successor system.

### 14.5 Evaluation criteria at series completion

The final volume should prefer evidence that a candidate:

1. scales beyond a small proof of concept;
2. remains competitive under wall-clock, memory-bandwidth, communication, and serving constraints rather than FLOPs alone;
3. has been reproduced or extended by independent groups;
4. generalizes beyond one benchmark family or one modality;
5. integrates with realistic pretraining, post-training, inference, and deployment stacks;
6. creates a capability or efficiency frontier that incremental incumbent engineering does not easily recover;
7. changes how later researchers design models or systems, not merely how they tune one benchmark;
8. remains technically meaningful after the initial publication cycle;
9. survives comparison against increasingly sophisticated Transformer-derived baselines rather than an obsolete vanilla Transformer;
10. demonstrates whether it replaces, coexists with, or is absorbed into the incumbent substrate.

The issue should also consider whether apparently competing ideas have converged into a hybrid design.

A future architecture that combines attention, recurrent/state-space computation, test-time learning, adaptive depth, dynamic tokenization, and non-autoregressive generation would be a valid “next paradigm” even if no single component deserves sole credit.

### 14.6 2026-08-21 watch map — current observations, not commitments

The following is a **time-stamped editorial watchlist**, not a promise that these papers will appear in the final issue.

Its purpose is to preserve what currently looks structurally interesting so that later research can compare early expectations with what actually survived.

#### A. Test-time learning and neural memory

Current anchors:

- TTT (`Learning to (Learn at Test Time)`)
- Titans
- Nested Learning / Hope

Why this matters:

The conventional foundation-model picture separates training-time parameter updates from inference-time context use. These approaches explore hidden states or memory modules that are themselves learned or updated while processing test-time data.

Current assessment:

**Highest structural upside, but not an established successor.** Continual-learning stability, interference, systems cost, and broad production evidence remain decisive unknowns.

#### B. Latent recurrence and adaptive computation

Current anchors:

- Coconut
- recurrent-depth latent reasoning

Why this matters:

Current reasoning systems often buy more inference compute by generating longer visible chains of thought. These works explore repeated latent computation before emitting the next token.

Current assessment:

**One of the strongest candidates for a genuine inference-compute transition.** The important question is whether parameter count, architectural depth, reasoning depth, and output length can become substantially decoupled.

#### C. Diffusion and non-autoregressive language modeling

Current anchors:

- LLaDA
- iLLaDA

Why this matters:

This line challenges autoregressive factorization rather than necessarily replacing the Transformer backbone. iLLaDA materially strengthens the case by scaling masked diffusion pretraining to an 8B model and 12T training tokens.

Current assessment:

**Strong evidence that capable large language models need not be tied to left-to-right autoregression.** Whether decoding economics and deployment advantages justify a broad paradigm shift remains open.

#### D. State-space / recurrent / hybrid sequence models

Current anchors:

- Mamba
- Mamba-2 / State Space Duality

Why this matters:

The most important result may not be “Mamba beats Transformer,” but the possibility that attention and state-space approaches occupy a more unified design space than earlier rhetoric suggested.

Current assessment:

**The most mature backbone-alternative / hybridization path in the current watchlist.** A future winner may absorb attention rather than abolish it.

#### E. Byte-level and dynamically allocated representation

Current anchors:

- BLT
- Fast BLT

Why this matters:

These works challenge the assumption that a fixed subword vocabulary and fixed token granularity should define the interface between raw information and large-model computation.

Current assessment:

**An underappreciated representation/computation-unit transition** that may combine naturally with adaptive compute and non-autoregressive generation.

#### F. Latent predictive world models

Current anchor:

- V-JEPA 2

Why this matters:

JEPA-style approaches ask whether a useful predictive model must reconstruct every visible detail, or whether predicting latent structure is enough for understanding and planning.

Current assessment:

**Potentially high downstream importance for multimodal and Physical AI**, but not a general-purpose sequence-backbone successor by itself.

#### G. Test-time compute and system composition

This is a cross-cutting trend rather than one architecture.

Long-chain reasoning, sampling and verification, search, recurrent latent depth, adaptive per-token computation, test-time learning, tool use, memory, routing, and multi-agent decomposition all shift part of the capability/compute tradeoff from pretraining into inference and system execution.

The final volume should therefore ask not only:

> What replaces Transformer?

but also:

> **Where does the next generation of AI spend computation, what state is allowed to change while it spends it, and which parts of intelligence live outside the base model?**

This may prove more consequential than a single new block diagram.

### 14.7 Current synthesis

As of 2026-08-21, the strongest editorial hypothesis is **not** that one already-known paper is certain to become `Attention Is All You Need` 2.0.

The stronger observation is twofold.

First, Transformer-derived systems have shown extraordinary elasticity. They have absorbed increasingly large architectural and system-level modifications while remaining a practical frontier substrate.

Second, several assumptions stabilized during the Transformer/LLM era are now being reopened at once:

```text
fixed inference state
fixed architectural depth
verbalized reasoning
left-to-right autoregression
attention-centric sequence memory
fixed tokenization
training-time-dominated scaling
pixel/token reconstruction as the default predictive target
model-only intelligence rather than system-level composition
```

The eventual successor may therefore be compositional.

For example:

```text
dynamic byte / patch representation
  + attention / state-space hybrid memory
  + neural test-time memory
  + latent recurrent reasoning
  + adaptive inference compute
  + parallel / diffusion-style generation
  + latent world modeling
  + tool / search / environment integration
```

This would not mean Transformer “lost” in a clean historical battle. It could mean that Transformer became one component inside a more general architecture.

The final volume should not force this forecast to come true.

Its value will come from comparing this 2026 watch map with the evidence available when the series reaches its frontier.

### 14.8 Final-volume workflow

When the series approaches completion:

1. perform a new frontier-wide Source Intake from scratch rather than merely updating this watchlist;
2. identify what has already graduated into the practical mainstream or frontier substrate;
3. separate neural-backbone changes from system-level capability architecture;
4. reconstruct any already-established post-Transformer transition with the same attribution discipline used in historical volumes;
5. identify the strongest remaining contenders **beyond the then-current substrate**, even if that substrate is no longer Transformer;
6. compare them using technical, scaling, systems, adoption, and cross-modal evidence;
7. classify each major idea as established substrate, scaled contender, exploratory frontier, or absorbed innovation;
8. explicitly record which 2026 expectations succeeded, failed, merged with other ideas, were absorbed into Transformer-derived systems, or became irrelevant;
9. publish this issue last, so the series ends not with a claim that AI history is complete, but with a disciplined map of the next unresolved transition.

The final volume is therefore both a conclusion and an intentionally time-sensitive handoff from **history** to **frontier research**.
