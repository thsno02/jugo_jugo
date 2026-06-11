---
schema: justification_journal.v1
card: ../cards/session-lessons-extraction.md
created_time: 2026-06-11T10:00:00+08:00
---

## creation | 2026-06-11T10:00:00+08:00

生成方式：source extraction pass
来源：`data/raw/webpage/llm-wiki-net/markdown.md`
源证据：
- L37 — "Extract lessons learned from the current session — error->fix patterns, user corrections, discoveries. Saved as structured notes the wiki can query later. --rules emits enforceable rules instead of prose."
- L144 — "/wiki:ll Extract lessons from current session into wiki. --dry-run,--rules."
范围论证：会话教训提取是 LLM Wiki 中唯一明确面向**过程知识**而非**事实知识**的机制。现有卡片中 output-compounding-loop 描述事实知识的复利循环，audit-provenance-tracing 描述信任验证，都不涉及从 agent 工作会话中提取元学习经验。`--rules` 模式更构成了从观察到行为约束的独特转化能力。这是一个原子级的独立概念。
