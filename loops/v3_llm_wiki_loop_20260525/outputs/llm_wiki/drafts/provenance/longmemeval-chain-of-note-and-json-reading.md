---
schema: draft_card_provenance.v3
draft_card: ../cards/longmemeval-chain-of-note-and-json-reading.md
material_id: arxiv-longmemeval
digest_id: digest_arxiv-longmemeval
source_paths:
  - data/raw/arxiv/arxiv-longmemeval/agent_source_bundle.txt
created_time: 2026-05-26T14:35:00+08:00
edited_time: 2026-05-26T14:35:00+08:00
edited_entity: llm
---

## 源证据

- 第 1517-1521 行（§5.4 reading 结果正文）："First, we present retrieved items in a structured JSON format ... Additionally, we apply the Chain-of-Note (CoN) reading approach ... This effectively decomposes long-context reading into two simpler subtasks: copying important details and reasoning with more concise notes."
- 第 1526-1533 行：图 `fig:main-fig-reading-design` 报告"CoN+JSON 优于其他三组参数组合"。
- 第 1700-1714 行：CoN 与 non-CoN prompt 完整文本（appendix）。
- 第 178-203 行（pilot 表）：long-context LLM 在 LongMemEval-S 上 30-66% accuracy drop，"With Chain-of-Note"列与"No Chain-of-Note"列对比。
- 第 1768 行（error analysis 图）：correct retrieval / wrong generation 占 error 的 40-50%。

## 卡片范围是否成立

- "10 分增益"、"CoN 与 JSON 必须合用"、"reader 错占 40-50%"均直接引用论文数字与原文。
- "弱 reader 也能受益"基于附录 oracle 表 + LongMemEval-S 表的对比，未跨文献综合。
- 边界提到"800 token 上限"出自 appendix 第 1691 行 "set the maximum generation length to 800 tokens"。

## 发表门控结果

本轮未运行。

## 备注

- 与 CoN 原始论文（Yu et al. 2023）有概念引用关系，但本卡只描述 LongMemEval 内的实验结论，未越界引述 CoN 原文。
