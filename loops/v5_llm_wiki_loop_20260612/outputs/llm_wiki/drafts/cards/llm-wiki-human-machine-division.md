---
id: llm-wiki-human-machine-division
title: llm-wiki 人机职责分工
status: draft
card_type: design-principle
tags: [llm-wiki, human-machine-division, workflow, agent-skill]
created_time: 2026-06-12T19:00:00+08:00
edited_time: 2026-06-12T19:00:00+08:00
edited_entity: llm
source_ids: [repo-lewislulu-llm-wiki-skill]
evidence_basis: code_implementation
justification: ../justification/llm-wiki-human-machine-division.md
canonical_concept: llm-wiki-human-machine-division
aliases: [human-machine division, 人机分工, you own vs LLM owns, llm-wiki 职责边界]
summary: >-
  llm-wiki-human-machine-division 人机职责分工：用户负责(own)素材输入(sourcing raw material)、
  提出问题(asking good questions)、方向引导(steering direction)、对错误提反馈(filing feedback)；
  LLM 负责(own)所有写作、交叉引用、归档、簿记(bookkeeping)及处理反馈(acting on feedback)。
related: [compile-over-rag-wiki-pattern]
---

llm-wiki 明确划定人与 LLM 的职责边界。[^src-1]

用户拥有(own)四项职责：sourcing raw material（提供原始素材）、asking good questions（提出优质问题）、steering direction（把控方向）、filing feedback on things the AI got wrong（对 AI 错误提出反馈）。[^src-1]

LLM 拥有(own)五项职责：all writing（所有写作）、cross-referencing（交叉引用）、filing（归档）、bookkeeping（簿记）、acting on your feedback（处理用户反馈）。[^src-1] 据材料推测，这种分工设计让用户专注于高层决策和质量把控，而将繁重的知识结构化工作交给 LLM。[^card-1]

[^src-1]: `data/raw/github_repo/repo-lewislulu-llm-wiki-skill/repo/README.md` -- "What this is" P2 -- "You own: sourcing raw material, asking good questions, steering direction, filing feedback on things the AI got wrong. LLM owns: all writing, cross-referencing, filing, bookkeeping, and acting on your feedback."
[^card-1]: [[compile-over-rag-wiki-pattern]] — 编译式模式下 LLM 承担写作和结构化的全部工作，人只负责输入和反馈
