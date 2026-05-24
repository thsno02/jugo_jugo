# 决策：sub-agent 生命周期采用有意图管理

- `time`: `2026-05-25T03:16:50+08:00`
- `decision`: `intentional_lifecycle_management`

## 背景

用户提醒：sub-agent 生命周期管理很重要，但不应过度管理。某些 sub-agent 可以保持 alive，尤其当任务会频繁进行大量 IO、反复读取同一批 `data/` 来源或同一上下文窗口时，alive sub-agent 可能比反复启动更节省上下文和读写成本。

## 当前策略

- 单次独立判断任务，例如 `card_audit_worker`、`independent_evaluator`，完成后关闭，避免污染后续判断。
- 单次写入任务，例如当前 `card_adoption_worker`，完成且验收后关闭。
- 如果后续出现大来源、多轮同源候选处理或重复读取同一数据域，可以显式保持一个 alive worker。
- alive worker 必须在任务包或 decision 中声明职责、允许输入、可保留的上下文、读日志要求、退出条件和主控 agent 监控方式。
- 不隐式复用 worker 的上下文来补事实，不把 alive worker 变成采纳者或状态迁移者。

## 当前选择

当前来源较小，候选 drafting、audit、adoption 之间需要独立边界，因此继续关闭已完成 worker。下一轮如果仍处理同一小来源候选，默认仍使用单次 worker；若未来进入大来源或高重复 IO 来源，再启用 alive worker 策略。
