---
id: etamp-environment-injected-memory-poisoning
title: eTAMP：仅靠环境观测就能完成跨 session、跨 site 的 web agent 记忆投毒
status: accepted
card_type: concept
tags: [#agent-security, #memory-poisoning, #prompt-injection, #web-agent, #etamp]
created_time: 2026-05-26T11:00:00+08:00
edited_time: 2026-05-28T15:08:00+08:00
edited_entity: llm
source_ids: [arxiv-etamp-memory-poisoning]
provenance_card: ../provenance/etamp-environment-injected-memory-poisoning.md
aliases: [Environment-injected Trajectory-based Agent Memory Poisoning, 环境注入记忆投毒, eTAMP threat model]
related: [mem0-extract-update-pipeline, memgpt-main-vs-external-context, poisonedrag-knowledge-database-attack-surface, owasp-agentic-top10-2026-positioning]
---

## 攻击定义

**eTAMP（Environment-injected Trajectory-based Agent Memory Poisoning）** 是 Zou、Dong 等（2026, Amazon + PSU）提出的首个"**仅靠环境观测**即可完成 **跨 session、跨 site** 记忆投毒"的攻击[^src1]。攻击者**不需要**直接写入 agent 的 memory store（如 Mem0 的 extract-update 管线[^v3-1] 或 MemGPT 的 main/external 分层[^v3-2] 这类 memory backbone），也**不假设**多用户共享 memory；只要 agent 在 Task A 中访问到一个被污染的网页（如商品页 / 论坛帖），恶意指令就会被 trajectory memory 被动捕获，并在未来 Task B 中被语义检索唤起。

## 与既有威胁模型的区别

- **传统假设**：攻击者要么能直接写入 memory，要么能利用跨用户共享的 memory；这两条都依赖很强的访问权限。
- **eTAMP 假设**：攻击者只能在 user-generated content（评论、商品描述、论坛贴）里塞文本；不能访问 memory、不能访问 model、不能访问 system prompt；甚至**不能保证**自己的内容会被检索召回（只能写"likely to be retrieved"的内容）。
- 这是 lethal trifecta 类的 indirect prompt injection 的"记忆持久化"版本。它与 PoisonedRAG 把"知识库写入权限"作为新攻击面[^v3-3] 同源——都是把攻击面从"模型 / prompt"挪到"agent 部署时被动消费的外部数据"。

## 三条独有特性（攻击者视角的诱惑）

1. **一次污染、多次触发**：同一条被污染的 Task A trajectory 会作为 personalization context 被多个未来任务召回[^src2]。
2. **绕过 permission-based 防御**：基于"只能访问当前 site"的权限隔离在这里失效，因为恶意指令在 Site A 写入、却在 Site B 被合法权限触发。
3. **贴合真实跨 site 工作流**：现实里 agent 经常要先在社交媒体调研、再到电商完成购买——攻击者正是搭这条合法路径的车[^src3]。这也是 OWASP Agentic Top 10[^v3-4] 把 plan / act / decide across workflows 单独列为风险范围的原因。

## 实证效果（无需环境压力时）

在 (Visual)WebArena 约 280 对跨 site 任务上：GPT-OSS-120B 最易受 baseline injection 攻击（19.5%），GPT-5.2 对 authority framing 异常脆弱（22.3%）；Qwen2.5-VL-72B 看似稳健但 task success rate 也很低，**稳健性与可用性是 trade-off**。

## 边界 / 误用条件

- 论文聚焦 **raw trajectory memory**（未压缩、直接当 in-context 示例），不覆盖 consolidated memory（先经 LLM 总结再存）[^src4]。后者攻击难度因总结策略而异，需独立研究。
- 攻击成功率不等于"必然成功"——上限 32.5%（GPT-5-mini + frustration + chaos）仍意味着大多数尝试失败；但 web 流量规模下，即便 5% 的命中率已构成生产级威胁。

## Footnotes

[^src1]: `data/raw/arxiv/arxiv-etamp-memory-poisoning/agent_source_bundle.txt` — 行 88 — "We introduce Environment-injected Trajectory-based Agent Memory Poisoning (eTAMP), the first attack to achieve cross-session, cross-site compromise without requiring direct memory access."
[^src2]: `data/raw/arxiv/arxiv-etamp-memory-poisoning/agent_source_bundle.txt` — 行 145-149 — eTAMP 三条独有特性（一次污染多次触发、绕过 permission 隔离、贴合跨 site 工作流）
[^src3]: `data/raw/arxiv/arxiv-etamp-memory-poisoning/agent_source_bundle.txt` — 行 125 — Xbox controller skin → Reddit review → Shopping 一键下单的完整跨 site 攻击链路示例
[^src4]: `data/raw/arxiv/arxiv-etamp-memory-poisoning/agent_source_bundle.txt` — 行 101 — "We focus on raw trajectory memory rather than consolidated memory, as the latter involves diverse consolidation strategies that would substantially expand the experimental scope."
[^v3-1]: [mem0-extract-update-pipeline](mem0-extract-update-pipeline.md) — eTAMP 不直接写入 Mem0 类 memory 管线，但被污染的 trajectory 会经其 extract 步骤进入长期记忆
[^v3-2]: [memgpt-main-vs-external-context](memgpt-main-vs-external-context.md) — MemGPT 五区结构是受到 eTAMP 影响的典型 memory backbone
[^v3-3]: [poisonedrag-knowledge-database-attack-surface](poisonedrag-knowledge-database-attack-surface.md) — 同样把"被动消费的外部数据"立为新攻击面
[^v3-4]: [owasp-agentic-top10-2026-positioning](owasp-agentic-top10-2026-positioning.md) — agentic 风险清单的范围限定语正对应 eTAMP 的跨 session 跨 site 攻击模型
