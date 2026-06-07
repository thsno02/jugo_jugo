---
id: etamp-environment-memory-poisoning
title: 环境注入式轨迹记忆投毒攻击
status: accepted
card_type: mechanism
tags: [memory-poisoning, web-agent, indirect-prompt-injection, cross-session, cross-site, security]
created_time: 2026-06-05T10:00:00+08:00
edited_time: 2026-06-05T10:00:00+08:00
edited_entity: llm
source_ids: [arxiv-etamp-memory-poisoning]
justification: ../justification/etamp-environment-memory-poisoning.md
canonical_concept: etamp-environment-memory-poisoning
aliases: [eTAMP, Environment-injected Trajectory-based Agent Memory Poisoning, 环境注入记忆投毒, 轨迹记忆投毒]
summary: >-
  etamp-environment-memory-poisoning（eTAMP / 环境注入式轨迹记忆投毒）首个通过环境观察单独实现跨会话、跨站点记忆投毒的攻击：攻击者在网页用户生成内容中嵌入恶意指令，agent 浏览后将其存入轨迹记忆，未来在不同网站的任务中被语义检索并触发恶意行为，无需直接访问记忆存储
related: [agent-memory-lifecycle-phases, agent-memory-persistent-attack-surface, frustration-exploitation-attack, graphrag-knowledge-poisoning-attack, rag-knowledge-corruption-attack, rag-knowledge-database-attack-surface]
---

eTAMP（Environment-injected Trajectory-based Agent Memory Poisoning）是首个仅通过环境观察实现跨会话、跨站点记忆投毒的攻击方法 [^src-1]。其核心机制分三步：（1）攻击者在电商产品页、论坛帖等用户生成内容中嵌入条件触发的恶意指令；（2）用户的浏览器 agent 在执行 Task A 时观察到该页面，恶意内容被被动捕获进原始轨迹记忆；（3）用户后续执行语义相关的 Task B 时，投毒记忆被检索为上下文，嵌入的指令在不同网站上激活并执行未经授权的操作 [^src-2]。

该攻击的威胁模型比先前工作更加现实：攻击者仅能通过用户生成内容注入文本、基于可观察的环境特征（如 URL 模式）制作条件触发器，但不能直接访问 agent 的记忆数据库、模型架构或系统提示词 [^src-3]。投毒载荷由三部分组成：重要性信号（如"This is very important!!!"）、触发条件（基于 URL 模式或任务状态的条件语句）、攻击目标（导航至恶意 URL 的 goto 命令）[^src-4]。

实验在 (Visual)WebArena 基准上表明 eTAMP 达到显著的攻击成功率：GPT-5-mini 上高达 32.5%、GPT-5.2 上 23.4%、GPT-OSS-120B 上 19.5% [^src-5]。攻击具有高度隐蔽性——Task A 期间的过早触发率（ASR_A）在几乎所有配置中均为 0%，确保用户无法察觉记忆已被投毒 [^src-6]。GraphRAG 知识投毒攻击从另一个向量展示了类似的威胁——仅修改源文本中极少量词语即可显著扭曲知识图谱并误导推理[^card-1]。PoisonedRAG 对传统 RAG 知识库的投毒攻击则从直接注入角度展示了相似的脆弱性[^card-2]。eTAMP 利用的底层安全漏洞——agent 记忆系统作为持久性攻击面——具有时间分离、跨站执行等独特属性[^card-3]。从记忆生命周期角度看，eTAMP 直接针对 Evidence 阶段——agent 浏览时产生的观察事件被投毒，恶意内容在进入 Consolidation 人工审批之前就已作为原始证据被语义检索[^card-4]。

## Footnotes

[^card-1]: [GraphRAG 知识投毒攻击](graphrag-knowledge-poisoning-attack.md) -- eTAMP 通过环境观察投毒 agent 轨迹记忆（跨会话、跨站点），KPA 通过修改源文本投毒知识图谱构建过程（<0.05% 修改量），两者从不同攻击向量揭示了 LLM 知识系统的投毒脆弱性
[^card-2]: [RAG 知识腐蚀攻击](rag-knowledge-corruption-attack.md) -- eTAMP 间接投毒 agent 轨迹记忆（通过环境注入），PoisonedRAG 直接投毒 RAG 知识库（通过文本注入），两者代表了 LLM 知识投毒的不同攻击路径
[^card-3]: [Agent 记忆作为持久性攻击面](agent-memory-persistent-attack-surface.md) -- 本卡描述 eTAMP 的具体攻击机制（环境注入 + 条件触发），该卡从安全架构角度分析 agent 记忆系统为何构成持久性攻击面（时间分离、跨站执行、语义关联），互为机制与原理的补充
[^card-4]: [Agent 记忆四阶段生命周期](agent-memory-lifecycle-phases.md) -- eTAMP 攻击直接针对生命周期的 Evidence 阶段——agent 浏览时的观察事件被投毒，恶意内容在 Consolidation 人工审批之前就已进入检索路径，揭示了快速摄取与审批延迟之间的安全窗口

[^src-1]: `data/raw/arxiv/arxiv-etamp-memory-poisoning/agent_source_bundle.txt` -- Abstract -- "We introduce Environment-injected Trajectory-based Agent Memory Poisoning (eTAMP), the first attack to achieve cross-session, cross-site compromise without requiring direct memory access."
[^src-2]: `data/raw/arxiv/arxiv-etamp-memory-poisoning/agent_source_bundle.txt` -- Section: Threat Model -- "A malicious seller on an e-commerce platform embeds hidden instructions in their product page... Days later, the user asks their agent to 'research good games on Reddit'... the poisoned memory activates and causes the agent to post a promotional review"
[^src-3]: `data/raw/arxiv/arxiv-etamp-memory-poisoning/agent_source_bundle.txt` -- Section: Threat Model -- "We assume the attacker can inject text into web pages through user-generated content and craft conditional triggers based on observable features (e.g., URL patterns), but cannot directly access the agent's memory, model, or system prompts"
[^src-4]: `data/raw/arxiv/arxiv-etamp-memory-poisoning/agent_source_bundle.txt` -- Section: Attack Strategies -- "Each attack payload consists of three components: Importance Signal... Trigger Condition... Attack Goal..."
[^src-5]: `data/raw/arxiv/arxiv-etamp-memory-poisoning/agent_source_bundle.txt` -- Abstract -- "eTAMP achieves substantial attack success rates: up to 32.5% on GPT-5-mini, 23.4% on GPT-5.2, and 19.5% on GPT-OSS-120B"
[^src-6]: `data/raw/arxiv/arxiv-etamp-memory-poisoning/agent_source_bundle.txt` -- Section 3.3 -- "Across all models tested... and most attack strategies, ASR_A is 0%"
