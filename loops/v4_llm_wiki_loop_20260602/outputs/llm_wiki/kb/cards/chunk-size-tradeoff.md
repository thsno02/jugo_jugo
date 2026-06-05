---
id: chunk-size-tradeoff
title: 分块大小权衡
status: accepted
card_type: mechanism
tags: [rag, chunking, retrieval, tradeoff]
created_time: 2026-06-05T10:00:00+08:00
edited_time: 2026-06-05T10:00:00+08:00
edited_entity: llm
source_ids: [kunal-local-knowledge-base]
justification: ../justification/chunk-size-tradeoff.md
canonical_concept: chunk-size-tradeoff
aliases: [分块权衡, chunk size tradeoff, 分块粒度, chunking granularity, 分块大小]
summary: >-
  chunk-size-tradeoff（分块权衡 / chunk size tradeoff / 分块粒度）是 RAG 管线中文档分块大小（典型 256-512 token）的核心权衡：太小则丢失上下文，太大则检索噪声增大；朴素固定大小分块丢弃文档结构，语义分块和混合搜索是演进方向
related: [full-context-anti-rag, llm-wiki-mainstream-prerequisites, memory-value-granularity-tradeoff, memory-vs-rag-salience, relevant-vs-irrelevant-noise-sensitivity, source-granularity-effect]
---

在 RAG 管线的摄入阶段，文档被切分为块（chunk），典型大小为 256-512 token。分块大小是一个被教程低估的关键参数——"比大多数教程承认的更重要"[^src-1]：

- **太小**——丢失上下文。单个块无法承载理解一段论述所需的背景信息。
- **太大**——检索噪声增大。块中混入不相关内容，降低检索精度。

当前主流实现使用朴素的固定大小分块（naive fixed-size chunking），这种方式**丢弃了文档结构**——标题层级、段落边界、列表等结构信息在等长切割中消失[^src-2]。作者指出三种改进方向需要成为标准但目前仍处于"研究项目领域"：

1. **语义分块（semantic chunking）**——根据语义边界而非固定长度切分
2. **层次化索引（hierarchical indexing）**——保留文档的层级结构信息
3. **混合搜索（hybrid search）**——将向量相似度与 BM25 关键词匹配相结合[^src-3]

RAGChecker 的实验为这一权衡提供了量化证据：生成器对相关块中的噪声（NS-I）远比无关块噪声（NS-II）敏感，说明分块质量比分块数量更关键 [^card-1]。然而，全上下文方案的支持者认为分块本身就是根本缺陷——Karpathy LLM Wiki 直接拒绝分块检索，主张将完整知识图谱提供给长上下文模型[^dist-1]。Mem0 实验数据则从量化角度展示了 chunk size 对 RAG 性能的非单调效应：chunk=256 时 RAG 表现最佳但仍低于结构化记忆系统[^card-2]。wiki 编译场景中的实证发现进一步印证了语义切分的价值：相同模型和提示词下，章节级切分对整书处理产生了质的提升[^card-3]。对话记忆系统中的存储粒度权衡也反映了同一规律——轮次级分解优于会话级[^card-4]。

## Footnotes

[^src-1]: `data/raw/webpage/kunal-local-knowledge-base/text.txt` -- L72 -- "Chunk size matters more than most tutorials admit — too small and you lose context, too large and your retrieval gets noisy."
[^src-2]: `data/raw/webpage/kunal-local-knowledge-base/text.txt` -- L125 -- "Naive fixed-size chunking throws away document structure."
[^src-3]: `data/raw/webpage/kunal-local-knowledge-base/text.txt` -- L125-126 -- "Semantic chunking, hierarchical indexing, and hybrid search (combining vector similarity with BM25 keyword matching) need to become standard. Right now they're research-project territory for most setups."
[^card-1]: [相关噪声与无关噪声敏感度的区分](relevant-vs-irrelevant-noise-sensitivity.md) -- RAGChecker 量化了生成器的块级信任模式，相关块噪声远大于无关块噪声，为分块质量优先于分块数量提供实证
[^dist-1]: [全上下文反 RAG 架构选择](full-context-anti-rag.md) -- 本卡在 RAG 范式内优化分块粒度，该卡主张完全拒绝分块检索以保持跨知识图谱推理能力，区分点在于分块是可优化参数还是根本设计缺陷
[^card-2]: [记忆系统 vs RAG 的显著性优势](memory-vs-rag-salience.md) -- 本卡从理论角度分析分块大小权衡，该卡从 Mem0 实验量化了 chunk size 的非单调效应（chunk=256 最优但仍低于记忆系统），提供实证补充
[^card-3]: [源文件粒度效应](source-granularity-effect.md) -- 本卡讨论 RAG 管线中固定分块的缺陷和语义分块方向，该卡在 wiki 编译场景中实证验证了章节级语义切分对朴素整文件处理的压倒性优势
[^card-4]: [记忆存储粒度权衡](memory-value-granularity-tradeoff.md) -- 本卡在 RAG 管线探讨分块大小，该卡在对话记忆场景探讨存储粒度（会话/轮次/事实），共同论证检索单元粒度是跨领域的关键设计参数
