# planner task

run_dir:: .llmwiki/runs/run_20260524_050634_major_impact_simulation

## 职责

选择 loop 和本次 run target，写 run_plan，不直接写 card。

## 安全边界

你不是 repo 里唯一的执行者。不要 revert、overwrite 或清理无关文件。任何超出 scoped inputs 的读取都应记录理由。
