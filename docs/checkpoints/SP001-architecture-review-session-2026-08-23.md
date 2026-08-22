# SP001 Architecture Review session worklog — 2026-08-23 continuation

Status: `ACTIVE`  
Continues: `docs/checkpoints/SP001-architecture-review-session-2026-08-22.md`

Target: `SP001`  
Requested stop: `ARCHITECTURE_REVIEW`  
Canonical work branch: `special/SP001-v2-work`

## Purpose

This continuation records actions actually performed after the session crossed midnight JST. It is operational provenance only; canonical Production Profile/State and Stage Checkpoints remain authoritative for lifecycle state.

## Actions completed in this continuation

### 1. Completed broad direct primary-source intake map

Created:

`sources/SP001/raw/direct-primary-intake-2026-08-23.md`

Commit:

`4e33c972320d61207e366ae1502bf91d045415d5`

The note records exact source locators, source classes, obligation mapping, concise operator observations, residual gaps, and a saturation judgment. It is explicitly marked `RAW_OPERATOR_OBSERVATION`, not publication-grade Evidence.

Coverage includes:

- GLM / GLM-130B / ChatGLM historical lineage;
- Qwen 1 → Qwen2 → Qwen2.5 → Qwen3 → Qwen3.5/3.6;
- DeepSeek LLM → V2 → V3 → R1 → V4/V4-Flash;
- GLM-4 → GLM-4.5 → GLM-5/5.2;
- Kimi k1.5 → K2 → Kimi Linear → K3;
- Yi, Baichuan and MiniMax as possible bridge/parallel branches;
- local inference, serving, long-context, reasoning/coding/agentic capability;
- Open Weight vs Open Source and concrete license-boundary differences.

### 2. Closed residual primary-source gaps

Created:

`sources/SP001/raw/direct-primary-gapfill-2026-08-23.md`

Commit:

`fe973265715e31f6e216d78179a677116d9da77c`

Concrete closures:

#### GLM-4

Located the version-specific primary paper:

`ChatGLM: A Family of Large Language Models from GLM-130B to GLM-4 All Tools`  
https://arxiv.org/abs/2406.12793

This replaces the earlier weaker reliance on retrospective repository history for GLM-4 lineage and All Tools claims.

#### Kimi K3 license

Located exact primary license text:

https://huggingface.co/moonshotai/Kimi-K3/blob/main/LICENSE

The license is neither plain MIT nor Apache-2.0. It contains, among other conditions, separate-agreement requirements for certain Model-as-a-Service commercial use above a revenue threshold and prominent `Kimi K3` display requirements for very large commercial products/services. Later Evidence must preserve the exact subject and conditions rather than compressing it into a generic `permissive license` label.

#### MiniMax

Verified that MiniMax remains materially relevant to the 2026 general/frontier agentic model competition:

- MiniMax M2.5 — 2026-02-12
- MiniMax M2.7 — 2026-03-18

M2.7 is distributed as an open-weight model with common local/serving integrations and is positioned around complex agent harnesses, Agent Teams, skills, dynamic tool search and model-assisted self-evolution workflows.

Architecture implication: MiniMax should be visible as a material **parallel frontier branch**, but TS-001 still names DeepSeek/Qwen/GLM/Kimi as the four central families. Do not silently turn MiniMax into a fifth co-equal family chapter; prefer a compact parallel/competing-strategy section or comparative callout unless later materiality review changes that conclusion.

#### Yi

Verified Yi-1.5 / Yi-Coder as a meaningful 2024 open-weight, local-deployment and coding branch, but found no comparable 2025–2026 general Yi checkpoint in the official model catalog. Current disposition is historical/bridge rather than 2026 primary frontier.

#### Baichuan

Verified that Baichuan remains active in 2025–2026, but the current M2/M3 line is medical-specialized and uses Qwen-family bases. This is more useful as a specialization/derivative ecosystem case than as a continuous independent general-frontier family through 2026.

### 3. Updated Source Intake saturation judgment

Direct/conventional research is now considered structurally saturated enough for Discovery closure:

- all seven SP001 Profile dimensions have credible source lanes;
- all four central families have early-to-current lineages;
- 2026 frontier endpoints have been checked;
- material bridge/parallel families have been tested instead of assumed away;
- Open Weight/license differences have concrete primary-source anchors;
- remaining research should be driven by Screening/Evidence gaps rather than undirected source-count expansion.

Discovery Acceptance is still not legal yet because the required Grok/X run remains an outstanding Source Intake dependency.

## Current lifecycle state

Canonical Production State remains:

`ISSUE_INITIALIZED`

with:

`next_action = stage:discovery`

No Human Gate or Exception Gate has been reached.

## Immediate next action

Re-check the prepared Google Drive run folder:

`Grok_X_SourseIntake/Thematic_Special/SP001/open-weight-ecosystem-pass-01/`

If the Grok result is present, import its exact bytes to repository Raw, disposition it, close the X manifest, build accepted Discovery, and continue automatically through Screening/Evidence/Selection/Architecture.

If the result is absent, the only remaining interruption is the permitted manual Grok transport boundary. No editorial approval is required.
