# 预定义 sub-agent 的演化机制

预定义 sub-agent 不是固定不变的。它们可以被修改，也可以新增，但必须通过证据驱动的演化流程。

## 为什么需要演化

初始角色不可能覆盖所有失败情形。

可能出现：

- `source_mining_worker` 抽出的事实候选太粗。
- `card_drafting_worker` 把卡写成流程日志。
- `card_audit_worker` 对出处论证要求不稳定。
- `card_adoption_worker` 的索引策略不够清楚。
- `independent_evaluator` 过度依赖已有报告。
- `monitor` 状态判断太粗。

这些都应该通过演化解决，而不是让 main-agent 临场写长 prompt 补洞。

## 可演化对象

- `system_prompts/<role>.md`
- `task_templates/<role>_task.md`
- `loop_manifest.json`
- `SUBAGENT_SCOPE.md`
- `RUNBOOK.md`
- `tools/` 中的机械检查脚本

## 演化流程

```text
失败证据
-> 主控 agent 写 skill_evolution_worker 任务包
-> skill_evolution_worker 提出最小修改
-> validate_scope.py / 相关检查通过
-> independent_evaluator 审计
-> 主控 agent 写 decisions/
-> 更新 loop_state.json 和 loop_report.md
```

## 新增 sub-agent 条件

只有满足以下条件，才能新增 sub-agent：

- 现有角色无法表达这个任务。
- 新角色的允许输入、禁止输入、允许写入和成功门禁可以写清楚。
- 新角色不会承担主控 agent 的状态迁移、采纳决策或停止逻辑。
- 新角色不会把当前 loop 从原子事实卡生产带偏到枢纽页、聚类或主题覆盖。

## 修改 sub-agent 条件

修改已有 sub-agent 必须说明：

- 哪个失败触发修改。
- 修改了哪条规则。
- 修改会防止什么错误。
- 是否增加了权限。
- 是否需要独立审计。

## 禁止事项

- 不允许 main-agent 临场发明无边界 sub-agent。
- 不允许用“更强模型”替代边界设计。
- 不允许把父聊天上下文注入执行者作为默认做法。
- 不允许新增能够直接采纳知识卡的审计者。
