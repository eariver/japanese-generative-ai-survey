# Collector raw — Google DeepMind: Private AI Compute + secure server-side memory (Sep 23)

- collector_id: primary-webfetch
- collector_run_id: w39-primary-20260927-r1
- retrieved_at: 2026-09-27T18:41:00Z (webfetch excerpt of live page)
- source_url: https://deepmind.google/blog/advancing-private-ai-compute-with-secure-server-side-memory/
- source_type: PRIMARY_OFFICIAL
- published: 2026-09-23

## Consumed claims

1. EVENT: Architecture update enabling persistent cross-device server-side memory on Private AI Compute (previously stateless). Device-held keys (KEK on device, wrapped DEK), secure enclaves, encrypted channels, per-user encrypted stores; tamper-proof public software record for device-side attestation; independent cybersecurity audit (firm unnamed in excerpt). Co-developed DeepMind + Platforms&Devices + Core + Cloud. (PRIMARY_FACT as architecture announcement)
2. STATUS BOUNDARY: "will enable" / "will bring" language — forward-looking architecture disclosure, NOT a GA availability claim. Independent community note (miketechlife Threads, post-cutoff Sep 26): feature still planned, not generally available. Availability must NOT be claimed.
3. Technical brief PDF (services.google.com, Sep 2026) + audit results referenced but not separately consumed at claim level.

## Boundaries

- Security/architecture properties are vendor-described; audit firm/results not independently verified here.
- No memory-capability or product-availability claim made.
