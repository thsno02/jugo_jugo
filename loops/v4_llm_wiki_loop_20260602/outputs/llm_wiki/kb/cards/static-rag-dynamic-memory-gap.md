---
id: static-rag-dynamic-memory-gap
title: 静态 RAG 与动态 agent 记忆的鸿沟
status: accepted
card_type: distinction
tags: [RAG, agent_memory, dynamic_knowledge, enterprise, limitation]
created_time: 2026-06-05T10:00:00+08:00
edited_time: 2026-06-05T10:00:00+08:00
edited_entity: llm
source_ids: [arxiv-zep]
justification: ../justification/static-rag-dynamic-memory-gap.md
canonical_concept: static-rag-dynamic-memory-gap
aliases: [静态RAG与动态记忆鸿沟, static RAG limitation, RAG静态语料局限]
summary: >-
  static-rag-dynamic-memory-gap（静态RAG与动态记忆鸿沟, static RAG limitation）当前 RAG 方法聚焦于广泛领域知识和静态语料（文档内容很少变化），而企业 agent 需要从持续对话和业务数据中动态集成知识，这种根本差距需要知识图谱等新方法来弥合
related: [bi-temporal-fact-model, full-context-anti-rag, memory-vs-rag-salience, temporal-knowledge-graph-three-tier]
---

Zep 论文提出了一个关于当前 RAG 方法的根本性批评：现有 RAG 聚焦于广泛领域知识和基本静态的语料库——即加入语料库的文档内容很少发生变化 [^src-1]。

然而企业级 agent 面临完全不同的需求：它们需要访问来自用户交互、相关业务数据和世界数据的持续演变的大规模数据语料。论文将赋予 agent 这种广泛而动态的"记忆"视为实现 agent 愿景的"关键构建模块"，并明确主张"当前 RAG 方法不适合这个未来"[^src-2]。

这一差距具体表现在：完整的对话历史、业务数据集和其他领域特定内容无法有效放入 LLM 上下文窗口 [^src-3]。因此需要新的方法来处理 agent 记忆——Zep 选择的方案是时序感知的知识图谱引擎，能够动态综合非结构化对话数据和结构化业务数据，同时维护历史关系 [^src-4]。Mem0 的实验数据从量化角度印证了这一论点：提取显著事实的记忆系统一致优于所有 RAG 配置[^card-1]。Karpathy LLM Wiki 从知识完整性角度同样拒绝 RAG——认为分块检索碎片化知识并破坏跨图谱推理能力，选择向 LLM 提供完整上下文[^card-2]。

## Footnotes

[^card-1]: [记忆系统 vs RAG 的显著性优势](memory-vs-rag-salience.md) -- Zep 从架构层面论证 RAG 的静态语料局限，Mem0 从 LOCOMO 基准实验数据量化证明结构化记忆（Judge 67-68%）优于 RAG（最高 61%）
[^card-2]: [全上下文反 RAG 架构选择](full-context-anti-rag.md) -- 本卡从动态性角度批评 RAG 的静态语料假设，该卡从知识完整性角度拒绝 RAG 的分块检索以保持跨图谱推理，两者从不同维度论证 RAG 的局限性

[^src-1]: `data/raw/arxiv/arxiv-zep/agent_source_bundle.txt` -- Section 1 (Introduction) -- "Current approaches using RAG have focused on broad domain knowledge and largely static corpora—that is, document contents added to a corpus seldom change."
[^src-2]: `data/raw/arxiv/arxiv-zep/agent_source_bundle.txt` -- Section 1 -- "We view empowering agents with this broad and dynamic 'memory' as a crucial building block to actualize this vision, and we argue that current RAG approaches are unsuitable for this future."
[^src-3]: `data/raw/arxiv/arxiv-zep/agent_source_bundle.txt` -- Section 1 -- "entire conversation histories, business datasets, and other domain-specific content cannot fit effectively inside LLM context windows"
[^src-4]: `data/raw/arxiv/arxiv-zep/agent_source_bundle.txt` -- Abstract -- "Zep addresses this fundamental limitation through its core component Graphiti—a temporally-aware knowledge graph engine that dynamically synthesizes both unstructured conversational data and structured business data while maintaining historical relationships."
