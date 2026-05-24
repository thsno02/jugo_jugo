# CLI worker runtime smoke

日期：2026-05-25

本文件记录前置阶段对 Codex CLI 和 Claude CLI 的最小 worker runtime 验证。验证目标不是正式执行知识生产，而是确认外部 CLI 能否在低权限或无工具条件下完成一次隔离文本任务。

## Claude CLI

命令形态：

```text
claude -p --no-session-persistence --permission-mode default --tools "" --max-budget-usd 0.02 --system-prompt "你是只读 smoke worker。只能输出 READY。" "只输出 READY，不解释。"
```

结果：

```text
READY
```

结论：

- `claude -p` 可以作为无工具写作型 worker runtime 的候选。
- 本次只验证了文本输出，没有验证写文件能力。
- 如果后续要让 Claude CLI 写文件，需要单独设计允许工具、写入目录、成本上限和交付检查。

## Codex CLI

命令形态：

```text
codex exec --ephemeral --sandbox read-only -C /Users/lw/Desktop/GitHub/llm_wiki/jugo_jugo "只输出 READY，不要解释，不要读取文件，不要运行命令。"
```

结果要点：

```text
sandbox: read-only
session id: 019e5b25-2e3a-7732-a71d-5ba9de0afc74
hook: SessionStart
hook: UserPromptSubmit
hook: Stop
READY
```

结论：

- `codex exec` 可以作为外部只读 worker runtime 启动。
- `--ephemeral` 可以减少 session 持久化污染。
- 运行会触发已信任 hooks，并产生 hook / loader 日志噪声。
- 本次没有验证写文件 worker；写文件需要 `workspace-write` 或明确写入路径，并必须通过 `inspect_delivery.py` 检查产物。

## 当前可采纳判断

短期首选仍是 Codex 原生 sub-agent，因为它更贴近当前线程内的调度能力。

外部 CLI runtime 可以作为补充路线：

- Claude CLI：优先用于无工具写作、改写、审计草案等文本输出场景。
- Codex CLI：优先用于受控 sandbox、可恢复 session、需要 hooks guardrail 的外部 worker smoke。

二者都不应该绕过任务包、允许输入、允许写入、交付文件和独立审计。
