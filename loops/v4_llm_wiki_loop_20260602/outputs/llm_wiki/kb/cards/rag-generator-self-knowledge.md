---
id: rag-generator-self-knowledge
title: RAG 生成器的自有知识指标
status: accepted
card_type: concept
tags: [rag, self-knowledge, generator, hallucination, faithfulness]
created_time: 2026-06-05T10:00:00+08:00
edited_time: 2026-06-05T10:00:00+08:00
edited_entity: llm
source_ids: [arxiv-ragchecker]
justification: ../justification/rag-generator-self-knowledge.md
canonical_concept: rag-generator-self-knowledge
aliases: [RAG自有知识, generator self-knowledge, 生成器内部知识, 非上下文正确声明]
summary: >-
  rag-generator-self-knowledge（RAG自有知识 / generator self-knowledge / 非上下文正确声明）RAGChecker 定义的生成器指标：回答中正确但不被任何检索块蕴含的声明比例，反映生成器依赖自身参数化知识而非检索上下文的程度；在 RAG 场景中该值越低越好，因为 RAG 期望生成器完全依赖检索上下文
related: [ragchecker-three-tier-metrics, retrieval-improvement-faithfulness-noise-tradeoff, closed-book-citation-paradox]
---

RAGChecker 定义 self-knowledge（自有知识）为生成器回答中那些正确（与标准答案一致）但不被任何检索到的文本块蕴含的声明所占的比例[^src-1]。这些声明只能来自生成器 LLM 自身的参数化知识，而非从检索上下文中获取。

在 RAG 系统的设计期望中，生成器应完全依赖检索到的上下文来回答问题，因此 self-knowledge 越低越好[^src-1]。该指标与 hallucination 形成对称关系：hallucination 是不正确且不来自检索块的声明，self-knowledge 是正确但不来自检索块的声明——二者都反映了生成器脱离检索上下文的程度。

实验数据显示：（1）GPT-4 的 self-knowledge 明显高于开源模型（BM25 配对时 GPT-4=3.4 vs Llama3-70B=1.7），说明 GPT-4 更倾向于使用自身知识补充回答；（2）当检索质量提升（BM25->E5-Mistral），所有生成器的 self-knowledge 均下降（GPT-4: 3.4->1.4），说明生成器在检索上下文更丰富时更愿意依赖上下文[^src-2]。

这一指标在定义上与"正面的幻觉"相似——生成器产出了正确信息但来源不可追溯到检索上下文。在需要可溯源性的 RAG 应用（如医学、法律）中，高 self-knowledge 即便不降低准确性也构成可信度风险。

## Footnotes

[^src-1]: `data/raw/arxiv/arxiv-ragchecker/agent_source_bundle.txt` -- "sections/framework.tex, Generator Metrics" -- "A correct claim not entailed by any chunk can only be based on generator's self-knowledge... A lower self-knowledge score is better, when the generator is expected to fully depend on retrieved context only in a RAG system"
[^src-2]: `data/raw/arxiv/arxiv-ragchecker/agent_source_bundle.txt` -- "tables/ragchecker_results_avg.tex" -- "BM25_GPT-4 SK=3.4, E5-Mistral_GPT-4 SK=1.4; BM25_Llama3-70b SK=1.7, E5-Mistral_Llama3-70b SK=0.8"
[^card-closed-book-citation-paradox]: [闭卷-引用悖论](closed-book-citation-paradox.md) -- ALCE 实验定性揭示了 self-knowledge 现象的极端形态：ClosedBook 模式完全依赖参数化知识，正确性更高但引用 recall 骤降。本卡的 self-knowledge 指标是对该现象的量化操作化——将"正确但不可追溯"从二元判断变为连续度量
