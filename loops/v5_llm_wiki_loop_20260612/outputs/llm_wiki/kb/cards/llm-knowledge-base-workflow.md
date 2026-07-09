---
id: llm-knowledge-base-workflow
title: LLM 知识库端到端工作流
status: accepted
card_type: workflow-architecture
tags:
- knowledge-management
- llm-agent
- personal-wiki
created_time: 2026-06-12 17:00:00+08:00
edited_time: 2026-06-12 17:00:00+08:00
edited_entity: llm
source_ids:
- karpathy-x-launch-post
evidence_basis: practitioner_report
justification: ../justification/llm-knowledge-base-workflow.md
canonical_concept: llm-knowledge-base-workflow
aliases:
- LLM Knowledge Bases
- LLM wiki workflow
- LLM 个人知识库
summary: llm-knowledge-base-workflow LLM知识库端到端工作流 Karpathy提出的使用LLM构建个人知识库的完整流程： raw数据摄入→LLM增量编译为markdown wiki→Obsidian查看→Q&A查询→输出渲染归档→Linting健康检查→工具扩展。 token吞吐从代码操作转向知识操作。端到端流水线可视为新产品方向。
related:
- wiki-compilation-by-llm
- obsidian-as-llm-ide
- llm-wiki-qa-without-rag
- llm-wiki-linting
- llm-knowledge-base-pattern
- llm-wiki-three-step-workflow
- idea-file-concept
- llm-knowledge-base-scalability
- llm-wiki-output-filing-back
---
Andrej Karpathy 描述了一套使用 LLM 构建个人知识库的端到端工作流，核心阶段为：

1. **数据摄入 (Data ingest)**: 将源文档（文章、论文、仓库、数据集、图片等）索引到 `raw/` 目录
2. **Wiki 编译**: LLM 增量"编译"原始数据为结构化 .md wiki（含摘要、反向链接、概念分类、文章互联）
3. **IDE 查看**: 使用 Obsidian 作为前端浏览 raw 数据、编译后的 wiki 及衍生可视化
4. **问答 (Q&A)**: 对 wiki 执行复杂查询，LLM 自行研究并返回答案
5. **输出渲染**: 将结果渲染为 markdown/幻灯片/图表，归档回 wiki 形成累积
6. **Linting**: LLM 执行"健康检查"确保数据一致性
7. **工具扩展**: 自建搜索引擎等 CLI 工具供 LLM 使用

其核心洞察：大量 LLM token 吞吐正从操作代码转向操作知识（以 markdown 和图片存储）。[^src-1]

[^src-1]: `data/raw/webpage/karpathy-x-launch-post/text.txt` -- "LLM Knowledge Bases" -- "a large fraction of my recent token throughput is going less into manipulating code, and more into manipulating knowledge (stored as markdown and images)"
