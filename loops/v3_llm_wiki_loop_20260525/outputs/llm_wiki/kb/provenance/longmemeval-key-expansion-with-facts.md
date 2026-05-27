---
schema: accepted_card_provenance.v3
card: ../cards/longmemeval-key-expansion-with-facts.md
material_id: arxiv-longmemeval
digest_id: digest_arxiv-longmemeval
source_paths:
  - data/raw/arxiv/arxiv-longmemeval/agent_source_bundle.txt
draft_card: ../../drafts/cards/longmemeval-key-expansion-with-facts.md
draft_provenance: ../../drafts/provenance/longmemeval-key-expansion-with-facts.md
similarity_result: ../../drafts/similarity/longmemeval-key-expansion-with-facts.json
comparison_provenance: ../../drafts/comparison/longmemeval-key-expansion-with-facts.md
gate:
  type: publication_gate
  result: passed
  decided_at: 2026-05-27T11:30:00+08:00
  gate_notes: 6/6 项通过；K=V+fact 实测表 + +9.4%/+5.4% 增益 + rank vs key merging 解释 + 边界齐备。
created_time: 2026-05-26T14:30:00+08:00
edited_time: 2026-05-27T11:30:00+08:00
edited_entity: llm
---

## 源证据

- 第 1043-1062 行：表 `tab:main-results-key` 完整七 key 设计 × round / session × Recall / NDCG / GPT-4o / L3.1-70B / L3.1-8B 数据。
- 第 1493-1497 行：§5.2 正文，强调"replace 反而下降，expansion 才有效"+9.4% / +5.4% 增益。
- 第 1320-1322 行（introduction itemize 第二条）：相同主张被预告。
- 第 1745-1751 行：appendix 解释 rank merging 反而劣于 key merging。
- 第 1004-1019 行：appendix 表 `tab:key-results-full-appendix` 用 BM25 / Contriever / Stella V5 三 retriever 对比。

## 卡片范围是否成立

- 表中所有数字与 +9.4% / +5.4% 的"平均"声明均直接来自论文。
- "rank merging 因 index 翻 m+1 倍而失效"是论文显式给出的解释，没有引申。
- "fact 抽取依赖好 LLM"是合理边界提示：论文用 Llama 3.1 8B Instruct，说明门槛不高，但若更弱模型抽 fact 漏 / 错则不能保证增益。

## 发表门控结果

- 类型：publication_gate
- 结果：passed
- 决定时间：2026-05-27T11:30:00+08:00
- 检查要点：
  - operational_rule 卡明确"不要 replace、要 expand"规则 + 实测表，非标题复述。
  - 知识密度合格。
  - source_ids 含 `arxiv-longmemeval`，正文锚到第 1043-1062 / 1493-1497 / 1745-1751 行。
  - 含 `## References` 与 `## Footnotes`。
  - frontmatter 字段完整。
  - related 已挂上 5 张相关卡。

## 备注

- 与 v2 `auto-index-replaces-rag-at-small-scale` 概念域不同；本卡更细，属于 RAG indexing 层面的具体优化。
- 与 LoCoMo observation-RAG 卡互补：LoCoMo 的 observation = "fact-only key" 思路，LongMemEval 进一步说明"再把原始 round 拼回去"才是更稳的方案。

## 相关 v3 draft 工件

- draft card: `../../drafts/cards/longmemeval-key-expansion-with-facts.md`
- draft provenance: `../../drafts/provenance/longmemeval-key-expansion-with-facts.md`
- similarity: `../../drafts/similarity/longmemeval-key-expansion-with-facts.json`
- comparison provenance: `../../drafts/comparison/longmemeval-key-expansion-with-facts.md`
