# W43 r2 first-party reads (2026-10-24/25 UTC; Sol CR-01)

Retrieval: curl (generic UA) for raw HTML where possible; webfetch rendered markdown where bot-walled. No invented bytes; archive status per source below.

## 1. Anthropic auto-mode article — RAW ARCHIVED (599,884B)
- URL: https://claude.com/resources/articles/auto-mode-default-in-claude-code
- Raw: `collectors/primary/runs/20261024T191700Z-muse-r2-evidence/raw/anthropic-auto-mode.html` (HTTP 200).
- Published Aug 7, 2026; **updated Oct 22, 2026 (IN revision)**: auto mode rolls out NEXT WEEK as default for new sessions in MOST Claude apps (Pro/Max/Team); automated check approves safe actions, blocks risky ones and seeks alternatives; enterprise admins get email first.
- Already-default since Aug 14 in Claude Code for Pro/Max/Team (same usage limits; classifier overhead no longer billed); still opt-in for Enterprise, API, Bedrock, Google Agent Platform, Foundry; plan to extend to all apps with cloud partners.
- Safety: internal testing + third-party red-teaming; classifier uses small extra tokens per tool call.
- Chronology: original Aug 7 OUT; Oct 22 update IN as revision; rollout FUTURE at window close (do not claim completed default).

## 2. Decisions API product page — RENDERED BODY READ, NO BYTE ARCHIVE (curl 403)
- URL: https://openai.com/index/decisions-api/ (page dated Oct 22, 2026).
- Read: GA with GPT-6 Luna; v1/decisions; 3 answer types (predicate/choice/score); text/image/JSON; up to 400 questions (2x beta); caching; native GPT-Live integration (avatar reaction demo with session.triggers JSON); customer testimonials (Box 5x, Datadog 40x p95, Ramp 4x/30%, Sierra sub-280ms p95, SpeakBox -90%); $0.10/M input, $0.01/M cached, no output-token charge; US/EU residency, ZDR eligible.
- 10x vs Responses API is vendor-claimed, not independently tested.

## 3. OpenAI API changelog — RAW ARCHIVED (553,250B)
- URL: https://developers.openai.com/api/docs/changelog
- Read: Oct 22 entry "Decisions API now GA with gpt-6-luna" (cache shared input, images in questions, structured input_json); Oct 6 beta entry ("10x faster", 8 denoising steps...); 400-question limit (up from 200); $2 input/$0.20 cached/$10 output (GPT-6 Sol tier) and $0.10/$0.01 (Luna) rate lines.

## 4. Patch the Planet page — RENDERED BODY READ, NO BYTE ARCHIVE (curl 403)
- URL: https://openai.com/index/coordinated-disclosure-of-critical-vulnerabilities/ (page dated Oct 21, 2026).
- Read: PHP critical vulnerabilities found by Calif via GPT-6 Sol under Patch the Planet; Wiz independently found both; maintainers led fixes/patches; Wiz/Cloudflare coordination; 5-stage response framework (validate+fix, advance notice, government coordination incl. White House SIF/ONCD/CISA + intl partners, prepare updates, publish guidance); $1B Daybreak access; Codex skill PHP version checker; disclosure mitigations.
- NO specific CVE identifiers on the page — do not invent any. Distinct from Oct 23 training-containment and from the unverified W42 allegation.

## 5. Google Cloud Model Garden page — RAW ARCHIVED (224,991B)
- URL: https://cloud.google.com/blog/products/ai-machine-learning/google-cloud-brings-openai-models-to-customers
- Read: page dated Oct 22, 2026 (RSS observed Oct 21): GPT-6 Astra / GPT-6.1 Sol / GPT-6 Luna via Model Garden; single Google Cloud invoice, commitments/FSP; data perimeters, prompts never train models, ZDR coming soon.
- Distribution, not a new base model; region/enterprise terms partially stated.

## 6. MemT paper PDF — RAW ARCHIVED (7,096,280B, 65pp)
- arXiv 2610.26825 (abs: v1 submitted Oct 19, 2026).
- Read: abs + intro + Nano/Flash spec tables + benchmark/license sections (see interactive records). GDN-2, MoS, 34B tokens, 1.86x@128K, 66x storage; Nano Qwen3.6-35B-A3B (36B/3B/451M/10M); Flash DeepSeek-V4-Flash (288B/17B/3.61B/336M).
- License finding: paper text contains NO license terms; Apache 2.0/CC BY-NC-SA/PolyForm terms live in repo README (verified separately). Full 65pp equations unaudited.
