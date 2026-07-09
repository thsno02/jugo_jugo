---
id: graphrag-entity-extraction-self-reflection
title: GraphRAG 实体抽取中的 Self-Reflection 技术
status: accepted
card_type: technique
tags:
- graphrag
- entity-extraction
- self-reflection
- gleaning
- prompt-engineering
- recall
created_time: 2026-06-12 16:00:00+08:00
edited_time: 2026-06-12 16:00:00+08:00
edited_entity: llm
source_ids:
- arxiv-graphrag
evidence_basis: experimental_paper
justification: ../justification/graphrag-entity-extraction-self-reflection.md
canonical_concept: graphrag-entity-extraction-self-reflection
aliases:
- self-reflection
- gleaning
- entity gleaning
- 实体 gleaning
- 自反思实体抽取
summary: GraphRAG graphrag-entity-extraction-self-reflection self-reflection gleaning 技术在实体抽取后将已抽取实体返回 LLM，用 logit bias 100 强制 yes/no 判断是否遗漏，若是则追加 continuation 引导补抽。可迭代多轮（最多指定上限）。HotPotQA 实验中 600 token
  chunk 从 0 轮 9348 实体引用增至 3 轮 27240（约 3x 提升）。允许使用更大 chunk size 而不丧失抽取质量。GPT-4 在 chunk 2400 vs 600 时抽取实体近半，self-reflection 弥补此差距。
related:
- graphrag-pipeline-architecture
- graphrag-relationship-fine-tuning
---
GraphRAG 使用 self-reflection（又称 gleaning）提升知识图谱抽取阶段的实体召回率。

**动机**: LLM 从更大 chunk 中抽取的实体数量显著减少——在 HotPotQA 数据集上，GPT-4 在 chunk size 600 token 时抽取的实体引用数几乎是 chunk size 2400 的两倍。

**机制**:
1. 从 chunk 抽取实体后，将已抽取实体返回 LLM
2. 使用 logit bias=100 强制 yes/no 判断："是否有实体被遗漏？"
3. 若回答 yes，追加 continuation："MANY entities were missed in the last extraction" 引导 LLM 补充抽取
4. 重复此过程直至达到指定最大迭代次数

**实验效果**（HotPotQA, GPT-4-turbo）:
- 600 token chunk: 0 轮 → 9,348 实体引用; 3 轮 → 27,240
- 1200 token chunk: 0 轮 → 7,119; 3 轮 → 22,399
- 2400 token chunk: 0 轮 → 5,761; 3 轮 → 19,433

每轮 self-reflection 带来一致的增益，且不引入强制噪声。此设计允许在更大 chunk（更少 LLM 调用=更低成本）下维持抽取质量。

[^src-1]: `data/raw/arxiv/arxiv-graphrag/agent_source_bundle.txt` -- "Self-Reflection" (Appendix A.2) -- "we deploy a self-reflection prompt engineering approach...prompting it to glean any entities that it may have missed"
[^src-2]: `data/raw/arxiv/arxiv-graphrag/agent_source_bundle.txt` -- "Self-Reflection" (Appendix A.2) -- "GPT-4 extracted almost twice as many entity references when the chunk size was 600 tokens than when it was 2400"
[^card-1]: [graphrag-pipeline-architecture] 流水线第二步依赖此技术
