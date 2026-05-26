---
schema: draft_card_provenance.v3
draft_card: ../cards/karpathy-wiki-full-context-vs-rag.md
material_id: obsidian-community-plugin
digest_id: digest_obsidian-community-plugin
source_paths:
  - data/raw/webpage/obsidian-community-plugin/text.txt
created_time: 2026-05-26T12:40:00+08:00
edited_time: 2026-05-26T12:40:00+08:00
edited_entity: llm
---

## 源证据

- 第 344 行（立场 verbatim）：
  > "This plugin follows Karpathy's philosophy: feed the LLM full Wiki context, not chunked RAG retrieval. Long-context models are strongly recommended — the larger your Wiki grows, the more context the LLM needs."
- 第 346 行（反 RAG verbatim）：
  > "Karpathy's original critique argues that RAG fragments knowledge and breaks the LLM's ability to reason across the full knowledge graph."
- 第 348–366 行（模型选型表 verbatim）。
- 第 371 行（本地 Ollama 上下文限制 + 混合方案）：
  > "For local models (Ollama): context windows are typically smaller (8K–128K). Consider using a cloud provider for ingestion + local model for query."

## 卡片范围是否成立

- 卡片以 distinction 类型对比 RAG 与 Karpathy LLM Wiki 模式，并把这立场的工程后果（模型选型表 + 混合方案）连接起来——与页面"为什么这套不是 RAG"的核心论证一致。
- 直接来自源：立场陈述、反 RAG 一句、模型选型表、本地 Ollama 限制。
- 引申点：
  - 比较表（RAG vs 本插件）是对页面陈述的结构化整理；
  - "边界与代价" 那一节明确标注页面**未**公开的退化策略（超大 wiki 时如何降级），属诚实标注。

## 发表门控结果

本轮未运行。

## 备注

- 与 `karpathy-llm-wiki-obsidian-plugin-overview` 互补：overview 列出模型表，本卡解释为何选长上下文。
- 与本 batch `karpathy-wiki-extraction-granularity` 协同：抽取粒度的设计也是为了让长上下文窗口"装得下"。
- 与 v2 卡片 `auto-index-replaces-rag-at-small-scale` 概念近似（都谈 RAG 替代方案），comparison 阶段建议建立 cross-link 并评估范围差异。
