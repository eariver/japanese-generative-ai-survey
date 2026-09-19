# Retrieval provenance (edition-local collector raw, NOT exact HTTP bytes)
- source_url: https://blog.character.ai/cai-image-models/
- retrieved_at: 2026-09-19T00:00:00Z (worker webfetch markdown excerpt; exact HTTP bytes not captured)
- collector_id: primary-webfetch
- collector_run_id: w38-primary-20260919-r1
- published_date_on_page: Sep 16, 2026
- authority_class: PRIMARY_OFFICIAL (Character.ai first-party engineering blog)

# Post-training image models for fandom (excerpt)

CAI-Image family: own line of image models, post-trained versions of open-source Qwen-Image, tuned for character-driven storytelling. Draws (c.ai) Comics; powers Imagine/Imagine Message.

Rationale: character recognizability across styles/scenes/pages at speed/cost for millions of users — "generation in seconds, a fraction of the cost, control over every stage" (vendor positioning).

Four trained capabilities: style range/transfer (multitude of art styles by name; palette as direct instruction; image style reference incl. cross-subject); multi-character scenes + pose control (multi-image inputs: characters + pose + style + location in one generation); cinematic camera control (245 distinct camera positions in natural language: 5 distances x 7 horizontal x 7 vertical; reference-driven); manga/comics (dedicated page model: panel structure, accurate text, camera variation, emotion, frame-to-frame continuity; structured prompt assembly from chat/premise; 100+ page community works).

Infrastructure: CAI-MM-Studio full-stack (data pipelines, multi-node training, automated eval with purpose-built scoring models, optimized serving).

Next: CAI-Image V2 (consistent environments, finer inter-character emotion, smarter manga layout/text); Animate Comics (short story-driven videos, same characters); anime agent design post upcoming.

## Claim boundary notes (Sol consumption)
- VERIFIED from this page: family existence/launch (Sep 16 2026); Qwen-Image post-tune lineage (vendor-stated); four capability areas as vendor-described design goals; 245 camera positions (vendor-stated spec); CAI-MM-Studio existence (vendor-described).
- Side-by-side benchmark claims vs "strongest closed and open models" are vendor-presented visuals without reproducible methodology here — PARTIAL, not verified fact.
