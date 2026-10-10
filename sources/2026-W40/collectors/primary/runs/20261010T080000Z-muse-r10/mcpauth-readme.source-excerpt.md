# SOURCE EXCERPT (bounded) — workers-oauth-provider README (E01 MCP Auth spec)

- artifact_class: COPYRIGHT_BOUNDED_EXCERPT
- source_url: https://raw.githubusercontent.com/cloudflare/workers-oauth-provider/main/README.md
- retrieved_at: 2026-10-10T08:54:32Z (Muse webfetch text; rendered markdown, NOT byte-identical raw)
- access_mode: webfetch-read full README; bounded excerpt archived
- redistribution: bounded quotation only

## Bounded quotes

> `# OAuth 2.1 Provider Framework for Cloudflare Workers` / `@cloudflare/workers-oauth-provider adds OAuth 2.1
> authorization to HTTP APIs and remote MCP servers running on Cloudflare Workers.`
> Split roles (recommended): `OAuthAuthorizationServer` (signs users in, issues tokens) + `OAuthResourceServer`
> (validates over Service Binding, never crosses public Internet); `requiredScopes` vs `scopesSupported` semantics;
> `insufficientScope()` step-up in one line; `OAuthProvider` one-Worker shape retained.
> Threat-relevant mechanics: `resourceMetadata` (RFC 9728 protected-resource metadata); 401 challenge pointing at it;
> rejects tokens issued for any other resource; `props` encrypted with a holder-only key; tokens/codes/secrets stored
> only as hashes; handler owns scopes/ownership/tenancy (`library advertises the required scopes but doesn't enforce
> them, since only your code knows which scopes imply others`).
> Standards: `MCP authorization 2026-07-28`, OAuth 2.1 draft-ietf-oauth-v2-1-13, RFCs 6750/7009/7591/7636/8414/8693/
> 8707/9207/9728 + CIMD + OIDC RP Metadata + experimental MCP Enterprise-Managed Authorization.
> Docs: resource-servers / consent-page / upstream-sign-in / authorization-server reference / mcp-discovery /
> advanced-configuration / storage-schema (KV layout).

## Boundaries

- README consumed; per-doc pages (authorization-server reference, consent, discovery, storage-schema) NOT opened.
- Spec adherence STILL ≠ threat resistance (README itself: handler owns enforcement). No security testing performed.
