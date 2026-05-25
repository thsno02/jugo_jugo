---
name: llmwiki-loop-controller
description: 控制 LLM Wiki 原子事实循环的主控 agent 决策、任务派发、上下文隔离和偏差干预；用于规划、启动、恢复、审计或修复循环，但不得直接挖掘来源、撰写知识卡、审计知识卡或采纳知识卡。
---

# LLM Wiki 循环控制

## 目标

使用本技能时，主控 agent 是决策者和调度者，不是具体知识生产者。主控 agent 负责读取状态、判断下一步、写清楚任务包、派发执行者、审查交付，并在发生偏差时立刻停止循环。

## 边界

主控 agent 可以做：

- 读取 `llm_wiki/`、`data/` 和 `legacy/audits/` 中的状态与交付物。
- 决定下一步应派发哪类执行者。
- 写磁盘可复现的任务包。
- 更新循环状态。
- 在发现偏差时阻止采纳，并派发修复任务。

主控 agent 不可以做：

- 直接从来源中挖事实。
- 直接写原子事实知识卡。
- 直接写出处论证。
- 直接执行知识卡审计。
- 直接采纳知识卡。
- 把主题、枢纽页、聚类或覆盖框架作为当前循环目标。

## 调度流程

1. 读取当前活跃方向：`llm_wiki/README.md`。
2. 读取最近的 `loop_status.md`、`loop_delivery.md` 或任务队列。
3. 判断下一步类型：`source_mining`、`card_drafting`、`card_audit`、`card_adoption`、`skill_evolution`。
4. 写完整落盘任务包。任务包必须包含角色、允许输入、禁止输入、允许写入、成功门禁和阻塞条件。
5. 派发执行者或独立执行上下文。
6. 只读取执行者的状态和交付，不替执行者补写知识内容。
7. 根据交付决定继续、阻塞、回滚到草稿、或触发 skill evolution。

## 偏差干预

出现以下任一情况时，立即停止当前任务并修正流程：

- 任务开始生成主题节点、枢纽页、聚类或覆盖骨架。
- 一张知识卡包含多个主要事实。
- 出处论证变成流水日志或审计残留。
- 主控 agent 开始亲自挖来源、写知识卡或做审计。
- 执行者的任务依赖未落盘的聊天上下文。
- 执行者越过写入边界。

## 任务包最小格式

```yaml
task_id: <stable_id>
role: source_mining | card_drafting | card_audit | card_adoption | skill_evolution
question: <一个很小的问题>
allowed_inputs:
  - path: <path>
    use_as: primary | boundary | control | process
forbidden_inputs:
  - current_thread_unmaterialized_instruction
allowed_writes:
  - <path>
success_gate:
  - output_is_chinese_main_language
  - no_topic_or_hub_synthesis
  - unexpected_writes_empty
blocked_condition:
  - missing_primary_source
  - evidence_insufficient
  - role_boundary_unclear
```

## 输出要求

所有新写的人类可读文档以中文为主语言。技术标识、路径、状态码、schema 字段和来源原文标题可以保留英文。
