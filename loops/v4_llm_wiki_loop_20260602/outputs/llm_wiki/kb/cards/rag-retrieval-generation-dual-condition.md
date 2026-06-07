---
id: rag-retrieval-generation-dual-condition
title: RAG 攻击的检索与生成双条件
status: accepted
card_type: mechanism
tags: [rag, security, retrieval-condition, generation-condition, attack-design]
created_time: 2026-06-05T10:00:00+08:00
edited_time: 2026-06-05T10:00:00+08:00
edited_entity: llm
source_ids: [arxiv-poisonedrag]
justification: ../justification/rag-retrieval-generation-dual-condition.md
canonical_concept: rag-retrieval-generation-dual-condition
aliases: [检索条件与生成条件, retrieval condition and generation condition, RAG双条件攻击框架]
summary: >-
  rag-retrieval-generation-dual-condition（检索条件与生成条件 / retrieval and generation conditions）有效的 RAG 知识腐蚀攻击必须同时满足两个必要条件：检索条件（恶意文本被检索到）和生成条件（恶意文本作为上下文时 LLM 生成目标答案），现有基线方法只能满足其中一个条件因而效果不佳。
related: [poisonedrag-text-decomposition, rag-knowledge-database-attack-surface]
---

PoisonedRAG 论文的核心理论贡献是推导出有效 RAG 知识腐蚀攻击的两个**必要条件** [^src-1]：

**检索条件（Retrieval Condition）**：恶意文本 P 必须出现在目标问题 Q 的 top-k 检索结果中。这要求恶意文本与目标问题在嵌入空间中足够相似，即 Sim(f_Q(Q), f_T(P)) 必须足够大 [^src-2]。否则 P 无法进入 LLM 的上下文窗口，也就无法影响生成结果。

**生成条件（Generation Condition）**：当恶意文本 P 单独作为上下文时，LLM 应当为目标问题 Q 生成攻击者指定的目标答案 R。论文的洞察是：如果 P 单独作为上下文即可引导生成 R，那么当 P 与其他文本（恶意或干净文本）一起作为上下文时，LLM 更可能生成 R [^src-3]。

这两个条件在某些情况下可能冲突：如果恶意文本在语义上极度类似于目标问题（例如 P 就是 Q 本身），则检索条件满足但生成条件不满足 [^src-4]。现有基线方法的失败正是因为它们无法同时满足这两个条件：Naive Attack 和 Corpus Poisoning Attack 满足检索但不满足生成（ASR < 6%），GCG Attack 满足生成但不满足检索（F1-Score = 0.0），Prompt Injection Attack 部分满足两者但不如 PoisonedRAG 优化（ASR 62-93% vs 91-99%）[^src-5]。

## Footnotes

[^src-1]: `data/raw/arxiv/arxiv-poisonedrag/agent_source_bundle.txt` -- "method.tex" -- "Our major contribution is to derive two necessary conditions for an effective attack to RAG systems."
[^src-2]: `data/raw/arxiv/arxiv-poisonedrag/agent_source_bundle.txt` -- "method.tex" -- "the embedding vectors produced by a retriever for the malicious text P and the target question Q should be similar. We call this condition retrieval condition."
[^src-3]: `data/raw/arxiv/arxiv-poisonedrag/agent_source_bundle.txt` -- "method.tex" -- "the LLM should generate the target answer R when P alone is used as the context for the target question Q... We call this condition generation condition."
[^src-4]: `data/raw/arxiv/arxiv-poisonedrag/agent_source_bundle.txt` -- "method.tex" -- "if we craft the malicious text P such that it is extremely semantically similar to the target question Q... then we could achieve the retrieval condition but may not achieve the generation condition."
[^src-5]: `data/raw/arxiv/arxiv-poisonedrag/agent_source_bundle.txt` -- "evaluation.tex" -- "Existing baselines are not designed to simultaneously achieve retrieval and generation conditions, resulting in sub-optimal performance."
