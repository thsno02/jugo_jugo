---
id: karpathy-llm-wiki-concept
title: Karpathy LLM Wiki 理念
status: draft
card_type: design-philosophy
tags: [llm-wiki, knowledge-management, personal-knowledge-base]
created_time: 2026-06-12T17:00:00+08:00
edited_time: 2026-06-12T17:00:00+08:00
edited_entity: llm
source_ids: [obsidian-community-plugin]
evidence_basis: documentation
justification: ../justification/karpathy-llm-wiki-concept.md
canonical_concept: karpathy-llm-wiki-concept
aliases: [LLM Wiki, Karpathy's LLM Wiki, Karpathy Wiki]
summary: >-
  Karpathy LLM Wiki 理念：将用户笔记视为原材料，由 LLM 充当建筑师自动提取实体和概念，
  编织成结构化互联 Wiki，包含双向链接、自动索引和对话式查询界面。用户只写笔记，
  AI 负责组织、链接和维护知识图谱。
related: [full-context-vs-rag, three-layer-wiki-architecture]
---

Karpathy LLM Wiki 的核心理念是将用户笔记视为原材料，让 LLM 承担"建筑师"角色。LLM 阅读用户所写内容，提取实体（人物、组织、产品、事件）和概念（理论、方法、术语），将其编织成结构化 Wiki，包含 [[双向链接]]、自动生成的索引和对话式问答界面。[^src-1]

用户不再需要决定什么值得单独建页、维护交叉链接或担忧内容过时。将笔记放入 sources/ 后，LLM 负责阅读、提取、撰写、链接，甚至标记矛盾。[^src-1]

[^src-1]: `data/raw/webpage/obsidian-community-plugin/markdown.md` -- "The fix" P1 -- "Andrej Karpathy suggested something elegant: treat your notes as raw material, and let an LLM do the architect work. It reads what you write, pulls out entities and concepts, and weaves them into a structured Wiki"
