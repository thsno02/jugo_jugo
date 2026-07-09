---
id: ragas-faithfulness-metric
title: RAGAS Faithfulness 指标：claim 分解与验证
status: accepted
card_type: metric-definition
tags:
- faithfulness
- hallucination-detection
- claim-decomposition
- llm-verification
- rag-evaluation
created_time: 2026-06-12 16:00:00+08:00
edited_time: 2026-06-12 16:00:00+08:00
edited_entity: llm
source_ids:
- arxiv-ragas
evidence_basis: experimental_paper
justification: ../justification/ragas-faithfulness-metric.md
canonical_concept: ragas-faithfulness
aliases:
- Faithfulness
- RAGAS faithfulness score
- 忠实度指标
summary: RAGAS Faithfulness 指标通过两步 LLM prompting 计算：(1) claim decomposition 将答案拆为原子陈述集合 S； (2) verification 判断每条陈述是否可从 context 推出。F = |V| / |S|，其中 V 为 supported 陈述子集。 在 WikiEval 上准确率 0.95，远超 GPT Score (0.72)
  和 GPT Ranking (0.54)。
related:
- ragas-framework-overview
- ragas-answer-relevance-metric
- ragas-context-relevance-metric
- ares-ais-answer-faithfulness-evaluation
- selfcheckgpt-sampling-consistency
- wikieval-dataset
---
Faithfulness 衡量生成答案是否有 context 根据——即答案中的 claims 能否从检索到的上下文推出。[^src-1]

**计算流程**分两步：

1. **Claim decomposition**: 用 LLM 将答案拆为原子陈述集合 S(a_s(q))，prompt 为 "Given a question and answer, create one or more statements from each sentence in the given answer"。[^src-2]

2. **Verification**: 对每条陈述 s_i，用 LLM 判定 s_i 是否可从 context c(q) 推出，要求先给出简短解释再给 verdict (Yes/No)。[^src-3]

最终得分 F = |V| / |S|，其中 |V| 为被判定 supported 的陈述数，|S| 为全部陈述数。[^src-4]

在 WikiEval pairwise comparison 中，RAGAS Faithfulness 与人工判断一致率达 0.95。[^card-1][^src-5]

[^src-1]: `data/raw/arxiv/arxiv-ragas/agent_source_bundle.txt` -- "Evaluation Strategies / Faithfulness" P266 -- "Faithfulness refers to the idea that the answer should be grounded in the given context"
[^src-2]: `data/raw/arxiv/arxiv-ragas/agent_source_bundle.txt` -- "Evaluation Strategies / Faithfulness" P281-285 -- "create one or more statements from each sentence in the given answer"
[^src-3]: `data/raw/arxiv/arxiv-ragas/agent_source_bundle.txt` -- "Evaluation Strategies / Faithfulness" P288-293 -- "determine whether they are supported by the information present in the context"
[^src-4]: `data/raw/arxiv/arxiv-ragas/agent_source_bundle.txt` -- "Evaluation Strategies / Faithfulness" P294 -- "F = |V| / |S|"
[^src-5]: `data/raw/arxiv/arxiv-ragas/agent_source_bundle.txt` -- "Experiments / Table 1" P386 -- "Ragas 0.95"
[^card-1]: 见 [ragas-framework-overview] 对三维度的总体说明
