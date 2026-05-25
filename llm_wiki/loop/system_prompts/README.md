# 预定义 system prompt

这里保存主控 agent 和执行者的稳定 system prompt。

设计原则：

- system prompt 固定角色身份、边界和禁止事项。
- `task.md` 只提供本轮变量。
- `task.md` 只能收窄权限，不能放宽 system prompt。
- 主控 agent 负责选择角色、填任务包、派发、验收和状态迁移。
- 执行者负责完成窄任务，并把状态、读写和交付写回磁盘。

## 组合方式

执行者 prompt 由两部分组成：

```text
system prompt = base_worker.md + <role>.md
task input = 当前 iteration/task.md
```

主控 agent 使用：

```text
system prompt = main_agent.md
runtime inputs = README + loop_state.json + loop_manifest.json + task_queue.md + loop_report.md
```

## 文件说明

- `main_agent.md`：主控 agent 的稳定边界。
- `base_worker.md`：所有执行者共享的基础边界。
- `source_mining_worker.md`：来源挖掘执行者。
- `card_drafting_worker.md`：知识卡草稿执行者。
- `card_batch_drafting_worker.md`：批量知识卡草稿执行者。
- `card_similarity_gate_worker.md`：知识卡相似门执行者。
- `card_audit_worker.md`：知识卡审计执行者。
- `card_batch_audit_worker.md`：批量知识卡审计执行者。
- `card_adoption_worker.md`：知识卡采纳执行者。
- `card_batch_adoption_worker.md`：批量知识卡采纳执行者。
- `skill_evolution_worker.md`：技能演化执行者。
- `independent_evaluator.md`：独立审计执行者。
- `monitor.md`：低噪声状态监控者。
