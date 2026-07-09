---
id: human-llm-cognitive-division
title: 人机认知分工：策展与思考 vs 簿记与维护
status: accepted
card_type: design_principle
tags:
- llm-wiki
- human-llm-collaboration
- cognitive-division
- knowledge-maintenance
created_time: 2026-06-12 15:05:00+08:00
edited_time: 2026-06-12 15:05:00+08:00
edited_entity: llm
source_ids:
- karpathy-gist-llm-wiki
evidence_basis: practitioner_report
justification: ../justification/human-llm-cognitive-division.md
canonical_concept: human-llm-cognitive-division
aliases:
- human-LLM division of labor
- 人机认知分工
- curator vs bookkeeper
summary: human-llm-cognitive-division 明确划分 LLM Wiki 中的人机角色：人类负责 curate sources / direct analysis / ask good questions / think about meaning；LLM 负责 summarizing / cross-referencing / filing / bookkeeping
  —— 人类放弃维护 wiki 因为维护负担增长快于价值，LLM 使维护成本趋近零
related:
- persistent-compounding-artifact
- three-layer-architecture
- llm-kb-human-role-curation
- connections-as-value
- wiki-as-codebase-metaphor
---
LLM Wiki 建立在明确的人机认知分工之上：[^src-1]

**人类的角色**：curate sources（策展来源）、direct the analysis（引导分析方向）、ask good questions（提出好问题）、think about what it all means（思考意义）。这些是判断性、方向性的高阶认知活动。[^src-2]

**LLM 的角色**："everything else"——具体包括 summarizing、cross-referencing、filing、bookkeeping。这些是"grunt work"，即使人类做得到，规模化后也无法持续。[^src-3]

这种分工的根本理由：人类放弃维护 wiki 是因为"the maintenance burden grows faster than the value"。LLM 解决了这个问题——"LLMs don't get bored, don't forget to update a cross-reference, and can touch 15 files in one pass"。维护成本趋近零。[^src-4] [^card-1]

## Footnotes

[^src-1]: `data/raw/gist_raw/karpathy-gist-llm-wiki/text.txt` -- "Why this works" P2 -- "The human's job is to curate sources, direct the analysis, ask good questions, and think about what it all means. The LLM's job is everything else."
[^src-2]: `data/raw/gist_raw/karpathy-gist-llm-wiki/text.txt` -- "The core idea" P4 -- "You're in charge of sourcing, exploration, and asking the right questions."
[^src-3]: `data/raw/gist_raw/karpathy-gist-llm-wiki/text.txt` -- "The core idea" P4 -- "The LLM does all the grunt work — the summarizing, cross-referencing, filing, and bookkeeping"
[^src-4]: `data/raw/gist_raw/karpathy-gist-llm-wiki/text.txt` -- "Why this works" P1 -- "Humans abandon wikis because the maintenance burden grows faster than the value. LLMs don't get bored, don't forget to update a cross-reference, and can touch 15 files in one pass."
[^card-1]: [three-layer-architecture](three-layer-architecture.md) -- 分工映射到架构：人类控制 Raw sources 和 Schema，LLM 控制 Wiki 层
