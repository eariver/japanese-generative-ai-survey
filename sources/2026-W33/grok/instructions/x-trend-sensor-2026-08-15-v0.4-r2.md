# 2026-W33 X Trend Sensor Run Instruction — v0.4-r2

Instruction ID: `2026-W33-grok-trend-v0.4-r2-2026-08-15`

## 1. Authority

This is the issue-specific execution instruction for the 2026-W33 Weekly Survey X Trend Sensor run.

Read and apply the following repository files before beginning the search:

- `config/prompts/grok/x-trend-sensor-v0.4.md`
- `docs/editorial-specification.md`
- `docs/editorial-style-guide.md`

Prompt SHA-256:

`sha256:823dfc4ee31676caa7fac17e6d655ff1323209940ccb5a7378a99fc13bf1b89e`

If this Run Instruction conflicts with the generic prompt's automatic window-selection rules, **this Run Instruction takes precedence**.

## 2. Corrected W33 observation window

The previous W33 instruction used a rolling collection anchor and therefore did not represent the canonical W33 editorial week. Do not reuse that window for this run.

Use the following exact W33 window:

- Observation Window Start: `2026-08-07T18:00:00-04:00`
- Observation Window Start (Asia/Tokyo): `2026-08-08T07:00:00+09:00`
- Editorial Cutoff: `2026-08-14T18:00:00-04:00`
- Editorial Cutoff (Asia/Tokyo): `2026-08-15T07:00:00+09:00`

The normal W33 ranking window is therefore exactly one editorial week:

`2026-08-07 18:00 America/New_York -> 2026-08-14 18:00 America/New_York`

The actual Grok execution may occur after the Editorial Cutoff. Important topics that become materially significant after the cutoff and before the actual observation completion time must be separated as **Late Breaking** and must not be backfilled into the normal W33 ranking window.

Always distinguish:

- underlying Release / Event date
- X momentum start date
- X peak / persistence date where observable
- actual observation completion time

An underlying event may predate the window and still be a valid W33 candidate if fresh technical-community momentum occurs inside the corrected W33 window, for example through weights publication, Model Hub availability, quantization, local deployment, serving support, integration, independent benchmarking, reproduction, or newly discovered operational constraints.

## 3. Required search procedure

Execute `x-trend-sensor-v0.4` in its mandatory order:

1. Stage 1 — Coverage Scan
2. Stage 1.5 — Mandatory Media Generation Second Pass where required
3. Stage 2 — Candidate Pool
4. Stage 3 — Global Ranking
5. Stage 4 — Coverage Audit
6. Overall X Trend synthesis

Search all Coverage Lanes independently before ranking. Do not treat a global search result as proof that every lane was explored.

For C–F (Multimodal, Image, Video, Speech/Audio/Music), perform the required targeted second pass whenever the first pass is `NONE_FOUND` or `UNCERTAIN`.

Allow `NONE_FOUND`, `NONE_FOUND_CONFIRMED`, and `UNCERTAIN`. Do not promote weak candidates merely to fill a list or category.

Candidate Pool should preserve credible non-Top-10 candidates. Global Ranking must only be produced after Candidate Pool construction.

Do not rank primarily by raw post count, views, or likes. Use relative salience, independent technical participation, hands-on testing/reproduction, benchmark/integration evidence, technical novelty, operational importance, and later primary-source verifiability.

## 4. Evidence boundary

This run is **Trend Discovery / Raw Observation**, not technical factual verification.

X posts may establish:

- that a topic is receiving technical-community attention,
- what practitioners appear to be testing or discussing,
- potential leads for later primary-source verification.

X posts do **not** by themselves establish verified technical facts, benchmark superiority, chronology, resource requirements, product specifications, or general performance claims.

Flag such claims under `Verification Needed` for the downstream Evidence stage.

## 5. Prior W33 result handling

A Grok result generated from the earlier rolling-anchor W33 instruction may be retained as provenance, but it is **not a substitute for this corrected-window run**.

Do not copy its candidate list, ranking, or coverage conclusions into the new output without independently searching the corrected W33 window.

Do not use W32 Raw Observation as a substitute for current W33 searching either.

## 6. Expected output

Create an actual Markdown file named:

`x-trend-sensor-2026-08-15-v0.4-r2.md`

Intended repository path after external review/import:

`sources/2026-W33/grok/raw/x-trend-sensor-2026-08-15-v0.4-r2.md`

Do **not** push to GitHub. Present the Markdown file to the user for import.

The output Front Matter must include at least:

```yaml
sensor: grok
prompt_version: x-trend-sensor-v0.4
instruction_id: 2026-W33-grok-trend-v0.4-r2-2026-08-15
issue_id: "2026-W33"
observation_window_start: "2026-08-07T18:00:00-04:00"
editorial_cutoff: "2026-08-14T18:00:00-04:00"
status: raw
```

`observed_at` must be the actual timezone-bearing Grok completion time. Do not use the instruction-generation time as `observed_at`.

The completed run's collector provenance and hashes will be recorded separately after the file is reviewed and imported into the repository.
