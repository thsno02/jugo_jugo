---
id: rag-evaluation-tri-dimension
title: RAG 评估三维度分解
status: accepted
card_type: distinction
tags: [rag, evaluation, retrieval-quality, faithfulness, generation-quality, evaluation-dimensions]
created_time: 2026-06-05T10:00:00+08:00
edited_time: 2026-06-05T10:00:00+08:00
edited_entity: llm
source_ids: [arxiv-ragas]
justification: ../justification/rag-evaluation-tri-dimension.md
canonical_concept: rag-evaluation-tri-dimension
aliases: [RAG评估三维度, RAG evaluation dimensions, 检索-忠实性-生成质量三维度]
summary: >-
  rag-evaluation-tri-dimension（RAG评估三维度 / RAG evaluation dimensions / 检索-忠实性-生成质量三维度）RAGAS 将 RAG 管道评估分解为三个独立维度：检索系统识别相关且聚焦的上下文段落的能力、LLM 忠实利用上下文的能力、生成输出本身的质量。
related: [citation-quality-tri-dimension, rag-component-evaluation-tri-dimension, rag-retrieval-generation-dual-condition, ragas-reference-free-rag-evaluation, ragchecker-three-tier-metrics, retrieval-snr-tradeoff]
---

RAGAS 框架将 RAG 管道的评估挑战分解为三个独立维度，论文指出"评估 RAG 架构是具有挑战性的，因为有多个维度需要考虑" [^src-1]：

**维度一：检索质量（Context Relevance）**——"检索系统识别相关且聚焦的上下文段落的能力" [^src-2]。注意论文同时强调了"相关（relevant）"和"聚焦（focused）"两个属性，暗示检索不仅要召回相关内容，还要避免返回过于宽泛或噪声过多的段落。这与检索信噪比（SNR）的权衡直接相关。

**维度二：忠实性（Faithfulness）**——"LLM 忠实利用这些段落的能力" [^src-3]。这一维度衡量的是生成模型是否真正基于检索到的上下文来回答问题，而非依赖自身参数化知识或产生幻觉。忠实性（faithfulness）是 RAG 区别于纯 LLM 生成的关键评估维度。

**维度三：生成质量（Answer Quality）**——"生成本身的质量" [^src-4]。这一维度关注最终回答的整体可用性，独立于检索和忠实性之外。

三维分解的价值在于：它揭示了 RAG 管道的故障可能独立发生在不同组件上——检索可能召回了正确内容但 LLM 未能忠实使用，或 LLM 忠实使用了检索内容但检索本身返回了不相关的段落。单一维度的评估无法区分这些不同的失败模式。值得强调的是，这三个维度均在 RAGAS 的无参考框架下实现，无需 ground truth 答案即可评估[^card-3]。

ARES 独立提出了高度平行的三维组件评估框架（上下文相关性、回答忠实性、回答相关性），为这一分解的普遍性提供了跨研究验证[^card-1]。RAGChecker 则进一步将三维度扩展为三层级（整体/检索器/生成器），在生成器层引入 6 个细粒度诊断指标，将维度分析推向更深层次[^card-2]。

## Footnotes

[^card-1]: [RAG 组件评估三维度](rag-component-evaluation-tri-dimension.md) -- ARES 从不同来源独立提出了平行的三维组件评估（上下文相关性、回答忠实性、回答相关性），与 RAGAS 的三维度高度重叠
[^card-2]: [RAGChecker 三层诊断指标体系](ragchecker-three-tier-metrics.md) -- RAGChecker 将三维度扩展为三层级诊断体系，在生成器层引入 6 个细粒度指标，深化了维度分析的粒度
[^card-3]: [RAGAS 无参考评估框架](ragas-reference-free-rag-evaluation.md) -- 本卡描述三维度的内容（WHAT），该卡强调这些维度的评估无需依赖 ground truth（WHY/HOW）
[^card-4]: [引用评估三维度框架](citation-quality-tri-dimension.md) -- ALCE 从端到端输出质量角度分解为流畅度/正确性/引用质量三维度，与 RAGAS 的管道组件视角（检索/忠实性/生成）互补；共享"正交维度联合防止走捷径"的设计哲学

[^src-1]: `data/raw/arxiv/arxiv-ragas/agent_source_bundle.txt` -- Abstract L37 -- "Evaluating RAG architectures is, however, challenging because there are several dimensions to consider"
[^src-2]: `data/raw/arxiv/arxiv-ragas/agent_source_bundle.txt` -- Abstract L37 -- "the ability of the retrieval system to identify relevant and focused context passages"
[^src-3]: `data/raw/arxiv/arxiv-ragas/agent_source_bundle.txt` -- Abstract L37 -- "the ability of the LLM to exploit such passages in a faithful way"
[^src-4]: `data/raw/arxiv/arxiv-ragas/agent_source_bundle.txt` -- Abstract L37 -- "the quality of the generation itself"
