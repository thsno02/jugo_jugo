---
id: idea-file-concept
title: Idea File 概念与 LLM Agent 时代的知识分享
status: draft
card_type: concept
tags: [idea-file, agent-era, code-sharing, abstraction, gist]
created_time: 2026-06-12T17:00:00+08:00
edited_time: 2026-06-12T17:00:00+08:00
edited_entity: llm
source_ids: [karpathy-x-launch-post]
evidence_basis: practitioner_report
justification: ../justification/idea-file-concept.md
canonical_concept: idea-file-concept
aliases: [idea file, idea文件, 想法文件, sharing ideas not code]
summary: >-
  idea-file-concept Idea File概念 LLM Agent时代的知识分享方式变革 Karpathy提出在LLM agent时代，
  分享具体代码/应用的意义降低，更有效的方式是分享抽象的"idea file"，接收者的agent可根据特定需求
  定制并构建。故意保持抽象/模糊因为方向众多。以GitHub Gist格式发布。讨论区可供他人调整或贡献想法。
related: [llm-knowledge-base-workflow]
---

Karpathy 在后续推文中提出"idea file"概念，其核心主张：

**时代变迁**："in this era of LLM agents, there is less of a point/need of sharing the specific code/app, you just share the idea, then the other person's agent customizes & builds it for your specific needs." [^src-1]

**设计意图**：
- 故意保持抽象/模糊 ("intentionally kept a little bit abstract/vague")
- 因为"there are so many directions to take this in"
- 以 GitHub Gist 格式发布，讨论区供他人调整/贡献

**隐含范式转移**：
- 从分享可执行制品 (code/app) → 分享可解释意图 (idea)
- 从精确实现 → 抽象规格
- 从人工复用 → agent 定制化构建

这暗示软件分享的粒度正在上移：代码 → API → idea，每一层的抽象度提高对应 agent 能力的提升。[^card-1]

[^src-1]: `data/raw/webpage/karpathy-x-launch-post/text.txt` -- "follow-up tweet" -- "The idea of the idea file is that in this era of LLM agents, there is less of a point/need of sharing the specific code/app, you just share the idea, then the other person's agent customizes & builds it for your specific needs."
[^card-1]: 参见 [[llm-knowledge-base-workflow]] — idea file 所描述的正是该工作流本身
