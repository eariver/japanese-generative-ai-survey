# Retrieval provenance (edition-local collector record)
- collector_id: primary-webfetch
- collector_run_id: w37-primary-20260918-r1
- locator: https://openai.com/index/introducing-gpt-live-1-in-the-api
- observed_at: 2026-09-18T00:00:00Z
- published_at: 2026-09-10
- retrieval: webfetch markdown of OpenAI GPT-Live-1 API announcement; stored claim-relevant verbatim excerpts as returned. Page header shows September 10, 2026. Full page consumed via webfetch 2026-09-18.
- authority_class: PRIMARY_OFFICIAL

# Retrieved content (claim-relevant verbatim excerpts)

OpenAI

September 10, 2026

# Build more natural voice experiences with GPT-Live-1 in the API

GPT-Live-1 brings ChatGPT's natural, full-duplex conversations to the API, with more control over how voice agents speak and act.

We're launching GPT-Live-1 in the API, giving developers a powerful, natural voice model for building voice-enabled apps and business workflows. First introduced in ChatGPT, GPT-Live-1 is capable of listening and speaking at the same time, and, as seen with Codex and ChatGPT Work, can delegate deeper reasoning and actions to the models and tools it is paired with.

Key strengths of GPT-Live-1 in the API:

- Interruption handling: Improves interruption handling via a single model that reasons over incoming and outgoing audio together, avoiding the latency and brittle handoffs of chained STT-LLM-TTS architectures.
- Reasoning & tool calling delegation: GPT-Live-1 can delegate reasoning and tool calls to a backend text model like GPT-6 Astra or a third-party model.
- Tone, pace, and style: Lets developers shape an agent's tone, pace, and conversational style through the system prompt.
- Silent context management & background noise: Better handles background noise and silence without interrupting the conversation or narrating every step out loud.
- Long-session reliability: Improves context retention and conversational quality across extended interactions.
- Telephony support: Enables deployment of full-duplex voice agents for phone calls, from restaurant reservations to customer support.

Traditional voice agents stitch together speech-to-text, a reasoning model, and text-to-speech. Each handoff adds latency and creates more opportunities to lose timing, context, or the natural rhythm of a conversation.

GPT-Live-1 handles listening and speaking in a single model, simplifying the voice layer. It can respond to interruptions and acknowledgements as they happen, while delegating deeper reasoning to the back end.

Developers choose the models, tools, and agent harness behind the conversation. For example, they might pair GPT-Live-1 with a model like Luna for high-volume tasks like scheduling or order updates, and use a model like Astra for complex customer issues that require reasoning.

GPT-Live-1 natively provides ASR transcripts and response text. It also offers strong alphanumeric understanding and supports keyword biasing.

## Measuring the full-duplex advantage

Across our evaluations, GPT-Live-1 improves Full Duplex Bench performance by 30 percentage points over GPT-Realtime-2.1, with large gains in turn-taking latency and interactive behavior. Paired with GPT-6 Astra at medium reasoning effort, it also ranks #1 on Tau3, which measures frontier voice-agent intelligence on end-to-end tasks.

## What customers are saying

Yelp, Speak, Fin (Intercom), Cognition quoted as early users. Speak early evaluations: cut interruptions during thinking pauses by almost 80% compared with previous turn-based systems. Yelp Host: improved turn-taking and accuracy over traditional voice architecture.

## New voice options

Expanding from a small set of real-time voices to a broader selection across accents, dialects, and languages.

## Pricing & Availability

GPT-Live-1 is available in the API today at $0.05 per minute for the front-end voice layer. Pair it with the backend model and agent harness that fit your product.
