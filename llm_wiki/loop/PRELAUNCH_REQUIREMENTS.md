# 循环启动前置要求

本文件定义“正式开始生产 scoped knowledge cards”之前必须满足的条件。

当前阶段不是知识生产阶段，而是 loop 前置阶段。只有这些门禁通过后，主控 agent 才能派发第一轮 `source_mining_worker`。

## 前置门禁

### 1. 上下文隔离门禁

必须满足：

- 执行者只接收 `system_prompts/base_worker.md`、对应角色 prompt 和当前 `task.md`。
- 执行者默认 `fork_context: false`。
- `task.md` 明确允许输入、禁止输入、允许写入、成功门禁和阻塞条件。
- 任何允许输入之外的读取都先记录到 `read_log.md`。
- 执行者不能读取父聊天上下文、旧审计报告或其它执行者产物，除非任务包明确允许。

验收方式：

- `validate_scope.py` 能通过当前任务包。
- `independent_evaluator` 能只凭磁盘产物复核。

### 2. 受限 main-agent 弹性门禁

主控 agent 不能亲自做大段来源挖掘、写卡、审计或采纳，但它必须保留必要弹性。

允许的弹性：

- 创建或修改任务包。
- 选择一个具体来源。
- 调用 `tools/create_task.py`。
- 调用 `tools/render_dispatch.py` 生成 dispatch payload。
- 调用 `tools/validate_scope.py` 和 `tools/inspect_delivery.py` 做机械检查。
- 在执行者失败时创建 `skill_evolution_worker` 或 `independent_evaluator` 任务。

禁止的弹性：

- 亲自把来源内容整理成事实候选。
- 亲自把事实候选写成知识卡。
- 越过审计直接采纳知识卡。
- 通过“临时 prompt”放宽执行者边界。

### 3. 预定义 sub-agent 演化门禁

已有执行者必须预定义在：

- `loop_manifest.json`
- `system_prompts/<role>.md`
- `task_templates/<role>_task.md`

主控 agent 可以提出新增或修改 sub-agent，但不能临场发明一个无限权限的执行者。

新增或修改流程：

```text
失败证据
-> skill_evolution_worker 任务包
-> 修改 system prompt / task template / manifest
-> independent_evaluator 审计
-> 主控 agent 决策
```

### 4. 技术最小验证门禁

必须完成并记录：

- Codex hooks 可行性调查。
- Codex CLI 是否能作为受控 worker runtime。
- Claude CLI 是否能作为写作型 worker runtime。
- 如果某项不能可靠验证，必须说明原因和替代路线。

当前初步判断：

- Codex hooks 适合做 guardrail、context preprocessor、stop 检查。
- Codex hooks 当前不适合作为原生 sub-agent dispatcher。
- Claude CLI 存在，且支持 `--agents`、`--system-prompt`、`--append-system-prompt`、`--tools`、`--permission-mode`、`--max-budget-usd` 等参数；适合做隔离写作 worker 的候选。

### 5. sub-agent 生命周期门禁

必须明确哪些执行者可以常驻，哪些阅后即焚。

默认策略：

- `main_agent`：常驻决策者。
- `monitor`：可常驻或周期性短跑，只看状态文件。
- `source_mining_worker`：阅后即焚。
- `card_drafting_worker`：阅后即焚。
- `card_audit_worker`：阅后即焚。
- `card_adoption_worker`：阅后即焚。
- `independent_evaluator`：阅后即焚，且默认不读已有同类审计报告。
- `skill_evolution_worker`：短期驻留，只在一个失败簇内连续工作。

### 6. 用户洞察记录门禁

当前 chat session 中积压的用户约束、偏好、设计判断必须写入磁盘。

当前正式记录目标是：

- `user-insights/sessions/<session-id>/session_log.md`
- `user-insights/session_registry.json`
- `user-insights/session/cursor.json`
- `user-insights/session/sidecar_state.json`

`llm_wiki/loop/user_insights/` 是发现正式 skill 前的临时 fallback，只保留为历史痕迹；后续增量记录必须由 `user-insights` sidecar 写入顶层 `user-insights/`。

## 启动判定

只有当前置门禁都满足，`loop_state.json.status` 才能进入：

```text
READY_FOR_SOURCE_MINING
```

否则保持：

```text
PRELAUNCH_IN_PROGRESS
```
