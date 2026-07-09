---
id: longmemeval-retrieval-augmentation
title: LongMemEval 检索增强与 Index Expansion 策略
status: draft
card_type: method
tags: [retrieval, index-expansion, time-aware, RAG, memory-retrieval]
created_time: 2026-06-12T19:00:00+08:00
edited_time: 2026-06-12T19:00:00+08:00
edited_entity: llm
source_ids: [repo-longmemeval]
evidence_basis: code_implementation
justification: ../justification/longmemeval-retrieval-augmentation.md
canonical_concept: longmemeval-retrieval-augmentation
aliases: [index expansion, time-aware query expansion, memory retrieval baselines]
summary: >-
  LongMemEval (longmemeval-retrieval-augmentation) 提供多种记忆检索基线
  (BM25, Contriever, Stella V5 1.5B, GTE-Qwen2-7B) 支持 turn/session 粒度.
  Index expansion 策略包括 session-summ, session-keyphrase, session-userfact,
  turn-keyphrase, turn-userfact; join mode 有 separate/merge/replace 三种.
  时间感知查询扩展 (time-aware query expansion) 从 session 提取带时间戳事件
  并从 query 推断时间范围以缩小检索空间.
related: [longmemeval-benchmark-overview, longmemeval-dataset-variants]
---

LongMemEval 提供了完整的记忆检索实验框架，包括基线检索、索引扩展和时间感知查询扩展三个层次。[^src-1]

**基线检索器**: 支持 `flat-bm25`（稀疏）、`flat-contriever`（稠密）、`flat-stella`（Stella V5 1.5B）和 `flat-gte`（GTE-Qwen2-7B-instruct）四种检索器，均支持 `turn` 或 `session` 两种索引粒度。稠密模型支持多 GPU 检索。[^src-1]

**Index Expansion**: 通过离线生成的扩展内容增强检索 key。扩展类型包括 `session-summ`（会话摘要）、`session-keyphrase`/`turn-keyphrase`（关键短语）、`session-userfact`/`turn-userfact`（用户事实）。三种 join mode 决定扩展如何与原始 key 结合：`separate`（新增键值对）、`merge`（合并）、`replace`（替换）。[^src-2]

**Time-Aware Query Expansion**: 从 session 中提取带时间戳的事件，从 query 推断时间范围，据此缩小检索空间。该方法与任意检索实验的输出兼容，在论文中以 session 粒度使用。[^src-3]

[^src-1]: data/raw/github_repo/repo-longmemeval/repo/README.md -- "Baseline Retrieval" P1 -- "RETRIEVER: flat-bm25, flat-contriever, flat-stella (Stella V5 1.5B), or flat-gte (gte-Qwen2-7B-instruct)"
[^src-2]: data/raw/github_repo/repo-longmemeval/repo/README.md -- "Index Expansion" P1 -- "EXPANSION_TYPE: we support session-summ, session-keyphrase, session-userfact, turn-keyphrase, turn-userfact"
[^src-3]: data/raw/github_repo/repo-longmemeval/repo/README.md -- "Time-Aware Query Expansion" P1 -- "pruning out the search space by extracting timestamped events from the sessions, inferring time range from the query, and using the range to narrow down the search space"

[^card-1]: longmemeval-benchmark-overview -- 基准整体定位
[^card-3]: longmemeval-dataset-variants -- 数据集变体与检索场景的关系
