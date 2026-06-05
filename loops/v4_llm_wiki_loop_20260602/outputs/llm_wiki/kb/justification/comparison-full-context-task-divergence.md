# Justification: comparison-full-context-task-divergence

## 为什么需要这张卡

full-context-accuracy-ceiling 和 long-context-comprehension-illusion 两张卡分别记录了全上下文方法在不同任务上的表现，但单独阅读任一张卡都可能得出片面结论：前者暗示全上下文是准确率金标准，后者暗示长上下文必然退化。两者的分歧本身构成了一个独立的原子洞察——全上下文方法的效果取决于任务类型，而非简单的"越多越好"或"越多越差"。

## 来源依据

- LOCOMO QA 数据来自 Mem0 论文（arxiv-mem0）Table 2：Full-context Judge=72.90%
- LOCOMO 事件摘要数据来自 LoCoMo 论文（arxiv-locomo）Table 4：GPT-3.5-turbo F1=45.9 vs GPT-3.5-turbo-16K F1=39.9
- 两组数据均基于 LOCOMO 基准的不同子任务，确保了对比的公平性

## 判断类型

distinction -- 两张卡记录了同一方法（全上下文）在不同任务维度上的相反表现，其分歧本身是一个值得独立记录的设计考量
