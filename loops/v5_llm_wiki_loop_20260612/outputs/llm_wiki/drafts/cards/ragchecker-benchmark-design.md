---
id: ragchecker-benchmark-design
title: RAGChecker 评估基准设计
status: draft
card_type: dataset-description
tags: [benchmark, 10-domains, long-form-answer, odqa, ragchecker]
created_time: 2026-06-12T16:00:00+08:00
edited_time: 2026-06-12T16:00:00+08:00
edited_entity: llm
source_ids: [arxiv-ragchecker]
evidence_basis: experimental_paper
justification: ../justification/ragchecker-benchmark-design.md
canonical_concept: ragchecker-benchmark-design
aliases: [RAGChecker benchmark, RAGChecker evaluation benchmark, 10 域基准]
summary: >-
  RAGChecker 配套基准涵盖 10 个领域（Wikipedia/Novel/Writing/Biomedical/Finance/Lifestyle/Recreation/Science/Technology/AI Science）共 4162 个 query，源自 RobustQA、KIWI、ClapNQ、NovelQA 等公开 ODQA 数据集。关键设计：将原始短答案通过 GPT-4 转为长文本答案以匹配现代 LLM-based RAG 输出，并用 RefChecker 质控确保无幻觉。每条样本为 <query, documents, ground-truth answer> 三元组。
related: [ragchecker-framework-overview, claim-level-entailment-checking]
---

RAGChecker 框架配套了一个跨 10 领域的评估基准数据集。[^src-1]

**数据规模**：4,162 个 queries，覆盖 Wikipedia (ClapNQ, 300)、Novel (NovelQA, 280)、Writing (500)、Biomedical (BioASQ, 511)、Finance (500)、Lifestyle (500)、Recreation (500)、Science (500)、Technology (500)、AI Science (KIWI, 71)。[^src-2]

**关键设计决策**：现有 ODQA 数据集多为短答案，而现代 LLM-based RAG 生成长文本回答。因此需要将短答案转换为长文本答案：[^src-3]
- 对 RobustQA/NovelQA：使用 GPT-4 (gpt-4-turbo-2024-04-09) 将人工标注的短答案和对应 passage 转换为长文本答案
- 质控：用 RefChecker 检查所有长文本答案中的 claims 是否被源 passage 蕴含，仅保留无幻觉的答案

**数据格式**：每条样本为 <query q, documents D, ground-truth answer gt> 三元组，其中 D 被按固定 token 数切分为 chunks。[^src-4]

[^src-1]: `data/raw/arxiv/arxiv-ragchecker/agent_source_bundle.txt` -- "sections/experiments.tex Benchmark Datasets" -- "we curate a benchmark containing 4,162 queries across 10 domains...repurposed from public datasets of open domain question answering"
[^src-2]: `data/raw/arxiv/arxiv-ragchecker/agent_source_bundle.txt` -- "tables in sections/experiments.tex" -- Table 1 benchmark statistics
[^src-3]: `data/raw/arxiv/arxiv-ragchecker/agent_source_bundle.txt` -- "sections/appendix_data_curation.tex Long-form Answer Generation" -- "We employ GPT-4 to convert the human annotated short answers to long-form answers...We use RefChecker to check whether all the claims of a long-form answer are entailed by these passages"
[^src-4]: `data/raw/arxiv/arxiv-ragchecker/agent_source_bundle.txt` -- "sections/framework.tex Inputs to RAGChecker" -- "We prepare each sample in our benchmark dataset in the format of a tuple <q, D, gt>"

[^card-13]: 参见 [ragchecker-framework-overview] 了解框架如何消费这些数据
