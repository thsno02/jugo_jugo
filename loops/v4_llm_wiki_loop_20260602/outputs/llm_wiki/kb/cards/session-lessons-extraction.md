---
id: session-lessons-extraction
title: 会话教训提取机制
status: accepted
card_type: mechanism
tags: [llm-wiki, lessons-learned, session, error-patterns, meta-learning]
created_time: 2026-06-11T10:00:00+08:00
edited_time: 2026-06-11T10:00:00+08:00
edited_entity: llm
source_ids: [llm-wiki-net]
justification: ../justification/session-lessons-extraction.md
canonical_concept: session-lessons-extraction
aliases: [会话教训提取, lessons extraction, wiki:ll, 经验教训机制]
summary: >-
  session-lessons-extraction（会话教训提取 / lessons extraction / wiki:ll / 经验教训机制）
  是 LLM Wiki 的元学习命令：从当前会话中提取 error->fix 模式、用户纠正和发现，
  保存为结构化笔记供 wiki 后续查询，--rules 模式可产出可执行规则而非散文
related: [output-compounding-loop, audit-provenance-tracing]
---

`/wiki:ll`（lessons learned）是 LLM Wiki 中将**临时会话经验转化为持久知识**的机制[^src-1]。

**提取内容**包含三类[^src-2]：
1. **错误->修复模式（error->fix patterns）**——会话中犯的错误及其修正方式
2. **用户纠正（user corrections）**——用户对 agent 行为的反馈和修改
3. **发现（discoveries）**——会话过程中意外发现的有价值信息

**输出格式**有两种[^src-3]：
- **默认模式**：保存为**结构化笔记**，wiki 可在后续查询中引用这些经验
- **`--rules` 模式**：产出**可执行规则（enforceable rules）**而非散文——适合转化为系统行为约束

`--dry-run` 标志允许预览提取结果而不实际写入[^src-4]。

这一机制的设计位置处于**产出复利循环的元层**——普通产出（报告/幻灯片等）复利于 wiki 中的事实知识，lessons-learned 复利于 wiki 中的**过程知识**[^card-1]。当提取的教训涉及来源质量判断（如「这类博客通常不可靠」），它们也能间接强化审计追踪的判断基准[^card-2]。

从知识管理的角度看，lessons-learned 是 wiki 的**反射能力（reflexive capability）**——系统不仅积累外部世界的知识，也积累关于自身工作方式的知识。`--rules` 模式更进一步，将反射性观察转化为行为约束，实现从「知道教训」到「执行教训」的跨越。

## Footnotes

[^src-1]: `data/raw/webpage/llm-wiki-net/markdown.md` L37 -- "Extract lessons learned from the current session — error->fix patterns, user corrections, discoveries. Saved as structured notes the wiki can query later."
[^src-2]: `data/raw/webpage/llm-wiki-net/markdown.md` L37 -- "error->fix patterns, user corrections, discoveries"
[^src-3]: `data/raw/webpage/llm-wiki-net/markdown.md` L37 -- "--rules emits enforceable rules instead of prose."
[^src-4]: `data/raw/webpage/llm-wiki-net/markdown.md` L144 -- "/wiki:ll Extract lessons from current session into wiki. --dry-run,--rules."
[^card-1]: [产出复利循环](output-compounding-loop.md) -- lessons-learned 是产出复利的元层变体：普通产出复利于事实知识，教训提取复利于过程知识
[^card-2]: [审计与溯源追踪](audit-provenance-tracing.md) -- 提取的教训可间接强化审计判断基准（如来源质量模式）
