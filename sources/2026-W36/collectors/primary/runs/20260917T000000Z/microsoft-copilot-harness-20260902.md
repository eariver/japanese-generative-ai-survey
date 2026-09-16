# Retrieval provenance (edition-local collector record)
- collector_id: primary-webfetch
- collector_run_id: w36-primary-20260917-r1
- locator: https://www.microsoft.com/en-us/microsoft-copilot/blog/copilot-studio/new-and-improved-github-copilot-harness-agent-skills-and-richer-context
- observed_at: 2026-09-17T00:00:00Z
- published_at: 2026-09-02
- retrieval: webfetch markdown of Microsoft Copilot Blog "New and improved: GitHub Copilot harness, agent skills, and richer context"; stored verbatim as returned. Page label shows Monthly Updates, September 2, 6 min read; lede frames as August 2026 Copilot Studio updates.
- authority_class: PRIMARY_OFFICIAL

# Retrieved content (verbatim as returned)

# New and improved: GitHub Copilot harness, agent skills, and richer context

By Jason Moore, Vice President of Product, Microsoft Copilot Studio. Monthly Updates. September 2, 6 min read.

[Microsoft Copilot Studio](https://www.microsoft.com/en-us/microsoft-365-copilot/microsoft-copilot-studio/) is giving makers new ways to build agents that can reason through complex work, draw on richer context, and use a growing range of tools and capabilities to get real work done.

At the center of the latest Copilot Studio updates is the **general availability of the GitHub Copilot harness**, the new foundation for building reasoning-heavy agents and workflows in Copilot Studio. Alongside the harness, recent updates add new ways for agents to use skills, memory, enterprise knowledge, workflows, model context protocol (MCP) servers, connected agents, files, and more.

## Build agents and workflows for complex business processes with the GitHub Copilot harness

The GitHub Copilot harness is now generally available in Copilot Studio. This advanced harness is designed for reasoning-heavy agents and workflows that need to complete complex business processes.

The harness sits between the AI model and the agent or workflow you build, orchestrating how the components work together. It helps determine when to call the model, what context to provide, and which tools, MCP servers, or connected agents to use. This allows agents and workflows to plan steps and adapt their approach as they work toward the defined goal in a recursive manner. Basically, rather than relying on predefined paths, the agent or workflow can adjust its execution path based on the goal and the available inputs.

The harness also supports capabilities like **skills and memory** and can natively create and edit Word, Excel, PowerPoint, and PDF files. Each task runs in a secure sandbox governed by Copilot Studio.

All this makes the GitHub Copilot harness particularly well suited for scenarios that combine reasoning with action across multiple steps. For example, an accounts payable agent could read invoices, match them to purchase orders, gather missing information, and route exceptions for approval.

The GitHub Copilot harness is available alongside the standard harness, so you can choose the foundation that best fits what you're building.

## Expand what your agents can do with skills, tools, and connected agents

-   **Skills** let you package instructions into modular, reusable capabilities. Write a skill or upload an existing skill, add it to multiple agents, and share it with your teammates.
-   For larger solutions, **connected agents** (in preview) let a primary agent delegate requests to specialized agents.
-   Now in generally available, you can also add **workflows and MCP servers as tools**. Workflows can give agents access to multistep deterministic automation, while MCP servers can connect them to external services and capabilities.
-   With the **Windows 365 for Agents MCP server**, now generally available, agents can interact with a Windows 365 Cloud PC to work with desktop applications, browsers, and user interfaces.

## Give agents richer context with knowledge, memory, and files

With **Work IQ in Copilot Studio** (preview), agents powered by the GitHub Copilot harness can connect to organizational context such as emails, calendar events, files, Microsoft Teams messages, and people information. You can also connect an agent to **Foundry IQ** to use a knowledge base you've already built and tuned in Microsoft Foundry.

**Memory** (also in preview) allows an agent to retain relevant information from previous interactions with an individual user. When enabled, memory can capture preferences and patterns and apply them in later conversations.

Agents can also take on **larger, more complex document-based work**. Now in preview, users can give agents files to analyze and work with directly. Users can also view files the agent creates during the conversation.

## Manage agents with greater visibility and control

As of July 2026, Copilot Studio automatically creates a Microsoft Entra Agent ID for every new agent. This gives individual agents their own identity in Microsoft Entra and helps administrators apply identity and access controls at the agent level.

For agents using MCP servers, you can also now submit an MCP server for Microsoft certification. Certification provides customers and administrators with additional information that an MCP server has been evaluated against Microsoft expectations for areas including reliability, security, compliance, and responsible operation.

With **environment-level agent telemetry**, now in preview, administrators can export telemetry from Copilot Studio to Application Insights through the Microsoft Power Platform admin center.

## Reach customers across voice and digital channels with real-time agents

Previously available for voice experiences, **real-time agents can now also be deployed to digital messaging channels**. Currently in preview, this feature allows you to use the same agent configuration across voice and digital messaging.

For voice experiences, you can now use **GPT-5 Chat**. The model, also in preview, uses a text-based voice architecture that converts speech to text, generates a response, and synthesizes it back to speech.

You can **monitor real-time agents with Application Insights in Azure Monitor**.

## More improvements to help you build

-   **Choose from more models.** Claude Sonnet 5 and GPT-5.5 Chat are now generally available as primary models.
-   **Build with the right foundation for the job.** With multiple harness options available in Copilot Studio, you can choose between reasoning-heavy, multi-step experiences and more structured, predictable agent scenarios.

[truncated for edition-local storage: site navigation, images, related posts, and footer omitted; core article text preserved verbatim]
