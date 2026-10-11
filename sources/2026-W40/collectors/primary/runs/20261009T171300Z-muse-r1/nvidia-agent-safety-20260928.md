# Collector raw — NVIDIA: Open Agent Safety Platform (Sep 28)

- collector_id: primary-webfetch
- collector_run_id: w40-primary-20261009-muse-r1
- retrieved_at: 2026-10-09T17:13:32Z (webfetch excerpt of live newsroom page)
- source_url: https://nvidianews.nvidia.com/news/open-agent-safety-platform
- source_type: PRIMARY_OFFICIAL
- published: 2026-09-28 (newsroom header; investor release same date; technical blog Sep 28 by Myers/Watson/Golshan/Arkin)

## Consumed claims (claim-level)

1. EVENT: NVIDIA announced Open Agent Safety Platform on Sep 28, 2026: open software platform + reference system design for agent testing-to-deployment governance. (PRIMARY_FACT: announcement occurred, date)
2. COMPONENTS: OpenShell open-source secure runtime (sandboxed execution, kernel-level isolation, policy enforcement, verifiable tracing) now broadly available; Sentry reference design = out-of-band watchdog on BlueField-4 DPUs (DOCA), quarantines out-of-boundary agents in milliseconds, attested telemetry, identity/zero-trust enforcement. Optimized for Vera CPU + BlueField DPU; OpenShell extendable to Arm/Intel. (PRIMARY_FACT as vendor architecture description; effectiveness is vendor claim)
3. PRINCIPLES (technical blog): verifiable policy, out-of-band enforcement, controlling path to model, scaling authority with reasoning visibility, shared responsibility; Vera Rubin POD tray includes BlueField-4 on node's only path to model. (VENDOR_CLAIM as design rationale)
4. ECOSYSTEM (vendor-stated): 100+ orgs incl. Anthropic (Claude Managed Agents + OpenShell/BlueField), SpaceXAI (Cursor/Grok), Scale AI, Salesforce/Slack, SAP Joule, Accenture, CrowdStrike, Cisco, Dell, HPE, Red Hat/Canonical/SUSE, Baseten/CoreWeave/Nebius, Figure/Gecko/Skild, Citi/JPMorganChase, Hitachi Energy/EPRI. Partner quotes are vendor-published. (VENDOR_CLAIM as partnership status, not independent deployment proof)
5. AVAILABILITY: OpenShell + skills via developer resources page + GitHub (github.com/NVIDIA/OpenShell); Sentry is reference system design (no separate price/GA date in announcement; TechRepublic notes same). Open Secure AI Alliance (Linux Foundation, 120+ orgs) + SAFE exchange. (PRIMARY_FACT as vendor availability statement with noted limits)

## Boundaries / unresolved

- Reference architecture != empirically attack-proof containment; no independent red-team reproduction in this raw.
- Sentry hardware-isolated enforcement depends on BlueField-4 deployment; OpenShell alone does not include it.
- Investor-URL vs newsroom-URL are same announcement; use newsroom as canonical locator.
