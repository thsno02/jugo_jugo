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
related: [etamp-environment-memory-poisoning, rag-knowledge-corruption-attack, raw-vs-consolidated-memory-vulnerability]
  - etamp-environment-memory-poisoning
  - cross-session-continuity
  - rag-knowledge-database-attack-surface
---

LLM 驱动的 web agent 的记忆系统将个性化能力与安全风险紧密耦合 [^src-1]。记忆系统通过存储过去交互的轨迹来个性化未来任务，但这一设计无意中创建了一个**跨网站、跨会话**的持久性攻击面。与传统的单次注入攻击不同，记忆投毒创造的是**持久性漏洞**——一旦投毒成功，受污染的记忆可以在任何检索到该轨迹的未来任务中反复被触发 [^src-2]。

这种持久性攻击面具备三个独特属性。第一，**时间分离**：注入（Task A）和激活（Task B）发生在不同时间，使实时监控难以检测 [^src-3]。第二，**跨站执行**：攻击跨越网站边界——在电商站注入，在社交平台激活——从而绕过基于权限的防御。权限防御假设将 agent 的操作限制在当前任务的网站可防止未授权的跨站行为，但记忆投毒绕过了这一假设：恶意指令在 Task A 期间注入（仅源站可访问），在 Task B 期间激活（agent 对目标站合法拥有权限）[^src-4]。第三，**语义相关性**：攻击利用记忆检索机制，确保投毒内容与未来任务语义相关，从而增加被检索的可能性 [^src-5]。

随着 OpenClaw、ChatGPT Atlas、Perplexity Comet 等 AI 浏览器的兴起，许多缺乏安全专业知识的用户越来越依赖 agent 在多个网站上处理敏感工作流，这使得记忆攻击面的威胁更加紧迫 [^src-6]。eTAMP 是利用此攻击面的具体攻击机制，通过环境注入和条件触发实现跨会话投毒[^card-1]。类似的持久化知识存储脆弱性也存在于传统 RAG 系统中——PoisonedRAG 表明向知识库注入少量恶意文本即可控制 LLM 回答[^card-2]。进一步地，原始轨迹记忆因完整保留环境观察文本（含恶意指令），对此攻击面尤为脆弱，而整合记忆是否提供内在鲁棒性仍是开放问题[^card-3]。

## Footnotes

[^card-1]: [环境注入式轨迹记忆投毒攻击](etamp-environment-memory-poisoning.md) -- 本卡分析 agent 记忆系统为何构成持久性攻击面（时间分离、跨站执行、语义关联），该卡描述 eTAMP 作为利用此攻击面的具体攻击机制（环境注入 + 条件触发 + 跨会话激活），互为原理与机制的补充
[^card-2]: [RAG 知识腐蚀攻击](rag-knowledge-corruption-attack.md) -- 本卡聚焦 agent 轨迹记忆作为持久性攻击面，该卡展示传统 RAG 知识库同样可被投毒以误导 LLM 推理（约 90% ASR），两者共同表明 LLM 的外部持久化知识存储是系统性安全薄弱环节
[^card-3]: [原始轨迹记忆与整合记忆的脆弱性差异](raw-vs-consolidated-memory-vulnerability.md) -- 本卡分析 agent 记忆为何构成持久性攻击面，该卡进一步区分两种记忆表示范式的脆弱性差异：原始轨迹记忆因保留精确文本而更易受攻击，整合记忆的鲁棒性尚待验证

[^src-1]: `data/raw/arxiv/arxiv-etamp-memory-poisoning/agent_source_bundle.txt` -- Abstract -- "Memory makes LLM-based web agents personalized, powerful, yet exploitable. By storing past interactions to personalize future tasks, agents inadvertently create a persistent attack surface that spans websites and sessions."
[^src-2]: `data/raw/arxiv/arxiv-etamp-memory-poisoning/agent_source_bundle.txt` -- Section: Threat Model -- "The attack may be repeatedly triggered on any relevant future tasks. Multiple future tasks may retrieve the same Task A trajectory as memory for personalization, meaning a single poisoned memory can affect many subsequent tasks."
[^src-3]: `data/raw/arxiv/arxiv-etamp-memory-poisoning/agent_source_bundle.txt` -- Appendix: Attack Characteristics -- "Temporal Separation: The injection (Task A) and activation (Task B) occur at different times, making the attack difficult to detect through real-time monitoring."
[^src-4]: `data/raw/arxiv/arxiv-etamp-memory-poisoning/agent_source_bundle.txt` -- Section: Threat Model -- "Permission-based defenses... are ineffective because the attack is injected during Task A (when only the source site is accessible) but activates during Task B (when the agent legitimately has permission for the target site)."
[^src-5]: `data/raw/arxiv/arxiv-etamp-memory-poisoning/agent_source_bundle.txt` -- Appendix: Attack Characteristics -- "Semantic Relevance: The attack exploits the memory retrieval mechanism by ensuring the poisoned content is semantically related to future tasks"
[^src-6]: `data/raw/arxiv/arxiv-etamp-memory-poisoning/agent_source_bundle.txt` -- Section: Conclusion -- "The proliferation of AI browsers and personal agents such as OpenClaw, ChatGPT Atlas, and Perplexity Comet makes these concerns pressing."
