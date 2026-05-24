# Codex hooks 可行性 smoke

## 问题

是否可以用 Codex hooks 把 main-agent 从“临场写 sub-agent prompt”中进一步解放出来，让 main-agent 只做决策和调度？

## 只读 sub-agent 调查

独立执行者 `019e5b0d-4627-7f43-9929-2d558e09ee1b` 做了只读调查。

主要证据：

- 本机 `codex-cli 0.132.0`。
- `codex features list` 显示 `hooks stable true`、`plugin_hooks stable true`、`multi_agent stable true`。
- `~/.codex/config.toml` 中 `[features] hooks = true`。
- `~/.codex/hooks.json` 已配置 `PreToolUse`、`PostToolUse`、`SessionStart`、`UserPromptSubmit`、`Stop` command hook。
- 官方文档说明 project/user hooks 可放在 `~/.codex/hooks.json`、`~/.codex/config.toml`、`<repo>/.codex/hooks.json`、`<repo>/.codex/config.toml`。
- 官方文档说明 `UserPromptSubmit` 和 `SubagentStart` 可通过 stdout / JSON 输出追加 `additionalContext`。
- 官方文档说明 `PreToolUse` 可 block 或在支持范围内 `updatedInput`。
- 二进制字符串和官方文档都显示 hooks 是生命周期脚本，不是原生 sub-agent runtime。

## 本地 smoke 结果

已尝试以下低风险验证：

- `codex debug prompt-input` + 临时 `CODEX_HOME`：未触发 `UserPromptSubmit` hook；该命令不能作为 hook 执行验证。
- `codex exec` + 临时非 git 目录：失败于 git repo check，未触发项目 hook。
- `codex exec` + 临时 git repo + project hook：没有触发临时 project hook。原因推断是 project-local hooks 只在 project `.codex/` config layer 被信任时加载。
- `codex exec` + 临时 `CODEX_HOME` + copied auth + trusted temp project：没有触发临时 hook。
- 短暂追加 / 替换 `~/.codex/hooks.json` 后运行 `codex exec`：没有触发新增未受信任 hook；现象说明 CLI exec 对动态修改的 hooks 不能作为可靠 smoke，或者仍需要交互式 trust review / hot reload 路径。

所有临时改动都已清理或恢复。

## 可行性判断

可行部分：

- hooks 可以作为 guardrail、审计、上下文注入、停止前检查层。
- 已信任 hooks 在当前 Codex 环境中确实存在并被使用。
- `UserPromptSubmit` / `SubagentStart` 适合注入“当前 loop 控制面、角色边界、任务包路径”等轻量 context。
- `PreToolUse` 适合阻止 main-agent 越界读取 `data/raw/` 或直接写 `llm_wiki/kb/cards/`。
- `SubagentStop` / `Stop` 适合检查 `loop_status.md`、`loop_delivery.md`、`read_log.md` 是否存在，并要求继续补齐。

不可行或不应依赖的部分：

- hooks 当前不应被设计为原生 sub-agent dispatcher。
- hook 内部直接启动 `codex exec` 会变成外部独立 session，不是当前 thread 的 sub-agent。
- 动态创建未受信任 hook 做自动 smoke 不可靠。
- 当前 multi-agent 工具暴露的 role 仍是 `default` / `explorer` / `worker`，本轮没有验证 `.codex/agents/*.toml` 能直接变成可选 sub-agent role。

## 建议实现路线

先做 project-local、可审计、需要人类 review/trust 的最小原型：

```text
.codex/hooks.json
.codex/hooks/llmwiki-user-prompt-submit.sh
.codex/hooks/llmwiki-pre-tool-use.sh
.codex/hooks/llmwiki-stop.sh
```

配合：

```text
llm_wiki/loop/tools/create_task.py
llm_wiki/loop/tools/render_dispatch.py
llm_wiki/loop/tools/validate_scope.py
llm_wiki/loop/tools/inspect_delivery.py
```

运行方式：

```text
main-agent 选择 role 和少量变量
-> create_task.py 生成 task.md
-> render_dispatch.py 生成 dispatch payload
-> main-agent 调用已定义 sub-agent
-> hooks 做越界拦截和停止检查
```

这样 main-agent 仍会触发 sub-agent，但不再临场写大段 prompt。

## 当前结论

hooks 适合作为控制面防护层和 prompt/context preprocessor；custom agents / skills 适合作为稳定 role prompt 来源。二者组合能明显减少 main-agent 临场写 prompt 的比例。

但目前不应把 hooks 当作完全自动的 sub-agent 调度器。要实现真正的 dispatcher，需要 Codex 提供原生 agent hook，或者项目自己提供 MCP / plugin tool 来封装 `spawn_agent`。
