---
id: time-aware-query-expansion
title: 时间感知 Query Expansion 改善时间推理
status: accepted
card_type: empirical-finding
tags:
- long-term-memory
- temporal-reasoning
- query-expansion
- retrieval
created_time: 2026-06-12 16:00:00+08:00
edited_time: 2026-06-12 16:00:00+08:00
edited_entity: llm
source_ids:
- arxiv-longmemeval
evidence_basis: experimental_paper
justification: ../justification/time-aware-query-expansion.md
canonical_concept: time-aware-query-expansion
aliases:
- time-aware query expansion
- temporal query expansion
- 时间感知查询扩展
summary: time-aware-query-expansion 在 LongMemEval_M 时间推理子集上，通过时间感知索引和查询扩展策略——对 value 额外索引其包含事件的日期，检索时由 LLM 从时间敏感查询中提取时间范围并过滤无关 value——使用 round 作为 value 时平均提升 recall 11.3%，使用 session 时提升 6.8%。效果依赖于使用强 LLM（GPT-4o）进行时间范围推断；Llama
  3.1 8B 常产生幻觉时间范围或遗漏时间线索导致假阳性过滤。
related:
- unified-memory-framework-three-stages
- fact-augmented-key-expansion
- longmemeval-retrieval-augmentation
---

LongMemEval 揭示了一个关键挑战：利用元数据和用户话语中的时间信息来正确回答时间敏感查询。论文提出时间感知索引和查询扩展方案：[^src-1]

**索引阶段**：对 value 额外索引其包含事件的日期（由 Llama 3.1 8B 提取带时间戳的事件）。

**检索阶段**：由 LLM M_T 从时间敏感查询中提取时间范围，用于过滤大量无关 value。

实验结果（时间推理子集）：
- Value=Round 时平均提升 recall 11.3%（使用 GPT-4o 作为 M_T）
- Value=Session 时提升 6.8%
- 与 key expansion 组合后提升仍一致[^src-2]

效果高度依赖 M_T 的能力：
- GPT-4o 能正确判断查询是否包含时间引用并拒绝生成无依据的时间范围
- Llama 3.1 8B 即使有大量 in-context 示例也常幻觉出时间范围，导致错误剪枝搜索空间[^src-3]

[^src-1]: `data/raw/arxiv/arxiv-longmemeval/agent_source_bundle.txt` -- "text/5_experiment.tex" Section "Query: Time-aware query expansion" -- "we introduce a simple yet effective time-aware indexing and query expansion scheme"
[^src-2]: `data/raw/arxiv/arxiv-longmemeval/agent_source_bundle.txt` -- "text/5_experiment.tex" -- "this simple design improves recall by an average of 11.3% when using rounds as the value and by 6.8% when using sessions"
[^src-3]: `data/raw/arxiv/arxiv-longmemeval/agent_source_bundle.txt` -- "text/appendix.tex" Section "Strong and weak LLMs for extracting time ranges" -- "the model often mistakenly extracts a time range, which erroneously prunes out the search space"
