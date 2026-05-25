# 焦点漂移审计任务

`status`: `LOOP_DONE`
`decision`: `focus_drift_root_cause_identified`

## 目标

审计旧版 LLM Wiki 循环为什么从预期的“自下而上、来源支撑、原子事实知识卡生产”，漂移成“自上而下、主题/枢纽骨架生产”。

## 范围纪律

本审计只使用旧版 v1 的一手文件证据：协议、控制面、技能、执行者输入输出、运行任务包，以及若干已产出的 `versions/1.0/card.md`。它不依赖当前聊天上下文，不先读取已有审计结论，也不再派发 sub-agent。

## 避免的输入

- 不读取已有结论型审计报告作为证据。
- 不把主控 agent 对失败原因的解释当作结论。
- 不把用户当前纠偏意见当作证据，只把它作为审计问题的来源。

## 输出

- `evidence_log.md`
- `drift_timeline.md`
- `hypotheses.md`
- `hypothesis_validation.md`
- `root_cause_analysis.md`
- `recommendations_for_atomic_fact_loop.md`
- `loop_status.md`
- `loop_delivery.md`

