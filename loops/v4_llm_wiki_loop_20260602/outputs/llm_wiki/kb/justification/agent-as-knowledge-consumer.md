---
schema: justification_journal.v1
card: ../cards/agent-as-knowledge-consumer.md
created_time: 2026-06-11T10:00:00+08:00
---

## creation | 2026-06-11T10:00:00+08:00

生成方式：增量提取（falconer-enterprise-guide 第二轮）
来源：`data/raw/webpage/falconer-enterprise-guide/markdown.md`
源证据：
- "Step 5: Query the wiki" 段 — "increasingly by AI coding agents through protocols like Claude MCP. The agents query the same knowledge graph the humans do, which means agent outputs ground in the same current context the team operates from."
- FAQ "Can AI coding agents query an enterprise LLM wiki?" — "Coding agents reading stale internal documentation produce stale outputs; the Anthropic engineering team describes context as the scarcest resource for AI agents."
- "How Falconer maps to the pattern" 段 — "AI coding agents query the same graph through Claude MCP, so the agents read current context rather than the snapshot the wiki captured six months ago."
- YC RFS 引用 — "If we want every company to run on AI automation, we need a new primitive: a company brain."
范围论证：现有卡中 continuous-drift-detection 提及 Anthropic 的"context as scarcest resource"作为支撑论据，但未将 agent 作为知识消费者这一角色转变独立概念化。executable-guidance-vs-context-pile（来自 Cognition 源）关注的是消费内容的形态差异（技能 vs 笔记），本卡关注的是消费者身份的转变（从人类到 agent）和消费协议的标准化（Claude MCP）。两者正交互补。YC RFS 的"company brain"引用在该来源中被明确用于支撑 agent 消费的产业趋势论证，与 Cognition 源中对同一 RFS 的引用角度不同（Cognition 强调可执行性，Falconer 强调时效性和同一图谱）。
