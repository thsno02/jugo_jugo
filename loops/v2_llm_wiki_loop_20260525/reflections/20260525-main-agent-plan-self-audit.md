# Main-agent 长程执行计划自审计

日期：2026-05-25

审计对象：

- `llm_wiki/loop/plans/main_agent_long_horizon_execution_plan.md`
- `llm_wiki/loop/README.md`
- `llm_wiki/loop/RUNBOOK.md`
- `llm_wiki/loop/loop_state.json`
- `llm_wiki/loop/reports/loop_report.md`
- `~/.codex/skills/agent-loop-runner/SKILL.md`
- `~/.codex/skills/agent-loop-runner/references/long-horizon-loop-patterns.md`

## 审计问题

- 新 main-agent 是否能仅凭磁盘文件恢复并推进 loop？
- 计划是否覆盖 KB、skills、sub-agent prompt、控制面和反思链路的演化？
- 是否把当前 LLM Wiki 的具体规则误写进通用 `agent-loop-runner` skill？
- 是否保留 main-agent 的弹性，同时防止它变成执行者？
- 文件系统职责是否清楚？

## 证据

- 计划的恢复入口明确列出 `loop_state.json`、`loop_manifest.json`、`RUNBOOK.md`、`queues/task_queue.md`、`reports/loop_report.md` 和计划本身。
- 计划把长程工作拆成 KB 生产链路、skills/prompt 演化链路、sub-agent prompt 演化链路和 out-of-loop 反思链路。
- 计划明确 `user-insights/` 不是事实来源，`legacy/` 不是默认恢复入口。
- 计划为反思指定 `llm_wiki/loop/reflections/`，并要求反思给出下一步动作。
- 通用 skill 新增的 reference 使用 generic 名称，如 production lane、evolution lane、reflection lane、component-scale thinking，没有出现 LLM Wiki 专有对象、文件名或事实卡规则。

## 假设

- H1：计划足以让新的 main-agent 启动第一轮 source mining。
- H2：计划不会诱导 main-agent 绕过 worker 去亲自生产 KB。
- H3：通用 skill 更新是跨项目可用的 long-horizon loop pattern，不是当前 case 的硬编码。
- H4：out-of-loop 反思被纳入控制面，但不会污染事实生产。

## 验证

- H1 成立。计划给出选源、创建任务包、渲染 dispatch、派发 worker、验收 delivery 的具体步骤。
- H2 成立。计划多次把 main-agent 限定为调度、验收、决策和干预，不允许亲自读来源抽事实、写卡或采纳。
- H3 成立。skill reference 没有引用 `llm_wiki`、atomic card、中文主语言或本项目路径。
- H4 成立。反思链路只能使用 loop 状态、交付、审计和报告作为材料，不能把反思结论写成知识事实。

## concern

- 计划是主控层文档，尚未经过独立 sub-agent 审计。
- 计划新增 `reflections/` 目录职责，但当前 `loop_manifest.json` 尚未把它列为正式目录。
- 下一轮 source mining 仍需主控 agent 手动选择一个具体来源；计划没有替主控 agent 预选来源，以避免再次变成执行者。

## required_changes

- 已将 `plans/` 与 `reflections/` 加入 loop README 和 manifest。
- 后续如果计划在执行中造成歧义，应创建 `skill_evolution_worker` 或 `independent_evaluator` 任务，而不是由 main-agent 临场加长 prompt。

## 结论

```text
self_audit_result: pass_with_concerns
```

可以把当前状态保持为 `READY_FOR_SOURCE_MINING`。下一步应由 main-agent 读取本计划后创建第一轮 `source_mining_worker` 任务包。
