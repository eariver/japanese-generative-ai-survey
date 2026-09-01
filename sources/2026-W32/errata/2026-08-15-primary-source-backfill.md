# 2026-W32 primary-source backfill / chronology errata

Status: **non-destructive post-Release correction record**  
Recorded: `2026-08-15`  
Authority: user-approved W32→W33 carry-over audit correction in the 2026-W33 compilation session  
Published issue preserved: `weekly/2026-W32/v0.2`

This record does **not** replace or mutate the frozen 2026-W32 PDF, tag, source manifest, or Release asset. It documents factual/provenance defects discovered while auditing W32 carry-over during W33 compilation.

## 1. GPT-5.6 Sol W32 update was primary-confirmable

W32 Candidate Selection retained `openai-gpt-5.6-w32-update` as `HOLD_OUT` because the distinct W32 update was unresolved.

The W33 official-page collection preserved an OpenAI News RSS snapshot that contains the first-party item:

- title: `Improving GPT‑5.6 Sol in ChatGPT—and expanding access to GPT-5.6 Luna for free users`
- publication time: `2026-08-06T10:00:00Z`
- canonical URL: `https://openai.com/index/improving-gpt-5-6-sol-in-chatgpt`

That timestamp is inside the W32 main editorial window. The W32 unresolved disposition therefore reflects a verification miss, not absence of a primary source.

**Correction:** classify this as a W32 primary-source backfill. Do not redatetime it into W33.

Primary provenance retained by W33:

- `sources/2026-W33/collectors/official-pages/runs/20260815T104430Z/raw/openai-news-rss.html`
- raw SHA-256 from collector manifest: `382fe92628ebc1b69481cc6f62a56a05c3610ef3755291d2621923260356fb3a`

## 2. Claude Opus 4.1 API retirement was primary-confirmable

W32 Candidate Selection retained `claude-opus-4.1-api-retirement` as `HOLD_OUT` because the exact Anthropic retirement notice was unresolved.

Anthropic's first-party model-deprecation documentation records:

- model: `claude-opus-4-1-20250805`
- deprecation announcement: `2026-06-05`
- retirement date: `2026-08-05`
- recommended replacement at the recorded page: `claude-opus-4-8`

The retirement date is inside W32. The event was therefore primary-confirmable during W32 even though the W32 Evidence pass did not resolve it.

**Correction:** classify the Aug 5 retirement as a W32 primary-source backfill. Do not present it as a new W33 event.

Primary locator rechecked on 2026-08-15:

- `https://platform.claude.com/docs/en/docs/about-claude/model-deprecations`

Because this source is a living documentation page, the exact dates/model identifier above are the bounded facts of this erratum; later page changes must not silently alter this record.

## 3. Astra cyber item was not post-cutoff

W32 selected `openai-astra-cyber-critical-late` as `LATE_BREAKING` and described the OpenAI Preparedness/cyber update as an Aug 7 post-cutoff item.

The preserved OpenAI RSS snapshot gives the first-party publication time for:

- title: `Responding to the next frontier of critical cyber capabilities`
- publication time: `2026-08-07T15:20:00Z`
- canonical URL: `https://openai.com/index/responding-next-frontier-critical-cyber-capabilities`

On 2026-08-07 New York was on EDT (`UTC-04:00`), so the publication time is `2026-08-07 11:20 EDT`. The W32 editorial cutoff was `2026-08-07 18:00 EDT`.

**Correction:** this item was inside the W32 main window by 6 hours 40 minutes. Its `LATE_BREAKING` / post-cutoff chronology classification was incorrect. The substantive caution retained by W32—OpenAI said it could not rule out Critical cyber capability rather than declaring Astra formally Critical—remains unchanged.

Primary provenance retained by W33:

- `sources/2026-W33/collectors/official-pages/runs/20260815T104430Z/raw/openai-news-rss.html`
- raw SHA-256 from collector manifest: `382fe92628ebc1b69481cc6f62a56a05c3610ef3755291d2621923260356fb3a`

## Scope and publication effect

These corrections are provenance/chronology backfills only. They establish neither independent capability validation nor permission to rewrite the already-published W32 issue.

The original W32 Release remains the historical artifact. Future retrospective work and chronology generation should consume this erratum in addition to the frozen W32 source set so that the three corrected facts are not propagated incorrectly.
