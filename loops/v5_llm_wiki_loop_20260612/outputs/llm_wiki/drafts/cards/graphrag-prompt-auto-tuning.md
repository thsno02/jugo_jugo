---
id: graphrag-prompt-auto-tuning
title: GraphRAG Prompt 自动调优机制
status: draft
card_type: technique
tags: [prompt-tuning, auto-tuning, domain-adaptation, entity-extraction, few-shot]
created_time: 2026-06-12T18:00:00+08:00
edited_time: 2026-06-12T18:00:00+08:00
edited_entity: llm
source_ids: [repo-microsoft-graphrag]
evidence_basis: code_implementation
justification: ../justification/graphrag-prompt-auto-tuning.md
canonical_concept: graphrag-prompt-auto-tuning
aliases: [auto prompt tuning, prompt-tune, domain-adapted prompts, 自动提示词调优, graphrag prompt-tune]
summary: >-
  GraphRAG 提供 prompt auto-tuning 功能，通过加载输入文本、切分为小 chunk（默认200 token）、采样文本单元（random/top/all/auto 四种选择策略）、运行 LLM 推断域信息和实体类型，生成领域适配的 extract_graph/summarize_descriptions/community_report 三个 prompt 文件。auto 策略对文本嵌入降维后选取质心的 k 近邻。建议在正式索引前执行以提升图提取质量。prompt auto-tuning domain adaptation selection-method。
related: [graphrag-six-phase-indexing-pipeline, graphrag-fast-indexing-nlp-hybrid]
---

GraphRAG 强烈建议在正式索引前运行 Prompt Auto-Tuning（`graphrag prompt-tune`），以生成适配特定数据领域的 prompt，从而提升知识图谱提取质量。[^src-1]

Auto-Tuning 的工作流程：[^src-2]

1. 加载输入数据并切分为小文本单元（默认 chunk size 200 token）
2. 使用文档选择策略从文本单元中采样：
   - `random`（默认推荐）：随机选取
   - `top`：选取前 n 个
   - `all`：全量（仅适用于小数据集）
   - `auto`：对文本单元嵌入降维，选取距质心最近的 k 个邻居
3. 运行 LLM 推断域信息、发现实体类型
4. 通过模板替换生成最终 prompt 文件

产出三个 prompt 文件供索引使用：`extract_graph.txt`、`summarize_descriptions.txt`、`community_report.txt`。[^src-3]

关键参数包括 `--domain`（数据领域描述）、`--language`（处理语言）、`--discover-entity-types`（自动发现实体类型，适用于跨主题数据）、`--min-examples-required`（实体提取示例最低数量）。[^src-4]

[^src-1]: `data/raw/github_repo/repo-microsoft-graphrag/material_bundle.txt` -- "docs/prompt_tuning/overview.md" P1860-1867 -- "Auto Tuning leverages your input data and LLM interactions to create domain-adapted prompts"
[^src-2]: `data/raw/github_repo/repo-microsoft-graphrag/material_bundle.txt` -- "docs/prompt_tuning/auto_prompt_tuning.md" P1878-1879 -- "loading the inputs, splitting them into chunks... running a series of LLM invocations and template substitutions"
[^src-3]: `data/raw/github_repo/repo-microsoft-graphrag/material_bundle.txt` -- "docs/prompt_tuning/auto_prompt_tuning.md" P1956-1965 -- extract_graph, summarize_descriptions, community_report prompt paths
[^src-4]: `data/raw/github_repo/repo-microsoft-graphrag/material_bundle.txt` -- "docs/prompt_tuning/auto_prompt_tuning.md" P1899-1924 -- command-line options including --domain, --selection-method, --discover-entity-types
[^card-1]: [graphrag-six-phase-indexing-pipeline](graphrag-six-phase-indexing-pipeline.md) -- auto-tuning 生成的 prompt 用于 Phase 3 图提取
