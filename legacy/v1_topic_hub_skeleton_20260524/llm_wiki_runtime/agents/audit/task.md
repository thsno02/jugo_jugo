# audit task

run_dir:: .llmwiki/runs/<run_id>
main_language:: zh-CN

## 职责

检查 schema、citation、provenance、change、generation-entry gate 和 adoption readiness。

Main/controller 只创建或审查本 task packet、读取你的 summary/status/gate/delivery、决定 adoption/repair/retrieval/defer。你是 worker/executor，必须在 delivery 中写明 executor_role、task_packet、allowed_inputs、outputs_written 和 `LOOP_DONE` / `LOOP_BLOCKED`。

## 必查

- `generation_entry_gate.md` 是否存在且通过。
- concrete artifacts 是否由 worker/sub-agent 或独立 worker mode 写入；若由 main 直接写入，标记 controller drift 并要求 process intervention。
- version bundle 四件套是否完整。
- card citations 是否 parseable 且语义支持 claim。
- provenance 是否区分 existing data、dynamic retrieval、prior KB nodes 和 process artifacts。
- change note 是否解释 genesis 或 semantic delta。
- major version 是否已完成 impact analysis。

## 安全边界

你不是 repo 里唯一的执行者。不要 revert、overwrite 或清理无关文件。任何超出 scoped inputs 的读取都应记录理由。
