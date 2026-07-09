---
id: graphrag-context-window-lost-in-middle
title: GraphRAG 中小 Context Window 优于大窗口的实验发现
status: draft
card_type: empirical-finding
tags: [graphrag, context-window, lost-in-middle, 8k-tokens, comprehensiveness]
created_time: 2026-06-12T16:00:00+08:00
edited_time: 2026-06-12T16:00:00+08:00
edited_entity: llm
source_ids: [arxiv-graphrag]
evidence_basis: experimental_paper
justification: ../justification/graphrag-context-window-lost-in-middle.md
canonical_concept: graphrag-context-window-lost-in-middle
aliases: [context window selection, lost in the middle, 8k context window, GraphRAG context size]
summary: >-
  GraphRAG graphrag-context-window-lost-in-middle 实验测试 8k 16k 32k 64k 四种 context window size 用于 gpt-4-turbo (128k max)。结果 8k 在 comprehensiveness 上普遍最优（平均 win rate 58.1%），diversity 和 empowerment 持平。论文将此归因于 lost in the middle 现象（Liu et al. 2023）——LLM 在长上下文中间的信息召回降低。因此 GraphRAG 固定使用 8k token context window 进行社区摘要生成和查询回答。
related: [graphrag-community-hierarchy-cost-performance, graphrag-pipeline-architecture]
---

GraphRAG 论文发现较小的 context window 在全局问答质量上反而优于较大窗口。

**实验设置**: 测试 8k / 16k / 32k / 64k 四种 context window size（模型为 gpt-4-turbo, 最大支持 128k token）。

**结果**:
- **Comprehensiveness**: 8k 普遍最优，平均 win rate 58.1%
- **Diversity**: 8k 与更大窗口持平，平均 win rate 52.4%
- **Empowerment**: 8k 与更大窗口持平，平均 win rate 51.3%

**解释**: 论文引用 "lost in the middle" 现象（Liu et al., 2023; Kuratov et al., 2024）——LLM 在处理长上下文时，位于中间位置的信息更容易被忽略或遗忘。较小窗口迫使每次 map 步骤处理更少但更集中的信息，避免信息稀释。

**设计决策**: 基于此发现，GraphRAG 在最终评估中统一使用 8k token 作为社区摘要生成、社区答案生成和全局答案生成的 context window size。

[^src-1]: `data/raw/arxiv/arxiv-graphrag/agent_source_bundle.txt` -- "Context Window Selection" (Appendix C) -- "the smallest context window size tested (8k) was universally better for all comparisons on comprehensiveness (average win rate of 58.1%)"
[^src-2]: `data/raw/arxiv/arxiv-graphrag/agent_source_bundle.txt` -- "Context Window Selection" (Appendix C) -- "Given the potential for information to be lost in the middle of longer contexts"
[^card-1]: [graphrag-community-hierarchy-cost-performance] context window 大小影响各层级的实际 token 使用
