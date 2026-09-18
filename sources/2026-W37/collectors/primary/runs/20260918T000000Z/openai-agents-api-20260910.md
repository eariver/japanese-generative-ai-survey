# Retrieval provenance (edition-local collector record)
- collector_id: primary-webfetch
- collector_run_id: w37-primary-20260918-r1
- locator: https://openai.com/index/introducing-the-agents-api
- observed_at: 2026-09-18T00:00:00Z
- published_at: 2026-09-10
- retrieval: webfetch markdown of OpenAI Agents API announcement; stored claim-relevant verbatim excerpts as returned. Page header shows September 10, 2026. Full page consumed via webfetch 2026-09-18.
- authority_class: PRIMARY_OFFICIAL

# Retrieved content (claim-relevant verbatim excerpts)

OpenAI

September 10, 2026

# Introducing the Agents API

Build and run cloud agents with the Codex harness, fully managed by OpenAI.

As we've scaled Codex and ChatGPT for Work to millions of people around the world, we've learned what it takes to make long-running agents work well in practice. Useful agents need a powerful harness that manages context, uses tools efficiently, and coordinates subagents.

Today, we're introducing the Agents API in public beta, bringing that same harness and infrastructure that powers Codex to developers through a simple, flexible API.

## Build cloud agents with a single API call

With the Agents API, you can create a production-ready agent in a single API call by specifying the task, model, tools, and environment. Example uses model gpt-6-astra with MCP tool and multi_agent max_concurrent_subagents 3.

OpenAI hosts and maintains the harness. You choose the agent's compute environment: in an OpenAI-managed sandbox, on your own infrastructure, or with one of our sandbox partners.

## Choose your agent environment

Partnering with ecosystem providers, including Blaxel, Cloudflare, Daytona, DigitalOcean, E2B, Modal, Oracle, Runloop, and Vercel.

## OpenAI hosted sandboxes

Introducing the OpenAI hosted sandbox. This leverages the same sandboxing infrastructure that powers Codex and ChatGPT.

## Build with an evolving Codex harness

Taking advantage of new model capabilities often means reworking your harness. The Agents API provides versioned access to these capabilities with each model launch.

Keep agents working across long sessions: The Agents API automatically compacts earlier context as a session approaches its context limit.

Help agents efficiently use more tools: Tool search loads relevant tool definitions as needed. Programmatic tool calling lets agents run calls in parallel, chain related operations, and filter or combine results in code. Supports MCP, custom functions, and built-in tools like web search.

Let agents parallelize work with subagents: The Agents API can break complex tasks into independent pieces and delegate them to subagents that work in parallel. Each subagent maintains its own context.

## An open-source foundation

The Agents API is powered by the open-source Codex harness. Developers can inspect and learn from its public codebase at github.com/openai/codex.

## Start building

Agents API is available in public beta today to all developers. There are no additional fees for using the Agents API – you simply pay for the tokens and tools your agents use.
