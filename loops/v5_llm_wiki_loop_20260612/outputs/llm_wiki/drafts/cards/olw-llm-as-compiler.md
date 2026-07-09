---
id: olw-llm-as-compiler
title: LLM 作为知识编译器而非对话伙伴
status: draft
card_type: design-philosophy
tags: [llm-wiki, karpathy, knowledge-compilation, persistent-artifact]
created_time: 2026-06-12T18:00:00+08:00
edited_time: 2026-06-12T18:00:00+08:00
edited_entity: llm
source_ids: [repo-kytmanov-obsidian-local]
evidence_basis: author_claim
justification: ../justification/olw-llm-as-compiler.md
canonical_concept: olw-llm-as-compiler
aliases: [LLM as compiler, LLM Wiki, Karpathy LLM Wiki, llm-wiki pattern]
summary: >-
  obsidian-llm-wiki 实现 Karpathy 提出的 LLM Wiki 模式：LLM 不是对话伙伴而是知识编译器，
  用户提供原始材料 raw notes 作为源，LLM 将其编译为持久化结构化 wiki 制品。
  区别于聊天机器人每次对话从零开始，wiki 持续积累 persists and compounds。
  笔记是源材料 source material 而非最终制品。LLM compiler not conversation partner
  persistent artifact。
related: [olw-three-stage-pipeline]
---

obsidian-llm-wiki 的设计哲学源自 Andrej Karpathy 提出的 "LLM Wiki" 构想 [^src-1]：

**核心定位**：LLM 是知识编译器（compiler），而非对话伙伴（conversation partner）。用户提供原始材料（raw notes），LLM 将其编译为结构化知识产物（structured wiki）。产出物是用户永久拥有的纯 markdown 文件 [^src-2]。

**与聊天机器人的根本区别**：聊天机器人遗忘——每次对话从零开始。而 LLM Wiki 构建的是持久化制品（persistent artifact），随着每一篇新笔记的加入而增长、积累（persists and compounds）[^src-3]。

**关键洞察**：将笔记视为"源材料"（source material）而非最终制品。LLM 负责综合、交叉引用、保持更新等"簿记"工作（bookkeeping），用户只需添加原始材料 [^src-1]。

[^src-1]: `data/raw/github_repo/repo-kytmanov-obsidian-local/repo/README.md` -- "The idea (Karpathy's LLM Wiki)" P36-40 -- "The key insight: treat your notes as source material, not as the final artifact. The LLM compiles them into a structured wiki that grows smarter as you add more."
[^src-2]: `data/raw/github_repo/repo-kytmanov-obsidian-local/repo/README.md` -- "Why not just use a chatbot?" P801-802 -- "The LLM is a compiler, not a conversation partner. You give it raw material; it produces structured knowledge. The output is plain markdown files you own forever."
[^src-3]: `data/raw/github_repo/repo-kytmanov-obsidian-local/repo/README.md` -- "Why not just use a chatbot?" P799 -- "Chatbots forget. Every conversation starts fresh. This tool builds a persistent artifact"
[^card-1]: 该理念通过 olw 三阶段管线 (olw-three-stage-pipeline) 落地实现
