- path: ~/.codex/skills/agent-loop-runner/SKILL.md
  reason: 开发者指令要求在循环任务中使用相关 skill。
  usage: 读取最小工作约束，确认不创建额外 agent 且只写任务包允许产物。
- path: llm_wiki/loop/iterations/iteration_20260525_0029_card_adoption_ingest_workflow/task.md
  reason: 当前任务包。
  usage: 确认允许输入、允许写入、采纳对象和成功门禁。
- path: llm_wiki/loop/iterations/iteration_20260525_0027_card_drafting_ingest_workflow/artifacts/draft_card.md
  reason: 任务允许输入。
  usage: 作为待采纳知识卡内容，并将 status 改为 accepted。
- path: llm_wiki/loop/iterations/iteration_20260525_0027_card_drafting_ingest_workflow/artifacts/provenance.md
  reason: 任务允许输入。
  usage: 作为出处论证内容。
- path: llm_wiki/loop/iterations/iteration_20260525_0028_card_audit_ingest_workflow/artifacts/audit_report.md
  reason: 任务允许输入。
  usage: 确认 audit_result 是否为 pass。
- path: llm_wiki/kb/cards/llm-wiki-ingest-example-flow.md
  reason: 任务允许输入。
  usage: 仅用于存在性和覆盖冲突检查。
- path: llm_wiki/kb/provenance/llm-wiki-ingest-example-flow.md
  reason: 任务允许输入。
  usage: 仅用于存在性和覆盖冲突检查。
- path: llm_wiki/kb/indexes/cards.md
  reason: 任务允许输入。
  usage: 保留既有最小索引内容并做增量更新。
