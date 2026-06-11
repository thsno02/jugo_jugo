- path: ~/.codex/skills/agent-loop-runner/SKILL.md
  reason: 当前环境技能规则要求在循环任务中使用该技能。
  use: 仅用于执行流程约束，不作为审计证据。
- path: llm_wiki/loop/iterations/iteration_20260525_0048_drafting_boundary_validation_evidence_audit/task.md
  reason: 当前任务包。
  use: 确认本轮审计目标、允许输入、禁止输入、允许写入和结论格式。
- path: llm_wiki/loop/iterations/iteration_20260525_0047_drafting_boundary_validation_evidence_repair/task.md
  reason: 目标执行者任务包。
  use: 审计目标执行者的输入输出边界和修复范围。
- path: llm_wiki/loop/iterations/iteration_20260525_0047_drafting_boundary_validation_evidence_repair/loop_status.md
  reason: 目标执行者状态产物。
  use: 判断状态是否落盘、是否可恢复。
- path: llm_wiki/loop/iterations/iteration_20260525_0047_drafting_boundary_validation_evidence_repair/loop_delivery.md
  reason: 目标执行者交付产物。
  use: 判断完成标记、声明产物和边界说明。
- path: llm_wiki/loop/iterations/iteration_20260525_0047_drafting_boundary_validation_evidence_repair/read_log.md
  reason: 目标执行者读日志。
  use: 检查读取范围是否和任务包允许输入一致。
- path: llm_wiki/loop/iterations/iteration_20260525_0047_drafting_boundary_validation_evidence_repair/artifacts/validation_evidence_report.md
  reason: 目标执行者核心产物。
  use: 审计 validation evidence 是否落盘、是否越界或漂移。
- path: llm_wiki/loop/iterations/iteration_20260525_0046_drafting_candidate_boundary_repair_audit/artifacts/independent_audit.md
  reason: prior audit concern。
  use: 核对 prior concern 指向的问题。
- path: llm_wiki/loop/decisions/20260525-0747-drafting-boundary-repair-audit-concern.md
  reason: prior concern decision。
  use: 核对主控对 prior concern 的处理要求。
- path: llm_wiki/loop/iterations/iteration_20260525_0045_drafting_candidate_boundary_repair/artifacts/prompt_repair_report.md
  reason: updated repair report。
  use: 核对原 prompt/template 修复内容是否被目标 correction 修改或漂移。
- path: llm_wiki/loop/iterations/iteration_20260525_0045_drafting_candidate_boundary_repair/task.md
  reason: original repair task。
  use: 核对原修复任务边界和允许写入范围。
- path: llm_wiki/loop/iterations/iteration_20260525_0045_drafting_candidate_boundary_repair/loop_delivery.md
  reason: original repair delivery。
  use: 核对原修复交付声明与本次 validation evidence 的关系。

未读取父聊天上下文、`data/` 来源正文、`user-insights/`、`legacy/`、候选 6 草稿卡正文或 provenance，未读取未列出的同主题审计报告。
