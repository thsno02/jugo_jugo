- path: `~/.codex/skills/agent-loop-runner/SKILL.md`
  reason: 本地技能触发规则要求在循环类任务中读取对应技能说明。
  purpose: 仅用于确认执行流程约束；不作为知识卡审计证据。
- path: `llm_wiki/loop/iterations/iteration_20260525_0031_card_audit_query_workflow/task.md`
  reason: 当前任务包。
  purpose: 确认审计对象、允许输入、允许写入、审计问题和完成门禁。
- path: `llm_wiki/loop/iterations/iteration_20260525_0030_card_drafting_query_workflow/artifacts/draft_card.md`
  reason: 任务包允许输入中的草稿知识卡。
  purpose: 审计 statement、fact_type、support、scope、status、References 和 Footnotes。
- path: `llm_wiki/loop/iterations/iteration_20260525_0030_card_drafting_query_workflow/artifacts/provenance.md`
  reason: 任务包允许输入中的出处论证。
  purpose: 核对草稿卡与指定来源证据之间的支撑关系。
- path: `data/raw/gist_raw/karpathy-gist-llm-wiki/raw.txt:39-40`
  reason: 任务包指定的来源证据行。
  purpose: 核对 Query 小节原文是否支撑草稿卡陈述。
