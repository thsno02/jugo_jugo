# 受限 main-agent 的弹性

主控 agent 必须被限制，否则它会把自己变成执行者；但它也不能被限制到无法自治。

本文件定义主控 agent 可以动什么、不能动什么，以及如何在不破坏上下文隔离的情况下保持弹性。

## 主控 agent 可以做

- 读取恢复入口。
- 更新 `loop_state.json`。
- 更新 `reports/loop_report.md`。
- 维护 `queues/task_queue.md`。
- 创建任务包。
- 调用 `tools/` 中的机械脚本。
- 派发预定义执行者。
- 检查执行者交付。
- 创建独立审计任务。
- 创建技能演化任务。
- 在证据充分时修改 system prompt、任务模板或 manifest。

## 主控 agent 不可以做

- 亲自阅读一个来源并抽取事实候选。
- 亲自把事实候选写成知识卡。
- 亲自审计知识卡并采纳。
- 通过临时 prompt 让执行者绕过 `SUBAGENT_SCOPE.md`。
- 用父聊天上下文补足来源证据。
- 通过批量脚本绕过出处论证和审计。

## 弹性机制

### 1. 机械脚本

机械脚本让主控 agent 少写 prompt：

- `tools/create_task.py`：生成任务包。
- `tools/render_dispatch.py`：组合 system prompt 和任务包，生成 dispatch payload。
- `tools/validate_scope.py`：检查任务包是否有必要边界。
- `tools/inspect_delivery.py`：检查执行者是否交付必要文件。

### 2. 技能演化

如果执行者失败不是偶发，而是流程或 prompt 问题，主控 agent 创建 `skill_evolution_worker` 任务。

技能演化只能基于失败证据，不能凭空扩张流程。

### 3. 独立审计

如果主控 agent 怀疑自己或执行者 drift，就创建 `independent_evaluator` 任务。

独立审计结论不自动改变状态，必须由主控 agent 写决策记录。

### 4. 暂停与搁置

如果公司网络、工具能力或 auth 状态阻塞，主控 agent 记录阻塞并选择下一个本地可做任务。

不要在网络 retrieve 上过度突破。

## 判定原则

主控 agent 的弹性只用于维护循环，不用于替代执行者生产知识。
