---
id: longmemeval-key-expansion-with-facts
title: K = V + fact 比裸 value 平均 +9.4% recall、+5.4% QA 准确率
status: accepted
card_type: operational_rule
tags: [#rag, #indexing, #key-design]
created_time: 2026-05-26T14:30:00+08:00
edited_time: 2026-05-28T10:40:00+08:00
edited_entity: llm
source_ids: [arxiv-longmemeval]
provenance_card: ../provenance/longmemeval-key-expansion-with-facts.md
aliases: [document expansion, multi-key indexing, fact-augmented key]
related: [longmemeval-three-stage-memory-framework, locomo-observation-rag-beats-summary-rag, longmemeval-time-aware-query-expansion, longmemeval-chain-of-note-and-json-reading, zep-hybrid-search-rerank]
---

## 规则

LongMemEval §5.2 系统比较了七种 key 设计[^src1]，确定一条工程优化原则——这是 LongMemEval 三阶段框架中 CP2 Key 的最优落点[^v3-1]：

- **不要只用 value 自身做 key**，也**不要只用 fact / summary / keyphrase 替换 value 做 key**（替换会丢上下文，recall 反而掉）。
- **正确做法**：indexing 时把抽出的 user fact 与原 value 拼接成新的 key（"document expansion"）。这条做法称为 **K = V + fact**。

实测在 LongMemEval-M（500 session）上：

| Value 粒度 | Key 设计 | Recall@10 | GPT-4o Top-10 QA |
|---|---|---|---|
| round | K = V | 0.692 | 0.670 |
| round | K = fact only | 0.654 | 0.664 |
| round | **K = V + fact** | **0.784** | **0.720** |
| session | K = V | 0.783 | 0.676 |
| session | **K = V + fact** | **0.862** | **0.700** |

平均：跨所有模型 recall@k 提升 +9.4%，最终 QA 准确率提升 +5.4%[^src2]。

## 为什么有效

- "value 自身"已经能利用 retriever 处理长文本语义的能力，但单一向量必然平均化；额外把 user fact 拼进 key，等于**多给一条匹配路径**——同一个 round 在向量空间被它本身 + 它包含的 fact 同时表达。
- 替换式（K = fact only）则丢掉了原始上下文里其他可能匹配的语义信号，因此 recall 反而比 K = V 还差[^src3]。
- 论文还试过另一种"多路径"策略：rank merging（fact 单独建索引，检索后按 rank 融合）——结果显著差于 key merging，因为 rank merging 把索引规模翻 m+1 倍，反而稀释 top-k[^src4]。
- 这条规则与 LoCoMo "observation 优于 summary" 在直觉上同向：在 key 侧增维优于在 chunk 侧替换[^v3-2]；Zep 的 hybrid search + rerank 是同一思想的另一种实现路径[^v3-3]。

## 边界

- "fact 拼上去"的前提是有足够好的 LLM 抽取 user fact——论文用 Llama 3.1 8B Instruct 抽，已经能 work。但 fact 抽取若漏掉关键事实，扩写过的 key 不会比裸 value 好。
- 当用 BM25 等稀疏检索器时，fact 扩写依然有用（论文 appendix 验证），但增益小于 dense retriever。
- summary / keyphrase 扩写在某些场景能涨点（如 Contriever + session-level value 的 Recall@5），但不如 fact 稳定，因此论文推荐 fact 作 default。

## Footnotes

[^src1]: `data/raw/arxiv/arxiv-longmemeval/agent_source_bundle.txt` — 第 1043-1062 行（表 `tab:main-results-key`）— 七种 key 设计实验。
[^src2]: `data/raw/arxiv/arxiv-longmemeval/agent_source_bundle.txt` — 第 1321 行 + 第 1497 行 — "This approach, particularly when using user facts, yielded an average improvement of 9.4\% in recall@$k$ and 5.4\% in final accuracy across all models."
[^src3]: `data/raw/arxiv/arxiv-longmemeval/agent_source_bundle.txt` — 第 1494 行 — "despite their more focused semantics, using these condensed forms alone does not enhance the memory recall performance. We hypothesize that this is due to the retriever's ability to already effectively handle long-text semantics."
[^src4]: `data/raw/arxiv/arxiv-longmemeval/agent_source_bundle.txt` — 第 1747-1751 行 + 第 1245-1263 行（表 `tab:rank-merging-eval`）— "rank merging increases the index size by $m+1$ times, where $m$ is the number of information pieces extracted from each (key, value) pair. By comparison, key merging highlights the important information while avoiding explording the size of the index."
[^v3-1]: [longmemeval-three-stage-memory-framework](longmemeval-three-stage-memory-framework.md) — K = V + fact 是 CP2 的最优落点。
[^v3-2]: [locomo-observation-rag-beats-summary-rag](locomo-observation-rag-beats-summary-rag.md) — LoCoMo 在 chunk 侧的"提精度"实验。
[^v3-3]: [zep-hybrid-search-rerank](zep-hybrid-search-rerank.md) — Zep 用 hybrid + rerank 增加召回精度的另一路径。
