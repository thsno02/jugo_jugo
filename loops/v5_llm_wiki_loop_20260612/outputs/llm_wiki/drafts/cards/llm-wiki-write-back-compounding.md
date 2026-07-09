---
id: llm-wiki-write-back-compounding
title: LLM Wiki write-back 复合增长机制
status: draft
card_type: mechanism
tags: [write-back, knowledge-compounding, llm-wiki, claude-code]
created_time: 2026-06-12T19:00:00+08:00
edited_time: 2026-06-12T19:00:00+08:00
edited_entity: llm
source_ids: [pypi-my-llm-wiki]
evidence_basis: documentation
justification: ../justification/llm-wiki-write-back-compounding.md
canonical_concept: llm-wiki-write-back-compounding
aliases: [write-back, llm-wiki note, knowledge compounding, wiki write-back]
summary: >-
  my-llm-wiki 的 write-back 机制通过 llm-wiki note "<insight>" 命令从 Claude Code sessions 将洞察写回知识图谱，实现 graph compounds over time 的复合增长。这体现 Karpathy 将 wiki 视为 persistent compounding artifact 的设计意图——知识随使用而积累，而非每次查询重新推导。
related: []
---

my-llm-wiki 提供 write-back 机制，允许从 Claude Code sessions 将新洞察写回知识图谱 [^src-1] [^card-1]：

```
llm-wiki note "<insight>"
```

该命令使知识图谱随时间复合增长（"the graph compounds over time"），体现了 Karpathy 将 wiki 定位为"persistent, compounding artifact"的核心设计意图 [^src-2] [^card-2]——知识不是每次查询时重新推导，而是在每次使用中持续积累。

结合 SHA256 cache（重跑跳过未修改文件）的增量更新策略，write-back 使得知识图谱成为一个活的（living）、持续演化的系统。

[^src-1]: `data/raw/pypi/pypi-my-llm-wiki/text.txt` -- "Project description" P104 -- "llm-wiki note \"<insight>\" writes back from your Claude Code sessions so the graph compounds over time"
[^src-2]: `data/raw/pypi/pypi-my-llm-wiki/text.txt` -- "Project description" P100 -- "persistent, compounding artifact"
[^card-1]: my-llm-wiki-tool-overview
[^card-2]: karpathy-llm-wiki-three-layer-architecture
