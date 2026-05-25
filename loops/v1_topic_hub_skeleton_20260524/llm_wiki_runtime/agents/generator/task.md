# generator task

run_dir:: .llmwiki/runs/<run_id>
main_language:: zh-CN
status:: generation_entry_gate_required

## 职责

在限定 evidence scope 内生成完整 version bundle；evidence 不足时先写 retrieval_request。

Main/controller 只创建或审查本 task packet、读取你的 summary/status/gate/delivery、决定 adoption/repair/retrieval/defer。你是 worker/executor，必须在 delivery 中写明 executor_role、task_packet、allowed_inputs、outputs_written 和 `LOOP_DONE` / `LOOP_BLOCKED`。

## 启动前硬闸门

只有在以下条件全部满足时才能写 `card.md`：

- `generation_entry_gate.md` 存在并且 result 是 `pass`。
- `next_task_packet.md` 指向 `knowledge_frontier.yaml` 中的 `ready_to_build` candidate。
- candidate 有 source mining artifacts 支持。
- source mining artifacts 不是未复核的 controller drift sample。
- allowed inputs、forbidden inputs、version target 和 output paths 都明确。

缺任一项，返回 `LOOP_BLOCKED`，不要生成 card。

## 安全边界

你不是 repo 里唯一的执行者。不要 revert、overwrite 或清理无关文件。任何超出 scoped inputs 的读取都应记录理由。
