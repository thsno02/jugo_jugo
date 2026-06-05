---
id: comparison-compression-vs-transformation-granularity
title: 有损压缩 vs 澄清性转化——粒度细化的两种路径
status: accepted
card_type: distinction
tags: [granularity, memory-system, compression, transformation, information-loss]
created_time: 2026-06-05T18:00:00+08:00
edited_time: 2026-06-05T18:00:00+08:00
edited_entity: llm
source_ids: [arxiv-longmemeval, arxiv-locomo]
justification: ../justification/comparison-compression-vs-transformation-granularity.md
canonical_concept: compression-vs-transformation-granularity
aliases: [压缩与转化的粒度区分, compression vs transformation in granularity]
summary: >-
  comparison-compression-vs-transformation-granularity（压缩与转化的粒度区分）揭示粒度细化的两条路径产生相反效果：LongMemEval 的事实提取是有损压缩（丢失信息、损害 QA），LoCoMo 的观察提取是澄清性转化（消除共指噪声、提升 QA）；设计记忆系统时，关键不是"要不要细化"而是"细化是否保留语义完整性"
related: [memory-value-granularity-tradeoff, observation-based-memory-representation]
---

将对话记忆从原始轮次进一步细化为更小单元时，两个独立基准得出了看似矛盾的结论：

**LongMemEval 发现事实提取损害性能**。将轮次压缩为摘要或用户事实虽然节省 token，但因信息丢失对总体 QA 产生了负面影响（唯一例外是跨会话推理）[^card-1]。

**LoCoMo 发现观察提取提升性能**。将对话轮次转化为关于说话者的断言式陈述（observation），以 top-5 获得 F1=41.4，显著优于原始对话的 31.7[^card-2]。

矛盾的根源在于两种"细化"本质不同：

| 维度 | 事实提取（LongMemEval） | 观察提取（LoCoMo） |
|------|----------------------|-------------------|
| 操作类型 | 有损压缩 | 澄清性转化 |
| 信息变化 | 丢弃上下文、细节、语气 | 消除共指、对话噪声 |
| 语义完整性 | 降低 | 保持或提升 |
| 典型效果 | QA 下降（除跨会话推理） | QA 上升（尤其时序推理） |

这一区分的设计启示是：在选择记忆存储粒度时，核心问题不是"是否进一步分解"，而是"分解过程是否保留了回答下游问题所需的语义完整性"。有损压缩通过删减实现简洁；澄清性转化通过重组实现清晰。两者的粒度产出可能相似（都是短文本片段），但信息保真度截然不同。

## Footnotes

[^card-1]: [记忆存储粒度权衡](memory-value-granularity-tradeoff.md) -- 本卡的"有损压缩"一侧：事实级压缩因信息丢失损害 QA，轮次级为最优存储粒度
[^card-2]: [观察断言式记忆表示优于原始对话检索](observation-based-memory-representation.md) -- 本卡的"澄清性转化"一侧：断言式观察消除共指噪声，以 F1=41.4 显著优于原始对话 31.7
