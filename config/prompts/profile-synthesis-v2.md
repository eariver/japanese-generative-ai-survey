# Survey Production Core v2 — Profile Synthesis

Prompt ID: `profile-synthesis-v2`

Produce exactly one JSON Profile Synthesis Result conforming to `schemas/profile-synthesis-v2-result.schema.json` from the supplied Synthesis Input.

Rules:

1. Synthesize only from the validated Draft Results supplied in `drafts`; do not introduce new factual claims or silently repair a Draft with external knowledge.
2. Follow `profile_payload_requirements` for the active Research Profile and `publication_payload_requirements` for the active Publication Profile.
3. Keep Research Profile semantics inside `profile_payload` and Publication Profile semantics inside `publication_payload`.
4. Weekly synthesis may discuss current signals/carry-over only when those requirements are supplied by the Weekly Profile. Thematic and Period work must never emit dummy `this_week_signals` or equivalent Weekly placeholders.
5. Thematic synthesis must preserve unresolved lineage/historical-attribution boundaries when those are required; do not convert uncertainty into direct ancestry or priority claims.
6. Preserve limitations and explicit Draft boundary handling. Synthesis may compress prose, but it may not erase a material caveat merely because several Draft packages are combined.
7. Return JSON only. Do not return Markdown fences, commentary, LaTeX, or prose outside the JSON object.
