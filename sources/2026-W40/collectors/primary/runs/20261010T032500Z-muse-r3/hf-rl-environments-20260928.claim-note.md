# CLAIM NOTE (derived) — HF RL Environments Hub (Sep 28)

- artifact_class: CLAIM_LEVEL_DERIVED_NOTE
- companion_excerpts: [`hf-rl-environments-20260928.source-excerpt.md`]
- read_status: READ (full page via webfetch 2026-10-10T03:25:59Z: all sections incl. 4 framework run examples, tag instructions, already-on-Hub lists, what-comes-next); bounded excerpt archived separately
- event_date_basis: DAY ONLY "Published September 28, 2026"; NO clock time/timezone evidenced -> Discovery published_at NULL + DATE_DAY_ONLY__DATETIME_NOT_PROVEN

## Consumed claims (claim-level)

1. EVENT: Hugging Face launched RL Environments Hub surface Sep 28, 2026 (day): dedicated `rl-environment` dataset filter + 4 framework compatibility tags (`harbor`, `verifiers`, `openenv`, `nemo-gym`) with per-framework generated `Use this dataset` snippets; dataset-repo-backed discoverability/versioning/discussion. (PRIMARY_FACT: feature launch, day only)
2. ARCHITECTURE (publisher-stated): taskset dataset separable from runtime + reward execution; no new repo type/registry/sign-up; framework loads files, runs locally or supported cloud (Jobs/Sandboxes); tag declares compatibility, does NOT convert formats or start jobs/sandboxes. Multi-tag allowed but each framework must support files. (PRIMARY_FACT as vendor architecture description)
3. EXAMPLES (publisher-provided, version-pinned): harbor oracle `harbor==0.21.0` on terminal-bench-2.1@2.1.0 `*regex-log`; verifiers v1 harbor integration (Docker/bash harness, registry.json conventions); openenv[harbor]==0.7.0 rollout (Docker, Gradio tunnel, reward None semantics); NeMo Gym structured-outputs (schema adherence, not factuality). (PUBLISHER_CLAIM as documented commands)
4. SEEDED CONTENT: already-on-Hub PRs — Harbor (BeyondSWE, Terminal-Lego-15k, harbor-mix 100, NatureBench 90); Verifiers (Reverse-Text-RL, Multi-SWE-RL-Verified 2,232/4,703, R2E-Gym-Subset, Scale-SWE-Verified 17,202/20,181); NeMo Gym (Workplace Assistant 5DB/26tools/690tasks, Structured Outputs, CFBench, SysBench). Counts are publisher-stated snapshots. (PUBLISHER_CLAIM)
5. SCOPE BOUNDARIES (publisher-stated, must preserve): this W40 launch is a new cross-framework discovery/integration feature, NOT the earlier 2025 creation of OpenEnv and NOT a new model training result; per-config snippets + structural detection are forward-looking (not shipped); reward-None/error inspection caveat; bare Hub repo ID cannot replace Harbor registry repo+dataset pair.
6. RELEVANCE (discovery lead, NOT selection): Hub distribution/interoperability for agent RL eval/training; lanes C/I/K/L (+ G infra-adjacent with distinction); distinct from Holo4 (agent models), Olmo-core 3 (MoE training stack), AutoSynthData (synthetic curriculum).

## Boundaries / unresolved

- No exact UTC instant; never invent T12:00:00Z.
- Commands/versions are Sep 28 snapshots; repos/frameworks evolve — Evidence must pin versions if cited.
- Materiality for Selection NOT decided here.
