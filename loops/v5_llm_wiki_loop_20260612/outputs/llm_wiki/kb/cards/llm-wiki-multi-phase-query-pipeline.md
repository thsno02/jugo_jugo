---
id: llm-wiki-multi-phase-query-pipeline
title: LLM Wiki 多阶段查询检索管线
status: accepted
card_type: architecture-pattern
tags:
- retrieval
- query-pipeline
- llm-wiki
- vector-search
- graph-expansion
- budget-control
created_time: 2026-06-12 19:00:00+08:00
edited_time: 2026-06-12 19:00:00+08:00
edited_entity: llm
source_ids:
- repo-nashsu-llm-wiki
evidence_basis: code_implementation
justification: ../justification/llm-wiki-multi-phase-query-pipeline.md
canonical_concept: llm-wiki-multi-phase-query-pipeline
aliases:
- multi-phase query pipeline
- 多阶段检索管线
- query retrieval pipeline
- optimized query retrieval
summary: LLM Wiki 多阶段查询检索管线（multi-phase query pipeline）：Phase 1 Tokenized Search（中文
  bigram + 英文分词）→ Phase 1.5 可选 Vector Semantic Search（LanceDB，recall 从 58.2% 提升至 71.4%）→
  Phase 2 Graph Expansion（4-signal 模型 2-hop 带衰减）→ Phase 3 Budget Control（60/20/5/15
  wiki/chat/index/system 分配）→ Phase 4 Context Assembly（编号页面 + citation）。
related:
- llm-wiki-query-phase
- llm-wiki-4-signal-relevance-model
- llm-wiki-local-api-agent-skill
---

LLM Wiki 将 Karpathy 原始设计中的简单查询（LLM 读取相关页面）扩展为多阶段检索管线：

**Phase 1 — Tokenized Search**：
- 英文：分词 + 停用词去除
- 中文：CJK bigram 分词
- 标题匹配加分（+10 score）
- 同时搜索 wiki/ 和 raw/sources/

**Phase 1.5 — Vector Semantic Search**（可选）：
- 通过任意 OpenAI 兼容的 /v1/embeddings 端点进行嵌入
- 存储于 LanceDB（Rust 后端），快速近似最近邻检索
- 余弦相似度发现无关键词重叠的语义相关页面
- 据材料数据，整体 recall 从 58.2% 提升至 71.4%

**Phase 2 — Graph Expansion**：
- 搜索结果的 top 页面作为种子节点
- 4-signal 相关性模型寻找关联页面
- 2-hop 遍历，带衰减以覆盖更深连接

**Phase 3 — Budget Control**：
- 可配置上下文窗口：4K → 1M tokens
- 比例分配：60% wiki 页面 / 20% 对话历史 / 5% index / 15% 系统提示

**Phase 4 — Context Assembly**：
- 编号页面（含完整内容而非摘要）
- 系统提示包含 purpose.md、语言规则、citation 格式、index.md
- LLM 按编号引用页面：[1], [2] 等 [^src-1] [^card-1] [^card-2]

[^src-1]: `data/raw/github_repo/repo-nashsu-llm-wiki/repo/README.md` -- "7. Optimized Query Retrieval Pipeline" P195-224 -- "Phase 1: Tokenized Search ... Phase 4: Context Assembly ... overall recall improved from 58.2% to 71.4% with vector search enabled"
[^card-1]: 参见 [[llm-wiki-4-signal-relevance-model]] 了解 Phase 2 使用的相关性模型
[^card-2]: 参见 [[llm-wiki-persistent-knowledge-compilation]] 了解为什么查询检索的是已编译的 wiki 而非原始文档
