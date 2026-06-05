---
id: wiki-write-back-mechanism
title: Wiki 回写机制
status: accepted
card_type: mechanism
tags: [llm-wiki, write-back, compounding, cli, bidirectional]
created_time: 2026-06-05T10:00:00+08:00
edited_time: 2026-06-05T10:00:00+08:00
edited_entity: llm
source_ids: [pypi-my-llm-wiki]
justification: ../justification/wiki-write-back-mechanism.md
canonical_concept: wiki-write-back-mechanism
aliases: [Wiki回写, write-back, llm-wiki note命令]
summary: >-
  wiki-write-back-mechanism（Wiki回写 / write-back / llm-wiki note命令）是使 LLM Wiki
  从只读编译产物变为持续增长的复利制品的关键机制：通过 llm-wiki note "<insight>" 命令，
  LLM 会话中产生的洞察可反向写入知识图谱，实现双向流动
related:
  - wiki-compounding-artifact
  - my-llm-wiki-implementation
  - query-and-answer-filing
  - output-compounding-loop
---

Wiki 回写机制是使知识图谱从单向编译产物升级为双向复利系统的关键能力。在 my-llm-wiki 中，这一机制通过 `llm-wiki note "<insight>"` CLI 命令实现：用户在 Claude Code 会话中产生的洞察可通过该命令写回知识图谱，使图谱随时间持续增长而非停留在初始编译状态[^src-1]。

这一机制的意义在于闭合了知识循环：
- **正向流**：原始文件 -> wiki 编译 -> LLM 查询（已被三层架构覆盖）
- **反向流**：LLM 会话洞察 -> `llm-wiki note` -> 知识图谱更新（回写机制补充的环节）

没有回写机制，wiki 只是原始文件的一次性编译快照；有了回写，wiki 成为 Karpathy 所说的"persistent, compounding artifact"[^src-2]。这与 Karpathy 原始设计中 answer filing（将问答结果归档回 wiki）的理念一致，但 my-llm-wiki 将其简化为单条 CLI 命令的交互形式。

## Footnotes

[^src-1]: `/Users/lw/Desktop/GitHub/llm_wiki/jugo_jugo/data/raw/pypi/pypi-my-llm-wiki/text.txt` -- L104 -- "llm-wiki note \"<insight>\" writes back from your Claude Code sessions so the graph compounds over time."
[^src-2]: `/Users/lw/Desktop/GitHub/llm_wiki/jugo_jugo/data/raw/pypi/pypi-my-llm-wiki/text.txt` -- L100 -- "let the wiki grow with every session as a \"persistent, compounding artifact\" rather than re-deriving knowledge on every query."
