---
schema: draft_card_provenance.v3
draft_card: ../cards/memgpt-nested-kv-multi-hop.md
material_id: arxiv-memgpt
digest_id: digest_arxiv-memgpt
source_paths:
  - data/raw/arxiv/arxiv-memgpt/agent_source_bundle.txt
created_time: 2026-05-26T11:40:00+08:00
edited_time: 2026-05-26T11:40:00+08:00
edited_entity: llm
---

## 源证据

- experiments 行 1511："We introduce a new task based on the synthetic Key-Value retrieval proposed in prior work. The goal of this task is to demonstrate how MemGPT can collate information from multiple data sources. ... We create a version of the KV task, nested KV retrieval, where values themselves may be keys, thus requiring the agent to perform a multi-hop lookup."
- experiments 行 1512：140 对 UUID、约 8k tokens、嵌套层数 0–4、30 个排序配置。
- experiments 行 1515：所有数值结果与失败模式。
- 图 caption 行 1475–1481："MemGPT is the only approach that is able to consistently complete the nested KV task beyond 2 nesting levels. While GPT-4 Turbo performs better as a baseline, MemGPT with GPT-4 Turbo performs worse than MemGPT with GPT-4."
- 图 caption 行 1495：嵌套 KV 解题示意，"831..ea5 → 5b8..4c3 → f37...617"；MemGPT 在最终查询只返回一个结果时停止——表明它通过结果数量判断终结条件。

## 卡片范围是否成立

本卡聚焦"嵌套 KV 这一基准 + 它揭示的洞见（上下文够不代表多跳能力够）"，独立成立。论文 §experiments 给出完整定义与结果。"外化成串行子查询"是把论文结果与 chaining 机制连起来的解释，仍是论文意图内的描述。

## 发表门控结果

本轮未运行。

## 备注

- 与 memgpt-function-chaining-heartbeat 互相印证：chaining 卡说"机制"，本卡说"验证"。
- 与 zep-dmr-benchmark-critique 主题相关（都谈 benchmark 设计），但视角不同：本卡是"嵌套 KV 揭示什么能力"，前者是"DMR 已失效"。
