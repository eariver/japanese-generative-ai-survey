# W43 r2 consumption note 02 — 1Password for Agents (DC-03, SUBSTANTIVELY_CONSUMED 2026-10-24)

Sources: blog `1password.com/blog/1password-for-ai-agents` (John Torrey, Oct 22, 7 min) + press `1password.com/press/2026/october/1password-for-agents-trust-layer-personal-ai-agents` (Toronto, Oct 22 9:00am EDT). Both webfetch-read in full.

## Mechanism (trust boundary, not credential sharing)
- Agent reaches sign-in → requests credential from 1Password vault → user approves on own device → 1Password autofills directly into site form; agent never sees password/OTP. Unique digital key verifies agent identity to 1Password. Disconnect anytime; single-vault updates propagate.
- Threat model addressed: pasting passwords into prompts (persistent copies), browser-saved/manual-takeover friction. Safeguards vary by integration; permissions are per-login approvals.

## Availability (live vs planned — do NOT claim all deployed)
- Rolling out over coming days (all platforms): Muse (Meta), Grok Bot (SpaceXSI).
- Coming soon: Claude Duet (Anthropic), ChatGPT Work + dots (OpenAI), Townie (Town web+iOS).
- Additional integrations coming: Browserbase, Browser Use, Dana, Instinct, KERNEL, Perplexity, Ramp, Tomo, Wajo.
- Offer: no additional cost for Individual/Family on 1Password.com; .eu/.ca NOT supported. Enterprise vault context: 1.6B credentials, 200k businesses.
- Partner quotes corroborate per-vendor framing: Nat Friedman (Meta), Ami Vora (Anthropic, "asks before sign-in; soon 1Password completes"), Glen Coates (OpenAI, no credential exposure to model), Tido Carriero (SpaceXSI), Jean-Denis Greze (Town).

## Why material for W43
- Agent credential-handoff standard intersecting Duet (Oct 21), Muse, ChatGPT Work/dots, Grok Bot in the same week. Complements (not duplicates) vendor safety promises: vendor model safety ≠ credential-plane control. Evidence must keep per-integration availability pinned; never present coming-soon as live.
