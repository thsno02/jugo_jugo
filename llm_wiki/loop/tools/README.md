# loop tools

这里放机械脚本，用来减少 main-agent 临场写 prompt 的比例。

这些脚本不能替代执行者做知识生产，只能做任务包生成、dispatch 渲染和交付检查。

## 工具

- `create_task.py`：从角色模板生成 iteration task。
- `render_dispatch.py`：组合 system prompt 和 task，生成 sub-agent dispatch payload。
- `validate_scope.py`：检查任务包是否包含必要边界。
- `inspect_delivery.py`：检查执行者是否留下必要交付。
- `cli_capability_probe.py`：记录 Codex / Claude CLI 的本地能力线索。

## 原则

- 脚本输出必须可审计。
- 脚本不能读取父聊天上下文。
- 脚本不能主动访问网络。
- 脚本不能写 KB 产物。
