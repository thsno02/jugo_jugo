---
id: graphrag-fast-indexing-nlp-hybrid
title: FastGraphRAG NLP 混合索引方法
status: accepted
card_type: algorithm-variant
tags:
- fast-graphrag
- nlp
- noun-phrase-extraction
- co-occurrence-graph
- cost-optimization
created_time: 2026-06-12 18:00:00+08:00
edited_time: 2026-06-12 18:00:00+08:00
edited_entity: llm
source_ids:
- repo-microsoft-graphrag
evidence_basis: code_implementation
justification: ../justification/graphrag-fast-indexing-nlp-hybrid.md
canonical_concept: graphrag-fast-indexing-nlp-hybrid
aliases:
- FastGraphRAG
- fast method
- NLP-based extraction
- 快速图谱RAG
summary: FastGraphRAG 是 GraphRAG 的低成本索引替代方案，用 NLP（NLTK/spaCy 名词短语提取）替代 LLM 进行实体提取，关系定义为实体对在 TextUnit 中的共现，跳过描述摘要和 claim 提取。社区报告使用直接文本块内容而非实体描述。图提取成本估计占索引总成本 75%，FastGraphRAG 显著降低 LLM 消耗但图质量较低且更有噪声。FastGraphRAG
  NLP noun-phrase co-occurrence hybrid indexing。
related:
- graphrag-six-phase-indexing-pipeline
- graphrag-knowledge-graph-augmented-rag
- graphrag-prompt-auto-tuning
---
FastGraphRAG 是 GraphRAG 提供的一种混合索引方法，用传统 NLP 替代部分 LLM 推理以降低成本和加速索引：[^src-1]

- **实体提取**：使用 NLTK + 正则表达式（默认）或 spaCy（semantic parsing / CFG）进行名词短语提取，无独立描述，以源 TextUnit 文本作为描述替代。
- **关系提取**：定义为实体对在 TextUnit 中的共现关系，无独立描述。
- **摘要步骤**：不需要实体/关系描述摘要。
- **Claim 提取**：不使用。
- **社区报告**：使用包含实体名词短语的直接文本块内容（而非实体描述）来 prompt LLM 生成报告。[^src-2]

据材料估计，图提取约占索引总成本的 75%，FastGraphRAG 因此显著降低 LLM 消耗。[^src-3] 代价是提取的图噪声更大，实体不如标准方法精确，不太适合需要高保真实体浏览的场景。若用例主要面向 Global Search 的摘要性问题，FastGraphRAG 能以更低成本提供高质量的概括能力。

使用时建议将 TextUnit chunk size 调小至 50-100 token 以获得更好的共现图效果。[^src-4]

[^src-1]: `data/raw/github_repo/repo-microsoft-graphrag/material_bundle.txt` -- "docs/index/methods.md" P581-596 -- "FastGraphRAG is a method that substitutes some of the language model reasoning for traditional natural language processing (NLP) methods"
[^src-2]: `data/raw/github_repo/repo-microsoft-graphrag/material_bundle.txt` -- "docs/index/methods.md" P589 -- "The direct text unit content containing each entity noun phrase is collected and used to prompt the LLM"
[^src-3]: `data/raw/github_repo/repo-microsoft-graphrag/material_bundle.txt` -- "docs/index/methods.md" P606 -- "We estimate graph extraction to constitute roughly 75% of indexing cost"
[^src-4]: `data/raw/github_repo/repo-microsoft-graphrag/material_bundle.txt` -- "docs/index/methods.md" P595 -- "we also generally configure the text chunking to produce much smaller chunks (50-100 tokens)"
[^card-1]: [graphrag-six-phase-indexing-pipeline](graphrag-six-phase-indexing-pipeline.md) -- FastGraphRAG 修改了该流水线 Phase 3 的实现方式
