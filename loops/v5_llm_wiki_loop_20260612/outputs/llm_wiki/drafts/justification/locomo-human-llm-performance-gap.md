# Justification: locomo-human-llm-performance-gap

## 抽取理由
人类与 LLM 的性能差距（overall 56%，temporal 73%）是 LoCoMo 论文的标志性发现之一，直接出现在 Abstract 和 Introduction 的核心结论中。这一定量差距对评估当前 LLM 长期记忆能力具有基准参考价值。

## 原子性检验
该卡聚焦于"人机差距的全局量化"——与 temporal-reasoning-difficulty 卡（聚焦类型间差异原因）和 adversarial-hallucination 卡（聚焦对抗性具体机制）互补但不重叠。本卡的知识价值在于提供全景式的 human baseline 对比。

## 来源锚定
- Table qa_results 第一行 Human baseline 数据
- Introduction 段落"improvements ranging from 22-66%... still significantly lag behind human levels (by 56%), especially in temporal reasoning (by 73%)"
