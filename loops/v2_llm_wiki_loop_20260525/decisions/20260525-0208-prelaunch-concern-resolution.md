# 前置门禁审计 concern 处理决策

日期：2026-05-25

## 背景

`iteration_20260525_0001_prelaunch_validation` 的独立审计已完成，结论为：

```text
audit_result: concern
```

审计结论认为控制面基本可用，但进入 `READY_FOR_SOURCE_MINING` 前需要处理三个 concern：

- `loop_report.md` 仍有一处用户洞察证据链接指向旧 fallback。
- `user-insights` 当前是 `coverage: partial`，需要主控 agent 明确是否接受为残余风险。
- 后续技术验证审计的允许输入需要包含 `cli_worker_smoke.md`，否则审计者不能复核新 smoke 证据。

## 处理决策

### 1. 用户洞察 canonical 链接

已将循环报告中的用户洞察证据入口改为顶层：

```text
user-insights/index.md
user-insights/sessions/session_20260525_llm_wiki_loop_bootstrap/session_log.md
```

`llm_wiki/loop/user_insights/` 只保留为 pre-skill fallback，不再作为 canonical 入口。

### 2. `coverage: partial` 的处理

接受 `user-insights` 当前 `coverage: partial` 作为进入第一轮 source mining 的残余风险，而不是阻塞项。

理由：

- `user-insights` 是人类 recall 和过程洞察记录，不是知识卡事实来源。
- 第一轮 source mining 的事实来源只能来自任务包明确列出的 `data/` 本地来源。
- `user-insights` sidecar 已明确标注 partial coverage，没有伪装成 full transcript。
- 如果未来可获得完整 transcript 或 verified refreshed fork，需要单独触发 coverage repair。

约束：

- 不得把 `user-insights` 中的任何总结当作 atomic fact card 的来源。
- 后续 source mining worker 不允许读取 `user-insights/`，除非任务包明确说明用途且不用于事实证明。

### 3. CLI smoke 审计入口

已将后续 CLI worker smoke 审计任务的输入范围更新为同时包含：

```text
llm_wiki/loop/iterations/iteration_0000_bootstrap/artifacts/cli_capability_probe.md
llm_wiki/loop/iterations/iteration_0000_bootstrap/artifacts/cli_worker_smoke.md
llm_wiki/loop/TECH_VALIDATION.md
```

这样后续审计者可以复核 CLI worker smoke 证据，而不需要读取未授权材料。

## 状态迁移

上述 concern 已处理。主控 agent 可以将 `loop_state.json.status` 从：

```text
PRELAUNCH_IN_PROGRESS
```

推进到：

```text
READY_FOR_SOURCE_MINING
```

下一步不是直接生产知识卡，而是创建第一轮 `source_mining_worker` 的窄任务包，并从 `data/` 中选择一个已获取来源。
