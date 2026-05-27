---
schema: accepted_card_provenance.v3
card: ../cards/memgpt-function-chaining-heartbeat.md
material_id: arxiv-memgpt
digest_id: digest_arxiv-memgpt
source_paths:
  - data/raw/arxiv/arxiv-memgpt/agent_source_bundle.txt
draft_card: ../../drafts/cards/memgpt-function-chaining-heartbeat.md
draft_provenance: ../../drafts/provenance/memgpt-function-chaining-heartbeat.md
similarity_result: ../../drafts/similarity/memgpt-function-chaining-heartbeat.json
comparison_provenance: ../../drafts/comparison/memgpt-function-chaining-heartbeat.md
gate:
  type: publication_gate
  result: passed
  decided_at: 2026-05-27T14:34:00+08:00
  gate_notes: 6/6 项通过；机制描述准确，heartbeat 与 yield 二分清晰。
created_time: 2026-05-26T11:35:00+08:00
edited_time: 2026-05-27T14:34:00+08:00
edited_entity: llm
---

## 源证据

- intro 图 caption（行 1625）："The LLM can request immediate follow-up LLM inference to chain function calls together by generating a special keyword argument (request_heartbeat=true) in its output; function chaining is what allows MemGPT to perform multi-step retrieval to answer user queries."
- method 行 1679："events are generalized inputs to MemGPT and can consist of user messages (in chat applications), system messages (e.g. main context capacity warnings), user interactions (e.g. an alert that a user just logged in, or an alert that they finished uploading a document), and timed events that are run on a regular schedule (allowing MemGPT to run 'unprompted' without user intervention)."
- method 行 1682–1686：function chaining 的完整描述，包括 yield 默认与 heartbeat flag 行为。
- experiments 行 1515：GPT-3.5 在嵌套 KV 任务上"主要失败模式是直接返回原值"，间接证明 chaining 对函数调用可靠性的依赖。

## 卡片范围是否成立

本卡只覆盖"function chaining + request_heartbeat 这一控制流机制"，与内存层卡、驱逐策略卡正交。所有 heartbeat 行为来自原文逐字，"events 是唯一触发源"也是原文。"实际部署需加步数预算"是工程性边界提示，非论文断言；保留作为 boundary 标注。

## 发表门控结果

- 类型：publication_gate
- 结果：passed
- 决定时间：2026-05-27T14:34:00+08:00
- 检查要点：
  - 标题已是机制描述，正文进一步分解 events / yield / heartbeat。
  - 价值、操作含义、边界三部分给出 substantive 引申。
  - source_ids 指向 arxiv-memgpt；正文 + Footnotes 都带行号 verbatim。
  - References 与 Footnotes 双在。
  - frontmatter 完整；related 含 4 张同系列 MemGPT 卡 + 1 张 langgraph 邻接卡。

## 备注

- 与 memgpt-nested-kv-multi-hop 有联系：嵌套 KV 实验是 chaining 的最佳验证用例。
- adoption 阶段无修订。

## 相关 v3 draft 工件

- draft card: `../../drafts/cards/memgpt-function-chaining-heartbeat.md`
- draft provenance: `../../drafts/provenance/memgpt-function-chaining-heartbeat.md`
- similarity: `../../drafts/similarity/memgpt-function-chaining-heartbeat.json`
- comparison provenance: `../../drafts/comparison/memgpt-function-chaining-heartbeat.md`
