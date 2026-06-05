---
id: agent-memory-persistent-attack-surface
title: Agent 记忆作为持久性攻击面
status: accepted
card_type: concept
tags: [agent-memory, attack-surface, cross-session, cross-site, permission-bypass, security]
created_time: 2026-06-05T10:00:00+08:00
edited_time: 2026-06-05T10:00:00+08:00
edited_entity: llm
source_ids: [arxiv-etamp-memory-poisoning]
justification: ../justification/agent-memory-persistent-attack-surface.md
canonical_concept: agent-memory-persistent-attack-surface
aliases: [agent记忆攻击面, memory as attack surface, 记忆持久性漏洞, persistent memory vulnerability]
summary: >-
  agent-memory-persistent-attack-surface（agent记忆攻击面 / persistent memory vulnerability）LLM agent 的记忆系统通过存储过去交互来个性化未来任务，但同时创建了一个跨网站、跨会话的持久性攻击面：单次投毒记忆可在任何检索到受污染轨迹的未来任务中反复触发，且能绕过基于权限的防御
related:
  - etamp-environment-memory-poisoning
  - cross-session-continuity
  - rag-knowledge-database-attack-surface
---

LLM 驱动的 web agent 的记忆系统将个性化能力与安全风险紧密耦合 [^src-1]。记忆系统通过存储过去交互的轨迹来个性化未来任务，但这一设计无意中创建了一个**跨网站、跨会话**的持久性攻击面。与传统的单次注入攻击不同，记忆投毒创造的是**持久性漏洞**——一旦投毒成功，受污染的记忆可以在任何检索到该轨迹的未来任务中反复被触发 [^src-2]。

这种持久性攻击面具备三个独特属性。第一，**时间分离**：注入（Task A）和激活（Task B）发生在不同时间，使实时监控难以检测 [^src-3]。第二，**跨站执行**：攻击跨越网站边界——在电商站注入，在社交平台激活——从而绕过基于权限的防御。权限防御假设将 agent 的操作限制在当前任务的网站可防止未授权的跨站行为，但记忆投毒绕过了这一假设：恶意指令在 Task A 期间注入（仅源站可访问），在 Task B 期间激活（agent 对目标站合法拥有权限）[^src-4]。第三，**语义相关性**：攻击利用记忆检索机制，确保投毒内容与未来任务语义相关，从而增加被检索的可能性 [^src-5]。

随着 OpenClaw、ChatGPT Atlas、Perplexity Comet 等 AI 浏览器的兴起，许多缺乏安全专业知识的用户越来越依赖 agent 在多个网站上处理敏感工作流，这使得记忆攻击面的威胁更加紧迫 [^src-6]。

## Footnotes

[^src-1]: `/Users/lw/Desktop/GitHub/llm_wiki/jugo_jugo/data/raw/arxiv/arxiv-etamp-memory-poisoning/agent_source_bundle.txt` -- Abstract -- "Memory makes LLM-based web agents personalized, powerful, yet exploitable. By storing past interactions to personalize future tasks, agents inadvertently create a persistent attack surface that spans websites and sessions."
[^src-2]: `/Users/lw/Desktop/GitHub/llm_wiki/jugo_jugo/data/raw/arxiv/arxiv-etamp-memory-poisoning/agent_source_bundle.txt` -- Section: Threat Model -- "The attack may be repeatedly triggered on any relevant future tasks. Multiple future tasks may retrieve the same Task A trajectory as memory for personalization, meaning a single poisoned memory can affect many subsequent tasks."
[^src-3]: `/Users/lw/Desktop/GitHub/llm_wiki/jugo_jugo/data/raw/arxiv/arxiv-etamp-memory-poisoning/agent_source_bundle.txt` -- Appendix: Attack Characteristics -- "Temporal Separation: The injection (Task A) and activation (Task B) occur at different times, making the attack difficult to detect through real-time monitoring."
[^src-4]: `/Users/lw/Desktop/GitHub/llm_wiki/jugo_jugo/data/raw/arxiv/arxiv-etamp-memory-poisoning/agent_source_bundle.txt` -- Section: Threat Model -- "Permission-based defenses... are ineffective because the attack is injected during Task A (when only the source site is accessible) but activates during Task B (when the agent legitimately has permission for the target site)."
[^src-5]: `/Users/lw/Desktop/GitHub/llm_wiki/jugo_jugo/data/raw/arxiv/arxiv-etamp-memory-poisoning/agent_source_bundle.txt` -- Appendix: Attack Characteristics -- "Semantic Relevance: The attack exploits the memory retrieval mechanism by ensuring the poisoned content is semantically related to future tasks"
[^src-6]: `/Users/lw/Desktop/GitHub/llm_wiki/jugo_jugo/data/raw/arxiv/arxiv-etamp-memory-poisoning/agent_source_bundle.txt` -- Section: Conclusion -- "The proliferation of AI browsers and personal agents such as OpenClaw, ChatGPT Atlas, and Perplexity Comet makes these concerns pressing."
