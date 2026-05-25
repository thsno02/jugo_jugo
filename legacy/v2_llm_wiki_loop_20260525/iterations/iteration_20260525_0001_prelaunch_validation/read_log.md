# read_log

## 审计材料读取

本次审计只把 dispatch payload 与 `task.md` 明确允许的文件作为审计证据。

已读取的允许输入：

- `llm_wiki/loop/iterations/iteration_20260525_0001_prelaunch_validation/task.md`
- `llm_wiki/loop/PRELAUNCH_REQUIREMENTS.md`
- `llm_wiki/loop/CONTEXT_ISOLATION.md`
- `llm_wiki/loop/MAIN_AGENT_ELASTICITY.md`
- `llm_wiki/loop/SUBAGENT_EVOLUTION.md`
- `llm_wiki/loop/SUBAGENT_LIFECYCLE.md`
- `llm_wiki/loop/TECH_VALIDATION.md`
- `llm_wiki/loop/RUNBOOK.md`
- `llm_wiki/loop/SUBAGENT_SCOPE.md`
- `llm_wiki/loop/loop_state.json`
- `llm_wiki/loop/loop_manifest.json`
- `llm_wiki/loop/queues/task_queue.md`
- `llm_wiki/loop/reports/loop_report.md`
- `llm_wiki/loop/tools/README.md`
- `llm_wiki/loop/tools/create_task.py`
- `llm_wiki/loop/tools/render_dispatch.py`
- `llm_wiki/loop/tools/validate_scope.py`
- `llm_wiki/loop/tools/inspect_delivery.py`
- `llm_wiki/loop/iterations/iteration_0000_bootstrap/artifacts/codex_hooks_feasibility_smoke.md`
- `llm_wiki/loop/iterations/iteration_0000_bootstrap/artifacts/cli_capability_probe.md`
- `user-insights/` 下本次 sidecar 写入的文件。

## 调度层读取

- `/Users/lw/Desktop/GitHub/llm_wiki/jugo_jugo/llm_wiki/loop/iterations/iteration_20260525_0001_prelaunch_validation/dispatch_request.json`：用户指定的 dispatch payload，用于启动任务。
- `/Users/lw/.codex/skills/agent-loop-runner/SKILL.md`：当前 Codex 技能规则要求读取，用于遵循 loop worker 工作流；未作为审计结论的事实证据。

## 禁止输入

未读取 `llm_wiki/legacy/`、`data/` 来源内容、知识卡草稿、hub、cluster、旧同主题审计报告或父聊天上下文。
