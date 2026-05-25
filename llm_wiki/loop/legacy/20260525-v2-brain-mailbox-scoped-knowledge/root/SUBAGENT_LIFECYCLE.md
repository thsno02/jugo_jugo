# sub-agent 生命周期

不同 sub-agent 的生命周期不同。生命周期设计的目标是降低上下文污染，同时保留必要的长期判断。

## 生命周期类型

### 常驻

常驻角色保留跨轮判断，但只读低噪声控制面。

当前常驻角色：

- `main_agent`
- `ops_brain`

可选常驻角色：

- `monitor`
- `production_brain`
- `similarity_brain`
- `audit_brain`

常驻 brain 可以保留 lane 判断，但跨 brain 请求必须通过 mailbox。main-agent 不能直接生产知识卡。

### 短期驻留

短期驻留角色可以围绕一个失败簇连续工作，但必须在任务结束后交付总结。

当前短期驻留角色：

- `skill_evolution_worker`
- `trajectory_reflector`，未来需要时再新增

### 阅后即焚

阅后即焚角色只处理一个任务包。完成后关闭，不带着上下文进入下一轮。

当前阅后即焚角色：

- `source_mining_worker`
- `card_drafting_worker`
- `card_audit_worker`
- `card_adoption_worker`
- `independent_evaluator`

## 为什么大多数执行者阅后即焚

scoped knowledge cards 仍然需要强 provenance。普通执行者保留太多历史上下文，反而容易把旧判断、主题结构和父聊天内容混进新卡。

阅后即焚让每张卡都重新从任务包和来源证据出发。

brain-agent 的长期上下文只用于 lane 控制、队列判断和流程记忆，不替代具体 task worker 的来源边界。

## 生命周期记录

每次派发执行者时，dispatch 记录应包含：

```text
agent_id
role
lifecycle: resident | short_lived | disposable
fork_context: false
task_path
allowed_inputs
allowed_writes
started_at
closed_at
```

## 关闭条件

执行者必须在以下条件满足后关闭：

- 写出 `loop_status.md`。
- 写出 `loop_delivery.md`。
- 写出 `read_log.md`。
- 产物路径存在，或明确 `LOOP_BLOCKED`。

## 例外

如果执行者连续失败，不能让同一个执行者无限修改自己。主控 agent 应创建 `independent_evaluator` 或 `skill_evolution_worker`。
