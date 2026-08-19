# Generative AI Foundations — Thematic Special Series Plan

Status: `SCOPED / living design memo`  
Established: 2026-08-20  
Updated: 2026-08-20

## 1. Purpose

This document records the design of a long-running Thematic Special series that reconstructs the technical and intellectual lineages leading to modern generative AI and multimodal AI.

It is intentionally separate from `docs/thematic-special-backlog.md`.

- `docs/thematic-special-backlog.md` records mostly stand-alone Thematic Special candidates such as TS-001 through TS-003.
- This document describes a **multi-volume series** whose volumes depend on one another and whose overall architecture is expected to evolve while research and drafting proceed.

The series is not intended to be a comprehensive history of artificial intelligence, machine learning, computer vision, natural language processing, reinforcement learning, or robotics. Its scope is narrower:

> **Re-read the papers, methods, and research transitions that materially contributed to the conceptual or technical foundations of today's generative AI and multimodal AI, and explain what was inherited, what was replaced, and what was later recombined.**

The series should remain compatible with the Evidence-first philosophy of the Special pipeline. Historical significance is not a substitute for source verification.

---

## 2. Core editorial thesis

Modern generative AI did not emerge from a single linear sequence such as:

```text
Perceptron -> Backpropagation -> CNN -> Attention -> Transformer -> LLM
```

That story is too simple. Several partly independent traditions developed in parallel and later converged:

```text
Learning / optimization
  Perceptron -> adaptive and stochastic learning -> backpropagation -> scalable optimization

Vision
  Cognitron / Neocognitron -> CNN -> ImageNet-era deep vision -> ViT

Language / sequence
  neural language models -> distributed representations -> RNN/LSTM
  -> Seq2Seq -> Attention -> Transformer -> generative pretraining -> scaling

Generative modeling
  stochastic / energy-based models -> VAE / GAN -> diffusion -> latent and multimodal generation

Search / decision / action
  minimax / heuristic search -> reinforcement learning -> deep RL -> neural-guided search
  -> world models / sequence decision models -> embodied and physical AI

Multimodal integration
  learned visual representation + learned language representation
  -> contrastive alignment -> multimodal foundation models -> perception/generation/action integration
```

The series should therefore be understood as a **directed graph of research lineages**, not as a single chronological ladder.

Chronology remains important inside each lineage and when explaining cross-lineage influence, but chronology alone does not determine volume order.

---

## 3. Scope and inclusion rule

### 3.1 Primary scope

A topic belongs in the main series when its connection to today's generative AI or multimodal AI can be explained without inventing a retrospective relationship that the evidence does not support.

As a planning heuristic, prefer topics for which a meaningful path to current systems can be drawn in roughly two or three major conceptual transitions.

Examples:

```text
Word2Vec
  -> distributed representations / embeddings
  -> Transformer token representations
  -> LLMs

Neocognitron
  -> convolutional hierarchical vision
  -> deep visual representation
  -> multimodal vision systems

Diffusion probabilistic models
  -> denoising diffusion
  -> latent / conditioned diffusion
  -> modern image and video generation

Deep RL + neural-guided search
  -> learned planning / search
  -> agentic inference and action systems
```

The two-or-three-transition rule is **not a mechanical gate**. Historically important bridge technologies may be included when the connection requires more steps but remains technically substantive.

### 3.2 Three planning tiers

Candidate material should be classified informally as:

- **Core** — the technical DNA remains clearly visible in current generative or multimodal systems.
- **Bridge** — not itself a generative-AI technique, but it handed over a major idea, architecture, learning paradigm, or problem formulation.
- **Context** — important for explaining why later research changed direction, but not a subject that needs its own volume by default.

Examples of likely Context material include parts of classical symbolic AI, expert systems, and early search research. They matter to the overall story, but the series must not expand into a general AI-history encyclopedia.

### 3.3 Explicit non-goal

Do not include a field simply because it is important to AI history.

For example, computer vision, game AI, reinforcement learning, robotics, knowledge representation, or expert systems should only receive detailed treatment where they clarify a lineage that reaches modern generative, multimodal, agentic, world-model, or physical-AI systems.

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

Examples of claims that require care:

- Backpropagation has a pre-1986 history; Rumelhart, Hinton, and Williams (1986) is a major dissemination and demonstration point, not a safe universal answer to “who invented backpropagation?”.
- Attention predates the Transformer; Bahdanau-style neural attention and the Transformer are distinct transitions.
- Natural gradient is historically and mathematically important, but it did not become the default optimizer for modern Transformer training.
- Neocognitron is an important ancestor in hierarchical visual modeling, but modern trainable CNNs also depend on later gradient-based formulations and engineering developments.

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

### 6.2 Role of the draft

The Volume 1 draft below is therefore **not publication prose and not the first manuscript**. It is a living synopsis of the story the series currently expects to tell.

---

# 7. Volume 1 draft — series overview

## Provisional title

**生成AIの源流 — 探索・学習・表現・生成が合流するまで**

Alternative working title:

**生成AIはどこから来たのか — 現代AIを形作った複数の研究系譜**

## Draft purpose

Today's generative AI is often narrated as a recent sequence beginning with the Transformer and accelerating through large language models. That account is useful for current product history but insufficient as a technical history.

The systems now called generative AI inherit ideas from several older research programs: machine learning from examples, optimization under uncertainty, distributed representation, hierarchical visual processing, recurrent sequence models, probabilistic generative modeling, adversarial learning, attention, large-scale self-supervised pretraining, reinforcement learning, and search.

Some of those traditions competed with one another. Some appeared to fail and later returned in new forms. Some did not directly survive but changed the questions the field asked.

Volume 1 should give the reader a map of those lineages before the later volumes examine them in detail.

## Draft section 1 — Before “deep learning”: competing ideas of intelligence

The opening should avoid pretending that early AI was simply an immature form of today's neural AI.

Early AI research explored several different answers to the question “what makes a machine intelligent?”

One answer emphasized **search**: enumerate possible actions or states, evaluate them, and choose a promising path. Game-playing research makes this idea especially visible. Minimax and heuristic search should appear here as examples of intelligence implemented through explicit exploration of alternatives rather than learned representation.

A second answer emphasized **symbolic reasoning**: represent facts and manipulate symbols according to rules.

A third answer emphasized **knowledge engineering**. Expert systems such as DENDRAL are useful not because modern generative AI directly descends from their implementation, but because they embody a contrasting design philosophy: much of the intelligence is supplied as explicit domain knowledge and heuristics.

A fourth answer emphasized **learning from examples**. This is the branch that eventually became dominant in deep learning, but Volume 1 should present it as one branch among several rather than as an inevitable winner known in advance.

The reader-facing question for this section is:

> How much intelligence should the programmer explicitly specify, and how much should the machine acquire from data or interaction?

That question remains relevant even in modern systems through retrieval, tools, search, planning, external memory, and reinforcement learning.

## Draft section 2 — The neural branch: from units to adaptive learning

The neural lineage should begin with brief context on mathematical neuron models and then move quickly to the Perceptron and adaptive pattern classification.

Rosenblatt's Perceptron is important not merely as an old classifier, but as a concrete expression of the idea that behavior can be changed by an update rule driven by examples.

Shun-ichi Amari's 1967 work on adaptive pattern classifiers belongs here as a major Japanese contribution to the theory of learning under general and nonseparable pattern distributions. The later detailed volume must distinguish carefully between Amari's probabilistic/stochastic descent ideas, later stochastic-gradient terminology, and the many independent lines that contributed to modern stochastic optimization.

The limitation story around perceptrons must also be handled carefully. `Perceptrons` by Minsky and Papert is historically important, but the series should avoid the simplistic legend that a single book “killed neural networks.” The more useful question is what classes of systems were being analyzed, what limitations were actually established, and why multilayer learning remained technically difficult.

## Draft section 3 — Hidden representations become learnable

The next transition is not just “backpropagation was invented.”

The important shift for this series is that multilayer networks became a practical framework in which internal hidden units could learn task-relevant representations through error-driven optimization.

The 1986 Rumelhart-Hinton-Williams paper is a major landmark because it clearly demonstrates learning useful internal representations through back-propagated error. Its historical treatment should include earlier precursors rather than attributing the entire mathematical idea to 1986.

In parallel, Hopfield networks and Boltzmann machines developed another neural tradition: collective dynamics, energy functions, stochastic units, and probabilistic generative interpretation. This lineage later connects to restricted Boltzmann machines, deep belief networks, energy-based modeling, and the broader history of generative learning.

## Draft section 4 — Vision and time create specialized architectures

General multilayer networks were not enough. Different data structures created different architectural pressures.

For vision, Fukushima's Cognitron and Neocognitron provide a major bridge toward hierarchical local feature processing and tolerance to positional variation. Later gradient-trained convolutional networks and LeNet turned related architectural ideas into trainable systems, and the ImageNet era showed what happens when architecture, data, computation, and optimization scale together.

For sequences, recurrent networks represented time through internal state. LSTM addressed the difficulty of learning long-range dependencies and became a central architecture for sequence modeling before the Transformer.

The point of this section is not to tell complete CNN or RNN history. It is to show that **representation was becoming structured around the modality and the dependency pattern of the data**.

## Draft section 5 — Deep learning returns, then scales

The 2000s revival should not begin at AlexNet alone.

Layer-wise unsupervised pretraining and deep belief networks helped re-establish the feasibility and value of learning multiple levels of representation. They also belong to the generative-model lineage, not only to an optimization story.

AlexNet then marks a different transition: a large convolutional model, a large labeled dataset, GPU computation, rectifying nonlinearities, and practical regularization combined to produce a decisive ImageNet result.

Subsequent techniques such as improved initialization and activations, dropout, adaptive optimization, batch/layer normalization, and residual connections helped turn deep networks from difficult research artifacts into a reusable engineering substrate.

Volume 1 should present “deep learning” not as one algorithm, but as the point at which representation learning, optimization, data scale, and compute scale became mutually reinforcing.

## Draft section 6 — Language becomes representation learning at scale

Language provides another route into modern generative AI.

Neural probabilistic language models made learned distributed word representations part of the language-modeling problem itself. Word2Vec then made continuous word-vector learning efficient and widely reusable at very large corpus scale.

RNN/LSTM encoder-decoder systems generalized neural models from fixed labels toward sequence generation. Seq2Seq made end-to-end sequence transformation a central neural problem, but encoding an entire source sequence into a fixed-length vector exposed a bottleneck.

Bahdanau-style attention changed that problem formulation by allowing the decoder to dynamically use relevant parts of the source representation. Transformer then made a second and distinct move: attention became the principal computational architecture rather than an auxiliary mechanism attached to recurrence.

This distinction is central to the series:

> **Attention is not synonymous with Transformer.**

The later Transformer volume should show why removing recurrence mattered for representation, dependency length, and parallel training.

## Draft section 7 — Generative modeling was developing on another branch

Modern generative AI should not be narrated as an LLM-only history.

Energy-based and latent-variable models had long addressed the problem of learning distributions. In the 2010s, VAE and GAN provided two influential deep-generative frameworks with very different training principles.

Diffusion models form another lineage. The 2015 nonequilibrium-thermodynamics formulation established an iterative corruption and learned reverse process; DDPM later demonstrated high-quality image synthesis; latent diffusion made high-resolution conditioned generation substantially more practical and connected diffusion generation directly to text conditioning through cross-attention.

The series should therefore describe modern media generation as the convergence of multiple traditions rather than as a direct derivative of language models.

## Draft section 8 — Foundation models and multimodal convergence

Transformer-based generative pretraining made it possible to reuse one learned model across many language tasks. GPT-style generative pretraining, BERT-style bidirectional pretraining, and related work should be treated as distinct answers to the same larger question: how much task-specific structure can be replaced by large-scale pretraining?

Scaling-law work and GPT-3 then made scale itself an explicit research variable. Few-shot and in-context behavior changed how users could specify tasks: some task adaptation moved from parameter updates into the prompt/context supplied at inference time.

In vision, ViT showed that image patches could be processed as Transformer sequences at scale. CLIP showed that image and natural-language supervision could be aligned through large-scale contrastive training. These developments are major bridges from separate vision and language pipelines toward modern multimodal systems.

Instruction tuning and human-feedback methods form another required transition. A next-token model is not automatically a useful assistant; post-training changes the relationship between base-model capability and user-directed behavior.

## Draft section 9 — Search returns; generation reaches action

The final part of the overview should reconnect modern AI to the classical AI ideas introduced at the beginning.

Deep reinforcement learning demonstrated that neural networks could learn representations and actions together from high-dimensional inputs. AlphaGo then combined learned policy/value networks with tree search: learning did not simply replace search; it made search dramatically more effective.

World-model research reframed generative modeling as learning an environment in which future states can be imagined. Decision Transformer showed that reinforcement-learning problems could themselves be recast as conditional sequence modeling.

This creates a credible bridge from generative modeling to agents and physical AI:

```text
predict / generate text
  -> predict / generate images and audio
  -> predict future world states
  -> generate actions conditioned on goals and observations
```

Physical AI should only be followed as far as this connection remains technically meaningful. The series is not intended to become a complete robotics history.

## Draft conclusion

The first volume should end by replacing the idea of a single “AI family tree” with a map of intersecting research rivers.

Modern generative and multimodal AI combines ideas that once belonged to separate communities:

- neural learning and stochastic optimization;
- representation learning;
- hierarchical perception;
- sequential prediction;
- probabilistic and adversarial generation;
- attention and Transformer architectures;
- large-scale pretraining and scaling;
- human-feedback post-training;
- search, reinforcement learning, and world modeling.

The later volumes then revisit the turning points one by one, using original sources to distinguish what the work actually established from what later history made possible.

---

# 8. Provisional volume architecture

This allocation is intentionally provisional. During research and drafting, volumes may be merged, split, inserted, removed, or renumbered.

The table describes **current editorial units**, not final publication commitments.

| Provisional volume | Working theme | Main material currently expected | Why it belongs in this series |
|---|---|---|---|
| **Vol. 1** | **生成AIの源流 — 総説** | Classical AI context; neural learning; representation; vision; sequence; generative modeling; Transformer; scaling; multimodal; search/action | Reader map for the complete series. Final manuscript is written after the major later volumes. |
| **Vol. 2** | **機械が学ぶという発想 — Perceptronと適応学習** | mathematical-neuron context; Rosenblatt; perceptron learning; Widrow-Hoff/ADALINE as needed; Amari 1967; separability and adaptation | Establishes learning-from-data and stochastic/adaptive update ideas before deep networks. |
| **Vol. 3** | **多層ネットワークを学習する — Backpropagationと内部表現** | multilayer-network problem; early gradient/backprop precursors; Rumelhart-Hinton-Williams; hidden representations | Connects error-driven optimization to learned internal representation. Avoid single-inventor mythology. |
| **Vol. 4** | **記憶・エネルギー・確率生成 — HopfieldからBoltzmannへ** | Hopfield networks; Boltzmann machines; stochastic units; energy functions; RBM / contrastive divergence as bridge | Important branch toward probabilistic neural generation, deep belief nets, and later energy-based thinking. |
| **Vol. 5** | **視覚を階層化する — NeocognitronからCNNへ** | Cognitron/Neocognitron; local receptive processing; LeCun-era trainable CNN / LeNet | Core ancestry of learned visual representation and later multimodal perception. |
| **Vol. 6** | **時間を記憶する — RNN、BPTT、LSTM** | recurrent representation; temporal credit assignment; vanishing/long-lag problem; LSTM | Necessary prehistory for Seq2Seq, Attention, and the meaning of replacing recurrence. |
| **Vol. 7** | **Deep Learning再興 — Unsupervised PretrainingとDeep Belief Nets** | RBM/DBN; greedy layer-wise training; autoencoder-related context; representation learning | Separates the 2006-era deep-learning revival from the later ImageNet/GPU revolution. |
| **Vol. 8** | **ImageNet Shock — データ・GPU・深いCNN** | ImageNet context; AlexNet; ReLU; GPU training; dropout/regularization as used in the transition | Shows how data scale, compute, architecture, and training practice jointly changed the field. |
| **Vol. 9** | **深いネットを実用基盤にする — Optimization、Normalization、Residual** | improved activations/initialization as needed; Adam; BatchNorm; LayerNorm; ResNet; residual pathways | These techniques form much of the engineering substrate later inherited by Transformer-scale models. |
| **Vol. 10** | **単語をベクトルにする — Neural Language ModelとWord2Vec** | Bengio et al. 2003; distributed representation; CBOW/Skip-gram; negative sampling; GloVe/contextual embeddings as needed | Makes the shift from symbolic word IDs toward learned continuous language representation explicit. |
| **Vol. 11** | **系列から系列へ — Encoder–DecoderとSeq2Seq** | neural machine translation context; LSTM encoder-decoder; Sutskever et al.; fixed-vector representation | Establishes the problem setting that directly motivates neural attention. |
| **Vol. 12** | **Attention — 必要な場所を見るという転換** | Bahdanau et al.; alignment; attention before Transformer; Luong-style variants if useful; self-attention precursors | Attention is treated as its own conceptual transition rather than retrospectively collapsed into Transformer. |
| **Vol. 13** | **Transformer — Attentionを中心アーキテクチャにする** | `Attention Is All You Need`; self-attention; multi-head attention; positional information; residual/normalization; training parallelism | Principal architectural bridge into modern LLMs and many multimodal models. |
| **Vol. 14** | **事前学習が基盤になる — ELMo、GPT、BERT、T5周辺** | contextual representations; generative pretraining; bidirectional pretraining; transfer/fine-tuning; text-to-text unification as needed | Explains the shift from task-specific models toward reusable pretrained foundation models. |
| **Vol. 15** | **ScalingとIn-Context Learning — 大きくすると何が変わるのか** | GPT-2; empirical scaling laws; GPT-3; compute/data/model tradeoffs; Chinchilla-style revision if required | Scale becomes an explicit design variable and some adaptation moves into inference-time context. |
| **Vol. 16** | **Deep Generative Models — VAEとGANが示した二つの答え** | AEVB/VAE; adversarial training/GAN; latent spaces; conditional variants as needed | Establishes major non-LLM deep-generative paradigms and their different answers to distribution learning. |
| **Vol. 17** | **Diffusion — 壊して戻す生成モデル** | Sohl-Dickstein et al.; score/denoising connections as needed; DDPM; guidance; Latent Diffusion | Direct lineage into modern image generation and an important branch of video/multimodal generation. |
| **Vol. 18** | **画像をTokenにし、言語と結ぶ — ViTとCLIP** | Vision Transformer; contrastive image-text pretraining; CLIP; related alignment work as needed | Major convergence point between the mature vision and language representation lineages. |
| **Vol. 19** | **指示に従うモデル — Instruction TuningとHuman Feedback** | supervised instruction tuning; preference/reward modeling; RLHF; InstructGPT and important precursors | Distinguishes base-model capability from assistant-like behavior and post-training. |
| **Vol. 20** | **音声を生成する — 統計的音声合成からNeural Speechへ** | HMM-based speech synthesis; Tokuda et al.; WaveNet; Tacotron-family developments; neural codec / speech-generation bridges as needed | Prevents “generative AI” from becoming text/image-only history and creates a Japanese-research bridge into multimodality. |
| **Vol. 21** | **Multimodal Foundation Models — 理解と生成の合流** | vision-language models; cross-attention/projector/Q-former style bridges as appropriate; image/audio/video integration; unified modeling | Follows the convergence of previously separate modality-specific representation and generation systems. Exact papers should be selected near production time because this area changes quickly. |
| **Vol. 22** | **探索と学習の再会 — Deep RL、DQN、AlphaGo** | classical search context; Q-learning/RL context; DQN; AlphaGo/AlphaZero; neural-guided search | Bridge volume explaining why learning did not eliminate search and how this lineage reconnects to modern reasoning/agent systems. |
| **Vol. 23** | **World ModelからPhysical AIへ — 予測から行動へ** | World Models; model-based learned environments; Decision Transformer; VLA / embodied foundation-model anchors as appropriate | Extends generative modeling from text/media into future-state and action generation without turning the series into a general robotics history. |

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
- Vol. 20 may expand beyond speech into audio/music only if doing so remains technically coherent; otherwise music/audio generation can be handled in a later multimodal or media-generation Special.
- Vol. 21 and Vol. 23 must be re-scoped near their production dates because their frontier reference points may change materially.

---

# 9. Cross-cutting Japanese research volume

## Status

`SCOPED concept / volume number TBD`

## Provisional title

**日本から生成AIへ — 学習・視覚・音声の源流**

## Editorial purpose

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

The Japanese cross-cutting volume may be published after the relevant foundational volumes so that it can synthesize rather than prematurely duplicate them.

---

# 10. Game AI and Physical AI boundary

Game AI and Physical AI are allowed only as **bridge themes** into current generative/multimodal systems.

### Game AI

Do not write a general history of chess, Go, search algorithms, or reinforcement learning.

Use the lineage primarily to explain:

```text
classical explicit search
  -> learned value / policy representations
  -> neural-guided search
  -> modern inference-time search / planning / agents
```

AlphaGo is particularly useful because policy/value networks and tree search are explicitly combined rather than presented as mutually exclusive paradigms.

### Physical AI

Do not write a general robotics history.

Follow the branch only where generative and sequence-model ideas remain central:

```text
learn representations of observations
  -> learn/predict environment dynamics
  -> model future trajectories
  -> condition action generation on observations and goals
  -> multimodal / vision-language-action systems
```

World Models and Decision Transformer are currently useful bridge points. The exact embodied/VLA papers used in the final volume should be selected during later Source Intake because this area is still changing rapidly.

---

# 11. Planning-level source anchors checked on 2026-08-20

This is **not** a completed Evidence inventory. These references were checked only to keep the present series architecture historically and technically plausible. Each production volume must perform its own complete Source Intake and Evidence work.

## Classical / neural foundations

- Frank Rosenblatt, “The Perceptron: A Probabilistic Model for Information Storage and Organization in the Brain” (1958), *Psychological Review* 65(6), 386–408. DOI: `10.1037/h0042519`.
- Shun-ichi Amari, “A Theory of Adaptive Pattern Classifiers” (1967), *IEEE Transactions on Electronic Computers* EC-16(3), 299–307. DOI: `10.1109/PGEC.1967.264666`.
- Marvin Minsky and Seymour Papert, *Perceptrons* (1969), MIT Press.
- David H. Ackley, Geoffrey E. Hinton, Terrence J. Sejnowski, “A Learning Algorithm for Boltzmann Machines” (1985), *Cognitive Science* 9, 147–169.
- David E. Rumelhart, Geoffrey E. Hinton, Ronald J. Williams, “Learning representations by back-propagating errors” (1986), *Nature* 323, 533–536. DOI: `10.1038/323533a0`.

## Vision and deep learning

- Kunihiko Fukushima, “Neocognitron: A self-organizing neural network model for a mechanism of pattern recognition unaffected by shift in position” (1980), *Biological Cybernetics* 36, 193–202. DOI: `10.1007/BF00344251`. A Japanese precursor paper appeared in IEICE in 1979.
- Yann LeCun et al., “Gradient-Based Learning Applied to Document Recognition” (1998), *Proceedings of the IEEE* 86(11), 2278–2324.
- Geoffrey E. Hinton, Simon Osindero, Yee-Whye Teh, “A Fast Learning Algorithm for Deep Belief Nets” (2006), *Neural Computation* 18, 1527–1554.
- Alex Krizhevsky, Ilya Sutskever, Geoffrey E. Hinton, “ImageNet Classification with Deep Convolutional Neural Networks” (2012), NeurIPS 25.
- Kaiming He et al., “Deep Residual Learning for Image Recognition” (2015/2016), CVPR 2016 / arXiv:1512.03385.

## Language / sequence / Transformer

- Sepp Hochreiter, Jürgen Schmidhuber, “Long Short-Term Memory” (1997), *Neural Computation* 9(8), 1735–1780.
- Yoshua Bengio et al., “A Neural Probabilistic Language Model” (2003), *JMLR* 3, 1137–1155.
- Tomas Mikolov et al., “Efficient Estimation of Word Representations in Vector Space” (2013), arXiv:1301.3781.
- Ilya Sutskever, Oriol Vinyals, Quoc V. Le, “Sequence to Sequence Learning with Neural Networks” (2014), arXiv:1409.3215 / NeurIPS 2014.
- Dzmitry Bahdanau, Kyunghyun Cho, Yoshua Bengio, “Neural Machine Translation by Jointly Learning to Align and Translate” (2014), arXiv:1409.0473 / ICLR 2015.
- Ashish Vaswani et al., “Attention Is All You Need” (2017), NeurIPS 30.
- OpenAI, “Improving Language Understanding by Generative Pre-Training” / accompanying 2018 research release.
- Jacob Devlin et al., “BERT: Pre-training of Deep Bidirectional Transformers for Language Understanding” (2018/2019), NAACL 2019.
- Jared Kaplan et al., “Scaling Laws for Neural Language Models” (2020), arXiv:2001.08361.
- Tom B. Brown et al., “Language Models are Few-Shot Learners” (2020), arXiv:2005.14165.

## Deep generative modeling

- Diederik P. Kingma, Max Welling, “Auto-Encoding Variational Bayes” (2013), arXiv:1312.6114 / ICLR 2014.
- Ian Goodfellow et al., “Generative Adversarial Nets” (2014), NeurIPS 27.
- Jascha Sohl-Dickstein et al., “Deep Unsupervised Learning using Nonequilibrium Thermodynamics” (2015), arXiv:1503.03585 / ICML 2015.
- Jonathan Ho, Ajay Jain, Pieter Abbeel, “Denoising Diffusion Probabilistic Models” (2020), arXiv:2006.11239 / NeurIPS 2020.
- Robin Rombach et al., “High-Resolution Image Synthesis with Latent Diffusion Models” (2021/2022), arXiv:2112.10752 / CVPR 2022.

## Multimodal / alignment / action

- Alexey Dosovitskiy et al., “An Image is Worth 16x16 Words: Transformers for Image Recognition at Scale” (2020/2021), arXiv:2010.11929 / ICLR 2021.
- Alec Radford et al., “Learning Transferable Visual Models From Natural Language Supervision” (2021), arXiv:2103.00020.
- Nisan Stiennon et al., “Learning to summarize from human feedback” (2020), arXiv:2009.01325.
- Long Ouyang et al., “Training language models to follow instructions with human feedback” (2022), arXiv:2203.02155.
- Volodymyr Mnih et al., “Human-level control through deep reinforcement learning” (2015), *Nature* 518, 529–533.
- David Silver et al., “Mastering the game of Go with deep neural networks and tree search” (2016), *Nature* 529, 484–489.
- David Ha, Jürgen Schmidhuber, “World Models” (2018), arXiv:1803.10122.
- Lili Chen et al., “Decision Transformer: Reinforcement Learning via Sequence Modeling” (2021), arXiv:2106.01345.

## Japanese speech-generation anchor

- Keiichi Tokuda et al., “Speech Parameter Generation Algorithms for HMM-Based Speech Synthesis” (2000), ICASSP 2000, vol. 3, pp. 1315–1318.
- Related HMM-based speech-synthesis and audio-visual-synthesis publications should be collected from the authors' institutional publication lists during the eventual volume Source Intake.

## Classical-AI context anchors

- Claude Shannon, “Programming a Computer for Playing Chess” (1950), *Philosophical Magazine*.
- Edward Feigenbaum, Bruce Buchanan, Georgia Sutherland and related Stanford Heuristic Programming Project work on DENDRAL (late 1960s).

---

# 12. Open editorial questions

These are intentionally unresolved and should be revisited during later work:

1. Should Vol. 2 explicitly include ADALINE / Widrow-Hoff, or keep the volume centered on Perceptron and Amari with other adaptive rules as context?
2. How much of the pre-1986 backpropagation history is necessary in Vol. 3 to make attribution accurate without turning the volume into a history-of-calculus detour?
3. Should RBM / contrastive divergence live primarily in Vol. 4 or Vol. 7?
4. Does the CNN lineage need two volumes (`Neocognitron -> LeNet` and `AlexNet -> ResNet`), or are Vol. 5, 8, and 9 sufficient?
5. Should Word2Vec receive a dedicated volume after a separate neural-language-model volume?
6. Does Attention require more than one volume before Transformer? Current assumption: one volume is sufficient, but it should remain separate from Transformer.
7. Should VAE and GAN remain one comparative volume or become two volumes?
8. How much score-based modeling is required to explain the modern diffusion lineage responsibly?
9. Should speech/audio generation become a broader audio/music volume, or remain speech-focused and leave music to a separate Thematic Special?
10. Which multimodal foundation-model papers will still represent the decisive transitions when Vol. 21 enters production?
11. Which embodied/VLA papers will best connect multimodal foundation models to Physical AI when Vol. 23 enters production?
12. When should the Japanese cross-cutting volume be published so that it synthesizes enough completed foundational volumes without becoming repetitive?

---

# 13. Maintenance rule

This file is a **living series architecture document**.

During work on Volume 2 onward:

- update the Volume 1 draft when primary-source findings change the overall story;
- update volume boundaries when a theme proves too large or too small;
- record newly discovered cross-lineage dependencies;
- do not preserve numbering merely for stability if a different grouping produces a more accurate history;
- keep abandoned ideas visible in Git history rather than retaining weak volumes solely because they once appeared in this table.

When the core later volumes are substantially complete, perform a dedicated architecture pass over this document and only then begin the reader-facing manuscript of Volume 1.
