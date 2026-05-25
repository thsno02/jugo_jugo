# eval task

run_dir:: .llmwiki/runs/<run_id>
main_language:: zh-CN

## 职责

评估本次 run 对 skill 的启发，区分 case-level observation 和 skill-level failure。

Main/controller 只创建或审查本 task packet、读取你的 summary/status/gate/delivery、决定是否 patch skill/process。你是 worker/executor，必须在 delivery 中写明 executor_role、task_packet、allowed_inputs、outputs_written 和 `LOOP_DONE` / `LOOP_BLOCKED`。

## 必查

- 是否出现绕过 source mining / frontier / generation-entry gate 的倾向。
- 是否出现 main agent 从 controller 漂移为 concrete executor 的倾向。
- 哪个 skill 应当承担预防责任。
- 问题是单次低风险观察、重复 failure、高风险 failure，还是 hard contract break。
- 是否需要 patch `.llmwiki/skills/llmwiki-*/SKILL.md` 或仅记录 case note。

## 安全边界

你不是 repo 里唯一的执行者。不要 revert、overwrite 或清理无关文件。任何超出 scoped inputs 的读取都应记录理由。
