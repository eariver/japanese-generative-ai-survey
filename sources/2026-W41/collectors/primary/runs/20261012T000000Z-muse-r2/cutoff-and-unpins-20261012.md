# Collector excerpts r2-B — cutoff-sensitive leads + r1 unpins (Muse r2)

Retrieved: 2026-10-12 (UTC). Cutoff: `2026-10-09T22:00:00Z`. Rule: day-only Oct 9 → TIME_UNRESOLVED.

## 1. Clef-omni issuer blog — UPGRADED TO IN-WINDOW (exact timestamp)

URL: https://blog.cloudflare.com/clef-faster-cheaper-multimodal/ (full first-party page read).
- JSON-LD: `datePublished: 2026-10-09T18:27:34.129Z`, `dateModified: 2026-10-09T22:14:16.400Z`.
- 18:27:34Z < 22:00:00Z cutoff → ORDINARY IN-WINDOW (exact-instant evidence; modification after cutoff is an update, not the event).
- Content: Qwen3-Omni-30B-A3B MoE backbone; native audio (wav/mp3) + video (mp4/webm); latencies (text ~130ms median, image ~150ms, 21s video ~1.5s); vendor benchmark table (BFCL 98.2, BANKING77 94.8, CLINC150 97.7, etc., all vendor-run); flash $0.09→$0.038/M (hosted context cut 64k→24k); Clef up to 2.0× via SGLang; HF open weights.
- Supersedes r1 TIME_UNRESOLVED row with exact timestamp.

## 2. Microsoft-Decision-1 (Oct 9, day-only → TIME_UNRESOLVED)

URL: https://commandline.microsoft.com/microsoft-decision-1-model-foundry/ (first-party page read; header `2026.10.09`, no clock observed).
- Qwen3.5-9B post-trained decision scorer; Foundry + OpenRouter; 36-benchmark 83.5% vendor claim; $0.042/M input, outputs free; rebase roadmap (MAI/OpenAI).
- Secondary (Oct 9–10) corroborates date but adds no clock. No pre-22:00Z proof → TIME_UNRESOLVED HOLD/CONTEXT.

## 3. Tencent Youtu-Parsing-Omni (HOLD/CONTEXT)

- HF repo tencent/Youtu-Parsing-Omni: weights upload ~20h before 2026-10-12 observation (≈Oct 10–11, POST-cutoff); License `youtu-parsing` (NOT Apache); 5B omni-modal; papers Jan/Jul 2026 (pre-window).
- No October issuer announcement event located; page-level "2026-10" insufficient for cutoff. → HOLD/CONTEXT (upload recency ≠ dated October event; post-cutoff upload).

## 4. r1 unpins resolved

- **Ironclad full body**: READ (Oct 6, day-only). 11 EDGAR-simulated tasks; Astra 55.0% vs Sol 41.6%; times are SIMULATED estimates (NOT measured savings — footnote-explicit). → first-party corroborated with simulation caveat.
- **Gemini rollout page**: READ (Cloud blog Oct 9, day-only — corroborates Oct 8 announcement, not a new event). Sub-agents with @agents.company.com identities, 4 memory types, skills registries, governance (identity/policy/audit/gateway), cost controls; customer figures vendor-stated. → announcement-level depth closed.
- **Mistral weights**: HF shows "Upcoming release", ETA Oct 31, "Waiting for the release" → NOT downloadable. Preserved.
- **Beam weights**: waitlist + beta API only (secondary Oct 11 corroborates) → NOT downloadable. Preserved.
- **llama.cpp v0.6.0**: tag NOT observed (rolling b1155x builds dated Oct 11, post-window) → UNRESOLVED, not claimed.
- **Mistral 49B/52B nuance**: HF placeholder text — "49B active per token (52B incl. embeddings/output layers)". Both r1 figures reconciled: use 49B/token-active vs 52B incl. embeddings with pins.
