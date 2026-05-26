---
schema: draft_card_provenance.v3
draft_card: ../cards/nvk-llm-wiki-parallel-multi-agent-research.md
material_id: llm-wiki-net
digest_id: digest_llm-wiki-net
source_paths:
  - data/raw/webpage/llm-wiki-net/text.txt
created_time: 2026-05-26T11:26:00+08:00
edited_time: 2026-05-26T11:26:00+08:00
edited_entity: llm
---

## 源证据

- 四阶段流程描述（行 276–296）：
  > "Stage 1: Ask a question or pick a topic ... llm-wiki auto-detects whether you're asking a question or naming a topic."
  > "Stage 2: Agents search in parallel ... 5 agents (8 with --deep , 10 with --retardmax )"
  > "Stage 3: Sources are ingested and compiled ... Top sources are saved to raw/ (immutable — never modified after ingestion). Then the compilation pass synthesizes them into wiki articles under wiki/concepts/ , wiki/topics/ , and wiki/references/"
  > "Stage 4: Gap report and follow-up"
- 命令行选项汇总（行 214）：
  > "/wiki:research <topic> 5 parallel agents. --plan (multi-path), --deep (8), --retardmax (10), --new-topic , --min-time 1h ."
- thesis 模式（行 471–478）。
- retardmax（行 466–470）。
- `--plan` 段（行 350–366）：
  > "all paths launch simultaneously. Each path runs its own 5-agent swarm. Sources are ingested in parallel (each path writes unique files), then a single compilation pass sees all sources at once for cross-path synthesis."
- fuzzy router（行 176、行 119）。

## 卡片范围是否成立

卡片完整覆盖 `wiki:research` 的模式开关与多轮 / 多 path / thesis / retardmax 的语义，所有数字与短语（5/8/10、`act first, think later`、`focuses harder on the weaker side`）都按原文引用。"why structure it as agent swarm + gap report" 段是设计动机分析，主要由源材料的"--min-time 1h"、"multiple plan-dispatch-compile cycles"、"counter-weight against confirmation bias"等明文要素直接引申，未越界。

## 发表门控结果

本轮未运行。

## 备注

- 与 `nvk-llm-wiki-hub-and-topic-wikis` 是结构 vs 流程的两面；可在比较阶段评估是否合并为"nvk/llm-wiki 工具概览"大卡。
