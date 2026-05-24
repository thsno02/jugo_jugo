# 技术最小验证

本文件记录 loop 前置阶段需要验证的技术路线。

## 已确认

### Codex CLI

本机存在：

```text
/opt/homebrew/bin/codex
codex-cli 0.132.0
```

`codex features list` 显示：

- `hooks stable true`
- `plugin_hooks stable true`
- `multi_agent stable true`

### Claude CLI

本机存在：

```text
/opt/homebrew/bin/claude
2.1.128 (Claude Code)
```

`claude --help` 显示它支持：

- `--agent`
- `--agents`
- `--system-prompt`
- `--append-system-prompt`
- `--tools`
- `--allowedTools`
- `--disallowedTools`
- `--permission-mode`
- `--max-budget-usd`
- `--no-session-persistence`
- `--output-format`

这使 Claude CLI 成为写作型隔离 worker 的候选 runtime。

## Codex hooks 结论

已记录在：

- `iterations/iteration_0000_bootstrap/artifacts/codex_hooks_feasibility_smoke.md`

当前结论：

- hooks 适合做 guardrail、context preprocessor、stop 检查。
- hooks 不适合被当成原生 sub-agent dispatcher。
- 动态创建未受信任 hook 的 smoke test 不可靠。
- 真正使用 project hooks 需要人类 review / trust。

## CLI smoke 结论

已记录在：

- `iterations/iteration_0000_bootstrap/artifacts/cli_capability_probe.md`
- `iterations/iteration_0000_bootstrap/artifacts/cli_worker_smoke.md`

### 1. Codex CLI 作为 worker runtime

已完成最小 smoke：

- `codex exec --ephemeral --sandbox read-only` 可以启动外部只读 worker。
- smoke 返回 `READY`。
- 运行会触发已信任 hooks，并产生 hook / loader 日志噪声。

仍未验证：

- 读取 `dispatch_request.md` 后写出 `loop_status.md`、`loop_delivery.md`、`read_log.md` 的完整 worker 闭环。
- `workspace-write` 下的写入隔离和交付检查。

### 2. Claude CLI 作为写作 worker runtime

已完成最小 smoke：

- `claude -p --no-session-persistence --tools "" --max-budget-usd 0.02` 可以启动无工具写作 worker。
- smoke 返回 `READY`。

建议最小命令形态：

```text
claude -p \
  --no-session-persistence \
  --permission-mode default \
  --tools "" \
  --max-budget-usd 0.05 \
  --system-prompt "<base_worker + role>" \
  "<task.md 内容>"
```

仍未验证：

- `--tools ""` 下不能写文件，只能输出文本；若要写文件，需要允许工具或由主控 agent 把输出落盘。
- Claude CLI 是外部 runtime，不是当前 Codex multi-agent 体系的一部分。

### 3. 原生 Codex sub-agent

目标：

- 继续使用 `multi_agent_v1.spawn_agent`。
- 用 `render_dispatch.py` 生成 message。
- main-agent 只复制 dispatch payload，不临场写 prompt。

风险：

- 当前可见 agent 类型只有 `default`、`explorer`、`worker`。
- 本轮没有验证 `.codex/agents/*.toml` 能直接变成可选 sub-agent type。

## 当前推荐

短期：

```text
Codex 原生 sub-agent + render_dispatch.py
```

中期：

```text
project hooks 做 guardrail
Claude CLI 做写作型外部 worker smoke
```

长期：

```text
MCP / plugin tool 封装 dispatch 与 spawn
```
