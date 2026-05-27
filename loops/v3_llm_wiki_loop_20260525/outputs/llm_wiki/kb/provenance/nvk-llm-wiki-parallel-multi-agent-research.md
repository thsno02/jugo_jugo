---
schema: accepted_card_provenance.v3
card: ../cards/nvk-llm-wiki-parallel-multi-agent-research.md
material_id: llm-wiki-net
digest_id: digest_llm-wiki-net
source_paths:
  - data/raw/webpage/llm-wiki-net/text.txt
draft_card: ../../drafts/cards/nvk-llm-wiki-parallel-multi-agent-research.md
draft_provenance: ../../drafts/provenance/nvk-llm-wiki-parallel-multi-agent-research.md
similarity_result: ../../drafts/similarity/nvk-llm-wiki-parallel-multi-agent-research.json
comparison_provenance: ../../drafts/comparison/nvk-llm-wiki-parallel-multi-agent-research.md
gate:
  type: publication_gate
  result: passed
  decided_at: 2026-05-27T15:14:00+08:00
  gate_notes: 6/6 项通过；5/8/10 agent 与 thesis / retardmax 模式有 verbatim 行号源。
created_time: 2026-05-26T11:26:00+08:00
edited_time: 2026-05-27T15:14:00+08:00
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

卡片完整覆盖 `wiki:research` 的模式开关与多轮 / 多 path / thesis / retardmax 的语义，所有数字与短语都按原文引用。"why structure it as agent swarm + gap report" 段是设计动机分析，主要由源材料明文要素直接引申。

## 发表门控结果

- 类型：publication_gate
- 结果：passed
- 决定时间：2026-05-27T15:14:00+08:00
- 检查要点：
  - 四阶段 + 关键模式 + 设计动机 + 边界 4 节。
  - 知识密度高；非标题复述。
  - 源支撑：5+ 段 verbatim + 行号。
  - References + Footnotes 双在；Footnotes 4 条 verbatim。
  - frontmatter 完整；related 含 5 张邻接卡。

## 备注

- 与 `nvk-llm-wiki-hub-and-topic-wikis` 是结构 vs 流程的两面。

## 相关 v3 draft 工件

- draft card: `../../drafts/cards/nvk-llm-wiki-parallel-multi-agent-research.md`
- draft provenance: `../../drafts/provenance/nvk-llm-wiki-parallel-multi-agent-research.md`
- similarity: `../../drafts/similarity/nvk-llm-wiki-parallel-multi-agent-research.json`
- comparison provenance: `../../drafts/comparison/nvk-llm-wiki-parallel-multi-agent-research.md`
