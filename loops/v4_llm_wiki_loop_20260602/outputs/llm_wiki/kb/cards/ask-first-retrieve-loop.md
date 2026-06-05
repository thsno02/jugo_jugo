---
id: ask-first-retrieve-loop
title: 先查后做的 Agent 工作循环
status: accepted
card_type: mechanism
tags: [agent-memory, workflow, skill-lookup, knowledge-reuse, team-memory]
created_time: 2026-06-05T10:00:00+08:00
edited_time: 2026-06-05T10:00:00+08:00
edited_entity: llm
source_ids: [cognitionus-llm-wiki-guide]
justification: ../justification/ask-first-retrieve-loop.md
canonical_concept: ask-first-retrieve-loop
aliases: [先查后做循环, ask-first loop, 技能查找-捕获-保存-检索循环, skill lookup retrieve loop]
summary: >-
  ask-first-retrieve-loop（先查后做循环 / ask-first loop / 技能查找-捕获-保存-检索循环）Cognition 的四步 agent 工作循环：任务开始时先查询团队已有技能（Ask first）→ 捕获工作证据（Capture work）→ 起草并审批技能（Save skills）→ 未来 agent 加载已有技能后再行动（Retrieve later），核心原则是检索先于猜测
related: [agent-memory-lifecycle-phases, confirm-first-skill-capture, executable-guidance-vs-context-pile, retrieval-vs-maintenance]
---

Cognition 定义了一个四步 agent 工作循环，其核心原则是**检索先于猜测**[^src-1]。

**Step 1 — Ask first（先查）**：任务开始时，agent 首先检查团队已有的知识积累[^src-2]。材料用技能查找界面（skill lookup）展示了这一步，列出如 `vercel-env-scoping`、`auth-callback-race`、`stripe-webhook-retry` 等已积累的技能[^src-3]。

**Step 2 — Capture work（捕获工作）**：agent 执行任务的过程中，命令、文件编辑、卡点和结果被记录为可复用工作流的证据[^src-4]。

**Step 3 — Save skills（保存技能）**：Cognition 从证据中起草 SKILL.md，等待人类批准后共享给团队[^src-5]。

**Step 4 — Retrieve later（后续检索）**：未来其他团队成员遇到相同问题时，其 agent 在尝试自行解决之前先加载已有的技能[^src-6]。

该循环的本质是将团队的重复问题解决模式从「每人独立猜测」转变为「先查已有方案，再补充新知」。材料用一个具体场景说明：Alice 解决了 Vercel 环境变量作用域问题，该技能被捕获并审批后，Bob 遇到同样问题时其 agent 直接加载 Alice 的修复方案[^src-7]。

这一循环的价值在企业知识管理分析中得到独立印证：大多数企业工具只是检索工具，真正的差异化在于维护循环而非搜索层 [^card-1]。

## Footnotes

[^src-1]: `data/raw/webpage/cognitionus-llm-wiki-guide/text.txt` -- "For organizations" section -- "let every agent ask the brain before guessing"
[^src-2]: `data/raw/webpage/cognitionus-llm-wiki-guide/text.txt` -- "Ask first" step -- "At task start, the agent checks what your team has already figured out."
[^src-3]: `data/raw/webpage/cognitionus-llm-wiki-guide/text.txt` -- "SKILL LOOKUP" section -- "vercel-env-scoping / auth-callback-race / stripe-webhook-retry"
[^src-4]: `data/raw/webpage/cognitionus-llm-wiki-guide/text.txt` -- "Capture work" step -- "Commands, file edits, stuck points, and outcomes become evidence for a reusable workflow."
[^src-5]: `data/raw/webpage/cognitionus-llm-wiki-guide/text.txt` -- "Save skills" step -- "Cognition drafts the SKILL.md and waits for a human yes before sharing it."
[^src-6]: `data/raw/webpage/cognitionus-llm-wiki-guide/text.txt` -- "Retrieve later" step -- "Bob hits the same wall later. His agent loads Alice's fix before guessing."
[^src-7]: `data/raw/webpage/cognitionus-llm-wiki-guide/text.txt` -- "Retrieve later" step -- "Bob hits the same wall later. His agent loads Alice's fix before guessing."
[^card-1]: [检索与维护的区别](retrieval-vs-maintenance.md) -- Falconer 指出大多数企业工具只是检索工具，真正的差异化在于维护循环，"先查后做"正是维护优先理念的具体实践
