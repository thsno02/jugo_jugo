---
id: graphrag-self-reflection-gleaning
title: GraphRAG 用 "self-reflection gleaning" 抵消大 chunk 的实体召回损失
status: accepted
card_type: operational_rule
tags: [#graphrag, #entity-extraction, #prompt-engineering, #self-reflection]
created_time: 2026-05-26T15:00:00+08:00
edited_time: 2026-05-28T11:25:00+08:00
edited_entity: llm
source_ids: [arxiv-graphrag]
provenance_card: ../provenance/graphrag-self-reflection-gleaning.md
aliases: ["graph extraction gleaning", "GraphRAG chunk size"]
related: [graphrag-global-sensemaking-pipeline, graphrag-leiden-community-hierarchy, graphrag-context-window-8k-optimal, mem0-extract-update-pipeline, karpathy-wiki-extraction-granularity, wikibase-item-property-snak-statement]
---

GraphRAG 索引阶段最敏感的工程参数是 chunk 大小：chunk 越大越省 LLM 调用，但 LLM 容易"漏抽实体"。论文用一个**多轮自我反思（self-reflection）"gleaning" 循环**把"大 chunk 省 token"和"小 chunk 高召回"两边的优势都拿到，是 GraphRAG 之所以能稳定生产知识图的关键 trick。

**问题数据**：在 HotPotQA 上用 `gpt-4-turbo` 抽实体，chunk 大小对实体引用数的影响是 **2× 量级**：

| chunk size | 0 轮 reflection | 1 轮 | 2 轮 | 3 轮 |
|---|---|---|---|---|
| 600 token | 9,348 | 15,976 | 19,491 | **27,240** |
| 1200 token | 7,119 | 12,877 | 17,794 | 22,399 |
| 2400 token | 5,761 | 10,606 | 14,897 | 19,433 |

即同一 chunk size 下，3 轮 reflection 能把实体召回提升到约 **3 倍**；2400 token chunk 加 3 轮后仍可逼近 600 token 0 轮的 2 倍。

**gleaning 循环的实现细节（论文 §App E.2）**：

1. 第一次抽完后，把已抽实体回喂给 LLM，问"还有没有遗漏的实体？"——这一步用 **logit bias = 100** 强迫输出 yes/no 二选一；
2. 若 yes，再追加一句 prompt：`"MANY entities were missed in the last extraction"`，刺激 LLM 把漏掉的找出来；
3. 重复直到 LLM 回答 no 或达到设定的最大迭代数。

**为何要 logit bias = 100**：让 LLM 不能给出"可能漏了几个但我不确定"的模糊回答，避免回避问题。强制二元决策才能真正进入下一轮 gleaning。

**操作含义**：

- 与其纠结"chunk size 应该是多少"，不如**先把 chunk 设大（如 2400 token）拿到 token 节省，再用 2-3 轮 gleaning 把召回补回来**。论文给出的优化空间是"自由调 chunk size + 用 gleaning 补 recall"。
- gleaning 是"在同一个 chunk 内"的多次 LLM 调用，与 community summary 阶段的 map-reduce 完全独立——这两个机制各自负责"抽得全"和"聚得对"。

**边界与误用**：

- 这一招对 *实体召回* 有效，对 *关系召回* 提升不一定线性——论文只报告了 entity reference 数。
- 用更弱的模型（非 GPT-4 系）做 gleaning 时，logit bias 强制 yes 容易引入幻觉式的"补充实体"。论文用的是 `gpt-4-turbo`。
- gleaning 增加的是 LLM 调用次数（每个 chunk 多 3 次），与"大 chunk 省 LLM 调用"的初衷存在权衡——只有当 chunk size 提升带来的节省 > 3 次额外 gleaning 调用时才划算。

## References

- §App A.2 Self-Reflection 与 chunk size / gleaning 的论述：`data/raw/arxiv/arxiv-graphrag/agent_source_bundle.txt` 行 60–77。
- Chunk size 与实体引用数的实验图 `fig:chunkentities` 数据：行 1441–1487。
- 论文正文对 chunk size tradeoff 的描述：行 769–774（"longer text chunks require fewer LLM calls ... but suffer from degraded recall"）。

## Footnotes

- "we first ask the LLM to assess whether all entities were extracted, using a logit bias of 100 to force a yes/no decision"——行 72。
- "If the LLM responds that entities were missed, then a continuation indicating that 'MANY entities were missed in the last extraction' encourages the LLM to detect these missing entities."——行 73。
- "This approach allows us to use larger chunk sizes without a drop in quality (\autoref{fig:chunkentities}) or the forced introduction of noise."——行 74。
- HotPotQA 上 GPT-4 在 600 / 2400 chunk 的实体数差距："GPT-4 extracted almost twice as many entity references when the chunk size was 600 tokens than when it was 2400."——行 69。
