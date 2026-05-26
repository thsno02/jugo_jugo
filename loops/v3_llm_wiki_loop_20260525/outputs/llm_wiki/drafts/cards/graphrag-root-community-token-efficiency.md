---
id: graphrag-root-community-token-efficiency
title: GraphRAG 根级社群摘要（C0）以 ~2% token 成本接近全局方法效果
status: draft
card_type: source_claim
tags: [#graphrag, #cost-efficiency, #context-window, #token-budget]
created_time: 2026-05-26T11:02:00+08:00
edited_time: 2026-05-26T11:02:00+08:00
edited_entity: llm
source_ids: [arxiv-graphrag]
provenance_card: ../provenance/graphrag-root-community-token-efficiency.md
aliases: ["C0 root summary", "GraphRAG cost tradeoff"]
related: [graphrag-leiden-community-hierarchy]
---

GraphRAG 论文里最直接落地的一个工程发现：当一个语料需要被**反复**用全局问题查询时，用**根级社群摘要（C0）**当索引，比把全部源文做 map-reduce 总结（TS 基线）便宜 9–43 倍，同时还保留对 vector RAG（SS 基线）72% / 62% 的 comprehensiveness / diversity 胜率。

**关键数字（来自 Table community summaries 与 Results §4.1）：**

| 数据集 | C0 单元数 | C0 tokens | TS tokens | C0 占 TS 比例 |
|---|---|---|---|---|
| Podcast | 34 | 26,657 | 1,014,611 | 2.6% |
| News | 55 | 39,770 | 1,707,694 | 2.3% |

也就是说，C0 用占源文 token 量 **~2%** 的索引就能驱动一次 map-reduce 全局问答。叶级 C3 占 66.8%–73.5%，相对 C0 多花 30 倍以上的 token 才换来 comprehensiveness 上"小但持续"的提升（Podcast intermediate-level 57%、News low-level 64% 的胜率，p<0.001）。

**为什么这点重要：**

- "iterative question answering that characterizes sensemaking activity" —— sensemaking 不是一次性查询，而是同一语料上的反复追问。指数式增长的 token 在 C3 上不划算。
- 对话式 / 看板式 LLM 应用里，把 C0 当默认上下文，C3 当"按需深挖"，正好对齐 root → drill-down 的人机交互模式。
- 论文 future work 段还提议把 embedding-based 局部匹配与 C0 摘要联用（"hybrid RAG schemes"，行 1027–1029），这是把成本进一步压低的下一步方向。

**边界与误用：**

- 这只在"全局意义建构"问题上成立。对事实型问题（directness 控制项），vector RAG 仍是最直接的；C0 反而可能漏掉具体引文（"empowerment" 评测里"specific examples, quotes, and citations" 是关键，C0 因为压缩太狠而被惩罚——见行 991–993）。
- 实验仅在两个 ~1M token 量级的语料上做过；论文 §5.1 自己提到 "More work is needed to understand how performance generalizes to datasets from various domains"。

## References

- `tab:community summaries`：`data/raw/arxiv/arxiv-graphrag/agent_source_bundle.txt` 行 438–446。
- 胜率与"9x-43x fewer tokens"叙述：行 434, 998–999。
- "iterative question answering that characterizes sensemaking activity" 与 C0 胜率：行 999。
- Empowerment 上对 specific examples / quotes 的发现：行 991–993。

## Footnotes

- "Map-reduce summarization of source texts is the most resource-intensive approach requiring the highest number of context tokens. Root-level community summaries (C0) require dramatically fewer tokens per query (9x-43x)."——行 434。
- "for low-level community summaries (C3), GraphRAG required 26-33% fewer context tokens, while for root-level community summaries (C0), it required over 97% fewer tokens." ——行 998。
- "For a modest drop in performance compared with other global methods, root-level GraphRAG offers a highly efficient method for the iterative question answering that characterizes sensemaking activity, while retaining advantages in comprehensiveness (72% win rate) and diversity (62% win rate) over vector RAG."——行 999。
