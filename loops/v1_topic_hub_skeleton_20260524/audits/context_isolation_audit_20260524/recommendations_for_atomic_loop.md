# 原子事实循环的隔离建议

`status`: `LOOP_DONE`

## 目标

下一版原子事实循环要让每个执行者收到最小、可复放、可审计的任务包，并返回机器可检查的输出。执行者不应继承 parent chat 的隐含结论，也不应越过自己的写入边界。

## 最小任务包

每个执行者都必须有完整落盘的任务包。不要再用 `task_packet:: user/controller instruction in current thread` 作为权威任务。

建议结构：

```yaml
schema: kb.atomic_worker_task.v1
task_id: <stable_id>
role: source_mining | card_drafting | provenance_check | adoption_view | audit
question: <一个很小的事实问题>
allowed_inputs:
  primary:
    - path: <source_path>
      reason: <为什么可用作证据>
  boundary_only:
    - path: <prior_card_or_status>
      reason: <只能用于边界，不能作为事实支持>
forbidden_inputs:
  - current_thread_unmaterialized_instructions
  - prior_audit_conclusions
allowed_writes:
  - <run_local_path>
forbidden_writes:
  - generated/
  - kb/
  - root_node_metadata
success_gate:
  - all_inputs_actually_read_recorded
  - claims_split_into_accepted_rejected_deferred
  - unexpected_writes_empty
```

## 上下文泄漏控制

- 执行者必须记录 `inputs_actually_read`，每条包含 `path`、`reason`、`use_as`。
- `use_as` 只允许 `primary`、`process`、`boundary`、`control`。
- 旧 KB、状态摘要和任务历史可以用于理解边界，不能直接当作新事实的支持。
- 执行者必须输出 `claims_accepted`、`claims_rejected`、`claims_deferred`，让审计者看到它如何独立评估证据。
- 控制器不要在任务包中预写最终叙事。可以给问题，不要给答案。

## 输入输出边界控制

- 每个角色有自己的命令 allowlist。审计角色不得运行会写 `generated/`、`kb/`、root `node.yaml`、边界文件或技能文件的脚本。
- 长任务前必须先写 `task.md`、初始 `loop_status.md` 和 `preflight_io_boundary.md`。
- 所有执行者都要记录 `unexpected_writes`。如果非空，默认以 `LOOP_BLOCKED` 结束，除非任务包明确授权恢复。
- 会写入全局状态的操作只允许采纳/视图角色执行。

## 执行者输出契约

所有 `loop_delivery.md` 至少包含：

```yaml
status: LOOP_DONE | LOOP_BLOCKED
executor_role: worker_executor
role: <role>
inputs_actually_read:
  - path: <path>
    use_as: primary | process | boundary | control
allowed_writes:
  - <path>
writes_performed:
  - <path>
unexpected_writes: []
decision: accepted | rejected | deferred | blocked
```

来源挖掘执行者额外输出：

```yaml
fact_candidates:
  - statement: <one atomic statement>
    support_path: <path>
    support_span_or_section: <locator>
    fact_type_candidate: known_fact | accepted_fact
    scope: <scope>
```

知识卡草稿执行者额外输出：

```yaml
card_path: <path>
provenance_path: <path>
status: draft
```

审计执行者额外输出：

```yaml
audit_decision: pass | fail | needs_revision
blocked_reason: <reason_if_any>
```

采纳/视图执行者额外输出：

```yaml
adopted_cards:
  - <card_id>
generated_outputs_refreshed:
  - <path>
```

## 主 Agent 边界

主控 agent 只负责：

- 读执行者状态和交付。
- 决定下一步派发哪个执行者。
- 更新控制面状态。
- 在发现偏差时阻止采纳。

主控 agent 不负责：

- 具体来源挖掘。
- 写知识卡。
- 写出处论证。
- 执行审计。
- 刷新生成视图。
- 直接修改技能契约，除非任务就是流程修复且已显式授权。

任何控制器写出的具体知识产物都应自动标记为 `controller_drift_sample`，并阻止进入正式 KB，直到有执行者重跑或独立复核。

## 原子事实单元

下一版循环的最小工作单元是一个原子事实候选，而不是主题、枢纽页或节点。一个执行者不应同时完成挖掘、规划、生成、审计、采纳和技能修订。需要多个角色时，先拆任务再派发。

## 停止条件

使用 `LOOP_BLOCKED` 的情况：

- 任务包依赖未落盘的聊天上下文。
- 需要读取的主来源不存在或不可访问。
- 只读执行者需要运行会写入的校验器。
- 发现 `unexpected_writes`。
- 证据不足以支持事实陈述。

只有在所有必要输出存在、没有越权写入、执行者决策能从磁盘复现时，才使用 `LOOP_DONE`。

