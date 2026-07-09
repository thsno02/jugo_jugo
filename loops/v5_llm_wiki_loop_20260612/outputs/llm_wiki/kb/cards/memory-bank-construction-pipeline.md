---
id: memory-bank-construction-pipeline
title: LLM 记忆系统构建流水线形式化
status: accepted
card_type: formalization
tags:
- memory-pipeline
- segmentation
- summarization
- update
- memory-bank
created_time: 2026-06-12 16:00:00+08:00
edited_time: 2026-06-12 16:00:00+08:00
edited_entity: llm
source_ids:
- arxiv-lightmem
evidence_basis: experimental_paper
justification: ../justification/memory-bank-construction-pipeline.md
canonical_concept: memory-bank-construction-pipeline
aliases:
- memory bank construction
- 记忆库构建流水线
- memory system pipeline
- conventional memory systems
summary: 论文将主流 LLM 记忆系统形式化为两大阶段：(I) 记忆库构建——含三个子阶段：(a) 分割 D^(g) = f_seg(D; g)，g 可为 turn/session/topic 级别；(b) 摘要/提取 E = f_sum(D^(g))，生成记忆条目并存入向量库或知识图谱；(c) 更新 M' = f_update(M, R; U)，M 为现有记忆库、R 为新条目、U 为更新策略。(II)
  检索与使用——新查询到达时检索相关条目、拼接 prompt、调用模型生成回答。该形式化为对比不同记忆系统（NaiveRAG、A-MEM、Mem0、MemoryOS、LightMem）提供了统一描述框架。
related:
- memory-system-three-limitations
- lightmem-three-stage-architecture
---

论文 Section 2.1 "Conventional Memory Systems for LLMs" 将主流记忆架构形式化为统一的两阶段流水线：

**阶段 I：记忆库构建（Memory Bank Construction）**

(a) **分割（Segment）**：原始数据 D 按选定粒度处理
- D^(g) = f_seg(D; g)，对话场景中 g in {turn, session, topic}

(b) **摘要/提取（Summary/Extract）**：分割后数据生成记忆条目
- E = f_sum(D^(g))
- 存入结构化后端（向量数据库/知识图谱）

(c) **更新（Update）**：缓解上下文冲突或过时信息
- M' = f_update(M, R; U)
- M: 现有记忆库, R: 新条目, U: 更新/遗忘策略

**阶段 II：检索与使用（Retrieval and Usage）**
- 新查询 → f_retrieve() 检索相关条目 → 拼接 prompt → f_chat() 生成回答

该框架的价值在于提供了跨系统对比的统一描述语言——NaiveRAG 仅有 (a)+(b)，传统记忆系统有 (a)+(b)+(c) 且全在线，LightMem 将 (c) 移至离线。[^src-1]

[^src-1]: `data/raw/arxiv/arxiv-lightmem/agent_source_bundle.txt` -- "Preliminary: Conventional Memory Systems for LLMs" P879-886 -- "Raw data D are first processed at a chosen level of granularity... summarized or extracted to generate memory entries... updating mechanism to mitigate issues"
