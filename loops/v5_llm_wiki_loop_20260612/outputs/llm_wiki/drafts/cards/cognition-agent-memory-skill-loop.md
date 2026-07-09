---
id: cognition-agent-memory-skill-loop
title: Cognition 的 Skill 循环四步法
status: draft
card_type: workflow
tags: [agent-memory, skill-reuse, team-knowledge, workflow]
created_time: 2026-06-12T18:00:00+08:00
edited_time: 2026-06-12T18:00:00+08:00
edited_entity: llm
source_ids: [cognitionus-llm-wiki-guide]
evidence_basis: practitioner_report
justification: ../justification/cognition-agent-memory-skill-loop.md
canonical_concept: agent-memory-skill-loop
aliases: [Cognition skill loop, agent skill reuse workflow, Ask-Capture-Save-Retrieve]
summary: >-
  Cognition agent-memory-skill-loop 四步工作流：(1) Ask first — agent 任务开始时查询团队已有
  skill；(2) Capture work — 命令/文件编辑/卡点/outcomes 成为 evidence；(3) Save skills —
  系统生成 SKILL.md 草稿并等待人类 approve（confirm-first capture）；(4) Retrieve later —
  后续 agent 遇同类问题自动加载已批准 skill。核心设计：人类审批门控、作者归因、可执行指导。
related: []
---

Cognition 产品定义了一个以 skill 为中心的 agent memory 循环，分四步 [^src-1]：

1. **Ask first** — agent 在任务启动时先查询团队已有知识（"the agent checks what your team has already figured out"）。
2. **Capture work** — 命令、文件编辑、卡点（stuck points）和结果自动成为可复用工作流的 evidence。
3. **Save skills** — 系统将 evidence 整合为 SKILL.md 草稿，等待人类显式审批后才写入团队共享池（confirm-first capture）。
4. **Retrieve later** — 后续团队成员遇到相同问题时，其 agent 自动加载已批准 skill，而非从头猜测。

该设计强调 confirm-first capture：系统绝不自动共享，必须经人类 yes 才存入团队知识库 [^src-2]。

[^src-1]: `data/raw/webpage/cognitionus-llm-wiki-guide/markdown.md` -- "how it compounds" P18-45 -- "At task start, the agent checks what your team has already figured out... Bob hits the same wall later. His agent loads Alice's fix before guessing."
[^src-2]: `data/raw/webpage/cognitionus-llm-wiki-guide/markdown.md` -- "Confirm-first capture" P57-58 -- "Cognition drafts skills and waits for explicit approval before saving anything to the group."
