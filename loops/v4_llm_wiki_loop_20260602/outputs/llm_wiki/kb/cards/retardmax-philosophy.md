---
id: retardmax-philosophy
title: Retardmax 研究哲学——先行动后思考
status: accepted
card_type: concept
tags: [llm-wiki, research, retardmax, speed-over-planning, iteration]
created_time: 2026-06-11T10:00:00+08:00
edited_time: 2026-06-11T10:00:00+08:00
edited_entity: llm
source_ids: [llm-wiki-net]
justification: ../justification/retardmax-philosophy.md
canonical_concept: retardmax-philosophy
aliases: [retardmax, retardmaxxing, 先行动后思考, act first think later]
summary: >-
  retardmax-philosophy（retardmax / retardmaxxing / 先行动后思考 / act first think later）
  是 LLM Wiki 的极端研究模式：10 个并行智能体、跳过计划阶段、撒最宽的网、
  激进摄入、快速编译、事后 lint 修复——灵感来自 Elisha Long 的 retardmaxxing 哲学
related: [parallel-multi-agent-research, credibility-scoring-pipeline, thesis-driven-research]
---

Retardmax 是 LLM Wiki 中一种**以速度为优先的极端研究模式**，其核心哲学是「先行动，后思考（act first, think later）」[^src-1]。

**具体参数**：
- 启动 **10 个并行智能体**（对比默认 5 个、deep 模式 8 个）[^src-2]
- **跳过计划阶段**——不预先分解研究路径[^src-3]
- **撒最宽的网（cast the widest net）**——不预设角度过滤[^src-4]
- **激进摄入**——降低可信度管道的拒绝阈值（接受 Medium 及以上），但仍计分[^src-5]
- **快速编译**——先出粗稿，事后通过 lint 修复问题[^src-6]

Retardmax 不仅适用于研究命令，也适用于产出命令——`/wiki:output report --retardmax` 立即出粗稿，后续迭代优化[^src-7]。

这一模式灵感来自 **Elisha Long 的 retardmaxxing 哲学**[^src-8]——一种行动优先、容错后置的决策风格。在知识工作语境下的具体含义是：当你不确定该研究什么时，用暴力搜索覆盖最大范围比精心规划更快收敛到有价值的方向。

从系统设计角度看，retardmax 是并行多智能体研究的参数极端化变体[^card-1]。在可信度评分管道中，retardmax 模式降低了拒绝阈值但保留了评分——分数作为 confidence 标签传递到文章中，为事后修复提供线索[^card-2]。与 thesis mode 的设计取向正好相反：thesis mode 追求聚焦（跳过与主张无关的来源），retardmax 追求覆盖（尽可能多地摄入）[^card-3]。

## Footnotes

[^src-1]: `data/raw/webpage/llm-wiki-net/markdown.md` L303 -- "A research mode inspired by Elisha Long's retardmaxxing philosophy — act first, think later."
[^src-2]: `data/raw/webpage/llm-wiki-net/markdown.md` L303 -- "Ten parallel agents, skip planning, cast the widest net, ingest aggressively, compile fast, lint later."
[^src-3]: `data/raw/webpage/llm-wiki-net/markdown.md` L303 -- "skip planning"
[^src-4]: `data/raw/webpage/llm-wiki-net/markdown.md` L303 -- "cast the widest net"
[^src-5]: `data/raw/webpage/llm-wiki-net/markdown.md` L185 -- "5 agents (8 with --deep, 10 with --retardmax) search simultaneously from different angles"
[^src-6]: `data/raw/webpage/llm-wiki-net/markdown.md` L303 -- "compile fast, lint later"
[^src-7]: `data/raw/webpage/llm-wiki-net/markdown.md` L268 -- "Retardmax mode works here too — /wiki:output report --retardmax ships a rough draft immediately. Iterate later."
[^src-8]: `data/raw/webpage/llm-wiki-net/markdown.md` L318 -- "Elisha Long — retardmaxxing philosophy."
[^card-1]: [并行多智能体研究机制](parallel-multi-agent-research.md) -- retardmax 是并行研究的参数极端化变体：10 智能体、不预设角度过滤
[^card-2]: [可信度评分管道](credibility-scoring-pipeline.md) -- retardmax 降低拒绝阈值但保留评分，分数作为 confidence 标签传递到文章
[^card-3]: [论点驱动研究模式](thesis-driven-research.md) -- thesis mode 追求聚焦（跳过无关来源），retardmax 追求覆盖（尽可能多摄入），两者是研究策略谱的两极
